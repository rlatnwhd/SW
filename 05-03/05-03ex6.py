'''
2023.05.03
김수종
#문제정의
    구구단 1~9단까지 모두 출력
#문제분석
    변수-i,j(반복횟수)
#알고리즘.
    논리(반복-이중for문)
        for i in range(2,10) : (조건)
            제목 출력
            for j in range(1,10) : (조건)
                구구단 출력
'''

for i in range(2,10) : #조건
    print(i,"단") #단 제목 출력
    for j in range(1,10) : #조건
        print("{} * {} = {}".format(i,j,i*j)) #출력