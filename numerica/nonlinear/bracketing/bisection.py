import math
from ...utils.math import haveSameSign

def bisection(fn, epsilon=0.1, a=-10, b=10):
  prevC = math.inf # infinity

  while True:
    c = (a + b) / 2
    fnc = fn(c)

    if (fnc == 0):
      return c

    fna = fn(a)

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