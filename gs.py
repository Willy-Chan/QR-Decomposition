import numpy as np
import math

def norm(v):
    """
    :param v: vector as a numpy array
    :return: norm value as a float

    >>> round(norm(np.array([2,3])))
    4

    >>> round(norm(np.array([12, -51, 4])))
    53

    >>> round(norm(np.array([6, 167, -68])))
    180
    """
    total = 0

    for elem in v:
        total += elem ** 2

    norm_value = math.sqrt(total)

    return norm_value



def get_proj(v1, v2):
    """
    :param v1: vector parallel to projection
    :param v2: vector to be projected onto v1
    :return: projection vector of v2 ONTO v1
    """
    proj_dir = v1 / norm(v1)
    proj_len = np.dot(v2, proj_dir)

    proj = proj_len * proj_dir

    return proj



def gram_schmidt(matrix):       #INPUT MATRIX IS ALREADY TRANSPOSED, SO THE "COLUMNS" ARE REALLY ROWS WITHIN THE NUMPY ARRAY

    # Create a new normalized matrix that's first 'empty' (contains only zeroes),
    # then appending the normalized vectors (REPLACING the zeroes).

    """
    NumPy arrays are stored in contiguous blocks of memory.
    To append rows or columns to an existing array, the entire array needs to be copied to a new block of memory,
    creating gaps for the new elements to be stored. This is very inefficient if done repeatedly.

    Instead of appending rows, allocate a suitably sized array, and then assign to it row-by-row
    """

    normalized_matrix = np.zeros(shape=matrix.shape)

    # num_rows, num_cols = matrix.shape               # Get shape of matrix (for future reference)

    matrix_row_length = len(matrix[0])
    matrix_col_length = len(matrix)

    for i in range(matrix_col_length):
        gs_terms = np.zeros(shape=matrix_row_length)  # G-S terms to be subtracted: RESETS EVERY TIME!!!

        for j in range(i):
                gs_terms += get_proj(normalized_matrix[j], matrix[i])       # Remember: GS terms are just the PROJECTION of one row onto all of the previous

        new_vector = matrix[i] - gs_terms  # Slice the entire ith element (individual row) & add to GS terms

        normalized_matrix[i] = new_vector / norm(new_vector)  # Replace the ith row in norm_matrix with the new (orthonormal) vector

    return normalized_matrix


square_matrix = np.array([[1, 1, 7],
                          [3, 3, -1],
                          [5, 1, 7]]).transpose()