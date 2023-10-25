# MINLP written by GAMS Convert at 05/07/21 17:13:00
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       219        7        0      212        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       154       84       70        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       810      600      210
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.b1 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b2 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b3 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b4 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b5 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b6 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b7 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b8 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b9 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b10 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b11 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b12 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b13 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b14 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b15 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b16 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b17 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b18 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b19 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b20 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b21 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b22 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b23 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b24 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b25 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b26 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b27 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b28 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b29 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b30 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b31 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b32 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b33 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b34 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b35 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b36 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b37 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b38 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b39 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b40 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b41 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b42 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b43 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b44 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b45 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b46 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b47 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b48 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b49 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b50 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b51 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b52 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b53 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b54 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b55 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b56 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b57 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b58 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b59 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b60 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b61 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b62 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b63 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b64 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b65 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b66 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b67 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b68 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b69 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b70 = Var(within=Binary, bounds=(0,1), initialize=0)
m.x71 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x72 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x73 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x74 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x75 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x76 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x77 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x78 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x79 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x80 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x81 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x82 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x83 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x84 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x85 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x86 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x87 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x88 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x89 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x90 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x91 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x92 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x93 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x94 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x95 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x96 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x97 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x98 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x99 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x100 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x101 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x102 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x103 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x104 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x105 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x106 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x107 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x108 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x109 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x110 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x111 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x112 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x113 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x114 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x115 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x116 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x117 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x118 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x119 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x120 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x121 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x122 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x123 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x124 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x125 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x126 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x127 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x128 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x129 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x130 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x131 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x132 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x133 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x134 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x135 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x136 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x137 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x138 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x139 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x140 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x141 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x142 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x143 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x144 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x145 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x146 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x147 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x148 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x149 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x150 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x151 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x152 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x153 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x154 = Var(within=Reals, bounds=(0,10), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x73 + m.x76 + m.x79 + m.x81 + m.x83
    + m.x85 + m.x87 + m.x89 + m.x91 + m.x93 + m.x95 + m.x97 + m.x99 + m.x101
    + m.x103 + m.x105 + m.x107 + m.x109 + m.x110 + m.x111 + m.x112 + m.x113 +
    m.x114 + m.x115 + m.x116 + m.x117 + m.x118 + m.x119 + m.x120 + m.x121 +
    m.x122 + m.x123 + m.x124 + m.x125 + m.x126 + m.x127 + m.x128 + m.x129 +
    m.x130 + m.x131 + m.x132 + m.x133 + m.x134 + m.x135 + m.x136 + m.x137 +
    m.x138 + m.x139 + m.x140 + m.x141 + m.x142 + m.x143 + m.x144 + m.x145 +
    m.x146 + m.x147 + m.x148 + m.x149 + m.x150 + m.x151 + m.x152 + m.x153 +
    m.x154)

