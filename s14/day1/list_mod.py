# -*- coding:utf-8 -*-
# auth: Admin

names = ["aaa","bbb","ccc","aaa","aaa"]

#新增
names.append("ddd")
print names

#新增制定位置
names.insert(1,"ABAB")
print names

#删除 method x 3
names.remove("ddd")
names.pop(2)
del names[1]
print names

#查找元素
print names.index("ccc")
print names.count("aaa")

#排序
names.sort()
print names

#清空
#names.clear()
print "------>：", names