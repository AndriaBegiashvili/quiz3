import json
import requests

url = "https://developers.deezer.com"
req = requests.get(url)

if req.status_code == 200:
    print('Connected')

print(type(req.headers))    

joni = int(input("შეიყვანეთ რიცხვი: "))
music_url = f'https://api.deezer.com/artist/{joni}'
req_mus = requests.get(music_url)
req_tx = req_mus.text
req_dic = json.loads(req_tx)
reqDic_list= json.dumps(req_dic, indent=4)

with open('music_json.json', 'w') as file:
    file.write(reqDic_list)


print(req_dic['name'])
print(req_dic['nb_album'])
print(req_dic['nb_fan'])