m.e1 = Constraint(expr= m.x71 - m.x72 - m.x73 <= 0)
m.e2 = Constraint(expr= -m.x71 + m.x72 - m.x73 <= 0)
m.e3 = Constraint(expr= m.x74 - m.x75 - m.x76 <= 0)
m.e4 = Constraint(expr= -m.x74 + m.x75 - m.x76 <= 0)
m.e5 = Constraint(expr= m.x77 - m.x78 - m.x79 <= 0)
m.e6 = Constraint(expr= -m.x77 + m.x78 - m.x79 <= 0)
m.e7 = Constraint(expr= m.x71 - m.x80 - m.x81 <= 0)
m.e8 = Constraint(expr= -m.x71 + m.x80 - m.x81 <= 0)
m.e9 = Constraint(expr= m.x74 - m.x82 - m.x83 <= 0)
m.e10 = Constraint(expr= -m.x74 + m.x82 - m.x83 <= 0)
m.e11 = Constraint(expr= m.x77 - m.x84 - m.x85 <= 0)
m.e12 = Constraint(expr= -m.x77 + m.x84 - m.x85 <= 0)
m.e13 = Constraint(expr= m.x71 - m.x86 - m.x87 <= 0)
m.e14 = Constraint(expr= -m.x71 + m.x86 - m.x87 <= 0)
m.e15 = Constraint(expr= m.x74 - m.x88 - m.x89 <= 0)
m.e16 = Constraint(expr= -m.x74 + m.x88 - m.x89 <= 0)
m.e17 = Constraint(expr= m.x77 - m.x90 - m.x91 <= 0)
m.e18 = Constraint(expr= -m.x77 + m.x90 - m.x91 <= 0)
m.e19 = Constraint(expr= m.x71 - m.x92 - m.x93 <= 0)
m.e20 = Constraint(expr= -m.x71 + m.x92 - m.x93 <= 0)
m.e21 = Constraint(expr= m.x74 - m.x94 - m.x95 <= 0)
m.e22 = Constraint(expr= -m.x74 + m.x94 - m.x95 <= 0)
m.e23 = Constraint(expr= m.x77 - m.x96 - m.x97 <= 0)
m.e24 = Constraint(expr= -m.x77 + m.x96 - m.x97 <= 0)
m.e25 = Constraint(expr= m.x71 - m.x98 - m.x99 <= 0)
m.e26 = Constraint(expr= -m.x71 + m.x98 - m.x99 <= 0)
m.e27 = Constraint(expr= m.x74 - m.x100 - m.x101 <= 0)
m.e28 = Constraint(expr= -m.x74 + m.x100 - m.x101 <= 0)
m.e29 = Constraint(expr= m.x77 - m.x102 - m.x103 <= 0)
m.e30 = Constraint(expr= -m.x77 + m.x102 - m.x103 <= 0)
m.e31 = Constraint(expr= m.x71 - m.x104 - m.x105 <= 0)
m.e32 = Constraint(expr= -m.x71 + m.x104 - m.x105 <= 0)
m.e33 = Constraint(expr= m.x74 - m.x106 - m.x107 <= 0)
m.e34 = Constraint(expr= -m.x74 + m.x106 - m.x107 <= 0)
m.e35 = Constraint(expr= m.x77 - m.x108 - m.x109 <= 0)
m.e36 = Constraint(expr= -m.x77 + m.x108 - m.x109 <= 0)
m.e37 = Constraint(expr= m.x72 - m.x80 - m.x110 <= 0)
m.e38 = Constraint(expr= -m.x72 + m.x80 - m.x110 <= 0)
m.e39 = Constraint(expr= m.x75 - m.x82 - m.x111 <= 0)
m.e40 = Constraint(expr= -m.x75 + m.x82 - m.x111 <= 0)
m.e41 = Constraint(expr= m.x78 - m.x84 - m.x112 <= 0)
m.e42 = Constraint(expr= -m.x78 + m.x84 - m.x112 <= 0)
m.e43 = Constraint(expr= m.x72 - m.x86 - m.x113 <= 0)
m.e44 = Constraint(expr= -m.x72 + m.x86 - m.x113 <= 0)
m.e45 = Constraint(expr= m.x75 - m.x88 - m.x114 <= 0)
m.e46 = Constraint(expr= -m.x75 + m.x88 - m.x114 <= 0)
m.e47 = Constraint(expr= m.x78 - m.x90 - m.x115 <= 0)
m.e48 = Constraint(expr= -m.x78 + m.x90 - m.x115 <= 0)
m.e49 = Constraint(expr= m.x72 - m.x92 - m.x116 <= 0)
m.e50 = Constraint(expr= -m.x72 + m.x92 - m.x116 <= 0)
m.e51 = Constraint(expr= m.x75 - m.x94 - m.x117 <= 0)
m.e52 = Constraint(expr= -m.x75 + m.x94 - m.x117 <= 0)
m.e53 = Constraint(expr= m.x78 - m.x96 - m.x118 <= 0)
m.e54 = Constraint(expr= -m.x78 + m.x96 - m.x118 <= 0)
m.e55 = Constraint(expr= m.x72 - m.x98 - m.x119 <= 0)
m.e56 = Constraint(expr= -m.x72 + m.x98 - m.x119 <= 0)
m.e57 = Constraint(expr= m.x75 - m.x100 - m.x120 <= 0)
m.e58 = Constraint(expr= -m.x75 + m.x100 - m.x120 <= 0)
m.e59 = Constraint(expr= m.x78 - m.x102 - m.x121 <= 0)
m.e60 = Constraint(expr= -m.x78 + m.x102 - m.x121 <= 0)
m.e61 = Constraint(expr= m.x72 - m.x104 - m.x122 <= 0)
m.e62 = Constraint(expr= -m.x72 + m.x104 - m.x122 <= 0)
m.e63 = Constraint(expr= m.x75 - m.x106 - m.x123 <= 0)
m.e64 = Constraint(expr= -m.x75 + m.x106 - m.x123 <= 0)
m.e65 = Constraint(expr= m.x78 - m.x108 - m.x124 <= 0)
m.e66 = Constraint(expr= -m.x78 + m.x108 - m.x124 <= 0)
m.e67 = Constraint(expr= m.x80 - m.x86 - m.x125 <= 0)
m.e68 = Constraint(expr= -m.x80 + m.x86 - m.x125 <= 0)
m.e69 = Constraint(expr= m.x82 - m.x88 - m.x126 <= 0)
m.e70 = Constraint(expr= -m.x82 + m.x88 - m.x126 <= 0)
m.e71 = Constraint(expr= m.x84 - m.x90 - m.x127 <= 0)
m.e72 = Constraint(expr= -m.x84 + m.x90 - m.x127 <= 0)
m.e73 = Constraint(expr= m.x80 - m.x92 - m.x128 <= 0)
m.e74 = Constraint(expr= -m.x80 + m.x92 - m.x128 <= 0)
m.e75 = Constraint(expr= m.x82 - m.x94 - m.x129 <= 0)
m.e76 = Constraint(expr= -m.x82 + m.x94 - m.x129 <= 0)
m.e77 = Constraint(expr= m.x84 - m.x96 - m.x130 <= 0)
m.e78 = Constraint(expr= -m.x84 + m.x96 - m.x130 <= 0)
m.e79 = Constraint(expr= m.x80 - m.x98 - m.x131 <= 0)
m.e80 = Constraint(expr= -m.x80 + m.x98 - m.x131 <= 0)
m.e81 = Constraint(expr= m.x82 - m.x100 - m.x132 <= 0)
m.e82 = Constraint(expr= -m.x82 + m.x100 - m.x132 <= 0)
m.e83 = Constraint(expr= m.x84 - m.x102 - m.x133 <= 0)
m.e84 = Constraint(expr= -m.x84 + m.x102 - m.x133 <= 0)
m.e85 = Constraint(expr= m.x80 - m.x104 - m.x134 <= 0)
m.e86 = Constraint(expr= -m.x80 + m.x104 - m.x134 <= 0)
m.e87 = Constraint(expr= m.x82 - m.x106 - m.x135 <= 0)
m.e88 = Constraint(expr= -m.x82 + m.x106 - m.x135 <= 0)
m.e89 = Constraint(expr= m.x84 - m.x108 - m.x136 <= 0)
m.e90 = Constraint(expr= -m.x84 + m.x108 - m.x136 <= 0)
m.e91 = Constraint(expr= m.x86 - m.x92 - m.x137 <= 0)
m.e92 = Constraint(expr= -m.x86 + m.x92 - m.x137 <= 0)
m.e93 = Constraint(expr= m.x88 - m.x94 - m.x138 <= 0)
m.e94 = Constraint(expr= -m.x88 + m.x94 - m.x138 <= 0)
m.e95 = Constraint(expr= m.x90 - m.x96 - m.x139 <= 0)
m.e96 = Constraint(expr= -m.x90 + m.x96 - m.x139 <= 0)
m.e97 = Constraint(expr= m.x86 - m.x98 - m.x140 <= 0)
m.e98 = Constraint(expr= -m.x86 + m.x98 - m.x140 <= 0)
m.e99 = Constraint(expr= m.x88 - m.x100 - m.x141 <= 0)
m.e100 = Constraint(expr= -m.x88 + m.x100 - m.x141 <= 0)
m.e101 = Constraint(expr= m.x90 - m.x102 - m.x142 <= 0)
m.e102 = Constraint(expr= -m.x90 + m.x102 - m.x142 <= 0)
m.e103 = Constraint(expr= m.x86 - m.x104 - m.x143 <= 0)
m.e104 = Constraint(expr= -m.x86 + m.x104 - m.x143 <= 0)
m.e105 = Constraint(expr= m.x88 - m.x106 - m.x144 <= 0)
m.e106 = Constraint(expr= -m.x88 + m.x106 - m.x144 <= 0)
m.e107 = Constraint(expr= m.x90 - m.x108 - m.x145 <= 0)
m.e108 = Constraint(expr= -m.x90 + m.x108 - m.x145 <= 0)
m.e109 = Constraint(expr= m.x92 - m.x98 - m.x146 <= 0)
m.e110 = Constraint(expr= -m.x92 + m.x98 - m.x146 <= 0)
m.e111 = Constraint(expr= m.x94 - m.x100 - m.x147 <= 0)
m.e112 = Constraint(expr= -m.x94 + m.x100 - m.x147 <= 0)
m.e113 = Constraint(expr= m.x96 - m.x102 - m.x148 <= 0)
m.e114 = Constraint(expr= -m.x96 + m.x102 - m.x148 <= 0)
m.e115 = Constraint(expr= m.x92 - m.x104 - m.x149 <= 0)
m.e116 = Constraint(expr= -m.x92 + m.x104 - m.x149 <= 0)
m.e117 = Constraint(expr= m.x94 - m.x106 - m.x150 <= 0)
m.e118 = Constraint(expr= -m.x94 + m.x106 - m.x150 <= 0)
m.e119 = Constraint(expr= m.x96 - m.x108 - m.x151 <= 0)
m.e120 = Constraint(expr= -m.x96 + m.x108 - m.x151 <= 0)
m.e121 = Constraint(expr= m.x98 - m.x104 - m.x152 <= 0)
m.e122 = Constraint(expr= -m.x98 + m.x104 - m.x152 <= 0)
m.e123 = Constraint(expr= m.x100 - m.x106 - m.x153 <= 0)
m.e124 = Constraint(expr= -m.x100 + m.x106 - m.x153 <= 0)
m.e125 = Constraint(expr= m.x102 - m.x108 - m.x154 <= 0)
m.e126 = Constraint(expr= -m.x102 + m.x108 - m.x154 <= 0)
m.e127 = Constraint(expr= (4.13263517293428 - m.x71)**2 + (9.89321475687716 -
    m.x74)**2 + (7.00543632985936 - m.x77)**2 + 89.4259075893627 * m.b1
    <= 90.4259075893627)
