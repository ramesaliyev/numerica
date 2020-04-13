from re import sub
from functools import partial

def fnx(coeff=[], baseExp=1, x=0):
  result = 0

  exp = len(coeff)
  for c in coeff:
    exp -= 1
    result += c * (x ** exp)

  return result ** baseExp

def c(outer, inner):
  return lambda x: outer(inner(x))

def f(coeff, baseExp=1):
  return partial(fnx, coeff, baseExp)

def fn(txt):
  def call(x=0, **keywords):
    fn = txt
    fn = fn.replace('^', '**')

    keywords['x'] = x

    for k in keywords:
      k = str(k)
      v = str(keywords[k])
      fn = sub(r'(\d+?)' + k, r'\g<1>*(' + v + ')', fn)
      fn = fn.replace(k, v)

    return float(eval(fn))
  return call