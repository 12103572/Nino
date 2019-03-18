# # 回顾:
# 两个容器类
#     set 集合(可变)
#         set() /set(iterable)
#             1,2,3}
#     集合推导式 {x for x in range(10)}
#     frozenset  固定集合(不可变)
#         frozenset/frozenset(iterable)
#     集合和固定集合运算：
#         & 交集运算 |并集 -补集  ^对称补集 < 子集  >超集
#         &=  |=  ^=  -=
#         <= >= == !=
#         in /not in
#         is / is not(全部可用)
#     函数:
#         len(x) max(x) min(x) sum(x) any(x)  all(x)
#     方法：
#         S.add(x)  添加
#         S.remove(x)  删除
#         S.discard(x)  删除（不报错误）
#         S.copy()       复制
#         S.clear()       清空
#         S.update(s2)    S&s2
#     所有的容器类都是可迭代对象
#         list str tuple set frozenset dict   bytes  bytearray
#     函数 function
#     def 语句
#         作用:
#             封装语句块，把一些语句看成功能整体
#         语法：
#             def 函数名(形参列表):
#                 语句块
#                 return None
#     return 语句()
#         作用:
#             结束当前函数的执行，返回到调用此函数的地方，同时返回
#             一个对象的引用关系(默认返回None)
#         语句:
#             return [表达式]
#         函数调用:
#             函数名(实际调用传参)
# ()的用法
#     (1+2)分组子表达式
#     (1,2,3)创建元组
#     max(1,2,3)调用max函数

# 练习:
#     写一个函数myadd,此函数可以计算两个数，三个数和四个数的和
#     如：
#         def myadd(...):
#             ...and
#         print(myadd(10,20))       #30
#         print(myadd(100,200,300)) #600
#         print(myadd(1,2,3,4))     #10
# def myadd(a,b=0,c=0,d=0):
#     return a + b + c + d
# print(myadd(10,20))
# print(myadd(100,200,300))
# print(myadd(1,2,3,4))

# def func(*args):
#     print("实参的个数是：", len(args))
#     print("args=", args)
# func()
# func(1, 2, 3, 4)
# func(1, 2, 3, 4, 'AAA', 'BBB')
# func(*"ABCDEFG")

# 练习:
#     写一个函数mysum　可以传入任意个数字实参，返回所有实参的和
#     如：
#         def mysum(...):
#             ...
#         print(mysum(1,2))
#         print(mysum(1,,2,3,4))
#         print(mysum(1,2,34,5,6,7,8))
# def mysum(*args):
#     print("和是：",sum(args))
# mysum(1,2)
# mysum(1,2,3,4)
# mysum(1,2,3,4,5,6,7,8)


# 练习:
#     已知内建函数　max的帮助文档是:
#     >>> help(max)
#     max(iterable)
#     max(arg1,arg2,args)
#     仿造max写一个mymax函数，功能与max函数完全相同
#     （要求:不允许调用max函数）
#     print(mymax([6,8,5,3]))  #8
#     print(mymax(100,200))  #200
#     print(mymax(1,2,5,9,7)) #9
# 方法一:print(mymax()) 是bug
# def mymax(*args):
#     # print(args)
#     #判断实参是一个可迭代对象，还是多个数据
#     if len(args)==1:#args里是一个可迭代对象
#         # 如：args=([6,8,5,3])
#         iterable=args[0]  #把可迭代对象取出
#         zuida=iterable[0]
#         for x in iterable:  #一次从第一个和zuida进行比较
#             if x>zuida:
#                 zuida=x
#         return zuida #返回最大值
#     elif len(args)>1:  #args里是两个或两个以上的数据
#         zuida=args[0]
#         for x in args:  #遍历所有实参
#             if x >zuida:
#                 zuida=x
#         return zuida
# print(mymax([6, 8, 5, 3]))  # 8
# print(mymax(100,200))  #200
# print(mymax(1,2,5,9,7)) #9
# 方法2.
# def mymax(a,*args):
#     if len(args)==0:
#         zuida=a[0]
#         for x in a:
#             if x>zuida:
#                 zuida=x
#         return zuida
#     elif len(args)>0:
#         zuida=a
#         for x in args:
#             if x >zuida:
#                 zuida=x
#         return zuida
# print(mymax([2,4,6,7,9]))
# print(mymax(1,16,1,2,5,6,7,9,))
# print(mymax([6,8,5,3]))
# print(mymax(100,200))
# print(mymax(1,2,5,9,7))
# 方法3：用max函数
# def mymax(a,*args):
#     if len(args)==0:
#         return max(a)
#     elif len(args)>0:
#         return max(a,max(args))
# print(mymax([2,4,6,7,9]))
# print(mymax(1,16,1,2,5,6,7,9,99))
# 方法4：用max函数
# def mymax(a,*args):
#     if len(args)==0:
#         return max(a)
#     elif len(args)>0:
#         return max(a,*args)#把args绑定的元组拆开再按位置传参
# print(mymax([2,4,6,7,9]))
# print(mymax(1,16,1,2,5,6,7,9,99))
# print(mymax([2,4,6,7,9]))
# print(mymax(1,16,1,2,5,6,7,9,))
# print(mymax([6,8,5,3]))
# print(mymax(100,200))
# print(mymax(1,2,5,9,7))

