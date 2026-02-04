#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extract chapters 100-150 from 第二卷_金丹岁月.md
"""

import re
import os

def extract_chapters(input_file, start_chapter, end_chapter):
    """Extract specific chapters from the main file"""

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all chapter markers
    chapter_pattern = r'(### 第(\d+)章[^\n]*\n(?:时间[^\n]*\n)?(?:地点[^\n]*\n)?(?:人物[^\n]*\n)?(?:事件[^\n]*\n)?)'

    chapters = {}
    current_chapter = None
    current_content = []
    in_chapter = False

    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if this is a chapter header
        chapter_match = re.match(r'### 第(\d+)章', line)

        if chapter_match:
            # Save previous chapter if exists
            if current_chapter and start_chapter <= current_chapter <= end_chapter:
                chapters[current_chapter] = '\n'.join(current_content)

            # Start new chapter
            current_chapter = int(chapter_match.group(1))
            current_content = [line]
            in_chapter = True

        elif in_chapter:
            current_content.append(line)

        i += 1

    # Don't forget the last chapter
    if current_chapter and start_chapter <= current_chapter <= end_chapter:
        chapters[current_chapter] = '\n'.join(current_content)

    return chapters

def save_individual_chapters(chapters, output_dir):
    """Save each chapter to its own file"""

    os.makedirs(output_dir, exist_ok=True)

    for chapter_num, content in chapters.items():
        filename = f"第{chapter_num}章_原始内容.md"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Saved: {filename}")

if __name__ == '__main__':
    input_file = r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md'
    output_dir = r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\原始章节'

    chapters = extract_chapters(input_file, 100, 150)
    save_individual_chapters(chapters, output_dir)

    print(f"\nExtracted {len(chapters)} chapters")
