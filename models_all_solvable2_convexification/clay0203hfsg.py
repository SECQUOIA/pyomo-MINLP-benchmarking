# MINLP written by GAMS Convert at 05/07/21 17:13:01
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       132       24       12       96        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        90       72       18        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       360      288       72
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(11.5,52.5), initialize=11.5)
m.x2 = Var(within=Reals, bounds=(12.5,51.5), initialize=12.5)
m.x3 = Var(within=Reals, bounds=(10.5,53.5), initialize=10.5)
m.x4 = Var(within=Reals, bounds=(7,82), initialize=7)
m.x5 = Var(within=Reals, bounds=(6.5,82.5), initialize=6.5)
m.x6 = Var(within=Reals, bounds=(5.5,83.5), initialize=5.5)
m.x7 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x8 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x9 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x10 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x11 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x12 = Var(within=Reals, bounds=(0,None), initialize=0)
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
m.x38 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x39 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x40 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x41 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x42 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x43 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x44 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x45 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x46 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x47 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x48 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x49 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x50 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x51 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x52 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x53 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x54 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x55 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x56 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x57 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x58 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x59 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x60 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x61 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x62 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x63 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x64 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x65 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x66 = Var(within=Reals, bounds=(0,None), initialize=0)
m.b67 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b68 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b69 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b70 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b71 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b72 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b73 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b74 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b75 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b76 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b77 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b78 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b79 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b80 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b81 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b82 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b83 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b84 = Var(within=Binary, bounds=(0,1), initialize=0)
m.x85 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x86 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x87 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x88 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x89 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x90 = Var(within=Reals, bounds=(0,None), initialize=0)

m.obj = Objective(sense=minimize, expr= 300 * m.x85 + 240 * m.x86 + 100 * m.x87
    + 300 * m.x88 + 240 * m.x89 + 100 * m.x90)

