from math import prod

def lagrange(pairs, n, x):
  result = 0

  for i in range(n+1):
    (xi, yi) = pairs[i]

    li = prod([
      (x - pairs[j][0]) / (xi - pairs[j][0])
      for j in range(n+1)
      if j != i
    ])

    result += li * yi

  return result