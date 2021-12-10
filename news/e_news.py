from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db_stock = client.stock

news_col = db_stock.news

p_url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'
e_url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101'
s_url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=102'

# 페이지 가져오기(이동)
def get_enew_html(in_url):
    driver = webdriver.Chrome('C:\chromedriver.exe')
    driver.maximize_window()
    driver.get(in_url)
    html_source_code = driver.execute_script("return document.body.innerHTML;")
    soup = BeautifulSoup(html_source_code, 'html.parser')        
    driver.close()
    return soup

def get_news_dict(soup , kind = ""):
    section_body = soup.find("div",{"id":"section_body"})
    # news_arr = []
    for li in section_body.find_all("li"):
        news_data = {}
        for idx , dts in enumerate(li.find_all("dt")):
            if idx == 0:
                continue
            else:
                news_data["title"] = dts.text
                news_data["href"] = dts.find("a")["href"]
        news_data["content"] = li.find("span",{"class" : "lede"}).text  
        news_data["compony"] = li.find("span",{"class" : "writing"}).text  
        news_data["kind"] = kind 
        
        find_news = news_col.find({"href" : news_data["href"]})
        
        if len(list(find_news)) == 0:
            news_col.insert_one(news_data)
    
p_soup = get_enew_html(p_url)   
get_news_dict(p_soup, kind = "politics")     

e_soup = get_enew_html(e_url)   
get_news_dict(e_soup, kind = "economy")    

s_soup = get_enew_html(s_url)   
get_news_dict(s_soup, kind = "social")     

for data in news_col.find():
    print(data)
print(" !!!!!!!!!!!!!!!!!!!! ")


def get_main_category_info():
    pass

def get_sub_main_category_info():
    pass

def get_submain_category_info():
    pass
