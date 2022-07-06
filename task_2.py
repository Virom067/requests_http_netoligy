import requests
import os

class YaUploader:
    def __init__(self, token):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.headers = {'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'Authorization': f'OAuth {self.token}'}

    def upload(self, path_to_file):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = self.url + '/upload'
        response = requests.get(upload_url,
                               headers=self.headers,
                               params={'path': os.path.basename(path_to_file),
                                       'overwrite': 'replace'})
        with open(path_to_file, 'rb') as f:
            try:
                requests.put(response.json()['href'], files={'file': f})
                print('OK!')
            except KeyError:
                print(response)



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
