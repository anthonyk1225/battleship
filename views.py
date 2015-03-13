class View:
	def __init__(self):
		pass

	def welcome(self):
		print ("Welcome to Battleship!!!!!  Hope you brought a life-jacket?")

	def first_player(self):
		player_one = input('Enter player 1 name: ')
		return player_one

	def second_player(self):
		player_two = input("Enter Player 2 name:  ")
		return player_two

	def show_open_sea(self, name):
		print("Okay, {}, let's deploy your armada!  Here is your sea to hide in.".format(name))

	def select_ship(self):
		ship_choice = input('''Now, pick your ship.
		5 for Aircraft carrier(5 slots)
		4 for Battleship (4 slots)
		3 for Submarine (3 slots)
		2 for Patrol Boat (2 slots)
		Selection: ''')
		return ship_choice

	def select_position(self):
		position = input('''Would you like to place your ship vertical, or horizontal?
		Press 1 for Vertical
		Press 2 for Horizontal
		Selection: ''')
		return position

	def starting_point_of_ship(self):
		starting_point = input('''Please select a coordinate to place your ship
		Selection: ''')
		return starting_point
