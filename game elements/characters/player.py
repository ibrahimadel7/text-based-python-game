from inventory import inventory

class Player:
    def __init__(self, health, potion, weapon, food, inventory):
        self.health = health
        self.potion = potion
        self.weapon = weapon
        self.food = food
        self.inventory = inventory

    def pickupitem(self, item):
        print(f"You picked up a {item}")
        # If inventory is a dict, add or increment item
        item_name = getattr(item, 'name', str(item))
        if item_name in self.inventory:
            self.inventory[item_name] += 1
        else:
            self.inventory[item_name] = 1