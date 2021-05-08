# MINLP written by GAMS Convert at 05/07/21 17:12:59
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       219       15        0      204        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       180      130       50        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       688      538      150
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
m.x51 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x52 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x53 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x54 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x55 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x56 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x57 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x58 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x59 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x60 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x61 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x62 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x63 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x64 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x65 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x66 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x67 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x68 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x69 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x70 = Var(within=Reals, bounds=(0,10), initialize=0)
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
m.x155 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x156 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x157 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x158 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x159 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x160 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x161 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x162 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x163 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x164 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x165 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x166 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x167 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x168 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x169 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x170 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x171 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x172 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x173 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x174 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x175 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x176 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x177 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x178 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x179 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x180 = Var(within=Reals, bounds=(0,10), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x53 + m.x56 + m.x58 + m.x60 + m.x62
    + m.x64 + m.x66 + m.x68 + m.x69 + m.x70 + m.x71 + m.x72 + m.x73 + m.x74 +
    m.x75 + m.x76 + m.x77 + m.x78 + m.x79 + m.x80)

m.e1 = Constraint(expr= m.x51 - m.x52 - m.x53 <= 0)
m.e2 = Constraint(expr= -m.x51 + m.x52 - m.x53 <= 0)
m.e3 = Constraint(expr= m.x54 - m.x55 - m.x56 <= 0)
m.e4 = Constraint(expr= -m.x54 + m.x55 - m.x56 <= 0)
m.e5 = Constraint(expr= m.x51 - m.x57 - m.x58 <= 0)
m.e6 = Constraint(expr= -m.x51 + m.x57 - m.x58 <= 0)
m.e7 = Constraint(expr= m.x54 - m.x59 - m.x60 <= 0)
m.e8 = Constraint(expr= -m.x54 + m.x59 - m.x60 <= 0)
m.e9 = Constraint(expr= m.x51 - m.x61 - m.x62 <= 0)
m.e10 = Constraint(expr= -m.x51 + m.x61 - m.x62 <= 0)
m.e11 = Constraint(expr= m.x54 - m.x63 - m.x64 <= 0)
m.e12 = Constraint(expr= -m.x54 + m.x63 - m.x64 <= 0)
m.e13 = Constraint(expr= m.x51 - m.x65 - m.x66 <= 0)
m.e14 = Constraint(expr= -m.x51 + m.x65 - m.x66 <= 0)
m.e15 = Constraint(expr= m.x54 - m.x67 - m.x68 <= 0)
m.e16 = Constraint(expr= -m.x54 + m.x67 - m.x68 <= 0)
m.e17 = Constraint(expr= m.x52 - m.x57 - m.x69 <= 0)
m.e18 = Constraint(expr= -m.x52 + m.x57 - m.x69 <= 0)
m.e19 = Constraint(expr= m.x55 - m.x59 - m.x70 <= 0)
m.e20 = Constraint(expr= -m.x55 + m.x59 - m.x70 <= 0)
m.e21 = Constraint(expr= m.x52 - m.x61 - m.x71 <= 0)
m.e22 = Constraint(expr= -m.x52 + m.x61 - m.x71 <= 0)
m.e23 = Constraint(expr= m.x55 - m.x63 - m.x72 <= 0)
m.e24 = Constraint(expr= -m.x55 + m.x63 - m.x72 <= 0)
m.e25 = Constraint(expr= m.x52 - m.x65 - m.x73 <= 0)
m.e26 = Constraint(expr= -m.x52 + m.x65 - m.x73 <= 0)
m.e27 = Constraint(expr= m.x55 - m.x67 - m.x74 <= 0)
m.e28 = Constraint(expr= -m.x55 + m.x67 - m.x74 <= 0)
m.e29 = Constraint(expr= m.x57 - m.x61 - m.x75 <= 0)
m.e30 = Constraint(expr= -m.x57 + m.x61 - m.x75 <= 0)
m.e31 = Constraint(expr= m.x59 - m.x63 - m.x76 <= 0)
m.e32 = Constraint(expr= -m.x59 + m.x63 - m.x76 <= 0)
m.e33 = Constraint(expr= m.x57 - m.x65 - m.x77 <= 0)
m.e34 = Constraint(expr= -m.x57 + m.x65 - m.x77 <= 0)
m.e35 = Constraint(expr= m.x59 - m.x67 - m.x78 <= 0)
m.e36 = Constraint(expr= -m.x59 + m.x67 - m.x78 <= 0)
m.e37 = Constraint(expr= m.x61 - m.x65 - m.x79 <= 0)
m.e38 = Constraint(expr= -m.x61 + m.x65 - m.x79 <= 0)
m.e39 = Constraint(expr= m.x63 - m.x67 - m.x80 <= 0)
m.e40 = Constraint(expr= -m.x63 + m.x67 - m.x80 <= 0)
m.e41 = Constraint(expr= ((-m.x81 / (0.0001 + 0.9999 * m.b1) +
    0.648386267690458)**2 + (-m.x82 / (0.0001 + 0.9999 * m.b1) +
    5.34198386756466)**2 - 1) * (0.0001 + 0.9999 * m.b1) + 0.00279571963934506
    * m.b1 <= 0.00279571963934506)
