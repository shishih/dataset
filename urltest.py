import re
import sys,os, urllib, urllib2, time, random, cookielib
import threading

file=open('channellist_sentiment.txt')
linklist=file.readlines()
file.close()

# linklist=['https://www.youtube.com/user/vertmb','https://www.youtube.com/user/tyleroakley','https://www.youtube.com/user/SeaLemonDIY','https://www.youtube.com/user/RobertoCPR','https://www.youtube.com/user/vertmb','https://www.youtube.com/user/myCNAjobs','https://www.youtube.com/user/pdflm','https://www.youtube.com/user/KatiMorton','https://www.youtube.com/user/PapuKiBaatain','https://www.youtube.com/user/talkingdownthesun','https://www.youtube.com/user/FlixRaider','https://www.youtube.com/user/networkpowercouple1','https://www.youtube.com/user/mlmcompanyreviewinfo','https://www.youtube.com/channel/UCwXy-j5GvXzgHbWrdjxkuYQ','https://www.youtube.com/channel/UCc8mfwWDH9Ur3wlVOXHkfPQ','https://www.youtube.com/channel/UC2gJdSRG6-Za5hzkzMz-uYw','https://www.youtube.com/user/hannahgirasol','https://www.youtube.com/channel/UCo-7xq2D-T5d06bDWazRK7g','https://www.youtube.com/channel/UC-p8Eaq7vTezQH_fCl2qegQ','https://www.youtube.com/channel/UCTelsunftpnisc5bkLqOL6Q','https://www.youtube.com/user/MrRyden94','https://www.youtube.com/user/marc2live','https://www.youtube.com/user/quietasmouse','https://www.youtube.com/user/savanamazing','https://www.youtube.com/user/tracireuter','https://www.youtube.com/user/StrongMindSet','https://www.youtube.com/user/HomeBusinessIdeas101','https://www.youtube.com/user/akadobiz','https://www.youtube.com/channel/UCc8mfwWDH9Ur3wlVOXHkfPQ','https://www.youtube.com/channel/UCULTq0HbqiI-kXLRs51iI6A','https://www.youtube.com/playlist?list=PLc6-qdSNfAOa3Dl0iOzcrL9VviNwxyJNc','https://www.youtube.com/playlist?list=PLRJNAhZxtqH8Awya4iITQ9-ffknKeVEnw','https://www.youtube.com/playlist?list=PLRJNAhZxtqH9rgU-W1SqojlC27wSDg6jC','https://www.youtube.com/playlist?list=PLD195797A7B28B75D','https://www.youtube.com/channel/UCxwbFLOlKDsXrwizV5jah7g/','https://www.youtube.com/channel/UCPVEZgw-VbDRbLV1MRGVQNQ','https://www.youtube.com/user/RepAndyBarr/','https://www.youtube.com/channel/UCtVl3kb7Xvt3pY7l6x-M6LA','https://www.youtube.com/user/XavierBecerra','https://www.youtube.com/user/CongressmanDan','https://www.youtube.com/user/RepGusBilirakis','https://www.youtube.com/user/RepBlumenauer','https://www.youtube.com/user/JohnBoehner','https://www.youtube.com/user/BradyPA01','https://www.youtube.com/user/RepMoBrooks','https://www.youtube.com/user/SusanWBrooks','https://www.youtube.com/user/RepJuliaBrownley','https://www.youtube.com/channel/UCHK7Wcwij7NoxXGTeSHUWzg','https://www.youtube.com/user/MichaelCBurgessMD','https://www.youtube.com/user/GKBNC01','https://www.youtube.com/user/RepKenCalvert','https://www.youtube.com/user/RepLoisCapps','https://www.youtube.com/user/RepMikeCapuano','https://www.youtube.com/user/RepKathyCastor','https://www.youtube.com/user/CongressmanChabot','https://www.youtube.com/user/RepJudyChu','https://www.youtube.com/user/repcleaver','https://www.youtube.com/playlist?list=PL179C4AB4A9A05D59','https://www.youtube.com/channel/UCJzU_8Bwz1lUyP1qz84L5jw','https://www.youtube.com/user/RepRodneyDavis','https://www.youtube.com/playlist?list=PLh5fBPfO7PDXMxMery81akTduyDIQF_my','https://www.youtube.com/user/CongressmanDent','https://www.youtube.com/playlist?list=PLfBlGAhBGQxsz8mty7Y4P1FlsQbRFm0am','https://www.youtube.com/playlist?list=PLfBlGAhBGQxsx78j6vuDOuOqP0_OT-lfg','https://www.youtube.com/playlist?list=PLfBlGAhBGQxv5s6Dgkd-PsZydDwno1k_G','https://www.youtube.com/channel/UCWMjA9uDEA7KGZmjctobg5w','https://www.youtube.com/playlist?list=PLCF9D37A7E881588D','https://www.youtube.com/user/doggett']
for link in linklist:
    # deal with different kind of links, including video, user, channel and playlist
    link=link.strip('\r\n')
    patternList=re.compile(r'playlist')
    matchList=patternList.search(link)
    patternWatch=re.compile(r'watch')
    matchWatch=patternWatch.search(link)
    if matchList:
        source_url=link
    elif matchWatch:
        source_url=link
    else:
        source_url=link+'/videos'
    print 'source_url:',source_url

    # get the links of video
    

    html=urllib2.urlopen(source_url)
    data=html.read()
    # file=open('html.txt','a')
    # file.write(data)
    # file.close()

    pattern=re.compile(r'\/watch\?v\=.+?\"')
    match=pattern.findall(data)
    print match
    file=open('playlist_sentiment.txt','a')
    file.write(str(len(match))+' '+source_url+'\n')
    for video in match:
        file.write('https://www.youtube.com'+str(video)+'\n')
    file.close()

    waitTime=random.uniform(15,30)
    print 'sleep'
    time.sleep(waitTime)