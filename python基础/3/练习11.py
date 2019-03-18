 # 回顾：
 #    全局变量
 #        一但创建不会自己销毁，需要用del 语句销毁
 #    局部变量
 #        在函数调用时（过程中）创建，自动销毁
 #    globals
 #        返回全局变量的字典
 #    locals
 #        返回局部变量的字典
 #    函数变量
 #        函数名是变量，它在创建时绑定一个“函数”
 #        函数可以作用形参传入另一个函数
 #        函数可以作为另一个函数的返回值
 #        函数嵌套定义
# def f1():
#     def f2():
#         print("hello")
#     return f2
# fx=f1()
# fx()  # hello
# 示例2:
# def fn(fx):
#     print("fn被调用")
#     return fx
# m= fn(max)
# print(m(1,2,3))
# m  is  max
# 作用域
#     局部作用域
#     外部嵌套函数作用域
#     全局作用域(模块内)
#     内建(内置)函数作用域
# global 语句
#  声明 为全局作用域
#     global v
# nonlacal 语句
#  声明为外部嵌套函数作用域
# lambda 表达式
#     创建函数的表达式
#     主要是用来创建简单函数
#     lambda x,y,*args,**kwargs: x + y +sum(args)
# eval
#     把字符串当成表达式来运行，返回表达式的运行结果
# exec
#     把字符串当成 python 语言的程序 来运行

# 练习:
#     1.求1**2+2**2+3**2+....+9**2的和
#     2.求1**3+2**3+3**3+....+9**3的和
#     3.求1**9+2**8+3**7...+9**1的和
# 1.
# L=[]
# def sum1(x):
#     return x**2
# for x in map(sum1,range(1,10)):
#     L.append(x)
# print(sum(L), end=" ")
# # 方法2：
# s=sum(map(lambda x:x**2,range(1,10)))
# print(s)
# 2.
# s=0
# for x in map(lambda x:x**3,range(1,10)):
#     s=s+x
# print(s)
# 3.
# def sum3(x,y):
#     return x**y
# for x in map(sum3,range(1,10),range(9,0,-1)):
#     print(x,end=" ")
# print()
#方法2：
# print(sum(map(pow,range(1,10),range(9,0,-1))))

# 练习:
#     用filter函数将1~100之间所有的素数prime存放于列表中
# def  prime(x):
#     if x<2:
#         return False
#     for i in range(2,x):
#         if  x % i ==0:
#             return False
#     return True
# L=list(filter(prime,range(2,100)))
# print(L)

# 练习:
#     将下列列表中的数据进行排序
#     L=[(1,5),(3,9),(4,1),(3,6)(5,3)]
#     1.将列表内的五个元组，按第二个数据的从小到大的顺序进行排序
#     结果如下:
#     L=[(1,5),(3,9),(4,1),(3,6)(5,3)]
# 2.将列表内的五个元组按第二个数的从大到小顺序进行排序，
#     打印排序之后的结果
# 3.假设元组中的数据是数学直角坐标系的坐标，则按他们距离原点
#     的距离进行排序
# 1.
# L=[(1,5),(3,9),(4,1),(3,6),(5,3)]
# def second_value(t):
#     return t[1]
# print(sorted(L,key=second_value))
# 2.
# print(sorted(L,key=second_value,reverse=True))
# 3.
# def distance(x):
#     return x[0]**2+x[1]**2
# print(sorted(L,key=distance,reverse=True))

# 练习:
#     试写一个递归函数 mysum(n),此函数用递归方式求
#     1+2+3...+n 的和
#     def musum(n):
#         ...
#     print(mysum(100))
# def mysum(n):
#     if n==1:
#         return 1
#     s=n+mysum(n-1)
#     return s
# print(mysum(100))

# 2.已知有五位朋友在一起:
# 第五个人说他比第四个人大2岁
# 第四个人说他比第三个人大2岁
# 第三个人说他比第二个人大2岁
# 第二个人说他比第1个人大2岁
# 第一个人说它十岁
# # 写函数get_age(n)求，第三个人几岁，第五个人几岁
# def get_age(n):
#     if n ==1:
#         return 10
#     return get_age(n-1)+2
# print(get_age(2))
# print(get_age(10))

# def give_yasui_money(m):
#     money = m
#     def child_buy(obj,m):
#         nonlocal money
#         if money > m:
#             money = money - m
#             print("买",obj,"花了",m,"元","剩余",money)
#         else:
#             print("买",obj,"失败")
#     return child_buy
# cb=give_yasui_money(1000)
# cb("变形金刚",200)
# cb("漫画三国",100)
# cb("手机",1300)

 # 练习：
 # 1.
 # 已知有列表
 # 递归
 # L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
 # 1)写一个函数
 # print_list(lst)
 # 打印出所有的数字
 # 如：
 # print_list(L)
 # # 打印 3,5,8,10,13,14,15,18,20
 # 2)写一个函数
 # sum_list(lst)
 # 返回列表中所有数字的和
 # 如:
 # print(sum_list(L))  # 106
 # 注: type(x)
 # 函数可以返回一个对象的类型
 # 如: type(20) is int  # True
 # type([1, 2, 3]) is list  # True
 # 2.
 # 写程序求出1
 # ~20
 # 阶乘的和
 # 即1！+2！!+3！..+20！
 #
 # 3.
 # 改写之前的学生信息管理程序，添加如下四个功能：
 # 5) 按学生成绩高低显示学生信息
 # 6) 按学生成绩低高显示学生信息
 # 7) 按学生年龄高低显示学生信息
 # 8) 按学生年龄低高显示学生信息
 # 1.1)
# L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
# def sumlist(lst):
#     #先循环遍历列表中的每个元素
#     #如果是数字则打印#
#     # 如果是列表，则打印这个列表sumlist
#     for x in lst:
#         if type(x) is int:
#             print(x,end=" ")
 #         else:
 #             sumlist(x)

# sumlist(L)
# print()
# # # 1.2)
# L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
# def sum_list(lst):
#     s=0
#     for x in lst:  #遍历列表中所有的数据
#          if type(x) is int:#x是整数，则加到s中
#             s=s+x
#          else:  #说明x是列表
#             s=s+sum_list(x)
#     return s
# print(sum_list(L))

# 2.
# def jc(m):
#         if m==1:
#             return 1
#         if m>1:
#             return jc(m - 1) * m
# print(sum(map(jc,range(1,21))))
# import math
# print(sum(map(acmath.ftorial,range(1,21))))







