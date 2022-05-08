import requests
import json
import pprint
from bs4 import BeautifulSoup

def scrap_top_list():
   
    url=("https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/")
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'html.parser')
    main_div=soup.find('div',class_="panel-body content_body allow-overflow")
    tbody=main_div.find('table',class_='table')

    trs=tbody.find_all('tr')
    # return trs

    top_movie_list=[]
   
    for tr in trs[1:]:
       
        position1=tr.find('td',class_='bold').get_text().strip()
        position=position1[:-1]
       
        name=tr.find('a',class_='unstyled articleLink').get_text().split()
        print(name)
        n=''
        for i in range(len(name)-1):
            n+=name[i]

        print(n)
       
        year=name[-1][1:5]
        print(year)
       
        rating=tr.find('span',class_="tMeterIcon tiny").get_text().strip()
       
        print(rating)
       
        link=tr.find('a',class_="unstyled articleLink")
        url=link['href']
        link_1="https://www.rottentomatoes.com"+url
       
        print(link)
       
        all_detailes={}
       
        all_detailes['position']=position
        all_detailes['name']=n
        all_detailes['year']=year
        all_detailes['rating']=rating
        all_detailes['url']=link_1
       
        top_movie_list.append(all_detailes)
       
    with open("movie_list1_task_1.json","w") as f:
        json.dump(top_movie_list,f,indent=6)
    return top_movie_list
top_movie_list=scrap_top_list()

