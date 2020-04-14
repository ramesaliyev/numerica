# Numerica
[![PyPI version](https://badge.fury.io/py/numerica.svg)](https://badge.fury.io/py/numerica)

My own experimental implementations of numerical methods as homework.<br />
Use [documentation](#documentation) to see how to use, and check [test.py](./test.py) for real examples.

# Table of Contents
  - [Usage](#usage)
    - [Importing](#importing)
    - [Function Definition](#function-definition)
    - [Matrix Definition](#matrix-definition)
  - [Documentation](#documentation)
    - [1- Solving Nonlinear Equations](#1--solving-nonlinear-equations)
      - [Root Bracketing Methods](#root-bracketing-methods)
        - [Graph](#graph)
        - [Bisection](#bisection)
        - [Regula-Falsi](#regula-falsi)
      - [Iterative Methods](#iterative-methods)
        - [Fixed-Point Iteration](#fixed-point-iteration)
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
      - [Jacobi](#jacobi)
      - [Gauss-Seidel](#gauss-seidel)
    - [4- Solving Systems of Nonlinear Equations](#4--solving-systems-of-nonlinear-equations)
    - [5- Numerical Integration](#5--numerical-integration)
      - [Trapezoidal](#trapezoidal)
      - [Simpson](#simpson)
    - [6- Numerical Differentiation](#6--numerical-differentiation)
      - [Euler Methods](#euler-methods)
        - [Backward](#backward)
        - [Forward](#forward)
        - [Midpoint](#midpoint)
    - [7- Finite Differences](#7--finite-differences)
        - [Determine  Degree of a Polynomial](#determine-degree-of-a-polynomial)
    - [8- Interpolation](#8--interpolation)
      - [Lagrange](#lagrange)
    - [9- Regression](#9--regression)
      - [Least Squares](#least-squares)
  - [Resources](#resources)
  - [Testing Package](#testing-package)
  - [Uploading to PyPI](#uploading-to-pypi)

# Usage
**python >= 3.8 is required**

## Importing
    import numerica as n
    from numerica import f // function definition
    from numerica import m // matrix definition

## Function Definition
    f('expression')

    fx = f('3x^2 + 2x + 3')
    fx(2)

## Matrix Definition
    m(
        a11, a12, a13;
        a21, a22, a23;
        a31, a32, a33
    )

    matrix = m('1,2,3; 4,5,6; 7,8,9');

# Documentation
## 1- Solving Nonlinear Equations
### Root Bracketing Methods
#### Graph
    n.nl_graph(fx, dx, epsilon, x)

#### Bisection
    n.nl_bisection(fx, epsilon, a, b)

#### Regula-Falsi
    n.nl_regulafalsi(fx, epsilon, a, b)

### Iterative Methods
#### Fixed-Point Iteration
    n.nl_fixedpoint(hx, epsilon, x)

#### Newton-Raphson
    n.nl_newtonraphson(fx, epsilon, x)

#### Secant
    n.nl_secant(fx, epsilon, x0, x1)

## 2- Matrix Operations
### Basic Operations
#### Matrix Definition
    m(
        a11, a12, a13;
        a21, a22, a23;
        a31, a32, a33
    )

#### Identity Matrix
    n.m_id(n)

#### Size of Matrix
    (m, n) = n.m_size(A)

#### Transpose of a Matrix
    n.m_transpose(A)

### Finding Inverse of a Matrix
#### Gauss-Jordan Method
    n.mi_gaussjordan(A)

### Matrix Utils
#### Concat Matrices by Row (Horizontal)
    n.m_rowconcat(A, B)

#### Concat Matrices by Column (Vertical)
    n.m_colconcat(A, B)

#### Map a Row of Matrix
    n.m_rowmap(A, i, iteratee)

#### Map all Matrix Cells
    n.m_cellmap(A, iteratee)

#### Is Matrix Check
    n.is_matrix(A)

#### Slice Matrix Vertically
    n.m_rowslice(A, start, stop, step)

## 3- Solving Systems of Linear Equations
### Gauss Elimination
    n.ls_gauss(A, C)

### Jacobi
    n.ls_jacobi(A, C, X, epsilon=0.001)

### Gauss-Seidel
    n.ls_gaussseidel(A, C, X, epsilon=0.001)

## 4- Solving Systems of Nonlinear Equations
## 5- Numerical Integration
### Trapezoidal
    n.itg_trapezoidal(fx, x0, xn, n)

### Simpson
    n.itg_simpson(fx, x0, xn, n)

## 6- Numerical Differentiation
### Euler Methods
#### Backward
    n.diff_backward(fx, x)

#### Forward
    n.diff_forward(fx, x)

#### Midpoint
    n.diff_midpoint(fx, x)

## 7- Finite Differences
### Determine Degree of a Polynomial
    n.fd_degree(pair_tuples)
    n.fd_degree([(x0,y0), (x1,y1), (x2,y3), ...])

## 8- Interpolation
### Lagrange
    n.itp_lagrange(pair_tuples)
    n.itp_lagrange([(x0,y0), (x1,y1), (x2,y3), ...], x)

## 9- Regression
### Least Squares
    n.reg_leastsquares(pair_tuples)
    n.reg_leastsquares([(x0,y0), (x1,y1), (x2,y3), ...], x, deg)

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
    # ...
##### or Use test.py Interactively
    python3.8 -i test.py
    # ...
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