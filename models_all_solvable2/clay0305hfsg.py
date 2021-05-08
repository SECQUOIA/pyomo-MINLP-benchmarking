# MINLP written by GAMS Convert at 05/07/21 17:13:02
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       395       65       40      290        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       275      220       55        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      1095      915      180
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(11.5,57.5), initialize=11.5)
m.x2 = Var(within=Reals, bounds=(12.5,56.5), initialize=12.5)
m.x3 = Var(within=Reals, bounds=(10.5,58.5), initialize=10.5)
m.x4 = Var(within=Reals, bounds=(10,59), initialize=10)
m.x5 = Var(within=Reals, bounds=(13.5,55.5), initialize=13.5)
m.x6 = Var(within=Reals, bounds=(7,87), initialize=7)
m.x7 = Var(within=Reals, bounds=(6.5,87.5), initialize=6.5)
m.x8 = Var(within=Reals, bounds=(5.5,88.5), initialize=5.5)
m.x9 = Var(within=Reals, bounds=(5.5,88.5), initialize=5.5)
m.x10 = Var(within=Reals, bounds=(7.5,86.5), initialize=7.5)
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
m.x67 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x68 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x69 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x70 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x71 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x72 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x73 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x74 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x75 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x76 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x77 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x78 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x79 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x80 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x81 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x82 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x83 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x84 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x85 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x86 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x87 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x88 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x89 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x90 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x91 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x92 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x93 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x94 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x95 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x96 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x97 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x98 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x99 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x100 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x101 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x102 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x103 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x104 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x105 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x106 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x107 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x108 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x109 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x110 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x111 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x112 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x113 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x114 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x115 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x116 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x117 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x118 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x119 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x120 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x121 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x122 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x123 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x124 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x125 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x126 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x127 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x128 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x129 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x130 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x131 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x132 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x133 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x134 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x135 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x136 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x137 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x138 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x139 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x140 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x141 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x142 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x143 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x144 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x145 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x146 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x147 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x148 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x149 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x150 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x151 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x152 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x153 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x154 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x155 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x156 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x157 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x158 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x159 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x160 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x161 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x162 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x163 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x164 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x165 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x166 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x167 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x168 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x169 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x170 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x171 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x172 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x173 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x174 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x175 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x176 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x177 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x178 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x179 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x180 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x181 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x182 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x183 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x184 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x185 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x186 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x187 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x188 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x189 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x190 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x191 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x192 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x193 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x194 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x195 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x196 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x197 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x198 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x199 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x200 = Var(within=Reals, bounds=(0,None), initialize=0)
m.b201 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b202 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b203 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b204 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b205 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b206 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b207 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b208 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b209 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b210 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b211 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b212 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b213 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b214 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b215 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b216 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b217 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b218 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b219 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b220 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b221 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b222 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b223 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b224 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b225 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b226 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b227 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b228 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b229 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b230 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b231 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b232 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b233 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b234 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b235 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b236 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b237 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b238 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b239 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b240 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b241 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b242 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b243 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b244 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b245 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b246 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b247 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b248 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b249 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b250 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b251 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b252 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b253 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b254 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b255 = Var(within=Binary, bounds=(0,1), initialize=0)
m.x256 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x257 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x258 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x259 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x260 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x261 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x262 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x263 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x264 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x265 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x266 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x267 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x268 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x269 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x270 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x271 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x272 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x273 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x274 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x275 = Var(within=Reals, bounds=(0,None), initialize=0)

m.obj = Objective(sense=minimize, expr= 300 * m.x256 + 240 * m.x257 + 210 *
    m.x258 + 50 * m.x259 + 100 * m.x260 + 150 * m.x261 + 30 * m.x262 + 120 *
    m.x263 + 25 * m.x264 + 60 * m.x265 + 300 * m.x266 + 240 * m.x267 + 210 *
    m.x268 + 50 * m.x269 + 100 * m.x270 + 150 * m.x271 + 30 * m.x272 + 120 *
    m.x273 + 25 * m.x274 + 60 * m.x275)

