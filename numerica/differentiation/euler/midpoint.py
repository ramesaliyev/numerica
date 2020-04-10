def midpoint(fn, x1, delta=0.0000000001):
  x0 = x1 - delta
  x2 = x1 + delta
  return (fn(x2) - fn(x0)) / (x2 - x0)