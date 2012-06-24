#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint,uniform
from math import ceil
from printlist import print_list as pl

class Sequence:
	def __init__(self):
		self.__sequence = []

	def __calculate_a(self,n):
		s = 0.0
		for j in range(2,n+2):
			s = s + 1.0/j
		return 1.0/s

	def __calculate_p(self,a,n):
		y = uniform(a/(n+1),a)

		# print "y : " + str(y)

		i = 1
		for p in range(1,n+1):
			if y <= a/(p + 1) and y > a/(p+2):
				# print "founded p :" + str(p)
				i = p
				break
		# print "i : " + str(i-1)
		return i-1

	def random_uniform_seq(self,instance,l,r,m = 4*2**10):
		self.sequence = []
		for i in range(0,m):
			self.sequence.append(instance[randint(l,r)])
		return self.sequence

	def random_beginning_seq(self,instance,l,r,m = 4*2**10,n = 2**10):
		a = self.__calculate_a(n)
		# print "a : " + str(a)
		self.sequence = []
		for i in range(0,m):
			p = self.__calculate_p(a,n)
			self.sequence.append(instance[p])
		return self.sequence

	def test(self):
		instance = [1,2,3,4,5,6,7,8,9,10]
		l = 0
		n = len(instance)
		r = n - 1
		m = 4*n
		while m<=8*n:			
			pl("random uniform",self.random_uniform_seq(instance,l,r,m))
			pl("random beginning uniform",self.random_beginning_seq(instance,l,r,m,n))
			m = m*2

#ejemplo de uso en test
# seq = Sequence()
# seq.test()