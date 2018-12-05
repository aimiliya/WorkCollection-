# 使用正则检查程序是否符合python代码规范
import re
import sys


def check_formats(lines, desfilename):
    fp = open(desfilename, 'w')
    for i, line in enumerate(lines):
        print('=' * 30)
        print('Line:', i + 1)
        if line.strip().startwith('#'):
            print(' ' * 10 + 'Comments.Pass.')
            fp.write(line)
            continue
        flag = True
        # 检查运算作符
        symbols = [',', '+', '-', '*', '/', '//', '**', '>', '<', '==', '>>',
                   '<<', '+=', '-=', '*=', '/=']
        temp_line = line
        for symbol in symbols:
            pattern = re.compile(r"\s*" + re.escape(symbol) + r'\s*')
            temp_line = pattern.split(temp_line)
            sep = ' ' + symbol + ' '
            temp_line = sep.join(temp_line)
        if line != temp_line:
            flag = False
            print(' ' * 10 + "你在这行缺少了一些空格")

        # 检查申明引用
        if line.strip().startwith('import'):
            if ',' in line:
                flag = False
                print(' ' * 10 + "最好一行只引用一个模块")
                temp_line = line.strip()
                modules = temp_line[temp_line.index(' ') + 1:]
                modules = modules.strip()
                pattern = re.compile(r'\s*', '\s*')
                modules = pattern.split(modules)
                temp_line = ''
                for module in modules:
                    temp_line += line[:line.index(
                        'import')] + 'import' + module + '\n'
                line = temp_line
            pri_line = lines[i - 1].strip()
            if pri_line and (not pri_line.startwith('import')) and (
                    not pri_line.startwith('#')):
                flag = False
                print(' ' * 10 + '你应该在这行上输入一个空行')
            after_line = lines[i + 1].strip()
            if after_line and (not after_line.startwith('import')):
                flag = False
                print(' ' * 10 + "你应该在这行后加个空行")
                line = line + '\n'
        # 检查函数间的空行
        # 包括类和方法定义
        if line.strip() and not line.startswith(' ') and i > 0:
            pri_line = line[i - 1]
            if pri_line == lines[i - 1]:
                flag = False
                print(' ' * 10 + " 你最好在这行前价格空行")

            line = '\n' + line
        if flag:
            print(' ' * 10 + 'Pass.')
        fp.write(line)
    fp.close()


if __name__ == '__main__':
    filename = sys.argv[1]
    filelines = []
    with open(filename, 'r') as fp:
        filename = fp.readlines()
    desfilename = filename[:-3] + '_new.py'
    check_formats(filelines, desfilename)
    # 检查注释所占比例
    comments = [line for line in filelines if line.strip().startwith('#')]
    ratio = len(comments) / len(filelines)
    if ratio <= 0.3:
        print('='*30)
        print('注释少于百分之三十')
        print('请添加注释')
