from itertools import count
from itertools import cycle

num_list = []
for num in count(3):
    if num <= 10:
        num_list.append(num)
    else:
        break
print(num_list)
c = 0
for el in cycle(num_list):
    if c >= len(num_list) * 3:
        break
    print(el)
    c += 1

