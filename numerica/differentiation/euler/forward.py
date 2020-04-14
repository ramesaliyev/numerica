from ...utils.function import parse_f

@parse_f()
def forward(fx, x0, delta=0.0000000001):
  x1 = x0 + delta
  return (fx(x1) - fx(x0)) / (x1 - x0)