m.e1 = Constraint(expr= -m.x1 + m.x2 + m.x256 >= 0)
m.e2 = Constraint(expr= -m.x1 + m.x3 + m.x257 >= 0)
m.e3 = Constraint(expr= -m.x1 + m.x4 + m.x258 >= 0)
m.e4 = Constraint(expr= -m.x1 + m.x5 + m.x259 >= 0)
m.e5 = Constraint(expr= -m.x2 + m.x3 + m.x260 >= 0)
m.e6 = Constraint(expr= -m.x2 + m.x4 + m.x261 >= 0)
m.e7 = Constraint(expr= -m.x2 + m.x5 + m.x262 >= 0)
m.e8 = Constraint(expr= -m.x3 + m.x4 + m.x263 >= 0)
m.e9 = Constraint(expr= -m.x3 + m.x5 + m.x264 >= 0)
m.e10 = Constraint(expr= -m.x4 + m.x5 + m.x265 >= 0)
m.e11 = Constraint(expr= m.x1 - m.x2 + m.x256 >= 0)
m.e12 = Constraint(expr= m.x1 - m.x3 + m.x257 >= 0)
m.e13 = Constraint(expr= m.x1 - m.x4 + m.x258 >= 0)
m.e14 = Constraint(expr= m.x1 - m.x5 + m.x259 >= 0)
m.e15 = Constraint(expr= m.x2 - m.x3 + m.x260 >= 0)
m.e16 = Constraint(expr= m.x2 - m.x4 + m.x261 >= 0)
m.e17 = Constraint(expr= m.x2 - m.x5 + m.x262 >= 0)
m.e18 = Constraint(expr= m.x3 - m.x4 + m.x263 >= 0)
m.e19 = Constraint(expr= m.x3 - m.x5 + m.x264 >= 0)
m.e20 = Constraint(expr= m.x4 - m.x5 + m.x265 >= 0)
m.e21 = Constraint(expr= -m.x6 + m.x7 + m.x266 >= 0)
m.e22 = Constraint(expr= -m.x6 + m.x8 + m.x267 >= 0)
m.e23 = Constraint(expr= -m.x6 + m.x9 + m.x268 >= 0)
m.e24 = Constraint(expr= -m.x6 + m.x10 + m.x269 >= 0)
m.e25 = Constraint(expr= -m.x7 + m.x8 + m.x270 >= 0)
m.e26 = Constraint(expr= -m.x7 + m.x9 + m.x271 >= 0)
m.e27 = Constraint(expr= -m.x7 + m.x10 + m.x272 >= 0)
m.e28 = Constraint(expr= -m.x8 + m.x9 + m.x273 >= 0)
m.e29 = Constraint(expr= -m.x8 + m.x10 + m.x274 >= 0)
m.e30 = Constraint(expr= -m.x9 + m.x10 + m.x275 >= 0)
m.e31 = Constraint(expr= m.x6 - m.x7 + m.x266 >= 0)
m.e32 = Constraint(expr= m.x6 - m.x8 + m.x267 >= 0)
m.e33 = Constraint(expr= m.x6 - m.x9 + m.x268 >= 0)
m.e34 = Constraint(expr= m.x6 - m.x10 + m.x269 >= 0)
m.e35 = Constraint(expr= m.x7 - m.x8 + m.x270 >= 0)
m.e36 = Constraint(expr= m.x7 - m.x9 + m.x271 >= 0)
m.e37 = Constraint(expr= m.x7 - m.x10 + m.x272 >= 0)
m.e38 = Constraint(expr= m.x8 - m.x9 + m.x273 >= 0)
m.e39 = Constraint(expr= m.x8 - m.x10 + m.x274 >= 0)
m.e40 = Constraint(expr= m.x9 - m.x10 + m.x275 >= 0)
m.e41 = Constraint(expr= m.x1 - m.x11 - m.x15 - m.x19 - m.x23 == 0)
m.e42 = Constraint(expr= m.x1 - m.x12 - m.x16 - m.x20 - m.x24 == 0)
m.e43 = Constraint(expr= m.x1 - m.x13 - m.x17 - m.x21 - m.x25 == 0)
m.e44 = Constraint(expr= m.x1 - m.x14 - m.x18 - m.x22 - m.x26 == 0)
m.e45 = Constraint(expr= m.x2 - m.x27 - m.x31 - m.x35 - m.x39 == 0)
m.e46 = Constraint(expr= m.x2 - m.x28 - m.x32 - m.x36 - m.x40 == 0)
m.e47 = Constraint(expr= m.x2 - m.x29 - m.x33 - m.x37 - m.x41 == 0)
m.e48 = Constraint(expr= m.x2 - m.x30 - m.x34 - m.x38 - m.x42 == 0)
m.e49 = Constraint(expr= m.x3 - m.x43 - m.x47 - m.x51 - m.x55 == 0)
m.e50 = Constraint(expr= m.x3 - m.x44 - m.x48 - m.x52 - m.x56 == 0)
m.e51 = Constraint(expr= m.x3 - m.x45 - m.x49 - m.x53 - m.x57 == 0)
m.e52 = Constraint(expr= m.x3 - m.x46 - m.x50 - m.x54 - m.x58 == 0)
m.e53 = Constraint(expr= m.x4 - m.x59 - m.x63 - m.x67 - m.x71 == 0)
m.e54 = Constraint(expr= m.x4 - m.x60 - m.x64 - m.x68 - m.x72 == 0)
m.e55 = Constraint(expr= m.x4 - m.x61 - m.x65 - m.x69 - m.x73 == 0)
m.e56 = Constraint(expr= m.x4 - m.x62 - m.x66 - m.x70 - m.x74 == 0)
m.e57 = Constraint(expr= m.x5 - m.x75 - m.x79 - m.x83 - m.x87 == 0)
m.e58 = Constraint(expr= m.x5 - m.x76 - m.x80 - m.x84 - m.x88 == 0)
m.e59 = Constraint(expr= m.x5 - m.x77 - m.x81 - m.x85 - m.x89 == 0)
m.e60 = Constraint(expr= m.x5 - m.x78 - m.x82 - m.x86 - m.x90 == 0)
m.e61 = Constraint(expr= m.x6 - m.x91 - m.x95 - m.x99 - m.x103 == 0)
m.e62 = Constraint(expr= m.x6 - m.x92 - m.x96 - m.x100 - m.x104 == 0)
m.e63 = Constraint(expr= m.x6 - m.x93 - m.x97 - m.x101 - m.x105 == 0)
m.e64 = Constraint(expr= m.x6 - m.x94 - m.x98 - m.x102 - m.x106 == 0)
m.e65 = Constraint(expr= m.x7 - m.x107 - m.x111 - m.x115 - m.x119 == 0)
m.e66 = Constraint(expr= m.x7 - m.x108 - m.x112 - m.x116 - m.x120 == 0)
m.e67 = Constraint(expr= m.x7 - m.x109 - m.x113 - m.x117 - m.x121 == 0)
m.e68 = Constraint(expr= m.x7 - m.x110 - m.x114 - m.x118 - m.x122 == 0)
m.e69 = Constraint(expr= m.x8 - m.x123 - m.x127 - m.x131 - m.x135 == 0)
m.e70 = Constraint(expr= m.x8 - m.x124 - m.x128 - m.x132 - m.x136 == 0)
m.e71 = Constraint(expr= m.x8 - m.x125 - m.x129 - m.x133 - m.x137 == 0)
m.e72 = Constraint(expr= m.x8 - m.x126 - m.x130 - m.x134 - m.x138 == 0)
m.e73 = Constraint(expr= m.x9 - m.x139 - m.x143 - m.x147 - m.x151 == 0)
m.e74 = Constraint(expr= m.x9 - m.x140 - m.x144 - m.x148 - m.x152 == 0)
m.e75 = Constraint(expr= m.x9 - m.x141 - m.x145 - m.x149 - m.x153 == 0)
m.e76 = Constraint(expr= m.x9 - m.x142 - m.x146 - m.x150 - m.x154 == 0)
m.e77 = Constraint(expr= m.x10 - m.x155 - m.x159 - m.x163 - m.x167 == 0)
m.e78 = Constraint(expr= m.x10 - m.x156 - m.x160 - m.x164 - m.x168 == 0)
m.e79 = Constraint(expr= m.x10 - m.x157 - m.x161 - m.x165 - m.x169 == 0)
m.e80 = Constraint(expr= m.x10 - m.x158 - m.x162 - m.x166 - m.x170 == 0)
m.e81 = Constraint(expr= m.x11 - 57.5 * m.b201 <= 0)
m.e82 = Constraint(expr= m.x12 - 57.5 * m.b202 <= 0)
m.e83 = Constraint(expr= m.x13 - 57.5 * m.b203 <= 0)
m.e84 = Constraint(expr= m.x14 - 57.5 * m.b204 <= 0)
m.e85 = Constraint(expr= m.x15 - 57.5 * m.b211 <= 0)
m.e86 = Constraint(expr= m.x16 - 57.5 * m.b212 <= 0)
m.e87 = Constraint(expr= m.x17 - 57.5 * m.b213 <= 0)
m.e88 = Constraint(expr= m.x18 - 57.5 * m.b214 <= 0)
m.e89 = Constraint(expr= m.x19 - 57.5 * m.b221 <= 0)
m.e90 = Constraint(expr= m.x20 - 57.5 * m.b222 <= 0)
m.e91 = Constraint(expr= m.x21 - 57.5 * m.b223 <= 0)
m.e92 = Constraint(expr= m.x22 - 57.5 * m.b224 <= 0)
m.e93 = Constraint(expr= m.x23 - 57.5 * m.b231 <= 0)
m.e94 = Constraint(expr= m.x24 - 57.5 * m.b232 <= 0)
m.e95 = Constraint(expr= m.x25 - 57.5 * m.b233 <= 0)
m.e96 = Constraint(expr= m.x26 - 57.5 * m.b234 <= 0)
m.e97 = Constraint(expr= m.x27 - 57.5 * m.b201 <= 0)
m.e98 = Constraint(expr= m.x28 - 56.5 * m.b205 <= 0)
m.e99 = Constraint(expr= m.x29 - 56.5 * m.b206 <= 0)
m.e100 = Constraint(expr= m.x30 - 56.5 * m.b207 <= 0)
m.e101 = Constraint(expr= m.x31 - 57.5 * m.b211 <= 0)
m.e102 = Constraint(expr= m.x32 - 56.5 * m.b215 <= 0)
m.e103 = Constraint(expr= m.x33 - 56.5 * m.b216 <= 0)
m.e104 = Constraint(expr= m.x34 - 56.5 * m.b217 <= 0)
m.e105 = Constraint(expr= m.x35 - 57.5 * m.b221 <= 0)
m.e106 = Constraint(expr= m.x36 - 56.5 * m.b225 <= 0)
m.e107 = Constraint(expr= m.x37 - 56.5 * m.b226 <= 0)
m.e108 = Constraint(expr= m.x38 - 56.5 * m.b227 <= 0)
m.e109 = Constraint(expr= m.x39 - 57.5 * m.b231 <= 0)
m.e110 = Constraint(expr= m.x40 - 56.5 * m.b235 <= 0)
m.e111 = Constraint(expr= m.x41 - 56.5 * m.b236 <= 0)
m.e112 = Constraint(expr= m.x42 - 56.5 * m.b237 <= 0)
m.e113 = Constraint(expr= m.x43 - 57.5 * m.b202 <= 0)
m.e114 = Constraint(expr= m.x44 - 56.5 * m.b205 <= 0)
m.e115 = Constraint(expr= m.x45 - 58.5 * m.b208 <= 0)
m.e116 = Constraint(expr= m.x46 - 58.5 * m.b209 <= 0)
m.e117 = Constraint(expr= m.x47 - 57.5 * m.b212 <= 0)
m.e118 = Constraint(expr= m.x48 - 56.5 * m.b215 <= 0)
m.e119 = Constraint(expr= m.x49 - 58.5 * m.b218 <= 0)
m.e120 = Constraint(expr= m.x50 - 58.5 * m.b219 <= 0)
m.e121 = Constraint(expr= m.x51 - 57.5 * m.b222 <= 0)
m.e122 = Constraint(expr= m.x52 - 56.5 * m.b225 <= 0)
m.e123 = Constraint(expr= m.x53 - 58.5 * m.b228 <= 0)
m.e124 = Constraint(expr= m.x54 - 58.5 * m.b229 <= 0)
m.e125 = Constraint(expr= m.x55 - 57.5 * m.b232 <= 0)
m.e126 = Constraint(expr= m.x56 - 56.5 * m.b235 <= 0)
m.e127 = Constraint(expr= m.x57 - 58.5 * m.b238 <= 0)
m.e128 = Constraint(expr= m.x58 - 58.5 * m.b239 <= 0)
m.e129 = Constraint(expr= m.x59 - 57.5 * m.b203 <= 0)
m.e130 = Constraint(expr= m.x60 - 56.5 * m.b206 <= 0)
m.e131 = Constraint(expr= m.x61 - 58.5 * m.b208 <= 0)
m.e132 = Constraint(expr= m.x62 - 59 * m.b210 <= 0)
m.e133 = Constraint(expr= m.x63 - 57.5 * m.b213 <= 0)
m.e134 = Constraint(expr= m.x64 - 56.5 * m.b216 <= 0)
m.e135 = Constraint(expr= m.x65 - 58.5 * m.b218 <= 0)
m.e136 = Constraint(expr= m.x66 - 59 * m.b220 <= 0)
m.e137 = Constraint(expr= m.x67 - 57.5 * m.b223 <= 0)
m.e138 = Constraint(expr= m.x68 - 56.5 * m.b226 <= 0)
m.e139 = Constraint(expr= m.x69 - 58.5 * m.b228 <= 0)
m.e140 = Constraint(expr= m.x70 - 59 * m.b230 <= 0)
m.e141 = Constraint(expr= m.x71 - 57.5 * m.b233 <= 0)
m.e142 = Constraint(expr= m.x72 - 56.5 * m.b236 <= 0)
m.e143 = Constraint(expr= m.x73 - 58.5 * m.b238 <= 0)
m.e144 = Constraint(expr= m.x74 - 59 * m.b240 <= 0)
m.e145 = Constraint(expr= m.x75 - 57.5 * m.b204 <= 0)
m.e146 = Constraint(expr= m.x76 - 56.5 * m.b207 <= 0)
m.e147 = Constraint(expr= m.x77 - 58.5 * m.b209 <= 0)
m.e148 = Constraint(expr= m.x78 - 59 * m.b210 <= 0)
m.e149 = Constraint(expr= m.x79 - 57.5 * m.b214 <= 0)
m.e150 = Constraint(expr= m.x80 - 56.5 * m.b217 <= 0)
m.e151 = Constraint(expr= m.x81 - 58.5 * m.b219 <= 0)
m.e152 = Constraint(expr= m.x82 - 59 * m.b220 <= 0)
m.e153 = Constraint(expr= m.x83 - 57.5 * m.b224 <= 0)
m.e154 = Constraint(expr= m.x84 - 56.5 * m.b227 <= 0)
m.e155 = Constraint(expr= m.x85 - 58.5 * m.b229 <= 0)
m.e156 = Constraint(expr= m.x86 - 59 * m.b230 <= 0)
m.e157 = Constraint(expr= m.x87 - 57.5 * m.b234 <= 0)
m.e158 = Constraint(expr= m.x88 - 56.5 * m.b237 <= 0)
m.e159 = Constraint(expr= m.x89 - 58.5 * m.b239 <= 0)
m.e160 = Constraint(expr= m.x90 - 59 * m.b240 <= 0)
m.e161 = Constraint(expr= m.x91 - 87 * m.b201 <= 0)
m.e162 = Constraint(expr= m.x92 - 87 * m.b202 <= 0)
m.e163 = Constraint(expr= m.x93 - 87 * m.b203 <= 0)
m.e164 = Constraint(expr= m.x94 - 87 * m.b204 <= 0)
m.e165 = Constraint(expr= m.x95 - 87 * m.b211 <= 0)
m.e166 = Constraint(expr= m.x96 - 87 * m.b212 <= 0)
m.e167 = Constraint(expr= m.x97 - 87 * m.b213 <= 0)
m.e168 = Constraint(expr= m.x98 - 87 * m.b214 <= 0)
m.e169 = Constraint(expr= m.x99 - 87 * m.b221 <= 0)
m.e170 = Constraint(expr= m.x100 - 87 * m.b222 <= 0)
m.e171 = Constraint(expr= m.x101 - 87 * m.b223 <= 0)
m.e172 = Constraint(expr= m.x102 - 87 * m.b224 <= 0)
m.e173 = Constraint(expr= m.x103 - 87 * m.b231 <= 0)
m.e174 = Constraint(expr= m.x104 - 87 * m.b232 <= 0)
m.e175 = Constraint(expr= m.x105 - 87 * m.b233 <= 0)
m.e176 = Constraint(expr= m.x106 - 87 * m.b234 <= 0)
m.e177 = Constraint(expr= m.x107 - 87 * m.b201 <= 0)
m.e178 = Constraint(expr= m.x108 - 87.5 * m.b205 <= 0)
m.e179 = Constraint(expr= m.x109 - 87.5 * m.b206 <= 0)
m.e180 = Constraint(expr= m.x110 - 87.5 * m.b207 <= 0)
m.e181 = Constraint(expr= m.x111 - 87 * m.b211 <= 0)
m.e182 = Constraint(expr= m.x112 - 87.5 * m.b215 <= 0)
m.e183 = Constraint(expr= m.x113 - 87.5 * m.b216 <= 0)
m.e184 = Constraint(expr= m.x114 - 87.5 * m.b217 <= 0)
m.e185 = Constraint(expr= m.x115 - 87 * m.b221 <= 0)
m.e186 = Constraint(expr= m.x116 - 87.5 * m.b225 <= 0)
m.e187 = Constraint(expr= m.x117 - 87.5 * m.b226 <= 0)
m.e188 = Constraint(expr= m.x118 - 87.5 * m.b227 <= 0)
m.e189 = Constraint(expr= m.x119 - 87 * m.b231 <= 0)
m.e190 = Constraint(expr= m.x120 - 87.5 * m.b235 <= 0)
m.e191 = Constraint(expr= m.x121 - 87.5 * m.b236 <= 0)
m.e192 = Constraint(expr= m.x122 - 87.5 * m.b237 <= 0)
m.e193 = Constraint(expr= m.x123 - 87 * m.b202 <= 0)
m.e194 = Constraint(expr= m.x124 - 87.5 * m.b205 <= 0)
m.e195 = Constraint(expr= m.x125 - 88.5 * m.b208 <= 0)
m.e196 = Constraint(expr= m.x126 - 88.5 * m.b209 <= 0)
m.e197 = Constraint(expr= m.x127 - 87 * m.b212 <= 0)
m.e198 = Constraint(expr= m.x128 - 87.5 * m.b215 <= 0)
m.e199 = Constraint(expr= m.x129 - 88.5 * m.b218 <= 0)
m.e200 = Constraint(expr= m.x130 - 88.5 * m.b219 <= 0)
m.e201 = Constraint(expr= m.x131 - 87 * m.b222 <= 0)
m.e202 = Constraint(expr= m.x132 - 87.5 * m.b225 <= 0)
m.e203 = Constraint(expr= m.x133 - 88.5 * m.b228 <= 0)
m.e204 = Constraint(expr= m.x134 - 88.5 * m.b229 <= 0)
m.e205 = Constraint(expr= m.x135 - 87 * m.b232 <= 0)
m.e206 = Constraint(expr= m.x136 - 87.5 * m.b235 <= 0)
m.e207 = Constraint(expr= m.x137 - 88.5 * m.b238 <= 0)
m.e208 = Constraint(expr= m.x138 - 88.5 * m.b239 <= 0)
m.e209 = Constraint(expr= m.x139 - 87 * m.b203 <= 0)
m.e210 = Constraint(expr= m.x140 - 87.5 * m.b206 <= 0)
m.e211 = Constraint(expr= m.x141 - 88.5 * m.b208 <= 0)
m.e212 = Constraint(expr= m.x142 - 88.5 * m.b210 <= 0)
m.e213 = Constraint(expr= m.x143 - 87 * m.b213 <= 0)
m.e214 = Constraint(expr= m.x144 - 87.5 * m.b216 <= 0)
m.e215 = Constraint(expr= m.x145 - 88.5 * m.b218 <= 0)
m.e216 = Constraint(expr= m.x146 - 88.5 * m.b220 <= 0)
m.e217 = Constraint(expr= m.x147 - 87 * m.b223 <= 0)
m.e218 = Constraint(expr= m.x148 - 87.5 * m.b226 <= 0)
m.e219 = Constraint(expr= m.x149 - 88.5 * m.b228 <= 0)
m.e220 = Constraint(expr= m.x150 - 88.5 * m.b230 <= 0)
m.e221 = Constraint(expr= m.x151 - 87 * m.b233 <= 0)
m.e222 = Constraint(expr= m.x152 - 87.5 * m.b236 <= 0)
m.e223 = Constraint(expr= m.x153 - 88.5 * m.b238 <= 0)
m.e224 = Constraint(expr= m.x154 - 88.5 * m.b240 <= 0)
m.e225 = Constraint(expr= m.x155 - 87 * m.b204 <= 0)
m.e226 = Constraint(expr= m.x156 - 87.5 * m.b207 <= 0)
m.e227 = Constraint(expr= m.x157 - 88.5 * m.b209 <= 0)
m.e228 = Constraint(expr= m.x158 - 88.5 * m.b210 <= 0)
m.e229 = Constraint(expr= m.x159 - 87 * m.b214 <= 0)
m.e230 = Constraint(expr= m.x160 - 87.5 * m.b217 <= 0)
m.e231 = Constraint(expr= m.x161 - 88.5 * m.b219 <= 0)
m.e232 = Constraint(expr= m.x162 - 88.5 * m.b220 <= 0)
m.e233 = Constraint(expr= m.x163 - 87 * m.b224 <= 0)
m.e234 = Constraint(expr= m.x164 - 87.5 * m.b227 <= 0)
m.e235 = Constraint(expr= m.x165 - 88.5 * m.b229 <= 0)
m.e236 = Constraint(expr= m.x166 - 88.5 * m.b230 <= 0)
m.e237 = Constraint(expr= m.x167 - 87 * m.b234 <= 0)
m.e238 = Constraint(expr= m.x168 - 87.5 * m.b237 <= 0)
m.e239 = Constraint(expr= m.x169 - 88.5 * m.b239 <= 0)
m.e240 = Constraint(expr= m.x170 - 88.5 * m.b240 <= 0)
m.e241 = Constraint(expr= m.x11 - m.x27 + 6 * m.b201 <= 0)
m.e242 = Constraint(expr= m.x12 - m.x43 + 4 * m.b202 <= 0)
m.e243 = Constraint(expr= m.x13 - m.x59 + 3.5 * m.b203 <= 0)
m.e244 = Constraint(expr= m.x14 - m.x75 + 7 * m.b204 <= 0)
m.e245 = Constraint(expr= m.x28 - m.x44 + 5 * m.b205 <= 0)
m.e246 = Constraint(expr= m.x29 - m.x60 + 4.5 * m.b206 <= 0)
m.e247 = Constraint(expr= m.x30 - m.x76 + 8 * m.b207 <= 0)
m.e248 = Constraint(expr= m.x45 - m.x61 + 2.5 * m.b208 <= 0)
m.e249 = Constraint(expr= m.x46 - m.x77 + 6 * m.b209 <= 0)
m.e250 = Constraint(expr= m.x62 - m.x78 + 5.5 * m.b210 <= 0)
m.e251 = Constraint(expr= -m.x15 + m.x31 + 6 * m.b211 <= 0)
m.e252 = Constraint(expr= -m.x16 + m.x47 + 4 * m.b212 <= 0)
m.e253 = Constraint(expr= -m.x17 + m.x63 + 3.5 * m.b213 <= 0)
m.e254 = Constraint(expr= -m.x18 + m.x79 + 7 * m.b214 <= 0)
m.e255 = Constraint(expr= -m.x32 + m.x48 + 5 * m.b215 <= 0)
m.e256 = Constraint(expr= -m.x33 + m.x64 + 4.5 * m.b216 <= 0)
m.e257 = Constraint(expr= -m.x34 + m.x80 + 8 * m.b217 <= 0)
m.e258 = Constraint(expr= -m.x49 + m.x65 + 2.5 * m.b218 <= 0)
m.e259 = Constraint(expr= -m.x50 + m.x81 + 6 * m.b219 <= 0)
m.e260 = Constraint(expr= -m.x66 + m.x82 + 5.5 * m.b220 <= 0)
m.e261 = Constraint(expr= m.x99 - m.x115 + 5.5 * m.b221 <= 0)
m.e262 = Constraint(expr= m.x100 - m.x131 + 4.5 * m.b222 <= 0)
m.e263 = Constraint(expr= m.x101 - m.x147 + 4.5 * m.b223 <= 0)
m.e264 = Constraint(expr= m.x102 - m.x163 + 6.5 * m.b224 <= 0)
m.e265 = Constraint(expr= m.x116 - m.x132 + 4 * m.b225 <= 0)
m.e266 = Constraint(expr= m.x117 - m.x148 + 4 * m.b226 <= 0)
m.e267 = Constraint(expr= m.x118 - m.x164 + 6 * m.b227 <= 0)
m.e268 = Constraint(expr= m.x133 - m.x149 + 3 * m.b228 <= 0)
m.e269 = Constraint(expr= m.x134 - m.x165 + 5 * m.b229 <= 0)
m.e270 = Constraint(expr= m.x150 - m.x166 + 5 * m.b230 <= 0)
m.e271 = Constraint(expr= -m.x103 + m.x119 + 5.5 * m.b231 <= 0)
m.e272 = Constraint(expr= -m.x104 + m.x135 + 4.5 * m.b232 <= 0)
m.e273 = Constraint(expr= -m.x105 + m.x151 + 4.5 * m.b233 <= 0)
m.e274 = Constraint(expr= -m.x106 + m.x167 + 6.5 * m.b234 <= 0)
m.e275 = Constraint(expr= -m.x120 + m.x136 + 4 * m.b235 <= 0)
m.e276 = Constraint(expr= -m.x121 + m.x152 + 4 * m.b236 <= 0)
m.e277 = Constraint(expr= -m.x122 + m.x168 + 6 * m.b237 <= 0)
m.e278 = Constraint(expr= -m.x137 + m.x153 + 3 * m.b238 <= 0)
m.e279 = Constraint(expr= -m.x138 + m.x169 + 5 * m.b239 <= 0)
m.e280 = Constraint(expr= -m.x154 + m.x170 + 5 * m.b240 <= 0)
m.e281 = Constraint(expr= m.b201 + m.b211 + m.b221 + m.b231 == 1)
m.e282 = Constraint(expr= m.b202 + m.b212 + m.b222 + m.b232 == 1)
m.e283 = Constraint(expr= m.b203 + m.b213 + m.b223 + m.b233 == 1)
m.e284 = Constraint(expr= m.b204 + m.b214 + m.b224 + m.b234 == 1)
m.e285 = Constraint(expr= m.b205 + m.b215 + m.b225 + m.b235 == 1)
m.e286 = Constraint(expr= m.b206 + m.b216 + m.b226 + m.b236 == 1)
m.e287 = Constraint(expr= m.b207 + m.b217 + m.b227 + m.b237 == 1)
m.e288 = Constraint(expr= m.b208 + m.b218 + m.b228 + m.b238 == 1)
m.e289 = Constraint(expr= m.b209 + m.b219 + m.b229 + m.b239 == 1)
m.e290 = Constraint(expr= m.b210 + m.b220 + m.b230 + m.b240 == 1)
m.e291 = Constraint(expr= m.x1 - m.x171 - m.x176 - m.x181 == 0)
m.e292 = Constraint(expr= m.x2 - m.x172 - m.x177 - m.x182 == 0)
m.e293 = Constraint(expr= m.x3 - m.x173 - m.x178 - m.x183 == 0)
m.e294 = Constraint(expr= m.x4 - m.x174 - m.x179 - m.x184 == 0)
m.e295 = Constraint(expr= m.x5 - m.x175 - m.x180 - m.x185 == 0)
m.e296 = Constraint(expr= m.x6 - m.x186 - m.x191 - m.x196 == 0)
m.e297 = Constraint(expr= m.x7 - m.x187 - m.x192 - m.x197 == 0)
m.e298 = Constraint(expr= m.x8 - m.x188 - m.x193 - m.x198 == 0)
m.e299 = Constraint(expr= m.x9 - m.x189 - m.x194 - m.x199 == 0)
m.e300 = Constraint(expr= m.x10 - m.x190 - m.x195 - m.x200 == 0)
m.e301 = Constraint(expr= m.x171 - 18.5 * m.b241 <= 0)
m.e302 = Constraint(expr= m.x172 - 17.5 * m.b242 <= 0)
m.e303 = Constraint(expr= m.x173 - 19.5 * m.b243 <= 0)
m.e304 = Constraint(expr= m.x174 - 20 * m.b244 <= 0)
m.e305 = Constraint(expr= m.x175 - 16.5 * m.b245 <= 0)
m.e306 = Constraint(expr= m.x176 - 57.5 * m.b246 <= 0)
m.e307 = Constraint(expr= m.x177 - 56.5 * m.b247 <= 0)
m.e308 = Constraint(expr= m.x178 - 58.5 * m.b248 <= 0)
m.e309 = Constraint(expr= m.x179 - 59 * m.b249 <= 0)
m.e310 = Constraint(expr= m.x180 - 55.5 * m.b250 <= 0)
m.e311 = Constraint(expr= m.x181 - 31.5 * m.b251 <= 0)
m.e312 = Constraint(expr= m.x182 - 30.5 * m.b252 <= 0)
m.e313 = Constraint(expr= m.x183 - 32.5 * m.b253 <= 0)
m.e314 = Constraint(expr= m.x184 - 33 * m.b254 <= 0)
m.e315 = Constraint(expr= m.x185 - 29.5 * m.b255 <= 0)
m.e316 = Constraint(expr= m.x186 - 13 * m.b241 <= 0)
m.e317 = Constraint(expr= m.x187 - 13.5 * m.b242 <= 0)
m.e318 = Constraint(expr= m.x188 - 14.5 * m.b243 <= 0)
m.e319 = Constraint(expr= m.x189 - 14.5 * m.b244 <= 0)
m.e320 = Constraint(expr= m.x190 - 12.5 * m.b245 <= 0)
m.e321 = Constraint(expr= m.x191 - 87 * m.b246 <= 0)
m.e322 = Constraint(expr= m.x192 - 87.5 * m.b247 <= 0)
m.e323 = Constraint(expr= m.x193 - 88.5 * m.b248 <= 0)
m.e324 = Constraint(expr= m.x194 - 88.5 * m.b249 <= 0)
m.e325 = Constraint(expr= m.x195 - 86.5 * m.b250 <= 0)
m.e326 = Constraint(expr= m.x196 - 51 * m.b251 <= 0)
m.e327 = Constraint(expr= m.x197 - 51.5 * m.b252 <= 0)
m.e328 = Constraint(expr= m.x198 - 52.5 * m.b253 <= 0)
m.e329 = Constraint(expr= m.x199 - 52.5 * m.b254 <= 0)
m.e330 = Constraint(expr= m.x200 - 50.5 * m.b255 <= 0)
m.e331 = Constraint(expr= ((m.x171 / (0.001 + 0.999 * m.b241))**2 - (35 *
    m.x171) / (0.001 + 0.999 * m.b241) + (m.x186 / (0.001 + 0.999 * m.b241))**2
    - (14 * m.x186) / (0.001 + 0.999 * m.b241)) * (0.001 + 0.999 * m.b241) +
    306.25 * m.b241 + 49 * m.b241 - 36 * m.b241 <= 0)