m.e1 = Constraint(expr= -m.x1 + m.x2 + m.x85 >= 0)
m.e2 = Constraint(expr= -m.x1 + m.x3 + m.x86 >= 0)
m.e3 = Constraint(expr= -m.x2 + m.x3 + m.x87 >= 0)
m.e4 = Constraint(expr= m.x1 - m.x2 + m.x85 >= 0)
m.e5 = Constraint(expr= m.x1 - m.x3 + m.x86 >= 0)
m.e6 = Constraint(expr= m.x2 - m.x3 + m.x87 >= 0)
m.e7 = Constraint(expr= -m.x4 + m.x5 + m.x88 >= 0)
m.e8 = Constraint(expr= -m.x4 + m.x6 + m.x89 >= 0)
m.e9 = Constraint(expr= -m.x5 + m.x6 + m.x90 >= 0)
m.e10 = Constraint(expr= m.x4 - m.x5 + m.x88 >= 0)
m.e11 = Constraint(expr= m.x4 - m.x6 + m.x89 >= 0)
m.e12 = Constraint(expr= m.x5 - m.x6 + m.x90 >= 0)
m.e13 = Constraint(expr= m.x1 - m.x7 - m.x9 - m.x11 - m.x13 == 0)
m.e14 = Constraint(expr= m.x1 - m.x8 - m.x10 - m.x12 - m.x14 == 0)
m.e15 = Constraint(expr= m.x2 - m.x15 - m.x17 - m.x19 - m.x21 == 0)
m.e16 = Constraint(expr= m.x2 - m.x16 - m.x18 - m.x20 - m.x22 == 0)
m.e17 = Constraint(expr= m.x3 - m.x23 - m.x25 - m.x27 - m.x29 == 0)
m.e18 = Constraint(expr= m.x3 - m.x24 - m.x26 - m.x28 - m.x30 == 0)
m.e19 = Constraint(expr= m.x4 - m.x31 - m.x33 - m.x35 - m.x37 == 0)
m.e20 = Constraint(expr= m.x4 - m.x32 - m.x34 - m.x36 - m.x38 == 0)
m.e21 = Constraint(expr= m.x5 - m.x39 - m.x41 - m.x43 - m.x45 == 0)
m.e22 = Constraint(expr= m.x5 - m.x40 - m.x42 - m.x44 - m.x46 == 0)
m.e23 = Constraint(expr= m.x6 - m.x47 - m.x49 - m.x51 - m.x53 == 0)
m.e24 = Constraint(expr= m.x6 - m.x48 - m.x50 - m.x52 - m.x54 == 0)
m.e25 = Constraint(expr= m.x7 - 52.5 * m.b67 <= 0)
m.e26 = Constraint(expr= m.x8 - 52.5 * m.b68 <= 0)
m.e27 = Constraint(expr= m.x9 - 52.5 * m.b70 <= 0)
m.e28 = Constraint(expr= m.x10 - 52.5 * m.b71 <= 0)
m.e29 = Constraint(expr= m.x11 - 52.5 * m.b73 <= 0)
m.e30 = Constraint(expr= m.x12 - 52.5 * m.b74 <= 0)
m.e31 = Constraint(expr= m.x13 - 52.5 * m.b76 <= 0)
m.e32 = Constraint(expr= m.x14 - 52.5 * m.b77 <= 0)
m.e33 = Constraint(expr= m.x15 - 52.5 * m.b67 <= 0)
m.e34 = Constraint(expr= m.x16 - 51.5 * m.b69 <= 0)
m.e35 = Constraint(expr= m.x17 - 52.5 * m.b70 <= 0)
m.e36 = Constraint(expr= m.x18 - 51.5 * m.b72 <= 0)
m.e37 = Constraint(expr= m.x19 - 52.5 * m.b73 <= 0)
m.e38 = Constraint(expr= m.x20 - 51.5 * m.b75 <= 0)
m.e39 = Constraint(expr= m.x21 - 52.5 * m.b76 <= 0)
m.e40 = Constraint(expr= m.x22 - 51.5 * m.b78 <= 0)
m.e41 = Constraint(expr= m.x23 - 52.5 * m.b68 <= 0)
m.e42 = Constraint(expr= m.x24 - 51.5 * m.b69 <= 0)
m.e43 = Constraint(expr= m.x25 - 52.5 * m.b71 <= 0)
m.e44 = Constraint(expr= m.x26 - 51.5 * m.b72 <= 0)
m.e45 = Constraint(expr= m.x27 - 52.5 * m.b74 <= 0)
m.e46 = Constraint(expr= m.x28 - 51.5 * m.b75 <= 0)
m.e47 = Constraint(expr= m.x29 - 52.5 * m.b77 <= 0)
m.e48 = Constraint(expr= m.x30 - 51.5 * m.b78 <= 0)
m.e49 = Constraint(expr= m.x31 - 82 * m.b67 <= 0)
m.e50 = Constraint(expr= m.x32 - 82 * m.b68 <= 0)
m.e51 = Constraint(expr= m.x33 - 82 * m.b70 <= 0)
m.e52 = Constraint(expr= m.x34 - 82 * m.b71 <= 0)
m.e53 = Constraint(expr= m.x35 - 82 * m.b73 <= 0)
m.e54 = Constraint(expr= m.x36 - 82 * m.b74 <= 0)
m.e55 = Constraint(expr= m.x37 - 82 * m.b76 <= 0)
m.e56 = Constraint(expr= m.x38 - 82 * m.b77 <= 0)
m.e57 = Constraint(expr= m.x39 - 82 * m.b67 <= 0)
m.e58 = Constraint(expr= m.x40 - 82.5 * m.b69 <= 0)
m.e59 = Constraint(expr= m.x41 - 82 * m.b70 <= 0)
m.e60 = Constraint(expr= m.x42 - 82.5 * m.b72 <= 0)
m.e61 = Constraint(expr= m.x43 - 82 * m.b73 <= 0)
m.e62 = Constraint(expr= m.x44 - 82.5 * m.b75 <= 0)
m.e63 = Constraint(expr= m.x45 - 82 * m.b76 <= 0)
m.e64 = Constraint(expr= m.x46 - 82.5 * m.b78 <= 0)
m.e65 = Constraint(expr= m.x47 - 82 * m.b68 <= 0)
m.e66 = Constraint(expr= m.x48 - 82.5 * m.b69 <= 0)
m.e67 = Constraint(expr= m.x49 - 82 * m.b71 <= 0)
m.e68 = Constraint(expr= m.x50 - 82.5 * m.b72 <= 0)
m.e69 = Constraint(expr= m.x51 - 82 * m.b74 <= 0)
m.e70 = Constraint(expr= m.x52 - 82.5 * m.b75 <= 0)
m.e71 = Constraint(expr= m.x53 - 82 * m.b77 <= 0)
m.e72 = Constraint(expr= m.x54 - 82.5 * m.b78 <= 0)
m.e73 = Constraint(expr= m.x7 - m.x15 + 6 * m.b67 <= 0)
m.e74 = Constraint(expr= m.x8 - m.x23 + 4 * m.b68 <= 0)
m.e75 = Constraint(expr= m.x16 - m.x24 + 5 * m.b69 <= 0)
m.e76 = Constraint(expr= -m.x9 + m.x17 + 6 * m.b70 <= 0)
m.e77 = Constraint(expr= -m.x10 + m.x25 + 4 * m.b71 <= 0)
m.e78 = Constraint(expr= -m.x18 + m.x26 + 5 * m.b72 <= 0)
m.e79 = Constraint(expr= m.x35 - m.x43 + 5.5 * m.b73 <= 0)
m.e80 = Constraint(expr= m.x36 - m.x51 + 4.5 * m.b74 <= 0)
m.e81 = Constraint(expr= m.x44 - m.x52 + 4 * m.b75 <= 0)
m.e82 = Constraint(expr= -m.x37 + m.x45 + 5.5 * m.b76 <= 0)
m.e83 = Constraint(expr= -m.x38 + m.x53 + 4.5 * m.b77 <= 0)
m.e84 = Constraint(expr= -m.x46 + m.x54 + 4 * m.b78 <= 0)
m.e85 = Constraint(expr= m.b67 + m.b70 + m.b73 + m.b76 == 1)
m.e86 = Constraint(expr= m.b68 + m.b71 + m.b74 + m.b77 == 1)
m.e87 = Constraint(expr= m.b69 + m.b72 + m.b75 + m.b78 == 1)
m.e88 = Constraint(expr= m.x1 - m.x55 - m.x58 == 0)
m.e89 = Constraint(expr= m.x2 - m.x56 - m.x59 == 0)
m.e90 = Constraint(expr= m.x3 - m.x57 - m.x60 == 0)
m.e91 = Constraint(expr= m.x4 - m.x61 - m.x64 == 0)
m.e92 = Constraint(expr= m.x5 - m.x62 - m.x65 == 0)
m.e93 = Constraint(expr= m.x6 - m.x63 - m.x66 == 0)
m.e94 = Constraint(expr= m.x55 - 18.5 * m.b79 <= 0)
m.e95 = Constraint(expr= m.x56 - 17.5 * m.b80 <= 0)
m.e96 = Constraint(expr= m.x57 - 19.5 * m.b81 <= 0)
m.e97 = Constraint(expr= m.x58 - 52.5 * m.b82 <= 0)
m.e98 = Constraint(expr= m.x59 - 51.5 * m.b83 <= 0)
m.e99 = Constraint(expr= m.x60 - 53.5 * m.b84 <= 0)
m.e100 = Constraint(expr= m.x61 - 13 * m.b79 <= 0)
m.e101 = Constraint(expr= m.x62 - 13.5 * m.b80 <= 0)
m.e102 = Constraint(expr= m.x63 - 14.5 * m.b81 <= 0)
m.e103 = Constraint(expr= m.x64 - 82 * m.b82 <= 0)
m.e104 = Constraint(expr= m.x65 - 82.5 * m.b83 <= 0)
m.e105 = Constraint(expr= m.x66 - 83.5 * m.b84 <= 0)
m.e106 = Constraint(expr= ((m.x55 / (0.001 + 0.999 * m.b79))**2 - (35 * m.x55)
    / (0.001 + 0.999 * m.b79) + (m.x61 / (0.001 + 0.999 * m.b79))**2 - (14 *
    m.x61) / (0.001 + 0.999 * m.b79)) * (0.001 + 0.999 * m.b79) + 306.25 *
    m.b79 + 49 * m.b79 - 36 * m.b79 <= 0)
