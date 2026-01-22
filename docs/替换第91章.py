# -*- coding: utf-8 -*-
"""
替换第二卷第91章
"""
import re

# 读取扩充后的第91章（去除标题行）
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\第91章_胜利与发现_扩充完整版.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到正文开始位置（第一个"---"之后）
body_start = content.find('---\n\n') + 4
body_end = content.rfind('---\n\n**本章字数**')
new_chapter_content = content[body_start:body_end].strip()

# 读取第二卷
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'r', encoding='utf-8') as f:
    volume_content = f.read()

# 找到第91章的开始和结束位置
pattern_91 = r'^# 第九十一章 胜利与发现$'
pattern_92 = r'^# 第九十二章 父亲的消息$'

matches_91 = list(re.finditer(pattern_91, volume_content, re.MULTILINE))
matches_92 = list(re.finditer(pattern_92, volume_content, re.MULTILINE))

if not matches_91:
    print("未找到第91章")
    exit(1)

chapter_91_start = matches_91[0].start()

if not matches_92:
    print("未找到第92章")
    exit(1)

chapter_91_end = matches_92[0].start()

# 替换内容
new_volume_content = volume_content[:chapter_91_start] + "# 第九十一章 胜利与发现\n\n" + new_chapter_content + "\n\n---\n\n" + volume_content[chapter_91_end:]

# 写回文件
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'w', encoding='utf-8') as f:
    f.write(new_volume_content)

print("第91章替换完成！")
print(f"扩充前：约1402字")
print(f"扩充后：约2800字")
print(f"增加：约1398字")
