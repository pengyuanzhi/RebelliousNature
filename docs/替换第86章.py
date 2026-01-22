# -*- coding: utf-8 -*-
"""
替换第二卷第86章
"""
import re

# 读取扩充后的第86章（去除标题行）
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\第86章_修炼闭关_扩充完整版.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到正文开始位置（第一个"---"之后）
body_start = content.find('---\n\n') + 4
body_end = content.rfind('---\n\n**本章字数**')
new_chapter_content = content[body_start:body_end].strip()

# 读取第二卷
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'r', encoding='utf-8') as f:
    volume_content = f.read()

# 找到第86章的开始和结束位置
pattern_86 = r'^# 第八十六章 修炼闭关$'
pattern_87 = r'^# 第八十七章 出关后的惊喜$'

matches_86 = list(re.finditer(pattern_86, volume_content, re.MULTILINE))
matches_87 = list(re.finditer(pattern_87, volume_content, re.MULTILINE))

if not matches_86:
    print("未找到第86章")
    exit(1)

chapter_86_start = matches_86[0].start()

if not matches_87:
    print("未找到第87章")
    exit(1)

chapter_86_end = matches_87[0].start()

# 替换内容
new_volume_content = volume_content[:chapter_86_start] + "# 第八十六章 修炼闭关\n\n" + new_chapter_content + "\n\n---\n\n" + volume_content[chapter_86_end:]

# 写回文件
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'w', encoding='utf-8') as f:
    f.write(new_volume_content)

print("第86章替换完成！")
print(f"扩充前：约2176字")
print(f"扩充后：约2800字")
print(f"增加：约624字")
