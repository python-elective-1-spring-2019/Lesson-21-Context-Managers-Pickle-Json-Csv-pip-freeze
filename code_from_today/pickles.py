import pickle

flowers = {'roses': 'red', 'violets': 'blue'}

with open('flowers.pickle', 'wb') as f:
    pickle.dump(flowers, f)

with open('flowers.pickle', 'rb') as f:
    new_flowers = pickle.load(f)
    
print(new_flowers)
