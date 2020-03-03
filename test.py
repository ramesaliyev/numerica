import numerica as n

from numerica import f, c
from numerica import diff_backward

fn1 = f([1, -6, 5]) # (x^2 - 6x + 5)^1
fn2 = f([1, -6.5, 13.5, -9]) # (1x^3 - 6.5x^2 + 13.5x - 9)^1
fn3 = f([1, -4, -4, 15]) # f = x^3 - 4x^2 - 4x + 15

# nonlinear.iterative.basic
gx = f([1, 0]) # g(x) = x
hx1 = f([2, 3], 1/2) # h(x) = (2x + 3)^(1/2)
hx2 = c(f([3, 0]), f([1, -2], -1)) # h(x) = (3 / (x - 2))
hx3 = c(f([1/2, 0]), f([1, 0, -3])) # h(x) = (x^2 - 3) / 2