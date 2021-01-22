import itertools


class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

#    def __getitem__(self, index):
#        return self.list_of_lists[index]
# класс работает как задуманно с __getitem__ и __iter__ вместе и поотдельности, но не работает без них обоих
# поэтому возник вопрос, какой метод правильнее использовать? По документации подходят они одинаково

    def __iter__(self):
        return iter(self.list_of_lists)

    def __str__(self):
        strings = []
        for lists in self.list_of_lists:
            lists = [str(el) for el in lists]
            strings.append(' '.join(lists))
        return '\n'.join(strings)

    def __add__(self, other):
        rows = []
        for index, lists in enumerate(other):
            rows.append([])
            rows[index].extend([x + y for x, y in zip(lists, self.list_of_lists[index])])
        new_matrix = (Matrix(rows))
        return new_matrix


my_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
my_list2 = [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
matrix = Matrix(my_list)
matrix2 = Matrix(my_list2)
print(matrix)
print(matrix2)
print(matrix + matrix2)
