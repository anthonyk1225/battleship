import sqlite3

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
		# self.board[3][7] = ' X'
		# self.board[3][2] = ' O'
		for line in self.board:
			print (('  ').join(line))
			print()

class Player:
	def __init__(self, name, board = None):
		self.name = name
		self.board = Gameboard()

	def fire_missle(self, coords):
		self.coords = coords
		if self.coords = Ship.start_coords or self.coords = ship.end_coords
			return True



class Ship:
	def __init__(self, length, starting_point, position):
		self.length = length
		self.starting_point = starting_point
		self.position = position

	def place_ship(self, start_coords, end_coords):
		self.start_cords = start_coords
		self.end_coords = end_cords

board = Gameboard()
board.seed_board()
(board.print_board())
