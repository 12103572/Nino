'''
回顾:
    自定义模块
        xxx.py
        导入方式：
            import 语句
            from  import 语句
            from import * 语句
    搜索路径顺序:
        1.查找内建模块
        2.查找当前工作路径
        3.查找sys.path里指定的路径中
    xxx.py---->xxx.pyc----->python3
    模块内还有一些预置的变量（属性）
     __doc__  #用来绑定文档字符串
     __name__  #用来绑定模块名，当为主模块时绑定  __main__
     __file__  #用来绑定模块的文件路径名
     __all__ 列表
        __all__ =['var1','var2']
        在用 from import * 语句时，只导入列表中的变量(属性)
    隐藏属性
        以 _ 开头的全局变量为隐藏属性
         from import * 语句
    包
        把一些模块以文件夹的方式呈现
        包含有一系列的模块或子文件夹

        导入语句
            绝对导入
                import 语句
                    import mypack.game.contra [ as v]
                from import 语句
                    from mypack.game.contra import play
                from import * 语句
                    from mypack.game.contra import *
            相对导入
                from . import context
                # mypack/games/contra.py 里
                from ..office.word import *
                __init__.py:
                必须有的文件，实现包的内容
                __all__列表  限制from import * 语句的操作

    内建模块
        通常C语言写的，看不到源代码
    标准库模块
        通常python 写的，可以看到源文件


    两个模块
    sys模块
     sys.platfrom  # 操作系统平台的信息’Linux','Win32' 'darwin'
     sys.version /  sys.version_info
     sys.argv  可以得到用户在命令行输入的内容
     sys.path 模块的搜索路径
     sys.exit() 退出程序
     sys.getrecursionlimit()   #得到最大的递归深度
     sys.setrecursionlimit(n)  #得到和修改递归嵌套层次的限制
    random 模块
        random.random() 返回一个0,1之间的随机数，不包括1
        random.randint(a,b) #返回 a,b之间的整数 包含a,b

'''


# 练习：
#     写一个函数 get_score() 获取学生的成绩(0~100中的整数)，
#     如果用户输入的成绩不是0~100之间的书，则返回0
#         如:
#             def get_score():
#                 s=intput("请输入成绩(0~100)")
#                 ...
#             score=get_score()
#             print("学生的成绩是:",score)
# def get_score():
#     s=input("请输入学生成绩")
#     try:
#         s=int(s)
#     except:
#         return 0
#     if  0<=s<=100:
#         return s
#     return 0
# score=get_score()
# print("学生的成绩是：",score)

# def fry_egg():
#     print("打开天然气点燃...")
#     try:
#         count=int(input("请输入鸡蛋个数："))
#         print("完成煎鸡蛋，共煎了%d个鸡蛋"%count)
#     finally:
#         print("关闭天然气") #<---此事必须要做
# try:
#     fry_egg()
# except ValueError:
#     print("煎鸡蛋失败！")

# def make_execpt():
#     print("开始...")
#     # raise ValueError   #触发ValueError 类型的异常
#     # raise ZeroDivisionError   #raise 类型
#     #创建一个错误对象用error来绑定
#     error = ValueError("XXX大街YYY号着火了！")
#     raise error  #触发ValueError 类型的错误对象
#     print("结束!!!")
# try:
#     make_execpt()
#     print("make_execpt 调用完成")
# except ValueError as err:
#     print("收到 ValueError类型的错误通知")
#     print("err=",err)  #err 使用来绑定 rasie 发出的错误对象
# except ZeroDivisionError:
#     print("被零除！！！")
# print("程序正常结束")

# def f1():
#     n=int(input("请输入整数：")) #此处可能触发 ValueError 错误
# def f2():
#     try:
#         f1()
#     except ValueError as err:
#         print("f1函数内出错")
#         # print("f2里的err=",err)
#         # raise err
#         raise
# try:
#     f2()
# except ValueError as err:
#     print("f2内发生了ValueError类型的错误")
#     print("err=",err)


# 练习：
#     写一个函数 gen_age() 用来获取一个人的年龄信息
#         此函数规定用户只能输入1~140之间的整数，如果用户输入其他的数
#         则直接触发ValueError 类型的错误
#     如：
#     def gen_age():
#         ...
#     try:
#         age=get_age()
#         print("用户输入的年龄是：",age)
#     except ValueError as err:
#         print("用户输入的不是1~140之间的整数")
# def get_age():
#     age=int(input("请输入您的年龄"))
#     if 1<=age<=140:
#         return age
#     shabi=ValueError("您输入的值超出范围，请重新输入，不然踢你哦")
#     raise  shabi
# try:
#     age = get_age()
#     print("用户输入的年龄是：", age)
# except ValueError as err:
#     print("用户输入的不是1~140之间的整数！！！")
#     print(err)

# def get_score():
#     s=int(input("请输入学生成绩："))
#     #此 assert 语句让 s 不在范围内时主动报错
#     assert 0 <= s <= 100 ,"成绩超出范围"
#     return s
# try:
#     score = get_score()
#     print("成绩是：",score)
# except AssertionError as err:
#     print("断言失败！err =",err)


# def f1():
#     '''此函数可能触发错误'''
#     s="我是错误信息"
#     raise  ValueError(s)
# def f2():
#     f1()
#
# def f3():
#     f2()
#
# def f4():
#     f3()
# try:
#     f4()
# except ValueError as err:
#     print("err =",err)

# L = [1,3,5,7]
# it = iter(L) #从对象L中获取迭代器，然后用it变量绑定
# print(next(it))     #1
# print(next(it))     #3
# print(next(it))     #5
# print(next(it))     #7
# print(next(it))     #StopIteration

# 练习：
# #     1.有一个集合：
# s={"唐僧","悟空","八戒","沙僧"}
#     用for 语句遍历所有元素如下：
# for x in s :
#     print(s)
# else:
#     print("遍历结束")
#     请将上面的for语句改写为while 语句的迭代器实现
#     2.一个小球从100米高空落下，每次落地后反弹高度为元高度的一半
#     再落下，
#     1)写程序算出皮球在第10次落地后反弹多高
#     2)打印出第10次反弹后小球经理的总路程
#     3.修改原学生信息管理程序，加入异常处理语句，让程序在任何情况下
#     都能按逻辑正常执行不至于崩溃，
#     如：输入年龄时，输入非数字字符会崩溃
# #
# # 1.
# s={"唐僧","悟空","八戒","沙僧"}
# it=iter(s)
# while True:
#     try:
#         x=next(it)
#         print(x,end=" ")
#     except StopIteration:
#         print()
#         print("遍历结束")
#         break
# #  2.
# # 1)
# def height(count): #创建一个函数记录反弹后的高度，count代表反弹的次数
#     return 100/(2**count) #每次都减少一半高度，所以总路程除以2的次数的平方
# print("第10次落地后反弹",height(10),"米")
# # 2)
# def distance(count): #创建一个记录总路程的函数，count代表小球反弹的次数
#     s=0  #创建变量记录总路程
#     for x in range(1,count+1): #创建一个循环来记录反弹次数
#         s=(150/2**x)*2+s #小球反弹一次后总路程除以次数
#     return s  #返回总路程
# print("第10次反弹后小球经历的总路程是:",distance(10),"米")











