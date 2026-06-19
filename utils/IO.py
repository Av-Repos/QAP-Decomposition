import sys
import os
import numpy as np

# Function that reads a QAP instance in QAPLIB format
def read_QAP(filename):
	with open(filename) as f:
		lines = [line.strip() for line in f if line.strip()]

		n = int(lines[0])

		d_matrix = np.array([
			[float(x) for x in lines[i + 1].split()]
			for i in range(n)
		])

		h_matrix = np.array([
			[float(x) for x in lines[i + 1 + n].split()]
			for i in range(n)
		])
		return(np.array(d_matrix),np.array(h_matrix),n)

# Function that prints a QAP instance in QAPLIB format
def print_QAP(d_matrix,h_matrix,n,filename):
	with open(filename,"+w") as f:
		print(str(n),file=f)
		for i in range(n):
			for j in range(n):
				print(str(round(d_matrix[i][j],15))+" ",end="",file=f)
			print(file=f)
		for i in range(n):
			for j in range(n):
				print(str(round(h_matrix[i][j],15))+" ",end="",file=f)
			print(file=f)
