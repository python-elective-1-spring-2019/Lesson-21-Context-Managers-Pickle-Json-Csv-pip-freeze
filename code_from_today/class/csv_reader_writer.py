import csv

with open('cities.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ',')
    count = 1
    for row in csv_reader:
        if count == 1:
            print('Headline', row)
        else:
            print(row)
        
