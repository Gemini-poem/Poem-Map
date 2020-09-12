from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    import requests
    import json
    return render(request,"index.html")

def poetrysearch(request):
    wenben = request.GET.get("wenben",'')
    dynasty = request.GET.get("dynasty",'')
    print(wenben)
    return render(request,"poetrysearch.html")

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

@csrf_exempt
def login(request):
        a = request.GET.get("username",'')
        b = request.GET.get("pass",'')
        print(a)
        return render(request,"login.html")