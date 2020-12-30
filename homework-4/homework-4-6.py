def fact(num):
    a = 1
    for i in range(1, num+1):
        a *= i
        yield a


g = fact(int(input('Enter number: ')))
factorial_list = [n for n in g]
print(factorial_list)
