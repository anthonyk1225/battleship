import sqlite3

class Gameboard:
	def __init__(self):
		self.board = []

	def print_board(self):
		for x in range(10):
			self.board.append(" ~ "*10)
		print('   ', '    '.join([(str(x) + " ") for x in range(1,11)]))
		x = 65
		for row in self.board:
			print(chr(x), ' '.join(row))
			print()
			x+=1

class Player:
	def __init__(self, name, board = None):
		self.name = name
		self.board = Gameboard()

class Ship:
	def __init__(self, length, starting_point, position):
		self.length = length
		self.starting_point = starting_point
		self.position = position
