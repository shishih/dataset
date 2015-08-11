# -*- coding: utf-8 -*-

file=open('inputlist.txt','a')
for i in range(1,1910):
    file.write(str(i)+'.mp4'+',,'+str(i)+'.txt'+'\n')

file.close()