m.e107 = Constraint(expr= ((m.x56 / (0.001 + 0.999 * m.b80))**2 - (37 * m.x56)
    / (0.001 + 0.999 * m.b80) + (m.x62 / (0.001 + 0.999 * m.b80))**2 - (15 *
    m.x62) / (0.001 + 0.999 * m.b80)) * (0.001 + 0.999 * m.b80) + 342.25 *
    m.b80 + 56.25 * m.b80 - 36 * m.b80 <= 0)
m.e108 = Constraint(expr= ((m.x57 / (0.001 + 0.999 * m.b81))**2 - (33 * m.x57)
    / (0.001 + 0.999 * m.b81) + (m.x63 / (0.001 + 0.999 * m.b81))**2 - (17 *
    m.x63) / (0.001 + 0.999 * m.b81)) * (0.001 + 0.999 * m.b81) + 272.25 *
    m.b81 + 72.25 * m.b81 - 36 * m.b81 <= 0)
m.e109 = Constraint(expr= ((m.x58 / (0.001 + 0.999 * m.b82))**2 - (105 * m.x58)
    / (0.001 + 0.999 * m.b82) + (m.x64 / (0.001 + 0.999 * m.b82))**2 - (154 *
    m.x64) / (0.001 + 0.999 * m.b82)) * (0.001 + 0.999 * m.b82) + 2756.25 *
    m.b82 + 5929 * m.b82 - 25 * m.b82 <= 0)
