# MINLP written by GAMS Convert at 05/07/21 17:12:59
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       294       20        0      274        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       245      195       50        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       953      753      200
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

m.obj = Objective(sense=minimize, expr= m.x53 + m.x56 + m.x59 + m.x61 + m.x63
    + m.x65 + m.x67 + m.x69 + m.x71 + m.x73 + m.x75 + m.x77 + m.x78 + m.x79 +
    m.x80 + m.x81 + m.x82 + m.x83 + m.x84 + m.x85 + m.x86 + m.x87 + m.x88 +
    m.x89 + m.x90 + m.x91 + m.x92 + m.x93 + m.x94 + m.x95)

m.e1 = Constraint(expr= m.x51 - m.x52 - m.x53 <= 0)
m.e2 = Constraint(expr= -m.x51 + m.x52 - m.x53 <= 0)
m.e3 = Constraint(expr= m.x54 - m.x55 - m.x56 <= 0)
m.e4 = Constraint(expr= -m.x54 + m.x55 - m.x56 <= 0)
m.e5 = Constraint(expr= m.x57 - m.x58 - m.x59 <= 0)
m.e6 = Constraint(expr= -m.x57 + m.x58 - m.x59 <= 0)
m.e7 = Constraint(expr= m.x51 - m.x60 - m.x61 <= 0)
m.e8 = Constraint(expr= -m.x51 + m.x60 - m.x61 <= 0)
m.e9 = Constraint(expr= m.x54 - m.x62 - m.x63 <= 0)
m.e10 = Constraint(expr= -m.x54 + m.x62 - m.x63 <= 0)
m.e11 = Constraint(expr= m.x57 - m.x64 - m.x65 <= 0)
m.e12 = Constraint(expr= -m.x57 + m.x64 - m.x65 <= 0)
m.e13 = Constraint(expr= m.x51 - m.x66 - m.x67 <= 0)
m.e14 = Constraint(expr= -m.x51 + m.x66 - m.x67 <= 0)
m.e15 = Constraint(expr= m.x54 - m.x68 - m.x69 <= 0)
m.e16 = Constraint(expr= -m.x54 + m.x68 - m.x69 <= 0)
m.e17 = Constraint(expr= m.x57 - m.x70 - m.x71 <= 0)
m.e18 = Constraint(expr= -m.x57 + m.x70 - m.x71 <= 0)
m.e19 = Constraint(expr= m.x51 - m.x72 - m.x73 <= 0)
m.e20 = Constraint(expr= -m.x51 + m.x72 - m.x73 <= 0)
m.e21 = Constraint(expr= m.x54 - m.x74 - m.x75 <= 0)
m.e22 = Constraint(expr= -m.x54 + m.x74 - m.x75 <= 0)
m.e23 = Constraint(expr= m.x57 - m.x76 - m.x77 <= 0)
m.e24 = Constraint(expr= -m.x57 + m.x76 - m.x77 <= 0)
m.e25 = Constraint(expr= m.x52 - m.x60 - m.x78 <= 0)
m.e26 = Constraint(expr= -m.x52 + m.x60 - m.x78 <= 0)
m.e27 = Constraint(expr= m.x55 - m.x62 - m.x79 <= 0)
m.e28 = Constraint(expr= -m.x55 + m.x62 - m.x79 <= 0)
m.e29 = Constraint(expr= m.x58 - m.x64 - m.x80 <= 0)
m.e30 = Constraint(expr= -m.x58 + m.x64 - m.x80 <= 0)
m.e31 = Constraint(expr= m.x52 - m.x66 - m.x81 <= 0)
m.e32 = Constraint(expr= -m.x52 + m.x66 - m.x81 <= 0)
m.e33 = Constraint(expr= m.x55 - m.x68 - m.x82 <= 0)
m.e34 = Constraint(expr= -m.x55 + m.x68 - m.x82 <= 0)
m.e35 = Constraint(expr= m.x58 - m.x70 - m.x83 <= 0)
m.e36 = Constraint(expr= -m.x58 + m.x70 - m.x83 <= 0)
m.e37 = Constraint(expr= m.x52 - m.x72 - m.x84 <= 0)
m.e38 = Constraint(expr= -m.x52 + m.x72 - m.x84 <= 0)
m.e39 = Constraint(expr= m.x55 - m.x74 - m.x85 <= 0)
m.e40 = Constraint(expr= -m.x55 + m.x74 - m.x85 <= 0)
m.e41 = Constraint(expr= m.x58 - m.x76 - m.x86 <= 0)
m.e42 = Constraint(expr= -m.x58 + m.x76 - m.x86 <= 0)
m.e43 = Constraint(expr= m.x60 - m.x66 - m.x87 <= 0)
m.e44 = Constraint(expr= -m.x60 + m.x66 - m.x87 <= 0)
m.e45 = Constraint(expr= m.x62 - m.x68 - m.x88 <= 0)
m.e46 = Constraint(expr= -m.x62 + m.x68 - m.x88 <= 0)
m.e47 = Constraint(expr= m.x64 - m.x70 - m.x89 <= 0)
m.e48 = Constraint(expr= -m.x64 + m.x70 - m.x89 <= 0)
m.e49 = Constraint(expr= m.x60 - m.x72 - m.x90 <= 0)
m.e50 = Constraint(expr= -m.x60 + m.x72 - m.x90 <= 0)
m.e51 = Constraint(expr= m.x62 - m.x74 - m.x91 <= 0)
m.e52 = Constraint(expr= -m.x62 + m.x74 - m.x91 <= 0)
m.e53 = Constraint(expr= m.x64 - m.x76 - m.x92 <= 0)
m.e54 = Constraint(expr= -m.x64 + m.x76 - m.x92 <= 0)
m.e55 = Constraint(expr= m.x66 - m.x72 - m.x93 <= 0)
m.e56 = Constraint(expr= -m.x66 + m.x72 - m.x93 <= 0)
m.e57 = Constraint(expr= m.x68 - m.x74 - m.x94 <= 0)
m.e58 = Constraint(expr= -m.x68 + m.x74 - m.x94 <= 0)
m.e59 = Constraint(expr= m.x70 - m.x76 - m.x95 <= 0)
m.e60 = Constraint(expr= -m.x70 + m.x76 - m.x95 <= 0)
m.e61 = Constraint(expr= ((-m.x96 / (0.0001 + 0.9999 * m.b1) + 3.55441530772447)
    **2 + (-m.x97 / (0.0001 + 0.9999 * m.b1) + 2.6588399811956)**2 + (-m.x98 /
    (0.0001 + 0.9999 * m.b1) + 5.16713392802669)**2 - 1) * (0.0001 + 0.9999 *
    m.b1) + 0.00454025712555548 * m.b1 <= 0.00454025712555548)