m.e128 = Constraint(expr= (5.36782363621885 - m.x71)**2 + (1.51651713640814 -
    m.x74)**2 + (6.16125243380265 - m.x77)**2 + 90.8634617423464 * m.b2
    <= 91.8634617423464)
m.e129 = Constraint(expr= (8.2275592328595 - m.x71)**2 + (4.51338886533517 -
    m.x74)**2 + (3.02091680975325 - m.x77)**2 + 77.2828440165495 * m.b3
    <= 78.2828440165495)
m.e130 = Constraint(expr= (4.45787019759725 - m.x71)**2 + (8.176601080562 -
    m.x74)**2 + (2.1384293807986 - m.x77)**2 + 94.0648155502126 * m.b4
    <= 95.0648155502126)
m.e131 = Constraint(expr= (8.002643257644 - m.x71)**2 + (5.28236491095606 -
    m.x74)**2 + (5.11938934174774 - m.x77)**2 + 68.4345962886061 * m.b5
    <= 69.4345962886061)
m.e132 = Constraint(expr= (6.24049438612365 - m.x71)**2 + (3.8120863088984 -
    m.x74)**2 + (9.50984985922338 - m.x77)**2 + 106.313114234833 * m.b6
    <= 107.313114234833)
m.e133 = Constraint(expr= (4.54775219913353 - m.x71)**2 + (5.50227429055218 -
    m.x74)**2 + (3.5032816165688 - m.x77)**2 + 54.7317080633338 * m.b7
    <= 55.7317080633338)
