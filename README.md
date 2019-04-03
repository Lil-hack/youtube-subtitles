# YouTube Subtitle  (automatically generated subtitles)


This is an python API which allows you to get the transcripts/subtitles for a given YouTube video. It works for automatically generated subtitles.

## Dependencies
 - `install python 3.7`
 - `install pip`
 - `sudo pip3 install -r requirements.txt`

## How to use it

`python3 read_json.py`

### In code

To get a transcript for a given video you can do:

```python
print('id видео = ' + video_info.get('id') + ' Название: '+video_info.get('title'))
print('id видео = ' + video_info.get('id') + ' Описание: ' + video_info.get('description'))
print('id видео = ' + video_info.get('id') + ' Фото: ' + video_info.get('preview'))
print('id видео = ' + video_info.get('id') + ' Субтитры: ' + video_info.get('text'))
```

This will return a list of id_video and other info 

### DataSet

DataSet_video_subtitles_part1.json 

DataSet_video_subtitles_part2.json

DataSet_video_subtitles_part3.json

In this files there are 6200 objects with the following fields:

- id 
- title
- description
- preview
- text 
```python
[  
   {  
      "id":"bAtooccIWyw",
      "title":"Лапси - Серия 8 - мистический триллер (2019) HD",
      "description":"Лапси - Серия 8 - мистический триллер HD. #Новый #сериал #Лапси смотри #триллер #мистика премьера. В НИИ вирусоло...",
      "preview":"https://i.ytimg.com/vi/bAtooccIWyw/hqdefault.jpg"
      "text":" в эфире новости и наша постоянная рубрика воры у власти прямо сейчас мы находимся у замка который принадлежит брату губернатора винокуро..."
    },
    ...
    
]   
```
