class IncorrectQuantity(Exception):
    def __init__(self, err_txt):
        self.err_txt = err_txt


class Warehouse:
    def __init__(self, address, capacity=100, equipment_list=[]):
        """
        :param address: уникальная метка объекта-склада
        :param capacity: вместимость склада
        :param equipment_list: список словарей атрибутов размещенных на складе объектов

        Немного не разобрался тут, нужно было назначить аргументу 'equipment_list'
        по умолчанию значение пустого списка, но PyCharm ругается на скобки, обозначающие этот список,
        подскажите, как это сделать правильнее, в гугле утонул в базовой информации по атрибутам,
        а нужной не нашел
        """
        self.address = address
        self.capacity = capacity
        self.equipment_list = equipment_list

    def get_equipment(self, *incoming_equipment):
        """

        :param incoming_equipment: неограниченное количество объектов наследников класса OfficeEquipment
        :return: размещает в конкретном объекте класса Warehouse объекты в указанном порядке
        в соотвтетсвии с вместимостью и количеством объектов; объекты, чье количество превосходит
        вместимость, размещены не будут.
        """
        for equipment in incoming_equipment:
            if self.capacity - equipment.quantity >= 0:
                self.capacity -= equipment.quantity
                self.equipment_list.append(equipment.__dict__)
                print(f'{equipment.name.capitalize()} {equipment.manufacturer} {equipment.model} '
                      f'в количестве {equipment.quantity} единиц '
                      f'принят на складе {self.address}')
                if self.capacity == 0:
                    print('Склад заполнен')
            else:
                print(f'На складе {self.address} недостаточно места, мы не можем принять '
                      f'{equipment.name} в таком количестве! Обратитесь на другой склад!')

    def give_equipment(self, department, *outgoing_equipment):
        """

        :param department: отдел компании, запрашивающий технику
        :param outgoing_equipment: объекты, которые необходимо выдать со склада
        :return: выдает указанному отделу запрашиваемую технику, если она есть на складе
        """
        e_l = self.equipment_list
        for equipment in outgoing_equipment:
            if equipment.__dict__ in e_l:
                self.capacity += equipment.quantity
                e_l.remove(equipment.__dict__)
                print(f'{equipment.name.capitalize()} {equipment.manufacturer} {equipment.model} '
                      f'выдан со склада {self.address} подразделению {department} '
                      f'в количестве {equipment.quantity}')
            else:
                print(f'Оборудования {equipment.name} на складе в {self.address} нет. '
                      f'Спросите на другом складе.')

    @property
    def info(self):
        """

        :return: информация о состоянии склада
        """
        total = 0
        copier_q = 0
        scanner_q = 0
        printer_q = 0
        for el in self.equipment_list:
            if el.get('name') == 'копировальный аппарат':
                copier_q += el.get('quantity')
            elif el.get('name') == 'сканер':
                scanner_q += el.get('quantity')
            elif el.get('name') == 'принтер':
                printer_q += el.get('quantity')
            total += el.get('quantity')
        return (f'На складе {self.address} размещено {total} единиц техники, '
                f'из которых {copier_q} единиц '
                f'копировальных аппаратов, {printer_q} единиц '
                f'принтеров,\n {scanner_q} единиц сканеров. '
                f'Осталось место для {self.capacity} единиц техники.')


class OfficeEquipment:
    def __init__(self, name, manufacturer, model, quantity=1):
        """

        :param name: имя типа оргтехники
        :param manufacturer: производитель
        :param model: модель
        :param quantity: количество

        Количество обязательно должно быть указано верно (натуральное число), в противном случае
        программа попросит исправить значение
        """
        self.name = name
        self.manufacturer = manufacturer
        self.model = model
        self.quantity = quantity
        while True:
            try:
                if int(self.quantity) < 0 or isinstance(self.quantity, float):
                    raise IncorrectQuantity(f'Количество {self.name} {self.model} указано неверно!')
                else:
                    self.quantity = int(self.quantity)
                    break
            except ValueError:
                self.quantity = input(f'Вы ввели неправильные данные о {self.name} {self.model}. '
                                      f'Укажите количество: ')
            except IncorrectQuantity as err:
                self.quantity = input(f'{err} Укажите количество: ')


class Printer(OfficeEquipment):
    def __init__(self, size_of_cartridge, manufacturer, model, quantity, name='принтер'):
        """

        :param size_of_cartridge: для объекта этого класса необходимо указать объем картриджа
        """
        OfficeEquipment.__init__(self, name, manufacturer, model, quantity)
        self.size_of_cartridge = size_of_cartridge


class Scanner(OfficeEquipment):
    def __init__(self, scan_resolution, manufacturer, model, quantity, name='сканер'):
        """

        :param scan_resolution: для объекта этого класса необходимо указать разрешение сканирования
        """
        OfficeEquipment.__init__(self, name, manufacturer, model, quantity)
        self.scan_resolution = scan_resolution


class Copier(OfficeEquipment):
    def __init__(self, tray_capacity, manufacturer, model, quantity, name='копировальный аппарат'):
        """

        :param tray_capacity: для объекта этого класса необходимо указать вместимость лотка для бумаги
        """
        OfficeEquipment.__init__(self, name, manufacturer, model, quantity)
        self.tray_capacity = tray_capacity


warehouse_1 = Warehouse('Делавер', 50)
printer_1 = Printer(1.5, 'HP', 'LaserJet', 50.1)
print(printer_1.__dict__)
scanner_1 = Scanner('16MP', 'HP', 'SuperScan', 20)
print(scanner_1.__dict__)
copier_1 = Copier(1000, 'Xerox', 'TX10', 15)
print(copier_1.__dict__)
copier_2 = Copier(1500, 'Xerox', 'CV5', 10)
print(copier_2.__dict__)
warehouse_1.get_equipment(copier_1, copier_2, printer_1, scanner_1)
print(warehouse_1.info)
warehouse_1.give_equipment("Отдел кадров", copier_1)
warehouse_1.give_equipment("Отдел кадров", printer_1)
print(warehouse_1.info)
