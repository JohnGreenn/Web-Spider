
import requests
#从bs4中导入BeautifulSoup模块
from bs4 import BeautifulSoup
#获取电影的名称（中文，外文，其他）
def get_movies_name():
    #定制请求的头部
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
        "Host":"movie.douban.com"
    }
    movie_chinese_list=[]
    movie_english_list=[]
    movie_other_name_list=[]
    for j in range(0,10):
        i = (25 * j)
        r = requests.get("https://movie.douban.com/top250?start="+str(i)+"&filter=",headers=headers)
        soup=BeautifulSoup(r.text,"html.parser")
        # 两个参数：（标签，标识符）
        div_list=soup.find_all("div",class_="hd")
        for each in div_list:
            #each.a.span只会定位到a标签下的第一个标签的内容
            #each.a.contents会定位到a标签下的每一个标签的内容
            #print(len(each.a.contents))
            #movie_chinese=each.a.span.text.strip()
            #第一个为0.
            movie_chinese=each.a.contents[1].text.strip()
            #strip()除去字符串开头和结尾指定的字符，默认为空格或换行
            movie_english=each.a.contents[3].text.strip()
            movie_english=movie_english[2:]
            #其他名称为第6个内容，但可能存在没有其他名称的电影。
            if len(each.a.contents)>5:
                movie_other=each.a.contents[5].text.strip()
            movie_other=movie_other[2:]
            movie_chinese_list.append(movie_chinese)
            movie_english_list.append(movie_english)
            movie_other_name_list.append(movie_other)
    return movie_chinese_list,movie_english_list,movie_other_name_list
#获取电影的导演和主演
def get_other_contents():
    i=0
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
        "Host":"movie.douban.com"
    }
    directors_list=[]#导演
    starring_list=[]#主演
    release_date_list=[]#上映年份
    movie_country_list=[]#电影国别
    film_classification_list=[]#电影分类
    for j in range(0, 10):
        i = (25 * j)
        r = requests.get("https://movie.douban.com/top250?start=" + str(i) + "&filter=", headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        div_list=soup.find_all("div",class_="bd")
        for each in div_list:
            if len(each.p.contents)>1:
                """国家，年份，类别"""
                #对得到的字符串进行处理
                movie_information=each.p.contents[2].strip()
                #对字符串通过”/“切片
                movie_information=movie_information.split("/")
                #去掉多余的字符。
                release_date_list.append(movie_information[0].strip("\xa0"))
                movie_country_list.append(movie_information[1].strip(" "))
                film_classification_list.append(movie_information[2].strip(" "))
                """导演，主演"""
                # 显示p标签下第一部分的全部内容
                #print(each.p.contents[0].strip())
                #用"   "对字符串进行分割
                each_movie = each.p.contents[0].strip().split("   ")
                director=each_movie[0]
                #存在有导演，无主演的电影（动画片）
                if len(each_movie)>1:
                    starring=each_movie[1]
                #去掉多余字符（导演：）
                directors_list.append(director.strip("导演:"))
                # 去掉多余字符（导演：. 和 /）
                starring_list.append(starring.strip("主演:").strip(".").strip("/"))
    return directors_list,starring_list,release_date_list,movie_country_list,film_classification_list
#获取电影评分和经典影评
def get_movie_score():
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
        "Host":"movie.douban.com"
    }
    movie_score_list = []#评分
    movie_review_list = []#经典影评
    for j in range(0, 10):
        i = (25 * j)
        r = requests.get("https://movie.douban.com/top250?start=" + str(i) + "&filter=", headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        div_list_1=soup.find_all("div",class_="star")
        div_list_2 = soup.find_all("p", class_="quote")
        for each_1 in div_list_1:
            #通过contents把代码转化成列表.
            #通过text提取关键字
            movie_score=each_1.contents[3].text
            movie_score_list.append(movie_score)
        for each_2 in div_list_2:
            #通过contents把代码转化成列表.
            #通过text提取关键字
            #列表中只有一个元素
            movie_review=each_2.text
            movie_review_list.append(movie_review.strip())
    return movie_review_list,movie_score_list
(movie_chinese_list,movie_english_list,movie_other_name_list)=get_movies_name()
print("豆瓣电影Top250中文电影名：(共%d个电影)"%len(movie_chinese_list))
print(movie_chinese_list)
print("豆瓣电影Top250外文电影名：(共%d个电影)"%len(movie_english_list))
print(movie_english_list)
print("豆瓣电影Top250其他电影名：(共%d个电影)"%len(movie_other_name_list))
print(movie_other_name_list)
 
(directors_list,starring_list,release_date_list,movie_country_list,film_classification_list)=get_other_contents()
print("导演:")
print(directors_list)
print("主演：")
print(starring_list)
print("年份：")
print(release_date_list)
print("国家：")
print(movie_country_list)
print("类别：")
print(film_classification_list)
 
(movie_review_list,movie_score_list)=get_movie_score()
print("评分：")
print(movie_score_list)
print("经典影评：")
print(movie_review_list)
