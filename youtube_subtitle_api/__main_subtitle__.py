

import json


from youtube_subtitle_api import YouTubeTranscriptApi

import csv
import requests
import json
import sys
import io
import codecs
import os

if __name__ == '__main__':



    with open('filename.json', 'r', encoding="utf8") as f:
        data = json.loads(f.read())
    with open('filename2.json', 'r', encoding="utf8") as f2:
        data =data+ json.loads(f2.read())
    with open('filename3.json', 'r', encoding="utf8") as f3:
        data = data + json.loads(f3.read())
    with open('filename4.json', 'r', encoding="utf8") as f4:
        data = data + json.loads(f4.read())
    with open('filename6.json', 'r', encoding="utf8") as f6:
        data = data + json.loads(f6.read())
    with open('filename7.json', 'r', encoding="utf8") as f7:
        data = data + json.loads(f7.read())

    print(data)
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
        print (data2[i])
        data3.append(data2[i])
        # new_dict = dict(zip(item.key, item.value))

    with io.open('data.json', 'w', encoding='utf8') as json_file:
        data3 = json.dumps(data2, ensure_ascii=False)

        json_file.write(data3)


    # print(my_list)
    # my_text=''
    # symbol='['
    # for item in my_list:
    #
    #     if item.get('text')[0]!=symbol:
    #         my_text=my_text+' '+item.get('text')
    #
    # print (my_text)