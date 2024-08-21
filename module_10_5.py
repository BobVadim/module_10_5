
from multiprocessing import Pool
from datetime import datetime


filenames = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as f:
        data = f.readline()
        while data:
            all_data.append(data)
            data = f.readline()


# start = datetime.now()
# read_info(filenames[0])
# read_info(filenames[1])
# read_info(filenames[2])
# read_info(filenames[3])
# finish = datetime.now()
# print(finish - start)

if __name__ == '__main__':
    start = datetime.now()
    with Pool(processes=3):
        Pool(processes=3).map(read_info, filenames)
    finish = datetime.now()
    print(finish - start)


