from models import *
from views import *

class Battleship:
	def __init__(self):
		self.view = View()
		self.board = Gameboard()
		self.view.welcome()

	def player_one_initiate(self):
		player_one_name = self.view.first_player()
		self.player_one = Player(player_one_name)
		player_one_ship = self.view.select_ship()
		player_one_position = self.view.select_position()
		self.player_one.board.print_board()
		player_one_starting_pointer = self.view.starting_point_of_ship()
		self.player_one_ship = Ship(player_one_ship, player_one_position,player_one_starting_pointer)
		self.player_two_initiate()

	def place_ship_on_board(self):
		pass

	def player_two_initiate(self):
		player_two_name = self.view.second_player()
		self.player_two = Player(player_two_name)
		player_two_ship = self.view.select_ship()
		player_two_position = self.view.select_position()
		self.player_two.board.print_board()
		player_two_starting_pointer = self.view.starting_point_of_ship()
		self.player_two_ship = Ship(player_two_ship, player_two_position,player_two_starting_pointer)
		self.print_information()

battleship = Battleship()
battleship.player_one_initiate()
