#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np

# 매개변수가 두개인 경우
def outlier_iqr3(df,data):
    # percentile() : 25%와 75% 시점의 데이터 값을 알려줍니다.(return)
    q1, q3 = np.percentile(df[data], [25, 75])
    print(q1)
    print(q3)
    
    # iqr 값 계산하기
    iqr = q3 - q1
    print(iqr)
    
    # 최대값 계산하기
    upper_bound = q3 + (iqr * 1.5)
    print(upper_bound)
    
    # 최소값 계산하기
    lower_bound = q1 - (iqr * 1.5)
    print(lower_bound)
    
    # 나이 데이터에서 이상치 값 조회하기
    df_temp=df[(df[data]>upper_bound) | 
                           (df[data]<lower_bound)]
    print(len(df_temp))

