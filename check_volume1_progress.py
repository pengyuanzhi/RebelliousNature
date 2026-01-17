import re
import sys

# 设置输出编码为UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# 读取第一卷文件
with open('D:/AI/homework/ClaudeCode/RebelliousNature/第一卷_山坳少年.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 提取第一卷所有章节
pattern = r'## (第[一二三四五六七八九十百]+章|第\d+章) ([^\n]+)\n(.*?)(?=## 第|$)'
matches = re.findall(pattern, content, re.DOTALL)

chapters = []
for match in matches[:74]:
    chapter_num, title, body = match
    char_count = len(body.replace('\n', '').replace(' ', ''))
    chapters.append({
        'chapter': chapter_num,
        'title': title.strip(),
        'total_chars': char_count
    })

# 新标准目标字数映射
targets = {
    1: 3000, 2: 3000, 3: 3500, 4: 3000, 5: 5000, 6: 4500, 7: 3000, 8: 3000, 9: 4000, 10: 3000,
    11: 3000, 12: 3500, 13: 3000, 14: 3000, 15: 4000, 16: 3000, 17: 3000, 18: 3000, 19: 4000, 20: 3000,
    21: 3500, 22: 5000, 23: 3500, 24: 3000, 25: 4000, 26: 4500, 27: 5000, 28: 3000, 29: 3000, 30: 3000,
    31: 3500, 32: 3500, 33: 3000, 34: 3000, 35: 3000, 36: 4000, 37: 4000, 38: 4500, 39: 5000, 40: 5000,
    41: 3000, 42: 4000, 43: 3000, 44: 4500, 45: 3000, 46: 3000, 47: 3000, 48: 3000, 49: 3500, 50: 4500,
    51: 4500, 52: 5000, 53: 6000, 54: 5000, 55: 3000, 56: 4000, 57: 5000, 58: 4500, 59: 3500, 60: 3000,
    61: 4500, 62: 3000, 63: 3000, 64: 5000, 65: 6000, 66: 7000, 67: 3000, 68: 3500, 69: 3000, 70: 3500,
    71: 3500, 72: 4500, 73: 7000, 74: 6000
}

# 统计达标情况
completed = []
not_completed = []
total_target = 0
total_actual = 0

for i, ch in enumerate(chapters, 1):
    target = targets.get(i, 3000)
    actual = ch['total_chars']
    total_target += target
    total_actual += actual

    status = '✅' if actual >= target * 0.95 else '❌'
    completion_rate = (actual / target) * 100

    chapter_info = {
        'num': i,
        'chapter': ch['chapter'],
        'title': ch['title'],
        'target': target,
        'actual': actual,
        'rate': completion_rate,
        'status': status
    }

    if actual >= target * 0.95:
        completed.append(chapter_info)
    else:
        not_completed.append(chapter_info)

# 生成报告
print('=' * 100)
print(' ' * 35 + '第一卷新标准扩充进度报告')
print(' ' * 30 + '(文件：第一卷_山坳少年.md)')
print('=' * 100)
print()
print(f'【总览统计】')
print(f'  总章节数: {len(chapters)}章')
print(f'  目标总字数: {total_target:,}字')
print(f'  实际总字数: {total_actual:,}字')
print(f'  整体完成率: {total_actual/total_target*100:.1f}%')
print(f'  已达标章节数: {len(completed)}章 ({len(completed)/len(chapters)*100:.1f}%)')
print(f'  未达标章节数: {len(not_completed)}章 ({len(not_completed)/len(chapters)*100:.1f}%)')
print()

# 分部分统计
print('=' * 100)
print('【分部分统计】')
print('=' * 100)

parts = [
    (1, 13, '第一部分:山坳少年(1-13章)'),
    (14, 22, '第二部分:太华宗招徒(14-22章)'),
    (23, 45, '第三部分:外门弟子(23-45章)'),
    (46, 54, '第四部分:内门大比(46-54章)'),
    (55, 62, '第五部分:核心弟子(55-62章)'),
    (63, 66, '第六部分:寻找父亲(63-66章)'),
    (67, 74, '第七部分:闭关突破(67-74章)')
]

for start, end, part_name in parts:
    part_target = sum(targets.get(i, 3000) for i in range(start, end+1))
    part_actual = sum(chapters[i-1]['total_chars'] for i in range(start, end+1))
    part_completed = sum(1 for i in range(start, end+1) if chapters[i-1]['total_chars'] >= targets.get(i, 3000) * 0.95)

    print(f'\n{part_name}')
    print(f'  目标: {part_target:,}字  实际: {part_actual:,}字  完成率: {part_actual/part_target*100:.1f}%  达标: {part_completed}/{end-start+1}章')

print()
print('=' * 100)

# 未达标章节详情
if not_completed:
    print()
    print('【未达标章节详情】')
    print('=' * 100)
    header1 = '序号'
    header2 = '章节'
    header3 = '标题'
    header4 = '目标'
    header5 = '实际'
    header6 = '完成率'
    header7 = '状态'
    print(f'{header1:<6}{header2:<12}{header3:<25}{header4:<10}{header5:<10}{header6:<12}{header7:<8}')
    print('-' * 100)

    for ch in not_completed:
        num = ch['num']
        chapter_name = ch['chapter']
        title = ch['title']
        target = ch['target']
        actual = ch['actual']
        rate = ch['rate']
        status = ch['status']
        print(f'{num:<6}{chapter_name:<12}{title:<25}{target:<10}{actual:<10}{rate:>6.1f}%{status:<8}')

print()
print('=' * 100)
print(f'【结论】')
print('=' * 100)
if len(completed) == len(chapters):
    print('🎉 恭喜!第一卷所有章节均已达到新标准要求!')
else:
    print(f'📋 第一卷还有{len(not_completed)}章未达标,需要继续扩充')
print('=' * 100)
