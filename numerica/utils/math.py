def haveSameSign(a, b):
  return (a >= 0) == (b >= 0)

def permutation(items):
  if len(items) <=1:
    yield items
  else:
    for perm in permutation(items[1:]):
      for i in range(len(items)):
        yield perm[:i] + items[0:1] + perm[i:]

def polynomial(coeff, x):
  deg = len(coeff) - 1
  return sum([
    c * (x ** (deg - i))
    for i, c in enumerate(coeff)
  ])