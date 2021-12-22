"""
Модуль, создержащий тест для функций из модуля stars_functions

Борисюк Кирилл Алексеевич. КИ21-17/1б. Практическая работа №6. Задача №9.

Функции:
--------
test_string_work:
    Функция-фикстура, проверяющая корректность работа функций из модуля stars_functions.py
"""

import pytest
from ..stars_functions import turn_single_star, turn_double_star


@pytest.mark.parametrize('str_turn, result', [('*str_test*', ('<em>str_test</em>', '*str_test*')),
                                              ('**str_test**', ('<em>*str_test*</em>', '<strong>str_test</strong>')),
                                              ('str_test', ('str_test', 'str_test')),
                                              ('***test***', ('<em>**test**</em>', '<strong>*test*</strong>')),
                                              ('***test**', ('<em>**test*</em>', '<strong>*test</strong>')),
                                              ('**test', ('**test', '**test')),
                                              ('test str', ('test str', 'test str')),
                                              ('*test str*', ('<em>test str</em>', '*test str*')),
                                              ('**test str**', ('<em>*test str*</em>', '<strong>test str</strong>')),
                                              ('*test* str', ('<em>test</em> str', '*test* str')),
                                              ('**test** str', ('<em>*test*</em> str', '<strong>test</strong> str')),
                                              ('**test* str', ('<em>*test</em> str', '**test* str')),
                                              ('*test str', ('*test str', '*test str')),
                                              ('*', ('*', '*')),
                                              ('**', ('**', '**')),
                                              ('***', ('<em>*</em>', '***')),
                                              ('****', ('<em>**</em>', '****')),
                                              ('*****', ('<em>***</em>', '<strong>*</strong>'))])
def test_string_work(str_turn, result):
    assert turn_single_star(str_turn) == result[0]
    assert turn_double_star(str_turn) == result[1]
