# creating a calculator 
a = int(input())
b = input()
c = int(input())

if(b == '+'):
    print(a+c)
elif(b=='-'):
    print(a-c)
elif(b=='*'):
    print(a*c)
else:
    print(a/c)