from math import prod

def lagrange(pairs, x, n=None):
  result = 0
  max_n = len(pairs) - 1

  if n == None or n > max_n:
    n = max_n

  for i in range(n+1):
    (xi, yi) = pairs[i]

    li = prod([
      (x - pairs[j][0]) / (xi - pairs[j][0])
      for j in range(n+1)
      if j != i
    ])

    result += li * yi

  return result