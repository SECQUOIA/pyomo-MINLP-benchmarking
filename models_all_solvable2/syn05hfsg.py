# MINLP written by GAMS Convert at 05/07/21 17:13:04
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#        58       30        3       25        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        42       37        5        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       127      118        9
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x2 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x3 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x4 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x5 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x6 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x7 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x8 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x9 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x10 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x11 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x12 = Var(within=Reals, bounds=(0,7), initialize=0)
m.x13 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x14 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x15 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x16 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x17 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x18 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x19 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x20 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x21 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x22 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x23 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x24 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x25 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x26 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x27 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x28 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x29 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x30 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x31 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x32 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x33 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x34 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x35 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x36 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x37 = Var(within=Reals, bounds=(0,None), initialize=0)
m.b38 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b39 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b40 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b41 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b42 = Var(within=Binary, bounds=(0,1), initialize=0)

m.obj = Objective(sense=maximize, expr= 5 * m.x7 - 2 * m.x12 + 200 * m.x13 +
    250 * m.x14 + 300 * m.x15 - 5 * m.b38 - 8 * m.b39 - 6 * m.b40 - 10 * m.b41
    - 6 * m.b42)

m.e1 = Constraint(expr= m.x1 - m.x2 - m.x3 == 0)
m.e2 = Constraint(expr= -m.x4 - m.x5 + m.x6 == 0)
m.e3 = Constraint(expr= m.x6 - m.x7 - m.x8 == 0)
m.e4 = Constraint(expr= m.x8 - m.x9 - m.x10 - m.x11 == 0)
m.e5 = Constraint(expr= (m.x20 / (0.001 + 0.999 * m.b38) - log(m.x16 / (0.001
    + 0.999 * m.b38) + 1)) * (0.001 + 0.999 * m.b38) <= 0)
m.e6 = Constraint(expr= m.x17 == 0)
m.e7 = Constraint(expr= m.x21 == 0)
m.e8 = Constraint(expr= m.x2 - m.x16 - m.x17 == 0)
m.e9 = Constraint(expr= m.x4 - m.x20 - m.x21 == 0)
m.e10 = Constraint(expr= m.x16 - 10 * m.b38 <= 0)
m.e11 = Constraint(expr= m.x17 + 10 * m.b38 <= 10)
m.e12 = Constraint(expr= m.x20 - 2.39789527279837 * m.b38 <= 0)
m.e13 = Constraint(expr= m.x21 + 2.39789527279837 * m.b38 <= 2.39789527279837)
m.e14 = Constraint(expr= (m.x22 / (0.001 + 0.999 * m.b39) - 1.2 * log(m.x18 / (
    0.001 + 0.999 * m.b39) + 1)) * (0.001 + 0.999 * m.b39) <= 0)
m.e15 = Constraint(expr= m.x19 == 0)
m.e16 = Constraint(expr= m.x23 == 0)
m.e17 = Constraint(expr= m.x3 - m.x18 - m.x19 == 0)
m.e18 = Constraint(expr= m.x5 - m.x22 - m.x23 == 0)
m.e19 = Constraint(expr= m.x18 - 10 * m.b39 <= 0)
m.e20 = Constraint(expr= m.x19 + 10 * m.b39 <= 10)
m.e21 = Constraint(expr= m.x22 - 2.87747432735804 * m.b39 <= 0)
m.e22 = Constraint(expr= m.x23 + 2.87747432735804 * m.b39 <= 2.87747432735804)
m.e23 = Constraint(expr= -0.75 * m.x24 + m.x32 == 0)
m.e24 = Constraint(expr= m.x25 == 0)
m.e25 = Constraint(expr= m.x33 == 0)
m.e26 = Constraint(expr= m.x9 - m.x24 - m.x25 == 0)
m.e27 = Constraint(expr= m.x13 - m.x32 - m.x33 == 0)
m.e28 = Constraint(expr= m.x24 - 2.87747432735804 * m.b40 <= 0)
m.e29 = Constraint(expr= m.x25 + 2.87747432735804 * m.b40 <= 2.87747432735804)
m.e30 = Constraint(expr= m.x32 - 2.15810574551853 * m.b40 <= 0)
m.e31 = Constraint(expr= m.x33 + 2.15810574551853 * m.b40 <= 2.15810574551853)
m.e32 = Constraint(expr= (m.x34 / (0.001 + 0.999 * m.b41) - 1.5 * log(m.x26 / (
    0.001 + 0.999 * m.b41) + 1)) * (0.001 + 0.999 * m.b41) <= 0)
m.e33 = Constraint(expr= m.x27 == 0)
m.e34 = Constraint(expr= m.x35 == 0)
m.e35 = Constraint(expr= m.x10 - m.x26 - m.x27 == 0)
m.e36 = Constraint(expr= m.x14 - m.x34 - m.x35 == 0)
m.e37 = Constraint(expr= m.x26 - 2.87747432735804 * m.b41 <= 0)
m.e38 = Constraint(expr= m.x27 + 2.87747432735804 * m.b41 <= 2.87747432735804)
m.e39 = Constraint(expr= m.x34 - 2.03277599268042 * m.b41 <= 0)
m.e40 = Constraint(expr= m.x35 + 2.03277599268042 * m.b41 <= 2.03277599268042)
m.e41 = Constraint(expr= -m.x28 + m.x36 == 0)
m.e42 = Constraint(expr= -0.5 * m.x30 + m.x36 == 0)
m.e43 = Constraint(expr= m.x29 == 0)
m.e44 = Constraint(expr= m.x31 == 0)
m.e45 = Constraint(expr= m.x37 == 0)
m.e46 = Constraint(expr= m.x11 - m.x28 - m.x29 == 0)
m.e47 = Constraint(expr= m.x12 - m.x30 - m.x31 == 0)
m.e48 = Constraint(expr= m.x15 - m.x36 - m.x37 == 0)
m.e49 = Constraint(expr= m.x28 - 2.87747432735804 * m.b42 <= 0)
m.e50 = Constraint(expr= m.x29 + 2.87747432735804 * m.b42 <= 2.87747432735804)
m.e51 = Constraint(expr= m.x30 - 7 * m.b42 <= 0)
m.e52 = Constraint(expr= m.x31 + 7 * m.b42 <= 7)
m.e53 = Constraint(expr= m.x36 - 3.5 * m.b42 <= 0)
m.e54 = Constraint(expr= m.x37 + 3.5 * m.b42 <= 3.5)
m.e55 = Constraint(expr= m.b38 + m.b39 == 1)
m.e56 = Constraint(expr= m.b38 + m.b39 - m.b40 >= 0)
m.e57 = Constraint(expr= m.b38 + m.b39 - m.b41 >= 0)
m.e58 = Constraint(expr= m.b38 + m.b39 - m.b42 >= 0)
