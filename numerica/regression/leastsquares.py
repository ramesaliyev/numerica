from ..finite_differences.degree import degree
from ..linear_systems.gauss import gauss
from ..utils.math import polynomial

def leastsquares(pairs, x, deg=None):
  if deg == None:
    deg = degree(pairs)

  n = deg + 1

  A = [[[0] for j in range(n)] for i in range(n)]
  C = [[0] for i in range(n)]

  for i in range(n):
    C[i][0] = sum([
      (pair[0] ** i) * pair[1]
      for pair in pairs
    ])

    for j in range(n):
      A[i][j] = sum([
        pair[0] ** (i + j)
        for pair in pairs
      ])

  X = gauss(A, C)

  result = polynomial([xi[0] for xi in X], x)
  return result