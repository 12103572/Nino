# 回顾：
#     函数的参数：
#         实参(给)
#             位置传参
#                 序列传参
#             关键字传参
#                 字典关键字传参
#             例：
#                 fx(1,2,3) 位置传参
#                 fx(*"abc")序列传参
#                 fx(a=1,b=2,c=3)关键字传参
#                 fx(**{"c":3,"b":2,"a":1}) 字典关键字传参
#         形参(接收)
#             接收的实参的引用关系(并不会复制对象)
#             缺省参数：
#                 def fx(a=10,b=20,c=30):
#                     pass
#             形参的定义
#                 位置形参
#                 *元组形参
#                 命名关键字形参
#                 **字典形参
#             def fx(a,b,*args,c,d,**kwargs)
#     全局变量 和 局部变量
#         全局变量：
#             .py文件内，函数外部的变量
#         局部变量：
#             函数内部的变量

# 练习:
#     写一个计算公式的解释执行器，已知有如下一些函数
#         def myadd(x,y):
#             return x + y
#         def mysub(x,y):
#             return x - y
#         def mymul(x,y):
#             return x * y
#         ...
#     另有一个函数get_func,有一个参数op 代表用给定的字符串:
#         def get_func():
#             ...
#     此函数在传入字符串"加”或“+”，时返回myadd 函数
#     此函数在传入字符串"减”或“-”，时返回myadd 函数
#     ...
#     在主函数中:
#     def main():
#         while True:
#             s=input("请输入计算公式：") #10 +20
#             L=s.split('')  #L=['10','加’，‘20’]
#             a=int(L[0])
#             b=int(L[2])
#             fn=get_func(L[1])
#             print("结果是：",fn(a,b)) #结果是：30

# def myadd(x, y):
#     return x + y
# def mysub(x, y):
#     return x - y
# def mymul(x, y):
#     return x * y
# def mychu(x,y):
#     return x / y
# def get_func(op):
#     if op == "加" or op == "+":
#         return myadd
#     elif op == "减" or op == "-":
#         return mysub
#     elif op == "乘" or op == "*":
#         return  mymul
#     elif op == "除" or op == "/":
#         return mychu
# def main():
#     while True:
#         s=input("请输入计算公式：")
#         L=s.split(' ')
#         a=int(L[0])
#         b=int(L[2])
#         fn=get_func(L[1])
#         print("结果是：",fn(a,b))
# main()


# 练习:
#     用全局变量记录一个函数 hello 被调用的次数，部分代码如下：
#         count=0
#         def hello(name):
#             print("你好")
#         hello("校长")
#         while True:
#             s=input("请输入姓名：")
#             if not s:
#                 break
#             hello(s)
#         print("hello函数调用的次数是",count)
# count=0
# def hello(name):
#     print("你好",name)
#     global count
#     count+=1
# hello("校长")
# while True:
#     s=input("请输入姓名：")
#     if not s:
#         break
#     hello(s)
# print("hello函数调用的次数是",count)

# 练习:
#     写一个lambda 表达式:
#     fx= lambda n:,...
#     此表达式创建一个函数，判断n这个数的2次方+1能否被5整除，
#     如果能整除返回True,否则返回False
#     如:
#     print(fx(3))   #True
#     print(fx(4))   #False
# fx = lambda n: (n**2+1)%5==0
# print(fx(3))
# print(fx(4))

# 2.写一个lambda表达式来创建函数，此函数返回两个参数的最大值
#     def mymax(x,y):
#         ...
#     mymax= lambda..
#     print(mymax(100,200))       #123
#     print(mymax("ABC","123")) #ABC
# mymax=lambda x,y: max(x,y)
# print(mymax(100,200))
# print(mymax("ABC","123"))

