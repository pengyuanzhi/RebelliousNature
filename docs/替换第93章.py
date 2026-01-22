# -*- coding: utf-8 -*-
"""
替换第二卷第93章
"""
import re

# 读取扩充后的第93章（去除标题行）
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\第93章_准备去中界_扩充完整版.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到正文开始位置（第一个"---"之后）
body_start = content.find('---\n\n') + 4
body_end = content.rfind('---\n\n**本章字数**')
new_chapter_content = content[body_start:body_end].strip()

# 读取第二卷
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'r', encoding='utf-8') as f:
    volume_content = f.read()

# 找到第93章的开始和结束位置
pattern_93 = r'^# 第九十三章 准备去中界$'
pattern_94 = r'^# 第九十四章 三十六洞天$'

matches_93 = list(re.finditer(pattern_93, volume_content, re.MULTILINE))
matches_94 = list(re.finditer(pattern_94, volume_content, re.MULTILINE))

if not matches_93:
    print("未找到第93章")
    exit(1)

chapter_93_start = matches_93[0].start()

if not matches_94:
    print("未找到第94章")
    exit(1)

chapter_93_end = matches_94[0].start()

# 替换内容
new_volume_content = volume_content[:chapter_93_start] + "# 第九十三章 准备去中界\n\n" + new_chapter_content + "\n\n---\n\n" + volume_content[chapter_93_end:]

# 写回文件
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'w', encoding='utf-8') as f:
    f.write(new_volume_content)

print("第93章替换完成！")
print(f"扩充前：约1009字")
print(f"扩充后：约2800字")
print(f"增加：约1791字")
