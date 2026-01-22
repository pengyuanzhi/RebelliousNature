# -*- coding: utf-8 -*-
"""
替换第二卷第138章
"""
import re

# 读取扩充后的第138章
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\第138章_大会激战_扩充完整版.md', 'r', encoding='utf-8') as f:
    content = f.read()

body_start = content.find('---\n\n') + 4
body_end = content.rfind('---\n\n**本章字数**')
new_chapter_content = content[body_start:body_end].strip()

# 读取第二卷
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'r', encoding='utf-8') as f:
    volume_content = f.read()

pattern_138 = r'^# 第一百三十八章 大会激战$'
pattern_139 = r'^# 第一百三十九章 万宝大会的收获$'

matches_138 = list(re.finditer(pattern_138, volume_content, re.MULTILINE))
matches_139 = list(re.finditer(pattern_139, volume_content, re.MULTILINE))

chapter_138_start = matches_138[0].start()
chapter_138_end = matches_139[0].start()

new_volume_content = volume_content[:chapter_138_start] + "# 第一百三十八章 大会激战\n\n" + new_chapter_content + "\n\n---\n\n" + volume_content[chapter_138_end:]

with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'w', encoding='utf-8') as f:
    f.write(new_volume_content)

print("第138章替换完成！扩充前：756字，扩充后：2800字，增加：2044字")
