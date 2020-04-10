import numerica as n

from numerica import f, c
from numerica import m
from numerica import diff_backward

fn1 = f([1, -6, 5]) # (x^2 - 6x + 5)^1
fn2 = f([1, -6.5, 13.5, -9]) # (1x^3 - 6.5x^2 + 13.5x - 9)^1
fn3 = f([1, -4, -4, 15]) # f = x^3 - 4x^2 - 4x + 15
fn4 = f([1, 0, -20, 16]) # x^3 - 20x + 16
fn5 = f([1, -2, -3]) # x^2 - 2x - 3

# nonlinear.iterative.basic
gx = f([1, 0]) # g(x) = x
hx1 = f([2, 3], 1/2) # h(x) = (2x + 3)^(1/2)
hx2 = c(f([3, 0]), f([1, -2], -1)) # h(x) = (3 / (x - 2))
hx3 = c(f([1/2, 0]), f([1, 0, -3])) # h(x) = (x^2 - 3) / 2

# Tests
oks = []
errors = []
def t(a, b, name):
  if (type(a) == int or type(a) == float): a = round(a, 1)
  if (type(b) == int or type(b) == float): b = round(b, 1)

  if (n.is_matrix(a)): a = n.m_cellmap(a, lambda cell: round(cell, 2))
  if (n.is_matrix(b)): b = n.m_cellmap(b, lambda cell: round(cell, 2))

  if (a != b):
    errors.append('[error] ' + name + ' expected: (' + str(b) + ') got: (' + str(a) + ')')
  else:
    oks.append('[ok] ' + name)

def finish():
  for log in (errors if len(errors) > 0 else oks): print(log)

# Utils
t(list(n.permutation([1,2])), [[1,2], [2,1]], 'utils.math.permutation.1')
t(list(n.permutation([1,2,3])), [[1,2,3], [2,1,3], [2,3,1], [1,3,2], [3,1,2], [3,2,1]], 'utils.math.permutation.2')

# Nonlinear
t(n.nl_graph(fn=fn1, dx=1, epsilon=0.001, x=0), 1, 'nonlinear.bracketing.graph.1')
t(n.nl_graph(fn=fn1, dx=1, epsilon=0.001, x=2), 5, 'nonlinear.bracketing.graph.2')

t(n.nl_bisection(fn=fn2, epsilon=0.001, a=0, b=1.75), 1.5, 'nonlinear.bracketing.bisection.1')
t(n.nl_bisection(fn=fn2, epsilon=0.001, a=1.75, b=2.5), 2, 'nonlinear.bracketing.bisection.2')
t(n.nl_bisection(fn=fn2, epsilon=0.001, a=2.5, b=6), 3, 'nonlinear.bracketing.bisection.3')

t(n.nl_regulafalsi(fn=fn2, epsilon=0.001, a=0, b=1.75), 1.5, 'nonlinear.bracketing.regulafalsi.1')
t(n.nl_regulafalsi(fn=fn2, epsilon=0.001, a=1.75, b=2.5), 2, 'nonlinear.bracketing.regulafalsi.2')
t(n.nl_regulafalsi(fn=fn2, epsilon=0.001, a=2.5, b=6), 3, 'nonlinear.bracketing.regulafalsi.3')

t(n.nl_basic(gx, hx1, epsilon=0.005, x=4), 3, 'nonlinear.iterative.basic.1')
t(n.nl_basic(gx, hx2, epsilon=0.005, x=4), -1, 'nonlinear.iterative.basic.2')
t(n.nl_basic(gx, hx3, epsilon=0.005, x=4), None, 'nonlinear.iterative.basic.3')

t(n.nl_newtonraphson(fn3, epsilon=0.00005, x=-2.5), -2, 'nonlinear.iterative.newtonraphson.1')

t(n.nl_secant(fn4, epsilon=0.02, x0=3, x1=5), 4, 'nonlinear.iterative.secant.1')