m.e134 = Constraint(expr= (1.674156677828 - m.x71)**2 + (4.99633600480765 -
    m.x74)**2 + (1.42648309916894 - m.x77)**2 + 106.313114234833 * m.b8
    <= 107.313114234833)
m.e135 = Constraint(expr= (1.82060210212647 - m.x71)**2 + (8.61550724971434 -
    m.x74)**2 + (4.93467653333678 - m.x77)**2 + 80.5431824405483 * m.b9
    <= 81.5431824405483)
m.e136 = Constraint(expr= (6.61159251106337 - m.x71)**2 + (9.89217063451911 -
    m.x74)**2 + (4.74850918126831 - m.x77)**2 + 90.8634617423464 * m.b10
    <= 91.8634617423464)
m.e137 = Constraint(expr= m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8
    + m.b9 + m.b10 == 1)
m.e138 = Constraint(expr= (4.13263517293428 - m.x72)**2 + (9.89321475687716 -
    m.x75)**2 + (7.00543632985936 - m.x78)**2 + 89.4259075893627 * m.b11
    <= 90.4259075893627)
m.e139 = Constraint(expr= (5.36782363621885 - m.x72)**2 + (1.51651713640814 -
    m.x75)**2 + (6.16125243380265 - m.x78)**2 + 90.8634617423464 * m.b12
    <= 91.8634617423464)
