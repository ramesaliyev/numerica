from math import prod
from ..utils.math import permutation
from ..matrix.define import parse_matrix
from ..matrix.operations import size, copy, rowconcat

@parse_matrix(3)
def gaussseidel(A, C, X, epsilon=0.01, max_iteration=1000000):
  (_, n) = size(A)

  orders = permutation(list(range(n)))
  biggest_order = None
  biggest_diagonal = float('-inf')

  for order in orders:
    diagonal = [A[i][j] for (j, i) in enumerate(order)]
    product = abs(prod(diagonal))

    if (product > biggest_diagonal):
      biggest_order = order
      biggest_diagonal = product

  A = [A[i] for i in biggest_order]
  C = [C[i] for i in biggest_order]

  prevX = X
  X = copy(X)

  iteration = max_iteration
  while iteration > 0:
    iteration -= 1

    for i in range(n):
      sum_of_rest = sum(
        [A[i][j] * X[j][0]
        for j in range(n) if j != i
      ])

      X[i][0] = (C[i][0] - sum_of_rest) / A[i][i]

    if all([abs(X[j][0] - prevX[j][0]) <= epsilon for j in range(n)]):
      return X

    prevX = copy(X)

  return X
