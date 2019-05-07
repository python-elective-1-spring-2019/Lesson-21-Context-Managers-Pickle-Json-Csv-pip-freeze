def read_file():
    f = open('python_zen.txt')
    print(f.read())
    f.close()

def read_better_way():
    try:
        f = open('python_zen.py')
        print(f.read())

    except:
        print('file does no exist!')

    finally:
        f.close()


def read_even_better():

    with open('python_zen.txt') as f:
        print(f.read())

    





