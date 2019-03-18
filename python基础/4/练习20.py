'''
回顾：
    面向对象编程语言：
            继承
                不改变原类的情况下，添加新的功能
            封装
            多态
                动态
                静态

封装：
    双下划线(__)开头的标识符(属性，方法)
    私有成员
多继承
    一个子类继承自两个或两个以上的父类(基类)

解决标识符冲突问题:

__mro__ 属性
    用mro显示调用相应的方法：
          super(类名，对象).方法名()
钻石继承

函数重写
    在类内添加相应的方法
    内建函数：
    repr(x)         def  __repr__(self):
    str(x)              __str__(self):
    abs(x)
    len(x)
    reversed(x)
    round(x)
    int(x)
    float(x)
    complex(x)
    bool(x)            __bool__,__len__,True

属性管理函数:
    hasattr(obj,"name")
    getattr(obj,name[,dafault)
    setattr(obj,name,value)
    delattr(obj,name)

可迭代对象，迭代器
    class A:
        def __iter__(self):
            return 迭代器  #return self
        def __next__(self)
             迭代器协议
            if  没有数据：
                raise StopIteration
            return 数据
issubclass(cls,类或元组)    判断继承关系
'''


# try:
#     with open("test.txt", "r", encoding='utf-8') as fr:
#         for line in fr:
#             print(line)
#     # fr.read()   出错，fr 已经被 with 语句自动关闭
# except OSError:
#     print("文件打开失败！")
#
# # 此示例示意自定义一个环境管理器，让其能用与with语句管理


# class A:
#     def __enter__(self):
#         print("__enter__方法被调用")
#         self.file = open("test.txt", encoding="utf-8")
#         return self  # return 返回的对象会被 as 变量所绑定
#
#     def __exit__(self, e_type, e_value, e_cb):
#         self.file.close()
#         if e_type is None:
#             print("正常离开with语句")
#         else:
#             print("在离开with语句时发生了异常")
#             print("异常类型是：", e_type)
#             print("错误对象是：", e_value)
#             print("追踪对象是：", e_cb)
#         print("A.__exit__ 被调用，已离开with语句")


# with A() as a:
#     print(a.file.readline())
#     # 3 / 0 #发生异常
#     print("这是with语句内部的语句")
#
# print("程序正常退出")


# class Mynumber:
#     def __init__(self, value):
#         self.data = value
#
#     def __repr__(self):
#         return 'Mynumber(%d)' % self.data
#
#     def __add__(self, other):
#         return Mynumber(self.data + other.data)  # 创建一个新的对象并返回
#
#     def __sub__(self, rhs):
#         return Mynumber(self.data - rhs.data)
#
#     def __mul__(self, rhs):
#         return Mynumber(self.data * rhs.data)


# n1 = Mynumber(100)
# n2 = Mynumber(200)
# print(n1)
# # n3 = n1.__add__(n2)
# n3 = n1 + n2  # 等同于 n3 = n1.__add(n2)
# print(n1, '+', n2, '=', n3)
# n4 = n1 - n2
# print(n1, '-', n2, '=', n4)
# n5 = n1 * n3
# print(n5)

# 练习：
# 此示例示意索引和切片运算符[]
# 的重载


# class Mylist:
#     def __init__(self, iterable=()):
#         self.iterable = [x for x in iterable]
#
#     def __repr__(self):
#         return 'Mylist(%s)' % self.iterable
#
#     def __getitem__(self, i):
#         print('__getiem__:i=', i)
#         if type(i) is int:
#             print('您正在做索引操作')
#         elif type(i) is slice:
#             print('您正在做切片操作')
#             print("起始值是：", i.start)
#             print("终止值是：", i.stop)
#             print("步长是：", i.step)
#         elif type(i) is str:
#             print("您在用字符串操作")
#             return 0
#         return self.iterable[i]


# L1 = Mylist([1, -2, 3, -4, 5])
# a = L1[::-1]  # a = L1.__getiem__(slice(None, None, None))
# print(a)

# 用装饰器方式实现特性属性


# class Student:
#     def __init__(self, s):
#         self.__score = s
#
#     @property
#     def score(self):
#         '''getter'''
#         return self.__score
#
#     @score.setter
#     def score(self, s):
#         '''setter'''
#         assert 0 <= s <= 100, '成绩效验失败！'
#         self.__score = s
#
#
# stu = Student(59)
# print(stu.score)  # 取值   stu.getscore()
# stu.score = 999  # 赋值 stu.setscore(999)
# print(stu.score)

# 练习：
#     实现有序集合类 OrderSet() 能实现两个集合的交集 &, 并集 | 补集 -，
#     对称补集 ^, ==, !=, in, not in 等操作
#         要求： 集合内部用list存储数据

# 如:

# class OrderSet:
#     def __init__(self, iterable=()):
#         self.data = iterable

#     def __repr__(self):
#         return 'OrderSet(%s)' % self.data

#     def __and__(self, rhs):
#         return OrderSet(list(set(self.data) & set(rhs.data)))

#     def __or__(self, rhs):
#         return OrderSet(list(set(self.data) | set(rhs.data)))

#     def __xor__(self, rhs):
#         return OrderSet(list(set(self.data) ^ set(rhs.data)))

#     def __ne__(self, rhs):
#         if self.data != rhs.data:
#             return True
#         return False

#     def __eq__(self, rhs):
#         if self.data == rhs.data:
#             return True
#         return False

#     def __contains__(self, e):
#         return e in self.data


# s1 = OrderSet([1, 2, 3, 4])
# s2 = OrderSet([3, 4, 5])

# print(s1 & s2)  # OrderSet([3, 4])
# print(s1 | s2)  # OrderSet([1, 2, 3, 4, 5])
# print(s1 ^ s2)  # OrderSet([1, 2, 5])

# if OrderSet([1, 2, 3]) != s1:
#     print("不相等")
# else:
#     print("相等")

# if s2 == OrderSet([3, 4, 5]):
#     print("s2 == OrderSet([3, 4, 5])")

# if 2 in s1:
#     print('2 in s1')

