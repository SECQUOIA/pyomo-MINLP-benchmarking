# MINLP written by GAMS Convert at 05/07/21 17:13:00
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       299       15        0      284        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       255      180       75        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       963      738      225
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
m.b71 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b72 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b73 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b74 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b75 = Var(within=Binary, bounds=(0,1), initialize=0)
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
m.x181 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x182 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x183 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x184 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x185 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x186 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x187 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x188 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x189 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x190 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x191 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x192 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x193 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x194 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x195 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x196 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x197 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x198 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x199 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x200 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x201 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x202 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x203 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x204 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x205 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x206 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x207 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x208 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x209 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x210 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x211 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x212 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x213 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x214 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x215 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x216 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x217 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x218 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x219 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x220 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x221 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x222 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x223 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x224 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x225 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x226 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x227 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x228 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x229 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x230 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x231 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x232 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x233 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x234 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x235 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x236 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x237 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x238 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x239 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x240 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x241 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x242 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x243 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x244 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x245 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x246 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x247 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x248 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x249 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x250 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x251 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x252 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x253 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x254 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x255 = Var(within=Reals, bounds=(0,10), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x78 + m.x81 + m.x83 + m.x85 + m.x87
    + m.x89 + m.x91 + m.x93 + m.x94 + m.x95 + m.x96 + m.x97 + m.x98 + m.x99 +
    m.x100 + m.x101 + m.x102 + m.x103 + m.x104 + m.x105)

m.e1 = Constraint(expr= m.x76 - m.x77 - m.x78 <= 0)
m.e2 = Constraint(expr= -m.x76 + m.x77 - m.x78 <= 0)
m.e3 = Constraint(expr= m.x79 - m.x80 - m.x81 <= 0)
m.e4 = Constraint(expr= -m.x79 + m.x80 - m.x81 <= 0)
m.e5 = Constraint(expr= m.x76 - m.x82 - m.x83 <= 0)
m.e6 = Constraint(expr= -m.x76 + m.x82 - m.x83 <= 0)
m.e7 = Constraint(expr= m.x79 - m.x84 - m.x85 <= 0)
m.e8 = Constraint(expr= -m.x79 + m.x84 - m.x85 <= 0)
m.e9 = Constraint(expr= m.x76 - m.x86 - m.x87 <= 0)
m.e10 = Constraint(expr= -m.x76 + m.x86 - m.x87 <= 0)
m.e11 = Constraint(expr= m.x79 - m.x88 - m.x89 <= 0)
m.e12 = Constraint(expr= -m.x79 + m.x88 - m.x89 <= 0)
m.e13 = Constraint(expr= m.x76 - m.x90 - m.x91 <= 0)
m.e14 = Constraint(expr= -m.x76 + m.x90 - m.x91 <= 0)
m.e15 = Constraint(expr= m.x79 - m.x92 - m.x93 <= 0)
m.e16 = Constraint(expr= -m.x79 + m.x92 - m.x93 <= 0)
m.e17 = Constraint(expr= m.x77 - m.x82 - m.x94 <= 0)
m.e18 = Constraint(expr= -m.x77 + m.x82 - m.x94 <= 0)
m.e19 = Constraint(expr= m.x80 - m.x84 - m.x95 <= 0)
m.e20 = Constraint(expr= -m.x80 + m.x84 - m.x95 <= 0)
m.e21 = Constraint(expr= m.x77 - m.x86 - m.x96 <= 0)
m.e22 = Constraint(expr= -m.x77 + m.x86 - m.x96 <= 0)
m.e23 = Constraint(expr= m.x80 - m.x88 - m.x97 <= 0)
m.e24 = Constraint(expr= -m.x80 + m.x88 - m.x97 <= 0)
m.e25 = Constraint(expr= m.x77 - m.x90 - m.x98 <= 0)
m.e26 = Constraint(expr= -m.x77 + m.x90 - m.x98 <= 0)
m.e27 = Constraint(expr= m.x80 - m.x92 - m.x99 <= 0)
m.e28 = Constraint(expr= -m.x80 + m.x92 - m.x99 <= 0)
m.e29 = Constraint(expr= m.x82 - m.x86 - m.x100 <= 0)
m.e30 = Constraint(expr= -m.x82 + m.x86 - m.x100 <= 0)
m.e31 = Constraint(expr= m.x84 - m.x88 - m.x101 <= 0)
m.e32 = Constraint(expr= -m.x84 + m.x88 - m.x101 <= 0)
m.e33 = Constraint(expr= m.x82 - m.x90 - m.x102 <= 0)
m.e34 = Constraint(expr= -m.x82 + m.x90 - m.x102 <= 0)
m.e35 = Constraint(expr= m.x84 - m.x92 - m.x103 <= 0)
m.e36 = Constraint(expr= -m.x84 + m.x92 - m.x103 <= 0)
m.e37 = Constraint(expr= m.x86 - m.x90 - m.x104 <= 0)
m.e38 = Constraint(expr= -m.x86 + m.x90 - m.x104 <= 0)
m.e39 = Constraint(expr= m.x88 - m.x92 - m.x105 <= 0)
m.e40 = Constraint(expr= -m.x88 + m.x92 - m.x105 <= 0)
m.e41 = Constraint(expr= ((-m.x106 / (0.0001 + 0.9999 * m.b1) +
    8.68340342427357)**2 + (-m.x107 / (0.0001 + 0.9999 * m.b1) +
    8.57974596088368)**2 - 1) * (0.0001 + 0.9999 * m.b1) + 0.0148013535781986 *
    m.b1 <= 0.0148013535781986)
m.e42 = Constraint(expr= ((-m.x108 / (0.0001 + 0.9999 * m.b2) +
    9.63614333912176)**2 + (-m.x109 / (0.0001 + 0.9999 * m.b2) +
    8.80176337918095)**2 - 1) * (0.0001 + 0.9999 * m.b2) + 0.0169326297035192 *
    m.b2 <= 0.0169326297035192)
m.e43 = Constraint(expr= ((-m.x110 / (0.0001 + 0.9999 * m.b3) +
    3.68142205418198)**2 + (-m.x111 / (0.0001 + 0.9999 * m.b3) +
    1.1692321814062)**2 - 1) * (0.0001 + 0.9999 * m.b3) + 0.00139199722350534 *
    m.b3 <= 0.00139199722350534)
m.e44 = Constraint(expr= ((-m.x112 / (0.0001 + 0.9999 * m.b4) + 9.7121756733827)
    **2 + (-m.x113 / (0.0001 + 0.9999 * m.b4) + 7.68772804421774)**2 - 1) * (
    0.0001 + 0.9999 * m.b4) + 0.0152427518792499 * m.b4 <= 0.0152427518792499)
