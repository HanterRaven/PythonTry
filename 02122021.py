import os.path, os, time


#
# print(os.path.split(r"E:\u4\pythonProject\now_papka"))
# print(os.path.dirname(r"E:\u4\pythonProject\now_papka"))
# print(os.path.basename(r"E:\u4\pythonProject\now_papka"))
# print(os.path.join(r"E:\u4\pythonProject", "now_papka"))

# dirs = ["Work\F1", "Work\F2\F21"]
# for i in dirs:
#     os.makedirs(i)
# files = {"Work": ["w.txt"], "Work\F1": ["f11.txt", "f12.txt", "f13.txt"], "Work\F2\F21": ["f211.txt", "f212.txt"]}
# for d, j in files.items():
#     for file in j:
#         file_path = os.path.join(d, file)
#         open(file_path, "w").close()
# file_with_text = [r"Work\w.txt", r"Work\F1\f12.txt", r"Work\F2\F21\f211.txt", r"Work\F2\F21\f212.txt"]
# for file in file_with_text:
#     with open(file, "w") as f:
#         f.write(f"Some sample text for {file} file")
#
#
# def print_tree(root, topdown):
#     print(f"Obhod {root} {'sverhu v niz' if topdown else 'snizu vverh'}")
#     for rot, dirs, files in os.walk(root, topdown=topdown):
#         print(rot)
#         print(dirs)
#         print(files)
#         print("-" * 50)
#
#
# print_tree("Work", topdown=False)
# print_tree("Work", topdown=True)
# print(os.path.exists(r"E:\u4\hren\tests\post.txt"))
# print(os.path.getctime(r"E:\u4\pythonProject\Work\w.txt"))  # создание время
# print(os.path.getatime(r"E:\u4\pythonProject\Work\w.txt"))  # ремя последнего доступа к файлу
# print(os.path.getmtime(r"E:\u4\pythonProject\Work\w.txt"))  # время последнего изменения файла
# print(os.path.getsize(r"E:\u4\pythonProject\Work\w.txt"))  # размер файла в байтах

# path = r"E:\js.zip"
# size = os.path.getsize(path)
# kb = size // 1024
# print("Razmer : ", kb, "Kb")
# atime = os.path.getatime(path)
# mtime = os.path.getmtime(path)
# print("Data last ispolzovanie :", time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime)))
# print("Data last redattirovaniya :", time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(mtime)))
#
# print(os.path.normcase(r"E:\u4\pythonProject\Work\w.txt"))
#
# print(os.path.relpath(r"E:\u4\pythonProject\Work\w.txt"))
# print(os.path.isfile(r"E:\u4\pythonProject\Work\w.txt"))  # proveraet nalichie fayla
# print(os.path.isdir("E:\\u4\\pythonProject\Work\\"))


# def print_tree(root):
#     for rot, dirs, files in os.walk(root, topdown=True):
#         if rot == root:
#             for i in dirs:
#                 print(i, "-dir")
#             for j in files:
#                 print(j, "-file",os.path.getsize(rot+"\\"+j), "byte")
#
#
#
# print_tree("Work")
# -A, --all Bсе файлы и вложенные дериктории
# z dopisal tut