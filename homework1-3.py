x = int(input('Enter number from 0 to 9: '))
if x > 9 or x < 0:
    int(input('Try again: '))
xx = int(str(x) * 2)
xxx = int(str(x) * 3)
p = x + xx + xxx
print(p)
