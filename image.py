import pandas as pd
import urllib.request as req
import os

def download(data):
    while True:
        try:
            if data['animal_kind'] == '狗':
                req.urlretrieve(data['album_file'], f"./dogs/{data['animal_id']}.jpg")
            elif data['animal_kind'] == '貓':
                req.urlretrieve(data['album_file'], f"./cats/{data['animal_id']}.jpg")
            else:
                req.urlretrieve(data['album_file'], f"./other/{data['animal_id']}.jpg")
            return
        except Exception as e:
            if str(e) == "HTTP Error 404: Not Found":
                print("檔案不存在")
                return
            else:
                print("連線失敗，重試中...")

data = pd.read_csv("https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&FOTT=CSV")

if not os.path.exists('dogs'):
    os.makedirs('dogs')

if not os.path.exists('cats'):
    os.makedirs('cats')

if not os.path.exists('other'):
    os.makedirs('other')

progress = 0
for i in data.iloc:
    if i['animal_status'] == "OPEN" and not pd.isna(i['album_file']):
        download(i)

    progress += 1
    if progress % 100 == 0:
        print(f"{progress // 100}%")

print("done!")