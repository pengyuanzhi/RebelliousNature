# -*- coding: utf-8 -*-
# Truncate file to first 8716 lines

with open('第二卷_金丹岁月.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Original file has {len(lines)} lines")

# Keep only first 8716 lines (0-indexed: 0-8715)
with open('第二卷_金丹岁月.md', 'w', encoding='utf-8') as f:
    f.writelines(lines[:8716])

print(f"File truncated to 8716 lines successfully")
