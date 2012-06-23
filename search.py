#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint

class Search:
	def __init(self,instance):
		self.__instance = instance

	def bin_search(self,instance,l,r,x):
		m = (l + r)/ 2
		if instance[m] < x:
			self.bin_search(instance,l,m-1,x)
		elif instance[m] > x:
			self.bin_search(instance,m+1,r,x)
		else:
			return x

	def interpolation_seach(self,instance,l,r,x):
		p = l + (r-l)*(x-instance[l]) /(instance[r]-instance[l])
		if instance[p] < x:
			self.interpolation_search(instance,l,p-1,x)
		elif instance[p] > x:
			self.bin_search(instance,p+1,r,x)
		else:
			return x

	def __one_step_bin_search(self,instance,l,r,x):
		m = (l + r)/ 2
		if instance[m] < x:
			self.__one_step_interpolation_search(instance,l,m-1,x)
		elif instance[m] > x:
			self.__one_step_interpolation_search(instance,m+1,r,x)
		else:
			return x

	def __one_step_interpolation_search(self,instance,l,r,x):
		p = l + (r-l)*(x-instance[l]) /(instance[r]-instance[l])
		if instance[p] < x:
			self.__one_step_bin_search(instance,l,p-1,x)
		elif instance[p] > x:
			self.__one_step_bin_search(instance,p+1,r,x)
		else:
			return x

	def mix_inter_search(self,instance,l,r,x):
		self.__one_step_bin_search(instance,l,r,x)