# 回顾
# 字符串
#     格式化表达式“姓名：%s ，年龄“%d ”%('tarena',15)
#     占位符类型码
#
# 循环语句
# while 语句
#     while 真值表达式：
#                 语句块1
#     else  :
#                 语句块2
#         while 真情表达式2：
#                     语句块3
#         else:
# break 语句
# 终止循环
# 结束循环语句while或for的执行
# 通常和if 语句一起使用
# break 只能终止包含它的那个循环语句（for ,while）
# 死循环
# whilr True:
# 通常用于循环次数不确定的循环
# for 语句

#
# 练习：
#     １．任意输入一段字符串，写程序做如下两件事：
#     １）计算出空格的个数，并打印个数
#         要求用for语句，不允许使用S。count方法
#     ２）计算字符串中全部英文字符的个数
#     注：英文字符的编码值为０～１２７，可用（ord（x））
#     函数进行判断
# a=input("请输入字符串")
# b=0 #记录空格的个数
# for x in a:
#     if x ==" ":
#         b+=1
# print("空格的个数是：", b)
# c=0 #记录英文字符的个数
# for x in a:
#     if 0<= ord(x) <=127:
#         c+=1
# print("英文字符的个数是：",c)
# while 方法
# s = input("输入字符串")
# i = 0 #当前字符的索引值
# a=input("输入一个字符串")
# b=len(a)-1
# while b>=0:
#     x=a[b]
#     print(x)
#     b-=1
#
# # a = input("输入一个字符串")
# for x in  a[::-1]:
#     print(x)
# 此示例示意rang函数的使用方法
# for x in range(4):
#     print(x) #0,1,2,3
# 练习：
#     1.用for语句打印１～２０的整数，打印在一行内
#     2.求１００以内有哪些整数与自身＋１的乘积再对１１求余结果
#     等于８？包含１００
#         即：x*(x+1)%11=8
#
# for x in range(1,21):
#     print(x,end=" ")
# else:
#     print()
#
#
# for a in range(101):
#     b = a * (a + 1) % 11
#     if b==8:
#         print(a,end=" ")
# 3.求1+2+...99的和
# b=0
# for x in range(1,100,2):
#     b=x+b
# print(b)

# i=6
# for x in range(1,i):
#     print("x=",x,"i=",i)
#     i-=1
# for x in "abc":
#     for y in "123":
#         print((x+y),end=" ")

# 练习：
#     １．输入一个整数，代表正方形的宽度，打印如下正方形
#     如：
#         请输入：３
#         打印：
#             １２３
#             １２３
#             １２３
#     ２．输入一个整数，代表正方形的宽度，打印如下正方形
#     如：
#         请输入：３
#         打印：
#             １２３
#             ２３４
#             ３４５

# a=int(input("输入正方形的宽度"))
# for x in range(1,a+1):
#     for a in range(1, a + 1):
#         print(a, end="")
#     print()#换行
# a=int(input("输入正方形的宽度"))
# for x in range(1,a+1):
#     b=1
#     while b<=a:
#         print(b,end="")
#         b=b+1
#     print()
# a=int(input("输入正方形的宽度"))
# for x in range(1,a+1):
#     b=1
#     c=x
#     while b<=a:
#         print(c,end=" ")
#         b=b+1
#         c=c+1
#     print()
# a=int(input("输入正方形的宽度"))
# for x in range(1,a+1):
#     b=1
#     while b<=a:
#         print(x,end=" ")
#         b=b+1
#         x=x+1
#     print()
# a=int(input("输入正方形的宽度"))
# for x in range(1,a+1):
#     for y in range(x,a+x):
#         print(y,end="")
#     print()

# for x in range(5):
#     if x==2:
#         continue#跳过2
#     print(x)
# num=0
# while num<10:
#     if num%2==1:
#         num+=1
#         continue
#     print(num)
#     num+=1
# s=0
# for x in range(1,101):
#     if x %2==0 or x%3 ==0 or x%5==0 or x%7==0:
#         continue
#     s=s+x
# print(s)

# 练习：
# 1.写一个程序，输入三行文字，将这三行文字保存于一个列表l中，
# 并打印这个列表
# 如：
#     请输入：abc
#     请输入：１２３
#     请输入：你好
#     生成如下列表：l=['abc‘,'123','你好']
#     print(l)#['abc','123','你好']
# a=input("请输入第一行文字")
# b=input("请输入第二行文字")
# c=input("请输入第三行文字")
# l=[a,b,c]
# print(l)