m.e62 = Constraint(expr= ((-m.x99 / (0.0001 + 0.9999 * m.b2) + 8.82094045941646)
    **2 + (-m.x100 / (0.0001 + 0.9999 * m.b2) + 9.51816335093057)**2 + (-m.x101
    / (0.0001 + 0.9999 * m.b2) + 0.894770759747333)**2 - 1) * (0.0001 + 0.9999
    * m.b2) + 0.0168205038876067 * m.b2 <= 0.0168205038876067)
m.e63 = Constraint(expr= ((-m.x102 / (0.0001 + 0.9999 * m.b3) +
    6.86229591973038)**2 + (-m.x103 / (0.0001 + 0.9999 * m.b3) +
    4.74665709736901)**2 + (-m.x104 / (0.0001 + 0.9999 * m.b3) +
    1.14651582775383)**2 - 1) * (0.0001 + 0.9999 * m.b3) + 0.0069936357433242 *
    m.b3 <= 0.0069936357433242)
m.e64 = Constraint(expr= ((-m.x105 / (0.0001 + 0.9999 * m.b4) +
    7.13880287505566)**2 + (-m.x106 / (0.0001 + 0.9999 * m.b4) +
    0.923639199248324)**2 + (-m.x107 / (0.0001 + 0.9999 * m.b4) +
    5.06906794010293)**2 - 1) * (0.0001 + 0.9999 * m.b4) + 0.00765110656406704
    * m.b4 <= 0.00765110656406704)
m.e65 = Constraint(expr= ((-m.x108 / (0.0001 + 0.9999 * m.b5) +
    9.54873475130122)**2 + (-m.x109 / (0.0001 + 0.9999 * m.b5) + 9.730708594994)
    **2 + (-m.x110 / (0.0001 + 0.9999 * m.b5) + 0.506682101270036)**2 - 1) * (
    0.0001 + 0.9999 * m.b5) + 0.0185121751863145 * m.b5 <= 0.0185121751863145)
m.e66 = Constraint(expr= ((-m.x111 / (0.0001 + 0.9999 * m.b6) +
    2.60295575976191)**2 + (-m.x112 / (0.0001 + 0.9999 * m.b6) +
    9.60525309364094)**2 + (-m.x113 / (0.0001 + 0.9999 * m.b6) +
    5.33059723504087)**2 - 1) * (0.0001 + 0.9999 * m.b6) + 0.0126451532562402 *
    m.b6 <= 0.0126451532562402)
m.e67 = Constraint(expr= ((-m.x114 / (0.0001 + 0.9999 * m.b7) + 8.7489239697277)
    **2 + (-m.x115 / (0.0001 + 0.9999 * m.b7) + 6.42418905563567)**2 + (-m.x116
    / (0.0001 + 0.9999 * m.b7) + 6.53764526999883)**2 - 1) * (0.0001 + 0.9999
    * m.b7) + 0.0159554681326963 * m.b7 <= 0.0159554681326963)
m.e68 = Constraint(expr= ((-m.x117 / (0.0001 + 0.9999 * m.b8) +
    2.98069751112782)**2 + (-m.x118 / (0.0001 + 0.9999 * m.b8) +
    1.4913715136506)**2 + (-m.x119 / (0.0001 + 0.9999 * m.b8) +
    2.04987567063475)**2 - 1) * (0.0001 + 0.9999 * m.b8) + 0.00143107369096323
    * m.b8 <= 0.00143107369096323)
m.e69 = Constraint(expr= ((-m.x120 / (0.0001 + 0.9999 * m.b9) +
    1.65791995565741)**2 + (-m.x121 / (0.0001 + 0.9999 * m.b9) +
    6.17322651944292)**2 + (-m.x122 / (0.0001 + 0.9999 * m.b9) +
    7.01412219987569)**2 - 1) * (0.0001 + 0.9999 * m.b9) + 0.00890553344745093
    * m.b9 <= 0.00890553344745093)
m.e70 = Constraint(expr= ((-m.x123 / (0.0001 + 0.9999 * m.b10) +
    2.41953526971379)**2 + (-m.x124 / (0.0001 + 0.9999 * m.b10) +
    1.09500973629707)**2 + (-m.x125 / (0.0001 + 0.9999 * m.b10) +
    2.60189595048839)**2 - 1) * (0.0001 + 0.9999 * m.b10) + 0.00128230597811422
    * m.b10 <= 0.00128230597811422)
m.e71 = Constraint(expr= m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8
    + m.b9 + m.b10 == 1)
m.e72 = Constraint(expr= ((-m.x126 / (0.0001 + 0.9999 * m.b11) +
    3.55441530772447)**2 + (-m.x127 / (0.0001 + 0.9999 * m.b11) +
    2.6588399811956)**2 + (-m.x128 / (0.0001 + 0.9999 * m.b11) +
    5.16713392802669)**2 - 1) * (0.0001 + 0.9999 * m.b11) + 0.00454025712555548
    * m.b11 <= 0.00454025712555548)
m.e73 = Constraint(expr= ((-m.x129 / (0.0001 + 0.9999 * m.b12) +
    8.82094045941646)**2 + (-m.x130 / (0.0001 + 0.9999 * m.b12) +
    9.51816335093057)**2 + (-m.x131 / (0.0001 + 0.9999 * m.b12) +
    0.894770759747333)**2 - 1) * (0.0001 + 0.9999 * m.b12) + 0.0168205038876067
    * m.b12 <= 0.0168205038876067)
