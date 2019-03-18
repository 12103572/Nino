'''
回顾：
    生成器 Generator
        能够动态提供数据的可迭代对象(现用现生成)
    两种生成器：
        1.生成器函数
            def myyield():
                yield 1  #生成的数据是给next(it) 函数
                yield 2
            yield 语句：
                yield 表达式
            访问生成器的方式：
                1.迭代器
                2.for  in 语句或各种推导式
        2.生成器表达式
        语法：
        (x**2 for x in range(10))
    迭代工具函数：
        zip(可迭代对象1，可迭代对象2，...)
        enumerate(可迭代对象，start=0)  #(索引，值)
字节 byte
    1字节(byte) = 8位(bit)
字节串 bytes 和字节数组 bytearray
字节串：
    创建
     字面值：
     b"hello"
      构造函数
        bytes()
        bytes(10)
        bytes(range(65,70))
        bytes("ABCD","utf-8")
字节数组
    创建：
        构造函数bytearray
            与字节一致
bytes 和 bytearray 的运算：
+ += * *=
<  <= > >= == !=
in/ not in
索引/切片
函数：
    len(x)  min(x)  max(x)  sum(x)    all(x)   any(x)

字符串 和 字节串 互转
    b = s.encode('utf-8')
    s = b.decode('utf-8')
    ba = bytearray(b'1234')
    s2 = ba.decode() # 可以的
字节数组的方法：
    B.clear()   清空
    B.append(x)  追加
    B.remove()   清空
       '''

#
# 练习：
#     自己写一个文件 info.txt 内容写入如下一些文字信息
#         张三    20  100
#         李四    21  96
#         小王    22  98
#         写程序将这些数据读取出来，并以如下格式打印在屏幕终端上
#         张三  今年  20 岁，成绩是：100
#         李四  今年  21 岁，成绩是：96
#         小王  今年  22 岁，成绩是：98

# try:
#     myinfo = open("info.txt.py",encoding='utf-8')
#     '''读取info.txt.py 内容，形成字典的列表返回'''
#     print("打开文件成功")
#     while True:
#         s= myinfo.readlines()
#         if not s :
#             print("读取文件结束")
#             break
#         s2 = s.rstrip() #去掉右边的空白字符
#         n,a,s=s2.split()
#         a = int(a)
#         s = int(s)
#         L.append(dick(name=n,age=a,score=s))
#     myinfo.close()
#     print("文件关闭成功")
# except OSError:
#     print("打开文件失败")

# 练习：
#     1.写一个程序，让用户输入很多个正整数，
#     最后将这些整数，存入文件， mynumbers.txt中
#     如：
#         请输入：1
#         请输入：2
#         请输入：3
#         请输入：4
#         请输入：-1 #结束
#         格式自己定义
#     2.写一个程序，将上一个程序输入的内容从 mynumbers文件中读取
#     出来，打印:和

# try:
#     fw = open("mynumbers.txt.py","w",encoding='utf-8')
#     L=[]
#     while True:
#         s=int(input("请输入正整数"))
#         if s == -1:
#             break
#         else:
#             L.append(s)
#         fw.write(str(s))
#         fw.write("\n")
#     fw.close()
#     print("写入文件成功")
# except :
#     print("写入文件失败")
# print("和是：",sum(L))

# 方法2：
# try:
#     fw = open("mynumbers.txt.py","w",encoding="utf-8")
#     #读取数据并写入文件中：
#     try:
#         while True:
#             n = int(input("请输入正整数"))
#             if n<0:
#                 break
#             fw.write(str(n))
#             fw.write("\n")
#     finally:
#         fw.close()
# except OSError:
#     print("打开失败！")
# except ValueError:
#     print("输入内容错误！")
#
# try:
#     fr = open("mynumbers.txt.py","r",encoding="utf-8")
#     L=[]
#     while True:
#         s = fr.readline()
#         if not s :
#             break
#         L.append(int(s.rstrip))
#     fr.close()
# except:
#     print("打开文件失败")
# print(sum(L))

# 练习:
#     1.写程序,实现文件的复制,(注:只复制文件,不复制文件夹)
#         要求:
#         1)  要考虑文件关闭的问题
#         2)  要考虑超大文件无法一下加载到内存的问题
#         3)  要能复制二进制文件(非文本文件)
#     2.为原学生信息管理程序添加两个功能:
#         9) 从文件中读取数据(si.txt)
#         10) 保存信息到文件(si.txt)
#         说明:
#         9)  相当于打开文件功能
#         10) 相当于保存功能
def copy(scr_file,dst_file):
    '''scr_file: 源文件名
        dst_file: 目标文件名'''
    try:
        fr = open(scr_file,"rb")
        try:
            fw = open(dst_file,"wb")
            try:
                while True:
                    b = fr.read(4096)
                    if not b:
                        break
                    fw.write(b)
            finally:
                fw.close()
        finally:
            fr.close()
        return True
    except OSError:
        return False
scr = input("请输入源文件名")
dst = input("请输入目标文件名")
if copy(scr,dst):
    print("复制文件成功！")
else:
    print("复制文件失败！")
# mywork.txt.py