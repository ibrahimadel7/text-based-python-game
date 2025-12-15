
# If running as a script, use relative imports
import sys
import os
import random
sys.path.append(os.path.join(os.path.dirname(__file__), 'game elements'))
from game_elements.characters.player import Player
from game_elements.items.item import Item
from game_elements.items.food import Food
from game_elements.items.weapons import Weapon
from map import Map

def main():
	inventory=[]
	apple = Food("Apple", 5)
	bread=Food("bread",10)
	soup=Food("soup",20)
	sword = Weapon("Sword", 10, False)
	stick=Weapon("stick",1,False)
	potion = Item("Health Potion", "potion", True)
	player = Player(health=100, potion=potion, weapon=None, hunger=100,inventory=inventory,pos_x=0,pos_y=0)
	foods=[apple,bread,soup]
	weapons=[sword,stick]
	all_items = foods + weapons + [potion]
	map_instance=Map()
	game_map=map_instance.generate_map(5,5)
	print(game_map)
	steps=20
	while True:
		found_item = generate_item(all_items)

		print(f"You found {found_item.name}")

		print(f"""\nSteps remaining to win : {steps}
			player states:
				your health: {player.health}
				your food: {player.hunger}
			Your position: ({player.pos_x}, {player.pos_y})
			Current tile: {game_map[player.pos_x][player.pos_y]}
		""")

		player_choice = input(
			"Choose what you want to do:\n"
			"move forward (f)\n"
			"move left (l)\n"
			"move right (r)\n"
			"pick up item (p) \n"
			"there is no way back\n> "
		).lower()



			
			# Determine intended move
		next_x, next_y = player.pos_x, player.pos_y
		if player_choice == "f":
			next_x += 1
			steps-=1
		elif player_choice == "l":
			next_y -= 1
			steps-=1
		elif player_choice == "r":
			next_y += 1
			steps-=1
		# Check map boundaries
		if 0 <= next_x < len(game_map) and 0 <= next_y < len(game_map[0]):
			tile = game_map[next_x][next_y]
			# Check if the tile is a wall (True) or not (False) using the obstacles dictionary
			if map_instance.obstacles[tile]:
				print("\n\tYou hit a wall!\n")
			else:
				# Only update player position if not a wall, for any valid move
				if player_choice in ("f", "l", "r"):
					player.pos_x, player.pos_y = next_x, next_y
				
		else:
			print("\n\tYou can't move outside the map!\n")

		#player.hunger -= 20
			# Show updated position and tile after move
		print(f"\nAfter move: Position: ({player.pos_x}, {player.pos_y}), Current tile: {game_map[player.pos_x][player.pos_y]}\n")





		if steps == 0:
			choose=input("You reached the end. You win! choose (r) to play again or anykey to quite: ")
			if(choose=="r"):
				player.health=100
				player.hunger=100
				steps=20
				continue
			else:
				break

		if player.hunger<=0 or player.health==0:
			choose=input("rip you are DEAD ! choose (r) to play again or anykey to quite:	")
			if(choose=="r"):
				player.health=100
				player.hunger=100
				steps=20
				continue
			else:
				break



		

		# Test inventory
def generate_item(items):
	rando = random.choice(items)
	return rando



if __name__ == "__main__":
	main()