m.e42 = Constraint(expr= ((-m.x83 / (0.0001 + 0.9999 * m.b2) + 0.38028139143083)
    **2 + (-m.x84 / (0.0001 + 0.9999 * m.b2) + 4.79200736168083)**2 - 1) * (
    0.0001 + 0.9999 * m.b2) + 0.00221079484910719 * m.b2
    <= 0.00221079484910719)
m.e43 = Constraint(expr= ((-m.x85 / (0.0001 + 0.9999 * m.b3) + 4.59553989190787)
    **2 + (-m.x86 / (0.0001 + 0.9999 * m.b3) + 2.92927044373959)**2 - 1) * (
    0.0001 + 0.9999 * m.b3) + 0.00286996122306829 * m.b3
    <= 0.00286996122306829)
m.e44 = Constraint(expr= ((-m.x87 / (0.0001 + 0.9999 * m.b4) + 7.79089239319392)
    **2 + (-m.x88 / (0.0001 + 0.9999 * m.b4) + 3.09688601355012)**2 - 1) * (
    0.0001 + 0.9999 * m.b4) + 0.00692887072632492 * m.b4
    <= 0.00692887072632492)
m.e45 = Constraint(expr= ((-m.x89 / (0.0001 + 0.9999 * m.b5) + 2.20597420581599)
    **2 + (-m.x90 / (0.0001 + 0.9999 * m.b5) + 0.880296019425143)**2 - 1) * (
    0.0001 + 0.9999 * m.b5) + 0.000464124327854123 * m.b5
    <= 0.000464124327854123)
m.e46 = Constraint(expr= ((-m.x91 / (0.0001 + 0.9999 * m.b6) + 4.31093077060147)
    **2 + (-m.x92 / (0.0001 + 0.9999 * m.b6) + 5.42555328385657)**2 - 1) * (
    0.0001 + 0.9999 * m.b6) + 0.00470207525448854 * m.b6
    <= 0.00470207525448854)
m.e47 = Constraint(expr= ((-m.x93 / (0.0001 + 0.9999 * m.b7) + 8.68776252232421)
    **2 + (-m.x94 / (0.0001 + 0.9999 * m.b7) + 7.42106012944621)**2 - 1) * (
    0.0001 + 0.9999 * m.b7) + 0.0129549351089157 * m.b7 <= 0.0129549351089157)
m.e48 = Constraint(expr= ((-m.x95 / (0.0001 + 0.9999 * m.b8) + 3.86794113528858)
    **2 + (-m.x96 / (0.0001 + 0.9999 * m.b8) + 9.34863265837716)**2 - 1) * (
    0.0001 + 0.9999 * m.b8) + 0.0101357901207334 * m.b8 <= 0.0101357901207334)
m.e49 = Constraint(expr= ((-m.x97 / (0.0001 + 0.9999 * m.b9) + 8.94294324678777)
    **2 + (-m.x98 / (0.0001 + 0.9999 * m.b9) + 0.712193380632226)**2 - 1) * (
    0.0001 + 0.9999 * m.b9) + 0.00794834533266834 * m.b9
    <= 0.00794834533266834)
m.e50 = Constraint(expr= ((-m.x99 / (0.0001 + 0.9999 * m.b10) +
    1.56734614217404)**2 + (-m.x100 / (0.0001 + 0.9999 * m.b10) +
    5.6469805099144)**2 - 1) * (0.0001 + 0.9999 * m.b10) + 0.00333449628087409
    * m.b10 <= 0.00333449628087409)
m.e51 = Constraint(expr= m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8
    + m.b9 + m.b10 == 1)
m.e52 = Constraint(expr= ((-m.x101 / (0.0001 + 0.9999 * m.b11) +
    0.648386267690458)**2 + (-m.x102 / (0.0001 + 0.9999 * m.b11) +
    5.34198386756466)**2 - 1) * (0.0001 + 0.9999 * m.b11) + 0.00279571963934506
    * m.b11 <= 0.00279571963934506)