m.e332 = Constraint(expr= ((m.x172 / (0.001 + 0.999 * m.b242))**2 - (37 *
    m.x172) / (0.001 + 0.999 * m.b242) + (m.x187 / (0.001 + 0.999 * m.b242))**2
    - (15 * m.x187) / (0.001 + 0.999 * m.b242)) * (0.001 + 0.999 * m.b242) +
    342.25 * m.b242 + 56.25 * m.b242 - 36 * m.b242 <= 0)
m.e333 = Constraint(expr= ((m.x173 / (0.001 + 0.999 * m.b243))**2 - (33 *
    m.x173) / (0.001 + 0.999 * m.b243) + (m.x188 / (0.001 + 0.999 * m.b243))**2
    - (17 * m.x188) / (0.001 + 0.999 * m.b243)) * (0.001 + 0.999 * m.b243) +
    272.25 * m.b243 + 72.25 * m.b243 - 36 * m.b243 <= 0)
m.e334 = Constraint(expr= ((m.x174 / (0.001 + 0.999 * m.b244))**2 - (32 *
    m.x174) / (0.001 + 0.999 * m.b244) + (m.x189 / (0.001 + 0.999 * m.b244))**2
    - (17 * m.x189) / (0.001 + 0.999 * m.b244)) * (0.001 + 0.999 * m.b244) +
    256 * m.b244 + 72.25 * m.b244 - 36 * m.b244 <= 0)
