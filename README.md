# PDF_Contents_Generator
这是PDF目录生成器

## 实现功能

1. 将提取的 txt 文件处理后保存在`output_txt`文件夹中
2. 将`output_txt`文件夹中的 txt 文档写入到 pdf 文件中，将`page_data.pkl`文件中存储的页码变量也写入 pdf 文件中
3. 将`output_txt`文件夹中的 txt 文档写入到 pdf 文件中，不写入页码信息，所有的页码都为5

## 使用方法

1. 首先使用`福昕阅读器`将下载的文档进行 OCR 识别，并将文档保存，保存该 pdf 到 `input_pdf` 文件夹中

![image-20230911110715280](https://vip2.loli.io/2023/09/11/UHviNgk7FaLItMJ.png)

2. 然后手动将PDF目录提取出来，如果需要处理txt目录，保存在`input_txt`文件夹中，如果不需要，则直接将txt目录存放在保存在`input_txt`文件夹中：

![image-20230911111053123](https://vip2.loli.io/2023/09/11/KiokPFWQRrGNHLa.png)

3. 然后根据需求执行上述的三个功能：

   1. 功能一：`is_modify_txt = 1`
      * 因为上述的txt文档存在一些问题，可能是页码问题，也可能会有特殊符号，如“.”，“…”，“/”等，需要手动删除，这部分的代码将后面的页码保存在`page_data.pkl`文件中，同时根据章节进行分级（判断方式为`.`的个数），同时删除每一行后面的数字和空格
      * 处理后的文档保存在output_txt文件夹中
   2. 功能二：`is_write_txt_to_pdf = 1`
      * 将准备好写入的txt文件保存在`output_txt`文件夹中
      * 将功能一中保存的`page_data.pkl`页码数据以及`output_txt`文件夹中的目录文件`xxx.txt`写入到 pdf 文件中
      * 注意，这里会覆盖到之前pdf文档中的目录
   3. 功能三：`is_write_txt_to_pdf_with_no_page_information = 1`
      * 将准备好写入的txt文件保存在`output_txt`文件夹中
      * 功能三相对功能二缺乏将页码存入到 pdf 文件中，这里仅仅将不包含页码的 txt 文件存入到 pdf 文件中

   