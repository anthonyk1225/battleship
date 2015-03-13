from models import *
from views import *

class Battleship:
	def __init__(self):
		self.view = View()
		self.board = Gameboard()
		self.view.welcome()

	def run(self):
		self.player_one_initialize()
		self.player_two_initialize()

	def player_one_initialize(self):
		player_one_name = self.view.first_player()
		self.view.show_open_sea(player_one_name)
		self.player_one = Player(player_one_name)
		self.player_one.board.print_board()
		player_one_ship = self.view.select_ship()
		player_one_position = self.view.select_position()
		player_one_starting_pointer = self.view.starting_point_of_ship()
		self.player_one_ship = Ship(player_one_ship, player_one_position,player_one_starting_pointer)

	def place_ship_on_board(self):
		pass

	def player_two_initialize(self):
		player_two_name = self.view.first_player()
		self.view.show_open_sea(player_two_name)
		self.player_two = Player(player_two_name)
		self.player_two.board.print_board()
		player_two_ship = self.view.select_ship()
		player_two_position = self.view.select_position()
		player_two_starting_pointer = self.view.starting_point_of_ship()
		self.player_two_ship = Ship(player_two_ship, player_two_position,player_two_starting_pointer)

Battleship().run()