m.e110 = Constraint(expr= ((m.x59 / (0.001 + 0.999 * m.b83))**2 - (107 * m.x59)
    / (0.001 + 0.999 * m.b83) + (m.x65 / (0.001 + 0.999 * m.b83))**2 - (155 *
    m.x65) / (0.001 + 0.999 * m.b83)) * (0.001 + 0.999 * m.b83) + 2862.25 *
    m.b83 + 6006.25 * m.b83 - 25 * m.b83 <= 0)
m.e111 = Constraint(expr= ((m.x60 / (0.001 + 0.999 * m.b84))**2 - (103 * m.x60)
    / (0.001 + 0.999 * m.b84) + (m.x66 / (0.001 + 0.999 * m.b84))**2 - (157 *
    m.x66) / (0.001 + 0.999 * m.b84)) * (0.001 + 0.999 * m.b84) + 2652.25 *
    m.b84 + 6162.25 * m.b84 - 25 * m.b84 <= 0)
m.e112 = Constraint(expr= ((m.x55 / (0.001 + 0.999 * m.b79))**2 - (35 * m.x55)
    / (0.001 + 0.999 * m.b79) + (m.x61 / (0.001 + 0.999 * m.b79))**2 - (26 *
    m.x61) / (0.001 + 0.999 * m.b79)) * (0.001 + 0.999 * m.b79) + 306.25 *
    m.b79 + 169 * m.b79 - 36 * m.b79 <= 0)
m.e113 = Constraint(expr= ((m.x56 / (0.001 + 0.999 * m.b80))**2 - (37 * m.x56)
    / (0.001 + 0.999 * m.b80) + (m.x62 / (0.001 + 0.999 * m.b80))**2 - (25 *
    m.x62) / (0.001 + 0.999 * m.b80)) * (0.001 + 0.999 * m.b80) + 342.25 *
    m.b80 + 156.25 * m.b80 - 36 * m.b80 <= 0)
