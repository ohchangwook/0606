def calc(num1,num2,act="+"):
    if act=="+":
        res==num1+num2
    elif act=="-":
        res=num1-num2
    elif act=="*":
        res==num1*num2
    elif act=="/":
        res==num1/num2
    else:
        res=="잘못된 연산기호입니다."
        

n1=int(input("첫 번쨰 정수 입력:"))
n2=int(input("두 번쨰 정수 입력:"))
print(calc(n1,n2))
print(calc(n1,n2,"-"))
print(calc(n1,n2,"*"))
print(calc(n1,n2,"/"))
print(calc(n1,n2,"^"))
