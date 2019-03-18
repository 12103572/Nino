l1='1,2,3,10,20,30'
import copy
l2=copy.deepcopy(l1)
print(l1)
print(l2)
l3=l2.split(',')
l=[int(x) for x in l3]
print(l)

# l='10,20,30'
# l2=l.split(',')
# print(l2)
# L=[int(x) for x in l2]
# print(L)

# l=1,2,3,'10,20,30'
# a='10,20,30'
# l2=a.split(',')
# l3=[int(x) for x in l2]
# print(l3)
# l=[1,2,3,l3]
# print(l)

# l=[1,2,3,4,16,16,1,7,17,6,6,8,8]
# l2=[]
# l3=[]
# print(l2)
# for x in l:
#     if x not in l2:
#         l2.append(x)
#     if l.count(x)==2 and x not in l3:
#         l3.append(x)
# print(sorted(l2))
# print((l3))

# l=[1,1]
# x=1
# y=1
# z=x+y
# a=len(l)
# for a in range(1,39):
#     l.append(z)
#     x=y
#     y=z
#     z=x+y
# print(l)
# print(len(l))

# # 回顾：
# 列表
#     索引和切片
#         取值
#             v=列表[整数表达式]
#             lst2= 列表[开始：结束：步长] #返回列表
#         赋值
#             列表[整数表达式]=v
#             列表[开始：结束：步长]=可迭代对象
# del 语句
#     del 列表[整数表达式]
#     del 列表[开始：结束：步长]
#     增加、删除、修改
# 可变对象：增。删、改 查
# 不可变对象：查
#
# 函数：
#     len(x) max(x) min(x) sum(x) any(x) all(x)
#     reversed(x) 将可迭代对象反转，返回另一个可迭代对象
#     sorted(x reversed=False) 排序（默认为升排序）
# 列表的方法：
#     l.append(x)  #追加
#     l.extend(可迭代对象)  #作用类似于l+=(可迭代对象)
#     l.count(x)  x在列表l中重复数字的次数
#     l.copy()    浅拷贝
#     l.remove(x) 删除
#     l.pop([索引]) 移除（去除）返回取出来的数据
#     l.clear() 清空
#     l.inserst([索引,obj]) 插入
#     l.sorted    作用于所有可以排序的对象
#     l.reversed()    作用于所有可以反向排序的对象
#
# 深拷贝和浅拷贝
#     不拷贝
#     l=l1    两个变量同时绑定同一个对象
#     浅拷贝：
#     l=l1.copy()  或l=l1[::] 只复制一层，深层对象共同拥有
#     深拷贝：
#     import copy
#     l=copy.deepcopy(l1)  #复制整数树形关联的对象
#
#     文本解析方法：
#     s,split(sep=None)   默认按照字符拆
#     s.splitlines()      默认按照换行符拆
#     s.join(字符串可迭代对象)
#
# 列表推导式：
#     创建列表的表达式
#     [表达式 for 变量 in 可迭代对象 if 真值表达式......]

# 1.生成0-9的整数的平方的元组，元组如下：
# （1,4,9,16，...81）
# t=()
# for x in range(1,10):
#     t=t+(x**2,)
# print(t)

# print(tuple([x**2 for x in range(1,10)]))

# d={'姓名':'tarena','年龄':15}
# print(len(d))

# L = [(1, 2), [3, 4], "AB"]
# d = dict(L) # d={1:2,3:4,‘A':'B'}
# print(d)

# d=dict(name='tarena',age=15)
# print(d)

# d={'name':'tarena','age':20}
# print(d['name'],'今年',d['age'],'岁')

# d = {}
# d['name'] = 'tarena'  # 创建'name'键，对应’tarena'
# d['age'] = 16  # 创建'age'键，绑定16
# d['age'] = 18  # 修改'age'键，绑定18
# d['sex']='girl'
# print(d)  #
# del d['sex']
# print(d)

# 练习:
#     1)写程序,将如下信息形成一个字典　seasons
#         '键'        '值'
#         1           '春季有1,2,3月'
#         2           '夏季有４,5,6月'
#         3           '秋季有7,8,9月'
#         4           '冬季有10,11,12月'
#     2) 让用户输入一个整数代表这个季度，打印这个季度的信息，
# #     如果用户输入的信息不在字典内，则打印"信息不存在"
# d={}                              #创建空字典
# d[1]='春季有1,2,3月'              #把对应的‘键’-‘值’添加到字典中
# d[2]='夏季有4,5,6月'
# d[3]='秋季有7,8,9月'
# d[4]='冬季有10,11,12月'
# print(d)                            #输出字典
# a=int(input("请输入1-4的整数"))
# if a in d:                           #如果a在字典d中，分别把键值对输出
#     print(d[a])
# else:                                    #输入的数不在字典中，则输入错误
#     print("信息不存在")

# d={'一':1,'二':2,'三':3}
# for key in d:
#     print("键",key,"值",d[key])

# 练习:
#     输入一段字符串，打印出这个字符串出现过的字符及出现过的字次数
#     如:
#         请输入:abcdabcaba
#         打印:
#             a:4次
#             b:3次
#             d:1次
#             c:2次
# #             不要求打印次序
# d={}
# a=input("请输入一段字符串")
# for x in a :
#     d[x]=a.count(x)
# print(d)



