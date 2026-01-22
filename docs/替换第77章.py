# -*- coding: utf-8 -*-
"""
替换第二卷第77章
"""
import re

# 读取扩充后的第77章（去除标题行）
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\第77章_前往青州城_扩充完整版.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到正文开始位置（第一个"---"之后）
body_start = content.find('---\n\n') + 4
body_end = content.rfind('---\n\n**本章字数**')
new_chapter_content = content[body_start:body_end].strip()

# 读取第二卷
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'r', encoding='utf-8') as f:
    volume_content = f.read()

# 找到第77章的开始和结束位置
pattern_77 = r'^# 第七十七章 前往青州城$'
pattern_78 = r'^# 第七十八章 久别重逢$'

matches_77 = list(re.finditer(pattern_77, volume_content, re.MULTILINE))
matches_78 = list(re.finditer(pattern_78, volume_content, re.MULTILINE))

if not matches_77:
    print("未找到第77章")
    exit(1)

chapter_77_start = matches_77[0].start()

if not matches_78:
    print("未找到第78章")
    exit(1)

chapter_77_end = matches_78[0].start()

# 替换内容
new_volume_content = volume_content[:chapter_77_start] + "# 第七十七章 前往青州城\n\n" + new_chapter_content + "\n\n---\n\n" + volume_content[chapter_77_end:]

# 写回文件
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'w', encoding='utf-8') as f:
    f.write(new_volume_content)

print("第77章替换完成！")
print(f"扩充前：约1222字")
print(f"扩充后：约5400字")
print(f"增加：约4178字")
