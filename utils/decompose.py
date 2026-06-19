import sys
import os
import numpy as np

# Function that decomposes a QAP flow matrix into the (n), (n-1,1), (n-2,2) and (n-2,1,1) components according to the Fourier transform
# (See "The distribution of values in combinatorial optimization problems", by Tamon Stephen, 2002)
def decompose(h_matrix,n):

	######## (n) component ########
	
	# 0th order (mean)

	in_diagonal = h_matrix[np.eye(n, dtype=bool)]
	off_diagonal = h_matrix[~np.eye(n, dtype=bool)]

	n_matrix = np.full((n,n),off_diagonal.mean())
	np.fill_diagonal(n_matrix, in_diagonal.mean())

	######## (n-1,1) component ########
	
	# 1st order
	
	row_sum = h_matrix.sum(axis=1, keepdims=True)  # shape: [n, 1]
	col_sum = h_matrix.sum(axis=0, keepdims=True)  # shape: [1, n]
	
	in_diagonal_sum = in_diagonal.sum()
	off_diagonal_sum = off_diagonal.sum()
	total_sum = off_diagonal_sum + in_diagonal_sum

	n_1_1_matrix = (
	(n - 1) * row_sum
	+ col_sum.T
	+ (n - 1) * col_sum
	+ row_sum.T
	- 2 * total_sum
	- n*np.diag(h_matrix)[:, None]
	- n*np.diag(h_matrix)[None, :]
	+ 2 * in_diagonal_sum
	) / (n * (n - 2))

	n_1_1_matrix[np.diag_indices(n)] += ((
	n*np.diag(h_matrix)[:, None]
	- in_diagonal_sum
	- row_sum
	- col_sum.T
	+ (2 / n) * total_sum
	) / (n - 2)).reshape(n)
	
	######## (n-2,1,1) component ########
	
	# Symmetric part (2nd order)
	
	n_2_1_1_matrix = (h_matrix-h_matrix.T+(-col_sum+row_sum.T-row_sum+col_sum.T)/n)/2
	
	######## (n-2,2) component ########
	
	# Anti-symmetric part (2nd order)
	
	n_2_2_matrix = h_matrix-(n_matrix+n_1_1_matrix+n_2_1_1_matrix) 

	return n_matrix, n_1_1_matrix, n_2_2_matrix, n_2_1_1_matrix
