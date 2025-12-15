
class Player:
    def __init__(self, health, potion, weapon, hunger,inventory,pos_x,pos_y):
        self.health = health
        self.potion = potion
        self.weapon = weapon
        self.hunger = hunger
        self.inventory = inventory
        self.pos_x=pos_x
        self.pos_y=pos_y

    def pickup_item(self, item):
        print(f"You picked up a {getattr(item, 'name', str(item))}")
        self.inventory.append(item)
    def move_forward(self):
        self.pos_x += 1
    def move_right(self):
        self.pos_y += 1
    def move_left(self):
        self.pos_y -= 1