'''
2023.04.19
김수종
두 개의 숫자를 입력받아서 두 번째 수가 첫 번쨰 수의 약수인지 구분하기.
#문제분석
    변수-정수1(num1), 정수2(num2)
    수식-num1%num2==0 (num2는 num1의 약수)
#알고리즘
    1. 변수 언선
        num1, num2 정수로 입력받기
    2. 논리(선택-if~else)
        if num1%num2==0:
            num2는 num1의 약수
        if num1%num2!=0:
            num2는 num1의 약수가 아니다
''' 

num1=int(input("첫번째 정수를 입력하세요. : "))
num2=int(input("두번째 정수를 입력하세요. : "))

if num1%num2==0 :
    print("{}는(은) {}의 약수입니다.".format(num2,num1))
else :
    print("{}는(은) {}의 약수가 아닙니다.".format(num2,num1))