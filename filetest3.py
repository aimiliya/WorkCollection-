# 编写程序，统计指定目录下所有C++源文件中不重复的代码数
from os.path import isdir, join
from os import listdir

AllLines = []  # 保存所有代码行
NotRepeatedlines = []  # 保存非重复的代码

file_num = 0  # 文件数
code_num = 0  # 代码数


def lines_count(directory):
    global AllLines
    global NotRepeatedlines
    global file_num
    global code_num

    for filename in listdir(directory):
        temp = join(directory, filename)
        if isdir(temp):
            lines_count(temp)  # 递归遍历子文件夹
        elif temp.endswith('.cpp'):
            file_num += 1
            with open(temp, 'r') as fp:
                while True:
                    line = fp.readline()
                    if not line:
                        break
                    if line not in NotRepeatedlines:
                        NotRepeatedlines.append(line)  # 记录非重复行
                    code_num += 1  # 记录所有代码行
    return (code_num, len(NotRepeatedlines))


path = r'E:\\programfile\\firstgame'
print("代码总行数：{0[0]}, 非重复代码行数{0[1]}".format(lines_count(path)))
print("文件总数：{}".format(file_num))
