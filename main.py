#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import time
from search import *
from generator import *
from sequence import *
from printlist import print_list as print_list
from math import sqrt

#init_time = time()

#n = [2**10,2**11 ... 2**20]
#m = [4*n,8*n]

N = 2**10
M = 4*N

g = InputGenerator([0,2**32-1],[1,16])
s = Search()
seq = Sequence()
e = 1

instance_vars = ["aleatoria-uniforme","aleatoria-dominio"]
search_vars = ["aleatoria-uniforme","aleatoria-inicio"]
search_algs = ["busqueda-binaria","busqueda-interpolacion","busqueda-inter-mixta"]

def get_stadistics(array):
	mu = sum(array)/len(array)
	sig = 0
	for i in range(0,len(array)):
		sig += (array[i] - mu)**2
	sigma = sqrt(sig/len(array))
	return [mu,sigma]

def do_experiment(N,M,instance,sequence,instance_var,search_var,search_alg):
	times = []
	counter = 0

	print "Experimento: " + str(e) + " | n: " + str(N) + " | m: " + str(M) + " | instancia: " + instance_var + " | busqueda: " + search_var + " | algoritmo: " + search_alg
	for k in range(1,11):	
		time1 = time()
		for elem in sequence:
			if search_alg == "busqueda-binaria":
				b = s.bin_search(instance,0,N-1,elem)
			elif search_alg == "busqueda-interpolacion":
				s.interpolation_search(instance,0,N-1,elem)
			else:
				s.mix_inter_search(instance,0,N-1,elem)

		time2 = time()
		if k ==1:
			counter += s.get_counter()
		else:
			s.get_counter()
		deltat = time2-time1
		# print "tiempo: " + str(deltat) + " | comparaciones(total): " + str(counter) + " | comparaciones(unitaria): " + str(counter/M)
		times.append(deltat)
	sta = get_stadistics(times)
	mu = sta[0]
	sigma = sta[1]
	print "tiempo(estadistico): " + str(mu) + " +/- " + str(sigma) + "| comparaciones(total): " + str(counter) + " | comparaciones(unitaria): " + str(counter/M) + "\n"

for i in range(1,5): #(1,11)
	instances = g.generate_next_instance()

	for instance_var in instance_vars:

		if instance_var == "aleatoria-uniforme":
			instance = instances[0]
		else:
			instance = instances[1]

		M = 4*N
		seq.reset_sequences(M)
		
		for j in range(1,3):
			if e< 24 and e>30:
				break
			sequences = seq.generate_next_sequences(instance,0,N-1,N)

			for search_var in search_vars:
				if search_var == "aleatoria-uniforme":
					sequence = sequences[0]
				else:
					sequence = sequences[1]

				for search_alg in search_algs:
					do_experiment(N,M,instance,sequence,instance_var,search_var,search_alg)
					e = e+1

			M = M*2
	N = N*2
