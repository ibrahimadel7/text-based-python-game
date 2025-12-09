from item import Item

class Food(Item):
    def __init__(self, name, amount):
        super().__init__(name, "Food")
        self.amount = amount