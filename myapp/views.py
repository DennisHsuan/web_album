from django.shortcuts import render
from django.http import HttpRequest


def test(request):
    return render(request,'test.html',locals())

def index (request): #首頁
    subjects = ["國文","英文","數學","自然","社會"]
    scores = [78, 83, 90, 62, 87]
    return render(request,'index.html',locals())
    