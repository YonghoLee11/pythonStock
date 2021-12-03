from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\chromedriver.exe')
driver.maximize_window()  

# 페이지 가져오기(이동)
driver.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101')
html_source_code = driver.execute_script("return document.body.innerHTML;")
html_soup = BeautifulSoup(html_source_code, 'html.parser')

##print(html_soup)

section_body = html_soup.find("div",{"id":"section_body"})
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
    print(news)
    if news != None:   
        news_arr.append(news)     

sleep(1)
