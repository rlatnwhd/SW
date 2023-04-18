'''
2023.04.18
김수종
성적 처리 프로그램
두 과목 모두 75이상, 총점 180이상 "최우수"
총점 160이상 "우수"
총점 150이상 "보통 학생"
두 과목 모두 75점 미만이면 "분발 합시다"
#문제분석
    변수:점수1(score1),점수2(score2),합계(total)
#알고리즘
    1.변수선언
        score1, score2에 정수 입력 받기
    2.논리(선택.중첩if)
        if(score1) >= 75 and (score2) >= 75 :
            if(total)>=180:
                "최우수"
            elif(total)>=160:
                "우수"
            else:
                "보통 학생"
        else:
            "분발 합시다"
            
'''

score1=int(input("성적1 입력 : ")) #점수를 정수로 입력
score2=int(input("성적2 입력 : ")) #점수를 정수로 입력
total=score1+score2 #총합
if (score1) >= 75 and (score2) >= 75 :
    if(total)>=180:
        print("최우수")
    elif(total)>=160:
        print("우수")
    else:
        print("보통 학생")
else:
    print("분발 합시다")