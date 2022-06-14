import pygame as pg
from utils.colors import *

class Tile:
	def __init__(self, pos):
		self.size = 35
		self.pos = pos
		self.color = WHITE
		self.selected = False
		self.rect = pg.Rect(pos[0], pos[1], self.size,self.size)
		self.font = pg.font.SysFont('Consolas', 32)
		self.flag = False


	def draw(self, screen, mousepos):
		if self.rect.collidepoint(mousepos):
			self.color = GREEN
			self.selected = True
		else:
			self.color = WHITE
			self.selected = False
		pg.draw.rect(screen, self.color, self.rect)
		if self.flag:
			surface = self.font.render('F', True, RED)
			screen.blit(surface, (self.pos[0]+10, self.pos[1]+4))


class Label:
	def __init__(self, pos, text):
		pg.font.init()
		self.pos = pos
		self.font = pg.font.SysFont('Consolas', 32)
		self.text = text

	def draw(self, screen):
		surface = None

		if self.text == '1':
			surface = self.font.render(self.text, True, ONE)
		elif self.text == '2':
			surface = self.font.render(self.text, True, TWO)
		elif self.text == '3':
			surface = self.font.render(self.text, True, THREE)
		elif self.text == '4':
			surface = self.font.render(self.text, True, FOUR)
		elif self.text == '5':
			surface = self.font.render(self.text, True, FIVE)
		elif self.text == '6':
			surface = self.font.render(self.text, True, SIX)
		elif self.text == '8':
			surface = self.font.render(self.text, True, EIGHT)
		else:
			surface = self.font.render(self.text, True, BLACK)

		screen.blit(surface, (self.pos[1], self.pos[0]))

	def __str__(self):
		return self.text
