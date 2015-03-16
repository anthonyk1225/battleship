import random

board = []

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
board = arr

class HAL:
    def __init__(self, board=None):
        pass

    def HAL_guess(self):
        guess_x = random.randint(1, 10)
        guess_y = random.randint(65, 75)
        return chr(guess_y), guess_x

hal = HAL()
print(hal.HAL_guess())
