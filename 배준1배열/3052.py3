array=[0] * 42

for i in range(1,11):
  array[int(input()) % 42] = 1

cnt = 0
for i in range(42):
  if array[i] == 1:
    cnt += 1
  
print(cnt)