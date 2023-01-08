from classes import *
from workdb import *

def main():
    lst = Listinizer(6, (10, 200))
    result0 = lst.get_list()
    result = lst.reduced()
    print(result, result0)


if __name__ == '__main__':
    main()
