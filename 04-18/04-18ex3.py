'''
2023.04.18
김수종
3장 연습문제 7번
두 정수 입력 x>y -> x//y, x<y -> x+y, x==y -> x*y
단, 나눗셈 몫 계산할 때 y는 0 안됨
#문제분석
    변수:x(정수1), y(정수2)
#알고리즘
    1.변수선언
        x와  y에 정수 입력 받기
    2.논리(선택.중첩if)
        if x>y : 
            if y!=0 :
                x//y
        elif x<y:
            x+y
        else:
            x*y
'''

x=int(input("x의 값을 입력하세요. : "))
y=int(input("y의 값을 입력하세요. : "))

if x>y : 
    if y!=0 :
        print("{} // {} = {}".format(x,y,x//y))
    else:
        print("y의 값이 0 입니다.")
elif x<y:
    print("{} + {} = {}".format(x,y,x+y))
else:
    print("{} + {} = {}".format(x,y,x+y))