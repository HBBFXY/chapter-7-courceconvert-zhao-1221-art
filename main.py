# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)

# 以下内容自行完成
import keyword

# 读取原文件内容
with open("random_int.py", "r", encoding="utf-8") as f:
    content = f.readlines()

processed_lines = []
# 遍历每一行处理
for line in content:
    # 拆分该行的单词（保留符号）
    tokens = []
    current_token = ""
    for char in line:
        if char.isalnum() or char == "_":  # 标识符的组成部分
            current_token += char
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
    if current_token:
        tokens.append(current_token)
    
    # 处理每个单词：保留字不变，其他转大写
    new_tokens = []
    for token in tokens:
        if keyword.iskeyword(token):
            new_tokens.append(token)
        else:
            new_tokens.append(token.upper())
    
    # 重组该行
    processed_lines.append("".join(new_tokens))

# 将处理后的内容写入新文件
with open("converted_random_int.py", "w", encoding="utf-8") as f:
    f.writelines(processed_lines)
