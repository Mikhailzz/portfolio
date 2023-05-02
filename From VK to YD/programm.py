import requests
from pprint import pprint
import json


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def create_folder(self, path):
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Accept': 'application/json', "Authorization": f"OAuth {self.token}"}
        requests.put(f'{URL}?path={path}', headers=headers)
        self.path = path
        return path

    def upload(self, url: str, i: int):
        headers = {'Accept': 'application/json', "Authorization": f"OAuth {self.token}"}
        params = {"path": f'{self.path}/{i + 1}.jpg', 'url': url}
        resource = requests.post("https://cloud-api.yandex.net/v1/disk/resources/upload", headers=headers,
                                 params=params)
        return resource


class VK:
    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

    def filefoto(self):
        params = {'owner_id': '39150232',
                  'album_id': 'profile',
                  'photo_sizes': 'z',
                  'extended': '1'
                  }
        url = 'https://api.vk.com/method/photos.get'
        response = requests.get(url, params={**self.params, **params})
        return response


access_token = ''

user_id = input('Введите id пользователя в ВК ')
token = input('Введите токен яндекса ')
vk = VK(access_token, user_id)

pprint(vk.users_info())
print(vk.filefoto())
resp = vk.filefoto()
with open("log.json", "w", encoding='utf-8') as write_fi:
    json.dump(vk.users_info(), write_fi, indent=2)
    json.dump(resp.json(), write_fi, indent=2)

pprint(resp.json(), width=1000)

resp_json = resp.json()

uploader = YaUploader(token)
uploader.create_folder('Pictures_of_AVATAR')

list_of_dict_picture = []
dict_one_pic = {}
like = set()
like.add(0)
height = 0
type = ''
j_element = 0

for i in range(len(resp_json['response']['items'])):
    for j in range(len(resp_json['response']['items'][i]['sizes'])):
        if resp_json['response']['items'][i]['sizes'][j]['height'] > height:
            height = resp_json['response']['items'][i]['sizes'][j]['height']
            type = resp_json['response']['items'][i]['sizes'][j]['type']
            j_element = j
    url = resp_json['response']['items'][i]['sizes'][j_element]['url']
    uploader.upload(url, i)
    if resp_json['response']['items'][i]['likes']['count'] not in like:
        dict_one_pic = {'file_name': resp_json['response']['items'][i]['likes']['count'],
                        'size': resp_json['response']['items'][i]['sizes'][j_element]['type']}
        like.add(resp_json['response']['items'][i]['likes']['count'])
        list_of_dict_picture.append(dict_one_pic)
    else:
        dict_one_pic = {'file_name': [resp_json['response']['items'][i]['likes']['count'],
                                      resp_json['response']['items'][i]['date']],
                        'size': resp_json['response']['items'][i]['sizes'][j_element]['type']}
        list_of_dict_picture.append(dict_one_pic)
    dict_one_pic = {}

pprint(list_of_dict_picture)

with open("log.json", "a") as write_fi:
    json.dump(list_of_dict_picture, write_fi, indent=2)

with open("itog.json", "w") as write_file:
    json.dump(list_of_dict_picture, write_file, indent=2)
