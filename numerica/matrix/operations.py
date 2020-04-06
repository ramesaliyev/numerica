from inspect import getargspec
from copy import deepcopy
from .define import parse_matrix

def identity(n):
  return [[(1 if i==j else 0) for j in range(n)] for i in range(n)]

@parse_matrix()
def copy(A):
  return deepcopy(A)

@parse_matrix()
def size(A):
  return (len(A), len(A[0]))

@parse_matrix()
def transpose(A):
  (r, c) = size(A)
  return [[A[i][j] for i in range(r)] for j in range(c)]

@parse_matrix(2)
def rowconcat(A, B):
  r = size(A)[0]
  return [A[i] + B[i] for i in range(r)]

@parse_matrix(2)
def colconcat(A, B):
  return A + B

@parse_matrix()
def rowslice(A, start = 0, stop = 0, step = 1):
  return [row[start:stop:step] for row in A]

@parse_matrix()
def rowmap(A, i, fn):
  i -= 1

  def call_fn(cell):
    (index, value) = list(cell)
    argc = len(getargspec(fn).args)
    return fn(value, index + 1) if argc == 2 else fn(value)

  A[i] = list(map(call_fn, enumerate(A[i])))

  return A

@parse_matrix()
def cellmap(A, fn):
  return [rowmap(A, i+1, fn)[i] for i in range(size(A)[0])]