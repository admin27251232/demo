# -*- coding:utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
import time

app = Flask(__name__)

def timer(func=None,param=None):
    print "111111111111111111111111:",func,param
    def out_deco(func):
        def deco(*args, **kwargs):
            startTime = time.time()
            res = func(*args, **kwargs)
            endTime = time.time()
            print "22222222222222222222222:", func, param
            print func, "执行时间：", (endTime - startTime)
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
    return render_template("html/home.html")


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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8899, debug=True)
