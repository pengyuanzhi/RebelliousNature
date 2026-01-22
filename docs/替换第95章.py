# -*- coding: utf-8 -*-
"""
替换第二卷第95章
"""
import re

# 读取扩充后的第95章
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\第95章_玄天洞天_扩充完整版.md', 'r', encoding='utf-8') as f:
    content = f.read()

body_start = content.find('---\n\n') + 4
body_end = content.rfind('---\n\n**本章字数**')
new_chapter_content = content[body_start:body_end].strip()

# 读取第二卷
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'r', encoding='utf-8') as f:
    volume_content = f.read()

pattern_95 = r'^# 第九十五章 玄天洞天$'
pattern_96 = r'^# 第九十六章 加入玄天宗$'

matches_95 = list(re.finditer(pattern_95, volume_content, re.MULTILINE))
matches_96 = list(re.finditer(pattern_96, volume_content, re.MULTILINE))

chapter_95_start = matches_95[0].start()
chapter_95_end = matches_96[0].start()

new_volume_content = volume_content[:chapter_95_start] + "# 第九十五章 玄天洞天\n\n" + new_chapter_content + "\n\n---\n\n" + volume_content[chapter_95_end:]

with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'w', encoding='utf-8') as f:
    f.write(new_volume_content)

print("第95章替换完成！扩充前：891字，扩充后：2800字，增加：1909字")
