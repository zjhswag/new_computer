file_path = r"C:\Users\14601\Desktop\语料\2.txt"  # Path to the uploaded file

# Read the content of the file
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Remove specific strings
content = (content.replace('- **答案**：', '').replace('- **解析**：', '').replace('.', '请判断以下说法是否正确。')
           .replace('- ', '').replace('**题目**：', '').replace('- **选项**：', '')
           .replace('正确答案：', '').replace('答案：', '').replace('答：', '').replace('答案:', ''))

# Remove the question numbers (assuming they are in the format like "1.", "2.", etc.)
import re

content = re.sub(r'\d+', '', content)
content = re.sub(r'\d+\)', '', content)
content = re.sub(r'\d+\）', '', content)
content = re.sub(r'\d+\.', '', content)


def remove_extra_spaces_preserve_empty_lines(text):
    lines = text.splitlines()
    processed_lines = []
    for line in lines:
        # 去除行首和行尾的空白字符
        stripped_line = line.strip()
        if stripped_line:
            # 移除单词之间的多余空格
            processed_line = ' '.join(stripped_line.split())
        else:
            # 保留空行
            processed_line = ''
        processed_lines.append(processed_line)
    return '\n'.join(processed_lines)


# 示例使用

content = remove_extra_spaces_preserve_empty_lines(content)

# Write the modified content back to the file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(content)
