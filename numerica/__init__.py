from .utils import function
from .utils.function import f, c

from .nonlinear.bracketing.graph import graph as nl_graph
from .nonlinear.bracketing.bisection import bisection as nl_bisection
from .nonlinear.bracketing.regulafalsi import regulafalsi as nl_regulafalsi
from .nonlinear.iterative.basic import basic as nl_basic
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

from .differentiation.backward import backward as diff_backward