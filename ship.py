#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'cqb'


import pygame
from settings import Settings

class Ship:
	"""管理飞机的类"""

	def __init__(self, ai_game):
		"""初始化飞船并设置其初始位置。"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# 加载飞船图像并获取其外接矩形。
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		# self.image.fill((230, 230, 230))

		# 对于每艘新飞船，都将其放在屏幕底部的中央
		self.rect.midbottom = self.screen_rect.midbottom

		# 在飞船的熟悉x中存储小数值
		self.x = float(self.rect.x)

		# 移动标志
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""根据移动标志调整飞船的位置。"""
		# 更新飞船而不是rect对象的x值
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0: # 0改成self.screen_rect.left也行
			self.x -= self.settings.ship_speed

		# 根据self.x更新对象
		self.rect.x = self.x

	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)
