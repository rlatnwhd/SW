'''
2023.05.03
김수종
#문제정의
    1~입력받은 숫자까지의 합계 구하기
#문제분석
    변수-sum(합계), i(반복횟수), num(숫자)
#알고리즘
    1.변수선언
        sum=0, i=1 저장
        num 정수로 입력 받기
    2.논리(반복for)
        for i in range(1,num+1) : (조건)
            sum+=i
    3.합계출력
        print("1 ~ {} 까지의 합계 : {}".format(num,sum))
'''

num=int(input("합계 구할 숫자 : "))
sum=0 #합계

for i in range(1,num+1) : #조건
    sum+=i #합계

print("1 ~ {} 까지의 합계 : {}".format(num,sum))