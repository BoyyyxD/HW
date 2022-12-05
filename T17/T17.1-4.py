

def abs_wrapper(function):
    def wrapper(*args, **kwargs):
        res = function(*args, **kwargs)
        if not isinstance(res,  (int, float, complex)):
            print("Error, got non-Numeric value")
            return
        if res <= 0:
            return abs(res)
        return res
    return wrapper


@abs_wrapper
def return_input():
    print("Тест функціі декоратора 'модуль' ")
    return int(input("Введить чісло "))

def range_wrapper(lower, upper):
    def _my_wrapper(function):
        def __my_wrapper(*args, **kwargs):
            res = function(*args, **kwargs)
            if not isinstance(res,  (int, float, complex)):
                print("Error, got non-Numeric value")
                return
            if res < lower:
                print("Число менше ніж нижня межа")
                return lower
            if res > upper:
                print("Число більше ніж верхня межа")
                return upper
            return res
        return __my_wrapper
    return _my_wrapper

@range_wrapper(-2, 10)
def test_input_in_range():
    print("Тест функціі декоратора 'межі'")
    return int(input("Введить чісло "))

def keyword_wrapper(function):
    def _mywrapper(*args, **kwargs):
        assert(len(args) == len(kwargs))
        func = function(*args, **kwargs)
        return func
    return _mywrapper

@keyword_wrapper
def get_function_value(*args, **kwargs):
    print(args)
    sum = 1
    for (i, j) in zip(args, kwargs.values()):
        if j == 0:
            return
        sum *= (i + 1/j)
    return sum

def check_string_parameters(function):
    def _my_wrapper(*args, **kwargs):
        for i in args:
            assert(isinstance(i, str))
        for i in kwargs.values():
            assert(isinstance(i, str))
        return function(*args, **kwargs)
    return _my_wrapper

@check_string_parameters
def return_list_without_repetitions(*args, **kwargs):
    temp = set(args)
    temp.union(set(kwargs.values()))
    return list(temp)


if __name__ == '__main__':
    print("Задача Т17.1: ")
    print(return_input())
    print("Задача Т17.2: ")
    print(test_input_in_range())
    print("Задача Т17.3: ")
    print(get_function_value(1,2,3, a=2, b=3, c=4))
    print("Задача Т17.4: ")
    print(return_list_without_repetitions("abcd", "abcd", "b", a="abcd", b="d", c=3))

    