num1=int(input("정수 1 입력 : "))
num2=int(input("정수 2 입력 : "))
op=input("연산자 입력 : ")
if op == '+' :
    print("{} + {} = {}".format(num1,num2,num1+num2))
elif op == '-' :
    print("{} - {} = {}".format(num1,num2,num1-num2))
elif op == '*' :
    print("{} * {} = {}".format(num1,num2,num1*num2))
else :
    print("{} / {} = {}".format(num1,num2,num1/num2))