m.e74 = Constraint(expr= ((-m.x132 / (0.0001 + 0.9999 * m.b13) +
    6.86229591973038)**2 + (-m.x133 / (0.0001 + 0.9999 * m.b13) +
    4.74665709736901)**2 + (-m.x134 / (0.0001 + 0.9999 * m.b13) +
    1.14651582775383)**2 - 1) * (0.0001 + 0.9999 * m.b13) + 0.0069936357433242
    * m.b13 <= 0.0069936357433242)
m.e75 = Constraint(expr= ((-m.x135 / (0.0001 + 0.9999 * m.b14) +
    7.13880287505566)**2 + (-m.x136 / (0.0001 + 0.9999 * m.b14) +
    0.923639199248324)**2 + (-m.x137 / (0.0001 + 0.9999 * m.b14) +
    5.06906794010293)**2 - 1) * (0.0001 + 0.9999 * m.b14) + 0.00765110656406704
    * m.b14 <= 0.00765110656406704)
m.e76 = Constraint(expr= ((-m.x138 / (0.0001 + 0.9999 * m.b15) +
    9.54873475130122)**2 + (-m.x139 / (0.0001 + 0.9999 * m.b15) +
    9.730708594994)**2 + (-m.x140 / (0.0001 + 0.9999 * m.b15) +
    0.506682101270036)**2 - 1) * (0.0001 + 0.9999 * m.b15) + 0.0185121751863145
    * m.b15 <= 0.0185121751863145)
m.e77 = Constraint(expr= ((-m.x141 / (0.0001 + 0.9999 * m.b16) +
    2.60295575976191)**2 + (-m.x142 / (0.0001 + 0.9999 * m.b16) +
    9.60525309364094)**2 + (-m.x143 / (0.0001 + 0.9999 * m.b16) +
    5.33059723504087)**2 - 1) * (0.0001 + 0.9999 * m.b16) + 0.0126451532562402
    * m.b16 <= 0.0126451532562402)
m.e78 = Constraint(expr= ((-m.x144 / (0.0001 + 0.9999 * m.b17) +
    8.7489239697277)**2 + (-m.x145 / (0.0001 + 0.9999 * m.b17) +
    6.42418905563567)**2 + (-m.x146 / (0.0001 + 0.9999 * m.b17) +
    6.53764526999883)**2 - 1) * (0.0001 + 0.9999 * m.b17) + 0.0159554681326963
    * m.b17 <= 0.0159554681326963)
m.e79 = Constraint(expr= ((-m.x147 / (0.0001 + 0.9999 * m.b18) +
    2.98069751112782)**2 + (-m.x148 / (0.0001 + 0.9999 * m.b18) +
    1.4913715136506)**2 + (-m.x149 / (0.0001 + 0.9999 * m.b18) +
    2.04987567063475)**2 - 1) * (0.0001 + 0.9999 * m.b18) + 0.00143107369096323
    * m.b18 <= 0.00143107369096323)
m.e80 = Constraint(expr= ((-m.x150 / (0.0001 + 0.9999 * m.b19) +
    1.65791995565741)**2 + (-m.x151 / (0.0001 + 0.9999 * m.b19) +
    6.17322651944292)**2 + (-m.x152 / (0.0001 + 0.9999 * m.b19) +
    7.01412219987569)**2 - 1) * (0.0001 + 0.9999 * m.b19) + 0.00890553344745093
    * m.b19 <= 0.00890553344745093)
m.e81 = Constraint(expr= ((-m.x153 / (0.0001 + 0.9999 * m.b20) +
    2.41953526971379)**2 + (-m.x154 / (0.0001 + 0.9999 * m.b20) +
    1.09500973629707)**2 + (-m.x155 / (0.0001 + 0.9999 * m.b20) +
    2.60189595048839)**2 - 1) * (0.0001 + 0.9999 * m.b20) + 0.00128230597811422
    * m.b20 <= 0.00128230597811422)
m.e82 = Constraint(expr= m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17
    + m.b18 + m.b19 + m.b20 == 1)
m.e83 = Constraint(expr= ((-m.x156 / (0.0001 + 0.9999 * m.b21) +
    3.55441530772447)**2 + (-m.x157 / (0.0001 + 0.9999 * m.b21) +
    2.6588399811956)**2 + (-m.x158 / (0.0001 + 0.9999 * m.b21) +
    5.16713392802669)**2 - 1) * (0.0001 + 0.9999 * m.b21) + 0.00454025712555548
    * m.b21 <= 0.00454025712555548)
m.e84 = Constraint(expr= ((-m.x159 / (0.0001 + 0.9999 * m.b22) +
    8.82094045941646)**2 + (-m.x160 / (0.0001 + 0.9999 * m.b22) +
    9.51816335093057)**2 + (-m.x161 / (0.0001 + 0.9999 * m.b22) +
    0.894770759747333)**2 - 1) * (0.0001 + 0.9999 * m.b22) + 0.0168205038876067
    * m.b22 <= 0.0168205038876067)
m.e85 = Constraint(expr= ((-m.x162 / (0.0001 + 0.9999 * m.b23) +
    6.86229591973038)**2 + (-m.x163 / (0.0001 + 0.9999 * m.b23) +
    4.74665709736901)**2 + (-m.x164 / (0.0001 + 0.9999 * m.b23) +
    1.14651582775383)**2 - 1) * (0.0001 + 0.9999 * m.b23) + 0.0069936357433242
    * m.b23 <= 0.0069936357433242)
m.e86 = Constraint(expr= ((-m.x165 / (0.0001 + 0.9999 * m.b24) +
    7.13880287505566)**2 + (-m.x166 / (0.0001 + 0.9999 * m.b24) +
    0.923639199248324)**2 + (-m.x167 / (0.0001 + 0.9999 * m.b24) +
    5.06906794010293)**2 - 1) * (0.0001 + 0.9999 * m.b24) + 0.00765110656406704
    * m.b24 <= 0.00765110656406704)
