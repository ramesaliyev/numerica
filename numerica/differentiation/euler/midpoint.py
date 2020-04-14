from ...utils.function import parse_f

@parse_f()
def midpoint(fx, x1, delta=0.0000000001):
  x0 = x1 - delta
  x2 = x1 + delta
  return (fx(x2) - fx(x0)) / (x2 - x0)