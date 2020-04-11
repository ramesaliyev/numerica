def simpson(fn, x0, xn, n):
  h = (xn - x0) / n

  return (h / 3) * (
    fn(x0) + fn(xn) +
    (4 * sum([fn(x0 + (i*h)) for i in range(1, n, 2)])) +
    (2 * sum([fn(x0 + (i*h)) for i in range(2, n-1, 2)]))
  )