'''回顾:
    异常
        异常是一种错误通知机制（信号通知），可以快速将错误信息传达给调用者
    异常相关的语句
        try-except 语句
            捕获（接收）错误通知，将异常状态改为正常状态
        try-finally 语句
            此语句能保证在(正常流程/异常流程)都能执行必须要执行的语句
        raise 语句
            发出异常通知，把程序转为异常状态(进入异常流程)
        assert 语句
            当条件不满足时，触发AssertionError 类型的错误通知

迭代器 Iterator
    迭代器是用来访问可迭代对象的工具
    iter(可迭代对象) 从可迭代对象中获取迭代器
    next(迭代器)      通过迭代器从可迭代对象中取值，没有值时
                        会触发StopIteration异常通知


    '''

# def myinteger(n):
#     i=0
#     while i <n:
#         yield i
#         i+=1
# for x  in myinteger(10):
#     print(x)
# print("----------------")
# it = iter(myinteger(20))
# print(next(it))  #0
# print(next(it))  #1
# L=[x for x in myinteger(20) if x %2==1]
# print(L)

# 练习：
#     写一个生成器函数 myeven(start,stop) #用来生成从
#     start 开始到stop结束区间的一系列偶数（不包含stop）
#     如：
#         def myeven(start,stop):
#             ...
#         evens=list(myeven(10,20))
#         print(evens)  #[10,12,14,16,18]
#         for x in myeven(21,30):
#             print(x)  #打印22,24,26,28
# def myeven(start,stop):
#     for x in range(start,stop):
#         if x % 2 ==0:
#             yield x
# evens=list(myeven(10,20))
# print(evens)  #[10,12,14,16,18]
# for x in myeven(21,30):
#     print(x) #打印22,24,26,28
#
# def myeven(start,stop):
#     while start< stop:
#         if start % 2 ==0:
#             yield start
#         stat += 1
# evens=list(myeven(10,20))
# print(evens)  #[10,12,14,16,18]
# for x in myeven(21,30):
#     print(x)

# 练习：
#     1.已知有列表：
#         L=[2,3,5,7]
#     1）写一个生成器函数，让此函数能够动态的提供数据，数据为
#     原列表中数字的平方+1 ，即 x**2+1
#     2）写一个生成器表达式，让此表达式能够动态提供数据，数据
#     同样为原列表中的数字的平方加1
#     3）生成一个列表，此列表内的数据为元列表L中的数字的平方加1
# 1)
# L=[2,3,5,7]
# def mygen(lst):
#     for x in lst:
#         yield x ** 2 + 1
# for x in mygen(L):
#     print(x,end=" ")
# print()
# # 2).
# for x in(x**2+1 for x in L):
#     print(x,end=" ")
# print()
# # 3).
# L1=[x**2+1 for x in L]
# print(L1)

# 2.
# 试写一个生成器函数
# myfilter(func, iterable)
# 要求此函数与python内建的函数的功能完全相同
# 如：
#
# def myfilter(func, iterable):
#     ...
# for i in myfilter(lambda x: x % 2 == 1, range(10)):
#     print(i)  # 1 3 5 7 9
# 方法一：
# def myfilter(func, iterable):
#     it=iter(iterable) #拿到可迭代对象的迭代器
#     while True:
#         try:
#             x=next(it)
#             if  func(x):
#                 yield x
#         except StopIteration:
#             return
# for i in myfilter(lambda x: x % 2 == 1, range(10)):
#     print(i)  # 1 3 5 7 9
# 方法2
# def myfilter(func, iterable):
#     for x in iterable:
#         if func(x):
#             yield x
# for i in myfilter(lambda x: x % 2 == 1, range(10)):
#     print(i)  # 1 3 5 7 9

# numbers = [10086,10000,10010,95588]
# names = ["中国移动","中国电信","中国联通"]
# for t in zip(numbers,names):
#     print(t)
# d=dict(zip(numbers,names))
# print(d)
# for name,numb  in zip(names,numbers):
#     print(name,"的客服电话是：",numb)

