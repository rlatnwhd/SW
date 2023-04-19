'''
2023.04.19
김수종
성별, 키, 몸무게를 입력 받아서 BMI지수를 구하고 비만도 측정하기
#문제분석
    변수 - 키(height), 성별(sex), 몸무게(weight), 평균체중(avg)
    수식 - 
        (남) avg = height * height * 22
        (여) avg = height * height * 21
        (BMI) weight/avg*100
#알고리즘
    1. 변수 언선
        height, sex, weight (실수)로 입력받기
    2. 논리(내포된 선택)
        if 성별이 여자 :
            avg  계산
            bmi 계산
            if  bmi>=120 :
                비만
            elif 110<=bmi<=119 :
                과체중
            else :
                표준
        elif 성별이 남자 :
            avg  계산
            bmi 계산
                if  bmi>=120 :
                    비만 체중
                elif 110<=bmi<=119 :
                    과체중
                else :
                    표준        
        else 성별 잘못 입력
''' 

sex=input("성별을 입력('M' or 'm' 또는 'F' or 'f') : ") #성별 입력 받기
height=float(input("키 입력(cm) : "))//100 #키 입력 받기
weight=float(input("몸무게 입력(kg) : ")) #몸무게 입력 받기


if sex=='m' or sex=='M' :
    avg=height*height*22
    bmi=weight/avg*100
    if 110<=bmi<=119 :
        print("과체중")
    elif bmi>=120 :
        print("비만 체중")
    else :
        print("표준 체중")
elif sex=='f' or sex=='F' :
    avg=height*height*21
    bmi=weight/avg*100
    if 110<=bmi<=119 :
        print("과체중")
    elif bmi>=120 :
        print("비만 체중")
    else :
        print("표준 체중")
else :
    "성별 입력이 잘못 되었습니다."