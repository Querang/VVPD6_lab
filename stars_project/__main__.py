"""
Точка входа программы

Борисюк Кирилл Алексеевич. КИ21-17/1б. Практическая работа №6. Задача №9.

Функции:
--------
main:
    Функция, запускающая программу и реализующая точку входа
"""

import argparse
from stars_functions import turn_single_star, turn_double_star


CLI = argparse.ArgumentParser()
CLI.add_argument('string_to_convert', type=str)
arg = CLI.parse_args()


def main(given_string):
    return turn_single_star(given_string), turn_double_star(given_string)


if __name__ == '__main__':
    print(main(arg.string_to_convert))
