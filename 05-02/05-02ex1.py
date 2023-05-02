'''
2023.05.02
김수종
파이썬 내장함수
'''

#자료형 변환 함수
s='123123' #2변수에 문자열 '123'저장

ch1=int(s) #ch1 변수에 s를 int(정수)로 변환해서 저장
ch2=list(s) #ch2 변수에 s를 list(리스트)로 변환해서 저장
ch3=tuple(s) #ch3 변수에 s를 tuple(튜플)로 변환해서 저장
ch4=set(s) #ch4 변수에 s를 set(집합)로 변환해서 저장(중복 제거)

print('{}의 자료형은 {}'.format(ch1,type(ch1)))
print('{}의 자료형은 {}'.format(ch2,type(ch2)))
print('{}의 자료형은 {}'.format(ch3,type(ch3)))
print('{}의 자료형은 {}'.format(ch4,type(ch4)))

print() #한줄 띄우기

num1=abs(-5) #num1변수에 -5의 절대값 저장
num2=round(4.6) #num2변수에 반올림 값 저장
num3=bin(10) #num3변수에 정수 10을 2진수로 변환해서 저장
str1=chr(97) #str1변수에 97에 해당하는 문자 반환
str2=ord('A') #str2변수에 'A'에 해당하는 숫자(아스키 코드 값) 반환

print('-5의 절대값 :', num1)
print("4.6의 반올림 값 :", num2)
print('정수10의 2진수값 :', num3)
print('97에 해당하는 문자 :', str1)
print('A에 해당하는 숫자(아스키 코드 값) :', str2)

print() #한줄 띄우기

num10=[6,3,5,1,9,2,8] #리스트자료형
print('num10 원소 중 가장 큰 값 :',max(num10))
print('num10 원소 중 가장 작은 값 :',min(num10))
print('num10 원소들의 합계 :',sum(num10))
print('num10 원소들 정렬 : :',sorted(num10))

print() #한줄 띄우기

print(zip('123',('kim','lee','park')))
print(list(zip('123',('kim','lee','park')))) #문자열과 튜플을 묶어서 리스트 자료형으로 반환
print(tuple(zip('123',('kim','lee','park')))) #문자열과 튜플을 묶어서 튜플 자료형으로 반환