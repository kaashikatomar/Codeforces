num = int(input())
copy = num
new = 0
while num > 0:
    digit = num % 10
    num = num // 10
    new = new * 10 + digit 
print (new)
if new == copy:
    print("YES")
else:
    print("NO")