m.e335 = Constraint(expr= ((m.x175 / (0.001 + 0.999 * m.b245))**2 - (39 *
    m.x175) / (0.001 + 0.999 * m.b245) + (m.x190 / (0.001 + 0.999 * m.b245))**2
    - (13 * m.x190) / (0.001 + 0.999 * m.b245)) * (0.001 + 0.999 * m.b245) +
    380.25 * m.b245 + 42.25 * m.b245 - 36 * m.b245 <= 0)
m.e336 = Constraint(expr= ((m.x176 / (0.001 + 0.999 * m.b246))**2 - (105 *
    m.x176) / (0.001 + 0.999 * m.b246) + (m.x191 / (0.001 + 0.999 * m.b246))**2
    - (154 * m.x191) / (0.001 + 0.999 * m.b246)) * (0.001 + 0.999 * m.b246) +
    2756.25 * m.b246 + 5929 * m.b246 - 100 * m.b246 <= 0)
m.e337 = Constraint(expr= ((m.x177 / (0.001 + 0.999 * m.b247))**2 - (107 *
    m.x177) / (0.001 + 0.999 * m.b247) + (m.x192 / (0.001 + 0.999 * m.b247))**2
    - (155 * m.x192) / (0.001 + 0.999 * m.b247)) * (0.001 + 0.999 * m.b247) +
    2862.25 * m.b247 + 6006.25 * m.b247 - 100 * m.b247 <= 0)
