# -*- coding: utf-8 -*-
"""
统计第二卷第81-90章字数
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

# 查找第81-90章
chapters = []
for i in range(81, 91):
    pattern = f'^# 第八十章{i-80}章[：:](.+)$' if i > 80 else '^# 第八十章[：:](.+)$'
    matches = list(re.finditer(pattern, main_content, re.MULTILINE))
    if matches:
        chapters.append({
            'num': f'第八十章{i-80}章' if i > 80 else '第八十章',
            'title': matches[0].group(1).strip() if matches[0].lastindex >= 1 else '',
            'start': matches[0].start()
        })

print(f'找到 {len(chapters)} 章')

# 计算每章字数
for i in range(len(chapters)):
    if i < len(chapters) - 1:
        chapter_content = main_content[chapters[i]['start']:chapters[i+1]['start']]
    else:
        # 找到第91章的位置
        next_pattern = '^# 第九十一章[：:](.+)$'
        remaining_content = main_content[chapters[i]['start']:]
        next_matches = list(re.finditer(next_pattern, remaining_content, re.MULTILINE))
        if next_matches:
            chapter_content = main_content[chapters[i]['start']:chapters[i]['start'] + next_matches[0].start()]
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

# 打印结果
print('\n' + '='*60)
print('第81-90章字数统计')
print('='*60)

for ch in chapters:
    title_part = f": {ch['title']}" if ch['title'] else ""
    status = "✅" if 2500 <= ch.get('chars', 0) <= 3500 else "❌"
    print(f"{ch['num']}{title_part}: {ch['chars']}字 {status}")

qualified = [ch for ch in chapters if 2500 <= ch.get('chars', 0) <= 3500]
need_expand = [ch for ch in chapters if ch.get('chars', 0) < 2500]

print(f'\n符合标准（2500-3500字）：{len(qualified)}/10章')
print(f'需要扩充（<2500字）：{len(need_expand)}/10章')