m.e45 = Constraint(expr= ((-m.x114 / (0.0001 + 0.9999 * m.b5) + 3.2772228491781)
    **2 + (-m.x115 / (0.0001 + 0.9999 * m.b5) + 8.20105404549271)**2 - 1) * (
    0.0001 + 0.9999 * m.b5) + 0.00769974770602674 * m.b5
    <= 0.00769974770602674)
m.e46 = Constraint(expr= ((-m.x116 / (0.0001 + 0.9999 * m.b6) +
    8.95169370625893)**2 + (-m.x117 / (0.0001 + 0.9999 * m.b6) +
    5.71833771240185)**2 - 1) * (0.0001 + 0.9999 * m.b6) + 0.0111832206403753 *
    m.b6 <= 0.0111832206403753)
m.e47 = Constraint(expr= ((-m.x118 / (0.0001 + 0.9999 * m.b7) +
    6.39713701672676)**2 + (-m.x119 / (0.0001 + 0.9999 * m.b7) +
    2.19374777991393)**2 - 1) * (0.0001 + 0.9999 * m.b7) + 0.00447358913326531
    * m.b7 <= 0.00447358913326531)
m.e48 = Constraint(expr= ((-m.x120 / (0.0001 + 0.9999 * m.b8) +
    8.63324272987351)**2 + (-m.x121 / (0.0001 + 0.9999 * m.b8) +
    2.92174290170279)**2 - 1) * (0.0001 + 0.9999 * m.b8) + 0.00820694616165644
    * m.b8 <= 0.00820694616165644)
m.e49 = Constraint(expr= ((-m.x122 / (0.0001 + 0.9999 * m.b9) +
    3.63244627881363)**2 + (-m.x123 / (0.0001 + 0.9999 * m.b9) +
    1.91739848753332)**2 - 1) * (0.0001 + 0.9999 * m.b9) + 0.00158710829284621
    * m.b9 <= 0.00158710829284621)
m.e50 = Constraint(expr= ((-m.x124 / (0.0001 + 0.9999 * m.b10) +
    0.303084489788861)**2 + (-m.x125 / (0.0001 + 0.9999 * m.b10) +
    2.88588654972735)**2 - 1) * (0.0001 + 0.9999 * m.b10) + 0.00074202013858478
    * m.b10 <= 0.00074202013858478)
m.e51 = Constraint(expr= ((-m.x126 / (0.0001 + 0.9999 * m.b11) +
    9.32557624217471)**2 + (-m.x127 / (0.0001 + 0.9999 * m.b11) +
    5.59175556022082)**2 - 1) * (0.0001 + 0.9999 * m.b11) + 0.0117234102493874
    * m.b11 <= 0.0117234102493874)
m.e52 = Constraint(expr= ((-m.x128 / (0.0001 + 0.9999 * m.b12) +
    8.52118108549064)**2 + (-m.x129 / (0.0001 + 0.9999 * m.b12) +
    5.32332318998315)**2 - 1) * (0.0001 + 0.9999 * m.b12) + 0.00999482968767358
    * m.b12 <= 0.00999482968767358)
m.e53 = Constraint(expr= ((-m.x130 / (0.0001 + 0.9999 * m.b13) +
    4.01861330995576)**2 + (-m.x131 / (0.0001 + 0.9999 * m.b13) +
    9.65380890252737)**2 - 1) * (0.0001 + 0.9999 * m.b13) + 0.010834527926147 *
    m.b13 <= 0.010834527926147)
m.e54 = Constraint(expr= ((-m.x132 / (0.0001 + 0.9999 * m.b14) +
    2.49020328922613)**2 + (-m.x133 / (0.0001 + 0.9999 * m.b14) +
    0.874596139412213)**2 - 1) * (0.0001 + 0.9999 * m.b14) +
    0.000596603082874738 * m.b14 <= 0.000596603082874738)
m.e55 = Constraint(expr= ((-m.x134 / (0.0001 + 0.9999 * m.b15) +
    0.545671492825244)**2 + (-m.x135 / (0.0001 + 0.9999 * m.b15) +
    3.81401698819633)**2 - 1) * (0.0001 + 0.9999 * m.b15) + 0.00138444829643323
    * m.b15 <= 0.00138444829643323)
m.e56 = Constraint(expr= m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8
    + m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 == 1)
m.e57 = Constraint(expr= ((-m.x136 / (0.0001 + 0.9999 * m.b16) +
    8.68340342427357)**2 + (-m.x137 / (0.0001 + 0.9999 * m.b16) +
    8.57974596088368)**2 - 1) * (0.0001 + 0.9999 * m.b16) + 0.0148013535781986
    * m.b16 <= 0.0148013535781986)
m.e58 = Constraint(expr= ((-m.x138 / (0.0001 + 0.9999 * m.b17) +
    9.63614333912176)**2 + (-m.x139 / (0.0001 + 0.9999 * m.b17) +
    8.80176337918095)**2 - 1) * (0.0001 + 0.9999 * m.b17) + 0.0169326297035192
    * m.b17 <= 0.0169326297035192)
m.e59 = Constraint(expr= ((-m.x140 / (0.0001 + 0.9999 * m.b18) +
    3.68142205418198)**2 + (-m.x141 / (0.0001 + 0.9999 * m.b18) +
    1.1692321814062)**2 - 1) * (0.0001 + 0.9999 * m.b18) + 0.00139199722350534
    * m.b18 <= 0.00139199722350534)
m.e60 = Constraint(expr= ((-m.x142 / (0.0001 + 0.9999 * m.b19) +
    9.7121756733827)**2 + (-m.x143 / (0.0001 + 0.9999 * m.b19) +
    7.68772804421774)**2 - 1) * (0.0001 + 0.9999 * m.b19) + 0.0152427518792499
    * m.b19 <= 0.0152427518792499)
m.e61 = Constraint(expr= ((-m.x144 / (0.0001 + 0.9999 * m.b20) +
    3.2772228491781)**2 + (-m.x145 / (0.0001 + 0.9999 * m.b20) +
    8.20105404549271)**2 - 1) * (0.0001 + 0.9999 * m.b20) + 0.00769974770602674
    * m.b20 <= 0.00769974770602674)
m.e62 = Constraint(expr= ((-m.x146 / (0.0001 + 0.9999 * m.b21) +
    8.95169370625893)**2 + (-m.x147 / (0.0001 + 0.9999 * m.b21) +
    5.71833771240185)**2 - 1) * (0.0001 + 0.9999 * m.b21) + 0.0111832206403753
    * m.b21 <= 0.0111832206403753)
