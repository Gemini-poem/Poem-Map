from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import requests
import json
import urllib.parse
import re
import os
from django.views.decorators.csrf import csrf_exempt

#ltp范例代码
import os
LTP_DATA_DIR = 'D:\ltp\ltp_data_v3.4.0'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`

from pyltp import Segmentor              #分词
from pyltp import Postagger              #词性标注   

#分词
def segmentor(sentence):
    segmentor = Segmentor()  # 初始化实例
    segmentor.load_with_lexicon(cws_model_path,r'D:\ltp\ltp_data_v3.4.0\user.dict')  # 加载模型
    words = segmentor.segment(sentence)  # 分词
    #默认可以这样输出
    print ('\t'.join(words))
    # 可以转换成List 输出
    words_list = list(words)
    segmentor.release()  # 释放模型
    return words_list

def posttagger(words):
    postagger = Postagger() # 初始化实例
    postagger.load(pos_model_path)  # 加载模型
    postags = postagger.postag(words)  # 词性标注
    Words_list= []
    for word,tag in zip(words,postags):
        if(tag=='ns'):
            Words_list.append(word) #查找出地名词汇并放入列表
    postagger.release()  # 释放模型
    return Words_list

def pic_url(keyword):
    header={
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
     "referer":"https://image.baidu.com"
    }
    url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word={word}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl&pn={pageNum}&rn=30&gsm=1e00000000001e&1490169411926="
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
    return img_url[1]
# Create your views here.
def index(request):
    import requests
    import json
    return render(request,"index.html")

def poetrysearch(request):
    wenben = request.GET.get("wenben",'')
    fenci= segmentor(wenben)
    tags = posttagger(fenci)
    P_url=[]
    for i in tags:
        p_url = pic_url(i)
        print(type(p_url))
        P_url.append(p_url)
    data=list(zip(tags,P_url))
    print(tags)
    print(P_url)
    print(data)
    if tags==[]:
        return render(request,"poetrysearch.html")
    else:
        return render(request,"result.html",{"data":data,"wenben":wenben})

def positionsearch(request):
    if request.method == "POST":
        positionname = request.POST.get('positionname')
        print(positionname)
    return render(request,"positionsearch.html")

def usermanual(request):
    import requests
    import json
    return render(request,"usermanual.html")

def result(request):
    pass
    return render(request,"result.html")

# @csrf_exempt
# def login(request):
#         a = request.GET.get("username",'')
#         b = request.GET.get("pass",'')
#         print(a)
#         return render(request,"login.html")