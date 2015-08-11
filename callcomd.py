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

cmd='ipconfig'
tmp = os.popen(cmd).readlines()
fp=open('file/cmdput.txt','a')
for line in tmp:
    fp.write(line)
fp.close()