m.e338 = Constraint(expr= ((m.x178 / (0.001 + 0.999 * m.b248))**2 - (103 *
    m.x178) / (0.001 + 0.999 * m.b248) + (m.x193 / (0.001 + 0.999 * m.b248))**2
    - (157 * m.x193) / (0.001 + 0.999 * m.b248)) * (0.001 + 0.999 * m.b248) +
    2652.25 * m.b248 + 6162.25 * m.b248 - 100 * m.b248 <= 0)
m.e339 = Constraint(expr= ((m.x179 / (0.001 + 0.999 * m.b249))**2 - (102 *
    m.x179) / (0.001 + 0.999 * m.b249) + (m.x194 / (0.001 + 0.999 * m.b249))**2
    - (157 * m.x194) / (0.001 + 0.999 * m.b249)) * (0.001 + 0.999 * m.b249) +
    2601 * m.b249 + 6162.25 * m.b249 - 100 * m.b249 <= 0)
m.e340 = Constraint(expr= ((m.x180 / (0.001 + 0.999 * m.b250))**2 - (109 *
    m.x180) / (0.001 + 0.999 * m.b250) + (m.x195 / (0.001 + 0.999 * m.b250))**2
    - (153 * m.x195) / (0.001 + 0.999 * m.b250)) * (0.001 + 0.999 * m.b250) +
    2970.25 * m.b250 + 5852.25 * m.b250 - 100 * m.b250 <= 0)
