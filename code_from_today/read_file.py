
def reading_file():
    f = open('_zen_of_python.txt')
    for textfile in f:
        print(f.read())
    
    f.close()


def better_way_of_reading_file():
    try:
        f = open('_zen_of_python.txt')
        for textline in f:
            print(f.read())
    except:
        print('Can not read file.')
    finally:            
        f.close()


def context_manager():
    with open('_zen_of_python.txt') as f:
        print(f.read())

quotes = ['The sun will keep on shining', 'Me too', 'Roses are red, violets are blue, flowers are beautiful, and so are you.']

def write_to_file_1():

    with open('quotes.txt', 'w') as f:
        for quote in quotes:
            f.write(quote)

def write_to_file_2():
    with open('quotes.txt', 'w') as f:
        for quote in quotes:
            print(quote, file=f)
