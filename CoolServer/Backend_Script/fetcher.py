from threading import Thread
from bs4 import BeautifulSoup
from newspaper import Article
from newspaper import Config
from Shaunak import Shaunak
from Sumit import Sumit
from Shaktijit import Shaktijit
import time
import sys
import json
import requests

def get_article(Q,link):
    art={}
    config = Config()
    config.request_timeout = 10
    toi_article = Article(link['link'],config=config)
    
    #To download the article
    toi_article.download()

    #To parse the article
    toi_article.parse()

    #To perform natural language processing ie..nlp
    toi_article.nlp()
    
    if link['link'].find('thehindu')!= -1:
        sdata=requests.get(link['link'])
        soup = BeautifulSoup(sdata.content,'html.parser')
        mydivs = soup.find("div", {"class": "img-container picture"})
        img=soup.find("picture")
        img=soup.find("source")
        art["Image"]=""+str(img['srcset'])
        
    else:
        art["Image"]=""+toi_article.top_image

    art["Link"]=""+link['link']    
    art["Title"]=""+link['title']
    art["Description"]=""+link['desc']
    art["Text"] =""+toi_article.text
    art["Date"] =""+link['date']
    Q.append(art)
    
    

def main(key):
    threads = []
    data1,data2,data3 = Shaunak(), Sumit(), Shaktijit()
    res=[]
    #keys=set(data1.get_keys()+data2.get_keys()+data3.get_keys())
    #print(keys)
    #key=input("Enter catergories: ")
    t0= time.clock()
    if key in list(data1.get_keys()):
        urls1=data1.get_data(key)
        for x in urls1:
            process = Thread(target= get_article,args=(res,x, ))
            process.start()
            threads.append(process)
        for process in threads:
            process.join()
    if key in list(data2.get_keys()):
        urls2=data2.get_data(key)
        for x in urls2:
            process = Thread(target= get_article,args=(res,x, ))
            process.start()
            threads.append(process)
        for process in threads:
            process.join()
    if key in list(data3.get_keys()):
        urls3=data3.get_data(key)
        for x in urls3:
            process = Thread(target= get_article,args=(res,x, ))
            process.start()
            threads.append(process)
        for process in threads:
            process.join()
    print(time.clock() - t0)
    #print(len(res))
    
    with open('/home/ubuntu/django/news-scrapper-django-server/CoolServer/Backend_Script/'+key+'.json', 'w', encoding="utf-8") as f:
        json.dump(res,f,indent=2, sort_keys=True)
    
if __name__ == "__main__":
    main('Life')
