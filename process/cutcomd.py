# -*- coding: utf-8 -*-

# from subprocess import call
# call('ipconfig')

# from subprocess import Popen, PIPE
# # cmd = "ipconfig"

# videofile='17.mp4'
# # cmd='-FWidth 100 -FHeight 60 -OptSteps 10 -HeadSize 200 -HistorySize 5 -WindowSize 20 -DiffThreshold 35 -AcceptableDiffPercentPerWindow 40 -VsPath '+videopath+' -CPUFaceClassifier ../data/haarcascades/haarcascade_frontalface_alt.xml'
# # cmd='./YouTubeFilters.exe -FWidth 100 -FHeight 60 -OptSteps 10 -HeadSize 200 -HistorySize 5 -WindowSize 20 -DiffThreshold 35 -AcceptableDiffPercentPerWindow 40 -VsPath ../YouTubeFilters/tests/'+videofile+' -CPUFaceClassifier C:/Yushi/YouTubeFilters/data/haarcascades/haarcascade_frontalface_alt.xml'
# # +videofile+'.log'
# cmd='ipconfig'
# p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
# out, err = p.communicate()
# print "Return code: ", p.returncode
# print 'print begin: ',out.rstrip(), err.rstrip()

import os
# cmd='./YouTubeFilters.exe -FWidth 100 -FHeight 60 -OptSteps 10 -HeadSize 200 -HistorySize 5 -WindowSize 20 -DiffThreshold 35 -AcceptableDiffPercentPerWindow 40 -VsPath ../YouTubeFilters/tests/'+videofile+' -CPUFaceClassifier C:/Yushi/YouTubeFilters/data/haarcascades/haarcascade_frontalface_alt.xml'
# cmd='ipconfig'
file=open(logfile)
record=file.readlines()
file.close()
begin=1
for i in range(len(record)):
    record[i]=record[i].strip()

videofile='9.mp4'
starttime=2.3
lastframe=300
frameRate=30
endtime=starttime+lastframe/frameRate
cmd='ffmpeg.exe -i '+videofile+' -ss '+str(starttime)+' -vframes '+str(lastframe)+' -y -f mp4 '+videofile[0:-4]+'_'+str(starttime)+'_'+str(endtime)+'.mp4'
tmp = os.popen(cmd).readlines()
print tmp
# fp=open('file/cmdput.txt','a')
# for line in tmp:
#     fp.write(line)
# fp.close()

