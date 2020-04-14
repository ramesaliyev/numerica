import math
from ...utils.function import parse_f
from ...utils.math import haveSameSign

@parse_f()
def regulafalsi(fx, epsilon=0.1, a=-10, b=10):
  prevC = math.inf # infinity

  if (fx(a) == 0):
    return a

  if (fx(b) == 0):
    return b

  while True:
    fna = fx(a)
    fnb = fx(b)

    c = ((fna * b) - (fnb * a)) / (fna - fnb)
    fnc = fx(c)

    if (fnc == 0):
      return c

    if abs(prevC - c) <= epsilon:
      return c

    if haveSameSign(fnc, fna):
      a = c
    else:
      b = c

    prevC = c