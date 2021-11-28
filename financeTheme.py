from bs4 import BeautifulSoup
import requests

input_event = "058110"
##input_event = "멕아이씨에스"

def getMaxNavi():
    url = "https://finance.naver.com/sise/theme.naver?&page=1"
    res = requests.get(url , verify = False)
    soup = BeautifulSoup(res.text, "html.parser")
    
    navi = soup.find("table",{"class" : "Nnavi"}).find_all("td")
    max_navi = 0
    for tds in navi:
        try:
            max_navi = int(tds.text.strip())
        except:    
            print(tds.text.strip() + " not int !!")
    return max_navi        

def getThemesObj():##테마주 정보 가져오기
    themes = []
    for num in range(getMaxNavi()):
        url = "https://finance.naver.com/sise/theme.naver?&page=" + str(num+1)
        res = requests.get(url , verify = False)
        soup = BeautifulSoup(res.text, "html.parser")
        
        for idx , tds in enumerate(soup.find_all("td",{"class" : "col_type1"})):
            
            theme = {}
            theme["theme_name"] = tds.text
            theme["href"] = "https://finance.naver.com" + tds.find("a")["href"]
            theme["theme_no"] = theme["href"].split("=")[-1]
            
            td2 = soup.find_all("td",{"class" : "col_type2"})[idx]
            theme["updown_onday"] =  td2.text.strip()
            
            td3 = soup.find_all("td",{"class" : "col_type3"})[idx]
            theme["updown_threeday"] =  td3.text.strip()
            
            themes.append(theme)
    return themes 

def getEventsObj(param):##테마주 관련 종목 가져오기
    turl = param["href"]
    ##turl = "https://finance.naver.com/sise/sise_group_detail.naver?type=theme&no=242"
    tres = requests.get(turl , verify = False)
    tsoup = BeautifulSoup(tres.text, "html.parser")
    events = []
    for items in tsoup.find_all("tbody"):
        for item in items.find_all("tr"):
            event = {}
            try:
                event["theme_no"] = param["theme_no"]
                event["theme_name"] = param["theme_name"]
                event["href"] = "https://finance.naver.com" + item.find("a")["href"]
                event["event_no"] = event["href"].split("=")[-1]
                event["event_name"] = item.find("a").text.strip()
                event["transfer_reason"] = item.find("p",{"class","info_txt"}).text
                for n_idx , val in enumerate(item.find_all("td",{"class":"number"})):
                    if n_idx == 0:
                        event["current_price"] = val.text.strip()   ##현재가
                    if n_idx == 1:
                        event["pre_ratio"] = val.text.strip() ##전일비
                    if n_idx == 2:
                        event["fluctuation_rate"] = val.text.strip() ##등락률
                    if n_idx == 3:
                        event["ask_buy"] = val.text.strip() ##매수호가   
                    if n_idx == 4:
                        event["ask_sell"] = val.text.strip() ##매도호가
                    if n_idx == 5:
                        event["quant"] = val.text.strip() ##거래량
                    if n_idx == 6:
                        event["amount"] = val.text.strip() ##거래대금
                    if n_idx == 7:
                        event["prev_quant"] = val.text.strip() ##전일거래량                           
                events.append(event)
            except Exception as e:
                pass
                ##print(e)
    return events   

#종목의 현재 테마주 정보 가져오기
def getItemIncludeThemeInfo():
    item_in_thems = []
    
    try:
        input_event_no = int(input_event)                   ##정수 확인용 , 문자일 경우 exception으로..
        print(input_event_no , "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        themes = getThemesObj()   
        for theme in  themes :
            events = getEventsObj(theme)
            for event in events:
                if event["event_no"] == input_event:
                    item_in_thems.append(theme)              
    except (TypeError, AttributeError , ValueError) as ex: ##조회조건을 종목명으로 했을 경우
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        themes = getThemesObj()   
        for theme in  themes :
            events = getEventsObj(theme)
            for event in events:
                if event["event_name"] == input_event:
                    item_in_thems.append(theme)         
    except Exception as ex:
        print(type(ex).__name__)
    finally:
        return item_in_thems    
    
    # themes = getThemesObj()   
    # item_in_thems = []
    # for theme in  themes :
    #     events = getEventsObj(theme)
    #     for event in events:
    #         ##if event["event_name"] == event_name:
    #         if event["evnet_no"] == input_event:
    #             item_in_thems.append(theme)    
    # return  item_in_thems

##종목의 다른 테마주 정보 가져오기
def get_same_theme_items():
    events = []
    item_themes =  getItemIncludeThemeInfo()
    for theme in item_themes:
        events = getEventsObj(theme)
    return events

##테마 관련 종목 정보 불러오기
def getThemsEventsObj():
    themes = getThemesObj()
    events = []
    for idx, theme in enumerate(themes):
        events += getEventsObj(theme)
        # if idx >= 10:   ##상위 10개 테마
        #     break
    return events 

##테마별 시세 가져오기
# themes = getThemesObj()
# for idx , theme in enumerate(themes):
#     print(idx + 1, theme) 

##종목의 관련 테마 주 종목 정보 
events = get_same_theme_items()
for event in events:
    print(event)              

##종목의 테마 정보 
#print(getItemIncludeThemeInfo()) 

##전체 테마주 전체 종목 가져오기
# eventsObj = getThemsEventsObj()
# for idx,events in enumerate(eventsObj):
#     print(idx , events)