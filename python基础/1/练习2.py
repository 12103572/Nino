# 1.练习：
#     输入三行文字，让这三行文字依次以２０个字符的宽度右对齐
#     输出
#     如：
#         请输入第１行：heloo world
#         请输入第２行：abcd
#         地输入第３行：a
#     输出结果为：
#                 hello world
#                        abcd
#                           a
#       再思考：
#         能否以最长的字符串长度进行右对齐显示（左侧填充空格）
1.
# a=input("请输入第一行")
# b=input("请输入第二行")
# c=input("请输入第三行")
# # print("%20s"%a)
# # print("%20s"%b)
# # print("%20s"%c)
# x=max(len(a),len(b),len(c))
# print(" "*(x-len(a))+a)
# print(" "*(x-len(b))+b)
# print(" "*(x-len(c))+c)

# 2.
# 问题：
# 输入一个整数n，写程序打印如下：
# 这是第１行
# 这是第2行
# .......
# 这是第n行 问题：
#         输入一个整数n，写程序打印如下：
#         这是第１行
#         这是第2行
#         .......
#         这是第n行
# n=int(input("输入一个整数"))
# m =1
# while m<=n:
#     print("这是第%d行"%m)
#     m = m+1

# 3.练习：
#   1.打印1~20的整数，打印在一行内显示，
#     每个整数之间用一个空格分隔
#     如:
#     1 2 3 4 5 6...20
#   2.打印1~20的整数，每五个数字打印一行，打印四行
#   如：
#   　1 2 3 4 5
#     6 7 8 9 10
#     ........
#     提示：
#         可以将if语句嵌入到while语句中
# a=1
# while a <= 20:
#     print(a, end=" ")
#     a = a + 1

# a= 1
# while a<=20:
#     if a%5==1 and a!=1:
#         print()
#     print(a,end=" ",)
#     a=a+1

# 练习：
#     写一个程序，输入一个开始的整数用变量begin绑定
#     输入一个结束的整数用变量end绑定
#     打印从begin到end不包含（end）之间的每个整数
#     打印在一行内
#     如：
#         请输入开始值：８
#         请输入结束值：２０
#     打印：８　９　１０．。。19
# begin=int(input("输入一个开始的整数"))
# end=int(input("输入一个结束的整数"))
# i=begin
# p=0
# while i<end:
#     print(i,end=" ")
#     p=p+1
#     if p%5==0:
#         print()
#     i = i+1
# else:
#     print()

# 练习：写一个程序，输入一个整数n，打印一个宽度和高度都为n个字符的
# 长方形
# 如：
# 　　输入４
#     ＊＊＊＊
#     ＊　　＊
#     ＊　　＊
#     ＊＊＊＊
# n=int(input("输入一个整数"))
# print("*"*n)
# m=1
# while m<=n-2:
#     print("*"+(n-2)*" "+"*")
#     m =m+1
# if n>=2:
#     print("*"*n)
# 练习：
# 写一个程序来计算：
#     １＋２＋３＋４＋．．．１００的和
#     答案５０５０
# s = 0
# i=1
# while i<=100:
#     s=i+s
#     i=1+i
# print(s)
# m=0
# n=1
# while n<=100:
#     m=n+m
#     n=n+1
# print(m)

# 示例：
#     打印１～２０的整数，打印在一行
#     １．２．３．．．．２０
#     打印１０行
# b=1
# while b<=10:
#     a=1
#     while a<=20:
#         print(a,end=' ')
#         a=a+1
#     else:
#         print()
#     b=b+1

# 练习：
#     输入一个数，打印制定宽度的正方形
#     如：
#         请输入正方形的宽度：５
#     打印如下：１２３４５
#             １２３４５
#             １２３４５
#             １２３４５
#             １２３４５
# a=int(input("请输入正方形的宽度："))
# b=1 #代表当前的行号
# while b<=a:
#     c=1 #代表起始数
#     while c<=a:
#         print(c,end=" ")
#         c=c+1
#     else:
#         print()#换行
#     b=b+1

# break 示例
# i =1
# while i <=6:
#     print("循环开始时：i=",i)
#     if i==3: #i为3时终止当前循环
#         break
#     print("循环结束时：i=",i)
#     i+=1
# else:
#     print("这是while的else子句")
# print("程序结束")
# 练习：
#     让用户任意输入一些整数，当输入负数时结束输入：
#         当输入完成后，打印用输入的所有整数的和
#     如：
#     请输入：１
#     请输入：２
#     请输入：３
#     请输入：－１
#     打印如下：
#         您输入的这些数的和是：１０

# b=0  #此变量用来记录所有数据的累加和
# while True:
#     a = int(input("请输入整数"))
#     if  a>0:
#         b=a+b
#     if a<0:
#         break
# print("您输入这些数的和是：",b)
# b=0
# while True:
#     a = int(input("请输入整数"))
#     if  a<0:
#         break
#     b+=a
# print("您输入这些数的和是：", b)

