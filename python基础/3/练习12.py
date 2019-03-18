# 回顾：
# 函数式编程
#     推荐写小函数，用小函数构建大型程序
# 函数的可重入性
#     函数里如果没有使用除局部变量以外的变量，则此函数必然为
#     可重入函数
# 高阶函数
#     1.有一个函数作为参数传入的函数
#     2.函数返回另一个函数
# 三个内建的高阶函数
#     map,filter,sorted
#     map（func,*args(iterables)） 用多个可迭代对象生成一个可迭代对象
#     filter(func,iterable)  过滤
#     sorted(iterable,key=None,reverse=False) 排序   返回排序后的列表
# 递归 recursion
#     函数直接或间接的调用自身
#     优点:
#         把问题简单化
#     缺点:
#         受递归的层数限制
#         占用内存
# 闭包 closure
#     一个函数引用了外部嵌套函数的变量
#     特点:
#         封闭外部嵌套函数中的变量，只让当前函数可见
#         闭包创建函数(外部嵌套函数)中的变量会延长生命周期
#     缺点:
#         占用内存大，不会释放

# 练习：
#     1.写一个程序，输入圆的半径，打印出这个圆的面积
#     2.输入一个圆的面积，打印出这个圆的半径
#         (要求:用math模块里的函数实现，详见：help(math))
# 1.
# import math as m
# r=float(input("请输入圆的半径"))
# area=m.pi * r ** 2
# print("这个圆的面积是：",area)
# 2.
# n=float(input("请输入圆的面积"))
# r=m.sqrt(n/m.pi)
# print("这个圆的半径是：",r)

# import time
# print("这是第一句，十秒后打印第二句")
# time.sleep(15) #让程序睡眠10秒钟，然后再继续
# print("这是第二句")

# 练习：
#     写一个程序，输入你的生日(年 月 日)
#         1)算出你已经出生了多少天
#         1)算出你出生那天是星期几？
# import time
# year=int(input("请输入您出生的年："))
# month=int(input("请输入您出生的月："))
# day=int(input("请输入您出生的日："))
# born=(year,month,day,0,0,0,0,0,0)
# #计算出生时计算机的内部时间描述
# born_second=time.mktime(born)
# #再计算出生的时长（单位为秒）
# life_second=time.time() - born_second
# life_day=life_second / 60 /60 //24
# print("您已出生:",life_day,"天")
# week={
#     0:'一',
#     1:'二',
#     2:'三',
#     3:'四',
#     4:'五',
#     5:'六',
#     6:'日',
# }
# #得到出生时的时间元组
# born=time.localtime(born_second)
# print("您出生的那天是星期",week[born[6]])

# 练习：
#     1.写一个程序，以电子时钟的格式打印时间:
#     格式为:
#         HH:MM:SS
#     如：
#     17：51:20
#     时间自动变化
#     2.编写一个闹钟程序，启动时设置定时时间，到时间后打印一句
#     “时间到！！！”然后退出程序
#     3.编写函数fun 基本功能是计算下列多项式的和
#     Sn=1+1/1!+1/2!....+1/n!
#     （建议用数学模块中的factorial）
#     求当n得20时，Sn的值
#     即：
#     print(fun(20))  #2.718281828...
# # 1.
# import time
# while True:
#     t=time.localtime()
#     print("%02d:%02d:%02d"%t[3:6])
#     time.sleep(1)
# 2.
# def run_alarm(hour,minute):
#     #此函数用来等待时间，当时间开始与设定时间相等时退出此函数
#     import time
#     while True:
#         t=time.localtime()
#         print("%02d:%02d:%02d"%t[3:6])
#         if t[3:5]==(hour,minute):
#             return
#         time.sleep(1)
# h=int(input("请输入定时的小时"))
# m=int(input("请输入定时的分钟"))
# run_alarm(h,m)
# print("时间到！！！")
# 3.
# def fun(n):  #创建一个阶乘和的函数
#     Sn=0      #创建变量以便求和
#     for x in range(n+1):  #遍历所有的分母
#         import math     #创建数学模块
#         Sn=Sn+1/math.factorial(x)  #用数学模块中的阶乘求出阶乘的和
#     return Sn  #返回和
# print("Sn的值是:",fun(20))  #得出当n得20时，Sn的值
# import math
# print(sum(map(lambda x:1/math.factorial(x),range(20))))
#
# def sumfun(fn):
#     def fun1(n):
#         print("+++++++++++")
#         fn(5)
#         print("-----------")
#     return fun1
# @sumfun
# def fun(x):
#     s=0
#     for x in range(1,10):
#        s=s+x
#     print("结果是：",s)
# # fun=sumfun(fun)
# fun(5)
# import time
# while True:
#     t=time.localtime()
#     print("%02d:%02d:%02d"%t[3:6])
#     time.sleep(1)
# import time
# def short_up(h,m):
#     while True:
#         t=time.localtime()
#         print("%02d:%02d:%02d"%t[3:6])
#         time.sleep(1)
#         if t[3:5]==(h,m):
#             return
# h=int(input("请输入停止的小时"))
# m=int(input("请输入停止的分钟"))
# short_up(h,m)
# print("时间到了！！！")






