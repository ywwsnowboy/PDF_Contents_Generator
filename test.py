# import os
# import PyPDF2
#
# # 定义文件夹路径
# input_folder = "input"
# midtxt_folder = "midtxt"
# output_folder = "output"
#
# # 如果输出文件夹不存在，创建它
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
#
# # 获取所有PDF和TXT文件名
# pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]
# txt_files = [f for f in os.listdir(midtxt_folder) if f.endswith('.txt')]
#
# for pdf_file in pdf_files:
#     base_name = os.path.splitext(pdf_file)[0]
#     txt_file = base_name + ".txt"
#
#     if txt_file in txt_files:
#         # 获取文件路径
#         input_pdf_path = os.path.join(input_folder, pdf_file)
#         txt_path = os.path.join(midtxt_folder, txt_file)
#         output_pdf_path = os.path.join(output_folder, pdf_file)
#
#         # 读取txt文件中的内容，每一行作为一个目录项
#         with open(txt_path, 'r', encoding='utf-8') as txt_file:
#             lines = txt_file.readlines()
#
#         # 读取原始PDF
#         with open(input_pdf_path, 'rb') as pdf_file:
#             pdf_reader = PyPDF2.PdfFileReader(pdf_file)
#             pdf_writer = PyPDF2.PdfFileWriter()
#
#             # 将原始PDF的每一页添加到新PDF
#             for page_num in range(pdf_reader.numPages):
#                 page = pdf_reader.getPage(page_num)
#                 pdf_writer.addPage(page)
#
#             # 初始化父目录列表
#             parent_bookmarks = [None] * 8  # 假设最大层级为5
#
#             # 为新PDF添加目录
#             for index, line in enumerate(lines):
#                 leading_spaces = len(line) - len(line.lstrip(' '))
#                 level = leading_spaces // 2  # 每两个空格代表一个层级
#
#                 # 如果行数超过页数，只链接到最后一页
#                 pagenum = min(index, pdf_reader.numPages - 1)
#
#                 # 根据层级确定父目录
#                 if level <= 1:
#                     parent = None
#                 else:
#                     parent = parent_bookmarks[level - 2]
#
#                 # 添加目录项
#                 new_bookmark = pdf_writer.addBookmark(title=line.strip(), pagenum=pagenum, parent=parent)
#
#                 # 更新父目录列表
#                 parent_bookmarks[level - 1] = new_bookmark
#
#             # 保存新PDF
#             with open(output_pdf_path, 'wb') as output_pdf_file:
#                 pdf_writer.write(output_pdf_file)
#
# print("处理完成！所有带目录的PDF都已保存在output文件夹中。")