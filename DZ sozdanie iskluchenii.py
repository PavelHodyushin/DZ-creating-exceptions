class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


def func_mat(a, b):
    if b == 0:
        raise InvalidDataException("Деление на 0")
    elif type(a) != int:
        raise ProcessingException(f"Значение переменной {a}, должно быть числом!")
    else:
        return a / b


def the_func_of_varexc(a, b):
    try:
        d = func_mat(a, b)
        print(d)
    except InvalidDataException as e:
        print(f"Ошибка: {e}")
    except ProcessingException as e:
        print(f"Внимание: {e}")
    finally:
        print(f"Программа выполнена, блок FINALLY выполняется всегда!")


the_func_of_varexc("i",2)
the_func_of_varexc(6,0)