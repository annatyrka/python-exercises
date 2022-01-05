import shelve

shelf_file = shelve.open('my_data')
cats = ['Ciapek', 'Pooka', 'Simon']
shelf_file['cats'] = cats
shelf_file.close()

shelf_file = shelve.open('my_data')
print(list(shelf_file.values()))
