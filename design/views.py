from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'design/index.html')

def WW(request):
    return render(request,'design/warp-weft-def.html')
