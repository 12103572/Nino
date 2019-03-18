try:
    fw = open("mywork.txt.py","r",encoding='utf-8')
    print("打开文件成功！")
    for x in fw:
        print(x)
except OSError:
    print("文件打开失败！")
try:
    fw2 = open("mywork1.txt.py","w",encoding='utf-8')
    fw2.write("平安夜快乐!""\n")
    fw2.write("圣诞节快乐!""\n")
    fw2.flush()
    fw2.close()
    print("文件已关闭！")
except OSError:
    print("文件打开失败！")
