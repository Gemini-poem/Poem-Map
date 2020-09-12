from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    import requests
    import json
    return render(request,"index.html")

def poetrysearch(request):
    import requests
    import json
    return render(request,"poetrysearch.html")

def positionsearch(request):
    import requests
    import json
    return render(request,"positionsearch.html")

def usermanual(request):
    import requests
    import json
    return render(request,"usermanual.html")

def result(request):
    import requests
    import json
    return render(request,"result.html")