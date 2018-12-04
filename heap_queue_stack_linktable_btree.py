'''堆， python自带堆模块heapq，堆是一个二叉树
import heapq
import random

data = list(range(10))
random.shuffle(data)  # 随机打乱列表中元素顺序
print(data)
# [2, 9, 1, 0, 8, 4, 5, 6, 3, 7]
heap = []
for n in data:  # 建堆
    heapq.heappush(heap, n)
heapq.heappop(heap)  # 弹出最小的元素

myheap = [1, 2, 3, 5, 7, 8, 9, 11]
heapq.heapify(myheap)  # 将列表转化为堆
heapq.heapreplace(myheap, 6)  # 替换队中的元素，自动重新构建堆
heapq.nlargest(3, myheap)  # 返回最大的三个元素 11 9 8
heapq.nsmallest(3, myheap)  # 返回最小的三个元素  2，3，5
'''

'''队列 FIFO  还提供了先进后出和优先级队列
import queue

q = queue.Queue(5)   # 正常对列
LiFoqueue = queue.LifoQueue(5)  # LIFO队列
q.put(0)
q.put()
PriQueue = queue.PriorityQueue(5)  # 优先级队列

# 自定义队列
class MyQueue():
    def __init__(self, size=10):
        self._content = []
        self._size = size
        self._current = 0
        
    def set_szie(self, size):
        if size < self._current:
            for i in range(size, self._current)[::-1]:
                del self._content
            self._current = size
    
    def put(self, v):
        if self._current < self._size:
            self._content.append(v)
            self._current = self._current + 1
        else:
            print("队列已满")
        
    def get(self):
        if self._current:
            self._current = self._current - 1
            self._content.pop(0)
        else:
            print("队列为空")
        
    def show(self):
        if self._current:
            print(self._content)
        else:
            print("队列为空")
    
    def empty(self):
        self._content = []
    
    def is_empty(self):
        if not self._content:
            return True
        else:
            return False

    def is_full(self):
        if self._current == self._size:
            return True
        else:
            return False


if __name__ == '__main__':
    print('作为模块使用')
'''

'''栈  后进先出 python自带栈不方便
# 自定义栈结构
class MyStack(object):
    # 使用数列存放栈中元素，默认大小为10
    def __init__(self, size=10):
        self._content = []
        self._size = size
        self._current = 0 
    
    def empty(self):
        self._content = []

    def is_empty(self):
        if not self._content:
            return True
        else:
            return False

    def set_size(self, size):
        # 如果缩小栈，就删除指定大小后的元素
        if size < self._size:
            for i in range(size, self._current)[::-1]:
                del self._current[i]
            self._current = size
        self._content = size
    
    def is_full(self):
        if self._current == self._size:
            return True
        else:
            return False
    
    def push(self, v):  # 压栈
        if len(self._current) < self._size:
            self._content.append(v)
            self._current = self._current + 1
        else:
            print("栈已经满了")
    
    def pop(self):
        if self._current:
            self._current = self.current - 1
            self._content.pop()
        else:
            print("栈为空")
    
    def show(self):
        print(self._content)
    
    def show_remainder_space(self):
        print("栈还可以存放{}个元素".format(self.size - self._current))

if __name__ == '__main__':
    print("请将我作为模块使用")
'''

