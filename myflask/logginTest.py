# -*- coding:utf-8 -*-
# auth: Admin

import logging

from functools import wraps
import logging
import traceback
from time import sleep
import DBConfig
import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# 查询时显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
app.config.from_object(DBConfig)
db = SQLAlchemy(app)




logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
)

def decoratore(func):
    @wraps(func)
    def log(*args,**kwargs):
        try:
            print
            logging.info(func.__name__)
            return func(*args,**kwargs)
        except Exception as e:
            logging.getLogger().error(func.__name__,"{func.__name__} is error,here are details:",{traceback.format_exc()})
    return log
'''
logger = logging.getLogger() #获取logger
# logging.basicConfig函数对日志的输出格式及方式做相关配置
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
)
'''

@decoratore
def usr():
    print "usr ......."
    sleep(1)

@decoratore
def pwd():
    print "pwd ......"
    sleep(1)

if __name__ == '__main__':
    print "is the main..."
    usr()
    pwd()
    print "end ..."

    # res = db.session.execute("select user,host from user;")
    # for itm in res:
    #     print itm

    sql = u""" select user,host from user where user = :user
                        """
    results = db.session.execute(sql, {"user": "root"})
    for itm in results:
        print itm

    # 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
    # logging.info('this is a loggging info message')
    # logging.debug('this is a loggging debug message')
    # logging.warning('this is loggging a warning message')
    # logging.error('this is an loggging error message')
    # logging.critical('this is a loggging critical message')


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    user = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True)
    pswd = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'User:%s' % self.name

'''

    创建表：db.create_all()
    删除表: db.drop_all()
    插入行:
    db.session.add()
    db.session.addAll([])
    db.session.commit()
    查询全部数据: User.query.all()
    过滤查询: User.query.filter_by(id=id).first()
    join多表查询：User.query.filter_by(env_id=env_id,id=id).join(Environments,Variable.env_id == Environments.id).first_or_404()
    count返回数量: User.query.filter_by(id=id).count()
    修改数据

#根据条件查询一行数据
admin_role = Role.query.filter_by(role_name = 'Amdmin').first()
#修改数据-
admin_role.role_name = 'Admin'
db.session.add(admin_role)
db.session.commit()

    删除数据：
    db.session.delete(User)
    db.session.commit()
    删除多条数据

variablelists= Variable.query.filter_by(env_id=env_id).all()

for var in variablelists:

    db.session.delete(var)

db.session.commit()

    直接执行sql语句

sql = u""" update net_internet_ip set removed = current_timestamp() where uuid not in :uuid and removed is null
                    """
results = db.session.execute(sql, {"uuid": uuid})
'''