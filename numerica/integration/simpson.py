from ..utils.function import parse_f

@parse_f()
def simpson(fx, x0, xn, n):
  h = (xn - x0) / n

  return (h / 3) * (
    fx(x0) + fx(xn) +
    (4 * sum([fx(x0 + (i*h)) for i in range(1, n, 2)])) +
    (2 * sum([fx(x0 + (i*h)) for i in range(2, n-1, 2)]))
  )