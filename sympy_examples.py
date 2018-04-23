# Welcome to my VERY brief tutoring for SymPy

#This code solves for square roots
import math
import sympy as sp
sp.init_printing(use_unicode=True)

print('Square root of 9 =',math.sqrt(9))
print('Square root of 8 =',math.sqrt(8))
print('Square root of 8 =',sp.sqrt(8))
sp.pprint(sp.sqrt(8))
print('')









# pretty-print an integral
x = sp.Symbol('x')
sp.pprint(sp.Integral(x**2, x), use_unicode=True)
print('')


#This code solves the quadratic equation: x^2 - 1 = 0

from sympy.solvers import solve
y = sp.Symbol('y')
A = solve(y**2 - 1, y)
sp.pprint(A)
print('')



# Solve diff eq: f(x)''+ 9*f(x)=0
from sympy import Function, dsolve, Eq, Derivative, sin, cos, symbols
f = Function('f')
B = dsolve(Derivative(f(x), x, x) + 9*f(x), f(x))
sp.pprint(B)
