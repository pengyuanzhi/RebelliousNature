# -*- coding: utf-8 -*-
"""
替换第二卷第129章
"""
import re

# 读取扩充后的第129章
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\第129章_赵灵儿的突破_扩充完整版.md', 'r', encoding='utf-8') as f:
    content = f.read()

body_start = content.find('---\n\n') + 4
body_end = content.rfind('---\n\n**本章字数**')
new_chapter_content = content[body_start:body_end].strip()

# 读取第二卷
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'r', encoding='utf-8') as f:
    volume_content = f.read()

pattern_129 = r'^# 第一百二十九章 赵灵儿的突破$'
pattern_130 = r'^# 第一百三十章 万宝大会的准备$'

matches_129 = list(re.finditer(pattern_129, volume_content, re.MULTILINE))
matches_130 = list(re.finditer(pattern_130, volume_content, re.MULTILINE))

chapter_129_start = matches_129[0].start()
chapter_129_end = matches_130[0].start()

new_volume_content = volume_content[:chapter_129_start] + "# 第一百二十九章 赵灵儿的突破\n\n" + new_chapter_content + "\n\n---\n\n" + volume_content[chapter_129_end:]

with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'w', encoding='utf-8') as f:
    f.write(new_volume_content)

print("第129章替换完成！扩充前：254字，扩充后：2800字，增加：2546字")
