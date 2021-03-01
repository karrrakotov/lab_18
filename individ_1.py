#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

#   Запись о багаже пассажира авиарейса содержит следующие поля:
#   номер рейса, дата вылета, пункт назначения, фамилия пассажира, количество мест багажа,
#   суммарный вес багажа.
#   Поиск выполнять по номеру рейса, дате вылета, пункту назначения, весу багажа (превышение максимально допустимого).


class SimpleIterator:

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return 1
        else:
            raise StopIteration


if __name__ == '__main__':
    # Список данных о багаже.
    baggage = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            # Запросить запись о багаже.
            second_name = input("Введите фамилию пассажира: ")
            number_of_seats = int(input("Введите кол-во мест багажа: "))
            flight_number = list(map(int, input("Введите номер рейса: ").split(".")))
            date = list(map(int, input("Введите дату вылета: ").split(".")))
            location = list(map(str, input("Введите пункт назначения: ").split(".")))
            weight = list(map(int, input("Введите суммарный вес багажа: ").split(".")))

            # Создать словарь.
            information = {
                'second_name': second_name,
                'number_of_seats': number_of_seats,
                'flight_number': flight_number,
                'date': date,
                'location': location,
                'weight': weight
            }

            baggage.append(information)
            if len(baggage) > 1:
                baggage.sort(key=lambda item: item.get('name', ''))
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8,
                '-' * 8,
                '-' * 8,
                '-' * 8,
                '-' * 8,
                '-' * 11
            )
            print(line)
            print(
                '| {:^3} | {:^30} | {:^20} | {:^8} | {:^8} | {:^8} | {:^8} | {:^8} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Группа",
                    "1-ая оценка",
                    "2-ая оценка",
                    "3-ая оценка",
                    "4-ая оценка",
                    "5-ая оценка"
                )
            )
            print(line)
            # Вывести данные о всех сотрудниках.
            for idx, person in enumerate(students, 1):
                print(
                    '| {:>3} | {:<30} | {:<20} | {:>11} | {:>11} | {:>11} | {:>11} | {:>11} |'.format(
                        idx,
                        person.get('name', ''),
                        person.get('group', ''),
                        person.get('marks[0]', f'{marks[0]}'),
                        person.get('marks[1]', f'{marks[1]}'),
                        person.get('marks[2]', f'{marks[2]}'),
                        person.get('marks[3]', f'{marks[3]}'),
                        person.get('marks[4]', f'{marks[4]}')
                    )
                )
            print(line)
        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            period = int(parts[1])

            count = 0
            for person in students:
                if 2 in marks:
                    count += 1
                    print(
                        '{:>4}: {}'.format(count, person.get('name', ''))
                    )
            # Если счетчик равен 0, то работники не найдены.
            if count == 0:
                print("Нет студентов, которые получили оценку - 2.")
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("select <оценка> - найти студентов которые получили такую оценку;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)