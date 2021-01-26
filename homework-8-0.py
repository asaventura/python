class Date:
    def __init__(self, dd_mm_yy='00-00-00'):
        self.date_string = dd_mm_yy

    @classmethod
    def divided_int(cls, dd_mm_yy='00-00-00'):
        date_list = [int(el) for el in dd_mm_yy.split('-')]
        return date_list

    @staticmethod
    def valid_date(dd_mm_yy='00-00-00'):
        """
        :param dd_mm_yy: дата в формате строки "dd-mm-yyyy"
        :return: проверяет правильность даты с учетом дней в каждом месяце и високосных лет
        """
        valid_date = 'The date is valid'
        invalid_date = 'The date is not valid'
        date_list = [int(el) for el in dd_mm_yy.split('-')]
        if date_list[1] in range(1, 13):
            if date_list[1] in {1, 3, 5, 7, 8, 10, 12} and date_list[0] in range(1, 32):
                return valid_date
            elif date_list[1] in {4, 6, 9, 11} and date_list[0] in range(1, 31):
                return valid_date
            elif date_list[1] == 2 and date_list[0] in range(1, 30):
                if date_list[0] == 29 and date_list[2] % 400 != 0:
                    if date_list[2] % 4 != 0 or date_list[2] % 100 == 0:
                        return invalid_date
                    else:
                        return valid_date
                else:
                    return valid_date
            else:
                return invalid_date
        else:
            return invalid_date


date = Date.valid_date('29-02-2000')
print(date)
