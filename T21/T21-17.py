import re

 
#blacklist=["http://lol.com", '2']
#mployees_list = {"248.0.0.127": "Sasha"}
CONST_PATH_TO_FILE=''
blacklist = []
employees_list = {}

def solve(path_to_file, blacklist, employee_list):
    with open(path_to_file, "r", encoding="UTF-8") as data:
        data = data.read()
    ip_part = r"(?P<ip>(?:\d{1,3}[.]){3}\d{1,3})"
    http_part = r"(?P<h>http://[^ ]*[ ])"
    date_part = r"(?P<date>\d{2}.\d{2}.\d{4} \d{2}.\d{2}.\d{2})"
    full_exp = ip_part + ' ' + http_part + date_part
    data = re.finditer(full_exp, data)
    blacklist_by_ip = {}
    for i in employee_list.values():
        blacklist_by_ip[i] = 0
    for i in data:
        if i.group('h')[:-1] in blacklist:
            blacklist_by_ip[employee_list[i.group("ip")]] += 1
    blacklist_by_ip = sorted(blacklist_by_ip, key=lambda x: blacklist_by_ip[x], reverse=True)
    return blacklist_by_ip

if __name__ == '__main__':
    print("T21.17")
    print("Оскільки в умові не було специфікацій, то я зробив декілька припущень:")
    print("1: Чорний список - лист із заборониними сайтами, всі сайти у задачі - http")
    print("2: Список робітників - словар, де ключі - айпі, а Імена - значення")
    solve(CONST_PATH_TO_FILE, blacklist, employees_list)








