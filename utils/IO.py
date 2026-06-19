import sys
import os
import numpy as np

# Function that reads a QAP instance in QAPLIB format
def read_QAP(filename):
	with open(filename) as f:
		n = [int(x) for x in next(f).split()][0] # read first line
		d_matrix = []
		h_matrix = []
		i = 0
		for line in f:# read rest of lines
			if i < n:
			    d_matrix.append(np.array([float(x) for x in line.split()]))
			    i += 1
			elif i < 2*n:
			    h_matrix.append(np.array([float(x) for x in line.split()]))
			    i += 1
		return(np.array(d_matrix),np.array(h_matrix),n)

# Function that prints a QAP instance in QAPLIB format
def print_QAP(d_matrix,h_matrix,n,filename):
	with open(filename,"+w") as f:
		print(str(n),file=f)
		for i in range(n):
			for j in range(n):
				print(str(round(d_matrix[i][j],10))+" ",end="",file=f)
			print(file=f)
		for i in range(n):
			for j in range(n):
				print(str(round(h_matrix[i][j],10))+" ",end="",file=f)
			print(file=f)
