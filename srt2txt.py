# -*- coding: utf-8 -*-

import re

def trans(fileSrt,fileTxt):
    pattern=re.compile(r'^\d{1}.+\s')
    data=fileSrt.readlines()
    for line in data:
        match=pattern.search(line)
        if match:
            pass
        else:
            fileTxt.write(line)

def main():
    srtFile='srttest.srt'
    txtFile='txttest.txt'
    fileSrt=open(srtFile,'a')
    fileTxt=open(txtFile,'a')
    trans(fileSrt,fileTxt)
    fileSrt.close()
    fileTxt.close()

if __name__ == '__main__':
    main()