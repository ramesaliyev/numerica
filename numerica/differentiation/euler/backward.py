def backward(fn, x1, delta = 0.0000000001):
  x0 = x1 - delta
  return (fn(x0) - fn(x1)) / (x0 - x1)