m.e87 = Constraint(expr= ((-m.x168 / (0.0001 + 0.9999 * m.b25) +
    9.54873475130122)**2 + (-m.x169 / (0.0001 + 0.9999 * m.b25) +
    9.730708594994)**2 + (-m.x170 / (0.0001 + 0.9999 * m.b25) +
    0.506682101270036)**2 - 1) * (0.0001 + 0.9999 * m.b25) + 0.0185121751863145
    * m.b25 <= 0.0185121751863145)
m.e88 = Constraint(expr= ((-m.x171 / (0.0001 + 0.9999 * m.b26) +
    2.60295575976191)**2 + (-m.x172 / (0.0001 + 0.9999 * m.b26) +
    9.60525309364094)**2 + (-m.x173 / (0.0001 + 0.9999 * m.b26) +
    5.33059723504087)**2 - 1) * (0.0001 + 0.9999 * m.b26) + 0.0126451532562402
    * m.b26 <= 0.0126451532562402)
m.e89 = Constraint(expr= ((-m.x174 / (0.0001 + 0.9999 * m.b27) +
    8.7489239697277)**2 + (-m.x175 / (0.0001 + 0.9999 * m.b27) +
    6.42418905563567)**2 + (-m.x176 / (0.0001 + 0.9999 * m.b27) +
    6.53764526999883)**2 - 1) * (0.0001 + 0.9999 * m.b27) + 0.0159554681326963
    * m.b27 <= 0.0159554681326963)
m.e90 = Constraint(expr= ((-m.x177 / (0.0001 + 0.9999 * m.b28) +
    2.98069751112782)**2 + (-m.x178 / (0.0001 + 0.9999 * m.b28) +
    1.4913715136506)**2 + (-m.x179 / (0.0001 + 0.9999 * m.b28) +
    2.04987567063475)**2 - 1) * (0.0001 + 0.9999 * m.b28) + 0.00143107369096323
    * m.b28 <= 0.00143107369096323)
m.e91 = Constraint(expr= ((-m.x180 / (0.0001 + 0.9999 * m.b29) +
    1.65791995565741)**2 + (-m.x181 / (0.0001 + 0.9999 * m.b29) +
    6.17322651944292)**2 + (-m.x182 / (0.0001 + 0.9999 * m.b29) +
    7.01412219987569)**2 - 1) * (0.0001 + 0.9999 * m.b29) + 0.00890553344745093
    * m.b29 <= 0.00890553344745093)
m.e92 = Constraint(expr= ((-m.x183 / (0.0001 + 0.9999 * m.b30) +
    2.41953526971379)**2 + (-m.x184 / (0.0001 + 0.9999 * m.b30) +
    1.09500973629707)**2 + (-m.x185 / (0.0001 + 0.9999 * m.b30) +
    2.60189595048839)**2 - 1) * (0.0001 + 0.9999 * m.b30) + 0.00128230597811422
    * m.b30 <= 0.00128230597811422)
m.e93 = Constraint(expr= m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 + m.b27
    + m.b28 + m.b29 + m.b30 == 1)
m.e94 = Constraint(expr= ((-m.x186 / (0.0001 + 0.9999 * m.b31) +
    3.55441530772447)**2 + (-m.x187 / (0.0001 + 0.9999 * m.b31) +
    2.6588399811956)**2 + (-m.x188 / (0.0001 + 0.9999 * m.b31) +
    5.16713392802669)**2 - 1) * (0.0001 + 0.9999 * m.b31) + 0.00454025712555548
    * m.b31 <= 0.00454025712555548)
m.e95 = Constraint(expr= ((-m.x189 / (0.0001 + 0.9999 * m.b32) +
    8.82094045941646)**2 + (-m.x190 / (0.0001 + 0.9999 * m.b32) +
    9.51816335093057)**2 + (-m.x191 / (0.0001 + 0.9999 * m.b32) +
    0.894770759747333)**2 - 1) * (0.0001 + 0.9999 * m.b32) + 0.0168205038876067
    * m.b32 <= 0.0168205038876067)
m.e96 = Constraint(expr= ((-m.x192 / (0.0001 + 0.9999 * m.b33) +
    6.86229591973038)**2 + (-m.x193 / (0.0001 + 0.9999 * m.b33) +
    4.74665709736901)**2 + (-m.x194 / (0.0001 + 0.9999 * m.b33) +
    1.14651582775383)**2 - 1) * (0.0001 + 0.9999 * m.b33) + 0.0069936357433242
    * m.b33 <= 0.0069936357433242)
m.e97 = Constraint(expr= ((-m.x195 / (0.0001 + 0.9999 * m.b34) +
    7.13880287505566)**2 + (-m.x196 / (0.0001 + 0.9999 * m.b34) +
    0.923639199248324)**2 + (-m.x197 / (0.0001 + 0.9999 * m.b34) +
    5.06906794010293)**2 - 1) * (0.0001 + 0.9999 * m.b34) + 0.00765110656406704
    * m.b34 <= 0.00765110656406704)
m.e98 = Constraint(expr= ((-m.x198 / (0.0001 + 0.9999 * m.b35) +
    9.54873475130122)**2 + (-m.x199 / (0.0001 + 0.9999 * m.b35) +
    9.730708594994)**2 + (-m.x200 / (0.0001 + 0.9999 * m.b35) +
    0.506682101270036)**2 - 1) * (0.0001 + 0.9999 * m.b35) + 0.0185121751863145
    * m.b35 <= 0.0185121751863145)
m.e99 = Constraint(expr= ((-m.x201 / (0.0001 + 0.9999 * m.b36) +
    2.60295575976191)**2 + (-m.x202 / (0.0001 + 0.9999 * m.b36) +
    9.60525309364094)**2 + (-m.x203 / (0.0001 + 0.9999 * m.b36) +
    5.33059723504087)**2 - 1) * (0.0001 + 0.9999 * m.b36) + 0.0126451532562402
    * m.b36 <= 0.0126451532562402)
m.e100 = Constraint(expr= ((-m.x204 / (0.0001 + 0.9999 * m.b37) +
    8.7489239697277)**2 + (-m.x205 / (0.0001 + 0.9999 * m.b37) +
    6.42418905563567)**2 + (-m.x206 / (0.0001 + 0.9999 * m.b37) +
    6.53764526999883)**2 - 1) * (0.0001 + 0.9999 * m.b37) + 0.0159554681326963
    * m.b37 <= 0.0159554681326963)
