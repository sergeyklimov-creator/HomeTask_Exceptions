class DiscrepancyException(Exception):
   def __init__(self, message):
        self.text = message

def get_prefix_lists(text, *operations):
    math_list = []
    number_list = text.split()
    
    while number_list[0] in operations:
        math_list += number_list.pop(0)
        
    return math_list[::-1], number_list


def main():
   
    try:
        math_list, number_list = get_prefix_lists(
            input('Введите пример "польской" нотации: ').strip(),
            '+', '-', '*', '/'
        )
        assert len(math_list) != 0, 'не указаны операции'
        if len(math_list)+1 != len(number_list):
            raise DiscrepancyException('ОШИБКА: количество операций не соответвует количеству операндов')

    except IndexError:
        print('ОШИБКА: отсуствует требуемый набор входных данных')
        return None
    except AssertionError:
        print('ОШИБКА: в начале строки д.б. указаны операции. Допустимые операции: +, -, *, /')
        return None
    except DiscrepancyException as de:
        print(de)
        return None
    result = number_list.pop(0)
    
    try:
        for number, operation in zip(number_list, math_list):
            print(f'  действие: {str(result)} {operation} {number} = {eval(str(result) + operation + number)}')
            result = eval(str(result) + operation + number)
    except ZeroDivisionError:
        print('ОШИБКА: деление на ноль. Проверьте входные данные')
    except SyntaxError:
        print(f'ОШИБКА: невозможно выполнить арифметическую операцию над строками: {str(result)}{operation}{number}. Проверьте входные данные')
    else:    
        print(f'Итог вычислений: {result}')
    
main()