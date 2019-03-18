'''回顾：
    文件 file
        用来长期存储数据
        以字节为单位进行顺序存储
    文件的操作步骤
        1.打开:
            open(文件名，默认是"rt")
        2.读写：
            读：
                F.read(n)
                F.readline()
                F.readlines()
            写：
                F.write(字符串或字节串)
                F.writelines(字符串或字节串列表)
        3.关闭：
                F.close()
两种操作方式：
    文本文件操作
        打开模式:"t"
        自动进行编码(write)/解码(read)操作  "utf-8"
        默认将"\r\n" 转换为"\n"
    二进制文件操作
        打开模式："b"
            不会自动编解码，会把文件当成字节串来看待
其他方法：
    F.tell()得到当前的读写位置(整数)
    F.seek(偏移量，相对位置)
    F。fulsh()  清空缓冲区
     缓冲区的作用：
        减少对外部输入输出(I/O)的次数
汉字的编码：
    GB 国际
        GB2312
          GBK
            GB18030(二字节或四字节)
    UINCODE 国际标准
        UNICODE32(四字节)
          WUICODE16(二字节)
        UTF-8 (1~3~6)
编码字符串：
    gbk2312
    gbk
    gb18030
    utf-8
    ASCII
编码注释：
# _*_ coding:utf-8 _*_
        '''


# class Dog:
#     '''这是类的文档字符串，此类用于描述一种小动物行为和属性
#     '''
#     def eat(self, food):
#         print("ID为:",id(self),"小狗正在吃", food)
#     def play(self,plays):
#         print("小狗正在玩",plays)
#     def shangtian(self):
#         print("ID为：",id(self),"小狗正在准备上天")
# dog1 = Dog()  # 用Dog类来创建一个Dog类型的对象
# dog1.eat("骨头")
# dog1.play("皮球")
# Dog.eat(dog1,"狗头")
# dog1.shangtian()
# print(id(dog1))

# dog2 = Dog()  # 用构造函数来创建另一个Dog类型的对象
# dog2.eat("窝窝头")
# # print(id(dog2))
# #
# # lst1=Dog()
# # lst1.eat("狗粮")

# 练习：
#     定义一个"人" 类
#     class Human:
#         def set_info(self,name,age,address="不详")
#         '''此方法为self对象添加姓名，年龄，家庭住址属性'''
#         ......
#         def show_info(self):
#             '''此方法显示某个人(实例)的信息'''
#             ......
# h1 = Human()
# s1.set_info("小张"，20，"郑州市金水区")
# h2 = Human()
# h2.set_info("小李",18)
# h1.show_info() #小张今年20岁，家庭住址：郑州市金水区
# h2.show_info() #小李今年18岁，家庭住址：不详
# class Human:
#     def set_info(self,name,age,address="不详"):
#         self.name=name
#         self.age=age
#         self.address=address
#     def show_info(self):
#         print(self.name, "今年", self.age, "岁，家庭住址：", self.address)
# h1 = Human()
# h1.set_info("小张",20,"郑州市金水区")
# h2 = Human()
# h2.set_info("小李",18)
# h1.show_info() #小张今年20岁，家庭住址：郑州市金水区
# h2.show_info() #小李今年18岁，家庭住址：不详
#
# h3 = Human()

# class Car:
#     '''此类定义一个小汽车类'''
#     def __init__(self,c,b,m):
#         self.color = c
#         self.brand = b
#         self.model = m
#         print(" __init__ 初始化方法被调用!!!")
#     def run(self,speed):
#         print(self.color,"的",self.brand,self.model,"正在以",speed,"公里/小时的速度从我身上碾压过去")
#
# a4 = Car("红色","奥迪","A4")
# a4.run(199)
#
# b5 = Car("买不起的","宝马",'X5')
# b5.run(1.1)
#
# Car("蓝色","宝马",'X5').run(255)

# 练习：
#     写一个学生student类，此类用于描述学生信息，学生信息由
#     姓名，年龄成绩(默认为0)
#     1.为该类添加初始化方法，实现在创建对象时自己自动设置，
#     姓名，年龄，成绩
#     2.添加 set_score 方法能力对象修改成绩信息
#     3.添加show_info方法打印学生对象信息
#     如：
#         class Student:
#             def __init__():
#
#             def get_score():
#
#             def show_info():
#         L = []
#         L.append(Student("小张",20,100))
#         L.append(Student("小李",18,98))
#         L.append(Student("小王",19,))
#         L[2].get_score(80)
#         for s  in L:
#             s.show_info()   #显示每个对象的信息
# class Student:
#     def __init__(self,n,a,s=0):
#         self.name = n
#         self.age = a
#         self.score = s
#     def get_score(self,s):
#         self.score =s
#
#     def show_info(self):
#         print("姓名：",self.name,"年龄",self.age,"成绩",self.score)
# L = []
# L.append(Student("小张",20,100))
# L.append(Student("小李",18,98))
# L.append(Student("小王",19,))
# L[2].get_score(80)
# for s  in L:
#     s.show_info()

# class Car:
#     def __init__(self,info):
#         self.info = info
#         print("汽车：",info,"对象被创建")
#     def __del__(self):
#         print("汽车：",self.info,"对象将被销毁!!!")
# c1 = Car("BYD E6")
#
# # c1 = False
# # c1 = 0
# # c1 = None
# # del c1
# input("请输入回车键继续:")
# print("程序正常退出")

