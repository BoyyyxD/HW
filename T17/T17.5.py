

def check_arguments_type(type):
    def __my_wrapper(function):
        def _my_wrapper(*args, **kwargs):
            for i in args:
                assert(isinstance(i, type))
            for i in kwargs.values():
                assert(isinstance(i, type))
            return function(*args, **kwargs)
        return _my_wrapper
    return __my_wrapper


@check_arguments_type(int)
def find_average_value(*args, **kwargs):
    tmp = list(args)
    for i in kwargs.values():
        tmp.append(i)
    assert(tmp) 
    return sum(tmp)/len(tmp)


if __name__ == "__main__":
    print("Задача Т17.5, для int:")
    print(find_average_value(2, 3, 4, lol=2, b=6))

