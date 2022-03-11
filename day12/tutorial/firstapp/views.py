from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# View = 전체를 컨트롤 하는 함수

def index1(request) :
    return HttpResponse("<u>Hello....</u>")

def index2(request):
    return HttpResponse("<u>Hi</u>")

def main(request):
    return HttpResponse("<u>Main</u>")

def home(request):
    return HttpResponse("Home")

from .models import Curriculum

def insert(request):
    # 1-linux 입력
    Curriculum.objects.create(name='linux')
    # 2-python 입력
    c = Curriculum(name='python')
    c.save()
    # 3-html/css/js 입력
    Curriculum(name='3-html/css/js').save()
    # 4-django 입력
    Curriculum(name='django').save()
    return HttpResponse('데이터 입력 완료')

# 모델을 활용한 데이터 조회
def show(request):
    curriculum = Curriculum.objects.all()
    result = ''
    for c in curriculum:
        result += c.name + '<br>'
    return HttpResponse(result)