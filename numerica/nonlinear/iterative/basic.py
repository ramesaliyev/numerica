from ...utils.math import haveSameSign
from ...differentiation.backward import backward as diff_backward

def basic(gx, hx, epsilon=0.1, x=0):
  if (diff_backward(gx, x) <= diff_backward(hx, x)):
    return None

  while True:
    g = gx(x)
    h = hx(x)

    if abs(g - h) <= epsilon:
      return x

    x = h