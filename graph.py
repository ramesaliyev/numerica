def fn(x):
  return (x ** 2) - (6*x) + 5

# 1 and 5

def hasSameSign(a, b):
  return (a >= 0) == (b >= 0)

def graph(x, dx=1, epsilon=0.1):
  prevX = x
  prevY = fn(x)

  while True:
    x += dx
    y = fn(x)

    if (y == 0):
      return x

    if hasSameSign(y, prevY):
      prevY = y
      prevX = x
    elif abs(x - prevX) > epsilon:
      x = prevX
      y = prevY
      dx /= 2
    else:
      return (x + prevX) / 2

print(fn(1))
print(fn(5))

print(hasSameSign(0, 0))
print(hasSameSign(1, 2))
print(hasSameSign(-1, 1))

print(graph(0))
print(graph(2))

print(graph(0.12, epsilon=0.00000000000001))
print(graph(2.12, epsilon=0.00000000000001))
