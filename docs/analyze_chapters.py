# -*- coding: utf-8 -*-
"""
Analyze chapters 100-150 to find which need expansion
"""
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def chinese_to_num(s):
    """Convert Chinese numbers to integers"""
    mapping = {
        '零': '0', '一': '1', '二': '2', '三': '3', '四': '4',
        '五': '5', '六': '6', '七': '7', '八': '8', '九': '9', '十': '10'
    }
    for k, v in mapping.items():
        s = s.replace(k, v)
    return int(s)

with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all chapter headings
chapter_pattern = r'^# (第一百[零一二三四五六七八九十百]+章 [^\n]+)$'
chapters = []

lines = content.split('\n')
for i, line in enumerate(lines):
    match = re.match(chapter_pattern, line)
    if match:
        try:
            num_match = re.search(r'一百([零一二三四五六七八九十百]+)章', line)
            if num_match:
                chapter_num = 100 + chinese_to_num(num_match.group(1))
                if 100 <= chapter_num <= 150:
                    chapters.append({
                        'title': match.group(1),
                        'line': i,
                        'chapter_num': chapter_num
                    })
        except:
            pass

chapters.sort(key=lambda x: x['chapter_num'])

print(f"Found {len(chapters)} chapters between 100-150\n")

# Calculate word counts for each chapter
needs_expansion = []
for idx, chapter in enumerate(chapters):
    start_line = chapter['line']

    # Find the end of this chapter (start of next chapter or end of volume)
    if idx + 1 < len(chapters):
        end_line = chapters[idx + 1]['line']
    else:
        end_line = len(lines)

    chapter_content = '\n'.join(lines[start_line:end_line])

    # Count Chinese characters
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', chapter_content)
    word_count = len(chinese_chars)

    if word_count < 2800:
        needs_expansion.append(chapter)
        print(f"Chapter {chapter['chapter_num']:3d}: {word_count:4d} chars - NEEDS +{2800-word_count} ({chapter['title']})")
    else:
        print(f"Chapter {chapter['chapter_num']:3d}: {word_count:4d} chars - OK ({chapter['title']})")

print(f"\nTotal chapters needing expansion: {len(needs_expansion)}")
