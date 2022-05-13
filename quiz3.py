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


print("არტისტის სახელი:",req_dic['name'])
print("ალბომების რაოდენობა:",req_dic['nb_album'])
print("ფანები:",req_dic['nb_fan'])


import sqlite3
connect = sqlite3.connect('music.sqlite')
cursor = connect.cursor()

cursor.execute('''create table if not exists mus
(id int,name varchar(700), fans int);''')

cursor.execute('insert into mus(id,name,fans) values(?,?,?)', (joni,req_dic['name'],req_dic['nb_fan']) )

connect.commit()
connect.close()
