import re

CONST_SMILE_SEQUENCE = "<Smile>"
CONST_PATH_TO_FILE = ''

def solve(path_to_file, smile):
    with open(path_to_file, 'r', encoding="UTF-8") as data:
        data = data.read()
    num_of_smiles = data.count(smile)
    exp = r"([^a-zA-Z']*)([a-zA-Z']*)([^a-zA-Z'])"
    data = [i.group(2) for i in re.finditer(exp, data)]
    if not data or not num_of_smiles or num_of_smiles-len(data) == 0:
        print("Щось пішло не так, програма знайшла 0 слів або 0 смайлів")
        return
    print(f"Індекс = {num_of_smiles/(len(data) - num_of_smiles)}\n")
    return

if __name__ == '__main__':
    print("Задача T21.9")
    print("Знову ж таки, оскільки задача не має чіткої умови, я ввів декілька умовностей:")
    print("Весь текст написаний англійською мовою. За слово, вважается будь-яка послідовність")
    print("Англійських літер, яка в собі може мати або не мати апостроф")
    print("Смайлик - фіксоване слово, яке можна змінити вверху програми")
    solve(CONST_PATH_TO_FILE, CONST_SMILE_SEQUENCE)




