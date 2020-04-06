from ..operations import identity, size, rowconcat, rowslice, rowmap, parse_matrix

@parse_matrix()
def gaussjordan(A):
  (_, n) = size(A)
  A = rowconcat(A, identity(n))

  for i in range(n):
    rowmap(A, i+1, lambda cell: cell / A[i][i])

    for k in range(n):
      if (i == k): continue
      rowmap(A, k+1, lambda cell, j: cell - (A[k][i] * A[i][j - 1]))

  return rowslice(A, n, 2 * n)