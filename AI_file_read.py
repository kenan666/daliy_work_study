#---------------------------
# 算法启停读取
#---------------------------

# -*- coding:UTF-8 -*-

import os
import re
import datetime

filter = ['.txt']

# 函数名称：read_and_find_all_AI_file()
# 函数功能：循环遍历文件夹
# 函数参数：model_file_path：模型文件路径
#         out_file：输出的数据文件
# 返回值：out_file：结果输出文件 
def read_and_find_all_AI_file(model_file_path,out_file):

    for maindir , subdir ,file_name_list in os.walk(model_file_path):

        for file_name in file_name_list:
            #合并成一个完整路径
            apath = os.path.join(maindir, file_name)
            portion = os.path.splitext(apath)
            # 获取文件后缀 [0]获取的是除了文件名以外的内容
            ext = portion[1]  

            if ext in filter:
                with open (out_file,'a+',encoding='utf-8') as outFile:
                    # 先清空文件，再重新写入数据
                    print ('test1')
                    outFile.seek(0)
                    outFile.truncate()
                    print ('1')
                    # print("file-name--->",file_name)
                    outFile.write(model_file_path + '/' + file_name + '\n')
                outFile.close()

    print ('write done!')


if __name__ == "__main__":
    model_path = '/Users/kenan/Desktop/test_file/test_mini_pro/test_file1'
    out_file = '/Users/kenan/Desktop/test_file/test_mini_pro/test_name.txt'

    read_and_find_all_AI_file(model_path,out_file)

