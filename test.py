import numerica as n

from numerica import fn
from numerica import m

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
t(fn('5')(0), 5, 'utils.function.fn.1')
t(fn('x')(3), 3, 'utils.function.fn.2')
t(fn('4x')(7), 28, 'utils.function.fn.3')
t(fn('x + 7')(4), 11, 'utils.function.fn.4')
t(fn('2x + 3')(4), 11, 'utils.function.fn.5')
t(fn('3x^2 + x + 7')(4), 59, 'utils.function.fn.6')
t(fn('3x^2 + 2x + 3')(2), 19, 'utils.function.fn.7')
t(fn('2x^2 + 3x + 5')(x=1), 10, 'utils.function.fn.8')
t(fn('x + y')(3, y=3), 6, 'utils.function.fn.9')
t(fn('2x^2 + 3x + 3y^2 + 5y')(x=2, y=3), 56, 'utils.function.fn.10')
t(fn('y + 20')(y=5), 25, 'utils.function.fn.11')
t(fn('(x)')(x=5), 5, 'utils.function.fn.12')
t(fn('(x + 5) * (x + 2)')(x=3), 40, 'utils.function.fn.13')
t(fn('x^3 - 4x^2 - 4x + 15')(x=-3), -36, 'utils.function.fn.14')

t(list(n.permutation([1,2])), [[1,2], [2,1]], 'utils.math.permutation.1')
t(list(n.permutation([1,2,3])), [[1,2,3], [2,1,3], [2,3,1], [1,3,2], [3,1,2], [3,2,1]], 'utils.math.permutation.2')

t(n.polynomial([3], 5), 3, 'utils.math.polynomial.1')
t(n.polynomial([1, 0], 5), 5, 'utils.math.polynomial.2')
t(n.polynomial([1, 3], 5), 8, 'utils.math.polynomial.3')
t(n.polynomial([2, 1, 3], 5), 58, 'utils.math.polynomial.4')

# Nonlinear
t(n.nl_graph(fn=fn('x^2 - 6x + 5'), dx=1, epsilon=0.001, x=0), 1, 'nonlinear.bracketing.graph.1')
t(n.nl_graph(fn=fn('x^2 - 6x + 5'), dx=1, epsilon=0.001, x=2), 5, 'nonlinear.bracketing.graph.2')

t(n.nl_bisection(fn=fn('x^3 - 6.5x^2 + 13.5x - 9'), epsilon=0.001, a=0, b=1.75), 1.5, 'nonlinear.bracketing.bisection.1')
t(n.nl_bisection(fn=fn('x^3 - 6.5x^2 + 13.5x - 9'), epsilon=0.001, a=1.75, b=2.5), 2, 'nonlinear.bracketing.bisection.2')
t(n.nl_bisection(fn=fn('x^3 - 6.5x^2 + 13.5x - 9'), epsilon=0.001, a=2.5, b=6), 3, 'nonlinear.bracketing.bisection.3')

t(n.nl_regulafalsi(fn=fn('x^3 - 6.5x^2 + 13.5x - 9'), epsilon=0.001, a=0, b=1.75), 1.5, 'nonlinear.bracketing.regulafalsi.1')
t(n.nl_regulafalsi(fn=fn('x^3 - 6.5x^2 + 13.5x - 9'), epsilon=0.001, a=1.75, b=2.5), 2, 'nonlinear.bracketing.regulafalsi.2')
t(n.nl_regulafalsi(fn=fn('x^3 - 6.5x^2 + 13.5x - 9'), epsilon=0.001, a=2.5, b=6), 3, 'nonlinear.bracketing.regulafalsi.3')

t(n.nl_fixedpoint(fn('x'), fn('(2x + 3)^(1/2)'), epsilon=0.005, x=4), 3, 'nonlinear.iterative.fixedpoint.1')
t(n.nl_fixedpoint(fn('x'), fn('(3 / (x - 2))'), epsilon=0.005, x=4), -1, 'nonlinear.iterative.fixedpoint.2')
t(n.nl_fixedpoint(fn('x'), fn('(x^2 - 3) / 2'), epsilon=0.005, x=4), None, 'nonlinear.iterative.fixedpoint.3')

t(n.nl_newtonraphson(fn('x^3 - 4x^2 - 4x + 15'), epsilon=0.00005, x=-2.5), -2, 'nonlinear.iterative.newtonraphson.1')

