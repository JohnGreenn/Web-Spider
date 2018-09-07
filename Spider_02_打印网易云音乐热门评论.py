import requests
import json


def get_hot_comments(res):
    comments_json = json.loads(res.text)
    hot_comments = comments_json['hotComments']
    with open("热门评论.txt",'w',encoding = 'utf-8') as file:
        for each in hot_comments:
            file.write(each['user']['nickname']+':\n\n')
            file.write(each['content'] + '\n')
            file.write('----------------------------\n')


def get_comments(url):
   
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4295.400 QQBrowser/9.7.12661.400',
               'referer':'http://music.163.com/'}
    params = 'FYmIjN5wlUIKv8Mn7GTcgHNgMhGqAESayLb+iAmfbYCgpCsmQfh883PwJwQB3Bc16hKvFCcWQryWbyyjC0dXDHGeUerPfKwa/0dzt5K6hC+mOzUKdgrfxWVK7wFcVpDKs4l3CbmX7pQE270VXYD7YuwAQYYxuqSFR0abXdDq2UojoK5StZHgI4JVcBx7jKUy'
    encSecKey = '4811a585b7b2c3dea7c02d31f9de1391b937c5c85bcaa624f5738c9fa287a5111a6e51e08d9d4e6144cf9de7bc9669f685a741d1bc0d295bdb45243d384417f6e0549cfe32a2daf59abaa68c4911a4de87f1b434c51cb261592577e4037783f02d0923f55f1f129549199d3d0c2533c95978f8ae57c6a4a2f863c1853d52508c'
    data = {
        'params':params,
        'encSecKey':encSecKey
        }
    name_id = url.split('=')[1]
    target_url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(name_id)
    res = requests.post(target_url,headers=headers,data=data)

    return res

def main():
    url = input("请输入链接地址:")
    res = get_comments(url)
    get_hot_comments(res)
    
   

if __name__ == "__main__":
    main()
        
