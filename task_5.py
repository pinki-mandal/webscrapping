from bs4 import BeautifulSoup
import requests
import json
from task_1 import adventure
from task_4 import details_movie

movie_details = []
for i in adventure[:100]:
# for i in range(100):
    url=i["movie URL"]
    # print(url)
    

    def get_movie_list_details(movies):

        page=requests.get(movies)
        # print(page)
        soup=BeautifulSoup(page.text,"html.parser")
        # print(soup)
        title_div=soup.find("div",class_="col mob col-center-right col-full-xs mop-main-column")
        # print(title_div)
        class_div=title_div.find("div",class_="thumbnail-scoreboard-wrap")
        # print(class_div)
        # poster_link=class_div.find("img",class_="posterImage js-lazyLoad")
        # poster_link_2=poster_link["data-src"]
        # print(poster_link_2)
        name=class_div.find("h1",class_="scoreboard__title").get_text()
        print(name)
        s=soup.find("ul",class_="content-meta info")
        # print(s)
        sub_title=s.find_all("li",class_="meta-row clearfix")
        # print(sub_title)
        movie_d={}
        movie_d["Name"]=name
        for i in sub_title:
            key=i.find("div",class_="meta-label subtle").get_text()[:-1]
            # print(key)
            value=i.find("div",class_="meta-value").get_text().strip().replace("\n","").replace(" ","").replace("\u00a0"," ")
            # print(value)
            movie_d[key]=value
            # movie_d["PosterLink"]=poster_link_2
        # time=int(movie_d["Runtime"][0])*60
        # for i in movie_d["Runtime"][2:]:
        #     if "m" not in i:
        #         time+=int(i)
        #     else:
        #         break
        # movie_d["Runtime"]=str(time)+'m'
        movie_details.append(movie_d)
        # movie_d["PosterLink"]=poster_link_2
        # movie_d[  "Original Language"]=movie_d["Original Language"].strip().split()
        # movie_d["Genre"]=genre
        # print(movie_d)
        with open("task5.json","w")as read_content:
            json.dump(movie_details,read_content,indent=4)
        return movie_details
    movie_list=get_movie_list_details(url)




