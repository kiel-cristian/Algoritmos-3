#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
from printlist import print_list as pl
#Esta clase representa un generador de instancias(arreglos de tamaño n) de las dos formas requeridas
#de la tarea, con distribucion uniforme, y de forma aleatoria en el dominio.

class InputGenerator:
	#range: rango de valores del dominio
	#n: numero de elementos del arreglo
	def __init__(self,range = [0,2**32-1],dist=[1,16]):
		self.__range = range
		self.__uniform = []
		self.__random  = []
		self.__dist = dist

	#dist: rango de distribución uniforme de elementos sucesivos de la instancia
	def uniform_gen(self,n = 2**10):
		rand_num = randint(self.__range[0],self.__range[1])
		previous = rand_num
		self.__uniform.append(rand_num)
		dist = self.__dist

		for i in range(1,n):
			#rangos [left,rigth] para la distribución uniforme del siguiente numero
			left = previous - (dist[1] + 1) + dist[0]
			if left<0:
				left = 0
			rigth = previous + (dist[1] + 1) - dist[0]

			rand_num = randint(left,rigth)
			previous = rand_num
			self.__uniform.append(rand_num)
		return self.__uniform

	def random_gen(self,n = 2**10):
		for i in range(0,n):
			self.__random.append(randint(self.__range[0],self.__range[1]))
		return self.__random

	def reset_instance(self):
		self.__uniform = []
		self.__random  = []

	def generate_next_instance(self):
		n = len(self.__uniform)
		if n==0:
			n = 2**10
		elif n == 2**20:
			return [self.__uniform,self.__random]

		uniform = self.uniform_gen(n)
		random  = self.random_gen(n)
		return [uniform,random]

	def test(self):
		for i in range(0,6):
			r = self.generate_next_instance()
			pl("uniform",r[0])
			pl("random",r[1])

#Ejemplo de uso en test:
# ig = InputGenerator()
# ig.test()