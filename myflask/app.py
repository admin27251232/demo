# -*- coding:utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
import time

app = Flask(__name__)

def timer(type):
    def out_deco(func):
        def deco(*args, **kwargs):
            startTime = time.time()
            res = func(*args, **kwargs)
            endTime = time.time()
            print func, "执行时间：", (endTime - startTime)
            return res
        return deco
    return out_deco


@app.route('/')
#@timer(type="index")
def hello_world():
    # return 'Hello World!'
    return render_template("html/home.html")


@app.route('/home')
@timer(type="home")
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
