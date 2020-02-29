# -*- coding:utf-8 -*-
import speech_recognition as sr

r = sr.Recognizer()

test = sr.AudioFile('/tmp/t1.wav')
print test
with test as source:
    audio = r.record(source)

type(audio)


#r.recognize_google(audio, language='zh-CN', show_all=True)
