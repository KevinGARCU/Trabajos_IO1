# -*- coding: utf-8 -*-
"""
Daniel Medina Sánchez – 20152020046
Anderson Jefrey López Jiménez -- 20162020424
Kevin Santiago García Cuellar -- 20181020074

"""

from sympy import symbols
from sympy import plot_implicit
from sympy import And


x, y = symbols('x, y')

print("EJERCICIOS METODO GRAFICO \n  ")

print("Ejercicio 1.\n 2x+y < 5")
plot_implicit(2*x + y < 5, (x, -8, 8), (y, -8, 8))

print("Ejercicio 2.\n y <= 5")
plot_implicit(y <= 5, (x, -8, 8), (y, -6, 8))

print("Ejercicio 3.\n 2(2x-y)<2(x+y)-4")
plot_implicit(2*x - 4*y < -4, (x, -8, 8), (y, -6, 8))

print("Ejercicio 4.\n 2x+y > 3 \n 2y-1 > 0 \n x >= y")
plot_implicit(And(2*x + y > 3, 2*y - 1 > 0, x >= y), (x, -8, 8), (y, -6, 8))

print("Ejercicio 5.\n 2x+3y <= 60 \n x >= 0 \n y >= 0")
plot_implicit(And(2*x + 3*y <= 60, x >= 0, y >= 0), (x, -10, 35), (y, -10, 25))