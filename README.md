# Python QR Decomposition Calculator
This project utilizes the NumPy library to decompose any real square matrix into an orthogonal matrix (Q) multiplied by an upper triangular matrix (R).

## Demo

## Overview
The QR-Decomposition breaks down a matrix A into the product of two matrices: an orthogonal matrix Q and an upper triangular matrix R. The decomposition is represented mathematically as:

$A = QR$

where
* $A$ is the original input matrix
* $Q$ is the orthogonal matrix
* $R$ is the upper triangular matrix

The orthogonal matrix $Q$ has the property $Q^T * Q = I$, where $Q^T$ denotes the transpose of $Q$ and $I$ is the identity matrix. The upper triangular matrix $R$ contains the transformed values of the original matrix $A$.

## Usage
To use the QR-Decomposition project, follow these steps:
* Ensure that you have NumPy installed. You can install it using the following command:
```shell
pip install numpy
```
* Open the Python script in your preferred code editor.
* Provide the matrix A that you want to decompose. You can specify the matrix by modifying the input array in the code.
* Run the script. The program will perform the QR-Decomposition and output the resulting orthogonal matrix $Q$ and upper triangular matrix $R$.

You can verify the decomposition by multiplying $Q^T$ with $R$ and comparing it to the original matrix $A$. Mathematically, this can be represented as:
$A = Q * R$
$A = Q^T * (Q * R)$

Please note that the QR-Decomposition project utilizes NumPy's built-in functions to perform the decomposition. It is designed for real square matrices.

## Support
If you encounter any issues or have questions regarding the QR-Decomposition project, please feel free to open an issue on the GitHub repository or contact me personally at **willyc@stanford.edu**

## License
The QR-Decomposition project is released under the MIT License. You are free to use, modify, and distribute the code in accordance with the terms and conditions of the license.
