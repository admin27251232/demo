# -*- coding:utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import session
import time
import psutil
import logging

import DBConfig

app = Flask(__name__)
# sessoin xuyao
app.config['SECRET_KEY'] = "123456"
#or
app.secret_key = "123456"
#热更新
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config.update({
    'DEBUG':True,
    'PORT':8899
})

app.config.from_object(DBConfig)
db = SQLAlchemy(app)

def timer(func=None,param=None):
    print "111111111111111111111111:",func,param
    def out_deco(func):
        def deco(*args, **kwargs):
            startTime = time.time()
            res = func(*args, **kwargs)
            endTime = time.time()
            print "22222222222222222222222:", func, param
            print func, "执行时间：【", (endTime - startTime),"】"
            return res

        print "---------------------------",deco.__name__ ,func.__name__
        deco.__name__ = func.__name__
        return deco
    #return out_deco
    return out_deco if not func else out_deco(func)
'''
def timer(func):
    def deco(*args, **kwargs):
        startTime = time.time()
        res = func(*args, **kwargs)
        endTime = time.time()
        print func, "执行时间：", (endTime - startTime)
        return res
    return deco
'''


@app.route('/')
@timer(func=None,param="helloworld")
def hello_world():
    # return 'Hello World!'
    dictRes = dict()
    for i in psutil.disk_partitions():
        print i[0], i[1], psutil.disk_usage(i[1])[3]
        dictRes[i[0]] = psutil.disk_usage(i[1])[3]

    context = {
        "getlogin"  : psutil.os.getlogin(),
        "ctermid"   : psutil.os.ctermid(),
        "cpu_count" : psutil.cpu_count(),
        "cpu_percent" : psutil.cpu_percent(),
        "cpu_stats" : psutil.cpu_stats(),
        "swap_memory" : psutil.swap_memory(),
        #"net_connections" : psutil.net_connections()
        "diskinfo"  : dictRes,
        "net_connections": ""
    }
    return render_template("html/index.html",**context)


@app.route('/req')
@timer(func=None,param="req_222")
def req1():
    res = request.args
    print res
    return res

@app.route('/home')
@timer(func=None,param="home_222")
def mhome():
    #get: request.args.get()
    #post: request.form.get()
    uname = request.args.get("uname")
    print uname
    context = {
        'uname' : uname,
        'age' : 18
    }
    return render_template("html/home.html",**context)
    # 使用url_for可以实现视图方法之间的内部跳转   ========  url_for("视图方法名")
    #return redirect(url_for("index"))

@app.route('/set_session')
@timer(func=None,param="setSession")
def set_session():
    print "SetSession"
    session["username"] = "xiaoming"
    return 'ok!'

@app.route('/get_session')
@timer(func=None,param="getSession")
def get_session():
    print "getSession"
    return session.get("username")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8899, debug=True)

