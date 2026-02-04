#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# 读取文件
with open("D:\\AI\\homework\\ClaudeCode\\RebelliousNature\\第二卷_金丹岁月.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 保留第1-12954行（第1-129章），删除第12955-13324行（第130-132章）
# 从第13325行开始是第133章，需要重新编号为第130章
result_lines = lines[:12954]  # 保留第1-129章

# 处理第133章开始的内容，重新编号
chapter_offset = 3  # 第133章变成第130章，减去3
for i in range(13325 - 1, len(lines)):  # 从第13325行开始
    line = lines[i]

    # 替换章节编号
    match = re.match(r"^(# 第一百)(三|四|五|六|七|八|九|十)([章零-九十百千]+章)", line)
    if match:
        prefix = match.group(1)
        digit = match.group(2)
        suffix = match.group(3)

        # 提取原章节号并减去3
        old_num_str = digit + suffix.replace("章", "")
        # 映射表
        num_map = {
            "三十三": "三十", "三十四": "三十一", "三十五": "三十二",
            "三十六": "三十三", "三十七": "三十四", "三十八": "三十五",
            "三十九": "三十六", "四十": "三十七", "四十一": "三十八",
            "四十二": "三十九", "四十三": "四十", "四十四": "四十一",
            "四十五": "四十二", "四十六": "四十三", "四十七": "四十四",
            "四十八": "四十五", "四十九": "四十六", "五十": "四十七",
        }

        if old_num_str in num_map:
            new_num_str = num_map[old_num_str]
            line = f"# 第一百{new_num_str}章\n"

    result_lines.append(line)

# 写入新文件
with open("D:\\AI\\homework\\ClaudeCode\\RebelliousNature\\docs\\第二卷_金丹岁月_修复版.md", "w", encoding="utf-8") as f:
    f.writelines(result_lines)

print("修复完成！")
print(f"原始文件: {len(lines)} 行")
print(f"修复后文件: {len(result_lines)} 行")
