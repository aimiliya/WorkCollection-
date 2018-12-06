# 利用io操作检查代码复用性
from os.path import isfile as isfile
from time import time as time

Result = {}
Allines = []
FileName = r"exam1.py"  # 检查的文件名


# FileName = input("请输入要检查文件名的，包括全路径")

def pre_operate():
    global Allines
    with open(FileName, 'r', encoding='utf-8') as fp:
        for line in fp:
            line = ''.join(line.split())
            if line != '':
                Allines.append(line)


# 检查当前位置是否是复制
def if_has_duplicated(index):
    for item in Result.values():
        for it in item:
            if index == it[0]:
                return it[1]  # 返回空格


# 如果当前第二个引位于重复的span中，返回True,否则返回false
def is_in_span(index2):
    for item in Result.values():
        for i in item:
            if i[0] <= index2 < i[0] + i[1]:
                return True
    return False


def main_check():
    global Result
    total_len = len(Allines)
    index1 = 0
    while index1 < total_len - 1:
        span = if_has_duplicated(index1)
        if span:
            index1 += span
            continue
        index2 = index1 + 1
        while index2 < total_len:
            if is_in_span(index2):
                index2 += 1
                continue
            src = ''
            des = ''
            for i in range(10):
                if index2 + i >= total_len:
                    break
                src += Allines[index1 + i]
                des += Allines[index2 + i]
                if src == des:
                    t = Result.get(index1, [])
                    for tt in t:
                        if tt[0] == index2:
                            tt[1] = i + 1
                            break
                        else:
                            t.append([index2, i + 1])
                    Result[index1] = t
                else:
                    t = Result.get(index1, [])
                    for tt in t:
                        if tt[0] == index2:
                            index2 += tt[1]
                            break
                    else:
                        index2 += 1

            # 优化Result字典，删除span小于3的条目
            Result[index1] = Result.get(index1, [])
            for n in Result[index1][::-1]:
                if n[1] < 3:
                    Result[index1].remove(n)
            if not Result[index1]:
                del Result[index1]

            # 计算最小复制代码的索引
            a = [ttt[1] for ttt in Result.get(index1, [[index1, 1]])]
            if a:
                index1 += max(a)
            else:
                index1 += 1


# 输出结果
def output():
    print('-' * 20)
    print('-' * 20)
    print('Result:')
    for key, value in Result.items():
        print('The original line is: \n {0}'.format(Allines[key]))
        print("It's line number is {0}".format(key))
        print('The duplicated line numbers are:')
        for i in value:
            print('    Start:', i[0], '   Span:', i[1])
        print('-' * 20)
    print('-' * 20)


if isfile(FileName):
    start = time()
    pre_operate()
    main_check()
    output()
    print('Time used:', time() - start)
