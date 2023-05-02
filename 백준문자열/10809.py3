a = input()

for i in range(26):
  if chr(ord("a")+i) in a:
    print(a.index(chr(ord("a")+i)),end=" ")


  else:
    print("-1", end=" ")