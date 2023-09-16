from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'design/index.html')
def dn(request):
    if request.method=='POST':
        #setAttribute2database
        print("setdn")
        return HttpResponse('{"POST":"POST"}')   
    else:
        print("getdn")
        return render(request,'design/design.html')



def WW(request):
    if request.method=='POST':
        #setAttribute2database
        print("setww")
        return HttpResponse('{"POST":"POST"}')   
    else:
        print("getWW")
        return render(request,'design/warp-weft-def.html')

def setww(request):
    print(request.method)
    if request.method=='POST':
        #setAttribute2database
        print("setww")
    return HttpResponse('{"POST":"POST"}')

def getValue(request):
    print(request.method)
    if request.method=='GET':
        print(request)
        return  HttpResponse ('{"get":"get"}')
    if request.method=='POST':
        return  HttpResponse('{"POST":"POST"}')    
    return HttpResponse('scdsafce')