# 练习:
#     写一个程序，
#       1)输入一些单词和解释，将单词作为键，解释作为值
#     存于字典中，当输入单词为空时结束输入
#     ２）然后进入查词过程（死循环）
#         输入单词，如果单词在字典中，则显示解释内容
#         如果单词不存在，则提示"没有此单词"
# d={}
# while True:
#     a=input("输入单词")
#     if a=='':
#         break
#     b = input("输入解释")
#     d[a]=b
# print(d)
# while True:
#     c=input("请输入您要查询的单词")
#     if c in d:
#         print(d[c])
#     else:
#         print("没有此单词")

# 练习：
#     有如下字符串列表:
#     L＝['tarena','xiaozhang'','hello']
#     请生成如下字典：
#     d={'tarena':6,'xiaozhang':9,'hello':5}
#     值为键的长度
# L=['tarena','laowang','hello']
# d={x:len(x) for x in L}
# print(d)

# 练习:
#     一直有两个等长度的列表list1　和list2，生成相应字典
# list1=[1001,1002,1005,1008]
# list2=['Tom','Jerry','Spike','Type']
#     生成的字典为：
#     {'Tom':1001....}
#方法1:
# list1=[1001,1002,1005,1008]
# list2=['Tom','Jerry','Spike','Type']
# d={}
# for x in range(len(list1)):
#     d[list2[x]]=list1[x]
# print(d)
# # 方法2：
# d={}
# for k in list2:
#     d[k]=list1[list2.index(k)]
# print(d)
#方法3
# d={list2[i]:list1[i]for i in range(len(list1))}
# print(d)

# 练习:
# 1.有一只小猴子，摘了很多桃。
#     第一天吃了全部桃子的一半，感觉不饱，又吃了一个
#     第二天吃了剩下的一半，感觉不饱又吃了一个
#     ...以此类推
#     到了第十天，发现只剩一个了
#     请问一天摘了多少桃子？
# 2.写一个程序，实现一个带有菜单界面的字典程序
#     菜单如下:
#         1)添加单词
#         2)删除单词
#         3)查找单词
#         4)q退出
#     示意见：
#     d={}  #先有个容器
#     while True:
#         1)添加单词
#         2)删除单词
#         3)查找单词
#         4)q退出
#         s=int("请选择")
#         if s=="1":
#             pass
#         elif s=="2":
#             pass
#         elif s=="3":
#             pass
#         elif s=="4":
#             break
# 3.项目　(学生信息管理)
#    输入任意个学生的信息，形成字典后存入列表
#         学生信息有：姓名，年龄，成绩
#     如:
#         请输入姓名：tarena
#         请输入年龄：age
#         请输入成绩：９９
#         请输入姓名：name2
#         请输入年龄：20
#         请输入成绩：80
#         请输入姓名:<回车> 结束输入
#     形成内部存储格式如下:
# infos=[{'name':'tarena','age':15,'score':99},
#     {'name':'name2','age':20,'score':80}]
# #第二步以表格的方式打印上述列表的内容:
# +-----------+---------+--------+
# | 姓名      ｜   年龄  |    成绩 ｜
# +-----------+---------+--------+
# |  tarena   |   15    |   99   |
# |   name2   |   18    |    80  |
# +-----------+---------+--------+

# 1.
# s=1
# for a in range(9,0,-1):
#     s=(s+1)*2
# print("第",a,"天有",s,"个桃")

# 2.
# d={}
# while True:
#     print("1","添加单词")
#     print("2","删除单词")
#     print("3","查找单词")
#     print("q","退出")
#     s = int(input("请选择选项"))
#     if s=="1":
#         key=input("请输入要添加的单词")
#         value=input("请输入解释")
#         if key in d :
#             print("单词已经存在，添加失败！")
#         else:
#             d[key]=value
#             print("添加成功！")
#     if s=="2":
#         key=input("输入您想删除的单词")
#         if key in d:
#             print("删除成功！")
#             del d[key]
#         else:
#             print("删除失败！")
#     if  s=="3":
#         key=input("请输入您要查找的单词")
#         if key in d:
#             print("单词的解释是:",d[key])
#         else:
#             print("您输入的单词并不在字典中!")
#     if  s=="q":
#         break

# 3.
# l=[]
# while True:
#     d={}
#     a=input("请输入姓名")
#     if a=='':
#         break
#     b = int(input("请输入年龄"))
#     c = int(input("请输入成绩"))
#     d["姓名"]=a
#     # print("姓名:",d)
#     d["年龄"]=b
#     # print("年龄:",d)
#     d["成绩"]=c
#     # print("infors=",d)
#     l.append(d)
# print(l)
# print("+---------------+----------+----------+")
# print("|    姓名       |   年龄   |   成绩   |")
# print("+---------------+----------+----------+")
# for d in l:
#     print("|"+d["姓名"].center(12),'|'+str(d["年龄"]).center(9),"|"+str(d["成绩"]).center(10)+"|")
# print("+---------------+----------+----------+")

# d={}
# a=input("输入一段字符串")
# for x in a :
#     d[x]=a.count(x)
# print(d)

# d={}
# L=['tarena', 'xiaozhang','hello']
# for x in L:
#     d[x]=len(x)
# print(d)

# list1 = [1001, 1002, 1005, 1008]
# list2 = ['Tom', 'Jerry', 'Spike', 'Type']
# d={}
# for x in range(len(list1)):
#     d[list1[x]]=list2[x]
# print(d)



