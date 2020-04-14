import math
from ...utils.function import parse_f
from ...utils.math import haveSameSign

@parse_f()
def bisection(fx, epsilon=0.1, a=-10, b=10):
  prevC = math.inf # infinity

  while True:
    c = (a + b) / 2
    fnc = fx(c)

    if (fnc == 0):
      return c

    fna = fx(a)

    if (fnc == 0):
      return c

    if (fna == 0):
      return a

    if abs(prevC - c) <= epsilon:
      return c

    if haveSameSign(fnc, fna):
      a = c
    else:
      b = c

    prevC = c