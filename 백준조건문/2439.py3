num = int(input())
for i in range(num, 0, -1):
    for k in range(i - 1, 0, -1):
        print(" ", end="")
    for z in range(i, num + 1):
        print("*", end="")
    print()