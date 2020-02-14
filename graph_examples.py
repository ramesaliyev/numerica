from functools import partial
from utils.function import fnx
from graph import graph

fn1 = partial(fnx, 2, [5, -6, 1])

print(graph(fn=fn1, x=0))
print(graph(fn=fn1, x=2))

print(graph(fn=fn1, x=0.12, epsilon=0.001))
print(graph(fn=fn1, x=2.12, epsilon=0.001))