
# a=input("输入一段字符串")
# b=0a="abcde"
# for x in a:
#     print(x,end=" ")
# for  x in a:
#     if x==" ":
#         b=b+1
# print(b)
# a=input("输入一段字符串")
# b=0
# for x in a:
#     if 0<=ord(x)<=127:
#         b=b+1
# print(b)
# a=input("输入一段字符串")
# for x in a[::-1]:
#     print(x)
# for x in range(1,21):
#     print(x,end=" ")
# for x in range(1,101):
#     if x*(x+1)%11==8:
#         print(x,end=" ")
# for x in "abc":
#     for y in "123":
#         print(x+y,end=" ")

# a=int(input("请输入一个整数"))
# for x in range(1,a+1):
#     for y in range(1,a+1):
#         print(y,end=" ")
#     print()
# a=int(input("请输入一个整数"))
# for x in range(1,a+1):
#     for y in range(x,a+x):
#         print(y,end=" ")
#     print()
#
# l=[]
# a=input("请输入一个整数")
# b=input("请输入一个整数")
# c=input("请输入一个整数")
# l=list(a)+list(b)+list(c)
# print(l)
# l=[]
# s=0
# while True:
#     a = int(input("请输入一个正整数"))
#     if a<0:
#         break
#     l=l+[a]
#     s=s+a
# print(l)
# print(s)
# for x in range(1,10):
#     for y in range(1,x+1):
#         print(y,"*",x,"=",x*y,end=" ")
#     print()
# a = int(input("请输入一个正整数"))
# for x in range(2,a):
#     if a%x==0:
#         print(a, "这个数不是素数")
#         break
# else:
#     print(a,"这个数是素数")
# a = int(input("请输入一个正整数"))
# b=2
# while b<a:
#     if a%b==0:
#         print(a,"这个数不是素数")
#         break
#     b=b+1
# else:
#     print(a,"这个数是素数")
a = int(input("请输入一个正整数"))
for x in range(1,a+1):
    print(" "*(a-x)+"*"*(2*x-1))
for y in range(1,a+1):
    print(" "*(a-1)+"*")
# a = input("请输入第一行文字")
# b = input("请输入第二行文字")
# c= input("请输入第三行文字")
# s=max(len(a),len(b),len(c))
# print(a)
# print(b)
# print(c)
# print(s)
# n=int(input("请输入一个整数"))
# a=1
# while a<=n:
#     print("这是第",a,"行")
#     a=a+1
# n=int(input("请输入一个整数"))
# for x in range(1,n+1):
#     print("这是第", x, "行")
# i = 1  # 定义一个变量来控置循环的次数
# while i <= 5:
#     print("hello")
#     i += 1  # 改变i的绑定，让其增大，让其接近２０
# else:
# #     print("执行完毕")   #ｉ = 21
# a=1
# while a<=20:
#     print(a, end=" ")
#     a=a+1
#     if (a-1)%5==0:
#         print()

# begin=int(input("输入开始的整数"))
# end=int(input("请输入结束的整数"))
# while begin<=end:
#     print(begin,end=" ")
#     begin+=1
# n=int(input("输入一个宽度为N的长方形"))
# print("*"*n)
# m=1
# while m<=n-2:
#     print("*"+" "*(n-2)+"*")
#     m=m+1
# print("*"*n)
# s=0
# a=1
# while a<=100:
#     s=s+a
#     a = a + 1
# print(s)
# s=0
# for x in range(1,101):
#     s=s+x
# print(s)

# a=1
# while a<=5:
#     b=1
#     while b<=20:
#         print(b,end=" ")
#         b=b+1
#     print()
#     a=a+1
# a=1
# s=0
# while a<=100:
#     s=s+a
#     a=a+1
# print(s)
# n=int(input("输入一个整数"))
# a=1
# while a<=n:
#     b=1
#     while b<=n:
#         print(b,end=" ")
#         b=b+1
#     print()
#     a=a+1
# n=int(input("输入一个正整数"))
# for x in range(1,n+1):
#         #print(x,end=" ")
#     for y in range(x,n+x):
#         print(y,end=" ")
#     print()
# n=int(input("输入一个正整数"))
# for a in range(1,n+1):
#     b=1
#     while b<=n:
#         print(a,end=" ")
#         b=b+1
#         a=a+1
#     print()
    # ２．输入一个整数，代表正方形的宽度，打印如下正方形