# 练习:
#     1. 看懂下面的程序在做什么?
#     def fx(f,x,y):
#         print(f(x,y))
#     fx((lambda a,b:a+b),100,200)
#     fx((lambda a,b:a ** b),3,4)
#     #程序直到此处有几个全局变量？
#     2.写一个函数 mysum(x) 来计算：
#     1+2+3+4...+x 的和，并返回
#     (要求：不允许调用 sum 函数)
#     如：
#         print(mysum(100)) #5050
#     3.写一个函数 myfac(n) 来计算 n！(n的阶乘)
#     n！ = 1*2*3*4...*n
#     如:
#         print(mafac(5))  #120
#     4.写一个函数计算 1+2**2+3**3+...n**n的和
#     (注:n 给个小点的数)
#     5.实现有界面的学生信息管理程序
#     选择菜单如下:
#     +----------------------------------+
#     | 1) 添加学生信息                    |
#     | 2) 显示学生信息                    |
#     | 3) 删除学生信息                    |
#     | 4) 修改学生成绩                    |
#     | q) 退出                           |
#     +----------------------------------+
#     请选择：
#         学生信息和存储方法与原程序相同:用列表里包含来存信息
#         要求:每个功能写一个函数与之相对应

# 1.
# def fx(f,x,y):
#     print(f(x,y))
# fx((lambda a,b:a+b),100,200)
# fx((lambda a,b:a**b),3,4)
# print(globals())
# 2.
# def mysum(x):
#     s=0
#     for i in range(x+1):
#         s = s +i
#     return s
# print(mysum(100))

# 3.
# def myfac(n):
#     s=1
#     for x in range(1,n+1):
#         s=s*x
#     return s
# print(myfac(9))

# 4.
# def dyy(n):
#     s=0
#     for x in range(1,n+1):
#         s=s+x**x
#     return s
# print(dyy(3))

# 5.
# def choice():
#     print("欢迎进入学生管理界面")
#     print("+"+"-"*32+"+")
#     print("|"+"1) 添加学生信息".center(26)+"|")
#     print("|" + "2) 显示学生信息".center(26) + "|")
#     print("|" + "3) 删除学生信息".center(26) + "|")
#     print("|" + "4) 修改学生信息".center(26) + "|")
#     print("|" + "q) 退出 ".center(21) +" "*9+ "|")
#     print("+" + "-" * 32 + "+")
#     s=input("请输入您选择的选项")
#     if s=="1":
#         add()
#     if s=="2":
#         show(L)
#     if s=="3":
#         del1()
#     if s=="4":
#         alter()
#     if s=="q":
#         return
# def add():
#     while True:
#         a=input("请输入学生姓名")
#         if a =="":
#             break
#         D={}
#         b=input("请输入学生性别")
#         c=input("请输入学生年龄")
#         d=input("请输入学生成绩")
#         D["姓名"]=a
#         D["性别"]=b
#         D["年龄"]=c
#         D["成绩"]=d
#         L.append(D)
#     return L
# #此函数用于显示学生信息
# def show(L):
#     print("+"+"-"*16+"+"+"-"*16+"+"+"-"*16+"+"+"-"*16+"+")
#     print("|"+"姓名".center(13)+"|"+"性别".center(13)+"|"+"年龄".center(13)+"|"+"成绩".center(13)+"|")
#     print("+" + "-" * 16 + "+" + "-" * 16 + "+" + "-" * 16 + "+" + "-" * 16 + "+")
#     for x in L:
#         print("|"+x["姓名"].center(13)+"|"+x["性别"].center(13)+"|"+str(x["年龄"]).center(13)+"|"\
#               +str(x["成绩"]).center(13)+"|")
#     print("+" + "-" * 16 + "+" + "-" * 16 + "+" + "-" * 16 + "+" + "-" * 16 + "+")
# #此函数用于删除学生信息
# def del1():
#     while True:
#         flag='1'
#         a = input("请输入要删除信息的学生姓名")
#         for x in L:
#             if x['姓名']==a:
#                 b=L.index(x)
#                 L.pop (b)
#                 flag='2'
#                 print("删除成功！")
#                 break
#         else:
#             print("没有此学生")
#             break
#         if flag=='2':
#             break
# #此函数用于修改学生成绩
# def alter():
#     while True:
#         a=input("请输入要修改的学生信息")
#         for x in range(len(L)):
#             if a==L[x]["姓名"]:
#                 L[x]["性别"]=input("请输入新的性别")
#                 L[x]["年龄"]=input("请输入新的年龄")
#                 L[x]["成绩"]=input("请输入新的成绩")
#                 print("修改成功！")
#                 break
#             else:
#                 print("您输入的姓名有误，请重新输入!")
#                 break
# L=[]
# while True:
#     choice()




