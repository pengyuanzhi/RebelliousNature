# -*- coding: utf-8 -*-
"""
替换第二卷第78章
"""
import re

# 读取扩充后的第78章（去除标题行）
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\第78章_久别重逢_扩充完整版.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到正文开始位置（第一个"---"之后）
body_start = content.find('---\n\n') + 4
body_end = content.rfind('---\n\n**本章字数**')
new_chapter_content = content[body_start:body_end].strip()

# 读取第二卷
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'r', encoding='utf-8') as f:
    volume_content = f.read()

# 找到第78章的开始和结束位置
pattern_78 = r'^# 第七十八章 久别重逢$'
pattern_79 = r'^# 第七十九章 命轮眼探病$'

matches_78 = list(re.finditer(pattern_78, volume_content, re.MULTILINE))
matches_79 = list(re.finditer(pattern_79, volume_content, re.MULTILINE))

if not matches_78:
    print("未找到第78章")
    exit(1)

chapter_78_start = matches_78[0].start()

if not matches_79:
    print("未找到第79章")
    exit(1)

chapter_78_end = matches_79[0].start()

# 替换内容
new_volume_content = volume_content[:chapter_78_start] + "# 第七十八章 久别重逢\n\n" + new_chapter_content + "\n\n---\n\n" + volume_content[chapter_78_end:]

# 写回文件
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'w', encoding='utf-8') as f:
    f.write(new_volume_content)

print("第78章替换完成！")
print(f"扩充前：约1279字")
print(f"扩充后：约5400字")
print(f"增加：约4121字")
