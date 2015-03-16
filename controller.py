from models import *
from views import *
import time
import random

class Battleship:
	def __init__(self):
		self.view = View()
		self.board = Gameboard()
		self.player = Player()
		self.ship = Ship()
		self.view.welcome()

	def main_menu(self):
		choice = self.view.game_mode()
		if choice is '1':
			self.two_player_game()
		elif choice is '2':
			self.one_player_game()

	def one_player_game(self):
		self.player_one_initiate()
		self.create_hal()
		self.man_v_comp()

	def two_player_game(self):
		self.player_one_initiate()
		self.player_two_initiate()
		self.shots_fired()

	def create_hal(self):
		self.hal = Player('Hal')

		self.hal.board.seed_board()
		self.hal_ship = Ship()
		self.hal.ship_location = self.hal_ship.create_ship_location(random.randint(2,5), str(random.randint(1,2)), str(chr(random.randint(65,74))) + str(random.randint(1,10)))

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
		self.view.clear_screen()
		current_player = self.player.switch_current_player(player)
		enemy_player = self.player.enemy_player(current_player)
		if current_player == 'player one':
			actual_current_player = self.player_one
		else:
			actual_current_player = self.player_two
		if enemy_player == 'player one':
			actual_enemy_player = self.player_one
		else:
			actual_enemy_player = self.player_two
		actual_current_player.board.print_board()
		shot_fired_at = self.view.fire_shot(actual_current_player.name).upper()
		a_hit = self.board.hit_or_miss(shot_fired_at, actual_enemy_player.ship_location)
		actual_current_player.board = self.board.updated_board(shot_fired_at, actual_current_player.board, actual_enemy_player.ship_location)
		actual_enemy_player.ship_location = self.ship.update_enemy_boat(shot_fired_at,actual_enemy_player.ship_location)
		if a_hit is True:
			self.view.its_a_hit()
		else:
			self.view.its_a_miss()
		time.sleep(1)
		if len(actual_enemy_player.ship_location) == 0:
			return self.view.end_game(actual_current_player.name)
		self.shots_fired(current_player)

	def man_v_comp(self):
		print(self.hal.ship_location)
		self.player_one.board.print_board()
		shot_fired_at = self.view.fire_shot(self.player_one.name).upper()
		self.player_one.board = self.board.updated_board(shot_fired_at, self.player_one.board, self.hal.ship_location)
		a_hit = self.board.hit_or_miss(shot_fired_at, self.hal.ship_location)
		if a_hit is True:
			self.view.its_a_hit()
		else:
			self.view.its_a_miss()
		self.hal.ship_location = self.ship.update_enemy_boat(shot_fired_at, self.hal.ship_location)
		if len(self.hal.ship_location) == 0:
			return self.view.end_game(self.player_one.name)
		self.view.hal_is_choosing()
		time.sleep(2)
		self.hals_turn()

	def hals_turn(self):
		hal_chooses = self.hal.hals_next_guess(self.hal.board)
		self.hal.board = self.board.updated_board(hal_chooses, self.hal.board, self.player_one.ship_location)
		a_hit = self.board.hit_or_miss(hal_chooses, self.player_one.ship_location)
		if a_hit is True:
			self.hal.hit.append(hal_chooses)
		else:
			self.hal.miss.append(hal_chooses)
		self.player_one.ship_location = self.ship.update_enemy_boat(hal_chooses, self.player_one.ship_location)
		print (self.hal.hit)
		print(self.hal.miss)
		if len(self.player_one.ship_location) == 0:
			return self.view.end_game(self.hal.name)
		self.view.hals_board()
		self.hal.board.print_board()
		self.man_v_comp()


battleship = Battleship()
battleship.main_menu()
