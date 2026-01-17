# -*- coding: utf-8 -*-
import re

# 读取文件
with open('第二卷_金丹岁月.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 找所有章节 - 更宽松的匹配
pattern = re.compile(r'^# 第[七九十百零零五六七八一二三四五六八九]+章 ', re.MULTILINE)

matches = list(pattern.finditer(content))

print(f'找到 {len(matches)} 个章节\n')

# 计算每章字数
for i, match in enumerate(matches):
    start_pos = match.start()
    title = match.group(0).strip()

    # 找到章节结束位置
    if i + 1 < len(matches):
        end_pos = matches[i+1].start()
    else:
        # 最后一章,找到文件结尾或某个标记
        end_pos = content.find('\n---\n', start_pos + 100)
        if end_pos == -1:
            end_pos = len(content)

    # 提取章节内容
    chapter_content = content[start_pos:end_pos]

    # 计算中文字符数(不包括空格、换行等)
    chinese_chars = re.findall(r'[\u4e00-\u9fff]', chapter_content)
    word_count = len(chinese_chars)

    # 提取章节名
    clean_title = title.replace('#', '').strip()

    print(f'{clean_title}: {word_count} 中文字符')