m.e53 = Constraint(expr= ((-m.x103 / (0.0001 + 0.9999 * m.b12) +
    0.38028139143083)**2 + (-m.x104 / (0.0001 + 0.9999 * m.b12) +
    4.79200736168083)**2 - 1) * (0.0001 + 0.9999 * m.b12) + 0.00221079484910719
    * m.b12 <= 0.00221079484910719)
m.e54 = Constraint(expr= ((-m.x105 / (0.0001 + 0.9999 * m.b13) +
    4.59553989190787)**2 + (-m.x106 / (0.0001 + 0.9999 * m.b13) +
    2.92927044373959)**2 - 1) * (0.0001 + 0.9999 * m.b13) + 0.00286996122306829
    * m.b13 <= 0.00286996122306829)
m.e55 = Constraint(expr= ((-m.x107 / (0.0001 + 0.9999 * m.b14) +
    7.79089239319392)**2 + (-m.x108 / (0.0001 + 0.9999 * m.b14) +
    3.09688601355012)**2 - 1) * (0.0001 + 0.9999 * m.b14) + 0.00692887072632492
    * m.b14 <= 0.00692887072632492)
m.e56 = Constraint(expr= ((-m.x109 / (0.0001 + 0.9999 * m.b15) +
    2.20597420581599)**2 + (-m.x110 / (0.0001 + 0.9999 * m.b15) +
    0.880296019425143)**2 - 1) * (0.0001 + 0.9999 * m.b15) +
    0.000464124327854123 * m.b15 <= 0.000464124327854123)
m.e57 = Constraint(expr= ((-m.x111 / (0.0001 + 0.9999 * m.b16) +
    4.31093077060147)**2 + (-m.x112 / (0.0001 + 0.9999 * m.b16) +
    5.42555328385657)**2 - 1) * (0.0001 + 0.9999 * m.b16) + 0.00470207525448854
    * m.b16 <= 0.00470207525448854)
m.e58 = Constraint(expr= ((-m.x113 / (0.0001 + 0.9999 * m.b17) +
    8.68776252232421)**2 + (-m.x114 / (0.0001 + 0.9999 * m.b17) +
    7.42106012944621)**2 - 1) * (0.0001 + 0.9999 * m.b17) + 0.0129549351089157
    * m.b17 <= 0.0129549351089157)
m.e59 = Constraint(expr= ((-m.x115 / (0.0001 + 0.9999 * m.b18) +
    3.86794113528858)**2 + (-m.x116 / (0.0001 + 0.9999 * m.b18) +
    9.34863265837716)**2 - 1) * (0.0001 + 0.9999 * m.b18) + 0.0101357901207334
    * m.b18 <= 0.0101357901207334)
m.e60 = Constraint(expr= ((-m.x117 / (0.0001 + 0.9999 * m.b19) +
    8.94294324678777)**2 + (-m.x118 / (0.0001 + 0.9999 * m.b19) +
    0.712193380632226)**2 - 1) * (0.0001 + 0.9999 * m.b19) +
    0.00794834533266834 * m.b19 <= 0.00794834533266834)
m.e61 = Constraint(expr= ((-m.x119 / (0.0001 + 0.9999 * m.b20) +
    1.56734614217404)**2 + (-m.x120 / (0.0001 + 0.9999 * m.b20) +
    5.6469805099144)**2 - 1) * (0.0001 + 0.9999 * m.b20) + 0.00333449628087409
    * m.b20 <= 0.00333449628087409)
m.e62 = Constraint(expr= m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17
    + m.b18 + m.b19 + m.b20 == 1)
m.e63 = Constraint(expr= ((-m.x121 / (0.0001 + 0.9999 * m.b21) +
    0.648386267690458)**2 + (-m.x122 / (0.0001 + 0.9999 * m.b21) +
    5.34198386756466)**2 - 1) * (0.0001 + 0.9999 * m.b21) + 0.00279571963934506
    * m.b21 <= 0.00279571963934506)
m.e64 = Constraint(expr= ((-m.x123 / (0.0001 + 0.9999 * m.b22) +
    0.38028139143083)**2 + (-m.x124 / (0.0001 + 0.9999 * m.b22) +
    4.79200736168083)**2 - 1) * (0.0001 + 0.9999 * m.b22) + 0.00221079484910719
    * m.b22 <= 0.00221079484910719)
m.e65 = Constraint(expr= ((-m.x125 / (0.0001 + 0.9999 * m.b23) +
    4.59553989190787)**2 + (-m.x126 / (0.0001 + 0.9999 * m.b23) +
    2.92927044373959)**2 - 1) * (0.0001 + 0.9999 * m.b23) + 0.00286996122306829
    * m.b23 <= 0.00286996122306829)