m.e101 = Constraint(expr= ((-m.x207 / (0.0001 + 0.9999 * m.b38) +
    2.98069751112782)**2 + (-m.x208 / (0.0001 + 0.9999 * m.b38) +
    1.4913715136506)**2 + (-m.x209 / (0.0001 + 0.9999 * m.b38) +
    2.04987567063475)**2 - 1) * (0.0001 + 0.9999 * m.b38) + 0.00143107369096323
    * m.b38 <= 0.00143107369096323)
m.e102 = Constraint(expr= ((-m.x210 / (0.0001 + 0.9999 * m.b39) +
    1.65791995565741)**2 + (-m.x211 / (0.0001 + 0.9999 * m.b39) +
    6.17322651944292)**2 + (-m.x212 / (0.0001 + 0.9999 * m.b39) +
    7.01412219987569)**2 - 1) * (0.0001 + 0.9999 * m.b39) + 0.00890553344745093
    * m.b39 <= 0.00890553344745093)
m.e103 = Constraint(expr= ((-m.x213 / (0.0001 + 0.9999 * m.b40) +
    2.41953526971379)**2 + (-m.x214 / (0.0001 + 0.9999 * m.b40) +
    1.09500973629707)**2 + (-m.x215 / (0.0001 + 0.9999 * m.b40) +
    2.60189595048839)**2 - 1) * (0.0001 + 0.9999 * m.b40) + 0.00128230597811422
    * m.b40 <= 0.00128230597811422)
m.e104 = Constraint(expr= m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 + m.b37
    + m.b38 + m.b39 + m.b40 == 1)
m.e105 = Constraint(expr= ((-m.x216 / (0.0001 + 0.9999 * m.b41) +
    3.55441530772447)**2 + (-m.x217 / (0.0001 + 0.9999 * m.b41) +
    2.6588399811956)**2 + (-m.x218 / (0.0001 + 0.9999 * m.b41) +
    5.16713392802669)**2 - 1) * (0.0001 + 0.9999 * m.b41) + 0.00454025712555548
    * m.b41 <= 0.00454025712555548)
m.e106 = Constraint(expr= ((-m.x219 / (0.0001 + 0.9999 * m.b42) +
    8.82094045941646)**2 + (-m.x220 / (0.0001 + 0.9999 * m.b42) +
    9.51816335093057)**2 + (-m.x221 / (0.0001 + 0.9999 * m.b42) +
    0.894770759747333)**2 - 1) * (0.0001 + 0.9999 * m.b42) + 0.0168205038876067
    * m.b42 <= 0.0168205038876067)
m.e107 = Constraint(expr= ((-m.x222 / (0.0001 + 0.9999 * m.b43) +
    6.86229591973038)**2 + (-m.x223 / (0.0001 + 0.9999 * m.b43) +
    4.74665709736901)**2 + (-m.x224 / (0.0001 + 0.9999 * m.b43) +
    1.14651582775383)**2 - 1) * (0.0001 + 0.9999 * m.b43) + 0.0069936357433242
    * m.b43 <= 0.0069936357433242)
m.e108 = Constraint(expr= ((-m.x225 / (0.0001 + 0.9999 * m.b44) +
    7.13880287505566)**2 + (-m.x226 / (0.0001 + 0.9999 * m.b44) +
    0.923639199248324)**2 + (-m.x227 / (0.0001 + 0.9999 * m.b44) +
    5.06906794010293)**2 - 1) * (0.0001 + 0.9999 * m.b44) + 0.00765110656406704
    * m.b44 <= 0.00765110656406704)
m.e109 = Constraint(expr= ((-m.x228 / (0.0001 + 0.9999 * m.b45) +
    9.54873475130122)**2 + (-m.x229 / (0.0001 + 0.9999 * m.b45) +
    9.730708594994)**2 + (-m.x230 / (0.0001 + 0.9999 * m.b45) +
    0.506682101270036)**2 - 1) * (0.0001 + 0.9999 * m.b45) + 0.0185121751863145
    * m.b45 <= 0.0185121751863145)
m.e110 = Constraint(expr= ((-m.x231 / (0.0001 + 0.9999 * m.b46) +
    2.60295575976191)**2 + (-m.x232 / (0.0001 + 0.9999 * m.b46) +
    9.60525309364094)**2 + (-m.x233 / (0.0001 + 0.9999 * m.b46) +
    5.33059723504087)**2 - 1) * (0.0001 + 0.9999 * m.b46) + 0.0126451532562402
    * m.b46 <= 0.0126451532562402)
m.e111 = Constraint(expr= ((-m.x234 / (0.0001 + 0.9999 * m.b47) +
    8.7489239697277)**2 + (-m.x235 / (0.0001 + 0.9999 * m.b47) +
    6.42418905563567)**2 + (-m.x236 / (0.0001 + 0.9999 * m.b47) +
    6.53764526999883)**2 - 1) * (0.0001 + 0.9999 * m.b47) + 0.0159554681326963
    * m.b47 <= 0.0159554681326963)
m.e112 = Constraint(expr= ((-m.x237 / (0.0001 + 0.9999 * m.b48) +
    2.98069751112782)**2 + (-m.x238 / (0.0001 + 0.9999 * m.b48) +
    1.4913715136506)**2 + (-m.x239 / (0.0001 + 0.9999 * m.b48) +
    2.04987567063475)**2 - 1) * (0.0001 + 0.9999 * m.b48) + 0.00143107369096323
    * m.b48 <= 0.00143107369096323)
m.e113 = Constraint(expr= ((-m.x240 / (0.0001 + 0.9999 * m.b49) +
    1.65791995565741)**2 + (-m.x241 / (0.0001 + 0.9999 * m.b49) +
    6.17322651944292)**2 + (-m.x242 / (0.0001 + 0.9999 * m.b49) +
    7.01412219987569)**2 - 1) * (0.0001 + 0.9999 * m.b49) + 0.00890553344745093
    * m.b49 <= 0.00890553344745093)
