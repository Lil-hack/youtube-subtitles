
import json


from youtube_subtitle_api import YouTubeTranscriptApi

import csv
import requests
import json
import sys
import io
import codecs



def game_playlist(channel_id):
    """ Get channel's upload videos| 50 limit"""


    YOUTUBE_URI = 'https://www.googleapis.com/youtube/v3/search?key={}&channelId={}&part=snippet,id&order=date&maxResults=50&regionCode=RU&type=playlist'
    FORMAT_YOUTUBE_URI = YOUTUBE_URI.format('AIzaSyAp14x-VYq9MRRQP0FtqYKE5grKTZ7p2pg', channel_id)

    content = requests.get(FORMAT_YOUTUBE_URI).text
    data = json.loads(content)
    print (data)
    video_list =[]
    keys = 'id', 'title'
    print(data.get('nextPageToken'))

    pages=data.get('pageInfo').get('totalResults')//50
    next_token=data.get('nextPageToken')
    for item in data.get('items'):
            try:

                id = item.get('id').get('playlistId')

                title=''
                values = id, title

                if id:
                    video_item =dict(zip(keys, values))
                    video_list.append(video_item)
            except:
                pass

    for i in range(0,5):
        try:
            YOUTUBE_URI2 = 'https://www.googleapis.com/youtube/v3/search?key={}&channelId={}&part=snippet,id&order=date&maxResults=50&regionCode=RU&type=playlist&pageToken={}'
            FORMAT_YOUTUBE_URI2 = YOUTUBE_URI2.format('AIzaSyCNFYpWH4TGP2_YEyJPy-yx2f3H6mk6c6A', channel_id, next_token)
            print(FORMAT_YOUTUBE_URI2)
            content2 = requests.get(FORMAT_YOUTUBE_URI2).text
            data2 = json.loads(content2)
            print(data2)
            keys = 'id', 'title'
            title = ''
            next_token = data2.get('nextPageToken')
            for item in data2.get('items'):
                try:
                    # print(item)
                    id = item.get('id').get('playlistId')
                    title = ''
                    values = id, title

                    if id:
                        video_item = dict(zip(keys, values))
                        video_list.append(video_item)
                except BaseException as e:

                    next_token = data2.get('nextPageToken')
        except  BaseException as e:

            next_token = data2.get('nextPageToken')
    return video_list


if __name__ == '__main__':

    list_video=game_playlist('UCZCWol-6RuRBa3QVzR_4tnQ')


    with io.open('playlist6.json', 'w', encoding='utf8') as json_file:
        data = json.dumps(list_video, ensure_ascii=False)
        json_file.write(data)
    print(len(list_video))


