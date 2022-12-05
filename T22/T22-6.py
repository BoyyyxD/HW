import os
from datetime import date, time, datetime

def check_file_size(const_part, f, size):
    try:
        num_of_bytes=os.fstat(f).st_size

        if num_of_bytes <= size:
            return f
        os.close(f)

        curr_time = str(date.today())
        f = os.open(curr_time + const_part, os.O_RDWR|os.O_CREAT|os.O_APPEND)
        return f
    except:
        raise AssertionError
    



if __name__ == "__main__":
    print("Задача T22.6: ")
    with open("output2.txt", "r", encoding="utf-8") as file:
        text = file.readline()
        fd = os.open( "output.txt", os.O_RDWR|os.O_APPEND)

        max_size = 20
        while(text):
            fd = check_file_size("put.txt", fd, max_size)
            os.write(fd, str.encode(text))
            text = file.readline()

        os.close(fd)

