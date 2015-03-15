from models import *
from views import *

class Battleship:
	def __init__(self):
		self.view = View()
		self.board = Gameboard()
		self.player = Player()
		self.view.welcome()

	def two_player_game(self):
		self.player_one_initiate()
		self.player_two_initiate()
		self.shots_fired()

	def player_one_initiate(self):
		player_one_name = self.view.first_player() #player 1 name
		self.player_one = Player(player_one_name) #instance of class Player

		player_one_ship = int(self.view.select_ship()) #player 1 ship choice (length)
		player_one_position = self.view.select_position() #player 1 vertical or horizontal

		self.player_one.board.seed_board()
		self.player_one.board.print_board() #prints the board

		player_one_starting_pointer = self.view.starting_point_of_ship().upper() #player 1 places the ship

		self.player_one_ship = Ship() #setting player one's ship
		self.player_one.ship_location = self.player_one_ship.create_ship_location(player_one_ship, player_one_position, player_one_starting_pointer)

	def player_two_initiate(self):
		player_two_name = self.view.second_player()
		self.player_two = Player(player_two_name)

		player_two_ship = int(self.view.select_ship())
		player_two_position = self.view.select_position()

		self.player_two.board.seed_board()
		self.player_two.board.print_board()

		player_two_starting_pointer = self.view.starting_point_of_ship().upper() #player 1 places the ship

		self.player_two_ship = Ship() #setting player two's ship
		self.player_two.ship_location = self.player_two_ship.create_ship_location(player_two_ship, player_two_position, player_two_starting_pointer)


	def shots_fired(self, player = None):
		current_player = self.player.switch_current_player()
		enemy_player = self.player.enemy_player(current_player)
		if current_player == 'player one':
			current_player = self.player_one
		else:
			current_player = self.player_two
		if enemy_player == 'player one':
			enemy_player = self.player_one
		else:
			enemy_player = self.player_two
		shot_fired_at = self.view.fire_shot(current_player.name)
		current_player.board = self.board.updated_board(shot_fired_at, current_player.board, (enemy_player.ship_location))




battleship = Battleship()
battleship.two_player_game()
