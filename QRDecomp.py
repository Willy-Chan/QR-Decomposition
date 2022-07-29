"""

QR Decomposition Program:

Decompose matrix A into Q (orthogonal / orthonormal matrix) and R (upper triangular matrix)

Q is found by taking the rows and doing gram-schmidt

"""

import numpy as np
import gs


square_matrix = np.array([[1, 1, 7],
                          [3, 3, -1],
                          [5, 1, 7]]).transpose()       #enter the COLS as the ROWS here


square_matrix_dim = len(square_matrix[0])


def main():
    q_matrix = gs.gram_schmidt(square_matrix)
    r_matrix = np.matmul(q_matrix.transpose(), square_matrix.transpose())


    print("Original Matrix: \n", square_matrix.round(2))
    print("Q:", "\n", q_matrix.round(2))
    print("R:", "\n", r_matrix.round(2))



if __name__ == '__main__':
    main()
