# f = open("text.txt", "r+")
# # print(f.read(3))
# # print(f.tell())
# # print(f.seek(1))
# # print(f.read())
# # print(f.tell())
#
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
#
# f.close()
#
# with open("text.txt", "w+") as f:
#     print(f.write("0123456789"))
# i = 0
# with open("text.txt", "r") as f:
#     for line in f:
#         print(line)
#         i += 1
# print(i)

# def get_line(lt):
#     lt = list(map(str, lt))
#     return "\t".join(lt)
#
#
# file_name = "res_1.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
# with open(file_name, "w") as f:
#     f.write(get_line(lst))
#
# print("Done")
#
# with open(file_name, "r") as f:
#     test = f.read()
#
# new_test = test.split("\t")
# new_test = list(map(float, new_test))
# print(test)
# print(new_test)
# print(len(new_test))

# def find_in_file(file_name):
#     max_l = 0
#     temp_res = []
#     res = []
#     c = 0
#     with open(file_name, "r") as new_file:
#         temp_file = new_file.read().split()
#         for i in temp_file:
#             temp_res.append(len(i))
#             if len(i) > max_l:
#                 max_l = len(i)
#         for j in temp_res:
#             if j == max_l:
#                 res.append(temp_file[c])
#             c += 1
#     return res
#
#
# print(find_in_file("poisk.txt"))

#
# text = "Строка№0\nСтрока№1\nСтрока№2\nСтрока№3\nСтрока№4\nСтрока№5\nСтрока№6\nСтрока№7\nСтрока№8\nСтрока№9\nСтрока№10\n"
# with open("one.txt", "w") as f:
#     f.write(text)
# read_file = "one.txt"
# write_file = "two.txt"
# with open(read_file, "r") as rf, open(write_file, "w") as wf:
#     for line in rf:
#         line = line.replace("Строка", "Line - ")
#         wf.write(line)
# with open(write_file,"r") as f:
#     for line in f:
#         print(line, end="")

# os
# os.path

import os

# print("Tekushaya deriktoriya", os.getcwd())
# print("Spisok ", os.listdir(".."))
# # os.mkdir("papka")
# # os.makedirs("papka\papka1\papka2")
#
# os.remove("two.txt")
# os.rename("papka", "now_papka")
# os.rename("1.txt", "now_papka/22.txt")
# os.renames("111.txt", "new_folder/text/test.txt")
# os.rmdir("123")

# for root, dirs, files in os.walk("e:/", topdown=True):
#     print("Root", root)
#     print("subRoot", dirs)
#     print("file", files)
#
#
# for root, dirs, files in os.walk("Work", topdown=False):
#
#     if len(dirs) == 0 and len(files) == 0:
#         print("Deriktoriya " + root + " udalena")
#         os.rmdir(root)

print("Noviy code")