m.e140 = Constraint(expr= (8.2275592328595 - m.x72)**2 + (4.51338886533517 -
    m.x75)**2 + (3.02091680975325 - m.x78)**2 + 77.2828440165495 * m.b13
    <= 78.2828440165495)
m.e141 = Constraint(expr= (4.45787019759725 - m.x72)**2 + (8.176601080562 -
    m.x75)**2 + (2.1384293807986 - m.x78)**2 + 94.0648155502126 * m.b14
    <= 95.0648155502126)
m.e142 = Constraint(expr= (8.002643257644 - m.x72)**2 + (5.28236491095606 -
    m.x75)**2 + (5.11938934174774 - m.x78)**2 + 68.4345962886061 * m.b15
    <= 69.4345962886061)
m.e143 = Constraint(expr= (6.24049438612365 - m.x72)**2 + (3.8120863088984 -
    m.x75)**2 + (9.50984985922338 - m.x78)**2 + 106.313114234833 * m.b16
    <= 107.313114234833)
m.e144 = Constraint(expr= (4.54775219913353 - m.x72)**2 + (5.50227429055218 -
    m.x75)**2 + (3.5032816165688 - m.x78)**2 + 54.7317080633338 * m.b17
    <= 55.7317080633338)
m.e145 = Constraint(expr= (1.674156677828 - m.x72)**2 + (4.99633600480765 -
    m.x75)**2 + (1.42648309916894 - m.x78)**2 + 106.313114234833 * m.b18
    <= 107.313114234833)
m.e146 = Constraint(expr= (1.82060210212647 - m.x72)**2 + (8.61550724971434 -
    m.x75)**2 + (4.93467653333678 - m.x78)**2 + 80.5431824405483 * m.b19
    <= 81.5431824405483)
m.e147 = Constraint(expr= (6.61159251106337 - m.x72)**2 + (9.89217063451911 -
    m.x75)**2 + (4.74850918126831 - m.x78)**2 + 90.8634617423464 * m.b20
    <= 91.8634617423464)
m.e148 = Constraint(expr= m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17
    + m.b18 + m.b19 + m.b20 == 1)
m.e149 = Constraint(expr= (4.13263517293428 - m.x80)**2 + (9.89321475687716 -
    m.x82)**2 + (7.00543632985936 - m.x84)**2 + 89.4259075893627 * m.b21
    <= 90.4259075893627)
m.e150 = Constraint(expr= (5.36782363621885 - m.x80)**2 + (1.51651713640814 -
    m.x82)**2 + (6.16125243380265 - m.x84)**2 + 90.8634617423464 * m.b22
    <= 91.8634617423464)
m.e151 = Constraint(expr= (8.2275592328595 - m.x80)**2 + (4.51338886533517 -
    m.x82)**2 + (3.02091680975325 - m.x84)**2 + 77.2828440165495 * m.b23
    <= 78.2828440165495)
m.e152 = Constraint(expr= (4.45787019759725 - m.x80)**2 + (8.176601080562 -
    m.x82)**2 + (2.1384293807986 - m.x84)**2 + 94.0648155502126 * m.b24
    <= 95.0648155502126)
m.e153 = Constraint(expr= (8.002643257644 - m.x80)**2 + (5.28236491095606 -
    m.x82)**2 + (5.11938934174774 - m.x84)**2 + 68.4345962886061 * m.b25
    <= 69.4345962886061)
m.e154 = Constraint(expr= (6.24049438612365 - m.x80)**2 + (3.8120863088984 -
    m.x82)**2 + (9.50984985922338 - m.x84)**2 + 106.313114234833 * m.b26
    <= 107.313114234833)
m.e155 = Constraint(expr= (4.54775219913353 - m.x80)**2 + (5.50227429055218 -
    m.x82)**2 + (3.5032816165688 - m.x84)**2 + 54.7317080633338 * m.b27
    <= 55.7317080633338)
m.e156 = Constraint(expr= (1.674156677828 - m.x80)**2 + (4.99633600480765 -
    m.x82)**2 + (1.42648309916894 - m.x84)**2 + 106.313114234833 * m.b28
    <= 107.313114234833)
