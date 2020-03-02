# -*- coding:utf-8 -*-
# auth: Admin

DEBUG = True

DIALCT = 'mysql'
DRIVER = "mysqldb"
USERNAME = 'root'
PASSWORD = '123456'
HOST = '172.17.0.2'
PORT = '3306'
DBNAME = 'mysql'
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALCT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DBNAME)
SQLALCHEMY_TRACK_MODIFICATIONS = True        #没有此配置会导致警告

