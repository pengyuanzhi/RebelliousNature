# -*- coding: utf-8 -*-
"""
替换第二卷第83章
"""
import re

# 读取扩充后的第83章（去除标题行）
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\第83章_丹塔的认可_扩充完整版.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到正文开始位置（第一个"---"之后）
body_start = content.find('---\n\n') + 4
body_end = content.rfind('---\n\n**本章字数**')
new_chapter_content = content[body_start:body_end].strip()

# 读取第二卷
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'r', encoding='utf-8') as f:
    volume_content = f.read()

# 找到第83章的开始和结束位置
pattern_83 = r'^# 第八十三章 丹塔的认可$'
pattern_84 = r'^# 第八十四章 返回太华宗$'

matches_83 = list(re.finditer(pattern_83, volume_content, re.MULTILINE))
matches_84 = list(re.finditer(pattern_84, volume_content, re.MULTILINE))

if not matches_83:
    print("未找到第83章")
    exit(1)

chapter_83_start = matches_83[0].start()

if not matches_84:
    print("未找到第84章")
    exit(1)

chapter_83_end = matches_84[0].start()

# 替换内容
new_volume_content = volume_content[:chapter_83_start] + "# 第八十三章 丹塔的认可\n\n" + new_chapter_content + "\n\n---\n\n" + volume_content[chapter_83_end:]

# 写回文件
with open(r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md', 'w', encoding='utf-8') as f:
    f.write(new_volume_content)

print("第83章替换完成！")
print(f"扩充前：约1341字")
print(f"扩充后：约2800字")
print(f"增加：约1459字")
