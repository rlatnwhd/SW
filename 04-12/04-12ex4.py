'''
2023.04.12
김수종
145p 6번 문제
#문제분석
    두 숫자가 모두 짝수이면 덧셈 값 출력
    줄 중 하나의 숫자가 홀수이면 몇 번째 숫자가 홀수인지 출력
    둘 다 홀수이면 둘 다 짝수로 입력하라고 출력
#알고리즘
    1.변수선언
        변수-num1,num2 정수 입력
        수식-num1%2==0 (num1은 짝수)/num1%2!=0 (num1은 홀수)
    2.논리(선택)
        if num1%2==0 num2%2==0:
            num1+num2
        elif num1%2!=0 num2%2==0:
            num1 짝수로 입력
        elif num1%2==0 num2%2!=0:
            num2 짝수로 입력
        else :
            둘 다 짝수로 입력
'''
num1=int(input("첫 번째 숫자 : "))
num2=int(input("두 번째 숫자 : "))

if num1%2==0 and num2%2==0 :
    print("{} + {} = {}".format(num1,num2,num1+num2))
elif num1%2!=0 and num2%2==0 :
    print("첫 번째 정수를 짝수로 입력하세요.")
elif num1%2==0 and num2%2!=0 :
    print("두 번째 정수를 짝수로 입력하세요.")
else :
    print("두 숫자 모두 짝수로 입력하세요.")