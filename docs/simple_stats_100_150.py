# -*- coding: utf-8 -*-
"""
简单统计第二卷第100-150章字数
"""
import re

file_path = r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 查找所有章节标题的位置
chapter_positions = []

for i, line in enumerate(lines):
    stripped = line.strip()
    # 匹配 # 第...章 的格式
    if stripped.startswith('# 第') and '章' in stripped:
        # 检查是否是第100-150章的范围
        if '一百' in stripped and '章' in stripped:
            # 提取章节号
            title = stripped
            chapter_positions.append({'line': i, 'title': title})

print(f'找到 {len(chapter_positions)} 个包含"一百"的章节标题')

# 筛选出第100-150章
chapters = []
for pos in chapter_positions:
    title = pos['title']
    # 手动检查章节号
    num = None
    if '第一百章' in title and '第一百零' not in title and '第一百一' not in title and '第一百二' not in title and '第一百三' not in title and '第一百四' not in title and '第一百五' not in title:
        num = 100
    elif '第一百零一章' in title:
        num = 101
    elif '第一百零二章' in title:
        num = 102
    elif '第一百零三章' in title:
        num = 103
    elif '第一百零四章' in title:
        num = 104
    elif '第一百零五章' in title:
        num = 105
    elif '第一百零六章' in title:
        num = 106
    elif '第一百零七章' in title:
        num = 107
    elif '第一百零八章' in title:
        num = 108
    elif '第一百零九章' in title:
        num = 109
    elif '第一百一十章' in title or '第一百一十章' in title:
        num = 110
    elif '第一百一十一章' in title:
        num = 111
    elif '第一百一十二章' in title:
        num = 112
    elif '第一百一十三章' in title:
        num = 113
    elif '第一百一十四章' in title:
        num = 114
    elif '第一百一十五章' in title:
        num = 115
    elif '第一百一十六章' in title:
        num = 116
    elif '第一百一十七章' in title:
        num = 117
    elif '第一百一十八章' in title:
        num = 118
    elif '第一百一十九章' in title:
        num = 119
    elif '第一百二十章' in title and '第一百二' not in title.replace('第一百二十章', ''):
        num = 120
    elif '第一百二十一章' in title:
        num = 121
    elif '第一百二十二章' in title:
        num = 122
    elif '第一百二十三章' in title:
        num = 123
    elif '第一百二十四章' in title:
        num = 124
    elif '第一百二十五章' in title:
        num = 125
    elif '第一百二十六章' in title:
        num = 126
    elif '第一百二十七章' in title:
        num = 127
    elif '第一百二十八章' in title:
        num = 128
    elif '第一百二十九章' in title:
        num = 129
    elif '第一百三十章' in title and '第一百三' not in title.replace('第一百三十章', ''):
        num = 130
    elif '第一百三十一章' in title:
        num = 131
    elif '第一百三十二章' in title:
        num = 132
    elif '第一百三十三章' in title:
        num = 133
    elif '第一百三十四章' in title:
        num = 134
    elif '第一百三十五章' in title:
        num = 135
    elif '第一百三十六章' in title:
        num = 136
    elif '第一百三十七章' in title:
        num = 137
    elif '第一百三十八章' in title:
        num = 138
    elif '第一百三十九章' in title:
        num = 139
    elif '第一百四十章' in title and '第一百四' not in title.replace('第一百四十章', ''):
        num = 140
    elif '第一百四十一章' in title:
        num = 141
    elif '第一百四十二章' in title:
        num = 142
    elif '第一百四十三章' in title:
        num = 143
    elif '第一百四十四章' in title:
        num = 144
    elif '第一百四十五章' in title:
        num = 145
    elif '第一百四十六章' in title:
        num = 146
    elif '第一百四十七章' in title:
        num = 147
    elif '第一百四十八章' in title:
        num = 148
    elif '第一百四十九章' in title:
        num = 149
    elif '第一百五十章' in title:
        num = 150

    if num is not None and 100 <= num <= 150:
        chapters.append({'num': num, 'line': pos['line'], 'title': title})

# 按章节号排序
chapters.sort(key=lambda x: x['num'])

print('='*80)
print('第100-150章字数统计')
print('='*80)
print(f'找到 {len(chapters)} 个章节\n')

chapters_info = []
need_expand_list = []

for i in range(len(chapters)):
    start_line = chapters[i]['line']
    if i < len(chapters) - 1:
        end_line = chapters[i+1]['line']
    else:
        end_line = len(lines)

    # 提取章节内容
    chapter_lines = lines[start_line:end_line]

    # 去除标题和空行
    content_lines = []
    for line in chapter_lines:
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

    title_display = chapters[i]['title'][3:25]  # 去掉 "# "
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