m.e63 = Constraint(expr= ((-m.x148 / (0.0001 + 0.9999 * m.b22) +
    6.39713701672676)**2 + (-m.x149 / (0.0001 + 0.9999 * m.b22) +
    2.19374777991393)**2 - 1) * (0.0001 + 0.9999 * m.b22) + 0.00447358913326531
    * m.b22 <= 0.00447358913326531)
m.e64 = Constraint(expr= ((-m.x150 / (0.0001 + 0.9999 * m.b23) +
    8.63324272987351)**2 + (-m.x151 / (0.0001 + 0.9999 * m.b23) +
    2.92174290170279)**2 - 1) * (0.0001 + 0.9999 * m.b23) + 0.00820694616165644
    * m.b23 <= 0.00820694616165644)
m.e65 = Constraint(expr= ((-m.x152 / (0.0001 + 0.9999 * m.b24) +
    3.63244627881363)**2 + (-m.x153 / (0.0001 + 0.9999 * m.b24) +
    1.91739848753332)**2 - 1) * (0.0001 + 0.9999 * m.b24) + 0.00158710829284621
    * m.b24 <= 0.00158710829284621)
m.e66 = Constraint(expr= ((-m.x154 / (0.0001 + 0.9999 * m.b25) +
    0.303084489788861)**2 + (-m.x155 / (0.0001 + 0.9999 * m.b25) +
    2.88588654972735)**2 - 1) * (0.0001 + 0.9999 * m.b25) + 0.00074202013858478
    * m.b25 <= 0.00074202013858478)
m.e67 = Constraint(expr= ((-m.x156 / (0.0001 + 0.9999 * m.b26) +
    9.32557624217471)**2 + (-m.x157 / (0.0001 + 0.9999 * m.b26) +
    5.59175556022082)**2 - 1) * (0.0001 + 0.9999 * m.b26) + 0.0117234102493874
    * m.b26 <= 0.0117234102493874)
m.e68 = Constraint(expr= ((-m.x158 / (0.0001 + 0.9999 * m.b27) +
    8.52118108549064)**2 + (-m.x159 / (0.0001 + 0.9999 * m.b27) +
    5.32332318998315)**2 - 1) * (0.0001 + 0.9999 * m.b27) + 0.00999482968767358
    * m.b27 <= 0.00999482968767358)
m.e69 = Constraint(expr= ((-m.x160 / (0.0001 + 0.9999 * m.b28) +
    4.01861330995576)**2 + (-m.x161 / (0.0001 + 0.9999 * m.b28) +
    9.65380890252737)**2 - 1) * (0.0001 + 0.9999 * m.b28) + 0.010834527926147 *
    m.b28 <= 0.010834527926147)
m.e70 = Constraint(expr= ((-m.x162 / (0.0001 + 0.9999 * m.b29) +
    2.49020328922613)**2 + (-m.x163 / (0.0001 + 0.9999 * m.b29) +
    0.874596139412213)**2 - 1) * (0.0001 + 0.9999 * m.b29) +
    0.000596603082874738 * m.b29 <= 0.000596603082874738)
m.e71 = Constraint(expr= ((-m.x164 / (0.0001 + 0.9999 * m.b30) +
    0.545671492825244)**2 + (-m.x165 / (0.0001 + 0.9999 * m.b30) +
    3.81401698819633)**2 - 1) * (0.0001 + 0.9999 * m.b30) + 0.00138444829643323
    * m.b30 <= 0.00138444829643323)
m.e72 = Constraint(expr= m.b16 + m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22
    + m.b23 + m.b24 + m.b25 + m.b26 + m.b27 + m.b28 + m.b29 + m.b30 == 1)
m.e73 = Constraint(expr= ((-m.x166 / (0.0001 + 0.9999 * m.b31) +
    8.68340342427357)**2 + (-m.x167 / (0.0001 + 0.9999 * m.b31) +
    8.57974596088368)**2 - 1) * (0.0001 + 0.9999 * m.b31) + 0.0148013535781986
    * m.b31 <= 0.0148013535781986)
m.e74 = Constraint(expr= ((-m.x168 / (0.0001 + 0.9999 * m.b32) +
    9.63614333912176)**2 + (-m.x169 / (0.0001 + 0.9999 * m.b32) +
    8.80176337918095)**2 - 1) * (0.0001 + 0.9999 * m.b32) + 0.0169326297035192
    * m.b32 <= 0.0169326297035192)
m.e75 = Constraint(expr= ((-m.x170 / (0.0001 + 0.9999 * m.b33) +
    3.68142205418198)**2 + (-m.x171 / (0.0001 + 0.9999 * m.b33) +
    1.1692321814062)**2 - 1) * (0.0001 + 0.9999 * m.b33) + 0.00139199722350534
    * m.b33 <= 0.00139199722350534)
m.e76 = Constraint(expr= ((-m.x172 / (0.0001 + 0.9999 * m.b34) +
    9.7121756733827)**2 + (-m.x173 / (0.0001 + 0.9999 * m.b34) +
    7.68772804421774)**2 - 1) * (0.0001 + 0.9999 * m.b34) + 0.0152427518792499
    * m.b34 <= 0.0152427518792499)
m.e77 = Constraint(expr= ((-m.x174 / (0.0001 + 0.9999 * m.b35) +
    3.2772228491781)**2 + (-m.x175 / (0.0001 + 0.9999 * m.b35) +
    8.20105404549271)**2 - 1) * (0.0001 + 0.9999 * m.b35) + 0.00769974770602674
    * m.b35 <= 0.00769974770602674)
m.e78 = Constraint(expr= ((-m.x176 / (0.0001 + 0.9999 * m.b36) +
    8.95169370625893)**2 + (-m.x177 / (0.0001 + 0.9999 * m.b36) +
    5.71833771240185)**2 - 1) * (0.0001 + 0.9999 * m.b36) + 0.0111832206403753
    * m.b36 <= 0.0111832206403753)
m.e79 = Constraint(expr= ((-m.x178 / (0.0001 + 0.9999 * m.b37) +
    6.39713701672676)**2 + (-m.x179 / (0.0001 + 0.9999 * m.b37) +
    2.19374777991393)**2 - 1) * (0.0001 + 0.9999 * m.b37) + 0.00447358913326531
    * m.b37 <= 0.00447358913326531)
m.e80 = Constraint(expr= ((-m.x180 / (0.0001 + 0.9999 * m.b38) +
    8.63324272987351)**2 + (-m.x181 / (0.0001 + 0.9999 * m.b38) +
    2.92174290170279)**2 - 1) * (0.0001 + 0.9999 * m.b38) + 0.00820694616165644
    * m.b38 <= 0.00820694616165644)
