#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint
from printlist import print_list as pl

class Search:
	def __init__(self):
		self.__counter = 0

	def get_counter(self):
		c = self.__counter
		self.__counter = 0
		return c

	def __in_range(self,instance,l,r,x):
		# print "l : " + str(l)
		# print "r : " + str(r)
		# if r-l == 1 or l==r:
		if l==r:
			if instance[l] == x:
				self.__counter += 1
				return x
		else:
			return -1

	def bin_search(self,instance,l,r,x):
		a = self.__in_range(instance,l,r,x)
		if a == x:
			return x

		m = (r + l)/ 2 + 1
		# print "-> m : " + str(m)

		self.__counter += 1
		if x < instance[m]:
			return self.bin_search(instance,l,m-1,x)
		else:
			return self.bin_search(instance,m,r,x)

	def interpolation_search(self,instance,l,r,x):
		a = self.__in_range(instance,l,r,x)
		if a == x:
			return x

		p = l + (r-l)*(x-instance[l]) /(instance[r]-instance[l])
		# print "-> p : " + str(p)

		if instance[p] < x:
			self.__counter += 1
			return self.interpolation_search(instance,l,p-1,x)
		elif x > instance[p]:
			self.__counter += 2
			return self.interpolation_search(instance,p,r,x)
		else:
			self.__counter += 2
			return x

	def __one_step_bin_search(self,instance,l,r,x):
		a = self.__in_range(instance,l,r,x)
		if a == x:
			return x

		m = (r + l)/ 2 + 1
		# print "-> m : " + str(m)

		self.__counter += 1
		if x < instance[m]:
			return self.__one_step_interpolation_search(instance,l,m-1,x)
		else:
			return self.__one_step_interpolation_search(instance,m,r,x)

	def __one_step_interpolation_search(self,instance,l,r,x):
		a = self.__in_range(instance,l,r,x)
		if a == x:
			return x

		p = l + (r-l)*(x-instance[l]) /(instance[r]-instance[l])
		# print "-> p : " + str(p)

		if x < instance[p]:
			self.__counter += 1
			return self.__one_step_bin_search(instance,l,p-1,x)
		elif x > instance[p]:
			self.__counter += 2
			return self.__one_step_bin_search(instance,p,r,x)
		else:
			self.__counter += 2
			return x

	def mix_inter_search(self,instance,l,r,x):
		return self.__one_step_bin_search(instance,l,r,x)

	def test(self):
		a = []
		for i in range(0,2**10):
			a.append(i)

		l = 0
		r = len(a) -1
		x = 4
		pl("a",a)

		print "mix search"
		self.mix_inter_search(a,l,r,x)
		print "comparations : " + str(self.get_counter())

		print "bin search"
		self.bin_search(a,l,r,x)
		print "comparations : " + str(self.get_counter())

		print "inter search"
		self.interpolation_search(a,l,r,x)
		print "comparations : " + str(self.get_counter())

#ejemplo de uso en funcion test
# s = Search()
# s.test()