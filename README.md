# Numerica
[![PyPI version](https://badge.fury.io/py/numerica.svg)](https://badge.fury.io/py/numerica)

My own experimental implementations of numerical methods as homework.

# Examples
    python3.8 -i test.py

## Preparation
    import numerica as n

    fn1 = n.fnx(degree=2, coefficients=[1, -6, 5], baseExp=1) # (x^2 - 6x + 5)^1
    fn2 = n.fnx(degree=3, coefficients=[1, -6.5, 13.5, -9], baseExp=1) # (1x^3 - 6.5x^2 + 13.5x - 9)^1

## Solving Nonlinear Equations
### Root Bracketing Methods
#### Graph Method
    root1 = n.graph(fn=fn1, dx=1, epsilon=0.01, x=0)
    root2 = n.graph(fn=fn1, dx=1, epsilon=0.01, x=2)

    print(root1, root2) # 1, 5

#### Bisection Method
    root1 = n.bisection(fn=fn2, epsilon=0.01, a=0, b=1.9)
    root2 = n.bisection(fn=fn2, epsilon=0.01, a=1.7, b=2.9)
    root3 = n.bisection(fn=fn2, epsilon=0.01, a=2.5, b=6)

    print(root1, root2, root3) # 1.5, 2, 3

#### Regula-Falsi Method
    root1 = n.regulafalsi(fn=fn2, epsilon=0.001, a=0, b=1.75)
    root2 = n.regulafalsi(fn=fn2, epsilon=0.001, a=1.75, b=2.75)
    root3 = n.regulafalsi(fn=fn2, epsilon=0.001, a=2.50, b=3.5)

    print(root1, root2, root3) # 1.5, 2, 3

### Iterative Methods
#### Fixed-Point Iteration


# Resources
- YTU Numerical Analysis Lecture Notes
- https://mat.iitm.ac.in/home/sryedida/public_html/caimna/content1.html

# Testing Package
##### Test Directly as Script
    python3.8 -m numerica
##### or Install Local Package
    pip3.8 install .
##### and Test It from REPL
    import numerica
    numerica.utils.function.fnx(2, [5, -6, 1], 1, 5) == 0

# Uploading to PyPI
##### Install Twine
    pip3.8 install twine
##### Build
    rm -rf build & rm -rf dist & rm -rf numerica.egg-info
    python3.8 setup.py sdist bdist_wheel
##### Upload
    twine upload dist/*