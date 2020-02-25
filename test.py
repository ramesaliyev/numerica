import numerica as n
from numerica import f, c

fn1 = f([1, -6, 5]) # (x^2 - 6x + 5)^1
fn2 = f([1, -6.5, 13.5, -9]) # (1x^3 - 6.5x^2 + 13.5x - 9)^1

# nonlinear.iterative.basic
gxfn = f([1, 0])
gxdg = f([1])
hxfn1 = f([2, 3], 1/2)
hxdh1 = f([2, 3], -1/2)
hxfn2 = c(f([3, 0]), f([1, -2], -1)) # f(x) = (3 / (x - 2))
hxdh2 = c(f([-3, 0]), f([1, -2], -2)) # f(x) = (-3 / (x - 2)^2)
hxfn3 = c(f([1/2, 0]), f([1, -3])) # f(x) = (x^2 - 3) / 2
hxdh3 = f([1, 0])
