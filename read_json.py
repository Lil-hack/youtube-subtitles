
import json
import os,sys

if __name__ == '__main__':

    # Определяем путь к папке
    app_dir = sys.path[0] or os.path.dirname(os.path.realpath(sys.argv[0])) or os.getcwd()
    print(app_dir)

    # Cчитываем json в лист
    data = []
    with open(app_dir+'\\DataSet_video_subtitles_part1.json', 'r', encoding="utf8") as f:
        data = json.loads(f.read())

    # Выводим необходимые данные
    for video in data:
        video_info=json.loads(str(video))
        # print('id видео = '+video_info.get('id')+' Название: '+video_info.get('title'))
        # print('id видео = ' + video_info.get('id') + ' Описание: ' + video_info.get('description'))
        # print('id видео = ' + video_info.get('id') + ' Фото: ' + video_info.get('preview'))
        print('id видео = ' + video_info.get('id') + ' Субтитры: ' + video_info.get('text'))

    print ('Число объектов в датасете = '+str(len(data)))

