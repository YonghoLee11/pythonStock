import urllib.request
import json
from bs4 import BeautifulSoup
import requests

kospi_url = "https://finance.naver.com/sise/sise_rise.naver?sosok=0"
kosdaq_url = "https://finance.naver.com/sise/sise_rise.naver?sosok=1"

def getSoupObj(url):
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
    ##url = "https://finance.naver.com/sise/sise_rise.naver?sosok=1"
    ##res = requests.get(url , headers = headers)
    res = requests.get(url , verify = False)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup


def getItems(division):
    if division == "kospi":
       soup = getSoupObj(kospi_url) 
    else:
       soup = getSoupObj(kosdaq_url)     
    
    for idx , tb in enumerate(soup.find_all('table',{"class":"type_2"})):
        items = []
        for tr_idx , trs in enumerate(tb.find_all("tr")):
            item = {
                "num" : "",
                "event_no" : "",
                "href" : "",
                "event_name" : "", ##종목명
                "current_price" : "", ##현재가
                "pre_ratio" : "", ##전일비
                "fluctuation_rate" : "", ##등락률
                "quant" : "", ##거래량
                "ask_buy" : "", ##매수호가
                "ask_sell" : "", ##매도호가
                "buy_remaining" : "", ##매수총잔량
                "sell_remaining" : "", ##매도총잔량
                "per" : "", ##PER
                "roe" : "" , ##ROE
            }
            if trs.find('td', {'class':'blank_06'}) != None or trs.find('td', {'class':'division_line'}) != None or trs.find('td', {'class':'blank_08'}) != None:
                continue
            if tr_idx < 2:
                continue
            for td_idx,tds in enumerate(trs.find_all("td")):
                if td_idx == 0:
                    item["num"] = tds.text.strip()
                if td_idx == 1:
                    item["event_name"] = tds.text.strip()
                    item["href"] = "https://finance.naver.com" + tds.find("a")["href"]
                    item["event_no"] = item["href"].split("=")[-1]
                if td_idx == 2:
                    item["current_price"] = tds.text.strip()
                if td_idx == 3:
                    item["pre_ratio"] = tds.text.strip()
                if td_idx == 4:
                    item["fluctuation_rate"] = tds.text.strip()
                if td_idx == 5:
                    item["quant"] = tds.text.strip()
                if td_idx == 6:
                    item["ask_buy"] = tds.text.strip()     
                if td_idx == 7:
                    item["ask_sell"] = tds.text.strip() 
                if td_idx == 8:
                    item["buy_remaining"] = tds.text.strip() 
                if td_idx == 9:
                    item["sell_remaining"] = tds.text.strip() 
                if td_idx == 10:
                    item["per"] = tds.text.strip() 
                if td_idx == 11:
                    item["roe"] = tds.text.strip()   
            items.append(item)                                                    
            if len(items) >= 20:
                break
        return items 

items = getItems("kosdaq")
for item in items:
    print(item)
    
    # if idx == 1:
    #     ##print(tItem.find_all('tr'))
    #     for idx , trs in enumerate(items.find_all('tr')):
    #         if trs.find('td', {'class':'blank_06'}) != None or trs.find('td', {'class':'division_line'}) != None or trs.find('td', {'class':'blank_08'}) != None:
    #             continue
    #         for tdIdx , tds in enumerate(trs.find_all('td')):
    #             print(tds.text.strip(),tdIdx,idx)
    #         if idx >= 20:
    #             break