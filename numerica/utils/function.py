from functools import partial

def _fnx(coeff=[], baseExp=1, x=0):
  result = 0

  exp = len(coeff)
  for c in coeff:
    exp -= 1
    result += c * (x ** exp)

  return result ** baseExp

def fnx(coeff=[], baseExp=1):
  return partial(_fnx, coeff, baseExp)