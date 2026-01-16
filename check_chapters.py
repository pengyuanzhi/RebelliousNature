#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys

def check_volume(filename, volume_name):
    """检查某卷的章节字数"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ 无法读取文件 {filename}: {e}")
        return

    # 查找正文内容部分
    main_content_start = content.find("## 三、正文内容")
    if main_content_start == -1:
        print(f"❌ {volume_name} - 未找到正文内容部分")
        return

    main_content = content[main_content_start:]

    # 提取所有章节
    # 匹配 ## 第X章 或 ## 第X章：标题
    chapter_pattern = re.compile(r'^##\s+第(\d+)章\s*', re.MULTILINE)

    chapters = []
    matches = list(chapter_pattern.finditer(main_content))

    for i, match in enumerate(matches):
        chapter_num = int(match.group(1))
        chapter_start = match.end()

        # 下一章的开始位置
        if i + 1 < len(matches):
            chapter_end = matches[i + 1].start()
        else:
            chapter_end = len(main_content)

        chapter_content = main_content[chapter_start:chapter_end].strip()
        word_count = len(chapter_content)
        chapters.append((chapter_num, word_count))

    # 统计
    total_chapters = len(chapters)
    short_chapters = [ch for ch in chapters if ch[1] < 1800]
    very_short = [ch for ch in chapters if ch[1] < 1000]

    print(f"\n{'='*60}")
    print(f"📊 {volume_name}")
    print(f"{'='*60}")
    print(f"总章节数：{total_chapters}")
    print(f"少于1800字：{len(short_chapters)}章 ({len(short_chapters)/total_chapters*100:.1f}%)")
    print(f"少于1000字：{len(very_short)}章 ({len(very_short)/total_chapters*100:.1f}%)")

    total_words = sum(ch[1] for ch in chapters)
    print(f"总字数：约{total_words:,}字 ({total_words/10000:.1f}万字)")
    print(f"平均每章：{total_words//total_chapters}字")

    if short_chapters:
        print(f"\n⚠️ 少于1800字的章节（前20个）：")
        for ch in short_chapters[:20]:
            print(f"   第{ch[0]:3d}章：{ch[1]:4d}字 {'❌' if ch[1] < 1000 else '⚠️'}")

    return total_chapters, total_words, len(short_chapters)

# 主函数
if __name__ == '__main__':
    volumes = [
        ("第一卷_山坳少年.md", "第一卷：山坳少年"),
        ("第二卷_金丹岁月.md", "第二卷：金丹岁月"),
        ("第三卷_元婴威震.md", "第三卷：元婴威震"),
        ("第四卷_化神之道.md", "第四卷：化神之道"),
        ("第五卷_合道争锋.md", "第五卷：合道争锋"),
        ("第六卷_天仙之路.md", "第六卷：天仙之路"),
    ]

    print("\n" + "="*60)
    print("《逆命问道》章节字数统计报告")
    print("="*60)

    total_all = 0
    words_all = 0
    short_all = 0

    for filename, name in volumes:
        result = check_volume(filename, name)
        if result:
            total_all += result[0]
            words_all += result[1]
            short_all += result[2]

    print(f"\n{'='*60}")
    print(f"📈 总体统计")
    print(f"{'='*60}")
    print(f"总章节数：{total_all}章")
    print(f"总字数：约{words_all:,}字 ({words_all/10000:.1f}万字)")
    print(f"少于1800字：{short_all}章 ({short_all/total_all*100:.1f}%)")
    print(f"应有字数（按1800字/章）：{total_all*1800:,}字 ({total_all*1800/10000:.1f}万字)")
    print(f"差距：{total_all*1800 - words_all:,}字 ({(total_all*1800 - words_all)/10000:.1f}万字)")
