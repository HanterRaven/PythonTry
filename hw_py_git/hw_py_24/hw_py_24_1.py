import os, time


def search_file(start_dir, find_file):
    is_file = False
    for root, dirs, files in os.walk(start_dir, topdown=True):
        if find_file in files:
            # print(f"{find_file}  ({root}) - последнее время доступа {os.path.getatime(root+'/'+find_file)}")
            # или
            vrem = os.path.getatime(root + '\\' + find_file)
            print(
                f"{find_file}  ({root}) - "
                f"последнее время доступа {time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(vrem))}")
            is_file = True
    if not is_file:
        print("Такого файла в указаной дериктории не существует")


search_file("test_dir", "4.txt")
