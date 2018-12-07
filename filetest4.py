# 递归删除指定文件夹下的指定文件 # 拓展删除大小为0的文件
# 方法一
'''
from os import remove, listdir
from os.path import isdir, join, splitext, getsize

filetypes = ['.tep', '.log', '.obj', '.txt']


def del_certain_files(directory):
    if not isdir(directory):
        return
    for filename in listdir(directory):
        temp = join(directory, filename)  # 路径拼接
        if isdir(temp):
            del_certain_files(temp)
        elif splitext(temp)[1] in filetypes:  # splitext 拆分成文件路径名和点后缀名
            remove(temp)
            print(temp, 'deleted.')
        elif getsize(temp) == 0:  # 文件大小为0 ，删除
            remove(temp)


def main():
    directory = r'E:\new'
    del_certain_files(directory)
'''
# 方法二
import win32con
import win32api
import os
from win32con import FILE_ATTRIBUTE_NORMAL


def del_dir(path):
    for file in os.listdir(path):
        file_or_dir = os.path.join(path, file)
        if os.path.isdir(file_or_dir) and not os.path.islink(file_or_dir):
            del_dir(file_or_dir)  # 递归删除子文件夹及其文件
        else:
            try:
                os.remove(file_or_dir)  # 尝试删除该文件
            except:  # 将文件设置为普通文件，再删除
                win32api.SetFileAttributes(file_or_dir, FILE_ATTRIBUTE_NORMAL)
                os.remove(file_or_dir)
    os.rmdir(path)


del_dir('E:\\old')
