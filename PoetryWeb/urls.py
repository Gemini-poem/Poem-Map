from django.urls import path
from PoetryWeb import views
urlpatterns = [
    #设置自己的url
     path("index/",views.index,name="index"),
     path("poetrysearch/",views.poetrysearch,name="poetrysearch"),
     path("positionsearch/",views.positionsearch,name="positionsearch"),
     path("usermanual/",views.usermanual,name="usermanual"),
     path("result/",views.result,name="result"),
]