m.e341 = Constraint(expr= ((m.x181 / (0.001 + 0.999 * m.b251))**2 - (65 *
    m.x181) / (0.001 + 0.999 * m.b251) + (m.x196 / (0.001 + 0.999 * m.b251))**2
    - (94 * m.x196) / (0.001 + 0.999 * m.b251)) * (0.001 + 0.999 * m.b251) +
    1056.25 * m.b251 + 2209 * m.b251 - 16 * m.b251 <= 0)
m.e342 = Constraint(expr= ((m.x182 / (0.001 + 0.999 * m.b252))**2 - (67 *
    m.x182) / (0.001 + 0.999 * m.b252) + (m.x197 / (0.001 + 0.999 * m.b252))**2
    - (95 * m.x197) / (0.001 + 0.999 * m.b252)) * (0.001 + 0.999 * m.b252) +
    1122.25 * m.b252 + 2256.25 * m.b252 - 16 * m.b252 <= 0)
m.e343 = Constraint(expr= ((m.x183 / (0.001 + 0.999 * m.b253))**2 - (63 *
    m.x183) / (0.001 + 0.999 * m.b253) + (m.x198 / (0.001 + 0.999 * m.b253))**2
    - (97 * m.x198) / (0.001 + 0.999 * m.b253)) * (0.001 + 0.999 * m.b253) +
    992.25 * m.b253 + 2352.25 * m.b253 - 16 * m.b253 <= 0)
m.e344 = Constraint(expr= ((m.x184 / (0.001 + 0.999 * m.b254))**2 - (62 *
    m.x184) / (0.001 + 0.999 * m.b254) + (m.x199 / (0.001 + 0.999 * m.b254))**2
    - (97 * m.x199) / (0.001 + 0.999 * m.b254)) * (0.001 + 0.999 * m.b254) +
    961 * m.b254 + 2352.25 * m.b254 - 16 * m.b254 <= 0)
m.e345 = Constraint(expr= ((m.x185 / (0.001 + 0.999 * m.b255))**2 - (69 *
    m.x185) / (0.001 + 0.999 * m.b255) + (m.x200 / (0.001 + 0.999 * m.b255))**2
    - (93 * m.x200) / (0.001 + 0.999 * m.b255)) * (0.001 + 0.999 * m.b255) +
    1190.25 * m.b255 + 2162.25 * m.b255 - 16 * m.b255 <= 0)
m.e346 = Constraint(expr= ((m.x171 / (0.001 + 0.999 * m.b241))**2 - (35 *
    m.x171) / (0.001 + 0.999 * m.b241) + (m.x186 / (0.001 + 0.999 * m.b241))**2
    - (26 * m.x186) / (0.001 + 0.999 * m.b241)) * (0.001 + 0.999 * m.b241) +
    306.25 * m.b241 + 169 * m.b241 - 36 * m.b241 <= 0)
m.e347 = Constraint(expr= ((m.x172 / (0.001 + 0.999 * m.b242))**2 - (37 *
    m.x172) / (0.001 + 0.999 * m.b242) + (m.x187 / (0.001 + 0.999 * m.b242))**2
    - (25 * m.x187) / (0.001 + 0.999 * m.b242)) * (0.001 + 0.999 * m.b242) +
    342.25 * m.b242 + 156.25 * m.b242 - 36 * m.b242 <= 0)
m.e348 = Constraint(expr= ((m.x173 / (0.001 + 0.999 * m.b243))**2 - (33 *
    m.x173) / (0.001 + 0.999 * m.b243) + (m.x188 / (0.001 + 0.999 * m.b243))**2
    - (23 * m.x188) / (0.001 + 0.999 * m.b243)) * (0.001 + 0.999 * m.b243) +
    272.25 * m.b243 + 132.25 * m.b243 - 36 * m.b243 <= 0)
m.e349 = Constraint(expr= ((m.x174 / (0.001 + 0.999 * m.b244))**2 - (32 *
    m.x174) / (0.001 + 0.999 * m.b244) + (m.x189 / (0.001 + 0.999 * m.b244))**2
    - (23 * m.x189) / (0.001 + 0.999 * m.b244)) * (0.001 + 0.999 * m.b244) +
    256 * m.b244 + 132.25 * m.b244 - 36 * m.b244 <= 0)
m.e350 = Constraint(expr= ((m.x175 / (0.001 + 0.999 * m.b245))**2 - (39 *
    m.x175) / (0.001 + 0.999 * m.b245) + (m.x190 / (0.001 + 0.999 * m.b245))**2
    - (27 * m.x190) / (0.001 + 0.999 * m.b245)) * (0.001 + 0.999 * m.b245) +
    380.25 * m.b245 + 182.25 * m.b245 - 36 * m.b245 <= 0)
m.e351 = Constraint(expr= ((m.x176 / (0.001 + 0.999 * m.b246))**2 - (105 *
    m.x176) / (0.001 + 0.999 * m.b246) + (m.x191 / (0.001 + 0.999 * m.b246))**2
    - (166 * m.x191) / (0.001 + 0.999 * m.b246)) * (0.001 + 0.999 * m.b246) +
    2756.25 * m.b246 + 6889 * m.b246 - 100 * m.b246 <= 0)
m.e352 = Constraint(expr= ((m.x177 / (0.001 + 0.999 * m.b247))**2 - (107 *
    m.x177) / (0.001 + 0.999 * m.b247) + (m.x192 / (0.001 + 0.999 * m.b247))**2
    - (165 * m.x192) / (0.001 + 0.999 * m.b247)) * (0.001 + 0.999 * m.b247) +
    2862.25 * m.b247 + 6806.25 * m.b247 - 100 * m.b247 <= 0)
m.e353 = Constraint(expr= ((m.x178 / (0.001 + 0.999 * m.b248))**2 - (103 *
    m.x178) / (0.001 + 0.999 * m.b248) + (m.x193 / (0.001 + 0.999 * m.b248))**2
    - (163 * m.x193) / (0.001 + 0.999 * m.b248)) * (0.001 + 0.999 * m.b248) +
    2652.25 * m.b248 + 6642.25 * m.b248 - 100 * m.b248 <= 0)
m.e354 = Constraint(expr= ((m.x179 / (0.001 + 0.999 * m.b249))**2 - (102 *
    m.x179) / (0.001 + 0.999 * m.b249) + (m.x194 / (0.001 + 0.999 * m.b249))**2
    - (163 * m.x194) / (0.001 + 0.999 * m.b249)) * (0.001 + 0.999 * m.b249) +
    2601 * m.b249 + 6642.25 * m.b249 - 100 * m.b249 <= 0)
m.e355 = Constraint(expr= ((m.x180 / (0.001 + 0.999 * m.b250))**2 - (109 *
    m.x180) / (0.001 + 0.999 * m.b250) + (m.x195 / (0.001 + 0.999 * m.b250))**2
    - (167 * m.x195) / (0.001 + 0.999 * m.b250)) * (0.001 + 0.999 * m.b250) +
    2970.25 * m.b250 + 6972.25 * m.b250 - 100 * m.b250 <= 0)
m.e356 = Constraint(expr= ((m.x181 / (0.001 + 0.999 * m.b251))**2 - (65 *
    m.x181) / (0.001 + 0.999 * m.b251) + (m.x196 / (0.001 + 0.999 * m.b251))**2
    - (106 * m.x196) / (0.001 + 0.999 * m.b251)) * (0.001 + 0.999 * m.b251) +
    1056.25 * m.b251 + 2809 * m.b251 - 16 * m.b251 <= 0)
m.e357 = Constraint(expr= ((m.x182 / (0.001 + 0.999 * m.b252))**2 - (67 *
    m.x182) / (0.001 + 0.999 * m.b252) + (m.x197 / (0.001 + 0.999 * m.b252))**2
    - (105 * m.x197) / (0.001 + 0.999 * m.b252)) * (0.001 + 0.999 * m.b252) +
    1122.25 * m.b252 + 2756.25 * m.b252 - 16 * m.b252 <= 0)
