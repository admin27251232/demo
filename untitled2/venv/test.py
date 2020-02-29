#coding=utf-8
#__author__ = 'Yong'

import flask
import psutil
import sys
import speech_recognition as sr

for i in psutil.disk_partitions():
    print i[0],i[1],psutil.disk_usage(i[1])[3]

print "---------------"
print psutil.os.uname()
print psutil.os.getlogin()
print psutil.os.ctermid()
print "---------------"
print psutil.cpu_count()
print psutil.cpu_percent()
print psutil.cpu_stats()
print "---------------"
print psutil.swap_memory()
print "---------------"
print psutil.net_connections()
print "---------------"
print psutil.sys.getcheckinterval()
print psutil.net_if_stats()['virbr0'].speed
print psutil.net_if_stats()['wlp3s0'].speed
#print psutil.net_if_stats()['docker0'].speed
print sys.getdefaultencoding()

#print ("zheyangjiukeyile？？？？？？？？？？？？？？？？？？？")