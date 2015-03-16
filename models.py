import sqlite3
import random

class Gameboard:
	def __init__(self):
		self.board = []

	def seed_board(self):
		arr = []
		for y in range(11):
			lst = []
			letter = chr(64 + y)
			for x in range(11):
				if x * y > 0:
					lst.append(" ~")
				elif x == 0 and y == 0:
					lst.append('')
				elif x == 0:
					lst.append(letter)
				elif y == 0:
					lst.append(" " + str(y+x))
			arr.append(lst)
		self.board = arr
		return self.board

	def print_board(self):
		for line in self.board:
			print (('  ').join(line))
			print()

	def hit_or_miss(self, player_guess, enemy_boat_location):
		if player_guess in enemy_boat_location:
			return True

	def updated_board(self, player_guess, player_board, enemy_boat_location):
		letter = int(ord(player_guess[0])) - 64
		if player_guess in enemy_boat_location:
			player_board.board[letter][int(player_guess[1:3])] = ' O'
		else:
			player_board.board[letter][int(player_guess[1:3])] = ' X'
		return player_board

class Player:
	def __init__(self, name=None, board = None, ship_location=None):
		self.name = name
		self.ship_location = ship_location
		self.board = Gameboard()

	def switch_current_player(self, player=None):
		if player == None or player == 'player two':
			return 'player one'
		return 'player two'

	def enemy_player(self, current_player):
		if current_player == 'player one':
			return 'player two'
		return 'player one'

	def hals_next_guess(self, hals_board):
		y_coord = random.randint(65,74)
		x_coord = random.randint(1,10)
		return chr(y_coord) + str(x_coord)

class Ship:
	def __init__(self):
		pass

	def create_ship_location(self, length, position, starting_point,):
		letter = ord(starting_point[0])
		ship_location = []
		for i in range(length):
			new_letter = chr(letter + i)
			if position == '1': #vertical
				ship_location.append(new_letter + starting_point[1:3])
			elif position == '2': #horizontal
				ship_location.append(starting_point[0] + str(int(starting_point[1:3]) + i))
		return ship_location

	def update_enemy_boat(self,player_guess,enemy_boat_location):
		if player_guess in enemy_boat_location:
			destroyed = enemy_boat_location.index(player_guess)
			enemy_boat_location.pop(destroyed)
			return enemy_boat_location
		return enemy_boat_location
