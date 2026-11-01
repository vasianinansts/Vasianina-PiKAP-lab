# Рубежный контроль №1 по курсу ПиК ЯП
# Васянина А.А., ИУ5-36Б
# Вариант Д9: Операционная система — Компьютер

from operator import itemgetter


class OS:
    def __init__(self, id, name, size, comp_id):
        self.id = id
        self.name = name
        self.size = size
        self.comp_id = comp_id


class Computer:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class OSComputer:
    def __init__(self, comp_id, os_id):
        self.comp_id = comp_id
        self.os_id = os_id


computers = [
    Computer(1, 'Аудиторный компьютер 305'),
    Computer(2, 'Сервер баз данных'),
    Computer(3, 'Административный компьютер'),
    Computer(4, 'Ноутбук преподавателя'),
]

oss = [
    OS(1, 'Astra Linux', 20, 1),
    OS(2, 'Ubuntu Server', 25, 2),
    OS(3, 'Windows 11', 64, 3),
    OS(4, 'Альт Рабочая станция', 30, 1),
    OS(5, 'Дебианов', 18, 2),
    OS(6, 'macOS', 35, 4),
]

oss_computers = [
    OSComputer(1, 1),
    OSComputer(1, 4),
    OSComputer(1, 3),
    OSComputer(2, 2),
    OSComputer(2, 5),
    OSComputer(3, 3),
    OSComputer(3, 1),
    OSComputer(4, 6),
    OSComputer(4, 2),
]


def main():
    one_to_many = [(o.name, o.size, c.name)
                   for c in computers
                   for o in oss
                   if o.comp_id == c.id]

    many_to_many_temp = [(c.name, oc.comp_id, oc.os_id)
                         for c in computers
                         for oc in oss_computers
                         if c.id == oc.comp_id]

    many_to_many = [(o.name, o.size, comp_name)
                    for comp_name, comp_id, os_id in many_to_many_temp
                    for o in oss if o.id == os_id]

    print('Задание Д1')
    res_1 = [(os_name, comp_name) for os_name, _, comp_name in one_to_many if os_name.endswith('ов')]
    for os_name, comp_name in res_1:
        print(f'{os_name} - {comp_name}')

    print('\nЗадание Д2')
    res_2_unsorted = []
    for c in computers:
        sizes = [size for _, size, comp_name in one_to_many if comp_name == c.name]
        if len(sizes) > 0:
            res_2_unsorted.append((c.name, sum(sizes) / len(sizes)))
    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    for comp_name, avg in res_2:
        print(f'{comp_name}: {avg:.2f} ГБ')

    print('\nЗадание Д3')
    res_3 = {}
    for c in computers:
        if c.name.startswith('А'):
            res_3[c.name] = [os_name for os_name, _, comp_name in many_to_many if comp_name == c.name]
    for comp_name, os_names in res_3.items():
        print(f'{comp_name}: {", ".join(os_names)}')


if __name__ == '__main__':
    main()
