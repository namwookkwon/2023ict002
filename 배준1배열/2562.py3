lin=[]

for i in range(1, 10):
    num=int(input())
    lin.append(num)
     
print(max(lin))
print(lin.index(max(lin))+1)