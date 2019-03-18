# 回顾：
#     两个容器：
#     元组tuple（不可变的列表）  字典 dict
#     元组的创建
#         ()  20, (20,)  (1,2,3,) 1,2,3,3
#         构造函数：tuple()    tuple(可迭代对象)
#
#         运算：
#             + += * *=
#             元组的比较运算:
#                 < <= > >= == !=
#                 同列表的比较规则完全相同
#             in/not in 运算
#             索引，切片
#             t(1)        t[1:10:2]
#             元组的方法：
#                 t.index(value[,begin[,end]])
#                 T.count(x)      返回元素个数
# 字典： dict
#     可变的，无序的，容器
#     键key-   值(value)  对
#     (不可变) (任意类型)
#     字典的创建方式：
#         字面值
#         {},{1:'一'} {1:1,2:2}
#         构造函数
#             dict()  dict(可迭代对象)，dict(关键字传参)
#         推导式
#             {键表达式：值表达式 for 变量 in 可迭代对象1  if 真值表达式}
#             dict={x:d[x] for x in L}
#         添加和修改字典的键值对
#         d[键]=值表达式
#         删除字典的键
#             del d[键]
#         查看字典的键对应的值
#             value =d[键]
#         字典是可迭代对象(可以迭代取出字典的键)
#
# 可迭代对象能用在什么地方：
#     for 变量 in 可迭代变量
#         ...
#     推导式中
#     [表达式 for 变量 in 可迭代对象]
#     in/not in 运算
#     比较运算：
#     == !=
#     函数：
#     len(x)  max(x) min(x) sum(x)  any(x)    all(x)
#     字典的方法:
#         D.clear()   {}
#         D.pop(key) 返回值
#         D.copy()      浅拷贝
#         D.update(d2)    添加d2到D，如果键重复，值变为d2的值
#         D.get(key,default=None) #D[key] 判断 key是否在D，有返回值，没有，返回dedaulr=None
#         D.keys()    返回所有键
#         D.values()  返回所有值
#         D.items()   返回所有键值对

# 练习:
#     经理有: 曹操.刘备，孙权
#     技术员有：曹操，孙权，张飞，关羽
#     用集合求：
#         １，既是经理也是技术员的有谁？
#         ２．是技术员，但不是经理的人有谁》
#         ３．是经理，但不是技术员的有谁？
#         ４．张飞是经理么？
#         ５．身兼一职的有谁？
#         ６．经理和技术人员共有几个人
# s1={"曹操","孙权","刘备"}
# s2={"曹操","孙权","张飞","关羽"}
# print(s1 & s2)
# print(s2  - s1)
# print(s1-s2)
# print("张飞" in  s1)
# print(s1 ^ s2)
# print(len(s1|s2))
#
# def say_hello():
#     print("hello world!")
#     print("hello china!")
#     print("hello tarena!")
#
# say_hello()
# say_hello()
# say_hello()

# 练习:
#     写一个函数myadd,此函数中的参数列表离有两个参数x,y
#     此函数的功能是打印调用参数的和，即 x + y
#     如:
#     def myadd(...):
#     ... # ...部分自己能实现
#     #调用：
#         myadd(100,200):  #300
#         myadd("ABC","123")  #ABC123
# def myadd(x,y):
#     print(x + y)
# myadd(100,200)
# myadd("ABC","123")

# 2.
# 写一个函数　print_even, 传入一个参数n代表终止的整数
# (注：不包含n)，此函数打印：
# ０　２　４　６　８到　n
# 为止的全部偶数
# 如：
# print_even(n):
# ...  # 此处自己实现
# # 调用
# print_even(10)　　  # 打印　０　　２　　４　６８
# def print_even(n):
#     for n in range(n):
#         if n %2==0:
#             print(n,end=" ")
# print_even(10)
# print_even(50)

# def say_hello2():
#     print("hello aaa")
#     print("hello bbb")
#     return[1,2,3,4]
#     print("hello ccc")
# v = say_hello2()
# print("v=", v)
# v2= say_hello2()
# print("v2=", v2)

