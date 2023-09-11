import os
import PyPDF2


class WriteTxtToPDF:

    def __init__(self, input_folder, output_folder, output_txt_folder, pdf_files, output_txt_files, page_init_number,
                 page_data):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.output_txt_folder = output_txt_folder
        self.pdf_files = pdf_files
        self.output_txt_files = output_txt_files
        self.page_init_number = page_init_number
        self.page_data = page_data

    def add_page_number_to_pdf(self, pdf_writer, lines):
        # 初始化父目录列表
        parent_bookmarks = [None] * 8  # 假设最大层级为5

        # 为新PDF添加目录
        for index, line in enumerate(lines):
            leading_spaces = len(line) - len(line.lstrip(' '))
            level = leading_spaces // 2  # 每两个空格代表一个层级

            # 如果行数超过页数，只链接到最后一页
            # page_num = min(index, pdf_reader.numPages - 1) # 这是设置的页码不超过PDF的总页数
            if self.page_init_number is not None:
                page_num = self.page_init_number + self.page_data[index - 1] - 1
            else:
                page_num = 5

            # 根据层级确定父目录
            if level > 1:
                parent = parent_bookmarks[level - 2]
            else:
                parent = None

            # 添加目录项
            new_bookmark = pdf_writer.addBookmark(title=line.strip(), pagenum=page_num, parent=parent)

            # 更新父目录列表
            parent_bookmarks[level - 1] = new_bookmark

    def write_txt_to_pdf(self):
        for pdf_file in self.pdf_files:
            base_name = os.path.splitext(pdf_file)[0]
            txt_file = base_name + ".txt"

            if txt_file in self.output_txt_files:
                # 获取文件路径
                input_pdf_path = os.path.join(self.input_folder, pdf_file)
                txt_path = os.path.join(self.output_txt_folder, txt_file)
                output_pdf_path = os.path.join(self.output_folder, pdf_file)

                # 读取txt文件中的内容，每一行作为一个目录项
                with open(txt_path, 'r', encoding='utf-8') as txt_file:
                    lines = txt_file.readlines()

                # 读取原始PDF
                with open(input_pdf_path, 'rb') as origin_pdf_file:
                    pdf_reader = PyPDF2.PdfFileReader(origin_pdf_file)
                    pdf_writer = PyPDF2.PdfFileWriter()

                    # 将原始PDF的每一页添加到新PDF
                    for page_num in range(pdf_reader.numPages):
                        page = pdf_reader.getPage(page_num)
                        pdf_writer.addPage(page)

                    self.add_page_number_to_pdf(pdf_writer, lines)

                    # 保存新PDF
                    with open(output_pdf_path, 'wb') as output_pdf_file:
                        pdf_writer.write(output_pdf_file)
        print("处理完成！所有带目录的PDF都已保存在output文件夹中。")
