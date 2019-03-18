#file:mypack/games/contra.py



def play():
    print("正在玩 魂斗罗...")

print("魂斗罗模块被加载!!!")

def gameove():
    '''此函数示意包的相对导入，在当前contra.py模块中
    导入上一级(mypack)里 meun.py里的show_menu,然后调用
    '''
   
print("游戏结束！！！")

import time
time.sleep(5)
#绝对导入
# from mypack.menu import show_menu
# show_menu()
#相对导入
from ..menu import show_menu
show_menu()


#ctrl + 鼠标左键  返回源码

