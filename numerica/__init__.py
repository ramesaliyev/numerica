from .utils import function
from .utils.function import f
from .utils.math import permutation, polynomial

from .nonlinear.bracketing.graph import graph as nl_graph
from .nonlinear.bracketing.bisection import bisection as nl_bisection
from .nonlinear.bracketing.regulafalsi import regulafalsi as nl_regulafalsi
from .nonlinear.iterative.fixedpoint import fixedpoint as nl_fixedpoint
from .nonlinear.iterative.newtonraphson import newtonraphson as nl_newtonraphson
from .nonlinear.iterative.secant import secant as nl_secant

from .matrix.define import m
from .matrix.define import is_matrix
from .matrix.operations import identity as m_id
from .matrix.operations import size as m_size
from .matrix.operations import transpose as m_transpose
from .matrix.operations import rowconcat as m_rowconcat
from .matrix.operations import colconcat as m_colconcat
from .matrix.operations import rowslice as m_rowslice
from .matrix.operations import rowmap as m_rowmap
from .matrix.operations import cellmap as m_cellmap
from .matrix.inverse.gaussjordan import gaussjordan as mi_gaussjordan

from .linear_systems.gauss import gauss as ls_gauss
from .linear_systems.jacobi import jacobi as ls_jacobi
from .linear_systems.gaussseidel import gaussseidel as ls_gaussseidel

from .differentiation.euler.backward import backward as diff_backward
from .differentiation.euler.forward import forward as diff_forward
from .differentiation.euler.midpoint import midpoint as diff_midpoint

from .integration.trapezoidal import trapezoidal as itg_trapezoidal
from .integration.simpson import simpson as itg_simpson

from .finite_differences.degree import degree as fd_degree

from .interpolation.lagrange import lagrange as itp_lagrange

from .regression.leastsquares import leastsquares as reg_leastsquares