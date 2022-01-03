import urllib.request
import json
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

news_querys = []

def req_news_api(news_query):
    ##mongo connect
    client = MongoClient('localhost', 27017)

    db_news = client.news

    news_col = db_news.news_col
    
    client_id = "mcqw21WtLaCOxmTkQ3vj"
    client_secret = "Xgt_F342K1"      
    # keyword = "형지" 
    url = "https://openapi.naver.com/v1/search/news.json"
    params = {"query" : news_query , "display" : 10 , "sort" : "date" , "start" : 1}
    ##params = {"display" : 100 , "sort" : "date" , "start" : 1}
    headers = {"X-Naver-Client-Id" : client_id,"X-Naver-Client-Secret" : client_secret}
    res = requests.get(url , params = params , headers=headers , verify = False)
    
    print(res.text , "@@@@@@@@@@@@@@" , type(res.text))
    
    res_objs = list(eval(res.text))
    
    for res_obj in res_objs:
        print(res_obj.title , "!!!!!!!!!!!!!!!!!"  )
        news_data = {}

        news_data["title"] = res_obj.title
        news_data["originallink"] = res_obj.originallink
        news_data["link"] = res_obj.link  
        news_data["description"] = res_obj.description  
        news_data["pubDate"] = res_obj.pubDate 
        
        find_news = news_col.find({"link" : news_data["link"]})
        
        if len(list(find_news)) == 0:
            news_col.insert_one(news_data)
    client.close()    
    
def get_news():   
 
    for query in news_querys:
        req_news_api(query)     
  

       
# def reqNewsApi():
#     client_id = "mcqw21WtLaCOxmTkQ3vj"
#     client_secret = "Xgt_F342K1"
#     url = "https://openapi.naver.com/v1/search/news.json"
#     option = "&display=50&sort=date&start=4"
#     query = "?query="+urllib.parse.quote('주가')
#     url_query = url + query + option
#     request = urllib.request.Request(url_query)
#     request.add_header("X-Naver-Client-Id",client_id)
#     request.add_header("X-Naver-Client-Secret",client_secret)
#     response = urllib.request.urlopen(request)
    
#     if response.getcode() == 200:
#         response_body = response.read().decode('utf-8')
#         resJson = json.loads(response_body)
#         response.close() 
#         return resJson 
#     else:
#         print(" err req api !!! ")
#         response.close() 
#         return ""
    
# print(reqNewsApi())    
    
# def getItem(data) :
#     return data['items']

# def getLink(data):
#     links = []
#     for item in data:
#         links.append(item["link"])
#     return links    

# def getHtmlText(data):
#     ##print(data)
#     for link in data:
#         try:
#             print("@@@@@@@@@@@@@@@@@@@" , link)
#             if "https://news.naver.com/main/read.naver" not in link :
#                 continue
#             res = requests.get(link , verify=False)   
#             soup = BeautifulSoup(res.text, "html.parser")
#             ##print(soup.find("h3",{"id":"articleTitle"}))   
#             for tag in soup.find_all('div'):
#                 print(tag.get_text())

#         except Exception as e:
#             print(e)

# apiRes = reqNewsApi()
# if apiRes!="":
#     items = getItem(apiRes)
#     links = getLink(items)
#     getHtmlText(links)    
