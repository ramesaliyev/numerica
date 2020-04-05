from copy import deepcopy
from .define import m

def parse_matrix(count = 1):
    def multiplier(fn):
        def function(*args, **kwargs):
            argz = [m(v) if i < count else v for (i,v) in enumerate(list(args))]

            return fn(*argz, **kwargs)
        return function
    return multiplier

def identity(n):
  return [[(1 if i==j else 0) for j in range(n)] for i in range(n)]

@parse_matrix()
def size(matrix):
  return (len(matrix), len(matrix[0]))

@parse_matrix()
def transpose(matrix):
  (r, c) = size(matrix)
  return [[matrix[i][j] for i in range(r)] for j in range(c)]

@parse_matrix(2)
def concat(A, B):
  r = size(A)[0]
  return [A[i] + B[i] for i in range(r)]

@parse_matrix(2)
def concat_v(A, B):
  return A + B
