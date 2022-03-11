from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def main(request):
    return HttpResponse("<u>Main</u>")

from .models import Course

# secondapp_course에 데이터 입력하기
def insert(request):
    Course(name='데이터 분석',  cnt=30).save()
    Course(name='데이터 수집',  cnt=20).save()
    Course(name='웹개발',       cnt=25).save()
    Course(name='인공지능',     cnt=20).save()
    
    return HttpResponse('secondapp_course 데이터 입력 완료')

# secondapp_curriculum에 데이터 조회하기
def show(request):
    course = Course.objects.all()
    result = ''
    for c in course:
        result += c.name + '<br>'
    return HttpResponse(result)