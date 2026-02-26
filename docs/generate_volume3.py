# -*- coding: utf-8 -*-
import os

# Read header from backup
backup_path = r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\第三卷_元婴威震_扩充前备份_20260204.md'
output_path = r'D:\AI\homework\ClaudeCode\RebelliousNature\第三卷_元婴威震.md'

with open(backup_path, "r", encoding="utf-8-sig") as f:
    backup = f.read()

# Get header (before chapter 151)
chapter_start = backup.find("# 第一百五十一章")
header = backup[:chapter_start] if chapter_start > 0 else backup

# Now we need to write all chapters
# For now, let's just write the header and a placeholder
with open(output_path, "w", encoding="utf-8") as f:
    f.write(header)
    f.write("
## 二、扩充后的正文内容

")
    f.write("[章节内容将在此生成]
")

print("File initialized with header")
