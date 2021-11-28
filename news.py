import urllib.request
import json
from bs4 import BeautifulSoup
import requests
   
# link = 'https://news.naver.com/main/read.naver?mode=LSD&mid=sec&sid1=102&oid=023&aid=0003654319'     
# headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}

# res = requests.get(link , headers = headers)
# soup = BeautifulSoup(res.text, "html.parser")       
# print(soup.find("h3",{"id":"articleTitle"}))   
       
def reqNewsApi():
    client_id = "mcqw21WtLaCOxmTkQ3vj"
    client_secret = "Xgt_F342K1"
    url = "https://openapi.naver.com/v1/search/news.json"
    option = "&display=20&sort=date&start=4"

    query = "?query="+urllib.parse.quote('주가')
    url_query = url + query + option
    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    
    if response.getcode() == 200:
        response_body = response.read().decode('utf-8')
        resJson = json.loads(response_body)
        response.close() 
        return resJson 
    else:
        print(" err req api !!! ")
        response.close() 
        return ""
    
def getItem(data) :
    return data['items']

def getLink(data):
    print(data)
    links = []
    for item in data:
        links.append(item["link"])
    return links    

def getHtmlText(data):
    ##print(data)
    newsDataList = []
    for link in data:
        newsDataDic = {}
        try:
            print("@@@@@@@@@@@@@@@@@@@" , link)
            headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}
            if "https://news.naver.com/main/read.naver" not in link :
                newsDataDic["link"] = link
                newsDataDic["title"] = ""
                newsDataDic["content"] = ""
                newsDataDic["err"] = ""
                newsDataDic["date"] = ""
                newsDataList.append(newsDataDic)
                continue
            res = requests.get(link , headers=headers)   
            soup = BeautifulSoup(res.text, "html.parser")
            title = soup.find("h3",{"id":"articleTitle"}).text  
            content = soup.find("div",{"id":"articleBodyContents"}).text, "content"
            newsDataDic["link"] = link
            newsDataDic["title"] = title
            newsDataDic["content"] = content
            newsDataDic["err"] = ""
            newsDataDic["date"] = ""
            newsDataList.append(newsDataDic)
            # for tag in soup.find_all('div'):
            #     print(tag.get_text())
        except Exception as e:
            print(e)
            newsDataDic["link"] = link
            newsDataDic["title"] = ""
            newsDataDic["content"] = ""
            newsDataDic["err"] = e
            newsDataDic["date"] = ""
        finally:
            print("==")        
    return newsDataList
#### getHtmlText end ###

apiRes = reqNewsApi()
if apiRes!="":
    items = getItem(apiRes)
    links = getLink(items)
    newsData = getHtmlText(links)    
    print(newsData)