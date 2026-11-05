num = int(input())
n = list(map(int, input().split()))
even = 0
odd = 0
positive = 0
negative = 0
def check_number(n):
    global even, odd, positive, negative
    if n > 0:
        positive += 1
    elif n < 0:
        negative += 1
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
x = check_number(n)
print ("Even:", even)
print ("Odd:", odd)
print ("Positive:", positive)
print ("Negative:", negative)

