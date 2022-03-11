from django.db import models

# Create your models here.
# 모델은 무조건 class로 만듬
# class 이름 = Table 이름
# 클래스 이름의 첫글자는 무조건 대문자

class Curriculum(models.Model):
    name = models.CharField(max_length=255)
