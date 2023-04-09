hour, min =map(int, input().split())

if min<45 and hour>0:
  min1 = min -45 
  if min1 <0 :
      hour1 =hour -1
      min2 = min1+60
      print(hour1 , min2) 

elif min<45 and hour<=0:
      min1 = min -45 
      if min1 <0:
        hour2 =hour -1
        min2 = min1+60
        if hour<=0:
            hour2 =hour2 +24
                
        print(hour2 , min2)
       
    
else :
  min3 = min-45
  print(hour, min3)
