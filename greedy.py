# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 20:29:52 2018

@author: mbeta
"""

import sys, math, csv, random
import numpy as np
#from 

# import data from csv

def greedy(data):
	best_pairs = [] # initialize to an array of 10, for example
	data_x = get_X(data)
	data_y = get_Y(data)


def get_Primes(number):
	primes = [2,5,7,11,13,17,19]
	for iterator in range(20,number):
		limit = round(iterator/2)
		divisor = 2
		isPrime = True
		while(divisor<limit and isPrime):
			if (iterator%divisor==0):
				isPrime = False
			divisor = divisor + 1
		if isPrime:
			primes.append(iterator)
	return primes


def readData(file):
	with open(file,'r', newline='') as csv_file:
		csv_reader = csv.reader(csv_file)
		cities		= []
		coorX       = []
		coorY       = []
		header = next(csv_reader)

		for rowData in csv_reader:
			#print(rowData)
			#rowData         = np.fromiter(row.split(","), dtype=int)
			currentCity     = int(rowData[0])
			currentCityX    = float(rowData[1])
			currentCityY    = float(rowData[2])
			
			cities.append(currentCity)
			coorX.append(currentCityX)
			coorY.append(currentCityY)


def randomPermutations(n):
	return random.sample(range(1,n+1),n)
		
def main():
	file = sys.argv[1]
	readData(file)

main()