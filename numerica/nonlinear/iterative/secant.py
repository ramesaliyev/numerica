from ...utils.math import haveSameSign

def secant(fn, epsilon=0.1, x0=-10, x1=10):
  while True:
    y0 = fn(x0)
    y1 = fn(x1)

    x2 = (x0 - (((x1-x0)/(y1 - y0)) * y0))
    y2 = fn(x2)

    if (y2 == 0):
      return x2

    if abs(x0 - x2) <= epsilon:
      return x2

    if haveSameSign(y0, y2):
      x0 = x2
    else:
      x1 = x2