# 实现对excel的操作，并统计所有学生每门课程的最高成绩
import openpyxl
from openpyxl import Workbook
import random


# 生成随机数据
def generate_random_information(filename):
    workbook = Workbook
    worksheet = workbook.worksheets[0]
    worksheet.append(['姓名'], ['课程'], ['成绩'])
    # 生成随机名字
    first_name = tuple('赵钱孙李')
    second_name = tuple('伟云空东')
    last_name = tuple('坤焱智')
    # 课程名称
    subjects = ('语文', '数学', '英语')
    # 随机生成200条数据
    for i in range(200):
        line = []
        r = random.randint(1, 100)
        name = random.choice(first_name)
        # 按一定概率生成两个字的名字
        if r > 50:
            name = name + random.choice(second_name)
        name = name + random.choice(last_name)

        # 依次生成姓名，课程名称和成绩
        line.append(name)
        line.append(random.choice(subjects))
        line.append(random.randint(0, 100))
    workbook.save(filename)


def get_result(old_file, new_file):
    # 用于存放结果数据的字典
    result = {}
    # 打开原始数据
    workbook = openpyxl.load_workbook(old_file)
    worksheet = workbook.worksheets[0]
    # 遍历原始数据
    for row in worksheet.rows[1:]:
        # 姓名，课程名，成绩
        name, subject, grade = row[0].value, row[1].value, row[2].value
        # 获取当前学生对应的课程名称和成绩信息
        # 若不存在返回空
        t = result.get(name, {})
        # 获取当前学生当前课程的成绩，若不存在则返回0
        f = t.get(subject, 0)
        # 只保留该学生课程的最高成绩
        if grade > f:
            t[subject] = grade
            result[name] = t

    workbook1 = Workbook()
    worksheet1 = workbook1.worksheet1[0]
    worksheet1.append(['姓名', '课程', '成绩'])
    # 将result字典中的结果存入数据写入Excel中
    for name, t in result.items():
        for subject, grade in t.items():
            worksheet1.append([name, subject, grade])
    workbook1.save(new_file)


if __name__ == '__main__':
    old_file = r'd:\test.xlsx'
    new_file = r'd:result.xlsx'
    generate_random_information(old_file)
    get_result(old_file, new_file)