m.e114 = Constraint(expr= ((m.x57 / (0.001 + 0.999 * m.b81))**2 - (33 * m.x57)
    / (0.001 + 0.999 * m.b81) + (m.x63 / (0.001 + 0.999 * m.b81))**2 - (23 *
    m.x63) / (0.001 + 0.999 * m.b81)) * (0.001 + 0.999 * m.b81) + 272.25 *
    m.b81 + 132.25 * m.b81 - 36 * m.b81 <= 0)
m.e115 = Constraint(expr= ((m.x58 / (0.001 + 0.999 * m.b82))**2 - (105 * m.x58)
    / (0.001 + 0.999 * m.b82) + (m.x64 / (0.001 + 0.999 * m.b82))**2 - (166 *
    m.x64) / (0.001 + 0.999 * m.b82)) * (0.001 + 0.999 * m.b82) + 2756.25 *
    m.b82 + 6889 * m.b82 - 25 * m.b82 <= 0)
m.e116 = Constraint(expr= ((m.x59 / (0.001 + 0.999 * m.b83))**2 - (107 * m.x59)
    / (0.001 + 0.999 * m.b83) + (m.x65 / (0.001 + 0.999 * m.b83))**2 - (165 *
    m.x65) / (0.001 + 0.999 * m.b83)) * (0.001 + 0.999 * m.b83) + 2862.25 *
    m.b83 + 6806.25 * m.b83 - 25 * m.b83 <= 0)
m.e117 = Constraint(expr= ((m.x60 / (0.001 + 0.999 * m.b84))**2 - (103 * m.x60)
    / (0.001 + 0.999 * m.b84) + (m.x66 / (0.001 + 0.999 * m.b84))**2 - (163 *
    m.x66) / (0.001 + 0.999 * m.b84)) * (0.001 + 0.999 * m.b84) + 2652.25 *
    m.b84 + 6642.25 * m.b84 - 25 * m.b84 <= 0)
m.e118 = Constraint(expr= ((m.x55 / (0.001 + 0.999 * m.b79))**2 - (25 * m.x55)
    / (0.001 + 0.999 * m.b79) + (m.x61 / (0.001 + 0.999 * m.b79))**2 - (14 *
    m.x61) / (0.001 + 0.999 * m.b79)) * (0.001 + 0.999 * m.b79) + 156.25 *
    m.b79 + 49 * m.b79 - 36 * m.b79 <= 0)
m.e119 = Constraint(expr= ((m.x56 / (0.001 + 0.999 * m.b80))**2 - (23 * m.x56)
    / (0.001 + 0.999 * m.b80) + (m.x62 / (0.001 + 0.999 * m.b80))**2 - (15 *
    m.x62) / (0.001 + 0.999 * m.b80)) * (0.001 + 0.999 * m.b80) + 132.25 *
    m.b80 + 56.25 * m.b80 - 36 * m.b80 <= 0)
m.e120 = Constraint(expr= ((m.x57 / (0.001 + 0.999 * m.b81))**2 - (27 * m.x57)
    / (0.001 + 0.999 * m.b81) + (m.x63 / (0.001 + 0.999 * m.b81))**2 - (17 *
    m.x63) / (0.001 + 0.999 * m.b81)) * (0.001 + 0.999 * m.b81) + 182.25 *
    m.b81 + 72.25 * m.b81 - 36 * m.b81 <= 0)
m.e121 = Constraint(expr= ((m.x58 / (0.001 + 0.999 * m.b82))**2 - (95 * m.x58)
    / (0.001 + 0.999 * m.b82) + (m.x64 / (0.001 + 0.999 * m.b82))**2 - (154 *
    m.x64) / (0.001 + 0.999 * m.b82)) * (0.001 + 0.999 * m.b82) + 2256.25 *
    m.b82 + 5929 * m.b82 - 25 * m.b82 <= 0)
