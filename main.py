import os
import pickle
from HandlePDF import WriteTxtToPDF
from HandleTXT import ModifyTXT

# 定义文件夹路径
input_folder = "input"
output_folder = "output"
input_txt_folder = "input_txt"
output_txt_folder = "output_txt"


# 如果输出文件夹不存在，创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取所有PDF和TXT文件名
pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]
output_txt_files = [f for f in os.listdir(output_txt_folder) if f.endswith('.txt')]
input_txt_files = [f for f in os.listdir(input_txt_folder) if f.endswith('.txt')]

# 进行哪些操作，如果值为 1 表示执行，如果值为 0，表示不执行
is_modify_txt = 0
is_write_txt_to_pdf = 0
is_write_txt_to_pdf_with_no_page_information = 1

if is_modify_txt == 1:
    modify_txt = ModifyTXT(input_txt_folder, output_txt_folder, input_txt_files)
    page_number = modify_txt.modify_txt_to_new_txt()
    with open('page_data.pkl', 'wb') as file:
        pickle.dump(page_number, file)
    print("保存完毕。")

if is_write_txt_to_pdf == 1:
    with open('page_data.pkl', 'rb') as file:
        page_data = pickle.load(file)
    print(page_data)
    try:
        page_init_number = int(input("请输入第一页之前的页码: "))
        print(f"你输入的整数是: {page_init_number}")
    except ValueError:
        print("不是整数。")

    writeTopdf = WriteTxtToPDF(input_folder, output_folder, output_txt_folder, pdf_files, output_txt_files, page_init_number, page_data)
    writeTopdf.write_txt_to_pdf()

if is_write_txt_to_pdf_with_no_page_information == 1:
    writeTopdf = WriteTxtToPDF(input_folder, output_folder, output_txt_folder, pdf_files, output_txt_files, page_init_number = None, page_data = None)
    writeTopdf.write_txt_to_pdf()


 # 这里会存在小bug，并不能够针对不同的PDF文档
 # 具体要修改的部分可通过检索来发现，全局检索冒号右侧的内容->：# $$$$$$$$$
 # 后续对该bug进行修复






