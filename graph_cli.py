from functools import partial
from utils.function import fnxFromCLI
from graph import graph

fnx = fnxFromCLI()

while True:
  dx = float(input('Enter dx: [default=1] ') or 1)
  epsilon = float(input('Enter epsilon: [default=0.1] ') or 0.1)

  graph_fn = partial(graph, fnx, dx, epsilon)

  while True:
    x = float(input('Enter start x: [default=0] (enter 666 to exit) ') or 0)

    if x == 666:
      break

    print(graph_fn(x))