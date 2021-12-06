from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


s_url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=102'
e_url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101'
p_url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'

# 페이지 가져오기(이동)
def get_enew_html(in_url):
    driver = webdriver.Chrome('C:\chromedriver.exe')
    driver.maximize_window()  
    driver.get(in_url)
    html_source_code = driver.execute_script("return document.body.innerHTML;")
    soup = BeautifulSoup(html_source_code, 'html.parser')
    driver.close()
    return soup


def get_news_dict(soup):
    section_body = soup.find("div",{"id":"section_body"})
    news_arr = []
    for li in section_body.find_all("li"):
        news = {}
        for idx , dts in enumerate(li.find_all("dt")):
            if idx == 0:
                continue
            else:
                news["title"] = dts.text
                news["href"] = dts.find("a")["href"]
        news["content"] = li.find("span",{"class" : "lede"}).text  
        news["compony"] = li.find("span",{"class" : "writing"}).text    
        if news != None:   
            news_arr.append(news)      
    return news_arr           

e_soup = get_enew_html(e_url)
print(get_news_dict(e_soup))
print("!!!!!!!!!!!!!!!!!!!!!!!!1")
s_soup = get_enew_html(s_url)
print(get_news_dict(s_soup))
print("!!!!!!!!!!!!!!!!!!!!!!!!1")
p_soup = get_enew_html(p_url)
print(get_news_dict(p_soup))
