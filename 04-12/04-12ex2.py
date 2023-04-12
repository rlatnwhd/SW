'''
2023.04.12
김수종
입력받은 두 수의 크기 비교
#문제분석
    변수-숫자1(num1),숫자2(num2)
#알고리즘
    1.변수 선언
        num1, num2에 정수 입력
    2.논리(선택if~else)
        if num1>num2:
            (참)큰 수 num1, 작은 수 num2
        else:
            (거짓)큰 수 num2, 작은 수 num1
'''

num1=int(input("첫 번째 숫자 입력 : ")) #첫 번째 숫자 정수로 입력
num2=int(input("두 번째 숫자 입력 : ")) #두 번째 숫자 정수로 입력

if num1>num2 : #조건
    print("두 수 중에 큰 수는 {}이고 작은 수는 {}입니다.".format(num1,num2)) #조건이 참
else :
    print("두 수 중에 큰 수는 {}이고 작은 수는 {}입니다.".format(num2,num1)) #조건이 거짓