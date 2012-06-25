#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint,uniform
from math import ceil
from printlist import print_list as pl
from time import time
from sys import exit

class Sequence:
	def __init__(self,m=4*2**10):
		self.__rand_uniform = []
		self.__rand_beginning = []
		self.__m = m
		self.__a = None
		self.reset = True

	def __calculate_a(self,n):
		s = 0.0
		for j in range(2,n+2):
			s = s + 1.0/j
		self.__a = 1.0/s

		# print self.__a

		return self.__a

	def __calculate_p_2_rec(self,a,l,r,y):
		if l==r:
			if y <= a/(l+1) and y >a/(l+2):
				return l-1
		elif r-l == 1:
			y_sup = a/(l+1)
			y_inf = a/(l+2)

			if y <= y_sup and y > y_inf:
				return l-1
			elif y <= y_inf:
				return l
			else:
				print "-> l :" + str(l)
				print "-> r :" + str(r)
				print "-> y :" + str(y)

				print "y sup : " + str(y_sup)
				print "y inf : " + str(y_inf)
				print "Error en secuencias"
				exit()

		p = (l+r)/2

		if y > a/(p+1):
			return self.__calculate_p_2_rec(a,l,p-1,y)
		elif y < a/(p+2):
			return self.__calculate_p_2_rec(a,p+1,r,y)
		else:
			return p-1

	def __calculate_p_2(self,a,n):
		y = uniform(a/(n+1),a)
		return self.__calculate_p_2_rec(a,1,n+1,y)

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

	def random_uniform_seq(self,instance,l,r):
		sequence = []
		# print "m: " + str(self.__m)
		for i in range(0,self.__m):
			sequence.append(instance[randint(l,r)])
		
		self.__rand_uniform = self.__rand_uniform + sequence
		return self.__rand_uniform

	def random_beginning_seq(self,instance,l,r,n = 2**10):
		a = self.__a
		sequence = []
		for i in range(0,self.__m):
			p = self.__calculate_p_2(a,n)
			sequence.append(instance[p])
		
		self.__rand_beginning = self.__rand_beginning + sequence
		return self.__rand_beginning

	def reset_sequences(self,m):
		self.__rand_beginning = []
		self.__rand_uniform = []
		self.reset = True
		self.__m = m

	def generate_next_sequences(self,instance,l,r,n,test= False):
		if self.reset:
			self.__calculate_a(n)
			self.reset = False

		if test:
			time1 = time()
		uniform = self.random_uniform_seq(instance,l,r)
		if test:
			print "benchmark random: " + str(time()-time1)

		if test:
			time1 = time()
		beginning = self.random_beginning_seq(instance,l,r,n)
		if test:
			print "benchmark random beginning: " + str(time()-time1)

		return [uniform,beginning]

	def test(self):

		for j in range(1,3):
			instance = []
			print j
			for i in range(0,2**10*j):
				instance.append(i)

			l = 0
			n = len(instance)
			print n
			r = n - 1
			m = 4*n
			print "-> M: " + str(m)
			self.reset_sequences(m)
			while m<=8*n:
				sequences = self.generate_next_sequences(instance,l,r,n,True)
				uniform = sequences[0]
				begin   = sequences[1]		
				pl("random uniform",uniform)
				pl("random beginning uniform",begin)
				m = m*2
			

#ejemplo de uso en test
# seq = Sequence()
# seq.test()