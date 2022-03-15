from django.shortcuts import render
import pandas as pd

from pandasapp.df.melon.melon_df import getDf_Melon

# Create your views here.
def melon(request) :
    
    df = pd.DataFrame()
    df["mem_id"]    = ["a001", "b001", "c001"]
    df["mem_pass"]  = ["a001pwd", "b001pwd", "c001pwd"]
    df["mem_name"]  = ["홍길동", "춘향이", "길동이"]
    
    # DataFrame 데이터의 행과 열을 
    # HTML의 Table 형태로 변환하기
    context = {"df" : df.to_html()}
    
    return render(
        request, 'pandasapp/melon.html', context
    )


# 함수(def)로 작성하여 결과값을 받아오는 방식으로 프로그래밍
def melon_df(request):
    df = getDf_Melon()
    
    # DataFrame 데이터의 행과 열을 HTML의 Table 형태로 변환
    context = {"df" : df.to_html()}
    
    return render(
        request, 'pandasapp/melon_df.html', context
    )
    