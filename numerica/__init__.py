from .utils import function
from .utils.function import f, c

from .nonlinear.bracketing.graph import graph
from .nonlinear.bracketing.bisection import bisection
from .nonlinear.bracketing.regulafalsi import regulafalsi
from .nonlinear.iterative.basic import basic
from .nonlinear.iterative.newtonraphson import newtonraphson
from .nonlinear.iterative.secant import secant

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

from .differentiation.backward import backward as diff_backward