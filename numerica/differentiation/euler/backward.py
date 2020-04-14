from ...utils.function import parse_f

@parse_f()
def backward(fx, x1, delta=0.0000000001):
  x0 = x1 - delta
  return (fx(x0) - fx(x1)) / (x0 - x1)