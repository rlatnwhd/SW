'''
2023.06.07
김수종
#문제정의
    랜덤으로 2개의 set를 만든 후 합집합, 교집합, 차집합 구하기
#문제분석
    변수 - num1, num2
#알고리즘
    1. 랜덤 모듈 추가
    2. 비어있는 세트 변수 생성
    3. 반복(무한반복)
        while True :
            if len(num1)<10 :
                num1애 랜덤 수 추가
            if len(num2)<10 :
                num2에 랜덤 수 추가
    4.합집합, 교집합, 차집합
'''

import random as r

num1=set()
num2=set()

while True :
    if len(num1)<10 :
        num1.add(r.randint(1,100))
    if len(num2)<10 :
        num2.add(r.randint(1,100))
    if len(num1)==10 and len(num2)==10:
        break

print("발생된 10개 난수 num1 : ",num1)
print("발생된 10개 난수 num2 : ",num2)
print("num1, num2의 합세트 : ",num1.union(num2))
print("num1, num2의 교세트 : ",num1.intersection(num2))
print("num1, num2의 차세트 : ",num1.difference(num2))