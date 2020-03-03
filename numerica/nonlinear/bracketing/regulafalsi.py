import math
from ...utils.math import haveSameSign

def regulafalsi(fn, epsilon=0.1, a=-10, b=10):
  prevC = math.inf # infinity

  if (fn(a) == 0):
    return a

  if (fn(b) == 0):
    return b

  while True:
    fna = fn(a)
    fnb = fn(b)

    c = ((fna * b) - (fnb * a)) / (fna - fnb)
    fnc = fn(c)

    if (fnc == 0):
      return c

    if abs(prevC - c) <= epsilon:
      return c

    if haveSameSign(fnc, fna):
      a = c
    else:
      b = c

    prevC = c