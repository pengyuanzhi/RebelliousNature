# -*- coding: utf-8 -*-
import re

with open(r"D:\AI\homework\ClaudeCode\RebelliousNature\第三卷_元婴威震.md", "r", encoding="utf-8") as f:
    content = f.read()

# 找到正文开始
start_idx = content.find("# 第一百五十一章")
end_idx = content.find("## 第三卷：元婴威震 完")

if start_idx != -1 and end_idx != -1:
    main_content = content[start_idx:end_idx]

    # 分割章节
    chapter_pattern = r"(^# 第一百\d+章[^\n]*\n)"
    chapters = re.split(chapter_pattern, main_content, flags=re.MULTILINE)

    print("=" * 60)
    print("第三卷章节分析")
    print("=" * 60)

    total_chars = 0
    valid_chapters = []

    for i in range(1, len(chapters), 2):
        if i + 1 < len(chapters):
            title = chapters[i].strip()
            body = chapters[i + 1]

            # 去除空格和换行
            body_clean = body.replace(" ", "").replace("\n", "").replace("\r", "")
            char_count = len(body_clean)

            # 提取标注的字数
            stated_match = re.search(r'\*\*本章字数\*\*：约(\d+)字', body)
            stated = stated_match.group(1) if stated_match else "未知"

            if char_count > 100:  # 有效章节
                total_chars += char_count
                valid_chapters.append((title, char_count, stated))
                print(f"{title}")
                print(f"  实际字数: {char_count} | 标注字数: {stated}")
                print()

    print("=" * 60)
    print(f"总章节数: {len(valid_chapters)}")
    print(f"总实际字数: {total_chars:,}")
    print(f"平均每章实际字数: {total_chars // len(valid_chapters) if valid_chapters else 0:,}")
    print("=" * 60)
