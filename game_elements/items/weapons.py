from game_elements.items.item import Item
class Weapon(Item):
    def __init__(self, name, damage, posion, exists=True):
        super().__init__(name, "weapon", exists)
        self.damage = damage

    def __str__(self):
        return f"Weapon: {self.name} (Damage: {self.damage})"