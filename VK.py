import json
import requests
from pprint import pprint


class VKPhoto:

    def profile_photo():
        user_id = '18427084'
        token = '88e2a31a5acf31c5bf5eb9ec3f486692f7eb17f9b77c5cf1a9d3dc1e2025fbac2a2024a351e5b72b0b27b'
        URL = 'http://api.vk.com/method/photos.get'
        params = {
            'owner_id': user_id,
            'access_token': token,
            'v': '5.131',
            'album_id': 'profile',
            'extended': '1',
            'photo_sizes': '1',
            'count': '200'
        }
        photos = {'height': '0', 'width': '0'}
        size_photo = {'height': '0', 'width': '0'}
        res = requests.get(URL, params=params).json()
        album = res['response']['items']
        likes_list = []
        list_of_photos = []
        biggest_photo = []
        photo_dict = {}
        list_for_json = []
        count = 7 # Колличество фотографий, загружаемых на диск
        for photo in album:
            photos['name'] = photo['likes']['count']
            for likes in likes_list:
                if photo['likes']['count'] == likes:
                    photos['name'] = photo['date']
                    break
            likes_list.append(photo['likes']['count'])
            for size in photo['sizes']:
                if (int(size['height']) + int(size['width'])) >= (int(photos['height']) + int(photos['width'])):
                    photos['height'] = size['height']
                    photos['width'] = size['width']
                    photos['url'] = size['url']
                    photos['type'] = size['type']
            list_of_photos.append([photos['name'], photos['url'], (int(photos['height']) + int(photos['width'])), photos['type']])
            photos = {'height': '0', 'width': '0'}
        for name in list_of_photos:
            biggest_photo.append(name[2])
        biggest_photo.sort()
        index_1 = 0
        while count != 0:
            for value in list_of_photos:
                if biggest_photo[-count] == value[2]:
                    photo_dict[value[0]] = value[1]
                    list_of_photos[index_1][2] = -1
                    list_for_json.append({"file_name": f"{list_of_photos[index_1][0]}.jpg", "size": list_of_photos[index_1][3]})
                    break
                index_1 += 1
            index_1 = 0
            count -= 1
        with open("vk_photo.json", "w") as f:
            json.dump(list_for_json, f, ensure_ascii=False, indent=2)
        return photo_dict