m.e66 = Constraint(expr= ((-m.x127 / (0.0001 + 0.9999 * m.b24) +
    7.79089239319392)**2 + (-m.x128 / (0.0001 + 0.9999 * m.b24) +
    3.09688601355012)**2 - 1) * (0.0001 + 0.9999 * m.b24) + 0.00692887072632492
    * m.b24 <= 0.00692887072632492)
m.e67 = Constraint(expr= ((-m.x129 / (0.0001 + 0.9999 * m.b25) +
    2.20597420581599)**2 + (-m.x130 / (0.0001 + 0.9999 * m.b25) +
    0.880296019425143)**2 - 1) * (0.0001 + 0.9999 * m.b25) +
    0.000464124327854123 * m.b25 <= 0.000464124327854123)
m.e68 = Constraint(expr= ((-m.x131 / (0.0001 + 0.9999 * m.b26) +
    4.31093077060147)**2 + (-m.x132 / (0.0001 + 0.9999 * m.b26) +
    5.42555328385657)**2 - 1) * (0.0001 + 0.9999 * m.b26) + 0.00470207525448854
    * m.b26 <= 0.00470207525448854)
m.e69 = Constraint(expr= ((-m.x133 / (0.0001 + 0.9999 * m.b27) +
    8.68776252232421)**2 + (-m.x134 / (0.0001 + 0.9999 * m.b27) +
    7.42106012944621)**2 - 1) * (0.0001 + 0.9999 * m.b27) + 0.0129549351089157
    * m.b27 <= 0.0129549351089157)
m.e70 = Constraint(expr= ((-m.x135 / (0.0001 + 0.9999 * m.b28) +
    3.86794113528858)**2 + (-m.x136 / (0.0001 + 0.9999 * m.b28) +
    9.34863265837716)**2 - 1) * (0.0001 + 0.9999 * m.b28) + 0.0101357901207334
    * m.b28 <= 0.0101357901207334)
m.e71 = Constraint(expr= ((-m.x137 / (0.0001 + 0.9999 * m.b29) +
    8.94294324678777)**2 + (-m.x138 / (0.0001 + 0.9999 * m.b29) +
    0.712193380632226)**2 - 1) * (0.0001 + 0.9999 * m.b29) +
    0.00794834533266834 * m.b29 <= 0.00794834533266834)
m.e72 = Constraint(expr= ((-m.x139 / (0.0001 + 0.9999 * m.b30) +
    1.56734614217404)**2 + (-m.x140 / (0.0001 + 0.9999 * m.b30) +
    5.6469805099144)**2 - 1) * (0.0001 + 0.9999 * m.b30) + 0.00333449628087409
    * m.b30 <= 0.00333449628087409)
m.e73 = Constraint(expr= m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 + m.b27
    + m.b28 + m.b29 + m.b30 == 1)
m.e74 = Constraint(expr= ((-m.x141 / (0.0001 + 0.9999 * m.b31) +
    0.648386267690458)**2 + (-m.x142 / (0.0001 + 0.9999 * m.b31) +
    5.34198386756466)**2 - 1) * (0.0001 + 0.9999 * m.b31) + 0.00279571963934506
    * m.b31 <= 0.00279571963934506)
m.e75 = Constraint(expr= ((-m.x143 / (0.0001 + 0.9999 * m.b32) +
    0.38028139143083)**2 + (-m.x144 / (0.0001 + 0.9999 * m.b32) +
    4.79200736168083)**2 - 1) * (0.0001 + 0.9999 * m.b32) + 0.00221079484910719
    * m.b32 <= 0.00221079484910719)
m.e76 = Constraint(expr= ((-m.x145 / (0.0001 + 0.9999 * m.b33) +
    4.59553989190787)**2 + (-m.x146 / (0.0001 + 0.9999 * m.b33) +
    2.92927044373959)**2 - 1) * (0.0001 + 0.9999 * m.b33) + 0.00286996122306829
    * m.b33 <= 0.00286996122306829)
m.e77 = Constraint(expr= ((-m.x147 / (0.0001 + 0.9999 * m.b34) +
    7.79089239319392)**2 + (-m.x148 / (0.0001 + 0.9999 * m.b34) +
    3.09688601355012)**2 - 1) * (0.0001 + 0.9999 * m.b34) + 0.00692887072632492
    * m.b34 <= 0.00692887072632492)
m.e78 = Constraint(expr= ((-m.x149 / (0.0001 + 0.9999 * m.b35) +
    2.20597420581599)**2 + (-m.x150 / (0.0001 + 0.9999 * m.b35) +
    0.880296019425143)**2 - 1) * (0.0001 + 0.9999 * m.b35) +
    0.000464124327854123 * m.b35 <= 0.000464124327854123)
