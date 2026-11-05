n = int(input())
for i in range (2, n+1):
    ans = True
    for j in range (2, i):
        if i % j == 0:
            ans = False
            break 
    if ans:
        print(i, end = " ")