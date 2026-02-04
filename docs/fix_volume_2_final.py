#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 读取文件
with open(r"D:\AI\homework\ClaudeCode\RebelliousNature\docs\第二卷_修复版.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 保留第1-13944行（第1-136章）
result_lines = lines[:13944]

# 处理第138章开始的内容（原第14030行开始），删除第137章，重新编号
for i in range(14030 - 1, len(lines)):
    line = lines[i]

    # 替换章节编号
    if "第一百三十八章" in line and line.startswith("# "):
        line = line.replace("第一百三十八章", "第一百三十七章")
    elif "第一百三十九章" in line and line.startswith("# "):
        line = line.replace("第一百三十九章", "第一百三十八章")
    elif "第一百四十章" in line and line.startswith("# "):
        line = line.replace("第一百四十章", "第一百三十九章")
    elif "第一百四十一章" in line and line.startswith("# "):
        line = line.replace("第一百四十一章", "第一百四十章")
    elif "第一百四十二章" in line and line.startswith("# "):
        line = line.replace("第一百四十二章", "第一百四十一章")
    elif "第一百四十三章" in line and line.startswith("# "):
        line = line.replace("第一百四十三章", "第一百四十二章")
    elif "第一百四十四章" in line and line.startswith("# "):
        line = line.replace("第一百四十四章", "第一百四十三章")
    elif "第一百四十五章" in line and line.startswith("# "):
        line = line.replace("第一百四十五章", "第一百四十四章")
    elif "第一百四十六章" in line and line.startswith("# "):
        line = line.replace("第一百四十六章", "第一百四十四章")
    elif "第一百四十七章" in line and line.startswith("# "):
        line = line.replace("第一百四十七章", "第一百四十四章")
    elif "第二卷完" in line:
        line = line.replace("第一百四十七章 第二卷完", "第一百四十四章 第二卷完")

    result_lines.append(line)

# 写入新文件
with open(r"D:\AI\homework\ClaudeCode\RebelliousNature\docs\第二卷_修复版2.md", "w", encoding="utf-8") as f:
    f.writelines(result_lines)

print("修复完成！")
print(f"原始文件: {len(lines)} 行")
print(f"修复后文件: {len(result_lines)} 行")
