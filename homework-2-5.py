prod_list = []
n = 0
while True:
    data_input = input('Введите через пробел название, цену, количество '
                       'и единицу измерения товара и нажмите Enter. '
                       'Введите "стоп", если хотите завершить ввод. ').split(' ')
    if data_input[0] != 'стоп':
        prod_dict = {"название": data_input[0], "цена": data_input[1], "количество": data_input[2], "ед": data_input[3]}
        n += 1
        prod_tuple = (n, prod_dict)
        prod_list.append(prod_tuple)
    else:
        break
analysis_dict = {"название": [], "цена": [], "количество": [], "ед": []}
for prod in prod_list:
    analysis_dict["название"].append(prod[1].get("название"))
    analysis_dict["цена"].append(prod[1].get("цена"))
    analysis_dict["количество"].append(prod[1].get("количество"))
    analysis_dict["ед"].append(prod[1].get("ед"))
print(analysis_dict)
