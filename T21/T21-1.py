CONST_PATH_FO_FIRST_FILE = ""
CONST_PATH_TO_SECOND_FILE = ""
CONST_PATH_TO_THIRD_FILE = ""
CONST_PATH_TO_FOURTH_FILE = ""



tmp = "12.12.2004 1004-12-02. 1004-02-02. 8999/12/12"

import re
from datetime import date

def name_of_output_file(string):
    return string.replace('.', '_output.')



def to_normal(form):
    if(type(form) != str):
        form = form.group(0)
    form = re.sub(r"\d{1}[.]|\d{2}[.]", lambda x: "0"+x.group(0) if x.group(0)[1] == "." else x.group(), form)
    return form

def slash_to_normal(form):
    form = form.group(0)
    form = form.replace("/", '.')
    form = '.'.join(form.split('.')[::-1])
    form = to_normal(form)
    return form

# T21.1 
def solve_first(path_to_file):
    pattern_slash = r"\d{4}[/]\d{1,2}[/]\d{1,2}"
    pattern = r"\d{1,2}[.]\d{1,2}[.]\d{4}"
    with open(path_to_file, "r", encoding="UTF-8") as file:
        file = file.read()
    file = re.sub(pattern_slash, slash_to_normal, file)
    file = re.sub(pattern, to_normal, file)
    with open(name_of_output_file(path_to_file), "w", encoding="utf-8") as out:
        out.write(file)


# T21.2
def solve_second(path_to_file):
    expr = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"
    with open(path_to_file, "r", encoding="UTF-8") as file:
        file = file.read()
    splitted = re.findall(expr, file)
    with open(name_of_output_file(path_to_file), "w", encoding="utf-8") as out:
        out.write(file)

# T21.4
def solve_third(path_to_file):
    d = date.today().strftime("%d.%m.%Y")
    expr = r"\d{2}[.]\d{2}[.]\d{4}"
    with open(path_to_file, "r", encoding="UTF-8") as file:
        file = file.read()
    file = file.replace("__.__.____", d)
    file = re.findall(expr,  file)
    with open(name_of_output_file(path_to_file), "w", encoding="utf-8") as out:
        out.write(file)

# T21.5
def solve_fourth(path_to_file, mode='.'):
    dot_format = r"(?P<d>\d{2}).(?P<m>\d{2}).(?P<y>\d{4})"
    other_format = r"(?P<y>\d{4})[-|/](?P<m>\d{2})[-|/](?P<d>\d{2})"
    with open(path_to_file, "r", encoding="UTF-8") as file:
        file = file.read()
    def _change(match):
        d = match.group('d')
        m = match.group('m')
        y = match.group('y')
        if mode == '.':
            return '.'.join([d, m, y])
        if mode == '-':
            return '-'.join([y, m, d])
        if mode == '/':
            return '/'.join([y, m, d])
        return "wrong_format"
    file = re.sub(dot_format, _change, file)
    file = re.sub(other_format, _change, file)
    with open(name_of_output_file(path_to_file), "w", encoding="utf-8") as out:
        out.write(file)

if __name__ == "__main__":
    print("Путь к файлу к задаче записан в самом вверху программы, пожалуйста, измините его")
    print("Ответ для задачи записан в `имя исходного файла-output`")
    solve_first(CONST_PATH_FO_FIRST_FILE)

    solve_second(CONST_PATH_TO_SECOND_FILE)

    solve_third(CONST_PATH_TO_THIRD_FILE)
    mode = input("Введите шаблон для 21.5")
    solve_fourth(CONST_PATH_TO_THIRD_FILE)
    
