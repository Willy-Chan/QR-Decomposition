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

    proj_len = np.dot(v2, v1 / norm(v1))
    proj_dir = v1 / norm(v1)

    proj = proj_len * proj_dir

    return proj



def gram_schmidt(matrix):

    # Create a new normalized matrix that's first 'empty' (contains only zeroes),
    # then appending the normalized vectors (REPLACING the zeroes).

    """
    NumPy arrays are stored in contiguous blocks of memory.
    To append rows or columns to an existing array, the entire array needs to be copied to a new block of memory,
    creating gaps for the new elements to be stored. This is very inefficient if done repeatedly.

    Instead of appending rows, allocate a suitably sized array, and then assign to it row-by-row
    """

    normalized_matrix = np.zeros(shape=matrix.shape)

    num_rows, num_cols = matrix.shape               # Get shape of matrix (for future reference)

    for i in range(len(matrix)):
        gs_terms = np.zeros(shape=len(matrix[0]))  # G-S terms to be subtracted: RESETS EVERY TIME!!!

        for j in range(i):
                gs_terms += get_proj(normalized_matrix[j], matrix[i])       # Remember: GS terms are just the PROJECTION of one row onto all of the previous

        new_vector = matrix[i] - gs_terms  # Slice the entire ith element (individual row) & add to GS terms

        normalized_matrix[i] = new_vector / norm(new_vector)  # Replace the ith row in norm_matrix with the new (orthonormal) vector

    return normalized_matrix


# input_matrix = np.array([[1, 1, 1], [2, 1, 0], [5, 1, 3]])
# print(gram_schmidt(input_matrix))