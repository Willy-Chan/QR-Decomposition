"""

QR Decomposition Program:

Decompose matrix A into Q (orthogonal / orthonormal matrix) and R (upper triangular matrix)

Q is found by taking the rows and doing gram-schmidt

"""

import numpy as np
import gs


square_matrix = np.array([[1, 3, 5], [1, 3, 1], [2, -1, 7]])
square_matrix_dim = len(square_matrix[0])


def main():
    q_matrix = gs.gram_schmidt(square_matrix)

    # QR = A, but since Q^(-1) = Q^T for orthogonal (orthonormal) matrices
    # (Q^(-1) * Q) * R = (I) * R = Q^T * A
    # R = Q^T * A

    r_matrix = np.dot(q_matrix.transpose(), square_matrix)


    print("Original Matrix: \n", square_matrix.round(2))
    print("Q:", "\n", q_matrix.round(2))
    print("R:", "\n", r_matrix.round(2))



if __name__ == '__main__':
    main()
