import pickle

flowers = {'Roses':'red', 'Violets':'blue'}

with open('flowers.txt', 'wb') as f:
    pickle.dump(flowers, f)

with open('flowers.txt', 'rb') as f:
    new_flowers = pickle.load(f)


print(new_flowers)