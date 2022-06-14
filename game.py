import pygame as pg
from utils.colors import *
from field import *
from tile import *
import os, sys
from win_screen import *


class Game:
	def __init__(self):
		pg.init()
		self.WIDTH, self.HEIGHT = 577, 583
		self.SCREEN = pg.display.set_mode((self.WIDTH, self.HEIGHT))
		self.FPS = 60
		self.CLOCK = pg.time.Clock()
		self.running = True
		self.field_size = 16
		self.field = Field((self.field_size,self.field_size),0)
		self.buttons = [[None for i in range(self.field_size)] for j in range(self.field_size)]
		self.create_buttons()
		self.win_screen = WinScreen(self)
		self.revealed = 0

	def draw(self, screen):
		screen.fill(GREY)
		self.check_win(screen)

		mousepos = pg.mouse.get_pos()
		for i in range(len(self.field.field)):
			pg.draw.line(screen, GREY_2, (0, (i*36)+42), (self.WIDTH, (i*36)+42))
			for j in range(len(self.field.field[i])):
				self.field.field[i][j].draw(screen)
				pg.draw.line(screen, GREY_2, ((j*36)+36,0), ((j*36)+36, self.HEIGHT))
				if self.buttons[i][j] != None:
					self.buttons[i][j].draw(screen, mousepos)



		pg.display.flip()

	def check_win(self, screen):
		while self.revealed >= self.field.safes:
			print('you win')
			self.win_screen.draw(screen)

	def handle_event(self, event):
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()
		elif event.type == pg.MOUSEBUTTONDOWN:
			if event.button == 1:
				for i in range(len(self.buttons)):
					for j in range(len(self.buttons[i])):
						if self.buttons[i][j] != None and self.buttons[i][j].selected:
							self.reveal((j,i))
			elif event.button == 3:
				for i in range(len(self.buttons)):
					for j in range(len(self.buttons[i])):
						if self.buttons[i][j] != None and self.buttons[i][j].selected:
							self.buttons[i][j].flag = True if not self.buttons[i][j].flag else False
	
	def reveal(self, pos, recursion=False):
		x,y=pos
		if self.field.field[y][x].text == '*' and not recursion and not self.buttons[y][x].flag:
			print('boom!')
		if self.buttons[y][x] != None and not self.buttons[y][x].flag:
			self.buttons[y][x] = None
			self.revealed += 1
		if self.field.field[y][x].text == ' ':
			if self.field.is_valid((x+1,y))   and self.field.field[y][x+1].text != '*'   and self.buttons[y][x+1]   != None and not self.buttons[y][x+1].flag: 
				self.reveal((x+1,y), True)
			if self.field.is_valid((x-1,y))   and self.field.field[y][x-1].text != '*'   and self.buttons[y][x-1]   != None and not self.buttons[y][x-1].flag: 
				self.reveal((x-1,y), True)
			if self.field.is_valid((x,y+1))   and self.field.field[y+1][x].text != '*'   and self.buttons[y+1][x]   != None and not self.buttons[y+1][x].flag: 
				self.reveal((x,y+1), True)
			if self.field.is_valid((x,y-1))   and self.field.field[y-1][x].text != '*'   and self.buttons[y-1][x]   != None and not self.buttons[y-1][x].flag: 
				self.reveal((x,y-1), True)
			if self.field.is_valid((x+1,y+1)) and self.field.field[y+1][x+1].text != '*' and self.buttons[y+1][x+1] != None and not self.buttons[y+1][x+1].flag: 
				self.reveal((x+1,y+1), True)
			if self.field.is_valid((x+1,y-1)) and self.field.field[y-1][x+1].text != '*' and self.buttons[y-1][x+1] != None and not self.buttons[y-1][x+1].flag: 
				self.reveal((x+1,y-1), True)
			if self.field.is_valid((x-1,y-1)) and self.field.field[y-1][x-1].text != '*' and self.buttons[y-1][x-1] != None and not self.buttons[y-1][x-1].flag: 
				self.reveal((x-1,y-1), True)
			if self.field.is_valid((x-1,y+1)) and self.field.field[y+1][x-1].text != '*' and self.buttons[y+1][x-1] != None and not self.buttons[y+1][x-1].flag: 
				self.reveal((x-1,y+1), True)




	def create_buttons(self):
		for i in range(len(self.buttons)):
			for j in range(len(self.buttons[i])):
				self.buttons[i][j] = Tile((j*36,i*36+7))


	def start(self):
		# print(self.field)
		while self.running:

			self.CLOCK.tick(self.FPS)
			self.draw(self.SCREEN)

			for event in pg.event.get():
				self.handle_event(event)
		