m.e114 = Constraint(expr= ((-m.x243 / (0.0001 + 0.9999 * m.b50) +
    2.41953526971379)**2 + (-m.x244 / (0.0001 + 0.9999 * m.b50) +
    1.09500973629707)**2 + (-m.x245 / (0.0001 + 0.9999 * m.b50) +
    2.60189595048839)**2 - 1) * (0.0001 + 0.9999 * m.b50) + 0.00128230597811422
    * m.b50 <= 0.00128230597811422)
m.e115 = Constraint(expr= m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47
    + m.b48 + m.b49 + m.b50 == 1)
m.e116 = Constraint(expr= m.b1 + m.b11 + m.b21 + m.b31 + m.b41 <= 1)
m.e117 = Constraint(expr= m.b2 + m.b12 + m.b22 + m.b32 + m.b42 <= 1)
m.e118 = Constraint(expr= m.b3 + m.b13 + m.b23 + m.b33 + m.b43 <= 1)
m.e119 = Constraint(expr= m.b4 + m.b14 + m.b24 + m.b34 + m.b44 <= 1)
m.e120 = Constraint(expr= m.b5 + m.b15 + m.b25 + m.b35 + m.b45 <= 1)
m.e121 = Constraint(expr= m.b6 + m.b16 + m.b26 + m.b36 + m.b46 <= 1)
m.e122 = Constraint(expr= m.b7 + m.b17 + m.b27 + m.b37 + m.b47 <= 1)
m.e123 = Constraint(expr= m.b8 + m.b18 + m.b28 + m.b38 + m.b48 <= 1)
m.e124 = Constraint(expr= m.b9 + m.b19 + m.b29 + m.b39 + m.b49 <= 1)
m.e125 = Constraint(expr= m.b10 + m.b20 + m.b30 + m.b40 + m.b50 <= 1)
m.e126 = Constraint(expr= -m.x51 + m.x96 + m.x99 + m.x102 + m.x105 + m.x108 +
    m.x111 + m.x114 + m.x117 + m.x120 + m.x123 == 0)
m.e127 = Constraint(expr= -m.x54 + m.x97 + m.x100 + m.x103 + m.x106 + m.x109 +
    m.x112 + m.x115 + m.x118 + m.x121 + m.x124 == 0)
m.e128 = Constraint(expr= -m.x57 + m.x98 + m.x101 + m.x104 + m.x107 + m.x110 +
    m.x113 + m.x116 + m.x119 + m.x122 + m.x125 == 0)
m.e129 = Constraint(expr= -m.x52 + m.x126 + m.x129 + m.x132 + m.x135 + m.x138
    + m.x141 + m.x144 + m.x147 + m.x150 + m.x153 == 0)
m.e130 = Constraint(expr= -m.x55 + m.x127 + m.x130 + m.x133 + m.x136 + m.x139
    + m.x142 + m.x145 + m.x148 + m.x151 + m.x154 == 0)
m.e131 = Constraint(expr= -m.x58 + m.x128 + m.x131 + m.x134 + m.x137 + m.x140
    + m.x143 + m.x146 + m.x149 + m.x152 + m.x155 == 0)
m.e132 = Constraint(expr= -m.x60 + m.x156 + m.x159 + m.x162 + m.x165 + m.x168
    + m.x171 + m.x174 + m.x177 + m.x180 + m.x183 == 0)
m.e133 = Constraint(expr= -m.x62 + m.x157 + m.x160 + m.x163 + m.x166 + m.x169
    + m.x172 + m.x175 + m.x178 + m.x181 + m.x184 == 0)
m.e134 = Constraint(expr= -m.x64 + m.x158 + m.x161 + m.x164 + m.x167 + m.x170
    + m.x173 + m.x176 + m.x179 + m.x182 + m.x185 == 0)
m.e135 = Constraint(expr= -m.x66 + m.x186 + m.x189 + m.x192 + m.x195 + m.x198
    + m.x201 + m.x204 + m.x207 + m.x210 + m.x213 == 0)
m.e136 = Constraint(expr= -m.x68 + m.x187 + m.x190 + m.x193 + m.x196 + m.x199
    + m.x202 + m.x205 + m.x208 + m.x211 + m.x214 == 0)
m.e137 = Constraint(expr= -m.x70 + m.x188 + m.x191 + m.x194 + m.x197 + m.x200
    + m.x203 + m.x206 + m.x209 + m.x212 + m.x215 == 0)
m.e138 = Constraint(expr= -m.x72 + m.x216 + m.x219 + m.x222 + m.x225 + m.x228
    + m.x231 + m.x234 + m.x237 + m.x240 + m.x243 == 0)
m.e139 = Constraint(expr= -m.x74 + m.x217 + m.x220 + m.x223 + m.x226 + m.x229
    + m.x232 + m.x235 + m.x238 + m.x241 + m.x244 == 0)
m.e140 = Constraint(expr= -m.x76 + m.x218 + m.x221 + m.x224 + m.x227 + m.x230
    + m.x233 + m.x236 + m.x239 + m.x242 + m.x245 == 0)
