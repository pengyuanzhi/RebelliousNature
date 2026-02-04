# -*- coding: utf-8 -*-
"""
统计第二卷第100-150章字数 - JSON输出
"""
import re
import json

file_path = r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 找到第100-150章
chapters = []

# 第一百章
pattern = re.search(r'^# 第一百章[：:](.+)$', content, re.MULTILINE)
if pattern:
    chapters.append({'num': 100, 'start': pattern.start(), 'title': pattern.group(1).strip()})

# 第一百零一章到第一百零九章
for i in range(101, 110):
    pattern = re.search(rf'^# 第一百零{i-100}章[：:](.+)$', content, re.MULTILINE)
    if pattern:
        chapters.append({'num': i, 'start': pattern.start(), 'title': pattern.group(1).strip()})

# 第一百一十章到一百一十九章
for i in range(110, 120):
    pattern = re.search(rf'^# 第一百一{i-110}章[：:](.+)$', content, re.MULTILINE)
    if pattern:
        chapters.append({'num': i, 'start': pattern.start(), 'title': pattern.group(1).strip()})

# 第一百二十章到一百二十九章
for i in range(120, 130):
    pattern = re.search(rf'^# 第一百二{i-120}章[：:](.+)$', content, re.MULTILINE)
    if pattern:
        chapters.append({'num': i, 'start': pattern.start(), 'title': pattern.group(1).strip()})

# 第一百三十章到一百三十九章
for i in range(130, 140):
    pattern = re.search(rf'^# 第一百三{i-130}章[：:](.+)$', content, re.MULTILINE)
    if pattern:
        chapters.append({'num': i, 'start': pattern.start(), 'title': pattern.group(1).strip()})

# 第一百四十章到一百四十九章
for i in range(140, 150):
    pattern = re.search(rf'^# 第一百四{i-140}章[：:](.+)$', content, re.MULTILINE)
    if pattern:
        chapters.append({'num': i, 'start': pattern.start(), 'title': pattern.group(1).strip()})

# 第一百五十章
pattern = re.search(r'^# 第一百五十章[：:](.+)$', content, re.MULTILINE)
if pattern:
    chapters.append({'num': 150, 'start': pattern.start(), 'title': pattern.group(1).strip()})

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
        status = "OK"
    elif char_count < 2500:
        status = "SHORT"
    else:
        status = "LONG"

    chapters_info.append({
        'num': chapters[i]['num'],
        'title': chapters[i]['title'],
        'chars': char_count,
        'status': status
    })

# 输出JSON
result = {
    'total_chapters': len(chapters_info),
    'qualified': sum(1 for ch in chapters_info if ch['status'] == 'OK'),
    'need_expand': sum(1 for ch in chapters_info if ch['status'] == 'SHORT'),
    'too_long': sum(1 for ch in chapters_info if ch['status'] == 'LONG'),
    'chapters': chapters_info
}

print(json.dumps(result, ensure_ascii=False, indent=2))