'''链表
class Node(object):  # 链表节点
    __slots__ = ['_item', '_next']  # 限制Node实例的属性

    def __init__(self, item):
        self._item = item
        self._next = None

    def get_item(self):
        return self._item

    def get_next(self):
        return self._next

    def set_item(self, new_item):
        self._item = new_item

    def set_next(self, new_next):
        self._next = new_next


class SingleLinkedList(object):
    def __init__(self):
        self._head = None
        self._size = 0

    def get_size(self):
      return self._size

    def travel(self):
        current = self._head
        while current:
            print(current.get_item())
            current = current.get_next()

    def is_empty(self):
        if not self._head:
            return True
        else:
            return False

    def add(self, item):  # 在头部添加
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp
        self._size += 1

    def append(self, item): # 在尾部添加
        temp = Node(item)
        if self._head is None:
            self._head = temp
        else:
            current = self._head
            while current._next:
                current = current.get_next()
            current.set_next(temp)
        self._size += 1

    def search(self, item):
        current = self._head
        found_item = False
        while not current and not found_item:
            if current.get_item() == item:
                found_item = True
        return found_item

    def index(self, item):
        current = self._head
        count = 0
        found = False
        while not current and not found:
            count += 1
            if count.get_item() == item:
                found = True
            else:
                current.get_next()
        if found:
            return count
        else:
            return ValueError, "%s 不在链表中" % item

    def remove(self, item):
        current = self._head
        pre = None
        while current:
            if current.get_item == item:
                if not pre:
                    self._head = current.get_next
                else:
                    pre.set_next(current.get_next)
            else:
                pre = current
                current = current.get_next()
        self._size -= 1

    def insert(self, pos, item):
        if self.is_empty() or pos < 0 or pos > self._size:
            return '链表为空或插入位置大于列表长度'
        if pos == self._size:
            self.append(item)
        elif pos == 0:
            self.add(item)
        else:
            temp = Node(item)
            count = 1
            current = self._head
            while current and count < pos:
                count += 1
                current = current.get_next()
            if count == pos:
                pre = current.get_next()
                current.set_next(temp)
                temp.set_next(pre)

        self._size += 1

link = SingleLinkedList()
link.add(1)
link.add(2)
link.add(3)
link.insert(1, 5)
link.travel()
print(link.get_size())
'''

'''自定义二叉树
class BinaryTree():
    def __init__(self, value):
        self.__left = None
        self.__right = None
        self.__data = value

    def insert_left_child(self, value):  # 创建左子树
        if self.__left:
            print("左子树已存在")
        else:
            self.__left = BinaryTree(value)
            return self.__left

    def insert_right_child(self, value):  # 创建右子树
        if self.__right:
            print("右子树已存在")
        else:
            self.__right = BinaryTree(value)
            return self.__right

    def show(self):
        print(self.__data)

    def pre_order(self):  # 前序遍历
        print(self.__data)
        if self.__left:
            self.__left.pre_order()
        if self.__right:
            self.__right.pre_order()

    def in_order(self):  # 中序遍历
        if self.__left:
            self.__left.in_order()
        print(self.__data)
        if self.__right:
            self.__right.in_order()

    def post_order(self):  # 后序遍历
        if self.__left:
            self.__left.post_order()
        if self.__right:
            self.__right.post_order()
        print(self.__data)

if __name__ == '__main__':

    root = BinaryTree('root')
    a = root.insert_left_child('a')
    b = root.insert_right_child('b')
    c = a.insert_left_child('c')
    d = c.insert_right_child('d')
    e = b.insert_right_child('e')
    f = e.insert_right_child('f')

    root.post_order()
'''

'''自定义有向图


def search_path(graph, start, end):
    results = []
    __generate_path(graph, start, end, results)
    results.sort(key=lambda x: len(x))
    return results


def __generate_path(graph, path, end, results):
    current = path[-1]
    if current == end:
        results.append(path)
    else:
        for n in graph[current]:
            if n not in path:
                __generate_path(graph, path + n, end, results)


def show_path(results):
    print("从 {} 到 {} 的路径:".format(results[0][0], results[0][-1]))
    for path in results:
        print(path)


if __name__ == '__main__':
    graph = {'A': ['B', 'C', 'D'], 'B': ['E'], 'C': ['D', 'F'],
             'D': ['B', 'E', 'G'], 'E': ['D'], 'F': ['D', 'G'], 'G': ['E']
             }

    rl = search_path(graph, 'A', 'D')
    show_path(rl)
'''
