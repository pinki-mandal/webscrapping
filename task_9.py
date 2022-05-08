import os.path
import random
import time
import json
from bs4 import BeautifulSoup
from task_1 import adventure
from task_4 import details_movie


list1=[]
for i in adventure[:10]:
    url=i["movie URL"]
    # print(url)
    def movie_details_with_url(URL):
        random_sleep=random.randint(1,3)
        for i in adventure:
            if i["movie URL"]==URL:
                url1=i["movie URL"][33:]
                # print(url1)
        var=os.path.exists("/home/pinky/Desktop/webscraping"+url1+".json")
        # print(var)
        if var==True:
            with open ("url_details_movie.json","r") as f:
                a=json.load(f)
        else:
            time.sleep(random_sleep)
            data=details_movie(URL)
            # print(data)
            list1.append(data)
            with open ("task_9.json","w") as f:
                json.dump(list1,f,indent=4)
        return list1
    movie_details_with_url(url)


