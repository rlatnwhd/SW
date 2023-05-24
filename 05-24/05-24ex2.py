'''
2023.05.23
김수종
파일 입출력
#문제정의
    score1.txt파일을 읽어서 각 학생의 등급을 결정하고 결과를 report1.txt파일에 저장하기
'''

score=[] #빈 리스트 변수생성
f=open("C:/data/score1.txt.txt","r") #읽기 모드의 파일 객체 생성
for i in range(10): #10명의 학생 점수 읽어 오기
    score.append(f.readline().split())

for i in range(10): #10명의 학생 점수에 대한 평균 등급 계산
    score[i][1]=float(score[i][1]) #문지열을 실수로 변횐

    if score[i][1] >= 90 : #점수가 90이상
        score[i].append("A") 
    elif score[i][1] >= 80 : #점수가 80이상, 90미만
        score[i].append("B") 
    elif score[i][1] >= 70 : #점수가 70이상, 80미만
        score[i].append("C")
    else : #점수가 70미만
        score[i].append("D")
    
for i in range(10): #10명 등급 화면 출력
    print("{:<5}{:>5}".format(score[i][0],score[i][2]))

f.close