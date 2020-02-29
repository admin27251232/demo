# -*- coding:utf-8 -*-
# auth: Admin
#装饰器的实现
#1.函数即“变量”
#2.高阶函数  ; a.把一个函数名当作实参传递 ； b.返回值中包含函数名
#3.函数嵌套
#
#高阶函数 + 嵌套函数 = 装饰器

import time

def timmer(func):
    def warpper():
        print "zhuangshiqi"
        func()
    return warpper

@timmer
def test1():
    time.sleep(3)
    print "in the test1"

test1()