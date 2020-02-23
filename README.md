# Numerica
[![PyPI version](https://badge.fury.io/py/numerica.svg)](https://badge.fury.io/py/numerica)

My own experimental implementations of numerical methods as homework.

# Examples
## Solving Nonlinear Equations
### Graph Method
    import numerica as n

    fn = n.fnx(degree=2, coefficients=[5, -6, 1], baseExp=1) # (x^2 - 6x + 5)^1

    root1 = n.graph(fn=fn, dx=1, epsilon=0.1, x=0)
    root2 = n.graph(fn=fn, dx=1, epsilon=0.1, x=2)

    print(root1, root2) # 1, 5

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