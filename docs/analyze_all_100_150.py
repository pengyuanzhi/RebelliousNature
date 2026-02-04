# -*- coding: utf-8 -*-
"""
统计第二卷第100-150章字数 - 最终版本
"""
import re

file_path = r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 查找所有章节标题
chapters = []

# 定义所有要查找的章节标题模式
patterns = [
    r'^# 第一百章\s+(.+)$',
    r'^# 第一百零[一二三四五六七八九]章\s+(.+)$',
    r'^# 第一百一[一二三四五六七八九]章\s+(.+)$',
    r'^# 第一百二[一二三四五六七八九]章\s+(.+)$',
    r'^# 第一百三[一二三四五六七八九]章\s+(.+)$',
    r'^# 第一百四[一二三四五六七八九]章\s+(.+)$',
    r'^# 第一百五十章\s+(.+)$',
]

# 使用组合模式查找所有章节
combined_pattern = '|'.join(patterns)
for match in re.finditer(combined_pattern, content, re.MULTILINE):
    title = match.group(0)
    # 提取章节号
    num_match = re.search(r'第([零一二三四五六七八九十百]+)章', title)
    if num_match:
        num_str = num_match.group(1)
        # 转换中文数字
        num_map = {'零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5,
                   '六': 6, '七': 7, '八': 8, '九': 9, '十': 10, '百': 100}
        # 简化处理：直接查找匹配
        for num in range(100, 151):
            if f'第一百章' in title and num == 100:
                chapters.append({'num': num, 'start': match.start(), 'title': title})
                break
            elif f'第一百零' in title:
                for i in range(1, 10):
                    if f'第一百零{["一","二","三","四","五","六","七","八","九"][i-1]}章' in title and num == 100 + i:
                        chapters.append({'num': num, 'start': match.start(), 'title': title})
                        break
                break
            elif f'第一百一' in title:
                for i in range(0, 10):
                    if i == 0:
                        check = '第一百一十章'
                    else:
                        check = f'第一百一{["一","二","三","四","五","六","七","八","九"][i-1]}章'
                    if check in title and num == 110 + i:
                        chapters.append({'num': num, 'start': match.start(), 'title': title})
                        break
                break
            elif f'第一百二' in title:
                for i in range(0, 10):
                    if i == 0:
                        check = '第一百二十章'
                    else:
                        check = f'第一百二{["一","二","三","四","五","六","七","八","九"][i-1]}章'
                    if check in title and num == 120 + i:
                        chapters.append({'num': num, 'start': match.start(), 'title': title})
                        break
                break
            elif f'第一百三' in title:
                for i in range(0, 10):
                    if i == 0:
                        check = '第一百三十章'
                    else:
                        check = f'第一百三{["一","二","三","四","五","六","七","八","九"][i-1]}章'
                    if check in title and num == 130 + i:
                        chapters.append({'num': num, 'start': match.start(), 'title': title})
                        break
                break
            elif f'第一百四' in title:
                for i in range(0, 10):
                    if i == 0:
                        check = '第一百四十章'
                    else:
                        check = f'第一百四{["一","二","三","四","五","六","七","八","九"][i-1]}章'
                    if check in title and num == 140 + i:
                        chapters.append({'num': num, 'start': match.start(), 'title': title})
                        break
                break
            elif f'第一百五十章' in title and num == 150:
                chapters.append({'num': num, 'start': match.start(), 'title': title})
                break

# 按章节号排序
chapters.sort(key=lambda x: x['num'])

print('='*80)
print('第100-150章字数统计')
print('='*80)
print(f'找到 {len(chapters)} 个章节\n')

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
        'title': chapters[i]['title'],
        'chars': char_count,
        'status': status
    })

    if char_count < 2500:
        need_expand_list.append({
            'num': chapters[i]['num'],
            'title': chapters[i]['title'],
            'chars': char_count
        })

    title_display = chapters[i]['title'][3:23]  # 去掉 "# "，取20字符
    print(f"第{chapters[i]['num']:3d}章 {title_display:25s}: {char_count:5d}字 {status}")

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
        print(f"  第{ch['num']:3d}章 {ch['title'][3:25]:25s}: {ch['chars']:5d}字 → 2800字 (+{need:4d}字)")