# 练习：
# 1.
# 写程序求下列算是的值：
# 1 / 1 - 1 / 3 + 1 / 5 - 1 / 7 + 1 / 9... - / (2 * n - 1)
# 求: 1)当n等于10000时，此算是的和并打印
# 2)将n等于10000时算式的和乘以４，打印其结果（3.14）
# s=0
# n=1
# m=1  #代表当前符号
# while n<=10000:
#
#     s+=m*1/(2*n-1)
#     n+=1
#     m*=-1  #变换符号
# print(s)
# print(s*4)
# 2.
# 用while语句打印三角形，输入一个三角形的宽度和高度，打印
# 相应的三角形
# 如：
# 请输入三角形的宽度：３
# 1)打印如下：
# *
# **
# ***
# a=int(input("输入三角形的宽度"))
# b=1
# while a>=b:
#     print(b*"*")
#     b=b+1


# 2)打印如下：
#             *
#            **
#           ***
# a=int(input("输入三角形的高度"))
# b=1
# while a>=b:
#     print(" "*(a-b)+"*"*b)
#     b=b+1
# 3)打印如下：
# ***
# **
# *
# a=int(input("输入三角形的高度"))
# b=a
# while b>=1:
#     print("*"*b)
#     b=b-1
# 4)打印如下
# 　　　  ***
#         **
#         *
# a=int(input("输入三角形的高度"))
# b=a
# while b>=1:
#     print(" "*(a-b)+"*"*b)
#     b=b-1

# 3)用程序while语句生成如下字符串，并打印结果
# 1)"ABCDE....XYZ"
# 2)"AaBb.....Zz"
# 函数：
# ord(x) / chr(x)
# A=65
# Z=90
# while A<=Z:
#     print(chr(A),end=" ")
#     A+=1
# m="A"
# n="Z"
# while ord(m)<=ord(n):
#     print(m,end="")
#     print(chr(ord(m)+32),end="")
#     m=chr(ord(m)+1)


# a=input("请输入第一行文字")
# b=input("请输入第二行文字")
# c=input("请输入第三行文字")
# x=max(len(a),len(b),len(c))
# # print("%20s"%a)
# # print("%20s"%b)
# # print("%20s"%c)
# print(" "*(x-len(a))+a)
# print(" "*(x-len(b))+b)
# print(" "*(x-len(c))+c)
# a=1
# while a<=20:
#     if a%5==1 and a !=1 :
#         print()
#     print(a, end=" ")
#     a=a+1
# n=int(input("输入一个整数"))
# m=1
# while n>=m:
#     print("这是第",m,"行")
#     m=m+1

# begin=int(input("开始值"))
# end =int(input("输入结束值"))
# a=begin
# while end>a:
#     print(a,end="")
#     a=a+1

# n=int(input("输入高度"))
# print("*"*n)
# a=1
# while a<=n-2:
#     print("*"+" "*(n-2)+"*")
#     a=a+1
# if a>=2:
#     print("*" * n)

# s=0
# n=1
# while n<=100:
#     s=s+n
#     n=n+1
# print(s)

# a=int(input("请输入正方形的宽度："))
# b=1 #代表当前的行号
# while b<=a:
#     c=1 #代表起始数
#     while c<=a:
#         print(c,end=" ")
#         c=c+1
#     else:
#         print()#换行
#     b=b+1
# a=1
# s=0
# while a<=100:
#     s=s+a
#     a=a+1
# print(s)
# n=int(input("输入"))
# m=1
# while m<=n:
#     print(m*"*")
# #     m=m+1
# n=int(input("输入"))
# m=1
# while m<=n:
#     print(" "*(n-m)+m*"*")
#     m=m+1
# n=int(input("shuru"))
# m=n
# while n>=1:
#     print(" "*(n-m)+n*"*")
#     n=n-1
# n=int(input("sr"))
# m=1
# while n>=1:
#     print(" "*m+n*"*")
#     n=n-1
#     m=m+1



# n=int(input("sh"))
# m=1
# while n>=m:
#     c=1
#     while c<=n:
#         print(c,end="")
#         c=c+1
#     else:
#         print()
#     m=m+1
# a=int(input("请输入正方形的宽度："))
# b=1 #代表当前的行号
# while b<=a:
#     c=1 #代表起始数
#     while c<=a:
#         print(c,end=" ")
#         c=c+1
#     else:
#         print()#换行
#     b=b+1
# s=0
# while True:
#     a=int(input("shuru"))
#     if a<0:
#         break
#     else:
#         s=s+a
# print(s)
# b=0  #此变量用来记录所有数据的累加和
# while True:
#     a = int(input("请输入整数"))
#     if  a>0:
#         b=a+b
#     if a<0:
#         break
# print("您输入这些数的和是：",b)
# b=0
# while True:
#     a = int(input("请输入整数"))
#     if  a<0:
#         break
#     b+=a
# print("您输入这些数的和是：", b)

# a=input("请输入第一行")
# b=input("请输入第二行")
# c=input("请输入第三行")
# print("%20s"%a)
# print("%20s"%b)
# print("%20s"%c)
# x=max(len(a),len(b),len(c))
# print((x-len(a))*" "+a)
# print((x-len(b))*" "+b)
# print((x-len(c))*" "+c)

#











