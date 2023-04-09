num1 , num2 , num3 = map(int, input().split())

if num1==num2==num3:
   print(10000+(num1*1000))

elif (num1==num2) or (num1==num3) or (num2==num3):
     if num1==num2:
       special=num1
       print(1000+(special*100))

     elif num1==num3:
       magic=num1
       print(1000+(magic*100))

     else:
        pan=num2
        print(1000+(pan*100))

else :
  max=num1 if num1 > num2 else num2
  max=num3 if num3 > max else max
  print(max*100)