from models import *
from views import *

class Battleship:
	def __init__(self):
		self.view = View()
		self.board = Gameboard()
		self.view.welcome()
		Battleship().attack_turn()

	def run(self):
		self.player_one_initialize()
		self.player_two_initialize()
		self.player_one_deploy()
		self.player_two_deploy()
		self.current = self.player_one
		self.next = self.player_two
		self.attack()

	def next_turn(self):
		swap = self.current
		self.current = self.next
		self.next = swap

	def player_one_initialize(self):
		player_one_name = self.view.first_player()
		self.view.show_open_sea(player_one_name)
		self.player_one = Player(player_one_name)
		self.player_one.board.print_board()

	def	player_one_deploy_ship(self):
		player_one_ship = self.view.select_ship()
		player_one_position = self.view.select_position()
		player_one_starting_pointer = self.view.starting_point_of_ship()
		self.player_one_ship = Ship(player_one_ship, player_one_position, player_one_starting_pointer)
		self.player_one_ship.place_bow(player_one_starting_pointer)

	def player_two_initialize(self):
		player_two_name = self.view.first_player()
		self.view.show_open_sea(player_two_name)
		self.player_two = Player(player_two_name)
		self.player_two.board.print_board()
		player_two_ship = self.view.select_ship()
		player_two_position = self.view.select_position()
		player_two_starting_pointer = self.view.starting_point_of_ship()
		self.player_two_ship = Ship(player_two_ship, player_two_position,player_two_starting_pointer)

	def	player_one_deploy_ship(self):
		player_one_ship = self.view.select_ship()
		player_one_position = self.view.select_position()
		player_one_starting_pointer = self.view.starting_point_of_ship()
		self.player_one_ship = Ship(player_one_ship, player_one_position, player_one_starting_pointer)
		self.player_one_ship.place_bow(player_one_starting_pointer)

	def attack_turn(self):
		# if player_one_ship == (sunk):   						#very much pseudocode
		# 	return self.views.game_over()
		# elif player_two_ship == (sunk):							#more psuedocode
		# 	return self.views.game_over()
		# else:
		attack_coords = self.views.attack_opponent()
		self.model.fire_missile(attack_coords)
