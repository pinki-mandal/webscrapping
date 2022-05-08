
from bs4 import BeautifulSoup
import requests
import json
import random
import time
from task_1 import adventure

url=adventure[10]["movie URL"]
movie_details = []
def details_movie (movie_url):
    movie_id = ''
    for id in movie_url[33:]:
        if '/' not in id:
            movie_id + id
        else:
            break
    for i in adventure:
        movie_name=adventure[0]["movie_name"]
    file_name = movie_id + '.json'
    movie_dic = {}
    page = requests.get(movie_url)
    soup = BeautifulSoup(page.text,'html.parser')
    movie_dic['movie_name'] = movie_name
    title = soup.find_all('div',class_='meta-label subtle')
    value = soup.find_all('div',class_='meta-value')
    for i in range(len(title)):
        movie_dic[str(title[i].get_text().strip())[:-1]] = value[i].get_text().replace(" ","").strip().replace("\n","")
    movie_details.append(movie_dic)
    with open('Task_8.json','w') as file:
        json.dump(movie_details,file,indent=4)
details_movie(url)



       

              