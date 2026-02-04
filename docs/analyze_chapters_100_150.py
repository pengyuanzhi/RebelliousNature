# -*- coding: utf-8 -*-
"""
统计第二卷第100-150章字数 - 简化版本
"""
import re

file_path = r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 查找所有以# 第...章开头的标题
all_chapters = []
for match in re.finditer(r'^# 第[零一二三四五六七八九十百]+章[^\n]*', content, re.MULTILINE):
    title = match.group(0)
    all_chapters.append({'start': match.start(), 'title': title})

# 找出第100-150章
chinese_nums = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九',
                '十', '百']

def contains_chapter_num(title, num):
    """检查标题是否包含指定章节数"""
    # 将数字转换为中文
    if num == 100:
        return '第一百章' in title
    elif num < 110:
        return f'第一百零{chinese_nums[num-100]}章' in title or f'第一百O{chinese_nums[num-100]}章' in title
    elif num < 120:
        return f'第一百一{chinese_nums[num-110]}章' in title
    elif num < 130:
        return f'第一百二{chinese_nums[num-120]}章' in title
    elif num < 140:
        return f'第一百三{chinese_nums[num-130]}章' in title
    elif num < 150:
        return f'第一百四{chinese_nums[num-140]}章' in title
    elif num == 150:
        return '第一百五十章' in title
    return False

chapters = []
for item in all_chapters:
    for num in range(100, 151):
        if contains_chapter_num(item['title'], num):
            chapters.append({'num': num, 'start': item['start'], 'title': item['title']})
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
        'title': chapters[i]['title'][3:] if 'title' in chapters[i] else '',  # 去掉 "# "
        'chars': char_count,
        'status': status
    })

    if char_count < 2500:
        need_expand_list.append({
            'num': chapters[i]['num'],
            'title': chapters[i]['title'][3:],
            'chars': char_count
        })

    title_display = chapters[i]['title'][3:20] if 'title' in chapters[i] else ''
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
