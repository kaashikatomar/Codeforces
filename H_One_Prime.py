n = int(input())
ans = "YES"
for i in range (2, n):
    if n % i == 0:
        ans = "NO"
        break
else:
    ans = "YES"
print (ans)