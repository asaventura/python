x = int(input('Enter income amount: '))
y = int(input('Now enter amount of expenses: '))
if x < y:
    print('Omg, your business if unprofitable!')
else:
    p = x - y
    print(f"Alright, you're gainig some cash! Youre profit is {p}$")
    r = p / x * 100
    print(f"Profitability of youre business is {r}%")
    q = int(input("Now enter quantity of employees: "))
    p1 = p / q
    print(f"Amount of profit per one employee is {p1}$")