m.e358 = Constraint(expr= ((m.x183 / (0.001 + 0.999 * m.b253))**2 - (63 *
    m.x183) / (0.001 + 0.999 * m.b253) + (m.x198 / (0.001 + 0.999 * m.b253))**2
    - (103 * m.x198) / (0.001 + 0.999 * m.b253)) * (0.001 + 0.999 * m.b253) +
    992.25 * m.b253 + 2652.25 * m.b253 - 16 * m.b253 <= 0)
m.e359 = Constraint(expr= ((m.x184 / (0.001 + 0.999 * m.b254))**2 - (62 *
    m.x184) / (0.001 + 0.999 * m.b254) + (m.x199 / (0.001 + 0.999 * m.b254))**2
    - (103 * m.x199) / (0.001 + 0.999 * m.b254)) * (0.001 + 0.999 * m.b254) +
    961 * m.b254 + 2652.25 * m.b254 - 16 * m.b254 <= 0)
m.e360 = Constraint(expr= ((m.x185 / (0.001 + 0.999 * m.b255))**2 - (69 *
    m.x185) / (0.001 + 0.999 * m.b255) + (m.x200 / (0.001 + 0.999 * m.b255))**2
    - (107 * m.x200) / (0.001 + 0.999 * m.b255)) * (0.001 + 0.999 * m.b255) +
    1190.25 * m.b255 + 2862.25 * m.b255 - 16 * m.b255 <= 0)
m.e361 = Constraint(expr= ((m.x171 / (0.001 + 0.999 * m.b241))**2 - (25 *
    m.x171) / (0.001 + 0.999 * m.b241) + (m.x186 / (0.001 + 0.999 * m.b241))**2
    - (14 * m.x186) / (0.001 + 0.999 * m.b241)) * (0.001 + 0.999 * m.b241) +
    156.25 * m.b241 + 49 * m.b241 - 36 * m.b241 <= 0)
m.e362 = Constraint(expr= ((m.x172 / (0.001 + 0.999 * m.b242))**2 - (23 *
    m.x172) / (0.001 + 0.999 * m.b242) + (m.x187 / (0.001 + 0.999 * m.b242))**2
    - (15 * m.x187) / (0.001 + 0.999 * m.b242)) * (0.001 + 0.999 * m.b242) +
    132.25 * m.b242 + 56.25 * m.b242 - 36 * m.b242 <= 0)
m.e363 = Constraint(expr= ((m.x173 / (0.001 + 0.999 * m.b243))**2 - (27 *
    m.x173) / (0.001 + 0.999 * m.b243) + (m.x188 / (0.001 + 0.999 * m.b243))**2
    - (17 * m.x188) / (0.001 + 0.999 * m.b243)) * (0.001 + 0.999 * m.b243) +
    182.25 * m.b243 + 72.25 * m.b243 - 36 * m.b243 <= 0)
m.e364 = Constraint(expr= ((m.x174 / (0.001 + 0.999 * m.b244))**2 - (28 *
    m.x174) / (0.001 + 0.999 * m.b244) + (m.x189 / (0.001 + 0.999 * m.b244))**2
    - (17 * m.x189) / (0.001 + 0.999 * m.b244)) * (0.001 + 0.999 * m.b244) +
    196 * m.b244 + 72.25 * m.b244 - 36 * m.b244 <= 0)
m.e365 = Constraint(expr= ((m.x175 / (0.001 + 0.999 * m.b245))**2 - (21 *
    m.x175) / (0.001 + 0.999 * m.b245) + (m.x190 / (0.001 + 0.999 * m.b245))**2
    - (13 * m.x190) / (0.001 + 0.999 * m.b245)) * (0.001 + 0.999 * m.b245) +
    110.25 * m.b245 + 42.25 * m.b245 - 36 * m.b245 <= 0)
m.e366 = Constraint(expr= ((m.x176 / (0.001 + 0.999 * m.b246))**2 - (95 *
    m.x176) / (0.001 + 0.999 * m.b246) + (m.x191 / (0.001 + 0.999 * m.b246))**2
    - (154 * m.x191) / (0.001 + 0.999 * m.b246)) * (0.001 + 0.999 * m.b246) +
    2256.25 * m.b246 + 5929 * m.b246 - 100 * m.b246 <= 0)
m.e367 = Constraint(expr= ((m.x177 / (0.001 + 0.999 * m.b247))**2 - (93 *
    m.x177) / (0.001 + 0.999 * m.b247) + (m.x192 / (0.001 + 0.999 * m.b247))**2
    - (155 * m.x192) / (0.001 + 0.999 * m.b247)) * (0.001 + 0.999 * m.b247) +
    2162.25 * m.b247 + 6006.25 * m.b247 - 100 * m.b247 <= 0)
m.e368 = Constraint(expr= ((m.x178 / (0.001 + 0.999 * m.b248))**2 - (97 *
    m.x178) / (0.001 + 0.999 * m.b248) + (m.x193 / (0.001 + 0.999 * m.b248))**2
    - (157 * m.x193) / (0.001 + 0.999 * m.b248)) * (0.001 + 0.999 * m.b248) +
    2352.25 * m.b248 + 6162.25 * m.b248 - 100 * m.b248 <= 0)
m.e369 = Constraint(expr= ((m.x179 / (0.001 + 0.999 * m.b249))**2 - (98 *
    m.x179) / (0.001 + 0.999 * m.b249) + (m.x194 / (0.001 + 0.999 * m.b249))**2
    - (157 * m.x194) / (0.001 + 0.999 * m.b249)) * (0.001 + 0.999 * m.b249) +
    2401 * m.b249 + 6162.25 * m.b249 - 100 * m.b249 <= 0)
m.e370 = Constraint(expr= ((m.x180 / (0.001 + 0.999 * m.b250))**2 - (91 *
    m.x180) / (0.001 + 0.999 * m.b250) + (m.x195 / (0.001 + 0.999 * m.b250))**2
    - (153 * m.x195) / (0.001 + 0.999 * m.b250)) * (0.001 + 0.999 * m.b250) +
    2070.25 * m.b250 + 5852.25 * m.b250 - 100 * m.b250 <= 0)
m.e371 = Constraint(expr= ((m.x181 / (0.001 + 0.999 * m.b251))**2 - (55 *
    m.x181) / (0.001 + 0.999 * m.b251) + (m.x196 / (0.001 + 0.999 * m.b251))**2
    - (94 * m.x196) / (0.001 + 0.999 * m.b251)) * (0.001 + 0.999 * m.b251) +
    756.25 * m.b251 + 2209 * m.b251 - 16 * m.b251 <= 0)
m.e372 = Constraint(expr= ((m.x182 / (0.001 + 0.999 * m.b252))**2 - (53 *
    m.x182) / (0.001 + 0.999 * m.b252) + (m.x197 / (0.001 + 0.999 * m.b252))**2
    - (95 * m.x197) / (0.001 + 0.999 * m.b252)) * (0.001 + 0.999 * m.b252) +
    702.25 * m.b252 + 2256.25 * m.b252 - 16 * m.b252 <= 0)
m.e373 = Constraint(expr= ((m.x183 / (0.001 + 0.999 * m.b253))**2 - (57 *
    m.x183) / (0.001 + 0.999 * m.b253) + (m.x198 / (0.001 + 0.999 * m.b253))**2
    - (97 * m.x198) / (0.001 + 0.999 * m.b253)) * (0.001 + 0.999 * m.b253) +
    812.25 * m.b253 + 2352.25 * m.b253 - 16 * m.b253 <= 0)
m.e374 = Constraint(expr= ((m.x184 / (0.001 + 0.999 * m.b254))**2 - (58 *
    m.x184) / (0.001 + 0.999 * m.b254) + (m.x199 / (0.001 + 0.999 * m.b254))**2
    - (97 * m.x199) / (0.001 + 0.999 * m.b254)) * (0.001 + 0.999 * m.b254) +
    841 * m.b254 + 2352.25 * m.b254 - 16 * m.b254 <= 0)
