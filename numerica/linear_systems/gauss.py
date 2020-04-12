from functools import reduce
from ..matrix.define import parse_matrix
from ..matrix.operations import rowmap, rowslice, rowconcat, size

@parse_matrix(2)
def gauss(A, C):
  (_, n) = size(A)
  A = rowconcat(A, C)

  for i in range(n):
    rowmap(A, i+1, lambda cell: cell / A[i][i])

    for k in range(i + 1, n):
      pivot = A[k][i]
      rowmap(A, k+1, lambda cell: cell / pivot)
      rowmap(A, k+1, lambda cell, j: cell - A[i][j-1])
      rowmap(A, k+1, lambda cell: cell * pivot)

  C = rowslice(A, n, n+1)
  A = rowslice(A, 0, n)

  X = [[0] for p in range(n)]

  for i in range(n-1, -1, -1):
    xi = (1 / A[i][i])

    xi *= (C[i][0] - sum([
      A[i][j] * X[j][0]
      for j in range(i+1, n)
    ]))

    X[i][0] = xi

  return X