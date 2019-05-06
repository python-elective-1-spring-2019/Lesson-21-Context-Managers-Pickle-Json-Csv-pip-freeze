# Lesson 21: Context Managers, Pickle, Json, Csv, pip freeze
> Agenda 07-05-2019



## Toady
* Context Managers





## Context Managers

````python

	# reading a file

	f = open('testfiles/bohr.txt')
		for textfile in f:
    			print(f.read())
	f.close()
````

````python

	# a better way of reading a file

	try:
    		f = open('testfiles/bohr.txt')
    		for textline in f:
      		  	print(f.read())
	except:
    		print('Can not read file.')
	finally:
    		f.close()
````

````python

	# using a context manager - even better

	with open('testfiles/bohr.txt') as f:
    		print(f.read())

````

`````python

quotes = ['The sun will keep on shining', 'Me too', 'Roses are red, violets are blue, flowers are beautiful, and so are you.']

def write_to_file_1():

    with open('quotes.txt', 'w') as f:
        for quote in quotes:
            f.write(quote)

def write_to_file_2():
    with open('quotes.txt', 'w') as f:
        for quote in quotes:
            print(quote, file=f)

````

## Your own context manager

````python
class my_file_reader():
    def __init__(self, file_path):
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path)
        return self

    def __exit__(self, type, val, tb):
        self.__file_object.close()

    # Additional methods implemented below  

````

## Pickles

````python

import pickle

flowers = {'roses': 'red', 'violets': 'blue'}

with open('flowers.pickle', 'wb') as f:
    pickle.dump(flowers, f)

with open('flowers.pickle', 'rb') as f:
    new_flowers = pickle.load(f)
    
print(new_flowers)

````

## JSON

````python

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)


########## 

import json

# a Python object (dict):

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
	
````

## CSV files




## Exercise: 

````

1. Get a JSON representation of your own github account. 
2. Serialize the json object and save to a file.
3. Deserialize the date and save it to a CSV file.
4. try to open the file in excell og google spreadsheet

````

## Pip Freeze

````
python -m venv tutorial-env
source tutorial-env/bin/activate

# win
source tutorial-env/Scripts/activate

````


````
pip install simple-colors
pip list

pip freeze > requirements.txt

````

## Exercise pip install





























