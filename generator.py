from random import randint
#Esta clase representa un generador de instancias(arreglos de tamaño n) de las dos formas requeridas
#de la tarea, con distribucion uniforme, y de forma aleatoria en el dominio.
class InputGenerator:
	#range: rango de valores del dominio
	#n: numero de elementos del arreglo
	def __init__(self,n = 2**10,range = [0,2**32-1]):
		self.__range = range
		self.__n = n
		#self.__input

	#dist: rango de distribución uniforme de elementos sucesivos de la instancia
	def uniform_gen(self,dist = [1,16]):
		rand_num = randint(self.range[0],self.range[1])
		previous = rand_num
		inputset = [rand_num]

		for i in range(1,self.__n):
			#rangos [left,rigth] para la distribución uniforme del siguiente numero
			left = previous - (dist[1] + 1) + dist[0]
			if left<0:
				left = 0
			rigth = previous + (dist[1] + 1) - dist[0]

			rand_num = randint(left,rigth)
			previous = rand_num
			inputset.append(rand_num)
		return inputset

	def random_gen(self):
		inputset = []
		for i in range(0,self.__n):
			inputset.append(randint(self.__range[0],self.__range[1]))