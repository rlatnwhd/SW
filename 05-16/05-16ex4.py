'''
2023.05.16
김수종
파일 입출력 - seek():파일의 처음으로 포인트 이동
'''

f=open("C:/data/test.txt","r") #읽기

print(f.read(10),end="")
print(f.read(10),end="")
print(f.read(10))

f.seek(0) #파일의 처음으로 포인트 이동

print(f.read(10),end="")
print(f.read(10),end="")
print(f.read(10))

f.close #파일 종료