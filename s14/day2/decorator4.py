# -*- coding:utf-8 -*-
# auth: Admin
#  装饰器的是运用定义

import time

def timer(func): #该参数为被装饰函数的内存地址，或说函数对象
    def deco(*args,**kwargs): #被装饰的函数有可能存在各种参数或没有参数 ，所以需要设定动态参数
        startTime = time.time()
        res = func(*args,**kwargs)
        endTime = time.time()
        print "函数执行时间为：%s" %(endTime-startTime)
        return res #为了test3()所写
    return deco

@timer
def test1():
    time.sleep(1)
    print "in the test1"

@timer
def test2(name,age):
    time.sleep(1)
    print "in the test2",name,age

@timer
def test3(name,age):
    time.sleep(1)
    print "in the test2",name,age
    return "WO you fan hui zhi "

test1()
test2("Admin",22)
print(test3("Admin",33))
