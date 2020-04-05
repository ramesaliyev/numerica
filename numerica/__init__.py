from .utils import function
from .utils.function import f, c

from .nonlinear.bracketing.graph import graph
from .nonlinear.bracketing.bisection import bisection
from .nonlinear.bracketing.regulafalsi import regulafalsi
from .nonlinear.iterative.basic import basic
from .nonlinear.iterative.newtonraphson import newtonraphson
from .nonlinear.iterative.secant import secant

from .matrix.define import m
from .matrix.operations import identity as m_id
from .matrix.operations import size as m_size
from .matrix.operations import transpose as m_transpose
from .matrix.operations import concat as m_concat
from .matrix.operations import concat_v as m_concat_v
from .matrix.inverse.gaussjordan import gaussjordan as mi_gaussjordan

from .differentiation.backward import backward as diff_backward