m.e375 = Constraint(expr= ((m.x185 / (0.001 + 0.999 * m.b255))**2 - (51 *
    m.x185) / (0.001 + 0.999 * m.b255) + (m.x200 / (0.001 + 0.999 * m.b255))**2
    - (93 * m.x200) / (0.001 + 0.999 * m.b255)) * (0.001 + 0.999 * m.b255) +
    650.25 * m.b255 + 2162.25 * m.b255 - 16 * m.b255 <= 0)
m.e376 = Constraint(expr= ((m.x171 / (0.001 + 0.999 * m.b241))**2 - (25 *
    m.x171) / (0.001 + 0.999 * m.b241) + (m.x186 / (0.001 + 0.999 * m.b241))**2
    - (26 * m.x186) / (0.001 + 0.999 * m.b241)) * (0.001 + 0.999 * m.b241) +
    156.25 * m.b241 + 169 * m.b241 - 36 * m.b241 <= 0)
m.e377 = Constraint(expr= ((m.x172 / (0.001 + 0.999 * m.b242))**2 - (23 *
    m.x172) / (0.001 + 0.999 * m.b242) + (m.x187 / (0.001 + 0.999 * m.b242))**2
    - (25 * m.x187) / (0.001 + 0.999 * m.b242)) * (0.001 + 0.999 * m.b242) +
    132.25 * m.b242 + 156.25 * m.b242 - 36 * m.b242 <= 0)
m.e378 = Constraint(expr= ((m.x173 / (0.001 + 0.999 * m.b243))**2 - (27 *
    m.x173) / (0.001 + 0.999 * m.b243) + (m.x188 / (0.001 + 0.999 * m.b243))**2
    - (23 * m.x188) / (0.001 + 0.999 * m.b243)) * (0.001 + 0.999 * m.b243) +
    182.25 * m.b243 + 132.25 * m.b243 - 36 * m.b243 <= 0)
m.e379 = Constraint(expr= ((m.x174 / (0.001 + 0.999 * m.b244))**2 - (28 *
    m.x174) / (0.001 + 0.999 * m.b244) + (m.x189 / (0.001 + 0.999 * m.b244))**2
    - (23 * m.x189) / (0.001 + 0.999 * m.b244)) * (0.001 + 0.999 * m.b244) +
    196 * m.b244 + 132.25 * m.b244 - 36 * m.b244 <= 0)
m.e380 = Constraint(expr= ((m.x175 / (0.001 + 0.999 * m.b245))**2 - (21 *
    m.x175) / (0.001 + 0.999 * m.b245) + (m.x190 / (0.001 + 0.999 * m.b245))**2
    - (27 * m.x190) / (0.001 + 0.999 * m.b245)) * (0.001 + 0.999 * m.b245) +
    110.25 * m.b245 + 182.25 * m.b245 - 36 * m.b245 <= 0)
m.e381 = Constraint(expr= ((m.x176 / (0.001 + 0.999 * m.b246))**2 - (95 *
    m.x176) / (0.001 + 0.999 * m.b246) + (m.x191 / (0.001 + 0.999 * m.b246))**2
    - (166 * m.x191) / (0.001 + 0.999 * m.b246)) * (0.001 + 0.999 * m.b246) +
    2256.25 * m.b246 + 6889 * m.b246 - 100 * m.b246 <= 0)
m.e382 = Constraint(expr= ((m.x177 / (0.001 + 0.999 * m.b247))**2 - (93 *
    m.x177) / (0.001 + 0.999 * m.b247) + (m.x192 / (0.001 + 0.999 * m.b247))**2
    - (165 * m.x192) / (0.001 + 0.999 * m.b247)) * (0.001 + 0.999 * m.b247) +
    2162.25 * m.b247 + 6806.25 * m.b247 - 100 * m.b247 <= 0)
m.e383 = Constraint(expr= ((m.x178 / (0.001 + 0.999 * m.b248))**2 - (97 *
    m.x178) / (0.001 + 0.999 * m.b248) + (m.x193 / (0.001 + 0.999 * m.b248))**2
    - (163 * m.x193) / (0.001 + 0.999 * m.b248)) * (0.001 + 0.999 * m.b248) +
    2352.25 * m.b248 + 6642.25 * m.b248 - 100 * m.b248 <= 0)
m.e384 = Constraint(expr= ((m.x179 / (0.001 + 0.999 * m.b249))**2 - (98 *
    m.x179) / (0.001 + 0.999 * m.b249) + (m.x194 / (0.001 + 0.999 * m.b249))**2
    - (163 * m.x194) / (0.001 + 0.999 * m.b249)) * (0.001 + 0.999 * m.b249) +
    2401 * m.b249 + 6642.25 * m.b249 - 100 * m.b249 <= 0)
m.e385 = Constraint(expr= ((m.x180 / (0.001 + 0.999 * m.b250))**2 - (91 *
    m.x180) / (0.001 + 0.999 * m.b250) + (m.x195 / (0.001 + 0.999 * m.b250))**2
    - (167 * m.x195) / (0.001 + 0.999 * m.b250)) * (0.001 + 0.999 * m.b250) +
    2070.25 * m.b250 + 6972.25 * m.b250 - 100 * m.b250 <= 0)
m.e386 = Constraint(expr= ((m.x181 / (0.001 + 0.999 * m.b251))**2 - (55 *
    m.x181) / (0.001 + 0.999 * m.b251) + (m.x196 / (0.001 + 0.999 * m.b251))**2
    - (106 * m.x196) / (0.001 + 0.999 * m.b251)) * (0.001 + 0.999 * m.b251) +
    756.25 * m.b251 + 2809 * m.b251 - 16 * m.b251 <= 0)
m.e387 = Constraint(expr= ((m.x182 / (0.001 + 0.999 * m.b252))**2 - (53 *
    m.x182) / (0.001 + 0.999 * m.b252) + (m.x197 / (0.001 + 0.999 * m.b252))**2
    - (105 * m.x197) / (0.001 + 0.999 * m.b252)) * (0.001 + 0.999 * m.b252) +
    702.25 * m.b252 + 2756.25 * m.b252 - 16 * m.b252 <= 0)
m.e388 = Constraint(expr= ((m.x183 / (0.001 + 0.999 * m.b253))**2 - (57 *
    m.x183) / (0.001 + 0.999 * m.b253) + (m.x198 / (0.001 + 0.999 * m.b253))**2
    - (103 * m.x198) / (0.001 + 0.999 * m.b253)) * (0.001 + 0.999 * m.b253) +
    812.25 * m.b253 + 2652.25 * m.b253 - 16 * m.b253 <= 0)
m.e389 = Constraint(expr= ((m.x184 / (0.001 + 0.999 * m.b254))**2 - (58 *
    m.x184) / (0.001 + 0.999 * m.b254) + (m.x199 / (0.001 + 0.999 * m.b254))**2
    - (103 * m.x199) / (0.001 + 0.999 * m.b254)) * (0.001 + 0.999 * m.b254) +
    841 * m.b254 + 2652.25 * m.b254 - 16 * m.b254 <= 0)
m.e390 = Constraint(expr= ((m.x185 / (0.001 + 0.999 * m.b255))**2 - (51 *
    m.x185) / (0.001 + 0.999 * m.b255) + (m.x200 / (0.001 + 0.999 * m.b255))**2
    - (107 * m.x200) / (0.001 + 0.999 * m.b255)) * (0.001 + 0.999 * m.b255) +
    650.25 * m.b255 + 2862.25 * m.b255 - 16 * m.b255 <= 0)
m.e391 = Constraint(expr= m.b241 + m.b246 + m.b251 == 1)
m.e392 = Constraint(expr= m.b242 + m.b247 + m.b252 == 1)
m.e393 = Constraint(expr= m.b243 + m.b248 + m.b253 == 1)
m.e394 = Constraint(expr= m.b244 + m.b249 + m.b254 == 1)
m.e395 = Constraint(expr= m.b245 + m.b250 + m.b255 == 1)