m.e79 = Constraint(expr= ((-m.x151 / (0.0001 + 0.9999 * m.b36) +
    4.31093077060147)**2 + (-m.x152 / (0.0001 + 0.9999 * m.b36) +
    5.42555328385657)**2 - 1) * (0.0001 + 0.9999 * m.b36) + 0.00470207525448854
    * m.b36 <= 0.00470207525448854)
m.e80 = Constraint(expr= ((-m.x153 / (0.0001 + 0.9999 * m.b37) +
    8.68776252232421)**2 + (-m.x154 / (0.0001 + 0.9999 * m.b37) +
    7.42106012944621)**2 - 1) * (0.0001 + 0.9999 * m.b37) + 0.0129549351089157
    * m.b37 <= 0.0129549351089157)
m.e81 = Constraint(expr= ((-m.x155 / (0.0001 + 0.9999 * m.b38) +
    3.86794113528858)**2 + (-m.x156 / (0.0001 + 0.9999 * m.b38) +
    9.34863265837716)**2 - 1) * (0.0001 + 0.9999 * m.b38) + 0.0101357901207334
    * m.b38 <= 0.0101357901207334)
m.e82 = Constraint(expr= ((-m.x157 / (0.0001 + 0.9999 * m.b39) +
    8.94294324678777)**2 + (-m.x158 / (0.0001 + 0.9999 * m.b39) +
    0.712193380632226)**2 - 1) * (0.0001 + 0.9999 * m.b39) +
    0.00794834533266834 * m.b39 <= 0.00794834533266834)
m.e83 = Constraint(expr= ((-m.x159 / (0.0001 + 0.9999 * m.b40) +
    1.56734614217404)**2 + (-m.x160 / (0.0001 + 0.9999 * m.b40) +
    5.6469805099144)**2 - 1) * (0.0001 + 0.9999 * m.b40) + 0.00333449628087409
    * m.b40 <= 0.00333449628087409)
m.e84 = Constraint(expr= m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 + m.b37
    + m.b38 + m.b39 + m.b40 == 1)
m.e85 = Constraint(expr= ((-m.x161 / (0.0001 + 0.9999 * m.b41) +
    0.648386267690458)**2 + (-m.x162 / (0.0001 + 0.9999 * m.b41) +
    5.34198386756466)**2 - 1) * (0.0001 + 0.9999 * m.b41) + 0.00279571963934506
    * m.b41 <= 0.00279571963934506)
m.e86 = Constraint(expr= ((-m.x163 / (0.0001 + 0.9999 * m.b42) +
    0.38028139143083)**2 + (-m.x164 / (0.0001 + 0.9999 * m.b42) +
    4.79200736168083)**2 - 1) * (0.0001 + 0.9999 * m.b42) + 0.00221079484910719
    * m.b42 <= 0.00221079484910719)
m.e87 = Constraint(expr= ((-m.x165 / (0.0001 + 0.9999 * m.b43) +
    4.59553989190787)**2 + (-m.x166 / (0.0001 + 0.9999 * m.b43) +
    2.92927044373959)**2 - 1) * (0.0001 + 0.9999 * m.b43) + 0.00286996122306829
    * m.b43 <= 0.00286996122306829)
m.e88 = Constraint(expr= ((-m.x167 / (0.0001 + 0.9999 * m.b44) +
    7.79089239319392)**2 + (-m.x168 / (0.0001 + 0.9999 * m.b44) +
    3.09688601355012)**2 - 1) * (0.0001 + 0.9999 * m.b44) + 0.00692887072632492
    * m.b44 <= 0.00692887072632492)
m.e89 = Constraint(expr= ((-m.x169 / (0.0001 + 0.9999 * m.b45) +
    2.20597420581599)**2 + (-m.x170 / (0.0001 + 0.9999 * m.b45) +
    0.880296019425143)**2 - 1) * (0.0001 + 0.9999 * m.b45) +
    0.000464124327854123 * m.b45 <= 0.000464124327854123)
m.e90 = Constraint(expr= ((-m.x171 / (0.0001 + 0.9999 * m.b46) +
    4.31093077060147)**2 + (-m.x172 / (0.0001 + 0.9999 * m.b46) +
    5.42555328385657)**2 - 1) * (0.0001 + 0.9999 * m.b46) + 0.00470207525448854
    * m.b46 <= 0.00470207525448854)
m.e91 = Constraint(expr= ((-m.x173 / (0.0001 + 0.9999 * m.b47) +
    8.68776252232421)**2 + (-m.x174 / (0.0001 + 0.9999 * m.b47) +
    7.42106012944621)**2 - 1) * (0.0001 + 0.9999 * m.b47) + 0.0129549351089157
    * m.b47 <= 0.0129549351089157)
