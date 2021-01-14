class mybooks:
    def __init__(self, name):
        self.name = name
        print("{} is my book".format(self.name))

    def __del__(self):
        print("{} removed from stock. ID: {}".format(self.name, id(self)))


def test_scope():
    book1 = mybooks("Jack and the beanstalk")

test_scope()

book2 = mybooks("Charlie and the chocolate factory")
del book2

book3 = mybooks("Tom and Jerry")

# print("My first book location is id: {}".format(id(book1)))
# print("My Second book location is id: {}".format(id(book2)))
