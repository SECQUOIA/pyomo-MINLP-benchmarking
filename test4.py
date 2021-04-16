from os import initgroups
from pyomo.core.base.piecewise import Bound
from pyomo.environ import *
from math import copysign, pi
from pyomo.core import minimize, value
from pyomo.core.expr import current as EXPR
from pyomo.contrib.gdpopt.util import identify_variables, time_code
from pyomo.contrib.mcpp.pyomo_mcpp import McCormick as mc, MCPP_Error


m = ConcreteModel()
m.x = Var(within=Reals, initialize=pi/4, bounds=(0, 10))
m.y = Var(within=Reals, initialize=1.123, bounds=(-5, 15))
# m.c = Constraint(expr=m.y == 3*sin(m.x)+m.x-1)
m.c = Constraint(expr=m.y == (exp(m.x/3)+2)/3)


counter = 0

vars_in_constr = list(
    identify_variables(m.c.body))

mc_eqn = mc(m.c.body)

ccSlope = mc_eqn.subcc()
cvSlope = mc_eqn.subcv()
ccStart = mc_eqn.concave()
cvStart = mc_eqn.convex()

print('Concave Relaxation')
for i in range(101):
    t = i/10
    # t = (1+i/100)*pi/6
    m.x.value = t
    m.y.value = 3*sin(t)+t-1
    ub_int = min(m.c.upper, mc_eqn.upper()
                 ) if m.c.has_ub() else mc_eqn.upper()
    lb_int = max(m.c.lower, mc_eqn.lower()
                 ) if m.c.has_lb() else mc_eqn.lower()
    mc_eqn = mc(m.c.body)
    print('(', t, ',', lb_int-mc_eqn.concave()+mc_eqn.subcc()[m.y]*m.y.value, ')', end=', ')

print('\n\nConvex Relaxation')
for i in range(101):
    t = i/10
    # t = (1+i/100)*pi/6
    m.x.value = t
    m.y.value = 3*sin(t)+t-1
    ub_int = min(m.c.upper, mc_eqn.upper()
                 ) if m.c.has_ub() else mc_eqn.upper()
    lb_int = max(m.c.lower, mc_eqn.lower()
                 ) if m.c.has_lb() else mc_eqn.lower()
    mc_eqn = mc(m.c.body)
    print('(', t, ',', ub_int-mc_eqn.convex() +
          mc_eqn.subcv()[m.y]*m.y.value, ')', end=', ')
