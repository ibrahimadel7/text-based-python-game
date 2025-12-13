
class Player:
    def __init__(self, health, potion, weapon, hunger,inventory):
        self.health = health
        self.potion = potion
        self.weapon = weapon
        self.hunger = hunger
        self.inventory = inventory

    def pickup_item(self, item):
        print(f"You picked up a {getattr(item, 'name', str(item))}")
        self.inventory.append(item)