# Numerica
[![PyPI version](https://badge.fury.io/py/numerica.svg)](https://badge.fury.io/py/numerica)

My own experimental implementations of numerical methods as homework.

# Examples
    python3.8 -i test.py #includes all definitions

## Preparation
    import numerica as n
    from numerica import f, c

    fn1 = f([1, -6, 5]) # (x^2 - 6x + 5)^1
    fn2 = f([1, -6.5, 13.5, -9]) # (1x^3 - 6.5x^2 + 13.5x - 9)^1
    fn3 = f([1, -4, -4, 15]) # f = x^3 - 4x^2 - 4x + 15
    fn4 = f([1, 0, -20, 16]) # x^3 - 20x + 16
    fn5 = f([1, -2, -3]) # x^2 - 2x - 3

## Solving Nonlinear Equations
### Root Bracketing Methods
#### Graph Method
    root1 = n.graph(fn=fn1, dx=1, epsilon=0.001, x=0)
    root2 = n.graph(fn=fn1, dx=1, epsilon=0.001, x=2)

    print(root1, root2) # 1, 5

#### Bisection Method
    root1 = n.bisection(fn=fn2, epsilon=0.001, a=0, b=1.75)
    root2 = n.bisection(fn=fn2, epsilon=0.001, a=1.75, b=2.5)
    root3 = n.bisection(fn=fn2, epsilon=0.001, a=2.5, b=6)

    print(root1, root2, root3) # ~1.5, ~2, ~3

#### Regula-Falsi Method
    root1 = n.regulafalsi(fn=fn2, epsilon=0.001, a=0, b=1.75)
    root2 = n.regulafalsi(fn=fn2, epsilon=0.001, a=1.75, b=2.5)
    root3 = n.regulafalsi(fn=fn2, epsilon=0.001, a=2.5, b=6)

    print(root1, root2, root3) # ~1.5, ~2, ~3

### Iterative Methods
#### Basic Iteration
    # f = x^2 - 2x - 3
    # x0=4

    gx = f([1, 0]) # g(x) = x
    hx1 = f([2, 3], 1/2) # h(x) = (2x + 3)^(1/2)
    hx2 = c(f([3, 0]), f([1, -2], -1)) # h(x) = (3 / (x - 2))
    hx3 = c(f([1/2, 0]), f([1, 0, -3])) # h(x) = (x^2 - 3) / 2

    root1 = n.basic(gx, hx1, epsilon=0.005, x=4)
    root2 = n.basic(gx, hx2, epsilon=0.005, x=4)
    root3 = n.basic(gx, hx3, epsilon=0.005, x=4)

    print(root1, root2, root3) # ~3, ~-1, None

#### Newton-Raphson
    root1 = n.newtonraphson(fn3, epsilon=0.00005, x=-2.5)

    print(root1) # ~-2

#### Secant
    root1 = n.secant(fn4, epsilon=0.02, x0=3, x1=5)

    print(root1) # ~4

### Differentiation Methods
#### Backward Method
    # f  = x^2 - 2x - 3
    # f' = 2x - 2

    n.diff_backward(fn5, 2) # 2
    n.diff_backward(fn5, 5) # 8

# Resources
- YTU Numerical Analysis Lecture Notes
- https://mat.iitm.ac.in/home/sryedida/public_html/caimna/index1.html

# Testing Package
##### Test Directly as Script
    python3.8 -m numerica
##### or Install Package Locally (from repo root dir)
    pip3.8 install .
##### and Test It from REPL
    import numerica as n
    n.utils.function.f([1, -6, 5])(5) == 0
##### or Use test.py
    python3.8 -i test.py
    n.diff_backward(f([1, -2, -3]), 2) == 2

# Uploading to PyPI
##### Install Twine
    pip3.8 install twine
##### Build
    rm -rf build & rm -rf dist & rm -rf numerica.egg-info
    python3.8 setup.py sdist bdist_wheel
##### Upload
    twine upload dist/*