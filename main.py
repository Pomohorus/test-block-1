from VK import VKPhoto

from Yandex_disk import YandexDisk

def upload_from_vk_to_yandex():
    ya = YandexDisk(yandex_token)
    vk = VKPhoto.profile_photo()
    ya.new_folder()
    index = 1
    length = len(vk)
    for names in vk:
        print(f'Progress: {"%.2f" % ((index / length) * 100)}%')
        index += 1
        ya.upload_vk(file_path=f'/vk/{str(names)}.jpg', file_url=vk[names])


if __name__ == '__main__':
    yandex_token = 'AQAAAAAw4-d2AADLW0RQNgXclU31rAbOF5SZUl8'
    upload_from_vk_to_yandex()
