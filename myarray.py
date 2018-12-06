# 类的案例精选 自定义一个数组类，

# 数组与数字间的四则运算，数组之间的加法运算，内积运算和比较大小，
# 数组元素访问和比较大小。数组元素访问和修改。以及成员测试等功能


class MyArray(object):
    # "所有元素必须为数字"
    __value = []  # 数组容器
    __size = []  # 数组大小

    def __is_number(self, n):
        if (not isinstance(n, int)) and (not isinstance(n, float)) and (
                not isinstance(n, complex)):
            return False
        return True

    def __init__(self, *args):
        if not args:
            self.__value = []
        else:
            for arg in args:
                if not self.__is_number(arg):
                    print('所有元素必须为数字')
                    return
            self.__value = list(args)

    # 数组中每个元素都与数字相加或数组相加
    def __add__(self, n):
        if self.__is_number(n):  # 若位数字，相加，返回新数组
            b = MyArray()
            for v in self.__value:
                b.__value.append(v + n)
            return b
        elif isinstance(n, MyArray):  # 若为数组，逐项相加，返回新数组
            if len(n.__value) == len(self.__value):
                c = MyArray
                for i, j in zip(self.__value, n.__value):
                    c.__value.append(i + j)
                return c
            else:
                print('数组长度不相等')
        else:
            print("不支持")

    def __sub__(self, n):  # 数组中每个元素都与n相减，返回新数组
        if not self.__is_number(n):
            print("不支持’-‘的数值类型")
            return
        b = MyArray()
        for v in self.__value:
            b.__value.append(v - n)
        return b

    def __mul__(self, n):  # 数组中每个数与n相乘，返回新数组
        if not self.__is_number(n):
            print("不支持 '*' 的数据类型")
        b = MyArray()
        for v in self.__value:
            b.__value.append(v * n)
        return b

    def __truediv__(self, n):  # 数组中每个数与n相乘，返回新数组
        if not self.__is_number(n):
            print("不支持'/'的数据类型")
        b = MyArray()
        for i in self.__value:
            b.__value.append(i / n)
        return b

    def __floordiv__(self, n):  # 数组中每个数与n整乘，返回新数组
        if not self.__is_number(n):
            print("不支持的数据类型")
            return
        b = MyArray()
        for i in self.__value:
            b.__value.append(i // n)
        return b

    def __mod__(self, n):  # 数组中每个数与n求余，返回新数组
        if not self.__is_number(n):
            print("不支持的数据类型")
            return
        b = MyArray()
        for i in self.__value:
            b.__value.append(i % n)
        return b

    def __pow__(self, n):  # 数组中每个数与n进行幂运算，返回新数组
        if not self.__is_number(n):
            print("不支持的数据类型")
            return
        b = MyArray()
        for i in self.__value:
            b.__value.append(i ** n)
        return b

    def __len__(self):  # 返回数组长度
        return len(self.__value)

    def __repr__(self):  # 直接使用对象作为语句时调用该函数
        return repr(self.__value)

    def __str__(self):
        return str(self.__value)

    def append(self, v):  # 添加元素
        if not self.__is_number(v):
            print("只可以添加数字")
        self.__value.append(v)

    def __getitem__(self, item):  # 获取指定位置的元素值
        if isinstance(item, int) and 0 <= item < len(self.__value):
            return self.__value[item]
        else:
            print("索引超出范围")

    def __setitem__(self, index, value):  # 设置指定位置的值
        if not self.__is_number(value):
            print("不支持的数据类型")
            return
        if isinstance(index, int) and 0 <= index < len(self.__value):
            self.__value[index] = value
        else:
            print("输入的索引超范围")

    def __contains__(self, v):  # 包含运算符 in
        if v in self.__value:
            return True
        else:
            return False

    def dot(self, v):  # 模拟向量内积
        if not isinstance(v, MyArray):
            print(v, "必须是MyAray的实例")
            return
        if len(v) != len(self.__value):
            print("长度不相等")
            return

        b = MyArray()
        for m, n in zip(v.__value, self.__value):
            b.__value.append(m * n)
        return b

    def __eq__(self, v):  # 关系运算符 ==
        if not isinstance(v, MyArray):
            print("不支持的数据类型")
            return
        if self.__value == v.__value:
            return True
        return False

    def __it__(self, v):  # 关系运算符<
        if not isinstance(v, MyArray):
            print(v, "不是MyArray的实例")
            return
        if self.__value < v.__value:
            return True
        return False


if __name__ == '__main__':
    # print('作为模块使用')
    x = MyArray(1, 2, 3, 4, 5)
    x = x+5
    print(x)