# def myzip(iterable1,iterable2):
#     it1=iter(iterable1)
#     it2=iter(iterable2)
#     while True:
#         try:
#             x1 = next(it1)
#             x2 = next(it2)
#             yield (x1,x2)
#         except StopIteration:
#             return
# numbers = [10086,10000,10010,95588]
# names = ["中国移动","中国电信","中国联通"]
# for t  in myzip(names,numbers):
#     print(t)

# def myenumerate(iterable,start=0):
#     it=iter(iterable)
#     it1=iter(range(start,start+len(iterable)))
#     try:
#         while True:
#             x1=next(it)
#             x2 = next(it1)
#             yield (x2,x1)
#     except StopIteration:
#         return
# names = ["中国移动","中国电信","中国联通"]
# for t in myenumerate(names,999):
#     print(t)
# #
# # 方法2：
# def myenumdrate(iterable,start=0):
#     for x in iterable:
#         yield (start,x)
#         start += 1
# names = ["中国移动","中国电信","中国联通"]
# for t in myenumerate(names,666):
#     print(t)
# s = "ABC中文"
# b = s.encode()  # 用utf-8编码规则转为字节串
# s2 = b.decode()  # 用utf-8编码规则解码为字符串
# print(s == s2)  # True

# ba = bytearray([65, 33, 48, 97, 100])
# print(ba) #bytearray(b'A!0ad')
# ba[1] = 66
# ba[3] = 49
# print(ba) #bytearray(b'AB01d')

# 练习:
# 1. 实现一个python2下的xrange([start,stop,[step]])生成器函数,
#     此生成器函数式按range规则来生成一系列整数
#     要求:myxrange功能完全相同,不允许调用range函数和列表
#     用自己写的myxrange结果生成器表达式求1~10以内所有技术的平方和
#     如:
#         def myxrange(start,stop=None,step=None):
#             ...
#         求1**2+3**2+5**2+7**2+9**2
# 2.写一个程序,从键盘输入一段字符串,用变量s绑定
#     1)将此字符串转为字节串用变量b绑定,并打印出此字节串b
#     2)打印字符串s的长度和字节串b的长度
#     3)将字节串b再转换为字符串用变量s2绑定,然后判断s2 和 s是否相同
# 3.分解质因数,输入一个正整数,分解质因数
#     如
#         输入:90
#     打印:
#         90 = 2*3*3*5
#     注:质因数是指最小能被原数整除的素数(不包括1)
# 4.预习文件操作,面向对象

# 1.
# def myxrange(start,stop=None,step=None):
#     if stop is None: #没有第二个参数
#         stop = start
#         start = 0
#     if step is None:
#         step = 1
#     if step > 0:  #正向生成
#         while start < stop:
#             yield start
#             start += step
#     elif  step < 0: #反向生成
#         while start > stop:
#             yield start
#             start += step  #因为step 为负数
# print(sum(x**2 for x in myxrange(1,10,2)))

# 2.
# s=input("请输入一段字符串")
# b = s.encode('utf-8')
# # print("字节串b=",b)
# print("字符串s的长度是：",len(s))
# print("字节串b的长度是:",len(b))
# s2=b.decode()
# if s == s2:
#     print("相同")
# else:
#     print("不同")

# 3.
# def sushu(n):
#     if n<2:
#         return False
#     for x in range(2,n):
#         if n %x ==0:
#             return False
#     return True
# def sushubiao(n):
#     return [x for x in range(2,n) if sushu(x)]
# s=int(input("请输入一个正整数"))
# def zhiyinshu(n):
#     L = sushubiao(n)
#     for x in L:
#         if n % x ==0:
#             return str(x)+"*"+zhiyinshu(n//x)
#     return str(n)
# print(s,"=",zhiyinshu(s))

# def get_all_yinsu(x):
#     '''此方法用来获取一个数x的所有因数，
#     返回因数的列表，如：x=90
#     返回[2,3,3,5]'''
#     L = []
#     while x >1:
#         #每次找一个质因数，然后加入到列表后，然后变换X的值，重新开始循环
#         for i in range(2,x+1):
#             if x % i ==0:   #找到质因数
#                 L.append(i)
#                 x = int(x //i)
#                 break
#     return L
# n = int(input("请输入"))
# L=get_all_yinsu(n)
# print(n,"=","*".join(str(x) for x in L))


