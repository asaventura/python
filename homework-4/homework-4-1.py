my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el[1] for el in enumerate(my_list) if el[1] > my_list[el[0] - 1] and el[0] != 0]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")
