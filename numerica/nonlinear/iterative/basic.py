from ...utils.math import haveSameSign

def basic(fngx, fnhx, dgdx, dhdx, epsilon=0.1, x=0):
  if (dgdx(x) <= dhdx(x)):
    return None

  while True:
    g = fngx(x)
    h = fnhx(x)

    if abs(g - h) > epsilon:
      x = h
    else:
      return x