m.e157 = Constraint(expr= (1.82060210212647 - m.x80)**2 + (8.61550724971434 -
    m.x82)**2 + (4.93467653333678 - m.x84)**2 + 80.5431824405483 * m.b29
    <= 81.5431824405483)
m.e158 = Constraint(expr= (6.61159251106337 - m.x80)**2 + (9.89217063451911 -
    m.x82)**2 + (4.74850918126831 - m.x84)**2 + 90.8634617423464 * m.b30
    <= 91.8634617423464)
m.e159 = Constraint(expr= m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 + m.b27
    + m.b28 + m.b29 + m.b30 == 1)
m.e160 = Constraint(expr= (4.13263517293428 - m.x86)**2 + (9.89321475687716 -
    m.x88)**2 + (7.00543632985936 - m.x90)**2 + 89.4259075893627 * m.b31
    <= 90.4259075893627)
m.e161 = Constraint(expr= (5.36782363621885 - m.x86)**2 + (1.51651713640814 -
    m.x88)**2 + (6.16125243380265 - m.x90)**2 + 90.8634617423464 * m.b32
    <= 91.8634617423464)
m.e162 = Constraint(expr= (8.2275592328595 - m.x86)**2 + (4.51338886533517 -
    m.x88)**2 + (3.02091680975325 - m.x90)**2 + 77.2828440165495 * m.b33
    <= 78.2828440165495)
m.e163 = Constraint(expr= (4.45787019759725 - m.x86)**2 + (8.176601080562 -
    m.x88)**2 + (2.1384293807986 - m.x90)**2 + 94.0648155502126 * m.b34
    <= 95.0648155502126)
m.e164 = Constraint(expr= (8.002643257644 - m.x86)**2 + (5.28236491095606 -
    m.x88)**2 + (5.11938934174774 - m.x90)**2 + 68.4345962886061 * m.b35
    <= 69.4345962886061)
m.e165 = Constraint(expr= (6.24049438612365 - m.x86)**2 + (3.8120863088984 -
    m.x88)**2 + (9.50984985922338 - m.x90)**2 + 106.313114234833 * m.b36
    <= 107.313114234833)
m.e166 = Constraint(expr= (4.54775219913353 - m.x86)**2 + (5.50227429055218 -
    m.x88)**2 + (3.5032816165688 - m.x90)**2 + 54.7317080633338 * m.b37
    <= 55.7317080633338)
m.e167 = Constraint(expr= (1.674156677828 - m.x86)**2 + (4.99633600480765 -
    m.x88)**2 + (1.42648309916894 - m.x90)**2 + 106.313114234833 * m.b38
    <= 107.313114234833)
m.e168 = Constraint(expr= (1.82060210212647 - m.x86)**2 + (8.61550724971434 -
    m.x88)**2 + (4.93467653333678 - m.x90)**2 + 80.5431824405483 * m.b39
    <= 81.5431824405483)
m.e169 = Constraint(expr= (6.61159251106337 - m.x86)**2 + (9.89217063451911 -
    m.x88)**2 + (4.74850918126831 - m.x90)**2 + 90.8634617423464 * m.b40
    <= 91.8634617423464)
m.e170 = Constraint(expr= m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 + m.b37
    + m.b38 + m.b39 + m.b40 == 1)
m.e171 = Constraint(expr= (4.13263517293428 - m.x92)**2 + (9.89321475687716 -
    m.x94)**2 + (7.00543632985936 - m.x96)**2 + 89.4259075893627 * m.b41
    <= 90.4259075893627)
m.e172 = Constraint(expr= (5.36782363621885 - m.x92)**2 + (1.51651713640814 -
    m.x94)**2 + (6.16125243380265 - m.x96)**2 + 90.8634617423464 * m.b42
    <= 91.8634617423464)
m.e173 = Constraint(expr= (8.2275592328595 - m.x92)**2 + (4.51338886533517 -
    m.x94)**2 + (3.02091680975325 - m.x96)**2 + 77.2828440165495 * m.b43
    <= 78.2828440165495)
m.e174 = Constraint(expr= (4.45787019759725 - m.x92)**2 + (8.176601080562 -
    m.x94)**2 + (2.1384293807986 - m.x96)**2 + 94.0648155502126 * m.b44
    <= 95.0648155502126)
m.e175 = Constraint(expr= (8.002643257644 - m.x92)**2 + (5.28236491095606 -
    m.x94)**2 + (5.11938934174774 - m.x96)**2 + 68.4345962886061 * m.b45
    <= 69.4345962886061)
