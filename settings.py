#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'cqb'


class Settings:
	"""存储游戏《外星人入侵》中所有设置的类"""

	def __init__(self):
		"""初始化游戏设置"""
		# 屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		# 浅灰色
		# self.bg_color = (230, 230, 230)
		# 红色
		# self.bg_color = (250, 0, 0)
		# 绿色
		# self.bg_color = (0, 250, 0)
		# 蓝色
		self.bg_color = (0, 0, 250)
