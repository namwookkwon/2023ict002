array=[]
count=0

while True:
    num=int(input())
    array.clear()
    if num==-1:
        break
    for i in range(1,num):
        if num%i==0:
            array.append(i)

    if sum(array)==num:
        print(num, end=' = ') 
        for x in range(len(array)):
            print(array[x], end='')
            if(x!=len(array)-1):
                print(' + ',end='')
        print()


    else:
        print(num, "is NOT perfect." )