from ...differentiation.backward import backward as diff_backward

def newtonraphson(fx, epsilon=0.1, x=0):
  while True:
    xPrev = x
    x = x - (fx(x) / diff_backward(fx, x))

    if (abs(x - xPrev) <= epsilon):
      return x