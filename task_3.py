import requests
import json 
import pprint
from task_1 import scrape_top_list
from task_2 import  group_by_year
dec_arg = group_by_year(scrape_top_list())

def group_by_decade(movies):
    moviedec = {}
    decade_year = []                  
    for index in movies:  
        Mod = index % 10    
        decade = index - Mod  
        if decade not in decade_year:
            decade_year.append(decade)   
    decade_year.sort() 
    for decade in decade_year:
        moviedec[decade] = []
    
    for moviedec_key in moviedec: #trask 2 ka solution hai jo
        dec10 = moviedec_key + 9    # dec10 = 1959
        for values in movies:
            if values >= moviedec_key and values <= dec10:   # 2018 >= 2010      2018 <= 2019
                moviedec[moviedec_key].append(movies[values])

    with open('top_movie_3.json', 'w') as file:
        json.dump(moviedec, file, indent=4)
    return moviedec

group_by_decade(dec_arg)          
            

