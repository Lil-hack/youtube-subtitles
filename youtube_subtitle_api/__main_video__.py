
import json


from youtube_subtitle_api import YouTubeTranscriptApi

import csv
import requests
import json
import sys
import io
import codecs

def game_video_list(channel_id):
    """ Get channel's upload videos| 50 limit"""


    YOUTUBE_URI = 'https://www.googleapis.com/youtube/v3/search?key={}&channelId={}&part=snippet,id&order=date&maxResults=50'
    FORMAT_YOUTUBE_URI = YOUTUBE_URI.format('AIzaSyBeoPL5ypEieeoqZq1-wArJZ6kFp_72nMk', channel_id)

    content = requests.get(FORMAT_YOUTUBE_URI).text
    data = json.loads(content)
    print (data)
    video_list =[]
    keys = 'id', 'title', 'description', 'preview'
    print(data.get('nextPageToken'))

    pages=data.get('pageInfo').get('totalResults')//50
    next_token=data.get('nextPageToken')
    for item in data.get('items'):
            try:
                print(item)
                id = item.get('id').get('videoId')
                title = item.get('snippet').get('title')
                description = item.get('snippet').get('description')
                preview = item.get('snippet').get('thumbnails').get('high').get('url')

                values = id, title, description, preview

                if id:
                    video_item =dict(zip(keys, values))
                    video_list.append(video_item)
            except:
                pass
    for i in range(0,pages):
        try:
            YOUTUBE_URI2 = 'https://www.googleapis.com/youtube/v3/search?key={}&channelId={}&part=snippet,id&order=date&maxResults=50&pageToken={}'
            FORMAT_YOUTUBE_URI2 = YOUTUBE_URI2.format('AIzaSyBeoPL5ypEieeoqZq1-wArJZ6kFp_72nMk', channel_id, next_token)
            content2 = requests.get(FORMAT_YOUTUBE_URI2).text
            data2 = json.loads(content2)
            keys = 'id', 'title', 'description', 'preview'
            next_token = data2.get('nextPageToken')
            for item in data2.get('items'):
                try:
                    print(item)
                    id = item.get('id').get('videoId')
                    title = item.get('snippet').get('title')
                    description = item.get('snippet').get('description')

                    values = id, title, description, preview

                    if id:
                        video_item = dict(zip(keys, values))
                        video_list.append(video_item)
                except:
                    pass
        except:
            pass
    return video_list


if __name__ == '__main__':

    # list_video=game_video_list('UCjvuO1gMPI-7PB_eSXdtfmA')
    list_video=game_video_list('UCJhvmNFBlkSl3ShxLqydhrQ')

    with io.open('data.json', 'w', encoding='utf8') as json_file:
        data = json.dumps(list_video, ensure_ascii=False)
        # unicode(data) auto-decodes data to unicode if str
        json_file.write(data)
    print(len(list_video))


    # my_list= YouTubeTranscriptApi.get_transcript('7NN2wEvTwUs')
    # print(len(my_list))
    # print(my_list)
    # my_text=''
    # symbol='['
    # for item in my_list:
    #
    #     if item.get('text')[0]!=symbol:
    #         my_text=my_text+' '+item.get('text')
    #
    # print (my_text)