m.e141 = Constraint(expr= -10 * m.b1 + m.x96 <= 0)
m.e142 = Constraint(expr= -10 * m.b2 + m.x99 <= 0)
m.e143 = Constraint(expr= -10 * m.b3 + m.x102 <= 0)
m.e144 = Constraint(expr= -10 * m.b4 + m.x105 <= 0)
m.e145 = Constraint(expr= -10 * m.b5 + m.x108 <= 0)
m.e146 = Constraint(expr= -10 * m.b6 + m.x111 <= 0)
m.e147 = Constraint(expr= -10 * m.b7 + m.x114 <= 0)
m.e148 = Constraint(expr= -10 * m.b8 + m.x117 <= 0)
m.e149 = Constraint(expr= -10 * m.b9 + m.x120 <= 0)
m.e150 = Constraint(expr= -10 * m.b10 + m.x123 <= 0)
m.e151 = Constraint(expr= -10 * m.b1 + m.x97 <= 0)
m.e152 = Constraint(expr= -10 * m.b2 + m.x100 <= 0)
m.e153 = Constraint(expr= -10 * m.b3 + m.x103 <= 0)
m.e154 = Constraint(expr= -10 * m.b4 + m.x106 <= 0)
m.e155 = Constraint(expr= -10 * m.b5 + m.x109 <= 0)
m.e156 = Constraint(expr= -10 * m.b6 + m.x112 <= 0)
m.e157 = Constraint(expr= -10 * m.b7 + m.x115 <= 0)
m.e158 = Constraint(expr= -10 * m.b8 + m.x118 <= 0)
m.e159 = Constraint(expr= -10 * m.b9 + m.x121 <= 0)
m.e160 = Constraint(expr= -10 * m.b10 + m.x124 <= 0)
m.e161 = Constraint(expr= -10 * m.b1 + m.x98 <= 0)
m.e162 = Constraint(expr= -10 * m.b2 + m.x101 <= 0)
m.e163 = Constraint(expr= -10 * m.b3 + m.x104 <= 0)
m.e164 = Constraint(expr= -10 * m.b4 + m.x107 <= 0)
m.e165 = Constraint(expr= -10 * m.b5 + m.x110 <= 0)
m.e166 = Constraint(expr= -10 * m.b6 + m.x113 <= 0)
m.e167 = Constraint(expr= -10 * m.b7 + m.x116 <= 0)
m.e168 = Constraint(expr= -10 * m.b8 + m.x119 <= 0)
m.e169 = Constraint(expr= -10 * m.b9 + m.x122 <= 0)
m.e170 = Constraint(expr= -10 * m.b10 + m.x125 <= 0)
m.e171 = Constraint(expr= -10 * m.b11 + m.x126 <= 0)
m.e172 = Constraint(expr= -10 * m.b12 + m.x129 <= 0)
m.e173 = Constraint(expr= -10 * m.b13 + m.x132 <= 0)
m.e174 = Constraint(expr= -10 * m.b14 + m.x135 <= 0)
m.e175 = Constraint(expr= -10 * m.b15 + m.x138 <= 0)
m.e176 = Constraint(expr= -10 * m.b16 + m.x141 <= 0)
m.e177 = Constraint(expr= -10 * m.b17 + m.x144 <= 0)
m.e178 = Constraint(expr= -10 * m.b18 + m.x147 <= 0)
m.e179 = Constraint(expr= -10 * m.b19 + m.x150 <= 0)
m.e180 = Constraint(expr= -10 * m.b20 + m.x153 <= 0)
m.e181 = Constraint(expr= -10 * m.b11 + m.x127 <= 0)
m.e182 = Constraint(expr= -10 * m.b12 + m.x130 <= 0)
m.e183 = Constraint(expr= -10 * m.b13 + m.x133 <= 0)
m.e184 = Constraint(expr= -10 * m.b14 + m.x136 <= 0)
m.e185 = Constraint(expr= -10 * m.b15 + m.x139 <= 0)
m.e186 = Constraint(expr= -10 * m.b16 + m.x142 <= 0)
m.e187 = Constraint(expr= -10 * m.b17 + m.x145 <= 0)
m.e188 = Constraint(expr= -10 * m.b18 + m.x148 <= 0)
m.e189 = Constraint(expr= -10 * m.b19 + m.x151 <= 0)
m.e190 = Constraint(expr= -10 * m.b20 + m.x154 <= 0)
m.e191 = Constraint(expr= -10 * m.b11 + m.x128 <= 0)
m.e192 = Constraint(expr= -10 * m.b12 + m.x131 <= 0)
m.e193 = Constraint(expr= -10 * m.b13 + m.x134 <= 0)
m.e194 = Constraint(expr= -10 * m.b14 + m.x137 <= 0)
m.e195 = Constraint(expr= -10 * m.b15 + m.x140 <= 0)
m.e196 = Constraint(expr= -10 * m.b16 + m.x143 <= 0)
m.e197 = Constraint(expr= -10 * m.b17 + m.x146 <= 0)
m.e198 = Constraint(expr= -10 * m.b18 + m.x149 <= 0)
m.e199 = Constraint(expr= -10 * m.b19 + m.x152 <= 0)
m.e200 = Constraint(expr= -10 * m.b20 + m.x155 <= 0)
m.e201 = Constraint(expr= -10 * m.b21 + m.x156 <= 0)
m.e202 = Constraint(expr= -10 * m.b22 + m.x159 <= 0)
m.e203 = Constraint(expr= -10 * m.b23 + m.x162 <= 0)
m.e204 = Constraint(expr= -10 * m.b24 + m.x165 <= 0)
m.e205 = Constraint(expr= -10 * m.b25 + m.x168 <= 0)
m.e206 = Constraint(expr= -10 * m.b26 + m.x171 <= 0)
m.e207 = Constraint(expr= -10 * m.b27 + m.x174 <= 0)
m.e208 = Constraint(expr= -10 * m.b28 + m.x177 <= 0)
m.e209 = Constraint(expr= -10 * m.b29 + m.x180 <= 0)
m.e210 = Constraint(expr= -10 * m.b30 + m.x183 <= 0)
m.e211 = Constraint(expr= -10 * m.b21 + m.x157 <= 0)
m.e212 = Constraint(expr= -10 * m.b22 + m.x160 <= 0)
m.e213 = Constraint(expr= -10 * m.b23 + m.x163 <= 0)
m.e214 = Constraint(expr= -10 * m.b24 + m.x166 <= 0)
m.e215 = Constraint(expr= -10 * m.b25 + m.x169 <= 0)
m.e216 = Constraint(expr= -10 * m.b26 + m.x172 <= 0)
m.e217 = Constraint(expr= -10 * m.b27 + m.x175 <= 0)
m.e218 = Constraint(expr= -10 * m.b28 + m.x178 <= 0)
m.e219 = Constraint(expr= -10 * m.b29 + m.x181 <= 0)
m.e220 = Constraint(expr= -10 * m.b30 + m.x184 <= 0)
m.e221 = Constraint(expr= -10 * m.b21 + m.x158 <= 0)
m.e222 = Constraint(expr= -10 * m.b22 + m.x161 <= 0)
m.e223 = Constraint(expr= -10 * m.b23 + m.x164 <= 0)
m.e224 = Constraint(expr= -10 * m.b24 + m.x167 <= 0)
m.e225 = Constraint(expr= -10 * m.b25 + m.x170 <= 0)
m.e226 = Constraint(expr= -10 * m.b26 + m.x173 <= 0)
m.e227 = Constraint(expr= -10 * m.b27 + m.x176 <= 0)
m.e228 = Constraint(expr= -10 * m.b28 + m.x179 <= 0)
m.e229 = Constraint(expr= -10 * m.b29 + m.x182 <= 0)
m.e230 = Constraint(expr= -10 * m.b30 + m.x185 <= 0)
m.e231 = Constraint(expr= -10 * m.b31 + m.x186 <= 0)
m.e232 = Constraint(expr= -10 * m.b32 + m.x189 <= 0)
m.e233 = Constraint(expr= -10 * m.b33 + m.x192 <= 0)
m.e234 = Constraint(expr= -10 * m.b34 + m.x195 <= 0)
m.e235 = Constraint(expr= -10 * m.b35 + m.x198 <= 0)
m.e236 = Constraint(expr= -10 * m.b36 + m.x201 <= 0)
m.e237 = Constraint(expr= -10 * m.b37 + m.x204 <= 0)
m.e238 = Constraint(expr= -10 * m.b38 + m.x207 <= 0)
m.e239 = Constraint(expr= -10 * m.b39 + m.x210 <= 0)
m.e240 = Constraint(expr= -10 * m.b40 + m.x213 <= 0)
m.e241 = Constraint(expr= -10 * m.b31 + m.x187 <= 0)
m.e242 = Constraint(expr= -10 * m.b32 + m.x190 <= 0)
m.e243 = Constraint(expr= -10 * m.b33 + m.x193 <= 0)
m.e244 = Constraint(expr= -10 * m.b34 + m.x196 <= 0)
m.e245 = Constraint(expr= -10 * m.b35 + m.x199 <= 0)
m.e246 = Constraint(expr= -10 * m.b36 + m.x202 <= 0)
m.e247 = Constraint(expr= -10 * m.b37 + m.x205 <= 0)
m.e248 = Constraint(expr= -10 * m.b38 + m.x208 <= 0)
m.e249 = Constraint(expr= -10 * m.b39 + m.x211 <= 0)
m.e250 = Constraint(expr= -10 * m.b40 + m.x214 <= 0)
m.e251 = Constraint(expr= -10 * m.b31 + m.x188 <= 0)
m.e252 = Constraint(expr= -10 * m.b32 + m.x191 <= 0)
m.e253 = Constraint(expr= -10 * m.b33 + m.x194 <= 0)
m.e254 = Constraint(expr= -10 * m.b34 + m.x197 <= 0)
m.e255 = Constraint(expr= -10 * m.b35 + m.x200 <= 0)
m.e256 = Constraint(expr= -10 * m.b36 + m.x203 <= 0)
m.e257 = Constraint(expr= -10 * m.b37 + m.x206 <= 0)
m.e258 = Constraint(expr= -10 * m.b38 + m.x209 <= 0)
m.e259 = Constraint(expr= -10 * m.b39 + m.x212 <= 0)
m.e260 = Constraint(expr= -10 * m.b40 + m.x215 <= 0)
m.e261 = Constraint(expr= -10 * m.b41 + m.x216 <= 0)
m.e262 = Constraint(expr= -10 * m.b42 + m.x219 <= 0)
m.e263 = Constraint(expr= -10 * m.b43 + m.x222 <= 0)
m.e264 = Constraint(expr= -10 * m.b44 + m.x225 <= 0)
m.e265 = Constraint(expr= -10 * m.b45 + m.x228 <= 0)
m.e266 = Constraint(expr= -10 * m.b46 + m.x231 <= 0)
m.e267 = Constraint(expr= -10 * m.b47 + m.x234 <= 0)
m.e268 = Constraint(expr= -10 * m.b48 + m.x237 <= 0)
m.e269 = Constraint(expr= -10 * m.b49 + m.x240 <= 0)
m.e270 = Constraint(expr= -10 * m.b50 + m.x243 <= 0)
m.e271 = Constraint(expr= -10 * m.b41 + m.x217 <= 0)
m.e272 = Constraint(expr= -10 * m.b42 + m.x220 <= 0)
m.e273 = Constraint(expr= -10 * m.b43 + m.x223 <= 0)
m.e274 = Constraint(expr= -10 * m.b44 + m.x226 <= 0)
m.e275 = Constraint(expr= -10 * m.b45 + m.x229 <= 0)
m.e276 = Constraint(expr= -10 * m.b46 + m.x232 <= 0)
m.e277 = Constraint(expr= -10 * m.b47 + m.x235 <= 0)
m.e278 = Constraint(expr= -10 * m.b48 + m.x238 <= 0)
m.e279 = Constraint(expr= -10 * m.b49 + m.x241 <= 0)
m.e280 = Constraint(expr= -10 * m.b50 + m.x244 <= 0)
m.e281 = Constraint(expr= -10 * m.b41 + m.x218 <= 0)
m.e282 = Constraint(expr= -10 * m.b42 + m.x221 <= 0)
m.e283 = Constraint(expr= -10 * m.b43 + m.x224 <= 0)
m.e284 = Constraint(expr= -10 * m.b44 + m.x227 <= 0)
m.e285 = Constraint(expr= -10 * m.b45 + m.x230 <= 0)
m.e286 = Constraint(expr= -10 * m.b46 + m.x233 <= 0)
m.e287 = Constraint(expr= -10 * m.b47 + m.x236 <= 0)
m.e288 = Constraint(expr= -10 * m.b48 + m.x239 <= 0)
m.e289 = Constraint(expr= -10 * m.b49 + m.x242 <= 0)
m.e290 = Constraint(expr= -10 * m.b50 + m.x245 <= 0)
m.e291 = Constraint(expr= m.x51 - m.x52 <= 0)
m.e292 = Constraint(expr= m.x52 - m.x60 <= 0)
m.e293 = Constraint(expr= m.x60 - m.x66 <= 0)
m.e294 = Constraint(expr= m.x66 - m.x72 <= 0)
