import sys
import os
import numpy as np
from utils.IO import *
from utils.decompose import *
from utils.standardize import *

print("######################## Fourier Transform-based instance decomposition of the QAP - By Xabier Benavides ########################")
print("###                                                                                                                           ###")
print("###       This program decomposes any given QAP instance into four sub-instances containing the mean information (n.dat),     ###")
print("###       the first-order information (n_1_1.dat), the second-order unordered information (n_2_2.dat) and the second-order    ###")
print("###       ordered information (n_2_1_1.dat) of the original problem, respectively. The decomposition is based on the          ###")
print("###       Fourier Transform of the objective function.                                                                        ###")
print("###                                                                                                                           ###")
print("#################################################################################################################################")

print()

# Instance reading
while(True):

	infile = input("Enter path to QAP instance in QAPLIB format: ")

	print()
	print("Reading instance...")
	
	try:
		d_matrix, h_matrix, n = read_QAP(infile)
	except:
		print("An unexpected error has occurred while reading the instance, try again!")
		print()
		continue
	
	break

# Instance decomposition	
print("Decomposing instance...")
n_matrix, n_1_1_matrix, n_2_2_matrix, n_2_1_1_matrix = decompose(h_matrix,n)
print()

while(True):
	res = input("Do you want to standardize the sub-instances? (Y/N) ")
	if res == "Y" or res == "y":
		print("Standardizing sub-instances...")
		n_1_1_matrix = standardize(d_matrix,n_1_1_matrix,n)
		n_2_2_matrix = standardize(d_matrix,n_2_2_matrix,n)
		n_2_1_1_matrix = standardize(d_matrix,n_2_1_1_matrix,n)
		print()
		break
	elif res == "N" or res == "n":
		print()
		break

# Sub-instance saving
while(True):
	outfile = input("Enter folder in which to save the sub-instances: ")

	print()
	print("Saving sub-instances...")
	try:
		print_QAP(d_matrix,n_matrix,n,outfile+"/n.dat")
		print_QAP(d_matrix,n_1_1_matrix,n,outfile+"/n_1_1.dat")
		print_QAP(d_matrix,n_2_2_matrix,n,outfile+"/n_2_2.dat")
		print_QAP(d_matrix,n_2_1_1_matrix,n,outfile+"/n_2_1_1.dat")
	except:
		print("An unexpected error has occurred while saving the sub-instances, try again!")
		print()
		continue
		
	print("Done!")
	break
