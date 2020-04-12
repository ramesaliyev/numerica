def degree(pairs, max_iteration=1000000):
  deg = 0
  diffs = [pair[1] for pair in pairs]

  iteration = max_iteration
  while iteration > 0:
    iteration -= 1

    n = len(diffs) - 1
    diffs = [diffs[i+1] - diffs[i] for i in range(n)]

    if (all([i == 0 for i in diffs])):
      break

    deg += 1

  return deg