from ...utils.function import parse_f
from ...differentiation.euler.midpoint import midpoint as diff_midpoint

@parse_f()
def newtonraphson(fx, epsilon=0.1, x=0):
  while True:
    xPrev = x
    x = x - (fx(x) / diff_midpoint(fx, x))

    if (abs(x - xPrev) <= epsilon):
      return x