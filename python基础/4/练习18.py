'''
回顾：
面向对象编码
    什么是对象
        对象时指物体或实体
    面向对象是把一切东西看成物体或实体

对象的特征：
    属性
        实例属性(实例变量)来记录对象自身的数据
    行为
        实例方法来描述对象的行为
类---->对象(实例方法,实例属性)

类是用来描述对象，创建对象的“工厂”
class 语句
    语法：
        class 类型(继承列表):
            实例方法
            初始化方法
            析构方法
            类变量
            类方法
            静态方法

构造函数：
    类名(调用传参)    #创建实例 instance（对象object）

实例方法：
    class myclass:
        def 方法名1(self,形参列表):
            语句块
        def __init__(self,形参列表...)
            """初始化方法"""
            self.name = "no name"
        def __del__(self):
            """析构方法"""
            对象创建之后立刻调用
实例属性：
    class Dog:
        pass
dog1 = Dog()
dog1.color = "白色"(通常不要在这里创建)

del dog1.color(删除属性)
预置实例属性：
    __dict__属性
        绑定存储此对象的实例属性的字典
    __clsaa__属性
        绑定创建此对象的类
isinstance(obj,类或元组)
    判断obj是不是某种类型
type(obj)   返回类型
'''
# #看懂下列代码中的类属性count的作用是什么
# class Human:
#     '''此示例示意类变量'''
#     count = 0
#     def __init__(self,name):
#         print(name,"对象被创建")
#         self.name = name
#         self.__class__.count += 1
#     def __del__(self):
#         print(self.name,"对象被销毁")
#         self.__class__.count -= 1
# L = [Human("孙悟空"),Human("猪八戒")]
# h1 = Human("沙僧")
# print("现在共有",Human.count,"个对象")
# del L
# print("现在共有",Human.count,"个实例对象 ")


# class Human:
#     #此 __slots__ 列表限定Human类型的对象只能有一个age属性
#     __slots__ = ["age"]
#     def __init__(self,age):
#         self.age = age
#     def show_info(self):
#         print("年龄是",self.age)
# h1 = Human(10)
# h1.show_info()
# # h1.Age = 11   #报错
# h1.show_info()

# class A:
#     @staticmethod
#     def myadd(a,b):
#         return a+b
# print(A.myadd(100,200))         #300
# print(A.myadd("ABC","123"))    #ABC 123
# a = A()
# print(a.myadd(3,5)) #8

# class Stundent:
#     __slots__ = ["name","age","score"]
#     def __init__(self,name,age,score=0):
#         self.name = name
#         self.age = age
#         self.score = score
# infos = []
# def add_student(infos,name,age,score):
#     '''添加一个学生信息'''
#     s = Stundent(name,age,score)
#     infos.append(s)
# def del_student(infos):
#     n = input("请输入要删除的学生的姓名")
#     for index,s  in enumerate(infos):
#         if s.name == n:
#             del infos[index]
#             print("删除",n,"成功")
#             return
#     print("删除失败！")
# def get_score(infos):
#     m=0
#     for s in infos:
#         m += s.score
#     return m/len(infos)
# add_student(infos,"小张",20, 100)
# add_student(infos,"小李",18, 66)
# add_student(infos,"小王",19, 55)
# add_student(infos,"小赵",22, 88)
# del_student(infos)
# print(len(infos))
# print("平均成绩是",get_score(infos))

# #此示例示意继承的语法和用法
# class Human:
#     '''定义人类的基类'''
#     def say(self,what):
#         print("say",what)
#     def walk(self,distance):
#         print("run",distance,"公里")
# h1 = Human()
# h1.say("天气变冷了")
# h1.walk(5)
#
# class Teacher(Human):
#     def teach(self,sbject):
#         print("teach",sbject)
# t1 = Teacher()
# t1.teach("继承/派生")
# t1.walk(6)
# t1.say("晚上吃啥啊")
#
# class Student(Teacher):
#     def study(self,sbject):
#         print("study",sbject)
# s1 = Student()
# s1.walk(4)
# s1.say("感觉还好")
# s1.study("面向对象")
# s1.teach("王者荣耀")

# 思考:
#     list 类里提供了几个方法,但没有提供带有一个参数的头部添加数据
# 的方法,试题能否在不改变原列表类 list的基础上,创建一个新的类
# Mylist,新类继承原类的全部的功能,并添加一个insert_head(n)的方法
# 如：
#     class Mylist(list):
#         def insert_head(self,n):
#
# myl = Mylist(range(3,6))
# print(myl)  #[3,4,5]
# my.insert_head(2)
# print(myl)  #[2,3,4,5]
# myl.append(6)
# print(myl)  #[2,3,4,5,6]

# class Mylist(list):
#     def insert_head(self,n):
#         self.reverse()
#         self.append(n)
#         self.reverse()
# myl=Mylist(range(3,6))
# print(myl)
# myl.insert_head(2)
# print(myl)
# myl.append(6)
# print(myl)

# print(object())

# print(help(__builtins__))

# class A:
#     def work(self):
#         print("A.WORK被调用！！！")
# class B(A):
#     def work(self):
#         print("B.work被调用!!!")
#     def do_somthing(self):
#         # 1.调用自己的work
#         self.work()
#         # 2.调用父类的work
#         # super(B, self).work()
#         super().work()
# #
# b=B()
# # super(B,b).work()   #借助于b来调用A类的方法
# b.do_somthing()

# class Human:
#     def __init__(self,n,a):
#         self.name = n
#         self.age = a
#         print("Humande __init__被调用")
#     def show_info(self):
#         print("姓名：",self.name)
#         print("年龄：",self.age)
#
# class Student(Human):
#     def __init__(self,n,a,s=0):
#         super().__init__(n,a) #显式调用父类的方法
#         self.score = s #在此类中添加新的属性
#         print("Student.__init__被调用!")
#     def show_info(self):
#         super().show_info()
#         print("成绩：",self.score)
# s1 = Student("小张",20)
# s1.show_info()

# 练习:
#     1.看懂学生信息管理系统的示例代码


