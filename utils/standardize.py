import sys
import os
import numpy as np
import math

# Standardize the entries in the flow matrix so that the resulting objective function has variance 1
def standardize(d_matrix,h_matrix,n):

	## Compute mean of objective function
	
	# Diagonal elements
	h_00 = sum(h_matrix[i][i] for i in range(n)) / n
	
	# Out-diagonal elements
	h_01 = sum(h_matrix[i][j] 
		     for j in range(n) for i in range(n)
		     if i != j) / (n * (n - 1))
	
	mean = (
	    sum(d_matrix[i][i]*h_00 
		for i in range(n))
		
	    + sum(d_matrix[i][j]*h_01 
		for j in range(n) for i in range(n) 
		if i != j )
	)
	
	## Compute mean of squared objective function
	
	# Different index structures (15 in total)
	
	h_0000 = sum(h_matrix[i][i] * h_matrix[i][i] for i in range(n)) / n

	h_0001 = sum(h_matrix[i][i] * h_matrix[i][j]
		     for j in range(n) for i in range(n)
		     if i != j) / (n * (n - 1))

	h_0010 = sum(h_matrix[i][i] * h_matrix[j][i]
		     for j in range(n) for i in range(n)
		     if i != j) / (n * (n - 1))

	h_0011 = sum(h_matrix[i][i] * h_matrix[j][j]
		     for j in range(n) for i in range(n)
		     if i != j) / (n * (n - 1))

	h_0012 = sum(h_matrix[i][i] * h_matrix[j][k]
		     for k in range(n) for j in range(n) for i in range(n)
		     if i != j and i != k and j != k) / (n * (n - 1) * (n - 2))

	h_0100 = sum(h_matrix[i][j] * h_matrix[i][i]
		     for j in range(n) for i in range(n)
		     if i != j) / (n * (n - 1))

	h_0101 = sum(h_matrix[i][j] * h_matrix[i][j]
		     for j in range(n) for i in range(n)
		     if i != j) / (n * (n - 1))

	h_0102 = sum(h_matrix[i][j] * h_matrix[i][k]
		     for k in range(n) for j in range(n) for i in range(n)
		     if i != j and i != k and j != k) / (n * (n - 1) * (n - 2))

	h_0110 = sum(h_matrix[i][j] * h_matrix[j][i]
		     for j in range(n) for i in range(n)
		     if i != j) / (n * (n - 1))

	h_0111 = sum(h_matrix[i][j] * h_matrix[j][j]
		     for j in range(n) for i in range(n)
		     if i != j) / (n * (n - 1))

	h_0112 = sum(h_matrix[i][j] * h_matrix[j][k]
		     for k in range(n) for j in range(n) for i in range(n)
		     if i != j and i != k and j != k) / (n * (n - 1) * (n - 2))

	h_0120 = sum(h_matrix[i][j] * h_matrix[k][i]
		     for k in range(n) for j in range(n) for i in range(n)
		     if i != j and i != k and j != k) / (n * (n - 1) * (n - 2))

	h_0121 = sum(h_matrix[i][j] * h_matrix[k][j]
		     for k in range(n) for j in range(n) for i in range(n)
		     if i != j and i != k and j != k) / (n * (n - 1) * (n - 2))

	h_0122 = sum(h_matrix[i][j] * h_matrix[k][k]
		     for k in range(n) for j in range(n) for i in range(n)
		     if i != j and i != k and j != k) / (n * (n - 1) * (n - 2))

	h_0123 = sum(h_matrix[i][j] * h_matrix[k][q]
		     for q in range(n) for k in range(n)
		     for j in range(n) for i in range(n)
		     if i != j and i != k and i != q
		     and j != k and j != q and k != q) / (n * (n - 1) * (n - 2) * (n - 3))
		     
	mean_2 = (
	    sum(d_matrix[i][i] * d_matrix[i][i] * h_0000
		for i in range(n))

	    + sum(d_matrix[i][i] * d_matrix[i][j] * h_0001
		  for j in range(n) for i in range(n)
		  if i != j)

	    + sum(d_matrix[i][i] * d_matrix[j][i] * h_0010
		  for j in range(n) for i in range(n)
		  if i != j)

	    + sum(d_matrix[i][i] * d_matrix[j][j] * h_0011
		  for j in range(n) for i in range(n)
		  if i != j)

	    + sum(d_matrix[i][i] * d_matrix[j][k] * h_0012
		  for k in range(n) for j in range(n) for i in range(n)
		  if i != j and i != k and j != k)

	    + sum(d_matrix[i][j] * d_matrix[i][i] * h_0100
		  for j in range(n) for i in range(n)
		  if i != j)

	    + sum(d_matrix[i][j] * d_matrix[i][j] * h_0101
		  for j in range(n) for i in range(n)
		  if i != j)

	    + sum(d_matrix[i][j] * d_matrix[i][k] * h_0102
		  for k in range(n) for j in range(n) for i in range(n)
		  if i != j and i != k and j != k)

	    + sum(d_matrix[i][j] * d_matrix[j][i] * h_0110
		  for j in range(n) for i in range(n)
		  if i != j)

	    + sum(d_matrix[i][j] * d_matrix[j][j] * h_0111
		  for j in range(n) for i in range(n)
		  if i != j)

	    + sum(d_matrix[i][j] * d_matrix[j][k] * h_0112
		  for k in range(n) for j in range(n) for i in range(n)
		  if i != j and i != k and j != k)

	    + sum(d_matrix[i][j] * d_matrix[k][i] * h_0120
		  for k in range(n) for j in range(n) for i in range(n)
		  if i != j and i != k and j != k)

	    + sum(d_matrix[i][j] * d_matrix[k][j] * h_0121
		  for k in range(n) for j in range(n) for i in range(n)
		  if i != j and i != k and j != k)

	    + sum(d_matrix[i][j] * d_matrix[k][k] * h_0122
		  for k in range(n) for j in range(n) for i in range(n)
		  if i != j and i != k and j != k)

	    + sum(d_matrix[i][j] * d_matrix[k][q] * h_0123
		  for q in range(n) for k in range(n)
		  for j in range(n) for i in range(n)
		  if i != j and i != k and i != q
		  and j != k and j != q and k != q)
	)
	
	## Compute standard deviation
	std = math.sqrt(mean_2-mean**2)
	
	# Scale entries in the flow matrix according to standard deviation
	h_matrix = h_matrix/std
	
	return(h_matrix)
