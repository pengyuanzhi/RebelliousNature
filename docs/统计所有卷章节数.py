# -*- coding: utf-8 -*-
"""
统计所有卷的章节字数
"""
import re
import os

volumes = [
    ('第一卷_山坳少年.md', '第一卷'),
    ('第二卷_金丹岁月.md', '第二卷'),
    ('第三卷_元婴威震.md', '第三卷'),
    ('第四卷_化神之道.md', '第四卷'),
    ('第五卷_合道争锋.md', '第五卷'),
    ('第六卷_天仙之路.md', '第六卷')
]

base_path = r'D:\AI\homework\ClaudeCode\RebelliousNature'
all_results = []

for filename, volume_name in volumes:
    file_path = os.path.join(base_path, filename)

    if not os.path.exists(file_path):
        print(f'警告：{filename} 不存在')
        continue

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 找到正文开始位置
    content_start = 0
    for i, line in enumerate(lines):
        if '## 三、正文内容' in line or '## 正文内容' in line:
            content_start = i + 1
            break

    # 如果没找到正文标记，假设从第537行开始（第一卷的情况）
    if content_start == 0 and volume_name == '第一卷':
        content_start = 536

    # 提取正文内容
    content_lines = lines[content_start:]
    content = ''.join(content_lines)

    # 统计总字符数（正文部分）
    total_chars = len(content)

    # 查找章节（支持多种格式）
    chapter_patterns = [
        r'^# 第(\d+)章[：:](.+)$',
        r'^第(\d+)章[：:](.+)$',
    ]

    chapters = []
    for pattern in chapter_patterns:
        matches = list(re.finditer(pattern, content, re.MULTILINE))
        if matches:
            for match in matches:
                chapters.append({
                    'num': match.group(1),
                    'title': match.group(2).strip(),
                    'start': match.start()
                })
            break

    # 如果没找到章节，尝试其他方式
    if not chapters:
        # 尝试查找 ## 开头的章节
        matches = re.finditer(r'^## (.+)$', content, re.MULTILINE)
        for match in matches:
            title = match.group(1).strip()
            if title.startswith('第') and '章' in title:
                chapters.append({
                    'num': 'N/A',
                    'title': title,
                    'start': match.start()
                })

    # 计算每章字数
    for i in range(len(chapters)):
        if i < len(chapters) - 1:
            chapter_content = content[chapters[i]['start']:chapters[i+1]['start']]
        else:
            chapter_content = content[chapters[i]['start']:]

        # 去除标题行
        lines_text = chapter_content.split('\n')
        content_lines = []
        for line in lines_text:
            stripped = line.strip()
            if stripped and not stripped.startswith('#') and not stripped.startswith('**') and not stripped.startswith('---'):
                content_lines.append(line)

        chapter_text = '\n'.join(content_lines)
        char_count = len(chapter_text)

        chapters[i]['chars'] = char_count

    # 统计
    total_chapters = len(chapters)
    qualified = [ch for ch in chapters if 2500 <= ch.get('chars', 0) <= 3500]
    unqualified = [ch for ch in chapters if ch.get('chars', 0) < 2500 or ch.get('chars', 0) > 3500]

    avg_chars = sum([ch.get('chars', 0) for ch in chapters]) / total_chapters if total_chapters > 0 else 0

    result = {
        'volume': volume_name,
        'filename': filename,
        'total_chars': total_chars,
        'total_chapters': total_chapters,
        'qualified_chapters': len(qualified),
        'unqualified_count': len(unqualified),
        'avg_chars': avg_chars,
        'chapters': chapters
    }

    all_results.append(result)

    # 打印结果
    print(f'\n{"="*60}')
    print(f'{volume_name}')
    print(f'{"="*60}')
    print(f'文件：{filename}')
    print(f'正文总字符数：{total_chars:,}')
    print(f'章节数：{total_chapters}')
    print(f'平均字数：{avg_chars:.0f}字/章')
    print(f'符合标准（2500-3500字）：{len(qualified)}/{total_chapters} ({len(qualified)/total_chapters*100 if total_chapters > 0 else 0:.1f}%)')

    if unqualified:
        print(f'\n不符合标准的章节 ({len(unqualified)}个)：')
        for ch in unqualified[:10]:
            print(f'  第{ch["num"]}章 {ch["title"]}: {ch["chars"]}字')
        if len(unqualified) > 10:
            print(f'  ... 还有{len(unqualified)-10}个')
    else:
        print(f'\n✅ 所有章节都符合标准！')

# 生成汇总
print(f'\n\n{"="*60}')
print('总体汇总')
print(f'{"="*60}')

total_all_chars = sum([r['total_chars'] for r in all_results])
total_all_chapters = sum([r['total_chapters'] for r in all_results])
total_qualified = sum([r['qualified_chapters'] for r in all_results])

print(f'所有卷总字符数：{total_all_chars:,}')
print(f'所有卷总章节数：{total_all_chapters}')
print(f'符合标准章节总数：{total_qualified}/{total_all_chapters} ({total_qualified/total_all_chapters*100:.1f}%)')

print('\n各卷对比：')
print(f'{"卷名":<10}{"章节数":<10}{"总字数":<15}{"平均字数":<15}{"符合率"}')
print('-'*70)
for r in all_results:
    rate = f"{r['qualified_chapters']/r['total_chapters']*100:.1f}%" if r['total_chapters'] > 0 else "N/A"
    print(f"{r['volume']:<10}{r['total_chapters']:<10}{r['total_chars']:<15,}{r['avg_chars']:<15.0f}{rate}")

print('\n统计完成！')
