'''
2023.05.23
김수종
파일 입출력
#문제정의
    단수를 발생시켜 num.txt파일을 만들고, 이 파일을 이용해서 각 학생의 평균을 구한다음 avg.txt파일에 저장 하기
'''

import random as r #난무 모듈 추가

with open("C:/data/num.txt","w") as f : #쓰기 모드의 파일 객체 생성
    for i in range(5) : #줄 반복
        for j in range(5) : #랜덤 수 찍기 반복
            f.write(str(r.randint(1,100))) #랜덤수 파일에 찍기
            f.write(' ') #숫자 다음 공백 찍기
        f.write('\n') #줄 바꿈

with open("C:/data/num.txt","r") as f1 : #읽기 모드의 파일 객체 생성
    with open("C:/data/avg.txt","w") as f2 : #쓰기 모드의 파일 객체 생성
        l=1 #학생 번호 출력
        while True : #무한 반복
            score=f1.readline() #한 줄 읽어오기
            if score=='' : #내용이 없으면
                break #반복문 중지
            scorelist=score.split() #읽어 온 한 줄을 공백 기준으로 리스트 변환
            sum=0 #합계
            for i in range(5) : #한 학생당 5과목의 점수 더하기
                    sum+=int(scorelist[i])
            print(l,"번 학생의 평균 : ", sum/5, file=f2) #결과 파일에 저장
            l+=1