t(n.nl_secant(fn('x^3 - 20x + 16'), epsilon=0.02, x0=3, x1=5), 4, 'nonlinear.iterative.secant.1')

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
t(n.ls_jacobi('-1,4,-3; 1,-1,4; 3,1,-2', '-8; 1; 9', '1;1;1', epsilon=0.001), m('3; -2; -1'), 'linearsystems.jacobi.1')
t(n.ls_gaussseidel('-1,4,-3; 1,-1,4; 3,1,-2', '-8; 1; 9', '1;1;1', epsilon=0.001), m('3; -2; -1'), 'linearsystems.gaussseidel.1')
t(n.ls_gaussseidel('2,1,4; 1,6,3; 5,-2,1', '14; 20; 8', '0; 0; 0', epsilon=0.09), m('2.05; 2.01; 1.97'), 'linearsystems.gaussseidel.2')

# Integration
t(n.itg_trapezoidal(fn('1 / (1 + x^2)'), 0, 1, 4), 0.78, 'integration.trapezoidal.1')
t(n.itg_trapezoidal(fn('x^3 + 2x^2 - x - 2'), -2, -1, 4), 0.39, 'integration.trapezoidal.2')
t(n.itg_simpson(fn('x^3'), 0, 2, 4), 4, 'integration.simpson.1')
t(n.itg_simpson(fn('x^3'), -1, 0, 4), -0.25, 'integration.simpson.2')
t(n.itg_simpson(fn('x^3 + 2x^2 - x - 2'), -2, -1, 4), 0.41, 'integration.simpson.3')

# Differentiation
t(n.diff_backward(fn('x^2 - 2x - 3'), 2), 2, 'differentiation.euler.backward.1')
t(n.diff_backward(fn('x^2 - 2x - 3'), 5), 8, 'differentiation.euler.backward.2')
t(n.diff_forward(fn('x^2 - 2x - 3'), 2), 2, 'differentiation.euler.forward.1')
t(n.diff_forward(fn('x^2 - 2x - 3'), 5), 8, 'differentiation.euler.forward.2')
t(n.diff_midpoint(fn('x^2 - 2x - 3'), 2), 2, 'differentiation.euler.midpoint.1')
t(n.diff_midpoint(fn('x^2 - 2x - 3'), 5), 8, 'differentiation.euler.midpoint.2')

# Finite differences
t(n.fd_degree([(0,0),(1,1),(2,2),(3,3)]), 1, 'finitedifferences.degree.1')
t(n.fd_degree([(-3,-18),(-2,-2),(-1,2),(0,0),(1,-2),(2,2)]), 3, 'finitedifferences.degree.2')
t(n.fd_degree([(0,8),(1,22),(2,134),(3,560),(4,1660)]), 4, 'finitedifferences.degree.3')
t(n.fd_degree([(0,8),(1,13),(2,40),(3,107),(4,232),(5,433)]), 3, 'finitedifferences.degree.4')

# Interpolation
t(n.itp_lagrange([(0,-5),(1,1),(3,25)], 1), 1, 'interpolation.lagrange.1')
t(n.itp_lagrange([(0,-5),(1,1),(3,25)], 2), 11, 'interpolation.lagrange.2')
t(n.itp_lagrange([(0,8),(1,22),(2,134),(3,560),(4,1660)], 2.5), 288.625, 'interpolation.lagrange.3')
t(n.itp_lagrange([(0,8),(1,13),(2,40),(3,107),(4,232),(5,433)], 3.25), 132.1, 'interpolation.lagrange.4')

# Regression
t(n.reg_leastsquares([(0,1),(2,5.1),(4,9),(6,13),(8,17),(10,21)], 6, 1), 8.2, 'regression.leastsquares.1')
t(n.reg_leastsquares([(0,0),(2,8),(3,10),(4,14),(5,17),(7,22),(8,26),(9,29),(10,32),(12,35)], 6, 1), 11.9, 'regression.leastsquares.2')
t(n.reg_leastsquares([(2,1),(3,6),(5,22),(6,33),(8,61)], 6, 2), -107, 'regression.leastsquares.3')
t(n.reg_leastsquares([(0,8),(1,22),(2,134),(3,560),(4,1660),(5,3938),(6,8042),(7,14764)], 17), 675110, 'regression.leastsquares.4')

# finish
finish()