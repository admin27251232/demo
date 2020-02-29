# -*- coding:utf-8 -*-
# auth: Admin

def test1():
    print "test1"

def test2(a,b):
    print a
    print b

#数组传参
def test3(*args):
    print args

#json格式传参
def test4(**kwargs):
    print kwargs

test1()
test2(1,2)
test3(1,2,3,45,6,78,8)
test4(a=1,b=2,c=3,d=4,e=5)
