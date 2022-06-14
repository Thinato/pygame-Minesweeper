import math
import random
from tile import *

class Field:
	def __init__(self, size:tuple, difficulty=0):
		self.x, self.y = size
		self.text_size = 36
		self.text_offset = 10
		self.field = [[Label((x*self.text_size+self.text_offset,y*self.text_size+self.text_offset), ' ') for x in range(self.x)] for y in range(self.y)]
		self.bombs = 0
		self.place_bombs(difficulty/6 + 0.1)
		self.safes = (self.x * self.y) - self.bombs
		self.place_numbers()

	def __str__(self):
		res = ''
		for i in range(len(self.field)):
			res+='\n'
			for j in range(len(self.field[i])):
				res += str(self.field[i][j]) + ' | '
		return res

	def place_bombs(self, percentage):
		n = math.floor(percentage * (self.x*self.y))
		self.bombs = n
		while n > 0:
			x, y = random.randint(0, self.x-1), random.randint(0, self.y-1)
			if self.field[y][x] != '*':
				self.field[y][x] = Label((y*self.text_size+self.text_offset,x*self.text_size+self.text_offset), '*')
				n-=1
	def is_valid(self, pos):
		if pos[0] in range(self.x) and pos[1] in range(self.y):
			return True
		return False

	def is_validbomb(self, pos) -> bool:
		if pos[0] in range(self.x) and pos[1] in range(self.y) and self.field[pos[0]][pos[1]].text == '*':
			return True
		return False

	def place_numbers(self):
		for y in range(len(self.field)):
			for x in range(len(self.field)):
				count = 0
				if self.field[y][x].text == '*':
					continue
				if self.is_validbomb((y-1,x)):
					count+=1
				if self.is_validbomb((y-1,x+1)):
					count+=1
				if self.is_validbomb((y,x+1)):
					count+=1
				if self.is_validbomb((y+1,x+1)):
					count+=1
				if self.is_validbomb((y+1,x)):
					count+=1
				if self.is_validbomb((y+1,x-1)):
					count+=1
				if self.is_validbomb((y,x-1)):
					count+=1
				if self.is_validbomb((y-1,x-1)):
					count+=1
				if count > 0:
					self.field[y][x] = Label((y*self.text_size+self.text_offset,x*self.text_size+self.text_offset), str(count))