m.e81 = Constraint(expr= ((-m.x182 / (0.0001 + 0.9999 * m.b39) +
    3.63244627881363)**2 + (-m.x183 / (0.0001 + 0.9999 * m.b39) +
    1.91739848753332)**2 - 1) * (0.0001 + 0.9999 * m.b39) + 0.00158710829284621
    * m.b39 <= 0.00158710829284621)
m.e82 = Constraint(expr= ((-m.x184 / (0.0001 + 0.9999 * m.b40) +
    0.303084489788861)**2 + (-m.x185 / (0.0001 + 0.9999 * m.b40) +
    2.88588654972735)**2 - 1) * (0.0001 + 0.9999 * m.b40) + 0.00074202013858478
    * m.b40 <= 0.00074202013858478)
m.e83 = Constraint(expr= ((-m.x186 / (0.0001 + 0.9999 * m.b41) +
    9.32557624217471)**2 + (-m.x187 / (0.0001 + 0.9999 * m.b41) +
    5.59175556022082)**2 - 1) * (0.0001 + 0.9999 * m.b41) + 0.0117234102493874
    * m.b41 <= 0.0117234102493874)
m.e84 = Constraint(expr= ((-m.x188 / (0.0001 + 0.9999 * m.b42) +
    8.52118108549064)**2 + (-m.x189 / (0.0001 + 0.9999 * m.b42) +
    5.32332318998315)**2 - 1) * (0.0001 + 0.9999 * m.b42) + 0.00999482968767358
    * m.b42 <= 0.00999482968767358)
m.e85 = Constraint(expr= ((-m.x190 / (0.0001 + 0.9999 * m.b43) +
    4.01861330995576)**2 + (-m.x191 / (0.0001 + 0.9999 * m.b43) +
    9.65380890252737)**2 - 1) * (0.0001 + 0.9999 * m.b43) + 0.010834527926147 *
    m.b43 <= 0.010834527926147)
m.e86 = Constraint(expr= ((-m.x192 / (0.0001 + 0.9999 * m.b44) +
    2.49020328922613)**2 + (-m.x193 / (0.0001 + 0.9999 * m.b44) +
    0.874596139412213)**2 - 1) * (0.0001 + 0.9999 * m.b44) +
    0.000596603082874738 * m.b44 <= 0.000596603082874738)
m.e87 = Constraint(expr= ((-m.x194 / (0.0001 + 0.9999 * m.b45) +
    0.545671492825244)**2 + (-m.x195 / (0.0001 + 0.9999 * m.b45) +
    3.81401698819633)**2 - 1) * (0.0001 + 0.9999 * m.b45) + 0.00138444829643323
    * m.b45 <= 0.00138444829643323)
m.e88 = Constraint(expr= m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 + m.b37
    + m.b38 + m.b39 + m.b40 + m.b41 + m.b42 + m.b43 + m.b44 + m.b45 == 1)
m.e89 = Constraint(expr= ((-m.x196 / (0.0001 + 0.9999 * m.b46) +
    8.68340342427357)**2 + (-m.x197 / (0.0001 + 0.9999 * m.b46) +
    8.57974596088368)**2 - 1) * (0.0001 + 0.9999 * m.b46) + 0.0148013535781986
    * m.b46 <= 0.0148013535781986)
m.e90 = Constraint(expr= ((-m.x198 / (0.0001 + 0.9999 * m.b47) +
    9.63614333912176)**2 + (-m.x199 / (0.0001 + 0.9999 * m.b47) +
    8.80176337918095)**2 - 1) * (0.0001 + 0.9999 * m.b47) + 0.0169326297035192
    * m.b47 <= 0.0169326297035192)
m.e91 = Constraint(expr= ((-m.x200 / (0.0001 + 0.9999 * m.b48) +
    3.68142205418198)**2 + (-m.x201 / (0.0001 + 0.9999 * m.b48) +
    1.1692321814062)**2 - 1) * (0.0001 + 0.9999 * m.b48) + 0.00139199722350534
    * m.b48 <= 0.00139199722350534)
m.e92 = Constraint(expr= ((-m.x202 / (0.0001 + 0.9999 * m.b49) +
    9.7121756733827)**2 + (-m.x203 / (0.0001 + 0.9999 * m.b49) +
    7.68772804421774)**2 - 1) * (0.0001 + 0.9999 * m.b49) + 0.0152427518792499
    * m.b49 <= 0.0152427518792499)
m.e93 = Constraint(expr= ((-m.x204 / (0.0001 + 0.9999 * m.b50) +
    3.2772228491781)**2 + (-m.x205 / (0.0001 + 0.9999 * m.b50) +
    8.20105404549271)**2 - 1) * (0.0001 + 0.9999 * m.b50) + 0.00769974770602674
    * m.b50 <= 0.00769974770602674)
m.e94 = Constraint(expr= ((-m.x206 / (0.0001 + 0.9999 * m.b51) +
    8.95169370625893)**2 + (-m.x207 / (0.0001 + 0.9999 * m.b51) +
    5.71833771240185)**2 - 1) * (0.0001 + 0.9999 * m.b51) + 0.0111832206403753
    * m.b51 <= 0.0111832206403753)
m.e95 = Constraint(expr= ((-m.x208 / (0.0001 + 0.9999 * m.b52) +
    6.39713701672676)**2 + (-m.x209 / (0.0001 + 0.9999 * m.b52) +
    2.19374777991393)**2 - 1) * (0.0001 + 0.9999 * m.b52) + 0.00447358913326531
    * m.b52 <= 0.00447358913326531)
m.e96 = Constraint(expr= ((-m.x210 / (0.0001 + 0.9999 * m.b53) +
    8.63324272987351)**2 + (-m.x211 / (0.0001 + 0.9999 * m.b53) +
    2.92174290170279)**2 - 1) * (0.0001 + 0.9999 * m.b53) + 0.00820694616165644
    * m.b53 <= 0.00820694616165644)
m.e97 = Constraint(expr= ((-m.x212 / (0.0001 + 0.9999 * m.b54) +
    3.63244627881363)**2 + (-m.x213 / (0.0001 + 0.9999 * m.b54) +
    1.91739848753332)**2 - 1) * (0.0001 + 0.9999 * m.b54) + 0.00158710829284621
    * m.b54 <= 0.00158710829284621)
