"""

QR Decomposition Program:

Decompose matrix A into Q (orthogonal / orthonormal matrix) and R (upper triangular matrix)

Q is found by taking the rows and doing gram-schmidt

"""

import numpy as np
import gs

# visual math style
square_matrix = np.array([[1, 3, 5],
                          [1, 3, 1],
                          [2, -1, 7]])

# real matrix by numpy
square_matrix = np.array([[1, 1, 2],
                          [3, 3, -1],
                          [5, 1, 7]])

# square_matrix = square_matrix.transpose()       # Transpose so rows become cols, easier to work with in numpy

square_matrix_dim = len(square_matrix[0])

def main():
    q_matrix = gs.gram_schmidt(square_matrix)
    #  R = Q(inverse/transpose) * Square_Matrix
    # (Rows and columns are flipped in numpy, so it's necessary to transpose square_matrix as well)

    #r_matrix = np.matmul(q_matrix.transpose(), square_matrix.transpose())

    r_matrix = np.matmul(q_matrix, square_matrix.transpose())

    print("Original Matrix: \n", square_matrix.transpose().round(2))
    print("Q:", "\n", q_matrix.transpose().round(2))
    print("R:", "\n", r_matrix.round(2))



if __name__ == '__main__':
    main()
