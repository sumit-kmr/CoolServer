import feedparser
import requests, re
import datetime
import time
class Shaktijit:
    def __init__(self):
        self.rss={
"Tech":["https://www.cnet.com/rss/all/","https://www.theverge.com/rss/index.xml","http://feeds.feedburner.com/digit/latest-from-digit"]
             }
        self.x=datetime.datetime.now()
        self.day = self.x.strftime("%a, %d %b")

    def get_data(self,key):
        articles=[]
        l=self.rss[key]
        for y in l:
            #print(y)
            feed = feedparser.parse(y)
            for x in feed['entries']:
                curr={}
                d=str(x['published'])
                if d.find(self.day) !=-1:
                    curr['title']=x['title']
                    curr['link']=x['link']
                    curr['desc']=x['description']
                    curr['date']=x['published']
                    articles.append(curr)
        return articles
    def get_keys(self):
        return list(self.rss.keys())
if __name__ == "__main__":
    key = input("Enter which topic you want to see? ")
    n = news()
    res=[]

    res=n.get_data(key)
    print(res)
