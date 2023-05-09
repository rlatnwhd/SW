'''
2023.05.09
김수종
#문제정의
    1부터 1000까지의 입력받은 숫자의 배수합 구하기
#문제분석
    변수-정수(num), 합계(total)
#알고리즘
    1.변수지정
    num을 정수로 입력 받기
    total=0
    2.프로그램 논리(반복 for)
    for i in range(num,1001,num)
        total+=i
'''

num=int(input("합을 원하는 배수 입력 : "))
total=0

for i in range(num,1001,num):
    total+=i

print("1부터 1000까지의 {}의 배수합은 : {}".format(num,total))