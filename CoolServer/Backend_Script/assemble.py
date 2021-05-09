from fetcher import main
from threading import Thread
keys=["Life", "Auto", "Tech", "India", "Business", "Edu", "Ent", "Sport", "World", "Trending"]
threads = []
for key in keys:
    process = Thread(target= main,args=(key, ))
    process.start()
    threads.append(process)
for process in threads:
    process.join()
