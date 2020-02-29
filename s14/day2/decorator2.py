# -*- coding:utf-8 -*-
# auth: Admin

import time

def bar():
    time.sleep(3)
    print "in the bar"

def test1(func):
    startTime = time.time()
    func()
    endTime = time.time()
    print "函数执行时间为：%s" %(endTime-startTime)
#调用bar函数的门牌号，所谓的内存地址
test1(bar)
