#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'cqb'


class Test:

	def __init__(self):
		self.aaa = 111
		print("我是类被实例化时就会执行")

	def test001(self):
		print(123)
		self.test003 = "wc"

	def test002(self):
		self.test001()
		print(self.test003)

print(Test)
print(Test())
# Test()
a = Test().test002()
