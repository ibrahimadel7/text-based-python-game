
# If running as a script, use relative imports
import sys
import os
import random
sys.path.append(os.path.join(os.path.dirname(__file__), 'game elements'))
from game_elements.characters.player import Player
from game_elements.items.item import Item
from game_elements.items.food import Food
from game_elements.items.weapons import Weapon

def main():
	inventory=[]
	apple = Food("Apple", 5)
	bread=Food("bread",10)
	soup=Food("soup",20)
	sword = Weapon("Sword", 10, False)
	stick=Weapon("stick",1,False)
	potion = Item("Health Potion", "potion", True)
	player = Player(health=100, potion=potion, weapon=None, hunger=100,inventory=inventory)
	foods=[apple,bread,soup]
	weapons=[sword,stick]
	all_items = foods + weapons + [potion]
	steps=20
	valid_moves = ['f', 'l', 'r']
	print("hello welcome to the the text based game")
	while True:
		
		
		
		print(f"""\nSteps remaining to win : {steps}\n
		 player states:
			your health: {player.health}
			your food: {player.hunger}
		""")
		
		player_choice = input(
			"Choose what you want to do:\n"
			"move forward (f)\n"
			"move left (l)\n"
			"move right (r)\n"
			"pick up item (p) \n"
			"there is no way back\n> "
		).lower()

		if player_choice in valid_moves:
			player.hunger -=5
			steps -= 1
		else:
			print("invalid chioce try moving again")

		


		found_item = generate_item(all_items)

		print(f"You moved and found {found_item.name}")

		if steps == 0:
			print("You reached the end. You win!")
			break



		

		# Test inventory
def generate_item(items):
	rando = random.choice(items)
	return rando



if __name__ == "__main__":
	main()
