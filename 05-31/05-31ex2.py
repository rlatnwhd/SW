'''
2023.05.31
김수종
#문제정의
    이차원 리스트의 학생 점수를 참고하여 각 학생의 3과목 총점 구하기
#문제분석
    변수 - 점수리스트(num)
#알고리즘
    1. 변수 초기화
        num=[]
    3. 반복
        for i in range(5):
            결과 출력((학생 이름)의 총점은 : (총합))
'''

num=[[2020001,2020002,2020003,2020004,2020005],[89,74,88,99,95],[91,75,68,98,88],[79,94,68,94,92]]
j=0
for i in range(len(num[0])): #리스트 요소만큼 반복
    print(num[j][i],"학생의 총점은 : ", num[j+1][i]+num[j+2][i]+num[j+3][i])