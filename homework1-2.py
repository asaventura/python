x = int(input('Enter amount of seconds: '))
s = x % 60
m1 = x // 60
m = m1 % 60
h1 = m1 // 60
h = h1 % 24
d = h1 // 24
print(f'{d}d:{h:02}h:{m:02}m:{s:02}s')
