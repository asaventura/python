list1 = list(input("Enter list: "))
list1[::2], list1[1::2] = list1[1::2], list1[::2]
print(list1)
