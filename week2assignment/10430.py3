A,B,C =map(int , input().split())

num1= (A+B)%C
num2 = ((A%C) + (B%C))%C
num3= (A*B)%C
num4 = ((A%C) * (B%C))%C

print(num1)
print(num2)
print(num3)
print(num4)