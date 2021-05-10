from bs4 import BeautifulSoup
import requests
import datetime
from dateutil.tz import gettz
import time
class Sumit:
        def __init__(self):
                self.rss = {
                "Sport": ['https://feeds.feedburner.com/ndtvsports-latest','https://indianexpress.com/section/sports/feed', 'https://economictimes.indiatimes.com/news/sports/rssfeeds/26407562.cms'],
                "India": ['https://feeds.feedburner.com/ndtvnews-india-news', 'https://www.livemint.com/rss/politics','https://indianexpress.com/section/india/feed' ,'https://economictimes.indiatimes.com/news/india/rssfeeds/81582957.cms'],
                "World": ['https://feeds.feedburner.com/ndtvnews-world-news','https://indianexpress.com/section/world/feed'],
                "Business": ['https://feeds.feedburner.com/ndtvprofit-latest', 'https://www.livemint.com/rss/markets', 'https://economictimes.indiatimes.com/news/economy/rssfeeds/1373380680.cms'],
                "Tech": ['https://feeds.feedburner.com/gadgets360-latest', 'https://indianexpress.com/section/technology/feed' ,'https://www.livemint.com/rss/technology', 'https://economictimes.indiatimes.com/tech/rssfeeds/13357270.cms'],
                "Ent": ['https://feeds.feedburner.com/ndtvmovies-latest', 'https://indianexpress.com/section/india/education/feed','https://indianexpress.com/section/entertainment/feed','https://economictimes.indiatimes.com/industry/media/entertainment/rssfeeds/13357212.cms'],
                "Trending": ['https://feeds.feedburner.com/ndtvnews-trending-news', 'https://www.livemint.com/rss/news']
                }
                self.x=datetime.datetime.now(tz=gettz('Asia/Kolkata'))
                self.day = self.x.strftime("%a, %d %b")

        def get_data(self, key):
                urls = self.rss[key]
                news = []
                for url in urls:
                        #print(url)
                        rss =requests.get(url).text 
                        soup = BeautifulSoup(rss,'xml')
                        #print(soup)
                        items = soup.find_all('item')
                        for item in items:
                                curr = {}
                                d=str(item.find('pubDate').text)
                                if d.find(self.day) != -1:
                                       # print('Yes')
                                        curr['title'] = item.find('title').text
                                        curr['desc'] = item.find('description').text
                                        curr['link'] = item.find('link').text
                                        curr['date'] = item.find('pubDate').text
                                        news.append(curr)
                return news
        def get_keys(self):
                return list(self.rss.keys())

if __name__ == "__main__":
    key = input("Enter which topic you want to see? ")
    n = Sumit()
    res=[]

    res=n.get_data(key)
    print(res)
