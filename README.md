# **Пакет, решающий задачу "Про Markdown"**

![](https://img.shields.io/github/watchers/Querang/VVPD6_lab?style=social)
![Python](https://img.shields.io/pypi/pyversions/clubhouse?color=red)

**stars_project** - основный пакет репозитория, выполняющий обрамление подаваемых строк, осуществляет реализацию интерфейса командный строки

Задача ссылается на непосредственное применение языка размертки [Markdown](https://ru.wikipedia.org/wiki/Markdown)

## **Описание**

```stars_functions```  - модуль, выполняющий непосредственное обрамление. Содержит в себе функции ```turn_single_string``` и ```turn_double_string```

Функция```turn_single_string``` выполняет обрамление строки в одинарные звездочки. Ниже представление пример:
```
Aргумент:
    *string_to_turn*

Возвращает:
    <em>string_to_turn</m>
```
Схожим образом работает и функция ```turn_double_string```, однако она уже обрамляет в двойные звездочки. Пример
```
Аргумент:
    **string_to_turn**
    
Возвращает:
    <strong>string_to_turn</strong>
```
**```__main__.py```** - модуль, для реализации интерфейса командной строки

## **Код основных модулей**

Код для модуля ```__main__.py```:
```python
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
```
Код для модуля ```stars_function.py```:
```python
def turn_single_star(string_to_turn):
    """
    Функци оборачивающая строки с одинарными звездочками

    :param string_to_turn: str, оборачиваемые строка
    :return str, обёрнутая или неизмененная строка
    """
    find_value_1 = string_to_turn.find('*')
    find_value_2 = string_to_turn.rfind('*')
    if find_value_1 == -1 or find_value_1 == find_value_2 or find_value_2 - find_value_1 == 1:
        return string_to_turn
    else:
        return '<em>' + string_to_turn[1:find_value_2] + '</em>' + string_to_turn[find_value_2+1:]


def turn_double_star(string_to_turn):
    """
    Функци оборачивающая строки с двойными звездочками звездочками

    :param string_to_turn: str, оборачиваемая строка
    :return str, обёрнутая или неизмененная строка
    """
    find_value_1 = string_to_turn.find('**')
    find_value_2 = string_to_turn.rfind('**')
    if find_value_1 == -1 or find_value_1 == find_value_2 or len(string_to_turn) <= 4\
            or find_value_2 - find_value_1 == 2:
        return string_to_turn
    else:
        return '<strong>' + string_to_turn[2:find_value_2] + '</strong>' + string_to_turn[find_value_2+2:]
```
## **Установка**

Чтобы установить текущую версию пакета введите в консоль команду:
```bash
pip install https://github.com/Querang/VVPD6_lab.git
```
## **Применение**

Для запуска программы программы из командой строки используйте команду:
```bash
python __main__.py string_to_turn
```
Пример:
```bash
python __main__.py '**cake is a lie**'
```
>```<em>*cake is a lie*</em>```
> 
> ```<strong>cake is a lie</strong>```

Для каждого отдельного модуля пакета была написана документация.

Лаборатная работа №6 по задаче №9, Выполнена Борисюком Кириллом Алексеевичем в рамках обучения в Сибирском 
Федеральном Университете
![SibFUlogotype](https://online.sfu-kras.ru/pluginfile.php/1606/mod_page/content/67/sfu.png)