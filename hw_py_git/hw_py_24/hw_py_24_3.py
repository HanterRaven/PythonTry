import os


def zero_file(start_dir):
    full_name_file = []
    for root, dirs, files in os.walk(start_dir):
        if len(files) > 0:
            for i in files:
                if os.path.getsize(root + "\\" + i) > 0:
                    print(f'{root + chr(92) + i} - {os.path.getsize(root + chr(92) + i)} bytes')
                else:
                    full_name_file.append(root + "\\" + i)
    print()
    return full_name_file


def work_file(file_name, start_dir, dir_for_zero_file):
    for i in file_name:
        if not os.path.isdir(start_dir + chr(92) + dir_for_zero_file):
            os.mkdir(start_dir + chr(92) + dir_for_zero_file)
        os.replace(i, (start_dir + chr(92) + dir_for_zero_file + chr(92) + os.path.basename(i)))
        print(f"Файл - {os.path.basename(i)}, был перемещен из дериктории {os.path.dirname(i)} "
              f"в дерикторию {start_dir + chr(92) + dir_for_zero_file}")


work_file(zero_file("work"), "work", "empty_file")