m.e122 = Constraint(expr= ((m.x59 / (0.001 + 0.999 * m.b83))**2 - (93 * m.x59)
    / (0.001 + 0.999 * m.b83) + (m.x65 / (0.001 + 0.999 * m.b83))**2 - (155 *
    m.x65) / (0.001 + 0.999 * m.b83)) * (0.001 + 0.999 * m.b83) + 2162.25 *
    m.b83 + 6006.25 * m.b83 - 25 * m.b83 <= 0)
m.e123 = Constraint(expr= ((m.x60 / (0.001 + 0.999 * m.b84))**2 - (97 * m.x60)
    / (0.001 + 0.999 * m.b84) + (m.x66 / (0.001 + 0.999 * m.b84))**2 - (157 *
    m.x66) / (0.001 + 0.999 * m.b84)) * (0.001 + 0.999 * m.b84) + 2352.25 *
    m.b84 + 6162.25 * m.b84 - 25 * m.b84 <= 0)
m.e124 = Constraint(expr= ((m.x55 / (0.001 + 0.999 * m.b79))**2 - (25 * m.x55)
    / (0.001 + 0.999 * m.b79) + (m.x61 / (0.001 + 0.999 * m.b79))**2 - (26 *
    m.x61) / (0.001 + 0.999 * m.b79)) * (0.001 + 0.999 * m.b79) + 156.25 *
    m.b79 + 169 * m.b79 - 36 * m.b79 <= 0)
m.e125 = Constraint(expr= ((m.x56 / (0.001 + 0.999 * m.b80))**2 - (23 * m.x56)
    / (0.001 + 0.999 * m.b80) + (m.x62 / (0.001 + 0.999 * m.b80))**2 - (25 *
    m.x62) / (0.001 + 0.999 * m.b80)) * (0.001 + 0.999 * m.b80) + 132.25 *
    m.b80 + 156.25 * m.b80 - 36 * m.b80 <= 0)
m.e126 = Constraint(expr= ((m.x57 / (0.001 + 0.999 * m.b81))**2 - (27 * m.x57)
    / (0.001 + 0.999 * m.b81) + (m.x63 / (0.001 + 0.999 * m.b81))**2 - (23 *
    m.x63) / (0.001 + 0.999 * m.b81)) * (0.001 + 0.999 * m.b81) + 182.25 *
    m.b81 + 132.25 * m.b81 - 36 * m.b81 <= 0)
m.e127 = Constraint(expr= ((m.x58 / (0.001 + 0.999 * m.b82))**2 - (95 * m.x58)
    / (0.001 + 0.999 * m.b82) + (m.x64 / (0.001 + 0.999 * m.b82))**2 - (166 *
    m.x64) / (0.001 + 0.999 * m.b82)) * (0.001 + 0.999 * m.b82) + 2256.25 *
    m.b82 + 6889 * m.b82 - 25 * m.b82 <= 0)
m.e128 = Constraint(expr= ((m.x59 / (0.001 + 0.999 * m.b83))**2 - (93 * m.x59)
    / (0.001 + 0.999 * m.b83) + (m.x65 / (0.001 + 0.999 * m.b83))**2 - (165 *
    m.x65) / (0.001 + 0.999 * m.b83)) * (0.001 + 0.999 * m.b83) + 2162.25 *
    m.b83 + 6806.25 * m.b83 - 25 * m.b83 <= 0)
m.e129 = Constraint(expr= ((m.x60 / (0.001 + 0.999 * m.b84))**2 - (97 * m.x60)
    / (0.001 + 0.999 * m.b84) + (m.x66 / (0.001 + 0.999 * m.b84))**2 - (163 *
    m.x66) / (0.001 + 0.999 * m.b84)) * (0.001 + 0.999 * m.b84) + 2352.25 *
    m.b84 + 6642.25 * m.b84 - 25 * m.b84 <= 0)
m.e130 = Constraint(expr= m.b79 + m.b82 == 1)
m.e131 = Constraint(expr= m.b80 + m.b83 == 1)
m.e132 = Constraint(expr= m.b81 + m.b84 == 1)
