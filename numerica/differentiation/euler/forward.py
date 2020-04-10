def forward(fn, x0, delta=0.0000000001):
  x1 = x0 + delta
  return (fn(x1) - fn(x0)) / (x1 - x0)