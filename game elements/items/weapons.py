from item import Item
class Weapon(Item):
  def __init__(self, name, damage,posion):
    super().__init__(name, "weapon") # Calls the item class's __init__
    self.damage = damage