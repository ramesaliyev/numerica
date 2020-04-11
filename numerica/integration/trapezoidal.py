def trapezoidal(fn, x0, xn, n):
  h = (xn - x0) / n

  return h * (
    ((fn(x0) + fn(xn)) / 2) + (
      sum([fn(x0 + (i*h)) for i in range(1, n)])
    )
  )