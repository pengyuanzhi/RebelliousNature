# -*- coding: utf-8 -*-
"""
替换第二卷第84章
"""
import re

# 读取扩充后的第84章（去除标题行）
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\第84章_返回太华宗_扩充完整版.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到正文开始位置（第一个"---"之后）
body_start = content.find('---\n\n') + 4
body_end = content.rfind('---\n\n**本章字数**')
new_chapter_content = content[body_start:body_end].strip()

# 读取第二卷
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'r', encoding='utf-8') as f:
    volume_content = f.read()

# 找到第84章的开始和结束位置
pattern_84 = r'^# 第八十四章 返回太华宗$'
pattern_85 = r'^# 第八十五章 苦海峰$'

matches_84 = list(re.finditer(pattern_84, volume_content, re.MULTILINE))
matches_85 = list(re.finditer(pattern_85, volume_content, re.MULTILINE))

if not matches_84:
    print("未找到第84章")
    exit(1)

chapter_84_start = matches_84[0].start()

if not matches_85:
    print("未找到第85章")
    exit(1)

chapter_84_end = matches_85[0].start()

# 替换内容
new_volume_content = volume_content[:chapter_84_start] + "# 第八十四章 返回太华宗\n\n" + new_chapter_content + "\n\n---\n\n" + volume_content[chapter_84_end:]

# 写回文件
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'w', encoding='utf-8') as f:
    f.write(new_volume_content)

print("第84章替换完成！")
print(f"扩充前：约1008字")
print(f"扩充后：约2800字")
print(f"增加：约1792字")
