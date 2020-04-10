# Numerica
[![PyPI version](https://badge.fury.io/py/numerica.svg)](https://badge.fury.io/py/numerica)

My own experimental implementations of numerical methods as homework.

# Table of Contents
  - [Usage](#usage)
    - [Importing](#importing)
    - [Function Definition](#function-definition)
    - [Matrix Definition](#matrix-definition)
  - [Examples](#examples)
    - [1- Solving Nonlinear Equations](#1--solving-nonlinear-equations)
      - [Root Bracketing Methods](#root-bracketing-methods)
        - [Graph Method](#graph-method)
        - [Bisection Method](#bisection-method)
        - [Regula-Falsi Method](#regula-falsi-method)
      - [Iterative Methods](#iterative-methods)
        - [Basic Iteration (Jacobi)](#basic-iteration-jacobi)
        - [Newton-Raphson](#newton-raphson)
        - [Secant](#secant)
    - [2- Matrix Operations](#2--matrix-operations)
      - [Basic Operations](#basic-operations)
        - [Definition](#matrix-definition)
        - [Creating an Identity Matrix by n](#identity-matrix)
        - [Getting Dimensions of a Matrix](#size-of-matrix)
        - [Transpose of a Matrix](#transpose-of-a-matrix)
      - [Finding Inverse of a Matrix](#finding-inverse-of-a-matrix)
        - [Gauss-Jordan Method](#gauss-jordan-method)
      - [Matrix Utils](#matrix-utils)
        - [Concat Matrices by Row (Horizontal)](#concat-matrices-by-row-horizontal)
        - [Concat Matrices by Column (Vertical)](#concat-matrices-by-column-vertical)
        - [Map a Row of Matrix](#map-a-row-of-matrix)
        - [Map all Matrix Cells](#map-all-matrix-cells)
        - [Is Matrix Check](#is-matrix-check)
        - [Slice Matrix Vertically](#slice-matrix-vertically)
    - [3- Solving Systems of Linear Equations](#3--solving-systems-of-linear-equations)
      - [Gauss Elimination](#gauss-elimination)
      - [Basic Iteration (Jacobi)](#basic-iteration-jacobi-1)
    - [4- Solving Systems of Nonlinear Equations](#4--solving-systems-of-nonlinear-equations)
    - [5- Numerical Integration](#5--numerical-integration)
    - [6- Numerical Differentiation](#6--numerical-differentiation)
      - [Backward Method](#backward-method)
    - [7- Finite Differences](#7--finite-differences)
    - [8- Interpolation](#8--interpolation)
  - [Resources](#resources)
  - [Testing Package](#testing-package)
  - [Uploading to PyPI](#uploading-to-pypi)

# Usage
    python3.8 -i test.py #includes all definitions and tests

## Importing
    import numerica as n
    from numerica import f, c // function definition & composition
    from numerica import m // matrix definition

## Function Definition
    fn1 = f([1, -6, 5]) # (x^2 - 6x + 5)^1
    fn2 = f([1, -6.5, 13.5, -9]) # (1x^3 - 6.5x^2 + 13.5x - 9)^1
    fn3 = f([1, -4, -4, 15]) # f = x^3 - 4x^2 - 4x + 15
    fn4 = f([1, 0, -20, 16]) # x^3 - 20x + 16
    fn5 = f([1, -2, -3]) # x^2 - 2x - 3

## Matrix Definition
    m1 = m('1,2,3; 4,5,6; 7,8,9');

# Examples
## 1- Solving Nonlinear Equations
### Root Bracketing Methods
#### Graph Method
    root1 = n.nl_graph(fn=fn1, dx=1, epsilon=0.001, x=0)
    root2 = n.nl_graph(fn=fn1, dx=1, epsilon=0.001, x=2)

    print(root1, root2) # 1, 5

#### Bisection Method
    root1 = n.nl_bisection(fn=fn2, epsilon=0.001, a=0, b=1.75)
    root2 = n.nl_bisection(fn=fn2, epsilon=0.001, a=1.75, b=2.5)
    root3 = n.nl_bisection(fn=fn2, epsilon=0.001, a=2.5, b=6)

    print(root1, root2, root3) # ~1.5, ~2, ~3

#### Regula-Falsi Method
    root1 = n.nl_regulafalsi(fn=fn2, epsilon=0.001, a=0, b=1.75)
    root2 = n.nl_regulafalsi(fn=fn2, epsilon=0.001, a=1.75, b=2.5)
    root3 = n.nl_regulafalsi(fn=fn2, epsilon=0.001, a=2.5, b=6)

    print(root1, root2, root3) # ~1.5, ~2, ~3

### Iterative Methods
#### Basic Iteration (Jacobi)
    # f = x^2 - 2x - 3
    # x0=4

    gx = f([1, 0]) # g(x) = x
    hx1 = f([2, 3], 1/2) # h(x) = (2x + 3)^(1/2)
    hx2 = c(f([3, 0]), f([1, -2], -1)) # h(x) = (3 / (x - 2))
    hx3 = c(f([1/2, 0]), f([1, 0, -3])) # h(x) = (x^2 - 3) / 2

    root1 = n.nl_basic(gx, hx1, epsilon=0.005, x=4)
    root2 = n.nl_basic(gx, hx2, epsilon=0.005, x=4)
    root3 = n.nl_basic(gx, hx3, epsilon=0.005, x=4)

    print(root1, root2, root3) # ~3, ~-1, None

#### Newton-Raphson
    root1 = n.nl_newtonraphson(fn3, epsilon=0.00005, x=-2.5)

    print(root1) # ~-2

#### Secant
    root1 = n.nl_secant(fn4, epsilon=0.02, x0=3, x1=5)

    print(root1) # ~4

## 2- Matrix Operations
### Basic Operations
#### Matrix Definition
    m1 = m('1,2,3; 4,5,6; 7,8,9')
    m2 = m('10,20,30; 40,50,60; 70,80,90')

#### Identity Matrix
    mid1 = n.m_id(1) // [[1]]
    mid2 = n.m_id(3) // [[1,0,0], [0,1,0], [0,0,1]]

#### Size of Matrix
    (m, n) = n.m_size(m1) // (3, 3)

#### Transpose of a Matrix
    n.m_transpose(m1) // transpose of m1

### Finding Inverse of a Matrix
#### Gauss-Jordan Method
    m3 = m('5, 2, -4; 1, 4, 2; 2, 3, 6');
    n.mi_gaussjordan(m3); // inverse of m3

### Matrix Utils
#### Concat Matrices by Row (Horizontal)
    n.m_rowconcat(m1, m2) // '1,2,3,10,20,30; 4,5,6,40,50,60; 7,8,9,70,80,90'

#### Concat Matrices by Column (Vertical)
    n.m_colconcat(m1, m2) // '1,2,3; 4,5,6; 7,8,9; 10,20,30; 40,50,60; 70,80,90'

#### Map a Row of Matrix
    n.m_rowmap('1,2,3; 4,5,6', 1, lambda cell: cell * 5) // '5,10,15; 4,5,6'

#### Map all Matrix Cells
    n.m_cellmap('1,2,3; 4,5,6', lambda cell: cell * 5) // '5,10,15; 20,25,30'

#### Is Matrix Check
    n.is_matrix([[1]]) // True

#### Slice Matrix Vertically
    n.m_rowslice('1,2,3; 4,5,6', 0, 1) // '1;4'

## 3- Solving Systems of Linear Equations
### Gauss Elimination
    n.ls_gauss('3.6,2.4,-1.8; 4.2,-5.8,2.1; 0.8,3.5,6.5', '6.3; 7.5; 3.7') // '1.81; 0.120; 0.281'

### Basic Iteration (Jacobi)
    n.ls_basic('-1,4,-3; 1,-1,4; 3,1,-2', '-8; 1; 9', '1;1;1', epsilon=0.001) // '3; -2; -1'

## 4- Solving Systems of Nonlinear Equations
## 5- Numerical Integration

## 6- Numerical Differentiation
#### Backward Method
    # f  = x^2 - 2x - 3
    # f' = 2x - 2

    n.diff_backward(fn5, 2) # 2
    n.diff_backward(fn5, 5) # 8

## 7- Finite Differences
## 8- Interpolation

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
##### or Use test.py Interactively
    python3.8 -i test.py
    n.diff_backward(f([1, -2, -3]), 2) == 2
##### or Just Test and Exit
    python3.8 test.py

# Uploading to PyPI
##### Install Twine
    pip3.8 install twine
##### Build
    rm -rf build & rm -rf dist & rm -rf numerica.egg-info
    python3.8 setup.py sdist bdist_wheel
##### Upload
    twine upload dist/*