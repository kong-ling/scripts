import speech_recognition as sr

import os
os.environ['http_proxy'] = 'lingkong:pass@proxy'
os.environ['HTTP_PROXY'] = 'lingkong:Tswcby^6@proxy'
os.environ['https_proxy'] = 'lingkong:Tswcby^6@proxy'
os.environ['HTTPS_PROXY'] = 'proxy'

r = sr.Recognizer()

harvard = sr.AudioFile('./m4.wav')
#harvard = sr.AudioFile('./e1.wav')

with harvard as source:
    audio = r.record(source)
#    audio1 = r.record(source,duration = 4)
#    audio2 = r.record(source,duration = 4)

#r.recognize_google(audio1, language='zh-CN', show_all= True)
#r.recognize_google(audio2, language='zh-CN', show_all= True)
print(r.recognize_google(audio, language='zh-CN', show_all= True))

