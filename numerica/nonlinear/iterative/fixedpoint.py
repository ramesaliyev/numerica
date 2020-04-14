from ...utils.function import parse_f, f
from ...utils.math import haveSameSign
from ...differentiation.euler.midpoint import midpoint as diff_midpoint

@parse_f()
def fixedpoint(hx, epsilon=0.1, x=0):
  gx = f('x')

  if (diff_midpoint(gx, x) <= diff_midpoint(hx, x)):
    return None

  while True:
    g = gx(x)
    h = hx(x)

    if abs(g - h) <= epsilon:
      return x

    x = h