# class Dog:
#     pass
# dog1 = Dog()
# print(dog1.__class__)  #{}
# print(dog1.__class__ is Dog)  #True
# dog2 = dog1.__class__()  #创建一个dog1的同类对象
# print(dog2.__class__)   #<class '__main__.Dog'>

# 练习：
#     有两个人:
#     1.姓名:刘桐     年龄:35
#     2.姓名:李鹏飞   年龄：15
#     行为：
#         1.教别人学东西 teach
#         2.工作赚钱      work
#         3.借钱      borrow(从XXX处借钱)
#         4.显示自己的信息    show_info
#     事情：
#         刘桐教李鹏飞学python
#         李鹏飞教刘桐学王者荣耀
#         刘桐上班赚钱1000元
#         李鹏飞向刘桐借钱200元
#         35岁的刘桐有钱800元，他学会的技能是:王者荣耀
#         15岁的李鹏飞有钱200元，他学会的技能是:pyrhon
#     类的封装如下：
# class Human:
#     def __init__(self,...):
#         ...
#
# liutong = Human("刘桐",35)
# lipengfei = Human("李鹏飞",15)
# class Human:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.money = 0
#         self.skill = []
#     def teach(self,other,subject):
#         print(self.name,"教",other.name,"学",subject)
#         other.skill.append(subject)
#
#     def work(self,money):
#         print(self.name,"上班赚钱",money,"元")
#         self.money += money
#     def borrow_from(self,other,money):
#         print(self.name,"向",other.name,"借钱",money,"元")
#         self.money += money
#         other.money -=money
#     def show_info(self):
#         print(self.age,"岁的",self.name,"有钱",self.money,"元",
#               "他学会的技能是",self.skill)
# liutong = Human("刘桐",35)
# lipengfei = Human("李鹏飞",15)
# liutong.teach(lipengfei,"python")
# lipengfei.teach(liutong,"王者荣耀")
# liutong.work(1000)
# lipengfei.borrow_from(liutong,200)
# liutong.show_info()
# lipengfei.show_info()
# class Human:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.money = 0
#         self.skill = []
#     def  teach(self,other,sbject):
#         print(self.name,"教",other.name,"学",sbject)
#         other.skill.append(sbject)
#     def work(self,money):
#         print(self.name,"工作赚了",money,"元")
#         self.money += money
#     def borrow(self,other,money):
#         print(self.name,"借了",other.name,money,"元")
#         self.money += money
#         other.money -= money
#     def show_info(self):
#         print(self.age,"的",self.name,"有钱",self.money,"元",
#               "他学会的技能是：",self.skill)
# li1 = Human("刘桐",35)
# fei2 = Human("李鹏飞",15)
# li1.teach(fei2,"python")
# fei2.teach(li1,"王者荣耀")
# li1.work(1000)
# fei2.borrow(li1,200)
# li1.show_info()
# fei2.show_info()

# class Human():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.money=0
#         self.skill=[]
#     def teach(self,other,sbject):
#         print(self.name,"教",other.name,"学",sbject)
#         other.skill.append(sbject)
#     def work(self,money):
#         print(self.name,"工作赚了",money,"元")
#         self.money += money
#     def borrw(self,other,money):
#         print(self.name,"向",other.name,"借钱",money,"元")
#         self.money += money
#         other.money -= money
#     def show_info(self):
#         print(self.age,"岁的",self.name,"有钱",self.money,"元",
#               "他学会的技能是：",self.skill)
# zhang3 = Human("张三",16)
# li4 = Human("李4",29)
# zhang3.teach(li4,"python")
# li4.teach(zhang3,"王者荣耀")
# zhang3.work(1000)
# li4.borrw(zhang3,200)
# zhang3.show_info()
# li4.show_info()

# class Student:
#     def __init__(self,name,age,score=0):
#         self.name =name
#         self.age = age
#         self.score = score
#
#     def get_score(self,score):
#         self.score=score
#
#     def show_info(self):
#         print(self.name,"年龄",self.age,"成绩",self.score)
#
#
# L = []
# L.append(Student("小张", 20, 100))
# L.append(Student("小李", 18, 98))
# L.append(Student("小王", 19 ))
# L[2].get_score(80)
# for s in L:
#     s.show_info()

# class Human:
#     def set_info(self,name,age,address="不详"):
#         self.name=name
#         self.age=age
#         self.address=address
#     def show_info(self):
#         print(self.name,"今年",self.age,"岁，家庭住址是：",self.address)
# h1 = Human()
# h1.set_info("小张",20,"郑州市金水区")
# h2 = Human()
# h2.set_info("小李", 18)
# h1.show_info()  # 小张今年20岁，家庭住址：郑州市金水区
# h2.show_info()  # 小李今年18岁，家庭住址：不详

# class Human:
#     def __init__(self,name,age):
#         self.name  = name
#         self.age   = age
#         self.money = 0
#         self.skill = []
#     def teac h(self,other,sbject):
#         print(self.name,"教",other.name,"学",sbject)
#         other.skill.append(sbject)
#     def work(self,money):
#         print(self.name,"上班赚了",money,"元")
#         self.money += money
#     def borrow(self,other,money):
#         print(self.name,"向",other.name,"借钱",money,"元")
#         self.money += money
#         other.money -= money
#     def show_info(self):
#         print(self.age,"岁的",self.name,"有钱",self.money,"元",
#               "他学会的技能是",self.skill)
# zhang3=Human("张三",25)
# li4=Human("李四",16)
# zhang3.teach(li4,"python")
# li4.teach(zhang3,"王者荣耀")
# zhang3.work(1000)
# li4.borrow(zhang3,200)
# zhang3.show_info()
# li4.show_info()


