class View:
	def __init__(self):
		pass

	def game_mode(self):
		game_type = input('''What game mode would you like to play?
		press 1 for 2 player mode
		press 2 to test your wits against the computer!
		Selection: ''')
		return game_type

	def welcome(self):
		print ("Welcome to Battleship!!!!!  Hope you brought a life-jacket?")

	def first_player(self):
		player_one = input('Enter player 1 name: ')
		return player_one

	def second_player(self):
		player_two = input("Enter Player 2 name:  ")
		return player_two

	def select_ship(self):
		ship_choice = input('''Let's place your ship! What would you like to use?
		Please press 5 for Aircraft carrier(5 slots)
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

	def fire_shot(self, current_player):
		shoot = input(current_player + ''' make your move!
		Please select a coordinate to shoot
		Selection: ''')
		return shoot

	def its_a_hit(self):
		print ("That's a hit!!")

	def its_a_miss(self):
		print("You've missed the enemy ship..")

	def end_game(self,winning_player):
		print('''Congratulations, ''' + winning_player + '''. You win!!!''')

	def clear_screen(self):
		print(chr(27) + "[2J")

	def hal_is_choosing(self):
		print("Please wait while Hal searches for your ship...")
