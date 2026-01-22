# -*- coding: utf-8 -*-
"""
快速统计第81-90章字数
"""
import re

file_path = r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 第81-90章的起始行号
chapter_starts = {
    81: 1849,
    82: 1965,
    83: 2089,
    84: 2205,
    85: 2303,
    86: 2418,
    87: 2610,
    88: 2750,
    89: 3006,
    90: None  # 会动态计算
}

# 找第90章的起始
for i, line in enumerate(lines):
    if '# 第九十章' in line and '战斗后的总结' in line:
        chapter_starts[90] = i + 1
        break

print('='*60)
print('第81-90章字数快速统计')
print('='*60)

chapters_info = []

for num in range(81, 91):
    start = chapter_starts.get(num)
    if start is None:
        continue

    # 找下一章的起始
    if num < 90:
        end = chapter_starts.get(num + 1)
        if end is None:
            continue
    else:
        # 第90章后找第91章
        for i in range(start, len(lines)):
            if '# 第九十一章' in lines[i]:
                end = i
                break
        else:
            end = len(lines)

    # 提取正文（去除标题和空行）
    content_lines = []
    for i in range(start + 4, end):  # 跳过标题行
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

    title = lines[start + 1].split(':', 1)[1].strip() if ':' in lines[start + 1] else ''

    chapters_info.append({
        'num': num,
        'title': title,
        'chars': char_count,
        'status': status
    })

    print(f"第{num}章 {title}: {char_count}字 {status}")

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
