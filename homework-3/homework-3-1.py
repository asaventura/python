def user_data(name, surname, yof, city, email, phone):
    """

    Ввозвращает введенные аргументы в одну строку
    """
    print(f'{name} {surname} {yof} {city} {email} {phone}')


user_input = input('Введите через пробел имя, фамилию, год рождения, город проживания, email и телефон: ').split(' ')
user_data(name=user_input[0], surname=user_input[1], yof=user_input[2],
          city=user_input[3], email=user_input[4], phone=user_input[5])
