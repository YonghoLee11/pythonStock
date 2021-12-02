from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# import Config

# options = webdriver.ChromeOptions()
# # options.add_argument('--headless')
# # options.add_argument('--no-sandbox')
# # options.add_argument('--disable-dev-shm-usage')
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")
# options.add_argument("verify=False")
# driver = webdriver.Chrome(executable_path=Config.CONFIG['CHROMEPATH'],options=options)


driver = webdriver.Chrome('/Users/gg0/Downloads/chromedriver')
driver.maximize_window()  

# driver.header_overrides = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
#     'verify': False
# }

print(1)



print(2)
# 페이지 가져오기(이동)
driver.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101')
sleep(2)
element =   driver.find_elements_by_id('section_body')
for ele in element:
    print(ele.text)
print(3)

sleep(5)

# login_form = driver.find_element_by_id('section_body')

# print(login_form)



# url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101"
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
# res = requests.get(url , verify = False , headers = headers)
# soup = BeautifulSoup(res.text, "html.parser")

# content = soup.find_all("ul")