# 练习:
# 1.写一个函数　isprime(x)判断x是否是素数,如果为素数则返回
#     Ture,否则返回False
# 2.写一个函数prime_m2n(m,n),返回从m开始,到n结束范围内
# 全部的素数(不包含n),返回这些素数的列表,并打印
# 如:
#     L＝prime_m2n(10,20)
#     print(L)  #[11,13,17,19]
# 3.写一个函数primes(n),返回指定范围内n(不包含n)的全部素数的
# 列表，并打印这些素数的列表
# L=primes(10)
# print(L)  #[2,3,5,7]
# 1)　打印100以内的全部素数
# 2)　打印100~200之间全部的素数的和


# 练习:
# 1.写一个函数　isprime(x)判断x是否是素数,如果为素数则返回
#     Ture,否则返回False
# 2.写一个函数prime_m2n(m,n),返回从m开始,到n结束范围内
# 全部的素数(不包含n),返回这些素数的列表,并打印
# 如:
#     L＝prime_m2n(10,20)
#     print(L)  #[11,13,17,19]
# 3.写一个函数primes(n),返回指定范围内n(不包含n)的全部素数的
# 列表，并打印这些素数的列表
# L=primes(10)
# print(L)  #[2,3,5,7]
# 1)　打印100以内的全部素数
# 2)　打印100~200之间全部的素数的和
# 4.改写之前的学生信息管理程序,将程序改为两个函数:
# def input_student():
#         ...#此函数用于获取学生的信息，形成包含有字典的列表
#         然后返回此列表
# def output_student(L):
#         ...#此函数以列格的形式打印学生信息的列表
# 测试(实现与之前相同的功能):
# infos=input_student()
# print(infos)
# # output_student(infos)

# 1.
# def isprime(x):
#     if x<2:
#         return False
#         # 能走到此处，x一定大于等于2
#     for n in range(2,x):
#         if x%n==0:
#             return False
#     return True
# x = int(input("请输入一个大于等于2的整数"))
# print(isprime(x))

# 2.
# def prime_m2n(m,n):
#     L=[]
#     for x in range(m,n):
#         if isprime(x):
#             L.append(x)
#     return L
# L=prime_m2n(10,20)
# print(L)
# 方法2：
# def prime_m2n(m,n):
#     return [x for x in range(m,n) if isprime(x)]
# print(prime_m2n(10,20))

# 3.
# def primes(n):
#     L=[]
#     for x in range(2,n):
#         if isprime(x):
#             L.append(x)
#     return L
# L=primes(100)
# print(L)
# print(sum(prime_m2n(100,200)))
# 方法2：
# def prinmes(n):
#     return prinme_m2n(0,n)
# print(prime_m2n(0,100))
# print(sum(prime_m2n(100,200)))

# 4.
# L = []
# def input_srudent():
#     while True:
#         d={}
#         a=input("请输入学生的姓名")
#         if a=="":
#             break
#         b=input("请输入学生的年龄")
#         c=input("请输入学生的成绩")
#         d["姓名"]=a
#         d["年龄"]=b
#         d["成绩"]=c
#         L.append(d)
#     return L
# infos=input_srudent()
# print(infos)
# def output_student(L):
#     print("+"+"-"*16+"+"+"-"*16+"+"+"-"*16+"+")
#     print("|"+'姓名'.center(14)+"|"+'年龄'.center(14)+"|"+'成绩'.center(14)+"|")
#     print("+" + "-" * 16 + "+" + "-" * 16 + "+" + "-" * 16 + "+")
#     for x in L:
#         print("|"+x["姓名"].center(13)+"|"+str(x["年龄"]).center(16)+"|"+str(x["成绩"]).center(16)+"|")
#     print("+" + "-" * 16 + "+" + "-" * 16 + "+" + "-" * 16 + "+")
# output_student(infos)




