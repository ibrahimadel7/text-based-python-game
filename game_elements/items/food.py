from game_elements.items.item import Item

class Food(Item):
    def __init__(self, name, amount, exists=True):
        super().__init__(name, "Food", exists)
        self.amount = amount

    def __str__(self):
        return f"Food: {self.name} (Amount: {self.amount})"