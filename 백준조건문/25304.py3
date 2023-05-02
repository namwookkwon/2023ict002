num = int(input())

n = int(input())

k=0
for i in range(n):
    a,b = map(int , input().split())
    k += a*b


if k==num:
    print("Yes")

else:
    print("No")