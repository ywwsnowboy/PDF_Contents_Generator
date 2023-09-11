import os
import re


def extract_values(line):
    # 1. 将 `. ` 替换为 `.`
    line = line.replace(". ", ".")

    # 2. 提取每行最后的数字
    match = re.search(r'(\d+)$', line)
    if match:
        num = int(match.group(1))
        line = line[:match.start()].rstrip()  # 移除数字部分
    else:
        num = 1

    # 3. 计算`.`的个数
    dot_count = line.split(' ', 1)[0].count('.')
    return line, num, dot_count


class ModifyTXT:

    def __init__(self, input_txt_folder, output_txt_folder, input_txt_files):
        self.input_txt_folder = input_txt_folder
        self.output_txt_folder = output_txt_folder
        self.input_txt_files = input_txt_files

    def modify_txt_to_new_txt(self):
        for txt_file in self.input_txt_files:
            input_path = os.path.join(self.input_txt_folder, txt_file)
            output_path = os.path.join(self.output_txt_folder, txt_file)

            with open(input_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            processed_lines = []
            page_number = []  # $$$$$$$$$
            dot_counts = []

            for line in lines:
                processed_line, num, dot_count = extract_values(line)
                processed_lines.append(processed_line)
                page_number.append(num)
                dot_counts.append(dot_count)

            with open(output_path, 'w', encoding='utf-8') as f:
                for idx, processed_line in enumerate(processed_lines):
                    indented_line = ' ' * ((dot_counts[idx] + 1) * 2) + processed_line
                    f.write(indented_line + "\n")
            print("TXT文件处理完毕。请查看 output_txt 文件夹。")
        return page_number

