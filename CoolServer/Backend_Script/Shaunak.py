import feedparser
import requests, re
import datetime
import time
class Shaunak:
    def __init__(self):
        self.rss={
"Ent":["https://timesofindia.indiatimes.com/rssfeeds/1081479906.cms","https://www.thehindu.com/entertainment/feeder/default.rss","http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml","https://rss.nytimes.com/services/xml/rss/nyt/Movies.xml"],
"India":["https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms","https://www.thehindu.com/news/national/feeder/default.rss","http://feeds.bbci.co.uk/news/world/asia/rss.xml","https://rss.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml"],
"World":["https://timesofindia.indiatimes.com/rssfeeds/296589292.cms","https://www.thehindu.com/news/international/feeder/default.rss","http://feeds.bbci.co.uk/news/world/rss.xml","https://rss.nytimes.com/services/xml/rss/nyt/World.xml"],
"Business":["https://timesofindia.indiatimes.com/rssfeeds/1898055.cms","https://www.thehindu.com/business/feeder/default.rss","http://feeds.bbci.co.uk/news/business/rss.xml","https://rss.nytimes.com/services/xml/rss/nyt/Business.xml"],
"Auto":["https://timesofindia.indiatimes.com/rssfeeds/74317216.cms","https://www.thehindu.com/life-and-style/motoring/feeder/default.rss","https://rss.nytimes.com/services/xml/rss/nyt/Automobiles.xml"],
"Life":["https://timesofindia.indiatimes.com/rssfeeds/2886704.cms","https://www.thehindu.com/life-and-style/feeder/default.rss","http://feeds.bbci.co.uk/news/health/rss.xml","https://rss.nytimes.com/services/xml/rss/nyt/Health.xml"],
"Edu":["https://timesofindia.indiatimes.com/rssfeeds/913168846.cms","http://feeds.bbci.co.uk/news/education/rss.xml"],
"Tech":["https://timesofindia.indiatimes.com/rssfeeds/66949542.cms","http://feeds.bbci.co.uk/news/technology/rss.xml","https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"],
"Sport":["https://timesofindia.indiatimes.com/rssfeeds/4719148.cms","https://www.thehindu.com/sport/feeder/default.rss","https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml"]
             }
        self.x=datetime.datetime.now()
        self.day = self.x.strftime("%a, %d %b")

    def get_data(self,key):
        articles=[]
        l=self.rss[key]
        for y in l:
            feed = feedparser.parse(y)
           # print(feed['entries'])
            for x in feed['entries']:
                #print(1)
                curr={}
                d=str(x['published'])
                #print(d)
                #print(d.find(self.day))
                #print(self.day)
                if d.find(self.day) != -1:
                    #print(x)
                    curr['title']=x['title']
                    curr['link']=x['link']
                    curr['desc']=x['description']
                    curr['date']=x['published']
                    articles.append(curr)
                    #print(curr)
                    #break
        return articles

    def get_keys(self):
        return list(self.rss.keys())

if __name__ == "__main__":
    key = input("Enter which topic you want to see? ")
    n = Shaunak()
    res=[]

    res=n.get_data(key)
    print(res)
