import json
import requests


class YandexDisk:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)

        }

    def new_folder(self):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {"path": 'vk'}
        response = requests.put(upload_url, headers=headers, params=params)

    def upload_vk(self, file_path, file_url):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path,
                  "url": file_url,
        }
        response = requests.post(upload_url, params=params, headers=headers)
        response.raise_for_status()
        if response.status_code == 202:
            print("Success")









if __name__ == '__main__':
    token = 'AQAAAAAw4-d2AADLW0RQNgXclU31rAbOF5SZUl8'

    newf = YandexDisk(token)
    result = newf.new_folder()