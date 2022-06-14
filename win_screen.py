import pygame as pg
from utils.colors import *
from field import *
from tile import *
import os, sys

class WinScreen:
	def __init__(self, parent):
		self.show = False
		self.font = pg.font.SysFont('Consolas', 32)
		self.size = (350, 450)
		self.pos = (parent.WIDTH//2-self.size[0]//2, parent.HEIGHT//2-self.size[1]//2)
		self.rect = pg.Rect(self.pos, self.size)
		self.restart_button = pg.Rect(parent.WIDTH//2-100, parent.HEIGHT//2+self.size[1]//2-100,200, 42)

	def draw(self, screen):
		if self.show:
			pg.draw.rect(screen, GREY_4, self.rect)
			title = self.font.render('Congratulations!', True, WHITE)
			screen.blit(title, (self.pos[0] + self.size[0]//2 - title.get_width()//2, self.pos[1]))
			pg.draw.rect(screen, GREY_2, self.restart_button)
			pg.display.flip()


