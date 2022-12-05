
def check_arguments(function):
    def _wrapper(*args, **kwargs):
        assert(not args)
        # Тут мала б бути перевірка, що ключі-рядки,
        # Але я не розумію як вони можуть бути не рядками
        for i in kwargs.values():
            assert isinstance(i, int) and i >= 0
        return function(*args, **kwargs)
    return _wrapper


@check_arguments
def most_common_word(*args, **kwargs):
    tmp = max(kwargs, key=lambda x: kwargs[x])
    print(f"Найбільше входжень: {tmp}")
    return tmp


if __name__ == "__main__":
    print("Задача Т17.8: ")
    most_common_word(abcd=2, lol=3, tmp=4, a=5, d=2, c=3)
