# -*- coding: utf-8 -*-

import msvcrt
from time import sleep
import sys
import threading
import os


def pwd_input():
    chars = []
    while True:
        try:
            newChar = msvcrt.getch().decode(encoding="utf-8")
        except:
            return input("你很可能不是在cmd命令行下运行，密码输入将不能隐藏:")
        if newChar in '\r\n':  # 如果是换行，则输入结束
            break
        elif newChar == '\b':  # 如果是退格，则删除密码末尾一位并且删除一个星号
            if chars:
                del chars[-1]
                msvcrt.putch('\b'.encode(encoding='utf-8'))  # 光标回退一格
                msvcrt.putch(' '.encode(encoding='utf-8'))  # 输出一个空格覆盖原来的星号
                msvcrt.putch('\b'.encode(encoding='utf-8'))  # 光标回退一格准备接受新的输入
        else:
            chars.append(newChar)
            msvcrt.putch('*'.encode(encoding='utf-8'))  # 显示为星号
    return (''.join(chars))


def t1():
    # pwd = input("please input password...\n")
    # print("\nyour password is:{}".format(pwd))
    while 1:
        print("1")
        sleep(2)
        os._exit(0)


def t2():
    while 1:
        print("2")
        sleep(1)


if __name__ == '__main__':
    thread2 = threading.Thread(target=t2)
    thread2.setDaemon(False)

    thread1 = threading.Thread(target=t1)
    thread1.setDaemon(False)


    thread1.start()
    thread2.start()

    #thread1.join()
    #thread2.join()

# main()
