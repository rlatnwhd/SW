'''
2023.06.13
김수종
#문제정의
    3개의 매개변수를 전달 받아서 가장 큰 값을 리턴하는
    findmax(a,b,c)함수 구현
#알고리즘
    1. findmax(a,b,c)함수 선언
        a, b, c중  가장 큰 값 찾기
    2. num1, num2, num3 정수 입력 받기
    3. findmax(num1, num2, num3) 호출
    4. 리턴받은 가장 큰 값 출력 
'''

def findmax(a,b,c):
    if a>b :
        biggest=a
    else:
        biggest=b

    if biggest<c:
        biggest=c

    return biggest #가장 큰값 반환

num1=int(input("num1 : "))
num2=int(input("num2 : "))
num3=int(input("num3 : "))

biggest_number=findmax(num1, num2, num3) #함수 호츨
print("가장 큰 숫자 :",biggest_number)