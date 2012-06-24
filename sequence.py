#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint,uniform
from math import ceil
from printlist import print_list as pl

class Sequence:
	def __init__(self,n=2**10,m=4*2**10):
		self.__rand_uniform = []
		self.__rand_beginning = []
		self.__n = n
		self.__m = m
		self.__instance = None
		self.__a = None

	def __calculate_a(self,n):
		s = 0.0
		for j in range(2,n+2):
			s = s + 1.0/j
		self.__a = 1.0/s

		# print self.__a

		return self.__a

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
		if len(self.__rand_uniform) == 0:
		 	rang = m
		else:
			rang = len(self.__rand_uniform)

		# print rang

		sequence = []
		for i in range(0,rang):
			sequence.append(instance[randint(l,r)])
		
		self.__rand_uniform = self.__rand_uniform + sequence
		return self.__rand_uniform

	def random_beginning_seq(self,instance,l,r,m = 4*2**10,n = 2**10):
		a = self.__a

		if len(self.__rand_beginning) == 0:
		 	rang = m
		else:
			rang = len(self.__rand_beginning)

		# print "a : " + str(a)
		sequence = []
		for i in range(0,rang):
			p = self.__calculate_p(a,n)
			sequence.append(instance[p])
		
		self.__rand_beginning = self.__rand_beginning + sequence
		return self.__rand_beginning

	def generate_next_sequences(self,instance,l,r,m,n):
		if self.__rand_uniform == [] or n > self.__n or self.__instance != instance:
			# print "change"
			# print self.__n
			# print "n : " + str(n)
			# print "m : " + str(m)

			self.__rand_uniform = []
			self.__rand_beginning = []
			self.__calculate_a(n)
			self.__n = n
			self.__instance = instance

		return [self.random_uniform_seq(instance,l,r,m),self.random_beginning_seq(instance,l,r,m,n)]

	def test(self):
		instance = []
		for i in range(0,2**12):
			instance.append(i)
		l = 0
		n = len(instance)
		r = n - 1
		m = 4*n
		while m<=8*n:
			sequences = self.generate_next_sequences(instance,l,r,m,n)
			uniform = sequences[0]
			begin   = sequences[1]		
			pl("random uniform",uniform)
			pl("random beginning uniform",begin)
			m = m*2

#ejemplo de uso en test
# seq = Sequence()
# seq.test()