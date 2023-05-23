'''
2023.05.23
김수종
파일 입출력
#문제정의
    stu.txt 파일을 읽어서 각 학생의 평균 성적 계산해서 출력하기
#문제분석
    변수 - 한 줄 씩 읽어서 저장(score), 리스트자료로 변환(scorelist)
           리스트에서 이름 항목 저장 (name), 합계(sum)
#알고리즘
    1. 파일 열기(읽기)
    2. 파일 처리
    (반복)While True :
        (선택)if  score='':
                break
        한 줄씩 읽어서 score에 저장
        읽어온 내용을 리스트로 변환해서 scorelist에 저장
        scorelist에서 첫 번째 항목(이름)을 name변수에 저장
        (반복) for i in range(1,4) :
            scorelist의 1, 2, 3 항목의 값을 sum에 더하기
    3. 파일 닫기
'''

f=open("C:/data/stu.txt.txt","r") #읽기모드 파일 객체 생성
while True : #무한반복
    score=f.readline() #한 줄씩 읽어오기
    if score=='' :
        break #반복 종료
    scorelist=score.split() #리스트 자료로 변환
    name=scorelist[0] #리스트 첫 번째 항목은이름

    sum=0 #합계
    for i in range(1, 4) :
        sum+=int(scorelist[i]) #3과목 성적의 합계

    print(name,"의 평균 성적은 :%.1f"%(sum/3))

f.close #파일 닫기