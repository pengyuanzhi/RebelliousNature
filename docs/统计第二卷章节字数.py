# -*- coding: utf-8 -*-
"""
统计第二卷各章节字数
"""
import re

file_path = r'D:\AI\homework\ClaudeCode\RebelliousNature\第二卷_金丹岁月.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 找到正文开始位置
content_start = content.find('## 三、正文内容')
if content_start == -1:
    content_start = content.find('## 正文内容')
if content_start == -1:
    print("未找到正文开始标记")
    exit(1)

main_content = content[content_start:]

# 查找所有章节
chapter_pattern = r'^# 第(.+?)章\s*(.*)$'

chapters = []
for match in re.finditer(chapter_pattern, main_content, re.MULTILINE):
    chapter_num = match.group(1)
    chapter_title = match.group(2).strip()
    chapter_start = match.start()
    chapters.append({
        'num': chapter_num,
        'title': chapter_title,
        'start': chapter_start
    })

# 计算每章字数
for i in range(len(chapters)):
    if i < len(chapters) - 1:
        chapter_content = main_content[chapters[i]['start']:chapters[i+1]['start']]
    else:
        chapter_content = main_content[chapters[i]['start']:]

    # 去除标题行和空行
    lines = chapter_content.split('\n')
    content_lines = []
    for line in lines:
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
need_expand = [ch for ch in chapters if ch.get('chars', 0) < 2500]

avg_chars = sum([ch.get('chars', 0) for ch in chapters]) / total_chapters if total_chapters > 0 else 0

# 打印结果
print('='*60)
print('第二卷章节字数统计')
print('='*60)
print(f'总章节数：{total_chapters}')
print(f'平均字数：{avg_chars:.0f}字/章')
print(f'符合标准（2500-3500字）：{len(qualified)}/{total_chapters} ({len(qualified)/total_chapters*100 if total_chapters > 0 else 0:.1f}%)')
print(f'需要扩充（<2500字）：{len(need_expand)}章')
print()

if need_expand:
    print(f'需要扩充的章节 ({len(need_expand)}个)：')
    print('-'*60)
    for ch in need_expand[:30]:  # 只显示前30个
        print(f'第{ch["num"]}章 {ch["title"]}: {ch["chars"]}字')
    if len(need_expand) > 30:
        print(f'  ... 还有{len(need_expand)-30}章')
else:
    print('✅ 所有章节都符合标准！')
