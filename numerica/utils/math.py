def haveSameSign(a, b):
  return (a >= 0) == (b >= 0)

def permutation(items):
  if len(items) == 1:
    return items

  result = []
  for (i, n) in enumerate(items):
    rest = items[:i] + items[(i + 1):]

    for m in permutation(rest):
      result.append([n] + (m if type(m) == list else [m]))

  return result