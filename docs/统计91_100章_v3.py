# -*- coding: utf-8 -*-
"""
快速统计第91-100章字数（使用行号）
"""
import re

file_path = r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 第91-100章的起始行号（从grep结果获得）
chapter_starts = {
    91: 4844,
    92: 4962,
    93: 5050,
    94: 5160,
    95: 5248,
    96: 5344,
    97: 5456,
    98: 5554,
    99: 5686,
    100: 5760
}

# 找第101章的起始
for i, line in enumerate(lines):
    if '# 第一百零一章' in line or '# 第101章' in line:
        chapter_starts[101] = i
        break

print('='*60)
print('第91-100章字数快速统计')
print('='*60)

chapters_info = []

for num in range(91, 101):
    start = chapter_starts.get(num)
    if start is None:
        continue

    # 找下一章的起始
    if num < 100:
        end = chapter_starts.get(num + 1)
        if end is None:
            continue
    else:
        # 第100章后找第101章
        if 101 in chapter_starts:
            end = chapter_starts[101]
        else:
            end = len(lines)

    # 提取正文（去除标题行）
    content_lines = []
    for i in range(start + 2, end):  # 跳过标题行和空行
        line = lines[i].strip()
        if line and not line.startswith('#') and not line.startswith('**') and not line.startswith('---'):
            content_lines.append(lines[i])

    content = ''.join(content_lines)
    char_count = len(content)

    if 2500 <= char_count <= 3500:
        status = "[OK]"
    elif char_count < 2500:
        status = "[SHORT]"
    else:
        status = "[LONG]"

    title = lines[start + 1].split(':', 1)[1].strip() if ':' in lines[start + 1] else lines[start].split(':', 1)[1].strip() if ':' in lines[start] else ''

    chapters_info.append({
        'num': num,
        'title': title[:20],
        'chars': char_count,
        'status': status
    })

    print(f"第{num}章 {title[:15]}: {char_count}字 {status}")

# 统计
qualified = sum(1 for ch in chapters_info if 2500 <= ch['chars'] <= 3500)
need_expand = sum(1 for ch in chapters_info if ch['chars'] < 2500)
too_long = sum(1 for ch in chapters_info if ch['chars'] > 3500)

print(f'\n符合标准（2500-3500字）: {qualified}/10章')
print(f'需要扩充（<2500字）: {need_expand}/10章')
print(f'需要压缩（>3500字）: {too_long}/10章')

if need_expand > 0:
    print(f'\n需要扩充的章节:')
    for ch in chapters_info:
        if ch['chars'] < 2500:
            need = 2800 - ch['chars']
            print(f"  第{ch['num']}章: {ch['chars']}字 → 2800字 (+{need}字)")

if too_long > 0:
    print(f'\n需要压缩的章节:')
    for ch in chapters_info:
        if ch['chars'] > 3500:
            excess = ch['chars'] - 3500
            print(f"  第{ch['num']}章: {ch['chars']}字 → 3500字 (-{excess}字)")
