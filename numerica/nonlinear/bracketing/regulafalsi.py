import math
from ...utils.math import haveSameSign

def regulafalsi(fn, epsilon=0.1, a=-10, b=10):
  prevC = math.inf # infinity

  while True:
    fna = fn(a)
    fnb = fn(b)

    c = ((fna * b) - (fnb * a)) / (fna - fnb)
    fnc = fn(c)

    if (fnc == 0):
      return c

    if haveSameSign(fnc, fna):
      a = c
    elif abs(prevC - c) > epsilon:
      b = c
    else:
      return c

    prevC = c