# Matrix Operations
t(m('1'), [[1.0]], 'matrix.define.2')
t(m('1,2,3'), [[1.0,2.0,3.0]], 'matrix.define.3')
t(m('1,2,3; 4,5,6'), [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], 'matrix.define.4')
t(m('1,2,3; 4,5,6; 7,8,9'), [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]], 'matrix.define.5')
t(m([[1.0]]), [[1.0]], 'matrix.define.6')

t(n.m_id(1), m('1'), 'matrix.operations.identity.1')
t(n.m_id(3), m('1,0,0;0,1,0;0,0,1'), 'matrix.operations.identity.2')

t(n.m_size([[1.0]]), (1,1), 'matrix.operations.size.1')
t(n.m_size('1,2,3; 4,5,6; 7,8,9'), (3,3), 'matrix.operations.size.2')

t(n.m_transpose(n.m_id(3)), n.m_id(3), 'matrix.operations.transpose.1')
t(n.m_transpose('1,2,3; 4,5,6; 7,8,9'), m('1,4,7; 2,5,8; 3,6,9'), 'matrix.operations.transpose.2')
t(n.m_transpose('1,2,3; 4,5,6'), m('1,4; 2,5; 3,6'), 'matrix.operations.transpose.3')

t(n.m_rowconcat('1,2,3; 4,5,6; 7,8,9', '10,20,30; 40,50,60; 70,80,90'), n.m('1,2,3,10,20,30; 4,5,6,40,50,60; 7,8,9,70,80,90'), 'matrix.operations.rowconcat.1')
t(n.m_colconcat('1,2,3; 4,5,6; 7,8,9', '10,20,30; 40,50,60; 70,80,90'), n.m('1,2,3; 4,5,6; 7,8,9; 10,20,30; 40,50,60; 70,80,90'), 'matrix.operations.colconcat.1')

t(n.m_rowslice('1,2,3; 4,5,6', 0, 1), m('1;4'), 'matrix.operations.rowslice.1')

t(n.m_rowmap('1,2,3; 4,5,6', 1, lambda cell: cell * 5), m('5,10,15; 4,5,6'), 'matrix.operations.rowmap.1')
t(n.m_rowmap('1,2,3; 4,5,6', 1, lambda cell, j: j * 7), m('7,14,21; 4,5,6'), 'matrix.operations.rowmap.2')
t(n.m_cellmap('1,2,3; 4,5,6', lambda cell: cell * 5), m('5,10,15; 20,25,30'), 'matrix.operations.cellmap.1')

t(n.mi_gaussjordan('5,2,-4; 1,4,2; 2,3,6'), m('0.17,-0.23,0.19; -0.02,0.36,-0.13; -0.05,-0.10,0.17'), 'matrix.inverse.gaussjordan.1')

# Systems of Linear Equations
t(n.ls_gauss('3.6,2.4,-1.8; 4.2,-5.8,2.1; 0.8,3.5,6.5', '6.3; 7.5; 3.7'), m('1.81; 0.120; 0.281'), 'linearsystems.gauss.1')
t(n.ls_basic('-1,4,-3; 1,-1,4; 3,1,-2', '-8; 1; 9', '1;1;1', epsilon=0.001), m('3; -2; -1'), 'linearsystems.basic.1')
t(n.ls_gaussseidel('-1,4,-3; 1,-1,4; 3,1,-2', '-8; 1; 9', '1;1;1', epsilon=0.001), m('3; -2; -1'), 'linearsystems.gaussseidel.1')
t(n.ls_gaussseidel('2,1,4; 1,6,3; 5,-2,1', '14; 20; 8', '0; 0; 0', epsilon=0.09), m('2.05; 2.01; 1.97'), 'linearsystems.gaussseidel.2')

# Differentiation
t(n.diff_backward(fn5, 2), 2, 'differentiation.backward.1')
t(n.diff_backward(fn5, 5), 8, 'differentiation.backward.2')

finish()