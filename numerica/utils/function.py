from functools import partial

def fnx(coeff=[], baseExp=1, x=0):
  result = 0

  exp = len(coeff)
  for c in coeff:
    exp -= 1
    result += c * (x ** exp)

  return result ** baseExp

def c(outer, inner):
  return lambda x: outer(inner(x))

def f(coeff, baseExp=1):
  return partial(fnx, coeff, baseExp)