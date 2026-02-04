# -*- coding: utf-8 -*-
"""
快速统计第91-100章字数
"""
import re

file_path = r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('='*60)
print('第91-100章字数快速统计')
print('='*60)

# 找到第91-100章的起始位置
chapters = []
for i in range(91, 101):
    pattern = f'^# 第九十一章[：:](.+)$' if i == 91 else f'^# 第九十{i-90}章[：:](.+)$' if i < 100 else f'^# 第一百章[：:](.+)$'

    for line_num, line in enumerate(lines):
        if re.match(pattern, line.strip()):
            chapters.append({'num': i, 'start': line_num, 'title': line.split(':', 1)[1].strip() if ':' in line else ''})
            break

# 统计每章字数
for i in range(len(chapters)):
    if i < len(chapters) - 1:
        end = chapters[i+1]['start']
    else:
        # 第100章后找第101章
        for j in range(chapters[i]['start'], len(lines)):
            if '# 第一百零一章' in lines[j] or '# 第101章' in lines[j]:
                end = j
                break
        else:
            end = len(lines)

    # 提取正文（去除标题和空行）
    content_lines = []
    for j in range(chapters[i]['start'] + 4, end):
        line = lines[j].strip()
        if line and not line.startswith('#') and not line.startswith('**') and not line.startswith('---'):
            content_lines.append(lines[j])

    content = ''.join(content_lines)
    char_count = len(content)

    if 2500 <= char_count <= 3500:
        status = "[OK]"
    elif char_count < 2500:
        status = "[SHORT]"
    else:
        status = "[LONG]"

    chapters[i]['chars'] = char_count
    chapters[i]['status'] = status

    print(f"第{chapters[i]['num']}章 {chapters[i]['title']}: {char_count}字 {status}")

# 统计
qualified = sum(1 for ch in chapters if 2500 <= ch.get('chars', 0) <= 3500)
need_expand = sum(1 for ch in chapters if ch.get('chars', 0) < 2500)
too_long = sum(1 for ch in chapters if ch.get('chars', 0) > 3500)

print(f'\n符合标准（2500-3500字）: {qualified}/10章')
print(f'需要扩充（<2500字）: {need_expand}/10章')
print(f'需要压缩（>3500字）: {too_long}/10章')

if need_expand > 0:
    print(f'\n需要扩充的章节:')
    for ch in chapters:
        if ch.get('chars', 0) < 2500:
            need = 2800 - ch['chars']
            print(f"  第{ch['num']}章: {ch['chars']}字 → 2800字 (+{need}字)")
