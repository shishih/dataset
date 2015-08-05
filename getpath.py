# coding: utf-8 -*-

import os
import string

def getname(path):
    nameList=[]
    initList=os.listdir(path)
    for filename in initList:
        nameList.append(os.path.splitext(filename))
    return nameList
def getSrt(nameList,file,path):
    for name in nameList:
        if name[1]=='.srt':
            file.write(name[0]+name[1]+'\n')
def getInput(nameList,file,path):
    srtName=''
    videoname=''
    txtname=''
    videoDic={}
    for name in nameList:
        if string.find(name[0],' ')!=-1:
            print 'error'
        if name[1]=='.mp4':
            if videoDic.has_key(name[0]):
                file.write(path+name[0]+'.mp4'+',,'+path+name[0]+'.en.txt'+'\n')
            else:
                videoDic[name[0]]=1

        elif name[1]=='.srt':
            if videoDic.has_key(name[0][:-3]):
                file.write(path+name[0][:-3]+'.mp4'+',,'+path+name[0][:-3]+'.en.txt'+'\n')
            else:
                videoDic[name[0][:-3]]=1
def main():
    # path='E:/users/yushiy/video/profiling/'
    path='F:\Research\Video\Dataset\pathtest'
    nameList=getname(path)
    # print nameList
    # file=open('srtlist_sentiment.txt','a')
    # getSrt(nameList,file,path)
    # file.close()
    file=open('inputList.txt','a')
    getInput(nameList,file,path)
    file.close()

if __name__ == '__main__':
    main()