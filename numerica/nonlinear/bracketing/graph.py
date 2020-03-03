from ...utils.math import haveSameSign

def graph(fn, dx=1, epsilon=0.1, x=0):
  prevX = x
  prevY = fn(x)

  while True:
    x += dx
    y = fn(x)

    if (y == 0):
      return x

    if abs(x - prevX) <= epsilon:
      return (x + prevX) / 2

    if haveSameSign(y, prevY):
      prevY = y
      prevX = x
    else:
      x = prevX
      y = prevY
      dx /= 2