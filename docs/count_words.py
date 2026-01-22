#!/usr/bin/env python3
import re

with open('第一卷_山坳少年.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到正文开始位置
start_pos = content.find('## 三、正文内容')
if start_pos > 0:
    text_content = content[start_pos:]
    
    # 提取所有章节
    chapter_pattern = r'## (第[0-9]+章[^\n]+)\s*\n(.*?)(?=## 第[0-9]+章|\Z)'
    matches = re.findall(chapter_pattern, text_content, re.DOTALL)
    
    # 统计每个章节字数
    below_1800 = []
    total_chapters = len(matches)
    
    for i, (title, body) in enumerate(matches, 1):
        # 计算正文字数（去掉空行）
        lines = body.strip().split('\n')
        content_lines = [line for line in lines if line.strip() and not line.startswith('##')]
        word_count = sum(len(line) for line in content_lines)
        
        is达标 = word_count >= 1800
        if not is达标:
            below_1800.append((i, title.strip().replace('## ', ''), word_count, 1800 - word_count))
        
        status = "✅ 达标" if is达标 else "⚠️ 不达标"
        shortage = f" (缺少 {1800 - word_count} 字)" if not is达标 else ""
        print(f"第{i}章 {title.strip().replace('## ', '')}: {word_count} 字 {status}{shortage}")
    
    print(f"\n总结:")
    print(f"总章节数: {total_chapters}")
    print(f"达标章节: {total_chapters - len(below_1800)}")
    print(f"不达标章节: {len(below_1800)}")
    print(f"\n不达标章节详情:")
    for num, title, count, shortage in below_1800:
        print(f"  第{num}章 {title}: {count} 字 (缺少 {shortage} 字)")
