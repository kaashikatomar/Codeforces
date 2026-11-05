n = list(map(int, input().split()))
m = 0
for i in range (1, len(n)):
    if n[i] > max(n):
        m = n[i]
print (m)