m.e176 = Constraint(expr= (6.24049438612365 - m.x92)**2 + (3.8120863088984 -
    m.x94)**2 + (9.50984985922338 - m.x96)**2 + 106.313114234833 * m.b46
    <= 107.313114234833)
m.e177 = Constraint(expr= (4.54775219913353 - m.x92)**2 + (5.50227429055218 -
    m.x94)**2 + (3.5032816165688 - m.x96)**2 + 54.7317080633338 * m.b47
    <= 55.7317080633338)
m.e178 = Constraint(expr= (1.674156677828 - m.x92)**2 + (4.99633600480765 -
    m.x94)**2 + (1.42648309916894 - m.x96)**2 + 106.313114234833 * m.b48
    <= 107.313114234833)
m.e179 = Constraint(expr= (1.82060210212647 - m.x92)**2 + (8.61550724971434 -
    m.x94)**2 + (4.93467653333678 - m.x96)**2 + 80.5431824405483 * m.b49
    <= 81.5431824405483)
m.e180 = Constraint(expr= (6.61159251106337 - m.x92)**2 + (9.89217063451911 -
    m.x94)**2 + (4.74850918126831 - m.x96)**2 + 90.8634617423464 * m.b50
    <= 91.8634617423464)
m.e181 = Constraint(expr= m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47
    + m.b48 + m.b49 + m.b50 == 1)
m.e182 = Constraint(expr= (4.13263517293428 - m.x98)**2 + (9.89321475687716 -
    m.x100)**2 + (7.00543632985936 - m.x102)**2 + 89.4259075893627 * m.b51
    <= 90.4259075893627)
m.e183 = Constraint(expr= (5.36782363621885 - m.x98)**2 + (1.51651713640814 -
    m.x100)**2 + (6.16125243380265 - m.x102)**2 + 90.8634617423464 * m.b52
    <= 91.8634617423464)
m.e184 = Constraint(expr= (8.2275592328595 - m.x98)**2 + (4.51338886533517 -
    m.x100)**2 + (3.02091680975325 - m.x102)**2 + 77.2828440165495 * m.b53
    <= 78.2828440165495)
m.e185 = Constraint(expr= (4.45787019759725 - m.x98)**2 + (8.176601080562 -
    m.x100)**2 + (2.1384293807986 - m.x102)**2 + 94.0648155502126 * m.b54
    <= 95.0648155502126)
m.e186 = Constraint(expr= (8.002643257644 - m.x98)**2 + (5.28236491095606 -
    m.x100)**2 + (5.11938934174774 - m.x102)**2 + 68.4345962886061 * m.b55
    <= 69.4345962886061)
m.e187 = Constraint(expr= (6.24049438612365 - m.x98)**2 + (3.8120863088984 -
    m.x100)**2 + (9.50984985922338 - m.x102)**2 + 106.313114234833 * m.b56
    <= 107.313114234833)
m.e188 = Constraint(expr= (4.54775219913353 - m.x98)**2 + (5.50227429055218 -
    m.x100)**2 + (3.5032816165688 - m.x102)**2 + 54.7317080633338 * m.b57
    <= 55.7317080633338)
m.e189 = Constraint(expr= (1.674156677828 - m.x98)**2 + (4.99633600480765 -
    m.x100)**2 + (1.42648309916894 - m.x102)**2 + 106.313114234833 * m.b58
    <= 107.313114234833)
m.e190 = Constraint(expr= (1.82060210212647 - m.x98)**2 + (8.61550724971434 -
    m.x100)**2 + (4.93467653333678 - m.x102)**2 + 80.5431824405483 * m.b59
    <= 81.5431824405483)
m.e191 = Constraint(expr= (6.61159251106337 - m.x98)**2 + (9.89217063451911 -
    m.x100)**2 + (4.74850918126831 - m.x102)**2 + 90.8634617423464 * m.b60
    <= 91.8634617423464)
m.e192 = Constraint(expr= m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 + m.b57
    + m.b58 + m.b59 + m.b60 == 1)
m.e193 = Constraint(expr= (4.13263517293428 - m.x104)**2 + (9.89321475687716 -
    m.x106)**2 + (7.00543632985936 - m.x108)**2 + 89.4259075893627 * m.b61
    <= 90.4259075893627)
