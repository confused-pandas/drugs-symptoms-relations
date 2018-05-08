from multiprocessing import Process
from multiprocessing import freeze_support
import re

def find():
    f = open('./res/database/omim/omimtest.txt','r').readlines()
    for line in f:
        word = line.rstrip()
        f = re.search(r'^*FIELD*', word)
        field = f.group(1)
        print(field)

if __name__ == '__main__':
    freeze_support()
    p = Process(target=find())
    p.start()

find()