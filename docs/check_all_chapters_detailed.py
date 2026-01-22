# -*- coding: utf-8 -*-
"""
检查第一卷所有章节的详细字数统计
"""
import re

def check_all_chapters(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 查找所有章节标题
    chapter_pattern = r'^## (第[一二三四五六七八九十百零千]+章[^\n]*)'
    matches = list(re.finditer(chapter_pattern, content, re.MULTILINE))

    results = []

    for i, match in enumerate(matches):
        chapter_title = match.group(1)
        start_pos = match.start()

        # 确定章节结束位置
        if i + 1 < len(matches):
            end_pos = matches[i + 1].start()
        else:
            end_pos = len(content)

        # 提取章节内容
        chapter_content = content[start_pos:end_pos]

        # 统计字数（排除章节标题和分隔线）
        lines = chapter_content.split('\n')
        word_count = 0
        for line in lines[1:]:  # 跳过标题行
            # 排除分隔线和元数据行
            if line.strip() and not line.strip().startswith('---') and not line.strip().startswith('*本章字数'):
                word_count += len(line.strip())

        # 检查是否有字数标记
        word_count_match = re.search(r'\*\*本章字数[：:](\d+)字\*\*', chapter_content)
        if word_count_match:
            marked_count = int(word_count_match.group(1))
            word_count = max(word_count, marked_count)  # 使用标记的字数

        results.append({
            'title': chapter_title,
            'word_count': word_count,
            'start': start_pos,
            'end': end_pos
        })

    # 输出结果
    print("=" * 100)
    print(" " * 35 + "第一卷所有章节字数统计")
    print("=" * 100)
    print(f"\n总章节数: {len(results)}章\n")

    # 按目标分类
    targets = {
        '第5章 母亲的葬礼': 5000,
        '第15章 父亲的信': 4000,
        '第22章 雨夜送茶': 5000,
        '第26章 废藏经阁的秘密': 4500,
        '第27章 苦海经的奥义': 5000,
        '第38章 命轮眼的成长': 4500,
        '第39章 苦战王莽': 5000,
        '第40章 外门第一': 5000,
        '第44章 林青云正式收徒': 4500,
        '第52章 命轮眼的秘密': 5000,
        '第53章 决战王莽': 6000,
        '第64章 救下少女': 5000,
        '第65章 寻找父亲': 6000,
        '第66章 安葬父亲': 7000,
        '第73章 凝聚金丹': 7000,
        '第74章 金丹期初期': 6000,
    }

    # 统计
    completed = 0
    total_words = 0

    for result in results:
        total_words += result['word_count']

        # 检查是否达到目标
        target = targets.get(result['title'].split(' ', 1)[1] if ' ' in result['title'] else result['title'])
        if target and result['word_count'] >= target:
            completed += 1

    print(f"当前总字数: {total_words:,}字")
    print(f"超重点章节完成: {completed}/16章\n")

    # 显示所有章节
    print("章节详情:")
    print("-" * 100)
    for i, result in enumerate(results, 1):
        target = targets.get(result['title'].split(' ', 1)[1] if ' ' in result['title'] else result['title'])
        status = "✓" if target and result['word_count'] >= target else " "
        wc = result['word_count']
        print(f"{i:3d}. {result['title']:<30} {wc:>6}字  {status}")

    print("=" * 100)

if __name__ == "__main__":
    check_all_chapters(r"D:\AI\homework\ClaudeCode\RebelliousNature\第一卷_山坳少年.md")
