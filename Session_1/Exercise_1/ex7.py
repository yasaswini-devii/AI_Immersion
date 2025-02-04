import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = A + B
print("Matrix Addition:")
print(C)

D = A - B
print("\nMatrix Subtraction:")
print(D)

E = A * B
print("\nElement-wise Matrix Multiplication:")
print(E)

F = np.dot(A, B)
print("\nMatrix Dot Product (Multiplication):")
print(F)

G = A / B
print("\nElement-wise Matrix Division:")
print(G)

H = np.transpose(A)
print("\nTranspose of Matrix A:")
print(H)

det_A = np.linalg.det(A)
print("\nDeterminant of Matrix A:")
print(det_A)

if det_A != 0:
    inv_A = np.linalg.inv(A)
    print("\nInverse of Matrix A:")
    print(inv_A)
else:
    print("\nMatrix A is not invertible.")
