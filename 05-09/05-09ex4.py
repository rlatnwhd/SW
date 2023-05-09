'''
2023.05.09
김수종
#문제정의
    1~100까지의 입력받은 숫자의 배수의 합계
#문제분석
    변수:정수(num),합계(sum),반복변수(i)
#알고리즘
    1.변수지정
        num변수에 정수 입력
        sum=0
        i=0
    2.논리(반복 while)
        while i<=100:
        i+=1
        if i%num!=0 :
            continue
    3.결과 출력
'''

num=int(input("배수 숫자 입력 : "))
sum=0
i=0

while i<=100: #선택 조건
    i+=1
    if i%num!=0:
        continue
    sum+=i

print("1부터 100까지 {}의 배수의 합은 : {}".format(num,sum))
