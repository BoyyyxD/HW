import os
from datetime import date, time, datetime
import tarfile

def find_differences(first_path, second_path, output_file):
    assert(os.path.exists(first_path))
    assert(os.path.exists(second_path))
    assert(os.path.isdir(first_path))
    assert(os.path.isdir(second_path))
    
    files_in_first_dir = [i for i in os.listdir(first_path)  
    if os.path.isfile(os.path.join(first_path, i))]
    
    files_in_second_dir = [i for i in os.listdir(second_path) 
    if os.path.isfile(os.path.join(second_path, i))]
    
    diff1, diff2 = [], []
    for i in files_in_first_dir:
        if i not in files_in_second_dir:
            diff1.append(i)
    for i in files_in_second_dir:
        if i not in files_in_first_dir:
            diff2.append(i)
    diff1 = "Файли в першій, але не в другій: \n" + '\n'.join(diff1)
    diff2 = "Файли в другій, але не в першій: \n" + '\n'.join(diff2)
    ans = diff1 + "\n" + diff2
    with open(output_file, 'w', encoding="utf-8") as file:
        file.write(ans)
    return

def find_similarities(first_path, second_path, output_file):
    assert(os.path.exists(first_path))
    assert(os.path.exists(second_path))
    assert(os.path.isdir(first_path))
    assert(os.path.isdir(second_path))
    
    files_in_first_dir = [i for i in os.listdir(first_path)  
    if os.path.isfile(os.path.join(first_path, i))]
    
    files_in_second_dir = [i for i in os.listdir(second_path) 
    if os.path.isfile(os.path.join(second_path, i))]
    
    sim = []
    for i in files_in_first_dir:
        if i in files_in_second_dir:
            sim.append(i)
    ans = ""
    for i in sim:
        time1 = os.path.getctime(os.path.join(first_path, i))
        time2 = os.path.getctime(os.path.join(second_path, i))
        if time1 > time2:
            ans += i + " у " + first_path + " Було створено пізніше на " + str(time1-time2) + "секунд \n"
        if time1 < time2:
            ans += i + " у " + second_path + " Було створено пізніше на " + str(time2-time1) + "секунд \n"

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(ans)

def sys_journal(path, archieve_name):
    assert(os.path.exists(path))
    assert(os.path.isdir(path))
    curr_time = date.today()
    curr_time = datetime.strptime(str(curr_time), '%Y-%m-%d').timestamp()
    files = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path, i))]
    tmp = []
    for i in files:
        creation_time = os.path.getctime(os.path.join(path, i))
        normal_time =  datetime.fromtimestamp(creation_time).strftime("%d-%m-%Y")
        if normal_time in i:
            tmp.append(i)
    tf = tarfile.open(archieve_name + '.tar.gz','w:gz')
    for i in tmp:
        tf.add(os.path.join(path, i))
    tf.close()



if __name__ == "__main__":
    find_differences("/root/nnrmu/prog/HW/T22/test1", "/root/nnrmu/prog/HW/T22/test2", "output.txt")
    find_similarities("/root/nnrmu/prog/HW/T22/test1", "/root/nnrmu/prog/HW/T22/test2", "output2.txt")
    sys_journal("/root/nnrmu/prog/HW/T22/test1", "lol")
