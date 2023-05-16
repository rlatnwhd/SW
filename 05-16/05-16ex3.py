'''
2023.05.16
김수종
파일 입출력 - 읽기
'''

f=open("C:/data/test.txt","r") #읽기

txts=f.read() #txt 파일의 전체 내용을 변수에 저장

print(txts) #txt 파일의 전체 내용을 저장한 변수를 출력

f.close #파일 종료