import re

def get_template(address, kvartira, pib, borg):
    ret_value = f"{address} {kvartira} \n\
Шановна(ий) {pib} \n\
Сума вашого боргу складає {borg}, \n\
Просимо сплатити борг протягом місяця. У іншому випадку,\n\
наданя послуг буде припинено"
    return ret_value




def solve(path, output_path):
    text = tmp
    add = r"((?:(?:адреса|адр[.]) [а-яА-Я0-9]* ))"
    kv = r"((?:кв. [0-9]* ))"
    tel = r"((?:(?:телефон|тел.) [0-9]* ))"
    return_value = ""
    with open(path, "r", encoding="UTF-8") as file:
        line = file.readline()
        while(line):
            try:
                a = re.findall(add, line, re.IGNORECASE)[0].replace('\n', '')
                telephone = re.findall(tel, line, re.IGNORECASE)[0].replace('\n', '')
                kvartira = re.findall(kv, line, re.IGNORECASE)
            except:
                line = file.readline()
                continue
            if kvartira:
                kvartira = kvartira[0]
                line = line.replace(kvartira, '').replace(a, '').replace(telephone, '')
            else:
                kvartira = ''
                line = line.replace(a, '').replace(telephone, '')
            borg = line.split(' ')[-1].replace('\n', '')
            pib = line.replace(borg, '').replace('\n', '')
            a = a.replace(a.split(' ')[0] + ' ', '')
            return_value += get_template(a, kvartira, pib, borg)
            return_value += '\n'
            line = file.readline()
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(return_value)




if __name__ == "__main__":
    path = input("Введіть шлях")
    solve(path, "outpuut.txt")
