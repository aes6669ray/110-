import cv2
from numpy.core.fromnumeric import shape
import pandas as pd
import heapq

# df=pd.read_csv("https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&FOTT=CSV",sep=",",encoding="utf-8")
# df.dropna(subset=["album_file"],inplace=True)

# filter1=df["animal_status"] == "OPEN"
# filter2=df["animal_kind"] == "狗"
# df=df[filter1]
# df=df[filter2]

# print(df)

def location(city,kind):
    df=pd.read_csv("https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&FOTT=CSV",sep=",",encoding="utf-8")
    df.dropna(subset=["album_file"],inplace=True)
    filter1=df["animal_status"] == "OPEN"
    filter2=df["animal_kind"] == str(kind)
    df=df[filter1]
    df=df[filter2]
    
    position=[]
    for i,n in enumerate(df["shelter_address"]):
        if str(city) == n[:3]:
            position.append(i)
    
    df=df.iloc[position]

    return df
##選擇縣市與動物種類
df=location("桃園市","狗")

all_img_metrics=[]
for i,n in enumerate(df["album_file"].iloc[:50]):
    if ".jpg" in n:
        cap = cv2.VideoCapture(n)
        ret,img = cap.read()
        H1 = cv2.calcHist([img], [1], None, [256], [0, 256]) 
        H1 = cv2.normalize(H1, H1, 0, 1, cv2.NORM_MINMAX, -1)
        all_img_metrics.append(H1)
    elif ".jpeg" in n:
        cap = cv2.VideoCapture(n)
        ret,img = cap.read()
        H1 = cv2.calcHist([img], [1], None, [256], [0, 256]) 
        H1 = cv2.normalize(H1, H1, 0, 1, cv2.NORM_MINMAX, -1)
        all_img_metrics.append(H1)
    elif ".JPG" in n:
        cap = cv2.VideoCapture(n)
        ret,img = cap.read()
        H1 = cv2.calcHist([img], [1], None, [256], [0, 256]) 
        H1 = cv2.normalize(H1, H1, 0, 1, cv2.NORM_MINMAX, -1)
        all_img_metrics.append(H1)
    elif ".JPEG" in n:
        cap = cv2.VideoCapture(n)
        ret,img = cap.read()
        H1 = cv2.calcHist([img], [1], None, [256], [0, 256]) 
        H1 = cv2.normalize(H1, H1, 0, 1, cv2.NORM_MINMAX, -1)
        all_img_metrics.append(H1)
    else:
        print("find error:",i)
        continue

# print(shape(all_img_metrics))

def compar(path):
    input=cv2.imread(path)
    Hi = cv2.calcHist([input], [1], None, [256], [0, 256]) 
    Hi = cv2.normalize(Hi, Hi, 0, 1, cv2.NORM_MINMAX, -1)

    sim=[]
    for i in all_img_metrics:
        si=cv2.compareHist(Hi, i, 0)
        sim.append(si)

    big3=heapq.nlargest(3, sim)
    st_index=sim.index(big3[0])
    nd_index=sim.index(big3[1])
    rd_index=sim.index(big3[2])

    st=df["album_file"].iloc[st_index]
    nd=df["album_file"].iloc[nd_index]
    rd=df["album_file"].iloc[rd_index]

    cap1 = cv2.VideoCapture(st)
    cap2 = cv2.VideoCapture(nd)
    cap3 = cv2.VideoCapture(rd)

    ret,img1 = cap1.read()
    ret,img2 = cap2.read()
    ret,img3 = cap3.read()

    cv2.imshow("mostlikely",img1)
    cv2.imshow("sec",img2)
    cv2.imshow("3rd",img3)

    cv2.waitKey(0)

##改成return index就好
    print(df.iloc[st_index])
    print(df.iloc[nd_index])
    print(df.iloc[rd_index])


##拿自己照片測試
compar("test1.jpg")



