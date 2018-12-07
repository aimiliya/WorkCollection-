# 统计指定文件夹的大小以及文件和子文件夹的数量
import os

total_size = 0  # 文件夹大小
file_num = 0  # 文件数量
dir_num = 0  # 子文件夹数量


def visit_dir(path):
    global total_size
    global file_num
    global dir_num
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        if os.path.isfile(sub_path):
            file_num = file_num + 1  # 统计文件数量
            total_size = total_size + os.path.getsize(sub_path)  # 统计文件总大小
        elif os.path.isdir(sub_path):
            dir_num = dir_num + 1  # 统计文件夹数量
            visit_dir(sub_path)  # 递归遍历子文件夹


def main(path):
    if not os.path.isdir(path):
        print("他不是个文件夹或文件不存在")
        return
    visit_dir(path)


def size_convert(size):  # 单位换算
    K, M, G = 1024, 1024 ** 2, 1024 ** 3
    if size >= G:
        return str(round(size / G, 2)) + 'G bytes'
    elif size >= M:
        return str(round(size / M, 2)) + 'M bytes'
    elif size >= K:
        return str(round(size / K, 2)) + 'K bytes'
    else:
        return str(round(size, 2)) + 'Bytes'


def output(path):
    print(path + "下文件总大小:{}".format(size_convert(total_size)))
    print(path + "下文件大小：{}".format(file_num))
    print(path + "下子文件夹数量：{}".format(dir_num))


if __name__ == '__main__':
    path = r"f:\workcollection"
    main(path)
    output(path)


