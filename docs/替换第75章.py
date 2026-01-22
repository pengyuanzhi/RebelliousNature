# -*- coding: utf-8 -*-
"""
替换第二卷第75章
"""
import re

# 读取第二卷
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 读取扩充后的第75章
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\第75章扩充版_金丹的稳固.md', 'r', encoding='utf-8') as f:
    new_chapter = f.read()

# 去掉标题行（第一行）
new_chapter_lines = new_chapter.split('\n')
new_chapter_content = '\n'.join(new_chapter_lines[1:])  # 跳过第一行标题

# 找到第75章的开始和结束位置
pattern = r'^# 第七十五章 金丹的稳固$'
matches = list(re.finditer(pattern, content, re.MULTILINE))

if not matches:
    print("未找到第75章")
    exit(1)

chapter_start = matches[0].start()

# 找到下一章的开始位置（第76章）
next_chapter_pattern = r'^# 第七十六章 命轮眼的突破$'
next_matches = list(re.finditer(next_chapter_pattern, content[chapter_start:], re.MULTILINE))

if next_matches:
    chapter_end = chapter_start + next_matches[0].start()
else:
    print("未找到第76章")
    exit(1)

# 替换内容
new_content = content[:chapter_start] + new_chapter_content + '\n\n' + content[chapter_end:]

# 写回文件
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("第75章替换完成！")
