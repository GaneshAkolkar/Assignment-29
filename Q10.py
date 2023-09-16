import pickle

with open('bookfile.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print(loaded_data)
