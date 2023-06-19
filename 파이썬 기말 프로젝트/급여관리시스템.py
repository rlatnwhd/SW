'''
2팀 급여관리 프로그램
김수종, 남태호, 김유민
! Chat GPT를 사용하지 않았습니다. !
'''
import datetime as d
with open("C:/Users/kimsj/OneDrive/바탕 화면/과제 모음/SW과제/과제/data/company_list.txt", "r", encoding="utf-8") as f:
    with open("C:/Users/kimsj/OneDrive/바탕 화면/과제 모음/SW과제/과제/data/tax.txt", "r", encoding="utf-8") as tax:
        while True :
            print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
            t=0
            print("안녕하세요! 급여 관리 시스템입니다.")
            start=input("앱을 사용하시려면 \"yes\"를, 종료 하시려면 \"no\"를 입력해주세요. : ")
            print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
            if start.lower()=='no' :
                break
            if start.lower()=='yes' :
                name1=input("성명을 띄어쓰기 없이 입력하여 주십시오. : ")
                print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
                print("성명 확인중입니다. 잠시만 기다려 주십시오.")
                print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
                while True :
                    company_list_t=f.readline()
                    if company_list_t=='' :
                        print("이름이 존재하지 않습니다.")
                        f.seek(0)
                        t=1
                        break
                    rank_list=company_list_t.split()
                    name2=rank_list[0]
                    if name1 == name2 :
                        print("반갑습니다!")
                        f.seek(0)
                        break
                    rank_list=[]
                    
                if t==0:
                    cnt=0
                    while True :
                        p=0
                        number=input("사원 번호를 입력해 주십시오. : ")
                        rank_list[2]
                        if rank_list[2]!=number :
                            cnt+=1
                            print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
                            print(f"잘못 입력하셨습니다. | 남은 시도 횟수 : {(3-cnt)}번")
                            print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
                        elif rank_list[2]==number :
                            break
                        if cnt==3 :
                            print(f"사원 번호 입력횟수 초과")
                            print(f"메인화면으로 돌아갑니다.")
                            p=1
                            break
                    if p==1 :
                        continue
                    print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
                    print("님의 이번달 급여액은 다음과 같습니다.")
                    print()
                    pay=2500000 #기본급
                    
                    if rank_list[1]=='사원' : #직급에 따른 월급 추가
                        pay+=500000
                    elif rank_list[1]=='주임' :
                        pay+=1000000
                    elif rank_list[1]=='대리' :
                        pay+=1500000
                    elif rank_list[1]=='과장' :
                        pay+=2000000
                    elif rank_list[1]=='차장' :
                        pay+=2500000
                    else :
                        pay+=3000000
                    
                    today=d.date.today() #입사년도의 1년마다 추가 월급
                    now_year=today.year
                    now_month=today.month
                    
                    hire_year=int(rank_list[3])
                    hire_month=int(rank_list[4])
                    
                    el_year=now_year - (hire_year)
                    
                    el_month=(now_year-hire_year)*12+(now_month-hire_month)
                    if (el_month//12)<1 :
                        salary_inc = 0
                    else :
                        salary_inc = (el_month//12) * 100000
            
                    pay+=salary_inc
                    
                    while True : #소득세
                        taxa=tax.readline()
                        if taxa=='':
                            print("소득세 범위 밖입니다.")
                            tax.seek(0)
                            break
                        tax_list=taxa.split()
                        if (int(tax_list[0])*1000)==pay :
                            inc_tax=int(tax_list[2])
                            tax.seek(0)
                            break
                        tax_list=[]
                        
                    #세금 계산
                    
                    local_inc_tax=inc_tax*0.10 
                    he_insurance=pay*0.03545
                    me_insurance=he_insurance*0.1281
                    em_insurance=pay*0.09
                    na_pesion=pay*0.045
                    pay-=local_inc_tax+he_insurance+me_insurance+em_insurance+na_pesion
                    
                    print("소득세 : {}원".format(format(int(inc_tax),',')))
                    print("지방소득세 : {}원".format(format(int(local_inc_tax),',')))
                    print("건강보험 : {}원".format(format(int(he_insurance),',')))
                    print("요양보험 : {}원".format(format(int(me_insurance),',')))
                    print("고용보험 : {}원".format(format(int(em_insurance),',')))
                    print("국민연금 : {}원".format(format(int(na_pesion),',')))
                    
                    print("이번달 실수령액 : {}원".format(format(int(pay),',')))
                    k=0
                    while True :
                        print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
                        report=input("봉급에 대한 이의를 제기하시려면 \"yes\"를, 종료 하시려면 \"no\"를 입력해주세요. : ")
                        print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
                        if report.lower()=='no':
                            print("메인 화면으로 돌아갑니다.")
                            break
                        elif report.lower()=='yes':
                            with open("C:/Users/kimsj/OneDrive/바탕 화면/과제 모음/SW과제/과제/data/report.txt", "w", encoding="utf-8") as ref:
                                report_main=input("이의 내용을 적어 주십시오.(내용 입력 시 엔터키 금지) : ")
                                while True :
                                    print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
                                    return_idt=input("전송 하시려면 \"yes\"를, 종료 하시려면 \"no\"를 입력해주세요. : ")
                                    print("―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
                                    if return_idt.lower()=='no':
                                        print("종료하고 메인화면으로 돌아갑니다.")
                                        k=1
                                        break
                                    elif return_idt.lower()=='yes':
                                        print((name1+" "+rank_list[1]+" : "+report_main),file=ref)
                                        print("성공적으로 전송되었습니다.")
                                        k=1
                                        break
                                    else: 
                                        print("올바르지 않습니다. 다시 입력해주십시오.")
                                if k==1 :
                                    break
                        else: 
                            print("올바르지 않습니다. 다시 입력해주십시오.")
            else :
                print("올바르지 않습니다. 다시 입력해주십시오.")
                                       
    print("이용해 주셔서 감사합니다!")