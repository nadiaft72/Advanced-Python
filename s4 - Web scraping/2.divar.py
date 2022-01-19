import requests
from bs4 import BeautifulSoup
res = requests.get('https://divar.ir/s/tehran')
soup = BeautifulSoup(res.text , 'html.parser')
res = soup.find_all("div" , attrs= {"class":"kt-post-card__body"})


for car in res:
    x = car.find("div" , attrs= {"class":"kt-post-card__title"} )
    t = car.find("div" , attrs =  {"class":"kt-post-card__description"} )
    if t!= None and t.text=="توافقی":
        print(x.text)
