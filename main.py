import item.financeRise as rise
import theme.financeTheme as f_theme

##코스피 / 코스닼 상위 20개 종목 조회
def get_rise_items():
    items = rise.getItems("kosdaq")
    for item in items:
        print(item)

get_rise_items()

    
##테마 관련 정보 가져오기
def get_themes():
    themes = f_theme.getThemesObj()     
    for theme in themes:
        print(theme)  
        
##get_themes()  

##테마명으로 테마정보 조회하기(like 검색)
def find_themes():
    themes = f_theme.find_thems()
    for theme in themes:
        print(theme) 
        
##find_themes()      

##종목의 테마정보 가져오기
def get_themes_include_item():
    themes = f_theme.get_themes_include_item()
    for theme in themes:
        print(theme)

##print(get_themes_include_item())       

##종목의 관련 테마 다른 종목 정보 가져오기
def get_same_theme_items():
    themes = f_theme.get_same_theme_items()
    for theme in themes:
        print(theme)  
##print(get_same_theme_items())                 
