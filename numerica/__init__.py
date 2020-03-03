from .utils import function
from .utils.function import f, c

from .nonlinear.bracketing.graph import graph
from .nonlinear.bracketing.bisection import bisection
from .nonlinear.bracketing.regulafalsi import regulafalsi
from .nonlinear.iterative.basic import basic
from .nonlinear.iterative.newtonraphson import newtonraphson
from .nonlinear.iterative.secant import secant

from .differentiation.backward import backward as diff_backward