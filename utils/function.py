from functools import partial

def fnx(degree, coefficients, x):
  result = 0

  for exp in range(0, degree + 1):
    result += coefficients[exp] * (x ** exp)

  return result

def fnxFromCLI():
  degree = int(input('Enter degree of function: [default=2] ') or 2)

  coefficient_count = degree + 1
  coefficients = [None] * coefficient_count

  for exp in range(0, coefficient_count):
    coefficients[exp] = int(input(f'Enter coefficient for degree {exp}: ') or 0)

  return partial(fnx, degree, coefficients)
