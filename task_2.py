import yadisk
import os

class YaUploader:
    def __init__(self, token: str):
        self.y = yadisk.YaDisk(token=token)

    def upload_for_disk(self, file_path: str):
        file_name = os.path.basename(file_path)
        self.y.upload(file, file_name)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    file = ...
    token = ...
    uploader = YaUploader(token)
    uploader.upload_for_disk(file)