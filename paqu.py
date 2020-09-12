import urllib.parse
import re
import os
import requests

header={
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
     "referer":"https://image.baidu.com"
    }
url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word={word}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl&pn={pageNum}&rn=30&gsm=1e00000000001e&1490169411926="
keyword = input("请输入要搜索的内容：")#要搜索的关键字
#如果文件夹不存在就创建一个
if os.path.isdir("{}".format(keyword)) != True:
    os.makedirs("{}".format(keyword))
keyword2 = urllib.parse.quote(keyword,'utf-8')#将关键字转换为utf-8的格式
Num = 0
img_url = []#图片的url
#总共爬取1页
while Num < 1:
    URL = url.format(word=keyword2,pageNum=Num)
    response = requests.get(URL,headers=header)
    text = response.text
    urls = re.findall('[a-zA-z]+://[^\s]*',text)#用正则表达式匹配所有的网址
    for i in range(len(urls)//10):
        if i%2 == 0:
            img_url.append(urls[i].split('"')[0])
            img_url.append(urls[i].split('"')[-2])
        else:
            img_url.append(urls[i].split('"')[0])
    Num += 1
num = 0
print(img_url[1])
for url in img_url:
    response = requests.get(url,headers=header)
    with open("{}/{}.jpg".format(keyword,num),'wb') as f:
        f.write(response.content)
    num += 1
    