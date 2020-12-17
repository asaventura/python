x = int(input('Enter positive integer: '))
l = x%10
x = x//10
while x > 0:
    if x%10 > l:
        l = x%10
    x = x//10
print(l)
