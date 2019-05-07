import json

# JSON object
x = '[{"name": "Claus", "age": 23, "cpr": "7456732645"}, {"name": "Claus", "age": 23, "cpr": "7456732645"}]'


y = json.loads(x)

print(y)


x = [{'name': 'Claus', 'age': 23, 'cpr': '7456732645'}, {'name': 'Claus', 'age': 23, 'cpr': '7456732645'}]

y = json.dumps(x)

print(y)