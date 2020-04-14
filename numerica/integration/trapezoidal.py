from ..utils.function import parse_f

@parse_f()
def trapezoidal(fx, x0, xn, n):
  h = (xn - x0) / n

  return h * (
    ((fx(x0) + fx(xn)) / 2) + (
      sum([fx(x0 + (i*h)) for i in range(1, n)])
    )
  )