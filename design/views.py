from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'design/index.html')

def getValue(request):
    print(request.method)
    if request.method=='GET':
        print(request.GET)
        return  HttpResponse ('{"get":"get"}')
    if request.method=='POST':
        return  HttpResponse('{"POST":"POST"}')    
    return HttpResponse('scdsafce')


def WW(request):
   
    return render(request,'design/warp-weft-def.html')
