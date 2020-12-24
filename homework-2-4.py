list1 = [7, 5, 3, 3, 2]
pos = 0
new_val = int(input('Введите натуральное число: '))
for val in list1:
    if new_val <= val:
        pos = list1.index(val) + 1
list1.insert(pos, new_val)
print(list1)