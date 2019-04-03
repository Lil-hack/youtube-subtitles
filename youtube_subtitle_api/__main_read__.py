
import json
import os,sys
import io

if __name__ == '__main__':

    # Определяем путь к папке
    app_dir = sys.path[0] or os.path.dirname(os.path.realpath(sys.argv[0])) or os.getcwd()
    print(app_dir)

    # Cчитываем json в лист
    data = []
    # with open(app_dir+'\\DataSet_video_subtitles5.json', 'r', encoding="utf8") as f:
    #     data = json.loads(f.read())
    # with open(app_dir+'\\DataSet_video_subtitles4.json', 'r', encoding="utf8") as f2:
    #     data =data + json.loads(f2.read())
    with open(app_dir+'\\DataSet_video_subtitles_part1.json', 'r', encoding="utf8") as f3:
        data =data + json.loads(f3.read())
    # with open(app_dir+'\\DataSet_video_subtitles2.json', 'r', encoding="utf8") as f4:
    #     data =data + json.loads(f4.read())
    # with open(app_dir+'\\DataSet_video_subtitles_part3.json', 'r', encoding="utf8") as f5:
    #     data =data + json.loads(f5.read())
    # Выводим необходимые данные
    # for video in data:
    #     video_info=json.loads(str(video))
        # print('id видео = '+video_info.get('id')+' Название: '+video_info.get('title'))
        # print('id видео = ' + video_info.get('id') + ' Описание: ' + video_info.get('description'))
        # print('id видео = ' + video_info.get('id') + ' Фото: ' + video_info.get('preview'))
        # print('id видео = ' + video_info.get('id') + ' Субтитры: ' + video_info.get('text'))

    print ('Число объектов в датасете = '+str(len(data)))




    # print(str(data2))

    data3 = []
    for i in range(len(data)//2,len(data) ):
        # print (data2[i])
        data3.append(data[i])
        # new_dict = dict(zip(item.key, item.value))

    with io.open('DataSet_video_subtitles_2' + '.json', 'w', encoding='utf8') as json_file:
        data3 = json.dumps(data3, ensure_ascii=False)

        json_file.write(data3)