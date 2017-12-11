import os

def rename_files():
    file_list = os.listdir("/Users/zichun.wan/Downloads/prank/")
    print(file_list)
    saved_path = os.getcwd()
    print(saved_path)
    os.chdir("/Users/zichun.wan/Downloads/prank/")
    for file in file_list:
        print("Old_name - " + file)
        os.rename(file, file.translate(str.maketrans('', '', "0123456789")))  ##translate()要配合translate()使用
        print("New_name - " + file.translate(str.maketrans('', '', "0123456789")))


rename_files()