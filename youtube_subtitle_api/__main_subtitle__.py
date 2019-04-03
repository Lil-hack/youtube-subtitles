

import json


from youtube_subtitle_api import YouTubeTranscriptApi

import csv
import requests
import json
import sys
import io
import codecs
import os


def get_subtitles_and_write(namefile_read,namefile_write):
    with open(namefile_read+'.json', 'r', encoding="utf8") as f:
        data = json.loads(f.read())


    print(len(data))

    data2=[]
    for i in data:
        try:
            my_list = YouTubeTranscriptApi.get_transcript(i.get('id'))
            print(len(my_list))
            my_text = ''

            for item in my_list:

                if item.get('text')[0] != '[' and len(my_list)>100:
                    my_text = my_text + ' ' + item.get('text')
            i['text'] = my_text
            if my_text!='':
                data2.append(json.dumps(i, ensure_ascii=False))
            print(i)
        except:
            pass

    # print(str(data2))

    data3=[]
    for i in range(0,len(data2)):
        # print (data2[i])
        data3.append(data2[i])
        # new_dict = dict(zip(item.key, item.value))

    with io.open(namefile_write+'.json', 'w', encoding='utf8') as json_file:
        data3 = json.dumps(data2, ensure_ascii=False)

        json_file.write(data3)

if __name__ == '__main__':

     get_subtitles_and_write('video','DataSet_video_subtitles')
     get_subtitles_and_write('video2', 'DataSet_video_subtitles2')
     get_subtitles_and_write('video4', 'DataSet_video_subtitles4')
     get_subtitles_and_write('video5', 'DataSet_video_subtitles5')
     get_subtitles_and_write('video3', 'DataSet_video_subtitles3')