#     如：
#         请输入：３
#         打印：
#             １２３
#             ２３４
#             ３４５
# a=int(input("输入一个整数"))
# #c为循环变量，限制循环次数为输入的数
# c=a
# #b为循环变量，但也控制着每次输出的第一位数（因为循环变量一直在递增）
# b=1
# #循环条件为b<=c（c不变，b一直在递增）
# while b<=c:
#     #每次循环都改变a的值（要保证每次便利的数字都是5个，每次开始便利的值都是b（递增））
#     for x in range(b,a+1):
#         #每次循环输出一次，以此输出所有便利的数字，用end使之在一行内输出
#         print(x,end=" ")
#     #每次便利输出一次所有的数字后，换行，然后改变变量的值，再次便利
#     print()
#     b += 1
#     a+=1

# a=int(input("输入一个整数"))
# b=1
# c=a
# while b<=c:
#     for x in range(b,a+1):
#         print(x,end=" ")
#     print()
#     b=b+1
#     a=a+1
# a=int(input("输入一个整数"))
# for x in range(1,a+1):
#     for y in  range(x,a+x):
#         print(y,end="")
#     print()


# s=0
# while True:
#     a = int(input("请输入整数"))
#     if a<0:
#         break
#     s=s+a
# print(s)

# n=1
# s=0
# m=1
# while n<=10000:
#     s=1/(2*n-1)+s
#     n=n+1
#     m=m*-1
# print(s)
# print(s*4)
# a=int(input("输入正整数"))
# for x in range(1,a+1):
#     print(x*"*")
# a=int(input("输入正整数"))
# for x in range(1,a+1):
#     print(" "*(a-x)+x*"*")
# a=int(input("输入正整数"))
# for x in range(a,0,-1):
#     print(x*"*")
# a=int(input("输入正整数"))
# for x in range(a,0,-1):
#     print(" "*(a-x)+x*"*")
# A=65
# while A<=65+25:
#     print(chr(A),end=" ")
#     A=A+1
# a=97
# A=65
# while A<=65+25:
#     while a<=97+25:
#         print(chr(A),end="")
#         A = A + 1
#         print(chr(a),end=" ")
#         a=a+1
# a=int(input("输入一个整数"))
# print("*"*a)
# b=2
# while b<a:
#     print("*"+" "*(a-2)+"*")
#     b=b+1
# print("*"*a)
# a=1
# while True:
#     print(a,end=" ")
#     if a==20:
#         break
#     a=a+1
# print()
# for x in range(1,21):
#     print(x,end=" ")
# print()
# a=1
# while a<=20:
#     print(a,end=" ")
#     a=a+1
# for x in range(1,21):
#     if x!=16:
#         continue
#     print(x,end=" ")
# a=(input("请输入一段字符串"))
# for x in a[::-1]:
#     print(x)
# for x in range(1,10):
#     for a in range(1,x+1):
#         print(a,"*",x,"=",x*a,end=" ")
#     print()

# for x in range(1,10):
#     for y in range(1,x+1):
#         print(y,"*",x,"=",x*y,end="  ")
#     print()
# a=1
# while a<=9:
#     b=1
#     while b<=a:
#         print(b,"*",a,"=",a*b,end=" ")
#         b=b+1
#     a=a+1
#     print()
# a=int(input("请输入数"))
# b=1
# while b<=a:
#     print(" "*(a-b)+"*"*(2*b-1))
#     b=b+1
# a=int(input("请输入数"))
# for x in range(1,a+1):
#     print(" "*(a-x)+"*"*(2*x-1))
# a=input("输入一段字符串")
# s=0
# c=len(a)
# b=0
# while b<=c:
#     if " "==b:
#         b=b+1
#     s=s+b
# print(s)


# a=input("输入字符串")
# b=0
# for x in a:
#     if x==" ":
#         b=b+1
# print(b)






















