import os


def search_in_dir(start_dir):
    result = []
    for root, dirs, file in os.walk(start_dir, topdown=True):
        result_file = ["Файл - " + i for i in file if root == start_dir and file]
        result_dir = ["Каталог - " + i for i in dirs if root == start_dir and dirs]
        # или
        # result_file = [("Файл - " + root + chr(92) + i) for i in file if root == start_dir and file]
        # result_dir = [("Каталог - " + root + "\\" + i) for i in dirs if root == start_dir and dirs]
        result += result_file + result_dir
    return result


print(search_in_dir("second_test"))
