# 🔢 Numerical Methods in Python

A comprehensive collection of **Numerical Methods** implemented in Python, covering root-finding, linear systems, eigenvalue problems, interpolation, curve fitting, numerical integration, and ODE solving. Each script is interactive — it prompts the user for input at runtime and visualizes results using Matplotlib where applicable.

---

## 📁 Project Structure

```
Numercal-Methods-main/
│
├── Root Finding
│   ├── bisection.py
│   ├── regula-falsi.py
│   ├── newton-raphson.py
│   └── secant.py
│
├── Linear Systems
│   ├── gauss-elimination.py
│   ├── gauss-jordan.py
│   ├── gauss-jordanPartialPivot.py
│   ├── gauss-seidal.py
│   └── LU-decomposition.py
│
├── Eigenvalue Problems
│   ├── power-method.py
│   └── inverse-power-method.py
│
├── Interpolation & Curve Fitting
│   ├── lagrange-interpolation.py
│   └── least-square-method.py
│
├── Numerical Integration
│   ├── trapezoidal-method.py
│   ├── simpson-one-third.py
│   └── simpson-three-eight.py
│
└── ODE Solvers
    ├── eulerMethod.py
    ├── modifiedEuler.py
    └── RK4.py
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.x** installed along with the following libraries:

```bash
pip install numpy scipy sympy pandas matplotlib
```

### Running a Script

All scripts are interactive. Simply run them from your terminal:

```bash
python bisection.py
```

Each script will prompt you for the required inputs (equation, initial guesses, tolerances, etc.).

---

## 📘 Methods Description

---

### 🔍 Root Finding

#### 1. Bisection Method — `bisection.py`
Finds a real root of a nonlinear equation f(x) = 0 by repeatedly halving the interval [a, b] where the sign of f changes.

- **Inputs:** Equation in x, two initial guesses (a, b), error tolerance, max iterations
- **Output:** Approximate root with iteration table and a plot of f(x) with midpoints labeled
- **Example:** `x**2 - np.cos(x)`

#### 2. Regula-Falsi Method — `regula-falsi.py`
Also called the *False Position* method. Improves on bisection by using the secant line between (a, f(a)) and (b, f(b)) to estimate the root.

- **Inputs:** Equation in x, two initial guesses, error tolerance, max iterations
- **Output:** Iteration table, root, and a labeled plot
- **Example:** `x**2 - np.cos(x)`

#### 3. Newton-Raphson Method — `newton-raphson.py`
Uses the tangent line to the curve at a guessed point to converge quickly to the root. The derivative is computed numerically using a finite difference.

- **Inputs:** Equation in x, initial guess, error tolerance, max iterations
- **Output:** Iteration table (x, f(x), f'(x), next estimate, error) and a plot

#### 4. Secant Method — `secant.py`
Similar to Newton-Raphson but uses two points instead of a derivative, making it derivative-free.

- **Inputs:** Equation in x, two initial guesses (a, b), error tolerance, max iterations
- **Output:** Iteration table and a labeled plot of successive approximations

---

### 🔢 Linear Systems

#### 5. Gauss Elimination — `gauss-elimination.py`
Solves a system of n linear equations using forward elimination with partial pivoting, followed by back substitution.

- **Inputs:** Number of variables, augmented matrix coefficients (row by row)
- **Output:** Step-by-step matrix after each elimination, and the final solution vector x

#### 6. Gauss-Jordan Method — `gauss-jordan.py`
Extends Gauss Elimination to full row-reduction (reduced row echelon form), eliminating the need for back substitution.

- **Inputs:** Number of variables, augmented matrix
- **Output:** Row operations displayed at each step, solution vector x

#### 7. Gauss-Jordan with Partial Pivoting — `gauss-jordanPartialPivot.py`
A variant of Gauss-Jordan that applies partial pivoting for numerical stability.

- **Inputs:** Number of variables, augmented matrix (space-separated rows)
- **Output:** Reduced matrix and solution vector

#### 8. Gauss-Seidel Iterative Method — `gauss-seidal.py`
An iterative method for solving diagonally dominant systems of linear equations. Updates each variable using the most recent values within the same iteration.

- **Inputs:** Number of variables, augmented matrix, initial guesses (x₁, x₂, ..., xₙ), tolerance, max iterations
- **Output:** Iteration table and final solution values

#### 9. LU Decomposition — `LU-decomposition.py`
Decomposes matrix A into lower (L) and upper (U) triangular matrices using SciPy, then solves Ax = B via forward and back substitution.

- **Inputs:** Number of variables, coefficient matrix A, constants vector B
- **Output:** L, U, P matrices and the solution vector x

---

### 📐 Eigenvalue Problems

#### 10. Power Method — `power-method.py`
Finds the **dominant (largest) eigenvalue** and its corresponding eigenvector by repeated matrix-vector multiplication.

- **Inputs:** Matrix order, matrix entries (row by row), initial vector, tolerance, max iterations
- **Output:** Iteration table with eigenvalue and eigenvector evolution, final dominant eigenvalue

#### 11. Inverse Power Method — `inverse-power-method.py`
Finds the **least (smallest) eigenvalue** and its corresponding eigenvector by applying the Power Method to the inverse of the matrix.

- **Inputs:** Matrix order, matrix entries, initial vector, tolerance, max iterations
- **Output:** Iteration table, least eigenvalue (as reciprocal of max of A⁻¹), eigenvector

---

### 📈 Interpolation & Curve Fitting

#### 12. Lagrange Interpolation — `lagrange-interpolation.py`
Constructs a polynomial passing through all given data points using the Lagrange basis formulation, then evaluates it at a specified point.

- **Inputs:** Number of data points, x-values, y-values, interpolation point
- **Output:** Symbolic Lagrange polynomial, interpolated value, and a plot

#### 13. Least Square Method — `least-square-method.py`
Fits a **second-degree polynomial** (y = a + bx + cx²) to a set of data points by solving the system of normal equations derived from minimizing the sum of squared errors.

- **Inputs:** Number of data points, x-values, y-values
- **Output:** Coefficient matrix, best-fit curve equation, and a plot
- **Example data:** x = [1 2 3 4 5], y = [1090 1220 1390 1625 1925]

---

### ∫ Numerical Integration

#### 14. Trapezoidal Method — `trapezoidal-method.py`
Approximates the definite integral ∫f(x)dx over [a, b] by summing the areas of trapezoids under the curve.

- **Inputs:** Lower limit a, upper limit b, number of partitions n, integrand function in x
- **Output:** Approximate integral value and a shaded area plot

#### 15. Simpson's 1/3 Rule — `simpson-one-third.py`
A more accurate integration formula based on fitting parabolas through successive pairs of sub-intervals. Requires n to be a multiple of 2.

- **Inputs:** Lower limit, upper limit, number of partitions (even), integrand function
- **Output:** Approximate integral and a shaded plot (pink panels for each parabolic segment)

#### 16. Simpson's 3/8 Rule — `simpson-three-eight.py`
Uses cubic polynomial fitting over groups of 3 sub-intervals. Requires n to be a multiple of 3.

- **Inputs:** Lower limit, upper limit, number of partitions (multiple of 3), integrand function
- **Output:** Approximate integral and shaded plot

---

### 🧮 ODE Solvers (Initial Value Problems)

All ODE solvers handle first-order IVPs of the form dy/dx = f(x, y), y(x₀) = y₀.

#### 17. Euler's Method — `eulerMethod.py`
The simplest ODE solver. Uses the slope at the current point to step forward.

- **Inputs:** ODE expression, initial x, initial y, step size h, number of steps
- **Output:** Table of (x, y) values and a line plot

#### 18. Modified Euler's Method (Heun's Method) — `modifiedEuler.py`
Improves accuracy over standard Euler by using a predictor-corrector approach: predict with Euler, then correct using the average of slopes at both ends.

- **Inputs:** ODE expression, initial conditions, step size h, number of steps
- **Output:** Table of (x, y) values and a line plot

#### 19. Runge-Kutta 4th Order (RK4) — `RK4.py`
The most widely used ODE solver. Computes four slope estimates per step (k1, k2, k3, k4) and combines them for high accuracy.

- **Inputs:** ODE expression, initial x, initial y, step size h, number of steps
- **Output:** Table of (x, y) values and a line plot

---

## 🛠️ Dependencies

| Library      | Purpose                                       |
|-------------|-----------------------------------------------|
| `numpy`     | Array operations, matrix math                 |
| `scipy`     | LU decomposition (`scipy.linalg`)             |
| `sympy`     | Symbolic math (Lagrange polynomial)           |
| `pandas`    | Tabular display of iteration results          |
| `matplotlib`| Plotting and visualization                    |

Install all at once:

```bash
pip install numpy scipy sympy pandas matplotlib
```

---

## 📌 Notes

- All equations must be entered using **Python math syntax** (e.g., `x**2 - np.cos(x)` instead of `x² - cos(x)`).
- For ODE methods, enter dy/dx as a Python expression in terms of `x` and `y` (e.g., `x + y`, `x**2 - y`).
- Gauss-Seidel converges best for **diagonally dominant** systems.
- Simpson methods require the number of partitions to be a specific multiple (2 or 3 respectively).
- The Inverse Power Method requires the matrix to be **non-singular** (invertible).

---

## 👨‍💻 Author

This project is a lab report submission for a **Numerical Methods** course, implemented in Python.

---

## 📄 License

This project is for educational purposes. Feel free to use, modify, and distribute it for learning.