m.e194 = Constraint(expr= (5.36782363621885 - m.x104)**2 + (1.51651713640814 -
    m.x106)**2 + (6.16125243380265 - m.x108)**2 + 90.8634617423464 * m.b62
    <= 91.8634617423464)
m.e195 = Constraint(expr= (8.2275592328595 - m.x104)**2 + (4.51338886533517 -
    m.x106)**2 + (3.02091680975325 - m.x108)**2 + 77.2828440165495 * m.b63
    <= 78.2828440165495)
m.e196 = Constraint(expr= (4.45787019759725 - m.x104)**2 + (8.176601080562 -
    m.x106)**2 + (2.1384293807986 - m.x108)**2 + 94.0648155502126 * m.b64
    <= 95.0648155502126)
m.e197 = Constraint(expr= (8.002643257644 - m.x104)**2 + (5.28236491095606 -
    m.x106)**2 + (5.11938934174774 - m.x108)**2 + 68.4345962886061 * m.b65
    <= 69.4345962886061)
m.e198 = Constraint(expr= (6.24049438612365 - m.x104)**2 + (3.8120863088984 -
    m.x106)**2 + (9.50984985922338 - m.x108)**2 + 106.313114234833 * m.b66
    <= 107.313114234833)
m.e199 = Constraint(expr= (4.54775219913353 - m.x104)**2 + (5.50227429055218 -
    m.x106)**2 + (3.5032816165688 - m.x108)**2 + 54.7317080633338 * m.b67
    <= 55.7317080633338)
m.e200 = Constraint(expr= (1.674156677828 - m.x104)**2 + (4.99633600480765 -
    m.x106)**2 + (1.42648309916894 - m.x108)**2 + 106.313114234833 * m.b68
    <= 107.313114234833)
m.e201 = Constraint(expr= (1.82060210212647 - m.x104)**2 + (8.61550724971434 -
    m.x106)**2 + (4.93467653333678 - m.x108)**2 + 80.5431824405483 * m.b69
    <= 81.5431824405483)
m.e202 = Constraint(expr= (6.61159251106337 - m.x104)**2 + (9.89217063451911 -
    m.x106)**2 + (4.74850918126831 - m.x108)**2 + 90.8634617423464 * m.b70
    <= 91.8634617423464)
m.e203 = Constraint(expr= m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b66 + m.b67
    + m.b68 + m.b69 + m.b70 == 1)
m.e204 = Constraint(expr= m.b1 + m.b11 + m.b21 + m.b31 + m.b41 + m.b51 + m.b61
    <= 1)
m.e205 = Constraint(expr= m.b2 + m.b12 + m.b22 + m.b32 + m.b42 + m.b52 + m.b62
    <= 1)
m.e206 = Constraint(expr= m.b3 + m.b13 + m.b23 + m.b33 + m.b43 + m.b53 + m.b63
    <= 1)
m.e207 = Constraint(expr= m.b4 + m.b14 + m.b24 + m.b34 + m.b44 + m.b54 + m.b64
    <= 1)
m.e208 = Constraint(expr= m.b5 + m.b15 + m.b25 + m.b35 + m.b45 + m.b55 + m.b65
    <= 1)
m.e209 = Constraint(expr= m.b6 + m.b16 + m.b26 + m.b36 + m.b46 + m.b56 + m.b66
    <= 1)
m.e210 = Constraint(expr= m.b7 + m.b17 + m.b27 + m.b37 + m.b47 + m.b57 + m.b67
    <= 1)
m.e211 = Constraint(expr= m.b8 + m.b18 + m.b28 + m.b38 + m.b48 + m.b58 + m.b68
    <= 1)
m.e212 = Constraint(expr= m.b9 + m.b19 + m.b29 + m.b39 + m.b49 + m.b59 + m.b69
    <= 1)
m.e213 = Constraint(expr= m.b10 + m.b20 + m.b30 + m.b40 + m.b50 + m.b60 + m.b70
    <= 1)
m.e214 = Constraint(expr= m.x71 - m.x72 <= 0)
m.e215 = Constraint(expr= m.x72 - m.x80 <= 0)
m.e216 = Constraint(expr= m.x80 - m.x86 <= 0)
m.e217 = Constraint(expr= m.x86 - m.x92 <= 0)
m.e218 = Constraint(expr= m.x92 - m.x98 <= 0)
m.e219 = Constraint(expr= m.x98 - m.x104 <= 0)
