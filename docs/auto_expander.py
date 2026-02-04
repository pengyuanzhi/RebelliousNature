#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automatic Chapter Expansion System for 《逆命问道》
Expands chapters 100-150 to 2800 words each
"""

import re
import os
import json
from datetime import datetime

# Chapters that need expansion with target 2800 words
CHAPTERS_TO_EXPAND = [
    (100, 950, 1850),    # Current: 950, Need: +1850
    (101, 2435, 365),    # Current: 2435, Need: +365
    (103, 2462, 338),    # Current: 2462, Need: +338
    (105, 2153, 647),    # Current: 2153, Need: +647
    (106, 1743, 1057),   # Current: 1743, Need: +1057
    (110, 2225, 575),    # Current: 2225, Need: +575
    (111, 1880, 920),    # Current: 1880, Need: +920
    (115, 1970, 830),    # Current: 1970, Need: +830
    (116, 2147, 653),    # Current: 2147, Need: +653
    (117, 1975, 825),    # Current: 1975, Need: +825
    (118, 2023, 777),    # Current: 2023, Need: +777
    (119, 1806, 994),    # Current: 1806, Need: +994
    (120, 1508, 1292),   # Current: 1508, Need: +1292
    (122, 1634, 1166),   # Current: 1634, Need: +1166
    (123, 1212, 1588),   # Current: 1212, Need: +1588
    (124, 1204, 1596),   # Current: 1204, Need: +1596
    (125, 1196, 1604),   # Current: 1196, Need: +1604
    (126, 895, 1905),    # Current: 895, Need: +1905
    (127, 1262, 1538),   # Current: 1262, Need: +1538
    (128, 1965, 835),    # Current: 1965, Need: +835
    (129, 254, 2546),    # Current: 254, Need: +2546 - CRITICAL
    (130, 2055, 745),    # Current: 2055, Need: +745
    (131, 2111, 689),    # Current: 2111, Need: +689
    (132, 1878, 922),    # Current: 1878, Need: +922
    (134, 1463, 1337),   # Current: 1463, Need: +1337
    (135, 375, 2425),    # Current: 375, Need: +2425 - CRITICAL
    (136, 387, 2413),    # Current: 387, Need: +2413 - CRITICAL
    (137, 596, 2204),    # Current: 596, Need: +2204 - CRITICAL
    (138, 756, 2044),    # Current: 756, Need: +2044 - CRITICAL
    (141, 2087, 713),    # Current: 2087, Need: +713
    (142, 1268, 1532),   # Current: 1268, Need: +1532
    (143, 1154, 1646),   # Current: 1154, Need: +1646
    (144, 1272, 1528),   # Current: 1272, Need: +1528
    (145, 1332, 1468),   # Current: 1332, Need: +1468
    (146, 1187, 1613),   # Current: 1187, Need: +1613
    (147, 1249, 1551),   # Current: 1249, Need: +1551
    (148, 1118, 1682),   # Current: 1118, Need: +1682
    (149, 1204, 1596),   # Current: 1204, Need: +1596
    (150, 1441, 1359),   # Current: 1441, Need: +1359
]

TARGET_WORD_COUNT = 2800

def count_chinese_chars(text):
    """Count Chinese characters in text"""
    clean_text = re.sub(r'[#*\-\[\](){}\-_=+<>.,!?;:""'']', '', text)
    clean_text = re.sub(r'\s+', '', clean_text)
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', clean_text)
    return len(chinese_chars)

def extract_chapter_from_file(file_path, chapter_num):
    """Extract a specific chapter from the main file"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the chapter
    pattern_start = rf'第{chapter_num}章[^\n]*'
    pattern_end = rf'第{chapter_num + 1}章'

    match_start = re.search(pattern_start, content)
    if not match_start:
        return None

    start_pos = match_start.start()

    # Find end
    match_end = re.search(pattern_end, content[start_pos + 50:])
    if match_end:
        end_pos = start_pos + 50 + match_end.start()
    else:
        end_pos = len(content)

    chapter_content = content[start_pos:end_pos]

    # Try to get chapter title
    title_match = re.search(r'第(\d+)章[：:：\s]*([^\n]+)', chapter_content)
    title = title_match.group(2) if title_match else f"第{chapter_num}章"

    return {
        'number': chapter_num,
        'title': title.strip(),
        'content': chapter_content.strip()
    }

