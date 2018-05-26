
def print_books(store):
    for shelf in store.keys():
        for cat in store[shelf].keys():
            print(store[shelf][cat])


bookstore = {
    "New Arrivals": {
        "COOKING": ["Everyday Italian", "Giada De Laurentiis", "2005", "30.00"],
        "CHILDREN": ["Harry Potter", "J K. Rowling", "2005", "29.99"],
        "WEB": ["Learning XML", "Erik T. Ray", "2003", "39.95"]
    }
}

print_books(bookstore)
