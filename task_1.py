# Beautiful Soup is a Python library for pulling data out of HTML and XML files
from bs4 import BeautifulSoup
import requests
import json


data="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
advanced=requests.get(data)
# print(advanced)
# get() method is used in Python to retrieve a value from a dictionary.

    # htmlcontent=advanced.content
    # print(advanced.text)
    
    

soup=BeautifulSoup(advanced.text,"html.parser")   
# The HTML parser is a structured markup processing tool. 
# It defines a class called HTMLParser, 
# ​which is used to parse HTML files.

# html parser html data ko python data convert krta h jo readable hota h 
 
 
# ppt sequence me lata h data 
def scrape_top_list():    
    table_tag=soup.find("table",class_="table")
    tr=table_tag.find_all("tr")
    top_movie=[]
    serial_no=1
    for i in tr:
        movie_rank=i.find_all("td",class_="bold")
        for j in movie_rank:
            rank=j.get_text() 
        movie_rating=i.find_all("span",class_="tMeterScore")
        for rate in movie_rating:
            rating=rate.get_text().strip()
            # the strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters 
            rating=rate.get_text()
        movie_name=i.find_all("a",class_="unstyled articleLink")
        for name in movie_name:
            title=name.get_text().strip()
            title=name.get_text()
            list=title.split()
            year=list[-1][1:5]
            year1=int(year)
            name_lenght=len(list)-1
            name=""
            for l in range(name_lenght):
                name+=""
                name+=list[l]
            movie_name=name
        movie_reviews=i.find_all("td",class_="right hidden-xs")
        for rev in movie_reviews:
            reviews=rev.get_text()
        url=i.find_all("a",class_="unstyled articleLink")
        for i in url:
            link=i["href"]
            movie_link="https://www.rottentomatoes.com"+link
            # print(movie_link)
            details={"movie_rank":"","movie_rating":"","movie_name":"","movie_reviews":"","movie URL":"","year":""}
            details["movie_rank"]=rank
            details["movie_rating"]=rating
            details["movie_name"]=movie_name
            details["movie_reviews"]=reviews
            details["movie URL"]=movie_link
            details["year"]=year1
            top_movie.append(details.copy())
            # print(top_movie)

  
    with open('task_1.json','w') as file:
        json.dump(top_movie,file,indent=4)
        return top_movie
adventure=scrape_top_list() 