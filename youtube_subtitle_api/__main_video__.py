
import json


from youtube_subtitle_api import YouTubeTranscriptApi

import csv
import requests
import json
import sys
import io
import codecs



def game_video_from_playlist(channel_id):
    """ Get channel's upload videos| 50 limit"""


    YOUTUBE_URI = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={}&maxResults=50&key={}'
    FORMAT_YOUTUBE_URI = YOUTUBE_URI.format( channel_id,'AIzaSyCNFYpWH4TGP2_YEyJPy-yx2f3H6mk6c6A')

    content = requests.get(FORMAT_YOUTUBE_URI).text
    data = json.loads(content)
    print(data)
    video_list = []
    keys = 'id', 'title', 'description', 'preview'
    print(len(data.get('items')))
    print(data.get('items'))


    for item in data.get('items'):
        try:
            # print(item)
            id = item.get('snippet').get('resourceId').get('videoId')
            print(id)
            title = item.get('snippet').get('title')
            print(title)
            description = item.get('snippet').get('description')
            preview = item.get('snippet').get('thumbnails').get('high').get('url')

            values = id, title, description, preview

            if id:
                video_item = dict(zip(keys, values))
                video_list.append(video_item)
        except  BaseException as e:
            pass
    return video_list

if __name__ == '__main__':


    list_video=[]
    with open('playlist6.json', 'r', encoding="utf8") as f:
        data = json.loads(f.read())
    for video in data:
        # video_info=json.loads(str(video))
        print(video.get('id'))
        list_video =list_video+ game_video_from_playlist(video.get('id'))


    # list_video=game_video_list('UCJhvmNFBlkSl3ShxLqydhrQ')
    print (list_video)
    with io.open('video6.json', 'w', encoding='utf8') as json_file:
        data = json.dumps(list_video, ensure_ascii=False)
        json_file.write(data)
    print(len(list_video))
