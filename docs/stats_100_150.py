# -*- coding: utf-8 -*-
"""
统计第二卷第100-150章字数
"""
import re

file_path = r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 找到第100-150章
chapters = []

# 第一百章 (检查是否有冒号或中文冒号)
for pattern_str in [r'^# 第一百章\s+(.+)$', r'^# 第一百章[：:](.+)$']:
    pattern = re.search(pattern_str, content, re.MULTILINE)
    if pattern:
        chapters.append({'num': 100, 'start': pattern.start(), 'title': pattern.group(1).strip()})
        break

# 第一百零一章到第一百零九章
for i in range(101, 110):
    for pattern_str in [rf'^# 第一百零{i-100}章\s+(.+)$', rf'^# 第一百零{i-100}章[：:](.+)$']:
        pattern = re.search(pattern_str, content, re.MULTILINE)
        if pattern:
            chapters.append({'num': i, 'start': pattern.start(), 'title': pattern.group(1).strip()})
            break

# 第一百一十章到一百一十九章
for i in range(110, 120):
    for pattern_str in [rf'^# 第一百一{i-110}章\s+(.+)$', rf'^# 第一百一{i-110}章[：:](.+)$']:
        pattern = re.search(pattern_str, content, re.MULTILINE)
        if pattern:
            chapters.append({'num': i, 'start': pattern.start(), 'title': pattern.group(1).strip()})
            break

# 第一百二十章到一百二十九章
for i in range(120, 130):
    for pattern_str in [rf'^# 第一百二{i-120}章\s+(.+)$', rf'^# 第一百二{i-120}章[：:](.+)$']:
        pattern = re.search(pattern_str, content, re.MULTILINE)
        if pattern:
            chapters.append({'num': i, 'start': pattern.start(), 'title': pattern.group(1).strip()})
            break

# 第一百三十章到一百三十九章
for i in range(130, 140):
    for pattern_str in [rf'^# 第一百三{i-130}章\s+(.+)$', rf'^# 第一百三{i-130}章[：:](.+)$']:
        pattern = re.search(pattern_str, content, re.MULTILINE)
        if pattern:
            chapters.append({'num': i, 'start': pattern.start(), 'title': pattern.group(1).strip()})
            break

# 第一百四十章到一百四十九章
for i in range(140, 150):
    for pattern_str in [rf'^# 第一百四{i-140}章\s+(.+)$', rf'^# 第一百四{i-140}章[：:](.+)$']:
        pattern = re.search(pattern_str, content, re.MULTILINE)
        if pattern:
            chapters.append({'num': i, 'start': pattern.start(), 'title': pattern.group(1).strip()})
            break

# 第一百五十章
for pattern_str in [r'^# 第一百五十章\s+(.+)$', r'^# 第一百五十章[：:](.+)$']:
    pattern = re.search(pattern_str, content, re.MULTILINE)
    if pattern:
        chapters.append({'num': 150, 'start': pattern.start(), 'title': pattern.group(1).strip()})
        break

print('='*80)
print('第100-150章字数统计')
print('='*80)

chapters_info = []
need_expand_list = []

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
        'title': chapters[i]['title'][:20] if 'title' in chapters[i] else '',
        'chars': char_count,
        'status': status
    })

    if char_count < 2500:
        need_expand_list.append({
            'num': chapters[i]['num'],
            'title': chapters[i]['title'],
            'chars': char_count
        })

    title_display = chapters[i]['title'][:15] if 'title' in chapters[i] else ''
    print(f"第{chapters[i]['num']:3d}章 {title_display:20s}: {char_count:5d}字 {status}")

# 统计
qualified = sum(1 for ch in chapters_info if 2500 <= ch['chars'] <= 3500)
need_expand_count = sum(1 for ch in chapters_info if ch['chars'] < 2500)
too_long = sum(1 for ch in chapters_info if ch['chars'] > 3500)

print(f'\n符合标准（2500-3500字）: {qualified}/{len(chapters_info)}章')
print(f'需要扩充（<2500字）: {need_expand_count}/{len(chapters_info)}章')
print(f'需要压缩（>3500字）: {too_long}/{len(chapters_info)}章')

if need_expand_list:
    print(f'\n需要扩充的章节:')
    for ch in need_expand_list:
        need = 2800 - ch['chars']
        print(f"  第{ch['num']:3d}章 {ch['title']:20s}: {ch['chars']:5d}字 → 2800字 (+{need:4d}字)")
