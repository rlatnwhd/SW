'''
2023.04.11
김수종
선택문 - if, if ~ else 함수 연습
성적이 90이상이면 'A' 출력
성적이 80이상 90미만이면 'B' 출력
성적이 70이상 80미만이면 'C' 출력
80미만이면 'F'
'''

score=int(input("성적 입력 : ")) #점수를 정수로 입력
if score >= 90 : #조건1
    print("A학점") #조건1이 참 일때만 실행
if score >= 80 : #조건2
    print("B학점") #조건2이 참 일때만 실행
if score >= 70 : #조건3
    print("C학점") #조건3이 참 일때만 실행
else : #조건4
    print("F학점") #조건이 거짓 일때만 실행
print("수고했습니다") #조건과 관계없이 항상 실행