# 练习：
#     1.写一个函数mymax,实现返回两个数的最大值：
#     如：
#         def mymax(a,b):
#             ...#此处自己实现
#         print(mymax(100,200) #300
#         print(mymax("ABC","ABCD")) #ABCD
# def mymax(a,b):
#     zuida=a
#     if zuida <b:
#         zuida=b
#     return zuida
# print(mymax(100,200))
# print(mymax("ABC","ABCD"))
# def mymax(a,b):
#     return max(a,b)
# print(mymax(100,200))
# print(mymax("ABC","ABCD"))

# 2.
# 写一个函数myadd，实现给出两个数，但会两个数的和
# 如:
# def myadd(x, y)
#     ...
# a = int(input("请输入第一个数:"))
# b = int(input("请输入第一个数:"))
# print(a, "+", b, "的和是"，myadd(a, b))
# def myadd(x,y):
#     return x+y
# a = int(input("请输入第一个数:"))
# b = int(input("请输入第一个数:"))
# print(a, "+", b, "的和是",myadd(a, b))

# 3.写一个函数 input_number
#     def input_number():
#         ...#此处自己实现
#     此函数用来获取用户循环输入的整数，当输入负数时结束输入
#     将用户输入的数字形成列表的形式返回，再用内建函数max，min，
#     sum，求用户输入的最大值，最小值及和
#     L＝input_number()
#     print("用户输入的最大值是："，max(L))
#     print("用户输入的最大值是："，min(L))
#     print("用户输入的全部数的和是："，sum(L))
# def input_number():
#     l= []
#     while True:
#         a=int(input("请输入整数"))
#         if a<0:
#             return l  #return执行时，此函数的所有语句都不再执行
#         else:
#             l.append(a)
# L=input_number()
# print("用户输入的最大值是：",max(L))
# print("用户输入的最大值是：",min(L))
# print("用户输入的全部数的和是：",sum(L))

# 练习：
# 1.写一个函数　get_chinese_char_count,此函数实现的
#     功能是给定一个字符串，返回这个字符串中中文字符的个数
#     def get_chinese_char_count(s):
#         ...#　此处自己实现
#     s=input("请输入中英文字混合的字符串：")
#     print("您输入的中文字符的个数是：",
#      get_chinese_char_count(s))
#     注:中文字符的编码范围是:0x4E00~0x9FA5（包含）
# 2.定义两个函数：
#     sum3(a,b,c)     用于返回三个数的和
#     pow3(x)         用于返回x的三次方
#     用以下函数计算：
#     1)　计算１的立方＋２的立方＋３的立方的和
#     2)即1**3+2**3+3**3　和(1+2+3)*3
# 3.编写函数fun，其功能是计算并返回下列多项式的值
# Sn=1+1/2+1/3+...1/n
#     def fun(n):
#         ...
#     print(fun(2)  #1.5
#     print(fun(3))  #1.83333333333333
#     print(fun(3))   #????
# 1.
# def get_chinese_char_count(s):
#     count=0
#     for x in s :
#         if 0x4E00<=ord(x)<=0x9FA5:
#             count += 1
#     return count
# s=input("请输入中英文字混合的字符串")
# print("您输入的中文字符的个数是:",
#       get_chinese_char_count(s))

# 2.
# def sum3(a,b,c):
#     return a+b+c
# # print(sum3(1,2,3))
# def pow3(x):
#     return x**3
# # print(pow3(6))
# print("１的立方＋２的立方＋３的立方的和是:",sum3(pow3(1),pow3(2),pow3(3)))
# print("三个数的立方是：",pow3(sum3(1,2,3)))

# 3.
# def fun(n):
#     Sn=0
#     for x in range(1,n+1):
#         Sn=1/x+Sn
#     return Sn
# print(fun(2))
# print(fun(3))
# print(fun(10))



