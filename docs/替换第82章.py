# -*- coding: utf-8 -*-
"""
替换第二卷第82章
"""
import re

# 读取扩充后的第82章（去除标题行）
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\第82章_双修的好处_扩充完整版.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到正文开始位置（第一个"---"之后）
body_start = content.find('---\n\n') + 4
body_end = content.rfind('---\n\n**本章字数**')
new_chapter_content = content[body_start:body_end].strip()

# 读取第二卷
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'r', encoding='utf-8') as f:
    volume_content = f.read()

# 找到第82章的开始和结束位置
pattern_82 = r'^# 第八十二章 双修的好处$'
pattern_83 = r'^# 第八十三章 丹塔的认可$'

matches_82 = list(re.finditer(pattern_82, volume_content, re.MULTILINE))
matches_83 = list(re.finditer(pattern_83, volume_content, re.MULTILINE))

if not matches_82:
    print("未找到第82章")
    exit(1)

chapter_82_start = matches_82[0].start()

if not matches_83:
    print("未找到第83章")
    exit(1)

chapter_82_end = matches_83[0].start()

# 替换内容
new_volume_content = volume_content[:chapter_82_start] + "# 第八十二章 双修的好处\n\n" + new_chapter_content + "\n\n---\n\n" + volume_content[chapter_82_end:]

# 写回文件
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'w', encoding='utf-8') as f:
    f.write(new_volume_content)

print("第82章替换完成！")
print(f"扩充前：约1371字")
print(f"扩充后：约2800字")
print(f"增加：约1429字")
