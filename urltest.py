import re
import sys,os, urllib, urllib2, time, random, cookielib
import threading

linklist=['https://www.youtube.com/user/AynRandInstitute']
for link in linklist:
    # to do :
    # if the url include playlist, then don't add videos in the end
    source_url=link+'/videos'
    # 
    html=urllib2.urlopen(source_url)
    data=html.read()
    file=open('html.txt','a')
    file.write(data)
    file.close()

    # pattern=re.compile(r'href="/watch?v=.+"')
    pattern=re.compile(r'href=\"\/watch\?v\=.+?\"')
    match=pattern.findall(data)
    print match
    file=open('playlist.txt','a')
    file.write(str(len(match))+'\n')
    for video in match:
        file.write(str(video)+'\n')
    file.close()
