'''
2023.04.04
김수종
5과목 점수 입력 받아서 합계 평균 구하기(117p - 14)
'''

sub1=int(input("과목1 : "))
sub2=int(input("과목2 : "))
sub3=int(input("과목3 : "))
sub4=int(input("과목4 : "))
sub5=int(input("과목5 : "))

total=sub1+sub2+sub3+sub4+sub5
avg=total/5
print("5과목의 합계는 {}이고, 평균은 {}이다.".format(total,avg))