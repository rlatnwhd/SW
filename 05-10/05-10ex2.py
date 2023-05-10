'''
2023.05.10
김수종
#문제정의
    입력받은 숫자의 합이 1000이상이면 합계와 평균 출력
#문제분석
    변수-합계(sum), 입력횟수(cnt), 평균(avg), 정수(num)
#알고리즘
    1.변수선언(변수 초기화)
        num을 정수로 입력 받기
        sum=0, cnt=0, avg=0
    2. 프로그램 논리(반복안에 선택 포함)
        while True:
            num  키보드로 입력
            cnt 1씩증가
            sum에 더하기
            if sum>=1000:
                break
'''

sum=0
cnt=0
avg=0

while True:
    num=int(input("숫자 입력 : "))
    cnt+=1
    sum+=num
    if sum>=1000:
        break

avg=sum/cnt 

print("1000을 넘은 수 :",sum,end=" ")
print("평균:%.2f"%avg)