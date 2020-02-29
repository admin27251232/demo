# -*- coding:utf-8 -*-
# auth: Admin


_user = "admin"
_pwd = "123"

#user = input("请输入用户名：") #需要输入表达是，例如字符串：‘admin’
user = raw_input("请输入用户名：")
#pwd = input("请输入密码：")
pwd = raw_input("请输入密码：")

if (user == _user and pwd == _pwd):
    print "登陆成功！"
else:
    print "帐号密码错误！"
    #continue
