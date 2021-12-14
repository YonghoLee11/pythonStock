import item.financeRise as rise
import theme.financeTheme as f_theme
from flask import Flask, jsonify, request

app = Flask (__name__)
app.config['JSON_AS_ASCII'] = False #한글깨짐 방지

##코스피 / 코스닼 상위 20개 종목 조회
@app.route('/get_rise_items')  
def get_rise_items():
    items = rise.getItems("kosdaq")
    return {
        "items" : items
    }

##get_rise_items()


##테마 관련 정보 가져오기
@app.route('/get_themes')  
def get_themes():
    themes = f_theme.getThemesObj()     
    return {
        "themes" : themes
    }
        
##get_themes()  

##테마명으로 테마정보 조회하기(like 검색)
@app.route('/find_themes')  
def find_themes():
    themes = f_theme.find_thems()
    return {
        "themes" : themes
    }
        
##find_themes()  

##테마명으로 테마 종목 정보 조회하기(like 검색)  
@app.route('/find_themes_items')  
def find_themes_items():
    events = f_theme.find_themes_items()
    return {
        "events" : events
    }
        
##find_themes_items()     
        
##종목의 테마정보 가져오기
@app.route('/get_themes_include_item')
def get_themes_include_item():
    themes = f_theme.get_themes_include_item()
    return {
        "themes" : themes
    }    

##print(get_themes_include_item())       

##종목의 관련 테마 다른 종목 정보 가져오기
@app.route('/get_same_theme_items')
def get_same_theme_items():
    themes = f_theme.get_same_theme_items()
    return {
        "themes" : themes
    }
    # for theme in themes:
    #     print(theme)  
##print(get_same_theme_items())       


@app.route('/')
def hello_world():
    return 'Hello, World!'

 
if __name__ == "__main__":
    app.run()          





# pip --trusted-host pypi.org --trusted-host files.pythonhosted.org install <라이브러리>
