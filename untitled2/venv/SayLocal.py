# -*- coding: utf-8 -*-
"""
本地语音文件识别测试
"""
import speech_recognition as sr
import sys

say = '你看看'
r = sr.Recognizer()
print '111111111111111111111111'
# 本地语音测试
#harvard = sr.AudioFile(sys.path[0]+'/youseesee.wav')
harvard = sr.AudioFile('/tmp/t1.wav')
print '222222222222222222222222'
with harvard as source:
    print '1133333333333333333'
    # 去噪
    r.adjust_for_ambient_noise(source, duration=0.2)
    audio = r.record(source)
    print '2233333333333333333'

print '4444444444444444444444444'
# 语音识别
test = r.recognize_google(audio, language="cmn-Hans-CN", show_all=True)
print(test)
print '55555555555555555555555555'

# 分析语音
flag = False
for t in test['alternative']:
    print(t)
    if say in t['transcript']:
        flag = True
        break
if flag:
    print('Bingo')