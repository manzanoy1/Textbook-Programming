#Yanira Manzano
#22/11/2019

from Person import Person

class Textbooks():
    def __init__(self, title, first, last, age, edition, ISBN, publisher, year, inventory, price):
        self.title = title
        self.author = Person(first, last, age)
        self.edition = edition
        self.ISBN = ISBN
        self.publisher = publisher
        self.year = year
        self.inventory = inventory
        self.price = price

    def add_to_inventory(self, qty):
        self.inventory = self.inventory + qty
