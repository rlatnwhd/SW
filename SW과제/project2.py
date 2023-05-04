'''
2023.05.04
김수종
1부터 100까지의 합을 구하는 프로그램
단, 10을 기준으로 합을 구함
1. 조건 추출
    i%10==0 (10으로 나누어 떨어질때마다 출력)
2. 연계된 논리 결정
    while i <= 100 : (100까지 실행)
3. 논리구조도
    while i <= 100 : (반복조건)
        sum+=1 (합계)
        if i%10==0 : (조건)
            1부터 i까지의 합 출력
        i+=1 (i가 1씩증가)
'''

sum=0 #합계 초기화
i=1 #반복횟수 초기화

while i <= 100 : #반복조건
    sum+=i #합계
    if i%10==0 : #조건
        print("1 ~ {} : {}".format(i,sum)) #합계출력
    i+=1 #i가 1씩 증가
