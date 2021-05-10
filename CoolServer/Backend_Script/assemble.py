from fetcher import main
from threading import Thread
from datetime import datetime
from dateutil.tz import gettz
date = datetime.now(tz=gettz('Asia/Kolkata'))
dt_str = date.strftime("%d/%m/%Y %H:%M:%S")
f = open("/home/ubuntu/lastupdate.txt","a")
f.write("last updated: "+dt_str+"\n")
f.close()
keys=["Life", "Auto", "Tech", "India", "Business", "Edu", "Ent", "Sport", "World", "Trending"]
threads = []
for key in keys:
    process = Thread(target= main,args=(key, ))
    process.start()
    threads.append(process)
for process in threads:
    process.join()
