class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

my_book = Book("The Alchemist", "Paulo Coelho", 1988)

# Method A: Using vars()
dict_keys = vars(my_book).keys()
print(type(dict_keys))

# print all the attributes of my_book using map and lambda
# output: ['title', 'author', 'year']
# print(list(map(lambda x: x, dict_keys)))