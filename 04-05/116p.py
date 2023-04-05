'''
2023.04.04
김수종
본봉과 수당을 정수로 입력 받아서 이번달 월급 수령액 구하기(116p - 9)
'''

sal=int(input("본봉 : ")) #본봉 입력
pay=int(input("수당 : ")) #수당 입력
tax=(sal+pay)*0.2 #세금 계산
res=sal+pay-tax #수령액 계산
print("본봉이 {}이고, 수당이 {}일때 실수령액은 {}만원이다.".format(sal,pay,res))