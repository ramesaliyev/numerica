from functools import partial

def _fnx(degree, coefficients, baseExp, x):
  result = 0

  for exp in range(0, degree + 1):
    result += coefficients[exp] * (x ** exp)

  return result ** baseExp

def fnx(degree, coefficients, baseExp):
  return partial(_fnx, degree, coefficients, baseExp)