m.e92 = Constraint(expr= ((-m.x175 / (0.0001 + 0.9999 * m.b48) +
    3.86794113528858)**2 + (-m.x176 / (0.0001 + 0.9999 * m.b48) +
    9.34863265837716)**2 - 1) * (0.0001 + 0.9999 * m.b48) + 0.0101357901207334
    * m.b48 <= 0.0101357901207334)
m.e93 = Constraint(expr= ((-m.x177 / (0.0001 + 0.9999 * m.b49) +
    8.94294324678777)**2 + (-m.x178 / (0.0001 + 0.9999 * m.b49) +
    0.712193380632226)**2 - 1) * (0.0001 + 0.9999 * m.b49) +
    0.00794834533266834 * m.b49 <= 0.00794834533266834)
m.e94 = Constraint(expr= ((-m.x179 / (0.0001 + 0.9999 * m.b50) +
    1.56734614217404)**2 + (-m.x180 / (0.0001 + 0.9999 * m.b50) +
    5.6469805099144)**2 - 1) * (0.0001 + 0.9999 * m.b50) + 0.00333449628087409
    * m.b50 <= 0.00333449628087409)
m.e95 = Constraint(expr= m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47
    + m.b48 + m.b49 + m.b50 == 1)
m.e96 = Constraint(expr= m.b1 + m.b11 + m.b21 + m.b31 + m.b41 <= 1)
m.e97 = Constraint(expr= m.b2 + m.b12 + m.b22 + m.b32 + m.b42 <= 1)
m.e98 = Constraint(expr= m.b3 + m.b13 + m.b23 + m.b33 + m.b43 <= 1)
m.e99 = Constraint(expr= m.b4 + m.b14 + m.b24 + m.b34 + m.b44 <= 1)
m.e100 = Constraint(expr= m.b5 + m.b15 + m.b25 + m.b35 + m.b45 <= 1)
m.e101 = Constraint(expr= m.b6 + m.b16 + m.b26 + m.b36 + m.b46 <= 1)
m.e102 = Constraint(expr= m.b7 + m.b17 + m.b27 + m.b37 + m.b47 <= 1)
m.e103 = Constraint(expr= m.b8 + m.b18 + m.b28 + m.b38 + m.b48 <= 1)
m.e104 = Constraint(expr= m.b9 + m.b19 + m.b29 + m.b39 + m.b49 <= 1)
m.e105 = Constraint(expr= m.b10 + m.b20 + m.b30 + m.b40 + m.b50 <= 1)
m.e106 = Constraint(expr= -m.x51 + m.x81 + m.x83 + m.x85 + m.x87 + m.x89 +
    m.x91 + m.x93 + m.x95 + m.x97 + m.x99 == 0)
m.e107 = Constraint(expr= -m.x54 + m.x82 + m.x84 + m.x86 + m.x88 + m.x90 +
    m.x92 + m.x94 + m.x96 + m.x98 + m.x100 == 0)
m.e108 = Constraint(expr= -m.x52 + m.x101 + m.x103 + m.x105 + m.x107 + m.x109
    + m.x111 + m.x113 + m.x115 + m.x117 + m.x119 == 0)
m.e109 = Constraint(expr= -m.x55 + m.x102 + m.x104 + m.x106 + m.x108 + m.x110
    + m.x112 + m.x114 + m.x116 + m.x118 + m.x120 == 0)
m.e110 = Constraint(expr= -m.x57 + m.x121 + m.x123 + m.x125 + m.x127 + m.x129
    + m.x131 + m.x133 + m.x135 + m.x137 + m.x139 == 0)
m.e111 = Constraint(expr= -m.x59 + m.x122 + m.x124 + m.x126 + m.x128 + m.x130
    + m.x132 + m.x134 + m.x136 + m.x138 + m.x140 == 0)
m.e112 = Constraint(expr= -m.x61 + m.x141 + m.x143 + m.x145 + m.x147 + m.x149
    + m.x151 + m.x153 + m.x155 + m.x157 + m.x159 == 0)
m.e113 = Constraint(expr= -m.x63 + m.x142 + m.x144 + m.x146 + m.x148 + m.x150
    + m.x152 + m.x154 + m.x156 + m.x158 + m.x160 == 0)
m.e114 = Constraint(expr= -m.x65 + m.x161 + m.x163 + m.x165 + m.x167 + m.x169
    + m.x171 + m.x173 + m.x175 + m.x177 + m.x179 == 0)