# 2.写一个程序，让用户输入很多个正整数，当输入负数时，结束输入
# 将用户输入的数字存于列表中，
#     1)然后打印这个列表
#     2)计算出这些数字的和，打印出这些和
#     如：
#         请输入：１
#         请输入：２
#         请输入：３
#         请输入：４
#         请输入：－１
#     打印:
#         [1,2,3,4]
#         和是：１０
# s=0
# l=[]    #创建一个空列表，用变量l绑定。准备存放数据
# while True:
#     a=int(input("请输入正整数"))
#     if a<0:
#         break
#     else:
#         l+=[a]  #把a追加到l绑定的列表末尾
#     s=s+a
# print(l)
# print(s)
# 练习：
# 1.写一个程序，输入三行文字，将这三行文字保存于一个列表l中，
# 并打印这个列表
# 如：
#     请输入：abc
#     请输入：１２３
#     请输入：你好
#     生成如下列表：l=['abc‘,'123','你好']
#     print(l)#['abc','123','你好']
#
# 2.写一个程序，让用户输入很多个正整数，当输入负数时，结束输入
# 将用户输入的数字存于列表中，
#     1)然后打印这个列表
#     2)计算出这些数字的和，打印出这些和
#     如：
#         请输入：１
#         请输入：２
#         请输入：３
#         请输入：４
#         请输入：－１
#     打印:
#         [1,2,3,4]
#         和是：１０
#
# 列表的　in / not in运算符
#     判断一个值是否存在于列表中，如果存在返回True，否则返回False
#     同字符串的 in　运算符，用于检查一个值是否存在于列表中
#
#     示例:
#     x=[1,'two',3,'四']
#     3 in x #True
#     1 in x #True
#     ５not in x #True
#     '四' not in x #False
#
# 练习：
#     1.写程序打印九九乘法表
#     1*1=2
#     1*2=2 2*2=4
#     ....
#     1*9=9...    9*9=81
#     2.写一个程序，任意输入一个整数，判断这个数是否为素数
#     素数(也叫质数)，是只能被１和自身整数的正整数
#     如：２　３　５　７　１１　１３　１７　１９
#     提示：
#         用排除法：当判断x是否为素数时，要让x分别除以
#         ２，３，４．．．x-1,只要有依次被整除，则x不是素数
#         否则x是素数
#     3.输入一个整数，此整数代表树干的高度，打印一颗如下形状
#     的圣诞树
#         如：
#             输入：２
#         打印：
#           *
#          ***
#           *
#           *
#         如：
#             输入：３
#         打印：
#           *
#          ***
#         *****
#           *
#           *
#           *
#
# 4.算出１００～９９９范围内的水仙花（Narcissisitic Number）
# 水仙花数是指百位的３次方＋十位的３次方＋个位的３次方
# 等于原数的整数
#     如：
#         153=1**3+5**3+3**3
#     答案：
#         153,370,.....
1.
for x in range(1,10):
    for y in range(1,x+1):
        print(y,'*',x,'=',x*y,end="  ")
    print()
# 2
# # 用 for 循环
# a=int(input("请输入一个大于1整数"))  #创建一个变量
# for x in range(2,a):                  #创建一个 for 循环
#     if  a%x==0:                         #判断是否为素数，True代表不是
#         print(a,"这个数不是素数")
#         break                             #当if为False时，终止当前循环
# else:
#     print(a,"这个数是素数")
#
# # 用while循环：
# a=int(input("请输入一个大于1的整数"))
# b=2
# while b<a:
#     if a%b==0:
#         print(a,"这个数不是素数")
#         break
#     b=b+1
# else:
#     print(a,"这个数是素数")
# 3.
# a=int(input("输入树干的高度"))
# for x in range(1,a+1):
#     print(" "*(a-x)+"*"*(2*x-1))
# for y in range(1,a+1):
#     print(" "*(a-1)+"*")
# 4.
# for x in range(100,999):
#     b=x//100  #b表示百位数字
#     c=x%100//10 #c表示十位数字
#     d=x%10        #d代表个位数字
#     a=b**3+c**3+d**3  #变量a表示循环中x的赋值
#     if x==a :  #判断是否为水仙花数，True or False
#         print(x,"这个数是水仙花数")






























