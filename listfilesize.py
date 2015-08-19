# -*_ coding: utf-8 -*-
import os
import string
import re

#执行重命名功能
# path = 'F:/Research/Video/coursera/'
path = 'E:/users/yushiy/video/profiling_coursera/'

sublist=os.listdir(path)
# print dirlist
patternAnno=re.compile(r'\.annotations$')
patternInfo=re.compile(r'\.info$')
patternEn=re.compile(r'\.en$')
namelist=[]

fp=open('file/coursera_size.txt','a')
for sub in sublist:
    dirlist=os.listdir(path+sub)
    for file in dirlist:
        # mainname=patternEn.sub('',patternInfo.sub('',patternAnno.sub('',os.path.splitext(file)[0])))
        # if not mainname in namelist:
        #     namelist.append(mainname)

        ext=os.path.splitext(file)[1]
        print path,sub,file
        filesize=os.path.getsize(path+sub+'/'+file)
        
        # newname=str(namelist.index(mainname))+ext
        if ext=='.mp4':
            fp.write(str(sub)+'/'+file+'$'+str(filesize)+'\n')
        # if newname in os.listdir(path+sub):
        # # if newname in dirlist:
        #     os.remove(path+sub+'/'+file)
        # else:
        #     # filelist.write(str(newname)+'\n')
        #     os.rename(os.path.join(path+sub,file),os.path.join(path+sub,newname))
fp.close()