m.e115 = Constraint(expr= -m.x67 + m.x162 + m.x164 + m.x166 + m.x168 + m.x170
    + m.x172 + m.x174 + m.x176 + m.x178 + m.x180 == 0)
m.e116 = Constraint(expr= -10 * m.b1 + m.x81 <= 0)
m.e117 = Constraint(expr= -10 * m.b2 + m.x83 <= 0)
m.e118 = Constraint(expr= -10 * m.b3 + m.x85 <= 0)
m.e119 = Constraint(expr= -10 * m.b4 + m.x87 <= 0)
m.e120 = Constraint(expr= -10 * m.b5 + m.x89 <= 0)
m.e121 = Constraint(expr= -10 * m.b6 + m.x91 <= 0)
m.e122 = Constraint(expr= -10 * m.b7 + m.x93 <= 0)
m.e123 = Constraint(expr= -10 * m.b8 + m.x95 <= 0)
m.e124 = Constraint(expr= -10 * m.b9 + m.x97 <= 0)
m.e125 = Constraint(expr= -10 * m.b10 + m.x99 <= 0)
m.e126 = Constraint(expr= -10 * m.b1 + m.x82 <= 0)
m.e127 = Constraint(expr= -10 * m.b2 + m.x84 <= 0)
m.e128 = Constraint(expr= -10 * m.b3 + m.x86 <= 0)
m.e129 = Constraint(expr= -10 * m.b4 + m.x88 <= 0)
m.e130 = Constraint(expr= -10 * m.b5 + m.x90 <= 0)
m.e131 = Constraint(expr= -10 * m.b6 + m.x92 <= 0)
m.e132 = Constraint(expr= -10 * m.b7 + m.x94 <= 0)
m.e133 = Constraint(expr= -10 * m.b8 + m.x96 <= 0)
m.e134 = Constraint(expr= -10 * m.b9 + m.x98 <= 0)
m.e135 = Constraint(expr= -10 * m.b10 + m.x100 <= 0)
m.e136 = Constraint(expr= -10 * m.b11 + m.x101 <= 0)
m.e137 = Constraint(expr= -10 * m.b12 + m.x103 <= 0)
m.e138 = Constraint(expr= -10 * m.b13 + m.x105 <= 0)
m.e139 = Constraint(expr= -10 * m.b14 + m.x107 <= 0)
m.e140 = Constraint(expr= -10 * m.b15 + m.x109 <= 0)
m.e141 = Constraint(expr= -10 * m.b16 + m.x111 <= 0)
m.e142 = Constraint(expr= -10 * m.b17 + m.x113 <= 0)
m.e143 = Constraint(expr= -10 * m.b18 + m.x115 <= 0)
m.e144 = Constraint(expr= -10 * m.b19 + m.x117 <= 0)
m.e145 = Constraint(expr= -10 * m.b20 + m.x119 <= 0)
m.e146 = Constraint(expr= -10 * m.b11 + m.x102 <= 0)
m.e147 = Constraint(expr= -10 * m.b12 + m.x104 <= 0)
m.e148 = Constraint(expr= -10 * m.b13 + m.x106 <= 0)
m.e149 = Constraint(expr= -10 * m.b14 + m.x108 <= 0)
m.e150 = Constraint(expr= -10 * m.b15 + m.x110 <= 0)
m.e151 = Constraint(expr= -10 * m.b16 + m.x112 <= 0)
m.e152 = Constraint(expr= -10 * m.b17 + m.x114 <= 0)
m.e153 = Constraint(expr= -10 * m.b18 + m.x116 <= 0)
m.e154 = Constraint(expr= -10 * m.b19 + m.x118 <= 0)
m.e155 = Constraint(expr= -10 * m.b20 + m.x120 <= 0)
m.e156 = Constraint(expr= -10 * m.b21 + m.x121 <= 0)
m.e157 = Constraint(expr= -10 * m.b22 + m.x123 <= 0)
m.e158 = Constraint(expr= -10 * m.b23 + m.x125 <= 0)
m.e159 = Constraint(expr= -10 * m.b24 + m.x127 <= 0)
m.e160 = Constraint(expr= -10 * m.b25 + m.x129 <= 0)
m.e161 = Constraint(expr= -10 * m.b26 + m.x131 <= 0)
m.e162 = Constraint(expr= -10 * m.b27 + m.x133 <= 0)
m.e163 = Constraint(expr= -10 * m.b28 + m.x135 <= 0)
m.e164 = Constraint(expr= -10 * m.b29 + m.x137 <= 0)
m.e165 = Constraint(expr= -10 * m.b30 + m.x139 <= 0)
m.e166 = Constraint(expr= -10 * m.b21 + m.x122 <= 0)
m.e167 = Constraint(expr= -10 * m.b22 + m.x124 <= 0)
m.e168 = Constraint(expr= -10 * m.b23 + m.x126 <= 0)
m.e169 = Constraint(expr= -10 * m.b24 + m.x128 <= 0)
m.e170 = Constraint(expr= -10 * m.b25 + m.x130 <= 0)
m.e171 = Constraint(expr= -10 * m.b26 + m.x132 <= 0)
m.e172 = Constraint(expr= -10 * m.b27 + m.x134 <= 0)
m.e173 = Constraint(expr= -10 * m.b28 + m.x136 <= 0)
m.e174 = Constraint(expr= -10 * m.b29 + m.x138 <= 0)
m.e175 = Constraint(expr= -10 * m.b30 + m.x140 <= 0)
m.e176 = Constraint(expr= -10 * m.b31 + m.x141 <= 0)
m.e177 = Constraint(expr= -10 * m.b32 + m.x143 <= 0)
m.e178 = Constraint(expr= -10 * m.b33 + m.x145 <= 0)
m.e179 = Constraint(expr= -10 * m.b34 + m.x147 <= 0)
m.e180 = Constraint(expr= -10 * m.b35 + m.x149 <= 0)
m.e181 = Constraint(expr= -10 * m.b36 + m.x151 <= 0)
m.e182 = Constraint(expr= -10 * m.b37 + m.x153 <= 0)
m.e183 = Constraint(expr= -10 * m.b38 + m.x155 <= 0)
m.e184 = Constraint(expr= -10 * m.b39 + m.x157 <= 0)
m.e185 = Constraint(expr= -10 * m.b40 + m.x159 <= 0)
m.e186 = Constraint(expr= -10 * m.b31 + m.x142 <= 0)
m.e187 = Constraint(expr= -10 * m.b32 + m.x144 <= 0)
m.e188 = Constraint(expr= -10 * m.b33 + m.x146 <= 0)
m.e189 = Constraint(expr= -10 * m.b34 + m.x148 <= 0)
m.e190 = Constraint(expr= -10 * m.b35 + m.x150 <= 0)
m.e191 = Constraint(expr= -10 * m.b36 + m.x152 <= 0)
m.e192 = Constraint(expr= -10 * m.b37 + m.x154 <= 0)
m.e193 = Constraint(expr= -10 * m.b38 + m.x156 <= 0)
m.e194 = Constraint(expr= -10 * m.b39 + m.x158 <= 0)
m.e195 = Constraint(expr= -10 * m.b40 + m.x160 <= 0)
m.e196 = Constraint(expr= -10 * m.b41 + m.x161 <= 0)
m.e197 = Constraint(expr= -10 * m.b42 + m.x163 <= 0)
m.e198 = Constraint(expr= -10 * m.b43 + m.x165 <= 0)
m.e199 = Constraint(expr= -10 * m.b44 + m.x167 <= 0)
m.e200 = Constraint(expr= -10 * m.b45 + m.x169 <= 0)
m.e201 = Constraint(expr= -10 * m.b46 + m.x171 <= 0)
m.e202 = Constraint(expr= -10 * m.b47 + m.x173 <= 0)
m.e203 = Constraint(expr= -10 * m.b48 + m.x175 <= 0)
m.e204 = Constraint(expr= -10 * m.b49 + m.x177 <= 0)
m.e205 = Constraint(expr= -10 * m.b50 + m.x179 <= 0)
m.e206 = Constraint(expr= -10 * m.b41 + m.x162 <= 0)
m.e207 = Constraint(expr= -10 * m.b42 + m.x164 <= 0)
m.e208 = Constraint(expr= -10 * m.b43 + m.x166 <= 0)
m.e209 = Constraint(expr= -10 * m.b44 + m.x168 <= 0)
m.e210 = Constraint(expr= -10 * m.b45 + m.x170 <= 0)
m.e211 = Constraint(expr= -10 * m.b46 + m.x172 <= 0)
m.e212 = Constraint(expr= -10 * m.b47 + m.x174 <= 0)
m.e213 = Constraint(expr= -10 * m.b48 + m.x176 <= 0)
m.e214 = Constraint(expr= -10 * m.b49 + m.x178 <= 0)
m.e215 = Constraint(expr= -10 * m.b50 + m.x180 <= 0)
m.e216 = Constraint(expr= m.x51 - m.x52 <= 0)
m.e217 = Constraint(expr= m.x52 - m.x57 <= 0)
m.e218 = Constraint(expr= m.x57 - m.x61 <= 0)
m.e219 = Constraint(expr= m.x61 - m.x65 <= 0)
