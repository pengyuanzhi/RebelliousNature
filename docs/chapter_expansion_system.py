#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter Expansion System for 《逆命问道》
Expands chapters 100-150 to 2800 words each
"""

import re
import os
import json
from datetime import datetime

class ChapterExpander:
    def __init__(self, source_file):
        self.source_file = source_file
        self.chapters = {}
        self.expansion_metadata = {
            'chapters_to_expand': [
                100, 101, 103, 105, 106, 110, 111, 115, 116, 117, 118, 119, 120,
                122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 134, 135,
                136, 137, 138, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150
            ],
            'target_word_count': 2800
        }

    def read_file(self):
        """Read source file with UTF-8 encoding"""
        try:
            with open(self.source_file, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return None

    def extract_chapter(self, content, chapter_num):
        """Extract a specific chapter from content"""

        # Pattern to match chapter headers
        patterns = [
            rf'# 第{chapter_num}章\s*[^\n]*',
            rf'第{chapter_num}章[^\n]*',
        ]

        chapter_start = -1
        chapter_end = -1

        for pattern in patterns:
            match = re.search(pattern, content)
            if match:
                chapter_start = match.start()
                break

        if chapter_start == -1:
            return None

        # Find the end (next chapter or end of file)
        next_chapter_patterns = [
            rf'# 第{chapter_num + 1}章',
            rf'第{chapter_num + 1}章',
            r'# 第\d+章',
            r'## \u672c\u5377\u5c0f\u7ed3'  # 本卷小结
        ]

        for pattern in next_chapter_patterns:
            match = re.search(pattern, content[chapter_start + 100:])
            if match:
                chapter_end = chapter_start + 100 + match.start()
                break

        if chapter_end == -1:
            chapter_content = content[chapter_start:]
        else:
            chapter_content = content[chapter_start:chapter_end]

        return chapter_content.strip()

    def count_words(self, text):
        """Count Chinese characters and words"""
        # Remove markdown and special characters
        clean_text = re.sub(r'[#*\-\[\](){}]', '', text)
        # Count Chinese characters
        chinese_chars = re.findall(r'[\u4e00-\u9fff]', clean_text)
        return len(chinese_chars)

    def extract_all_chapters(self, start=100, end=150):
        """Extract all chapters in range"""
        content = self.read_file()
        if not content:
            return False

        for chapter_num in range(start, end + 1):
            chapter_content = self.extract_chapter(content, chapter_num)
            if chapter_content:
                word_count = self.count_words(chapter_content)
                self.chapters[chapter_num] = {
                    'content': chapter_content,
                    'word_count': word_count,
                    'needs_expansion': chapter_num in self.expansion_metadata['chapters_to_expand']
                }
                print(f"Chapter {chapter_num}: {word_count} words")

        return True

    def generate_expansion_plan(self, chapter_num):
        """Generate expansion plan for a chapter"""

        if chapter_num not in self.chapters:
            return None

        chapter = self.chapters[chapter_num]
        current_count = chapter['word_count']
        target_count = self.expansion_metadata['target_word_count']
        needed = target_count - current_count

        if needed <= 0:
            return None

        plan = {
            'chapter': chapter_num,
            'current_words': current_count,
            'target_words': target_count,
            'words_needed': needed,
            'expansion_areas': {
                'environment': min(needed // 5, 400),  # 环境描写
                'psychology': min(needed // 5, 400),   # 心理活动
                'dialogue': min(needed // 4, 500),     # 对话细节
                'action': min(needed // 4, 500),       # 动作描写
                'foreshadowing': min(needed // 5, 400) # 伏笔铺垫
            }
        }

        return plan

    def save_original_chapter(self, chapter_num, output_dir):
        """Save original chapter to file"""
        if chapter_num not in self.chapters:
            return False

        os.makedirs(output_dir, exist_ok=True)
        filename = f"第{chapter_num}章_原始内容.md"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(self.chapters[chapter_num]['content'])

        return filepath

    def generate_expansion_report(self):
        """Generate report on chapters needing expansion"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'total_chapters': len(self.chapters),
            'chapters_needing_expansion': [],
            'expansion_summary': {
                'total_words_needed': 0,
                'average_words_needed': 0,
                'max_words_needed': 0,
                'min_words_needed': 0
            }
        }

        words_needed_list = []

        for chapter_num in sorted(self.chapters.keys()):
            chapter = self.chapters[chapter_num]

            if chapter['needs_expansion']:
                plan = self.generate_expansion_plan(chapter_num)
                if plan:
                    report['chapters_needing_expansion'].append(plan)
                    words_needed_list.append(plan['words_needed'])

        if words_needed_list:
            report['expansion_summary']['total_words_needed'] = sum(words_needed_list)
            report['expansion_summary']['average_words_needed'] = sum(words_needed_list) // len(words_needed_list)
            report['expansion_summary']['max_words_needed'] = max(words_needed_list)
            report['expansion_summary']['min_words_needed'] = min(words_needed_list)

        return report

    def save_report(self, report, output_file):
        """Save expansion report to JSON file"""
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)

        print(f"\nReport saved to: {output_file}")
        print(f"Total chapters needing expansion: {len(report['chapters_needing_expansion'])}")
        print(f"Total words needed: {report['expansion_summary']['total_words_needed']}")
        print(f"Average words needed per chapter: {report['expansion_summary']['average_words_needed']}")

def main():
    source_file = r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md'
    output_dir = r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\原始章节'
    report_file = r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\expansion_report.json'

    expander = ChapterExpander(source_file)

    print("Extracting chapters 100-150...")
    if not expander.extract_all_chapters(100, 150):
        print("Failed to extract chapters")
        return

    print(f"\nExtracted {len(expander.chapters)} chapters")

    # Save original chapters
    print("\nSaving original chapters...")
    for chapter_num in sorted(expander.chapters.keys()):
        filepath = expander.save_original_chapter(chapter_num, output_dir)
        if filepath:
            print(f"Saved: {os.path.basename(filepath)}")

    # Generate and save report
    print("\nGenerating expansion report...")
    report = expander.generate_expansion_report()
    expander.save_report(report, report_file)

    print("\nExtraction complete!")

if __name__ == '__main__':
    main()
