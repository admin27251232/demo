# -*- coding:utf-8 -*-
# auth: Admin
#  装饰器的是运用定义
#  模拟网站必须登陆状态

username = "admin"
password = "123"

def aut(auth_type): #这里就不能是func了，因为被装饰的函数向装饰器传参过来了
    print "被装饰函数传递到装饰器的参数：",auth_type
    def out_wrapper(func):# 新增一层嵌套函数，用于接受原有func参数
        def wrapper(*args, **kwargs):  # 非固定参数，非固定参数类型
            if auth_type == "local":
                print "zou de local............"
                user = raw_input("请输入用户名：")
                pwd = raw_input("请输入密码：")
                if (username == user and password == pwd):
                    print "帐号密码正确，可继续访问"
                    res = func(*args, **kwargs)
                    print "需要继续处理的业务逻辑..."
                    return res  # 之所以返回，是因为有些被装饰的函数，是有返回值的
                else:
                    print "帐号密码错误，退出使用"
                    exit("帐号密码错误，退出使用")  # 终止程序，后面内容不再运行
            elif  auth_type == "ldap":
                res = func(*args, **kwargs)
                print "zou de ldap..............."
                return res
        return wrapper

    return out_wrapper



def index():
    print "in the index"

@aut(auth_type="local")
def home():
    print "in the home"
    return "Home Return Result"

@aut(auth_type="ldap")
def bbs():
    print "in the bbs"

index()
print(home()) #有返回职的函数
bbs()