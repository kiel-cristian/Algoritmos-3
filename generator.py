#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
from printlist import print_list as pl
from radix import radixSort as radix_sort
#Esta clase representa un generador de instancias(arreglos de tamaño n) de las dos formas requeridas
#de la tarea, con distribucion uniforme, y de forma aleatoria en el dominio.

class InputGenerator:
	#range: rango de valores del dominio
	#n: numero de elementos del arreglo
	def __init__(self,range = [0,2**32-1],dist=[1,16]):
		self.__range = range
		self.__uniform = []
		self.__uniform_min =  2**32
		self.__random  = []
		self.__dist = dist

	#ajusta el valor minimo del arreglo uniforme en caso de desborde del maximo
	def __adjust_u_min(self,m):
		print "m : " + str(m)
		def minus_m(x):
			return x-m
		self.__uniform = map(minus_m,self.__uniform)

	#dist: rango de distribución uniforme de elementos sucesivos de la instancia
	def __uniform_gen(self,n = 2**10):
		u_min = self.__uniform_min
		dist = self.__dist
		max_num = self.__range[1]
		j = 0

		if self.__uniform == []:
			j += 1
			previous = randint(self.__range[0],self.__range[1])
			self.__uniform.append(previous)
			u_min = previous
		else:
			previous = self.__uniform[-1]

		for i in range(j,n):
			#rangos [left,rigth] para la distribución uniforme del siguiente numero
			left = previous + dist[0]
			rigth = previous + dist[1]
			rand_num = randint(left,rigth)
			previous = rand_num
			self.__uniform.append(rand_num)

			if rand_num > max_num:
				print "adjusting array"
				self.__adjust_u_min(u_min/2)
				previous = previous - u_min/2
				u_min = u_min/2

		self.__uniform_min = u_min
		return self.__uniform

	def __random_gen(self,n = 2**10):
		for i in range(0,n):
			self.__random.append(randint(self.__range[0],self.__range[1]))
		random = radix_sort(self.__random,32)
		self.__random = random
		return random

	def reset_instance(self):
		self.__uniform = []
		self.__random  = []

	def generate_next_instance(self):
		n = len(self.__uniform)
		if n==0:
			n = 2**10
		elif n == 2**20:
			return [self.__uniform,self.__random]

		uniform = self.__uniform_gen(n)
		random  = self.__random_gen(n)
		return [uniform,random]

	def test(self):
		for i in range(0,10):
			print i
			r = self.generate_next_instance()
			if i == 5:
				pl("uniform",r[0])
				pl("random",r[1])

#Ejemplo de uso en test:
# ig = InputGenerator()
# ig.test()