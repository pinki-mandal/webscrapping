# from bs4 import BeautifulSoup
# # from pprintpp import pprint
# import requests
# import json 
# import pprint
# from task_1 import adventure


# def group_by_year(movies):
#     years=[]
#     for i in movies:
#         year=i["year"]
#         if year not in years:
#             years.append(year)
            
                      
#     movie_dict={i:[] for i in years}
#     for i in movies:
#         year=i["year"]
#         for x in movie_dict:
#             if str(x)==str(year):
#                 movie_dict[x].append([i])

#     with open('task_2.json','w') as file:
#         json.dump(movie_dict,file,indent=4)
        
#         return movie_dict
    
# group_by_year(adventure)          
            

k=int(input())
n=int(input())
l=[]
for i in range(0,n):
    p=int(input())
    l.append(p)
    
def sumofnumber(l,n,k):
    i=1
    while i<=k:
        max=l[0]
        min=l[0]
        for j in l:
            if max<j:
                max=j
            if min>j:
                min=j
        if i!=k:
            l.remove(min) 
            l.remove(max) 
        else:
            sum=max+min
            return sum  
        i+=1
result=sumofnumber(l,n,k) 
print(result)                      