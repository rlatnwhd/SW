'''
2023.05.09
김수종
#문제정의
    입력받은 숫자의 팩토리얼 구하기
#문제분석
    변수-정수(num), 팩토리얼(fac)
#알고리즘
    1.변수지정
        num 정수로 입력받기
        fac=1
    2.논리(반복 for)
        for i in rang(num,0,-1):
            fac*=i
    3.결과 출력
'''

num=int(input("팩토리얼 숫자 입력 : "))
fac=1
for i in range(num,0,-1):
    fac*=i

print("%d의 팩토리얼 값은 : "%num,fac)