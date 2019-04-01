from django.http import HttpResponse
from django.shortcuts import render

def saimbhi(Request):
    return HttpResponse('hey, saimbhi this side !!')

def wordcount(Request):
    return render(Request,'home.html')

def countpage(Request):
    full_text=Request.GET['full_text']
    words=full_text.split()
    dictwords=dict()
    for word in words:
        if word in dictwords:
            dictwords[word] += 1
        else:
            dictwords[word]=1

    return render(Request,'count.html',{'full_text':full_text,'count':len(words),'words':dictwords})

def about(request):
    return render(request,'about.html')
