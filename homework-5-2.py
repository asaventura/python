with open('employees.txt') as employees:
    lines = employees.readlines()
    sum_salaries = 0
    for l in lines:
        if int(l.split(' ')[1]) < 20000:
            print(f'{l.split()[0]} has salary less then 20000$')
        sum_salaries += int(l.split(' ')[1])
    print(f'Average salary is {sum_salaries / len(lines)}$')
