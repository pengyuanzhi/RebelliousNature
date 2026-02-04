# -*- coding: utf-8 -*-
"""
快速统计第91-100章字数
"""
import re

file_path = r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 找第91-100章
chapters = []

# 查找第九十一章
pattern_91 = re.search(r'^(# 第九十一章.*?)$', content, re.MULTILINE)
if pattern_91:
    chapters.append({'num': 91, 'start': pattern_91.start(), 'title': pattern_91.group(1)})

# 查找第九十二-九十九章
for i in range(92, 100):
    pattern = re.search(rf'^# 第九十{i-90}章.*?$', content, re.MULTILINE)
    if pattern:
        chapters.append({'num': i, 'start': pattern.start(), 'title': pattern.group(0)})

# 查找第一百章
pattern_100 = re.search(r'^# 第一百章.*?$', content, re.MULTILINE)
if pattern_100:
    chapters.append({'num': 100, 'start': pattern_100.start(), 'title': pattern_100.group(0)})

# 查找第101章作为结束标记
pattern_101 = re.search(r'^# 第一百零一章.*?$', content, re.MULTILINE)

print('='*60)
print('第91-100章字数统计')
print('='*60)

for i in range(len(chapters)):
    if i < len(chapters) - 1:
        chapter_content = content[chapters[i]['start']:chapters[i+1]['start']]
    else:
        if pattern_101:
            chapter_content = content[chapters[i]['start']:pattern_101.start()]
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

    chapters[i]['chars'] = char_count
    chapters[i]['status'] = status

    title_short = chapters[i]['title'].split(':', 1)[1][:15] if ':' in chapters[i]['title'] else chapters[i]['title'][:15]
    print(f"第{chapters[i]['num']}章 {title_short}: {char_count}字 {status}")

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