m.e98 = Constraint(expr= ((-m.x214 / (0.0001 + 0.9999 * m.b55) +
    0.303084489788861)**2 + (-m.x215 / (0.0001 + 0.9999 * m.b55) +
    2.88588654972735)**2 - 1) * (0.0001 + 0.9999 * m.b55) + 0.00074202013858478
    * m.b55 <= 0.00074202013858478)
m.e99 = Constraint(expr= ((-m.x216 / (0.0001 + 0.9999 * m.b56) +
    9.32557624217471)**2 + (-m.x217 / (0.0001 + 0.9999 * m.b56) +
    5.59175556022082)**2 - 1) * (0.0001 + 0.9999 * m.b56) + 0.0117234102493874
    * m.b56 <= 0.0117234102493874)
m.e100 = Constraint(expr= ((-m.x218 / (0.0001 + 0.9999 * m.b57) +
    8.52118108549064)**2 + (-m.x219 / (0.0001 + 0.9999 * m.b57) +
    5.32332318998315)**2 - 1) * (0.0001 + 0.9999 * m.b57) + 0.00999482968767358
    * m.b57 <= 0.00999482968767358)
m.e101 = Constraint(expr= ((-m.x220 / (0.0001 + 0.9999 * m.b58) +
    4.01861330995576)**2 + (-m.x221 / (0.0001 + 0.9999 * m.b58) +
    9.65380890252737)**2 - 1) * (0.0001 + 0.9999 * m.b58) + 0.010834527926147 *
    m.b58 <= 0.010834527926147)
m.e102 = Constraint(expr= ((-m.x222 / (0.0001 + 0.9999 * m.b59) +
    2.49020328922613)**2 + (-m.x223 / (0.0001 + 0.9999 * m.b59) +
    0.874596139412213)**2 - 1) * (0.0001 + 0.9999 * m.b59) +
    0.000596603082874738 * m.b59 <= 0.000596603082874738)
m.e103 = Constraint(expr= ((-m.x224 / (0.0001 + 0.9999 * m.b60) +
    0.545671492825244)**2 + (-m.x225 / (0.0001 + 0.9999 * m.b60) +
    3.81401698819633)**2 - 1) * (0.0001 + 0.9999 * m.b60) + 0.00138444829643323
    * m.b60 <= 0.00138444829643323)
m.e104 = Constraint(expr= m.b46 + m.b47 + m.b48 + m.b49 + m.b50 + m.b51 + m.b52
    + m.b53 + m.b54 + m.b55 + m.b56 + m.b57 + m.b58 + m.b59 + m.b60 == 1)
m.e105 = Constraint(expr= ((-m.x226 / (0.0001 + 0.9999 * m.b61) +
    8.68340342427357)**2 + (-m.x227 / (0.0001 + 0.9999 * m.b61) +
    8.57974596088368)**2 - 1) * (0.0001 + 0.9999 * m.b61) + 0.0148013535781986
    * m.b61 <= 0.0148013535781986)
m.e106 = Constraint(expr= ((-m.x228 / (0.0001 + 0.9999 * m.b62) +
    9.63614333912176)**2 + (-m.x229 / (0.0001 + 0.9999 * m.b62) +
    8.80176337918095)**2 - 1) * (0.0001 + 0.9999 * m.b62) + 0.0169326297035192
    * m.b62 <= 0.0169326297035192)
m.e107 = Constraint(expr= ((-m.x230 / (0.0001 + 0.9999 * m.b63) +
    3.68142205418198)**2 + (-m.x231 / (0.0001 + 0.9999 * m.b63) +
    1.1692321814062)**2 - 1) * (0.0001 + 0.9999 * m.b63) + 0.00139199722350534
    * m.b63 <= 0.00139199722350534)
m.e108 = Constraint(expr= ((-m.x232 / (0.0001 + 0.9999 * m.b64) +
    9.7121756733827)**2 + (-m.x233 / (0.0001 + 0.9999 * m.b64) +
    7.68772804421774)**2 - 1) * (0.0001 + 0.9999 * m.b64) + 0.0152427518792499
    * m.b64 <= 0.0152427518792499)
m.e109 = Constraint(expr= ((-m.x234 / (0.0001 + 0.9999 * m.b65) +
    3.2772228491781)**2 + (-m.x235 / (0.0001 + 0.9999 * m.b65) +
    8.20105404549271)**2 - 1) * (0.0001 + 0.9999 * m.b65) + 0.00769974770602674
    * m.b65 <= 0.00769974770602674)
m.e110 = Constraint(expr= ((-m.x236 / (0.0001 + 0.9999 * m.b66) +
    8.95169370625893)**2 + (-m.x237 / (0.0001 + 0.9999 * m.b66) +
    5.71833771240185)**2 - 1) * (0.0001 + 0.9999 * m.b66) + 0.0111832206403753
    * m.b66 <= 0.0111832206403753)
m.e111 = Constraint(expr= ((-m.x238 / (0.0001 + 0.9999 * m.b67) +
    6.39713701672676)**2 + (-m.x239 / (0.0001 + 0.9999 * m.b67) +
    2.19374777991393)**2 - 1) * (0.0001 + 0.9999 * m.b67) + 0.00447358913326531
    * m.b67 <= 0.00447358913326531)
m.e112 = Constraint(expr= ((-m.x240 / (0.0001 + 0.9999 * m.b68) +
    8.63324272987351)**2 + (-m.x241 / (0.0001 + 0.9999 * m.b68) +
    2.92174290170279)**2 - 1) * (0.0001 + 0.9999 * m.b68) + 0.00820694616165644
    * m.b68 <= 0.00820694616165644)
m.e113 = Constraint(expr= ((-m.x242 / (0.0001 + 0.9999 * m.b69) +
    3.63244627881363)**2 + (-m.x243 / (0.0001 + 0.9999 * m.b69) +
    1.91739848753332)**2 - 1) * (0.0001 + 0.9999 * m.b69) + 0.00158710829284621
    * m.b69 <= 0.00158710829284621)
m.e114 = Constraint(expr= ((-m.x244 / (0.0001 + 0.9999 * m.b70) +
    0.303084489788861)**2 + (-m.x245 / (0.0001 + 0.9999 * m.b70) +
    2.88588654972735)**2 - 1) * (0.0001 + 0.9999 * m.b70) + 0.00074202013858478
    * m.b70 <= 0.00074202013858478)
m.e115 = Constraint(expr= ((-m.x246 / (0.0001 + 0.9999 * m.b71) +
    9.32557624217471)**2 + (-m.x247 / (0.0001 + 0.9999 * m.b71) +
    5.59175556022082)**2 - 1) * (0.0001 + 0.9999 * m.b71) + 0.0117234102493874
    * m.b71 <= 0.0117234102493874)
