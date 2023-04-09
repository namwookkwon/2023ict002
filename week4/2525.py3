hour,min= map(int, input().split())

count = int(input())



if min+count>=60 and hour+((min+count)//60) <24:
     mean=(min+count)//60
     kevin=(min+count)-(60*mean)
     master=hour+mean
     print(master ,kevin)
     
elif hour+ ((min+count)//60) >23 :
         mean=(min+count)//60
         kevin=(min+count)-(60*mean)
         master=hour+mean
         master=hour+mean-24
         print(master ,kevin)
     

else:
     print(hour, min+count)