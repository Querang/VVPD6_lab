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
