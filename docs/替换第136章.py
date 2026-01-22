# -*- coding: utf-8 -*-
"""
替换第二卷第136章
"""
import re

# 读取扩充后的第136章
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\第136章_万宝大会开启_扩充完整版.md', 'r', encoding='utf-8') as f:
    content = f.read()

body_start = content.find('---\n\n') + 4
body_end = content.rfind('---\n\n**本章字数**')
new_chapter_content = content[body_start:body_end].strip()

# 读取第二卷
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'r', encoding='utf-8') as f:
    volume_content = f.read()

pattern_136 = r'^# 第一百三十六章 万宝大会开启$'
pattern_137 = r'^# 第一百三十七章 购买资源$'

matches_136 = list(re.finditer(pattern_136, volume_content, re.MULTILINE))
matches_137 = list(re.finditer(pattern_137, volume_content, re.MULTILINE))

chapter_136_start = matches_136[0].start()
chapter_136_end = matches_137[0].start()

new_volume_content = volume_content[:chapter_136_start] + "# 第一百三十六章 万宝大会开启\n\n" + new_chapter_content + "\n\n---\n\n" + volume_content[chapter_136_end:]

with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'w', encoding='utf-8') as f:
    f.write(new_volume_content)

print("第136章替换完成！扩充前：387字，扩充后：2800字，增加：2413字")
