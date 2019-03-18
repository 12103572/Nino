'''
回顾:

装饰器  decorators
    装饰器本身是一个函数，通常是带有一个参数的函数
    作用是用来包装另一个函数或者类
语法:
    def 装饰器函数(fn):
        创建一个闭包函数
        def fx(形参列表同被装饰函数的形参列表):
            ...
            fn(实参)   #内部调用fn
            ...
        return fx
@装饰器函数
def myfun(a,b,c):
    ...
myfun(1,2,3)

函数的文档字符串
    def fa():
        """这是函数的文档字符串"""
        主要用于函数的注释
    fa.__doc__ 属性
        用来记录文档字符串

模块  module
    模块包含:函数，数据，类

    导入方式:
    import 语句
        在当前作用域创建一个变量来绑定 模块
    from xxx import  [as 变量名]语句
        在当前作用域创建一个或多个变量来绑定模块里的函数或数据
    from import * 语句
        创建多个变量，绑定模块里的所有函数和数据

内建模块
    math 模块
        math.e
        math.pi
        math.factorial(x)
    time 模块

'''

# import mymod
# mymod.myfac(5)
# mymod.mysum(100)
# print(mymod.name1)
# from mymod import name2
# print("name2=",name2)
# from mymod import *
# myfac(20)
# import imp
# imp.reload(mymod)
# print(name2)
# print(mymod.__doc__)
# print("mymod,__name__ 值为：",__name__)

# 练习：
#     1.猜数字游戏：
#     随机生成一个0~100之间的整数，用变量X绑定
#     让用户输入一个数用变量y绑定，然后输出猜数字的结果
#     1）如果y等于生成的数x，则提示用户"恭喜您猜对了”，并退出程序
#     2）如果y大于x则提示：您猜的数字大了，然后继续猜
#     3）如果y小于x，则提示：您猜小了，然后继续猜
#     知道猜对为止，最后显示用户猜数字的次数\

# import random as R
# x=R.randint(0,100)                      #先用随机模块生成一个数字，用变量X绑定
# count=0                                 #创建一个变量用来记录猜的次数
# while True:                             #不确定猜了多少次所以用循环
#     y=int(input("请输入0~100之间的整数"))
#     count+=1   #每猜一次，猜的次数+1
#     if x==y:
#         print("恭喜您猜对了!!!")
#         break   #猜对后退出程序
#     elif x<y:
#         print("您猜的数字大了，请继续")
#     elif x>y:
#         print("您猜的数字小了，请继续")
# print("您一共猜了%d次！！！"%count) #%d,代表整数，%count代表猜了几次

# 练习：
#     1.写一个程序，模拟斗地主发牌，牌共54张
#     种类有:黑桃('\u2660'),梅花('\u2663')，红桃('\u2665'),方块('\u2666')
#     数字有:A2-10JQK
#     大王和小王
#     输入回车，打印第1个人的17张牌
#     输入回车，打印第2个人的17张牌
#     输入回车，打印第3个人的17张牌
#     输入回车，打印最后3张底牌
#     2.将学生信息管理系统程序拆分为模块
#     要求:
#         1).主事件循环的main函数放在 main.py 中
#         2).显示菜单的函数 show_menu 放在 menu.py中
# #         3).与学生信息操作相关的函数放在student_info。py中
# L=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
# L1=['\u2660','\u2663','\u2665','\u2666']
# L2=["小王","大王"]
# for x in L: #遍历列表中的元素，添加四种花色
#     for y in L1:
#         L2.append(x+y)
# import random as R
# R.shuffle(L2)  #用随机模块让54张牌打乱顺序
# count=0 #创建一个变量记录空格的个数
#
# while True:
#     kongge=input("请输入回车") #通过输入空格来发牌
#     count+=1
#     if count==1:                        #下面是通过索引来拿到三人的牌和留下底牌
#         print("第1个人的牌是：",L2[:17],"共",len(L2[:17]),"张")
#     if count==2:
#         print("第2个人的牌是：",L2[17:34],"共",len(L2[17:34]),"张")
#     if count==3:
#         print("第3个人的牌是：", L2[34:51],"共",len(L2[34:51]),"张")
#     if count==4:
#          print("底牌是：", L2[51:],"共",len(L2[51:]),"张")
#          break