def expand_chapter_content(chapter_data, words_needed):
    """
    Generate expansion instructions for a chapter

    This creates a detailed plan for expanding the chapter
    """

    expansion_plan = f"""
# 第{chapter_data['number']}章扩充计划

## 原始信息
- 章节：第{chapter_data['number']}章
- 标题：{chapter_data['title']}
- 当前字数：{count_chinese_chars(chapter_data['content'])}
- 目标字数：{TARGET_WORD_COUNT}
- 需要增加：{words_needed}字

## 扩充策略

### 1. 环境描写 (+{words_needed // 5}字)
**扩充要点**：
- 建筑描写：详细刻画建筑外观、内部结构、装饰风格
- 自然景观：山川河流、花草树木、天气变化、光影效果
- 氛围渲染：通过环境烘托人物心境和剧情氛围

**实施方法**：
- 在现有环境描写基础上增加细节
- 加入五感描写（视觉、听觉、嗅觉、触觉、味觉）
- 使用比喻、拟人等修辞手法
- 通过环境变化暗示剧情走向

### 2. 心理活动 (+{words_needed // 5}字)
**扩充要点**：
- 主角内心独白
- 情感变化过程
- 回忆与联想
- 矛盾与抉择

**实施方法**：
- 在关键情节处增加心理描写
- 展现人物的犹豫、坚定、恐惧、喜悦等复杂情绪
- 通过回忆穿插增加深度
- 展现价值观和人格特质

### 3. 对话细节 (+{words_needed // 4}字)
**扩充要点**：
- 增加对话轮次
- 丰富对话内容
- 加入潜台词
- 描写语气神态

**实施方法**：
- 在对话中增加信息量
- 通过对话展现人物性格
- 加入笑谈、调侃等轻松元素
- 增加对话中的停顿、思考

### 4. 动作描写 (+{words_needed // 4}字)
**扩充要点**：
- 修炼细节：功法运转、灵力流动、突破过程
- 战斗过程：招式对决、闪避反击、法宝使用
- 日常互动：举手投足、眼神交流、细微动作

**实施方法**：
- 将"施展剑法"扩展为具体招式
- 详细描写灵力在经脉中的运行
- 增加战斗中的战术思考
- 加入动作的前因后果

### 5. 伏笔铺垫 (+{words_needed // 5}字)
**扩充要点**：
- 前后呼应
- 暗示未来剧情
- 回顾过往经历
- 铺垫后续发展

**实施方法**：
- 在对话中暗示未来事件
- 通过物品或环境埋下伏笔
- 回顾之前的经历，建立联系
- 预示即将到来的变化

## 扩充示例

### 原文
秦寒盘膝坐在洞府的蒲团上，开始修炼。

### 扩充后
秦寒盘膝坐在洞府中央那块由万年寒玉雕琢而成的蒲团上，调整呼吸，让心神逐渐沉静下来。

洞府内，十几颗月光石镶嵌在墙壁上，散发着柔和的光晕，将整个空间照耀得如同白昼。空气中弥漫着浓郁的灵气，这些灵气经过聚灵阵的层层聚集，浓度达到了外界的三倍之多。每深吸一口气，就能感到体内灵力在缓缓增长，如甘霖滋润干涸的土地。

秦寒缓缓闭上双眼，将所有的杂念排出脑海。体内的《苦海经》心法开始缓缓运转，丹田内的金色金丹微微颤动，散发出璀璨的光芒。

这颗金丹只有拇指大小，却蕴含着磅礴的力量。它表面流转着奇异的纹路，那是天地灵气凝聚而成的道韵，每一道纹路都蕴含着玄奥的道理。

秦寒小心翼翼地控制着灵力，让它们沿着经脉缓缓流淌，经过十二正经，最后汇聚到丹田，被金丹慢慢炼化。

## 注意事项
1. 保持原文风格和语调
2. 不改变核心剧情
3. 扩充内容要自然融入
4. 保持人物性格一致
5. 避免重复冗余
"""

    return expansion_plan

def main():
    source_file = r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md'
    output_dir = r'D:\AI\homework\ClaudeCode\RebelliousNature\docs\扩充计划'

    os.makedirs(output_dir, exist_ok=True)

    print("=" * 60)
    print("《逆命问道》章节扩充计划生成系统")
    print("=" * 60)
    print(f"\n总共需要扩充 {len(CHAPTERS_TO_EXPAND)} 个章节\n")

    # Generate expansion plans for all chapters
    summary = {
        'timestamp': datetime.now().isoformat(),
        'total_chapters': len(CHAPTERS_TO_EXPAND),
        'target_word_count': TARGET_WORD_COUNT,
        'total_words_needed': sum(ch[2] for ch in CHAPTERS_TO_EXPAND),
        'chapters': []
    }

    for i, (chapter_num, current_words, words_needed) in enumerate(CHAPTERS_TO_EXPAND, 1):
        print(f"[{i}/{len(CHAPTERS_TO_EXPAND)}] 处理第{chapter_num}章...")

        # Extract chapter
        chapter_data = extract_chapter_from_file(source_file, chapter_num)

        if not chapter_data:
            print(f"  [WARNING] 无法找到第{chapter_num}章")
            continue

        # Generate expansion plan
        plan = expand_chapter_content(chapter_data, words_needed)

        # Save plan
        plan_file = os.path.join(output_dir, f"第{chapter_num}章_扩充计划.md")
        with open(plan_file, 'w', encoding='utf-8') as f:
            f.write(plan)

        # Save original chapter
        original_file = os.path.join(output_dir, f"第{chapter_num}章_原始内容.md")
        with open(original_file, 'w', encoding='utf-8') as f:
            f.write(chapter_data['content'])

        print(f"  [OK] 当前字数: {current_words}")
        print(f"  [OK] 需要增加: {words_needed}字")
        print(f"  [OK] 计划已保存: 第{chapter_num}章_扩充计划.md")
        print()

        summary['chapters'].append({
            'chapter': chapter_num,
            'title': chapter_data['title'],
            'current_words': current_words,
            'words_needed': words_needed,
            'target_words': TARGET_WORD_COUNT
        })

    # Save summary
    summary_file = os.path.join(output_dir, '扩充计划总览.json')
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print("=" * 60)
    print("扩充计划生成完成！")
    print("=" * 60)
    print(f"\n总计:")
    print(f"  - 需扩充章节数: {len(CHAPTERS_TO_EXPAND)}")
    print(f"  - 目标字数: {TARGET_WORD_COUNT}字/章")
    print(f"  - 总共需要增加: {summary['total_words_needed']}字")
    print(f"\n所有计划已保存到: {output_dir}")

if __name__ == '__main__':
    main()
