'''
2023.05.10
김수종
#문제정의
    
#문제분석
    변수-숫자(num)
#알고리즘
    1. 변수선언(변수 초기화)
        num을 정수로 입력
    2. 프로그램 논리(중첩 2중 for문)
        (반복) for i in range(1, num+1):
                   for j in range(1, i+1):
                       별찍기
               한줄 띄우기
'''

num1=int(input("숫자 입력 : "))

for i in range(1, num1+1):
    for j in range(1, i+1):
        print("*",end="")
    print()

#거꾸로 출력

num2=int(input("숫자 입력 : "))

for i in range(1, num2+1):
    for j in range(i, num2+1):
        print("*",end="")
    print()