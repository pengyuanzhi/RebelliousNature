# -*- coding: utf-8 -*-
"""
统计第二卷所有章节（第75-150章）字数
"""
import re

file_path = r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 统计所有章节
chapters = []
for i in range(75, 151):
    if i < 81:
        pattern = f'^# 第八{i-70}章'
    elif i < 91:
        pattern = f'^# 第八十{i-80}章[：:]'
    elif i < 100:
        pattern = f'^# 第九十{i-90}章[：:]'
    elif i == 100:
        pattern = '^# 第一百章[：:]'
    elif i < 110:
        pattern = f'^# 第一百零{i-100}章[：:]'
    elif i < 120:
        pattern = f'^# 第一百一{i-110}章[：:]'
    elif i < 130:
        pattern = f'^# 第一百二{i-120}章[：:]'
    elif i < 140:
        pattern = f'^# 第一百三{i-130}章[：:]'
    elif i < 150:
        pattern = f'^# 第一百四{i-140}章[：:]'
    else:
        pattern = '^# 第一百五十章'

    matches = list(re.finditer(pattern, content, re.MULTILINE))
    if matches:
        chapters.append({'num': i, 'start': matches[0].start(), 'title': matches[0].group(0)})

print('='*60)
print('第二卷章节字数统计（第75-150章）')
print('='*60)

chapters_info = []

for i in range(len(chapters)):
    if i < len(chapters) - 1:
        chapter_content = content[chapters[i]['start']:chapters[i+1]['start']]
    else:
        chapter_content = content[chapters[i]['start']:]

    # 去除标题和空行
    lines = chapter_content.split('\n')
    content_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith('#') and not stripped.startswith('**') and not stripped.startswith('---'):
            content_lines.append(line)

    chapter_text = '\n'.join(content_lines)
    char_count = len(chapter_text)

    if 2500 <= char_count <= 3500:
        status = "[OK]"
    elif char_count < 2500:
        status = "[SHORT]"
    else:
        status = "[LONG]"

    chapters_info.append({
        'num': chapters[i]['num'],
        'chars': char_count,
        'status': status
    })

    if chapters[i]['num'] >= 81:
        print(f"第{chapters[i]['num']}章: {char_count}字 {status}")

# 统计第81-150章
qualified = sum(1 for ch in chapters_info if ch['num'] >= 81 and 2500 <= ch['chars'] <= 3500)
need_expand = sum(1 for ch in chapters_info if ch['num'] >= 81 and ch['chars'] < 2500)
too_long = sum(1 for ch in chapters_info if ch['num'] >= 81 and ch['chars'] > 3500)

print(f'\n第81-150章统计:')
print(f'符合标准（2500-3500字）: {qualified}/70章')
print(f'需要扩充（<2500字）: {need_expand}/70章')
print(f'需要压缩（>3500字）: {too_long}/70章')
