n, m = map (int,input().split())
x = min(n,m)
ans = 1
for i in range (1, x+1):
    if n % i == 0 and m % i == 0:
        ans = i
print (ans)