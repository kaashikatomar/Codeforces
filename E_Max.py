n = int(input())
num = list(map(int, input().split()))
m = 0
for i in range (0, len(num)):
    if num[i] > m:
        m = num[i]
print (m)