# day05回顾
# 循环
#  for 语句
#      遍历可迭代对象
#     语法：
#         for 变量列表 in 可迭代对象
#             语句块1
#         else
#             语句块2
#     可迭代对象：
#         字符串 str
#         列表 list
#         rang() 返回回来的对象
#         以及后面所学的所有容器类都是可迭代对象
#     range函数
#         range(终止 整数)
#         range （开始整数，终止整数)
#         range （开始整数，终止整数，步长）
#         作用：用于创建一个一个整数序列生成器（可迭代对象）
#
# continue
#     用于重新开始一次新的循环
#
# 列表容器
#     可以存储任意数据的容器
#     可变的序列
#
# 列表的创建：
#     子面值的创建方式
#     []  [1,2,3,4]  [1,2,[3,4,[5,6]]]
#     构造函数的创建方式
#     list()
#     list("abc")
#     list(range(1,10))
#     list([1,2,3,4])
# 列表的运算：
#  +  += * *=
#     列表 += 可迭代对象（实现追加可迭代对象内的数据）
#     列表的比较运算：
#     <  <=  >  >=  ==  !=
#         依次比较
#     in / not in 运算符
# l = [1, 2, 3, 4]
# l2 = l
# l = []
# print(l2)
#
# l=[1,2,3,4]
# l2=l
# l[::]=[]
# print(l2)

# 练习：
#     已知有列表
#     L=[3,5]
#     用索引和切片操作，将原列表改为：
#     L＝[1,2,3,4,5,6]
#     将列表翻转，删除最后一个元素后再打印此列表
#     。。。
#     print(L) #[6,5,4,3,2](尽可能让L绑定的对象的ID不变)
# L=[3,5]
# L[1:1]=[4]
# L[0:0]=[1,2]
# L[5:5]=[6]
# L=L[-1:-6:-1]
# print(L)
# print(L)
#
# L=[]
# while True:
#     a = int(input("请输入正整数"))
#     if a<0:
#         break
#     L=L+[a]
# print(L)
# print("输入的最大数是，:",max(L))
# print("这些数的平均值是：",sum(L)/len(L))

# 练习：
#     １．写一个程序，让用户输入两个以上的正整数，当输入负数时结束，
#     要求：限制用户，不允许输入重复的数
#     １）打印这些数字的和
#     ２）打印这些数中最大的一个数
#     ３）打印这些数中第二大的一个数
#     ４）删除最小的数
#     ２．昨晚上题后思考：
#         如何保证原数据的顺序不变，最后按原来的顺序打印出剩余
#         的数？
# l=[]
# while True:
#     a=int(input("输入正整数"))
#     if  a<0:
#         if len(l)>2:
#             break
#         else:
#             print("您输入的数字太少，请继续输入！！！")
#             continue
#     if a in l:
#         print("您已经输入过这个数了，请输入其他的数")
#     else:
#         l.append(a)
# print("这些数的和是：",sum(l))
# print("这些数中最大的一个数是：",max(l))
# m=max(l)
# l.remove(max(l))
# print("这些数中第二大的数是：",max(l))
# l.append(m)
# l.remove(min(l))
# # print("删除最小的数后为：",l)


# print(l2)
# l1 = [1, 2, [3.1, 3.2]]
# l2 = l1.copy()  # 不拷贝，两个变量同时绑定在一个对象上
# l2[1] =   2.2
# l2[2][0]= 3.14
# print(l1)
# print(l2)

# inmport copy#导入复制模块（语句后面会讲）
# l1 = [1, 2, [3.1, 3.2]]
# import copy
# l2 =copy.deepcopy(l1)
# l2[1] =   2.2
# l2[2][0]= 3.14
# print(l1)
# print(l2)

# l1=[1,2,[3.1,3.2],"hello"]
# l2=l1.copy()
# import copy
# l3=copy.deepcopy(l1)
# l2[0]=100
# l3[2][0]= 3.14
# print(l1)
# print(l2)
# print(l3)

# 联系：
#     有字符串＂hello"，生成字符串＂h e l l o"和"h-e-l-l-o"
# s="hello"
# l=list(s)
# l2=" ".join(l)
# print(l2)
# l3="-".join(l)
# print(l3)

# 生成一个数字1~9的整数的平方的列表，即：
# Ｌ=[1,4,9,25,36...81]
# L=[]
# for x in range(1,10):
#     L.append(x**2)
# print(L)
# L2=[x**2 for x in range(1,10)]
# print(L2)
#
# 练习：
#     用列表退到式生成1~100　内所有奇数的列表
# l=[x for x in range(1,100,2)]
# print(l)
# 生成一个数字1~9的奇数的平方的列表，即：
# l=[x**2 for x in range(1,10) if x%2==1]
# print(l)
# l=[x**2 for x in range(1,10,2)]
# print(l)
# 用字符串＂ＡＢＣ＂和字符串＂１２３＂生成如下列表：
#
# l=[x+y for x in "123" for y in "ABC"]
# print(l)
# 练习：
# 1.输入一个开始的整数用begin绑定
#     输入一个结束的整数用end绑定
#     将从begin开始，到end结束（不包含end）的偶数存于列表中，
#     并打印此列表
#     （建议用列表推导式实现）
# 2.已知有字符串：
#     s='100,200,300,500,800'
#     将其转化为列表，列表内部为位数字:
#     L＝[100,200,300,500,800]
# 3.已知有一个列表中存有很多数，还有重复的，如：
#     L=[1,3,2,1,6,4,2,...98,82]
#     1)　将列表中出现数字存入一个列表L2中
#         要求：重复出现多次的数字只能在L2中保留一份（去重）
#     2) 将L列表中出现两次的数字存于另外一个列表L3中，在L3中只
#     保留一份
# 4．写程序，生成前４０个斐波那契数（Fibonacci）
#     1 1 2 3 5 8 13...
#     要求将这些数存于一个列表中，最后打印这些数
# 练习：
# 1.
# begin=int(input("请输入一个开始的整数"))
# end=int(input("请输入一个结束的整数"))
# L=[x for x in range(begin,end)if x%2==0]
# print(L)

# 2.
# s='100,200,300,500,800'
# l=s.split(",")
# L=[int(x) for x in l]
# print(L)

# 3.
# l=[1,2,3,45,5,6,6,7,65,65,16,16]
# l2=[]
# l3=[]
# for x in l:
#     if x in l2:
#         pass
#     else:
#         l2.append(x)
#     if l.count(x)==2 and x not in l3:
#         l3.append(x)
# print(l2)
# print(l3)

# 4.
# x=0
# y=1
# l=[]
# while len(l)<40:
#     l.append(y)
#     x,y=y,x+y
# print(l)
# 方法2
# l=[1,1]
# while len(l)<40:
#     l.append(l[-1]+l[-2])
# print(l)

# L=reversed(l)
# print(list(L))
# # print(len(l))
# l=[1,5,6,7,3,16,16,2,2]
# # print(sorted(l))
# for x in l:
# #     L=l.count(x)
# # print(L)
#     L=l.remove(x)
# print(L)

# l=[1,5,6,7,3,16,16,2,2]
# l2=[]
# l3=[]
# for x in l:
#     if x not in l2:
#         l2.append(x)
#     if l.count(x)==2 and x not in l3:
#         l3.append(x)
# print(l2)
# print(l3)

# s='100,200,300,500,800'
# l=s.split(",")
# L=[int(x) for x in l]
# print(L)
# s='100,200,300,500,800'
# l=s.split(",")
# L=[int(x) for x in l]
# print(L)






