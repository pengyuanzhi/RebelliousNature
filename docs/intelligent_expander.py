#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intelligent Chapter Expander
Uses AI to expand chapters intelligently while maintaining quality
"""

import re
import os
from pathlib import Path

# Expansion patterns for different types of content
EXPANSION_PATTERNS = {
    'environment': {
        'keywords': ['洞府', '山峰', '森林', '宫殿', '房间', '天空', '云雾'],
        'templates': [
            "{location}散发着{atmosphere}，{lighting}。",
            "空气中弥漫着{scent}，{sound}。",
            "四周{surroundings}，{distant_view}。",
            "{time}，{weather}。",
            "墙壁上{decoration}，地面{floor}。",
        ]
    },
    'cultivation': {
        'keywords': ['修炼', '灵力', '丹田', '经脉', '突破', '功法'],
        'templates': [
            "{name}调整呼吸，让心境{state}。",
            "体内的{energy}在{meridians}中缓缓流动。",
            "{power}在{location}汇聚，{effect}。",
            "随着{process}，{result}。",
            "{name}能感到{feeling}，{realization}。"
        ]
    },
    'dialogue': {
        'keywords': ['说道', '问道', '回答', '沉默', '思考'],
        'templates': [
            "{name}{tone}地说道：\"{dialogue}\"",
            "他{expression}，{action}。",
            "\"{response}\"，{name}{reaction}。",
            "{name}{emotion}，{action}。",
            "两人{interaction}，{atmosphere}。"
        ]
    },
    'action': {
        'keywords': ['剑', '攻击', '防御', '闪避', '飞', '战'],
        'templates': [
            "{name}{prepare}，然后{action}。",
            "只见{visual}，{effect}。",
            "{weapon}发出{phenomenon}，{power}。",
            "{name}{move}，{result}。",
            "随着{action}，{change}。"
        ]
    },
    'psychology': {
        'keywords': ['心中', '想到', '回忆', '感觉', '明白'],
        'templates': [
            "{name}心中{emotion}，{thought}。",
            "回想起{memory}，{feeling}。",
            "他{realization}，{resolution}。",
            "{emotion}涌上心头，{reaction}。",
            "{name}深吸一口气，{determination}。"
        ]
    }
}

class IntelligentExpander:
    def __init__(self, source_file):
        self.source_file = source_file
        self.content = None
        self.chapters = {}

    def load_source(self):
        """Load the source file"""
        with open(self.source_file, 'r', encoding='utf-8') as f:
            self.content = f.read()
        return True

    def extract_chapter(self, chapter_num):
        """Extract a specific chapter"""
        if not self.content:
            self.load_source()

        # Find chapter
        pattern = rf'第{chapter_num}章[^\n]*\n'
        match = re.search(pattern, self.content)

        if not match:
            return None

        start = match.start()

        # Find next chapter or end
        next_pattern = rf'第{chapter_num + 1}章'
        next_match = re.search(next_pattern, self.content[start + 20:])

        if next_match:
            end = start + 20 + next_match.start()
        else:
            end = len(self.content)

        return self.content[start:end].strip()

    def analyze_chapter(self, chapter_content):
        """Analyze chapter to find expansion points"""
        lines = chapter_content.split('\n')

        analysis = {
            'environment_points': [],
            'dialogue_points': [],
            'action_points': [],
            'cultivation_points': [],
            'psychology_points': []
        }

        for i, line in enumerate(lines):
            for category, patterns in EXPANSION_PATTERNS.items():
                for keyword in patterns['keywords']:
                    if keyword in line:
                        analysis[f'{category}_points'].append({
                            'line_num': i,
                            'line': line,
                            'keyword': keyword
                        })
                        break

        return analysis

    def generate_expansion(self, chapter_num, chapter_content, words_needed):
        """Generate expanded version of chapter"""

        # Analyze chapter
        analysis = self.analyze_chapter(chapter_content)

        # Calculate expansion distribution
        expansions = {
            'environment': words_needed // 5,
            'psychology': words_needed // 5,
            'dialogue': words_needed // 4,
            'action': words_needed // 4,
            'cultivation': words_needed // 20
        }

        # Create expansion report
        report = f"""
# 第{chapter_num}章扩充分析报告

## 当前状态
- 需要增加字数：{words_needed}
- 扩充策略已生成

## 扩充点分析

### 环境描写扩充点 ({len(analysis['environment_points'])}个)
{chr(10).join(f"- 行{i}: {p['line'][:50]}" for i, p in enumerate(analysis['environment_points'][:5]))}
建议增加：{expansions['environment']}字

### 心理活动扩充点 ({len(analysis['psychology_points'])}个)
{chr(10).join(f"- 行{i}: {p['line'][:50]}" for i, p in enumerate(analysis['psychology_points'][:5]))}
建议增加：{expansions['psychology']}字

### 对话细节扩充点 ({len(analysis['dialogue_points'])}个)
{chr(10).join(f"- 行{i}: {p['line'][:50]}" for i, p in enumerate(analysis['dialogue_points'][:5]))}
建议增加：{expansions['dialogue']}字

### 动作描写扩充点 ({len(analysis['action_points'])}个)
{chr(10).join(f"- 行{i}: {p['line'][:50]}" for i, p in enumerate(analysis['action_points'][:5]))}
建议增加：{expansions['action']}字

### 修炼描写扩充点 ({len(analysis['cultivation_points'])}个)
{chr(10).join(f"- 行{i}: {p['line'][:50]}" for i, p in enumerate(analysis['cultivation_points'][:5]))}
建议增加：{expansions['cultivation']}字

## 扩充建议

由于本系统无法直接生成高质量的中文小说内容，
建议使用Claude Code的人工智能功能进行逐章扩充。

扩充时请参考上述扩充点，在相应位置插入扩充内容。
"""

        return report

def main():
    print("Intelligent Chapter Expander")
    print("=" * 60)

    source_file = r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md'
    output_dir = Path(r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\扩充分析')
    output_dir.mkdir(exist_ok=True)

    # Chapters to expand (critical ones first)
    critical_chapters = [
        (129, 2546),
        (135, 2425),
        (136, 2413),
        (137, 2204),
        (138, 2044),
    ]

    expander = IntelligentExpander(source_file)

    for chapter_num, words_needed in critical_chapters:
        print(f"\nAnalyzing chapter {chapter_num}...")

        content = expander.extract_chapter(chapter_num)

        if content:
            report = expander.generate_expansion(chapter_num, content, words_needed)

            report_file = output_dir / f"第{chapter_num}章_扩充分析.md"
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write(report)

            print(f"  -> Report saved: {report_file.name}")
        else:
            print(f"  -> Chapter not found!")

    print("\nDone! Reports generated for critical chapters.")

if __name__ == '__main__':
    main()
