import pickle

book_data = {
    "Book1": 20.99,
    "Book2": 15.50,
    "Book3": 12.75,
}

with open('bookfile.pkl', 'wb') as file:
    pickle.dump(book_data, file)
