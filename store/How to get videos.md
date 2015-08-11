How to get videos

1. get the link of user, channel, playlist 
2. deal with the links & get the link of videos  getlink.py
3. download the video youtube-dl
./youtube-dl --batch-file playlist_profiling_2.txt -i --write-sub --write-auto-sub --sub-lang 'en' -r 40M -R 5 --write-description --write-info-json --write-annotations --socket-timeout 10 -o '../../../video/profiling/%(uploader)s_%(title)s_%(uploader_id)s_%(id)s_%(format)s.%(ext)s'

./youtube-dl --batch-file playlist_sentiment.txt -i --write-sub --write-auto-sub --sub-lang 'en' -r 40M -R 5 --write-description --write-info-json --write-annotations --socket-timeout 10 -o '../../../video/sentiment/%(uploader)s_%(title)s_%(uploader_id)s_%(id)s_%(format)s.%(ext)s'

4. transform srt to txt srt2txt.py
5. change the name and print out the inputlist changename.py & getpath.py