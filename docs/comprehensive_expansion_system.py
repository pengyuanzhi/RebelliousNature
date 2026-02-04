#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive Chapter Expansion System for 《逆命问道》第二卷
Automates the expansion of chapters 100-150 to 2800 words each
"""

import re
import os
from pathlib import Path

# Chapter data from user requirements
CHAPTER_DATA = {
    100: {"title": "小九化形", "current": 950, "needed": 1850},
    101: {"title": "", "current": 2435, "needed": 365},
    103: {"title": "", "current": 2462, "needed": 338},
    105: {"title": "", "current": 2153, "needed": 647},
    106: {"title": "", "current": 1743, "needed": 1057},
    110: {"title": "", "current": 2225, "needed": 575},
    111: {"title": "", "current": 1880, "needed": 920},
    115: {"title": "", "current": 1970, "needed": 830},
    116: {"title": "", "current": 2147, "needed": 653},
    117: {"title": "", "current": 1975, "needed": 825},
    118: {"title": "", "current": 2023, "needed": 777},
    119: {"title": "", "current": 1806, "needed": 994},
    120: {"title": "", "current": 1508, "needed": 1292},
    122: {"title": "", "current": 1634, "needed": 1166},
    123: {"title": "", "current": 1212, "needed": 1588},
    124: {"title": "", "current": 1204, "needed": 1596},
    125: {"title": "", "current": 1196, "needed": 1604},
    126: {"title": "", "current": 895, "needed": 1905},
    127: {"title": "", "current": 1262, "needed": 1538},
    128: {"title": "", "current": 1965, "needed": 835},
    129: {"title": "", "current": 254, "needed": 2546},  # CRITICAL
    130: {"title": "", "current": 2055, "needed": 745},
    131: {"title": "", "current": 2111, "needed": 689},
    132: {"title": "", "current": 1878, "needed": 922},
    134: {"title": "", "current": 1463, "needed": 1337},
    135: {"title": "", "current": 375, "needed": 2425},  # CRITICAL
    136: {"title": "", "current": 387, "needed": 2413},  # CRITICAL
    137: {"title": "", "current": 596, "needed": 2204},  # CRITICAL
    138: {"title": "", "current": 756, "needed": 2044},  # CRITICAL
    141: {"title": "", "current": 2087, "needed": 713},
    142: {"title": "", "current": 1268, "needed": 1532},
    143: {"title": "", "current": 1154, "needed": 1646},
    144: {"title": "", "current": 1272, "needed": 1528},
    145: {"title": "", "current": 1332, "needed": 1468},
    146: {"title": "", "current": 1187, "needed": 1613},
    147: {"title": "", "current": 1249, "needed": 1551},
    148: {"title": "", "current": 1118, "needed": 1682},
    149: {"title": "", "current": 1204, "needed": 1596},
    150: {"title": "", "current": 1441, "needed": 1359},
}

TARGET_WORDS = 2800

def create_expansion_prompt(chapter_num, data):
    """Create a detailed expansion prompt for a chapter"""

    return f"""# 第{chapter_num}章扩充指令

## 目标
- 当前字数：{data['current']}字
- 目标字数：{TARGET_WORDS}字
- 需要增加：{data['needed']}字

## 扩充策略

### 1. 环境描写 (+{data['needed']//5}字)
增加建筑、自然景观、氛围渲染

### 2. 心理活动 (+{data['needed']//5}字)
增加内心活动、情感变化、回忆

### 3. 对话细节 (+{data['needed']//4}字)
增加人物交流、信息传递、情感表达

### 4. 动作描写 (+{data['needed']//4}字)
增加修炼细节、战斗过程、日常互动

### 5. 伏笔铺垫 (+{data['needed']//5}字)
增加伏笔埋设、前后呼应

## 注意事项
- 保持原文风格和语调
- 不改变核心剧情
- 扩充内容要自然融入
- 保持人物性格一致
"""

def main():
    print("=" * 70)
    print("《逆命问道》第二卷章节扩充系统")
    print("=" * 70)

    # Create output directories
    base_dir = Path(r'D:\AI\homework\ClaudeCode\RebelliousNature\docs')
    plans_dir = base_dir / '扩充计划'
    expanded_dir = base_dir / '扩充版本'

    plans_dir.mkdir(exist_ok=True)
    expanded_dir.mkdir(exist_ok=True)

    print(f"\n待扩充章节数: {len(CHAPTER_DATA)}")
    print(f"目标字数: {TARGET_WORDS}字/章")
    print(f"总共需要增加: {sum(d['needed'] for d in CHAPTER_DATA.values())}字")
    print()

    # Generate expansion plans for all chapters
    for i, (chapter_num, data) in enumerate(sorted(CHAPTER_DATA.items()), 1):
        print(f"[{i}/{len(CHAPTER_DATA)}] 第{chapter_num}章: {data['current']}→{TARGET_WORDS} (+{data['needed']})")

        # Create expansion plan
        plan = create_expansion_prompt(chapter_num, data)
        plan_file = plans_dir / f"第{chapter_num}章_扩充指令.txt"

        with open(plan_file, 'w', encoding='utf-8') as f:
            f.write(plan)

    print("\n扩充指令已生成完毕!")
    print(f"保存位置: {plans_dir}")
    print("\n下一步：逐章进行扩充")

    # Create master plan
    master_plan = f"""# 《逆命问道》第二卷扩充总计划

## 概览
- 待扩充章节：{len(CHAPTER_DATA)}章
- 目标字数：{TARGET_WORDS}字/章
- 总需增加：{sum(d['needed'] for d in CHAPTER_DATA.values()):,}字

## 优先级分类

### CRITICAL（急需扩充，需+2000字以上）
{chr(10).join(f"- 第{ch}章: {data['current']}→{TARGET_WORDS} (+{data['needed']})"
              for ch, data in CHAPTER_DATA.items() if data['needed'] >= 2000)}

### HIGH（急需扩充，需+1500-1999字）
{chr(10).join(f"- 第{ch}章: {data['current']}→{TARGET_WORDS} (+{data['needed']})"
              for ch, data in CHAPTER_DATA.items() if 1500 <= data['needed'] < 2000)}

### MEDIUM（需要扩充，需+1000-1499字）
{chr(10).join(f"- 第{ch}章: {data['current']}→{TARGET_WORDS} (+{data['needed']})"
              for ch, data in CHAPTER_DATA.items() if 1000 <= data['needed'] < 1500)}

### NORMAL（常规扩充，需+300-999字）
{chr(10).join(f"- 第{ch}章: {data['current']}→{TARGET_WORDS} (+{data['needed']})"
              for ch, data in CHAPTER_DATA.items() if data['needed'] < 1000)}

## 执行顺序建议
1. 先处理CRITICAL级别章节（共5章）
2. 再处理HIGH级别章节（共6章）
3. 然后处理MEDIUM级别章节（共10章）
4. 最后处理NORMAL级别章节（共18章）
"""

    master_file = base_dir / '扩充总计划.md'
    with open(master_file, 'w', encoding='utf-8') as f:
        f.write(master_plan)

    print(f"\n总计划已保存: {master_file}")

if __name__ == '__main__':
    main()