m.e116 = Constraint(expr= ((-m.x248 / (0.0001 + 0.9999 * m.b72) +
    8.52118108549064)**2 + (-m.x249 / (0.0001 + 0.9999 * m.b72) +
    5.32332318998315)**2 - 1) * (0.0001 + 0.9999 * m.b72) + 0.00999482968767358
    * m.b72 <= 0.00999482968767358)
m.e117 = Constraint(expr= ((-m.x250 / (0.0001 + 0.9999 * m.b73) +
    4.01861330995576)**2 + (-m.x251 / (0.0001 + 0.9999 * m.b73) +
    9.65380890252737)**2 - 1) * (0.0001 + 0.9999 * m.b73) + 0.010834527926147 *
    m.b73 <= 0.010834527926147)
m.e118 = Constraint(expr= ((-m.x252 / (0.0001 + 0.9999 * m.b74) +
    2.49020328922613)**2 + (-m.x253 / (0.0001 + 0.9999 * m.b74) +
    0.874596139412213)**2 - 1) * (0.0001 + 0.9999 * m.b74) +
    0.000596603082874738 * m.b74 <= 0.000596603082874738)
m.e119 = Constraint(expr= ((-m.x254 / (0.0001 + 0.9999 * m.b75) +
    0.545671492825244)**2 + (-m.x255 / (0.0001 + 0.9999 * m.b75) +
    3.81401698819633)**2 - 1) * (0.0001 + 0.9999 * m.b75) + 0.00138444829643323
    * m.b75 <= 0.00138444829643323)
m.e120 = Constraint(expr= m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b66 + m.b67
    + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 + m.b73 + m.b74 + m.b75 == 1)
m.e121 = Constraint(expr= m.b1 + m.b16 + m.b31 + m.b46 + m.b61 <= 1)
m.e122 = Constraint(expr= m.b2 + m.b17 + m.b32 + m.b47 + m.b62 <= 1)
m.e123 = Constraint(expr= m.b3 + m.b18 + m.b33 + m.b48 + m.b63 <= 1)
m.e124 = Constraint(expr= m.b4 + m.b19 + m.b34 + m.b49 + m.b64 <= 1)
m.e125 = Constraint(expr= m.b5 + m.b20 + m.b35 + m.b50 + m.b65 <= 1)
m.e126 = Constraint(expr= m.b6 + m.b21 + m.b36 + m.b51 + m.b66 <= 1)
m.e127 = Constraint(expr= m.b7 + m.b22 + m.b37 + m.b52 + m.b67 <= 1)
m.e128 = Constraint(expr= m.b8 + m.b23 + m.b38 + m.b53 + m.b68 <= 1)
m.e129 = Constraint(expr= m.b9 + m.b24 + m.b39 + m.b54 + m.b69 <= 1)
m.e130 = Constraint(expr= m.b10 + m.b25 + m.b40 + m.b55 + m.b70 <= 1)
m.e131 = Constraint(expr= m.b11 + m.b26 + m.b41 + m.b56 + m.b71 <= 1)
m.e132 = Constraint(expr= m.b12 + m.b27 + m.b42 + m.b57 + m.b72 <= 1)
m.e133 = Constraint(expr= m.b13 + m.b28 + m.b43 + m.b58 + m.b73 <= 1)
m.e134 = Constraint(expr= m.b14 + m.b29 + m.b44 + m.b59 + m.b74 <= 1)
m.e135 = Constraint(expr= m.b15 + m.b30 + m.b45 + m.b60 + m.b75 <= 1)
m.e136 = Constraint(expr= -m.x76 + m.x106 + m.x108 + m.x110 + m.x112 + m.x114
    + m.x116 + m.x118 + m.x120 + m.x122 + m.x124 + m.x126 + m.x128 + m.x130 +
    m.x132 + m.x134 == 0)
m.e137 = Constraint(expr= -m.x79 + m.x107 + m.x109 + m.x111 + m.x113 + m.x115
    + m.x117 + m.x119 + m.x121 + m.x123 + m.x125 + m.x127 + m.x129 + m.x131 +
    m.x133 + m.x135 == 0)
m.e138 = Constraint(expr= -m.x77 + m.x136 + m.x138 + m.x140 + m.x142 + m.x144
    + m.x146 + m.x148 + m.x150 + m.x152 + m.x154 + m.x156 + m.x158 + m.x160 +
    m.x162 + m.x164 == 0)
m.e139 = Constraint(expr= -m.x80 + m.x137 + m.x139 + m.x141 + m.x143 + m.x145
    + m.x147 + m.x149 + m.x151 + m.x153 + m.x155 + m.x157 + m.x159 + m.x161 +
    m.x163 + m.x165 == 0)
m.e140 = Constraint(expr= -m.x82 + m.x166 + m.x168 + m.x170 + m.x172 + m.x174
    + m.x176 + m.x178 + m.x180 + m.x182 + m.x184 + m.x186 + m.x188 + m.x190 +
    m.x192 + m.x194 == 0)
m.e141 = Constraint(expr= -m.x84 + m.x167 + m.x169 + m.x171 + m.x173 + m.x175
    + m.x177 + m.x179 + m.x181 + m.x183 + m.x185 + m.x187 + m.x189 + m.x191 +
    m.x193 + m.x195 == 0)
m.e142 = Constraint(expr= -m.x86 + m.x196 + m.x198 + m.x200 + m.x202 + m.x204
    + m.x206 + m.x208 + m.x210 + m.x212 + m.x214 + m.x216 + m.x218 + m.x220 +
    m.x222 + m.x224 == 0)
m.e143 = Constraint(expr= -m.x88 + m.x197 + m.x199 + m.x201 + m.x203 + m.x205
    + m.x207 + m.x209 + m.x211 + m.x213 + m.x215 + m.x217 + m.x219 + m.x221 +
    m.x223 + m.x225 == 0)
m.e144 = Constraint(expr= -m.x90 + m.x226 + m.x228 + m.x230 + m.x232 + m.x234
    + m.x236 + m.x238 + m.x240 + m.x242 + m.x244 + m.x246 + m.x248 + m.x250 +
    m.x252 + m.x254 == 0)
m.e145 = Constraint(expr= -m.x92 + m.x227 + m.x229 + m.x231 + m.x233 + m.x235
    + m.x237 + m.x239 + m.x241 + m.x243 + m.x245 + m.x247 + m.x249 + m.x251 +
    m.x253 + m.x255 == 0)
m.e146 = Constraint(expr= -10 * m.b1 + m.x106 <= 0)
m.e147 = Constraint(expr= -10 * m.b2 + m.x108 <= 0)
m.e148 = Constraint(expr= -10 * m.b3 + m.x110 <= 0)
m.e149 = Constraint(expr= -10 * m.b4 + m.x112 <= 0)
m.e150 = Constraint(expr= -10 * m.b5 + m.x114 <= 0)
m.e151 = Constraint(expr= -10 * m.b6 + m.x116 <= 0)
m.e152 = Constraint(expr= -10 * m.b7 + m.x118 <= 0)
m.e153 = Constraint(expr= -10 * m.b8 + m.x120 <= 0)
m.e154 = Constraint(expr= -10 * m.b9 + m.x122 <= 0)
m.e155 = Constraint(expr= -10 * m.b10 + m.x124 <= 0)
m.e156 = Constraint(expr= -10 * m.b11 + m.x126 <= 0)
m.e157 = Constraint(expr= -10 * m.b12 + m.x128 <= 0)
m.e158 = Constraint(expr= -10 * m.b13 + m.x130 <= 0)
m.e159 = Constraint(expr= -10 * m.b14 + m.x132 <= 0)
m.e160 = Constraint(expr= -10 * m.b15 + m.x134 <= 0)
m.e161 = Constraint(expr= -10 * m.b1 + m.x107 <= 0)
m.e162 = Constraint(expr= -10 * m.b2 + m.x109 <= 0)
m.e163 = Constraint(expr= -10 * m.b3 + m.x111 <= 0)
m.e164 = Constraint(expr= -10 * m.b4 + m.x113 <= 0)
m.e165 = Constraint(expr= -10 * m.b5 + m.x115 <= 0)
m.e166 = Constraint(expr= -10 * m.b6 + m.x117 <= 0)
m.e167 = Constraint(expr= -10 * m.b7 + m.x119 <= 0)
m.e168 = Constraint(expr= -10 * m.b8 + m.x121 <= 0)
m.e169 = Constraint(expr= -10 * m.b9 + m.x123 <= 0)
m.e170 = Constraint(expr= -10 * m.b10 + m.x125 <= 0)
m.e171 = Constraint(expr= -10 * m.b11 + m.x127 <= 0)
m.e172 = Constraint(expr= -10 * m.b12 + m.x129 <= 0)
m.e173 = Constraint(expr= -10 * m.b13 + m.x131 <= 0)
m.e174 = Constraint(expr= -10 * m.b14 + m.x133 <= 0)
m.e175 = Constraint(expr= -10 * m.b15 + m.x135 <= 0)
m.e176 = Constraint(expr= -10 * m.b16 + m.x136 <= 0)
m.e177 = Constraint(expr= -10 * m.b17 + m.x138 <= 0)
m.e178 = Constraint(expr= -10 * m.b18 + m.x140 <= 0)
m.e179 = Constraint(expr= -10 * m.b19 + m.x142 <= 0)
m.e180 = Constraint(expr= -10 * m.b20 + m.x144 <= 0)
m.e181 = Constraint(expr= -10 * m.b21 + m.x146 <= 0)
m.e182 = Constraint(expr= -10 * m.b22 + m.x148 <= 0)
m.e183 = Constraint(expr= -10 * m.b23 + m.x150 <= 0)
m.e184 = Constraint(expr= -10 * m.b24 + m.x152 <= 0)
m.e185 = Constraint(expr= -10 * m.b25 + m.x154 <= 0)
m.e186 = Constraint(expr= -10 * m.b26 + m.x156 <= 0)
m.e187 = Constraint(expr= -10 * m.b27 + m.x158 <= 0)
m.e188 = Constraint(expr= -10 * m.b28 + m.x160 <= 0)
m.e189 = Constraint(expr= -10 * m.b29 + m.x162 <= 0)
m.e190 = Constraint(expr= -10 * m.b30 + m.x164 <= 0)
m.e191 = Constraint(expr= -10 * m.b16 + m.x137 <= 0)
m.e192 = Constraint(expr= -10 * m.b17 + m.x139 <= 0)
m.e193 = Constraint(expr= -10 * m.b18 + m.x141 <= 0)
m.e194 = Constraint(expr= -10 * m.b19 + m.x143 <= 0)
m.e195 = Constraint(expr= -10 * m.b20 + m.x145 <= 0)
m.e196 = Constraint(expr= -10 * m.b21 + m.x147 <= 0)
m.e197 = Constraint(expr= -10 * m.b22 + m.x149 <= 0)
m.e198 = Constraint(expr= -10 * m.b23 + m.x151 <= 0)
m.e199 = Constraint(expr= -10 * m.b24 + m.x153 <= 0)
m.e200 = Constraint(expr= -10 * m.b25 + m.x155 <= 0)
m.e201 = Constraint(expr= -10 * m.b26 + m.x157 <= 0)
m.e202 = Constraint(expr= -10 * m.b27 + m.x159 <= 0)
m.e203 = Constraint(expr= -10 * m.b28 + m.x161 <= 0)
m.e204 = Constraint(expr= -10 * m.b29 + m.x163 <= 0)
m.e205 = Constraint(expr= -10 * m.b30 + m.x165 <= 0)
m.e206 = Constraint(expr= -10 * m.b31 + m.x166 <= 0)
m.e207 = Constraint(expr= -10 * m.b32 + m.x168 <= 0)
m.e208 = Constraint(expr= -10 * m.b33 + m.x170 <= 0)
m.e209 = Constraint(expr= -10 * m.b34 + m.x172 <= 0)
m.e210 = Constraint(expr= -10 * m.b35 + m.x174 <= 0)
m.e211 = Constraint(expr= -10 * m.b36 + m.x176 <= 0)
m.e212 = Constraint(expr= -10 * m.b37 + m.x178 <= 0)
m.e213 = Constraint(expr= -10 * m.b38 + m.x180 <= 0)
m.e214 = Constraint(expr= -10 * m.b39 + m.x182 <= 0)
m.e215 = Constraint(expr= -10 * m.b40 + m.x184 <= 0)
m.e216 = Constraint(expr= -10 * m.b41 + m.x186 <= 0)
m.e217 = Constraint(expr= -10 * m.b42 + m.x188 <= 0)
m.e218 = Constraint(expr= -10 * m.b43 + m.x190 <= 0)
m.e219 = Constraint(expr= -10 * m.b44 + m.x192 <= 0)
m.e220 = Constraint(expr= -10 * m.b45 + m.x194 <= 0)
m.e221 = Constraint(expr= -10 * m.b31 + m.x167 <= 0)
m.e222 = Constraint(expr= -10 * m.b32 + m.x169 <= 0)
m.e223 = Constraint(expr= -10 * m.b33 + m.x171 <= 0)
m.e224 = Constraint(expr= -10 * m.b34 + m.x173 <= 0)
m.e225 = Constraint(expr= -10 * m.b35 + m.x175 <= 0)
m.e226 = Constraint(expr= -10 * m.b36 + m.x177 <= 0)
m.e227 = Constraint(expr= -10 * m.b37 + m.x179 <= 0)
m.e228 = Constraint(expr= -10 * m.b38 + m.x181 <= 0)
m.e229 = Constraint(expr= -10 * m.b39 + m.x183 <= 0)
m.e230 = Constraint(expr= -10 * m.b40 + m.x185 <= 0)
m.e231 = Constraint(expr= -10 * m.b41 + m.x187 <= 0)
m.e232 = Constraint(expr= -10 * m.b42 + m.x189 <= 0)
m.e233 = Constraint(expr= -10 * m.b43 + m.x191 <= 0)
m.e234 = Constraint(expr= -10 * m.b44 + m.x193 <= 0)
m.e235 = Constraint(expr= -10 * m.b45 + m.x195 <= 0)
m.e236 = Constraint(expr= -10 * m.b46 + m.x196 <= 0)
m.e237 = Constraint(expr= -10 * m.b47 + m.x198 <= 0)
m.e238 = Constraint(expr= -10 * m.b48 + m.x200 <= 0)
m.e239 = Constraint(expr= -10 * m.b49 + m.x202 <= 0)
m.e240 = Constraint(expr= -10 * m.b50 + m.x204 <= 0)
m.e241 = Constraint(expr= -10 * m.b51 + m.x206 <= 0)
m.e242 = Constraint(expr= -10 * m.b52 + m.x208 <= 0)
m.e243 = Constraint(expr= -10 * m.b53 + m.x210 <= 0)
m.e244 = Constraint(expr= -10 * m.b54 + m.x212 <= 0)
m.e245 = Constraint(expr= -10 * m.b55 + m.x214 <= 0)
m.e246 = Constraint(expr= -10 * m.b56 + m.x216 <= 0)
m.e247 = Constraint(expr= -10 * m.b57 + m.x218 <= 0)
m.e248 = Constraint(expr= -10 * m.b58 + m.x220 <= 0)
m.e249 = Constraint(expr= -10 * m.b59 + m.x222 <= 0)
m.e250 = Constraint(expr= -10 * m.b60 + m.x224 <= 0)
m.e251 = Constraint(expr= -10 * m.b46 + m.x197 <= 0)
m.e252 = Constraint(expr= -10 * m.b47 + m.x199 <= 0)
m.e253 = Constraint(expr= -10 * m.b48 + m.x201 <= 0)
m.e254 = Constraint(expr= -10 * m.b49 + m.x203 <= 0)
m.e255 = Constraint(expr= -10 * m.b50 + m.x205 <= 0)
m.e256 = Constraint(expr= -10 * m.b51 + m.x207 <= 0)
m.e257 = Constraint(expr= -10 * m.b52 + m.x209 <= 0)
m.e258 = Constraint(expr= -10 * m.b53 + m.x211 <= 0)
m.e259 = Constraint(expr= -10 * m.b54 + m.x213 <= 0)
m.e260 = Constraint(expr= -10 * m.b55 + m.x215 <= 0)
m.e261 = Constraint(expr= -10 * m.b56 + m.x217 <= 0)
m.e262 = Constraint(expr= -10 * m.b57 + m.x219 <= 0)
m.e263 = Constraint(expr= -10 * m.b58 + m.x221 <= 0)
m.e264 = Constraint(expr= -10 * m.b59 + m.x223 <= 0)
m.e265 = Constraint(expr= -10 * m.b60 + m.x225 <= 0)
m.e266 = Constraint(expr= -10 * m.b61 + m.x226 <= 0)
m.e267 = Constraint(expr= -10 * m.b62 + m.x228 <= 0)
m.e268 = Constraint(expr= -10 * m.b63 + m.x230 <= 0)
m.e269 = Constraint(expr= -10 * m.b64 + m.x232 <= 0)
m.e270 = Constraint(expr= -10 * m.b65 + m.x234 <= 0)
m.e271 = Constraint(expr= -10 * m.b66 + m.x236 <= 0)
m.e272 = Constraint(expr= -10 * m.b67 + m.x238 <= 0)
m.e273 = Constraint(expr= -10 * m.b68 + m.x240 <= 0)
m.e274 = Constraint(expr= -10 * m.b69 + m.x242 <= 0)
m.e275 = Constraint(expr= -10 * m.b70 + m.x244 <= 0)
m.e276 = Constraint(expr= -10 * m.b71 + m.x246 <= 0)
m.e277 = Constraint(expr= -10 * m.b72 + m.x248 <= 0)
m.e278 = Constraint(expr= -10 * m.b73 + m.x250 <= 0)
m.e279 = Constraint(expr= -10 * m.b74 + m.x252 <= 0)
m.e280 = Constraint(expr= -10 * m.b75 + m.x254 <= 0)
m.e281 = Constraint(expr= -10 * m.b61 + m.x227 <= 0)
m.e282 = Constraint(expr= -10 * m.b62 + m.x229 <= 0)
m.e283 = Constraint(expr= -10 * m.b63 + m.x231 <= 0)
m.e284 = Constraint(expr= -10 * m.b64 + m.x233 <= 0)
m.e285 = Constraint(expr= -10 * m.b65 + m.x235 <= 0)
m.e286 = Constraint(expr= -10 * m.b66 + m.x237 <= 0)
m.e287 = Constraint(expr= -10 * m.b67 + m.x239 <= 0)
m.e288 = Constraint(expr= -10 * m.b68 + m.x241 <= 0)
m.e289 = Constraint(expr= -10 * m.b69 + m.x243 <= 0)
m.e290 = Constraint(expr= -10 * m.b70 + m.x245 <= 0)
m.e291 = Constraint(expr= -10 * m.b71 + m.x247 <= 0)
m.e292 = Constraint(expr= -10 * m.b72 + m.x249 <= 0)
m.e293 = Constraint(expr= -10 * m.b73 + m.x251 <= 0)
m.e294 = Constraint(expr= -10 * m.b74 + m.x253 <= 0)
m.e295 = Constraint(expr= -10 * m.b75 + m.x255 <= 0)
m.e296 = Constraint(expr= m.x76 - m.x77 <= 0)
m.e297 = Constraint(expr= m.x77 - m.x82 <= 0)
m.e298 = Constraint(expr= m.x82 - m.x86 <= 0)
m.e299 = Constraint(expr= m.x86 - m.x90 <= 0)
