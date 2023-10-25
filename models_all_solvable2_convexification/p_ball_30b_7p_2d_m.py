# MINLP written by GAMS Convert at 05/07/21 17:13:01
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       337        7        0      330        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       266       56      210        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      1314      894      420
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
m.b30 = Var(within=Binary, bounds=(0,1), initialize=1)
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
m.b52 = Var(within=Binary, bounds=(0,1), initialize=1)
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
m.b76 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b77 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b78 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b79 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b80 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b81 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b82 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b83 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b84 = Var(within=Binary, bounds=(0,1), initialize=1)
m.b85 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b86 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b87 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b88 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b89 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b90 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b91 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b92 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b93 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b94 = Var(within=Binary, bounds=(0,1), initialize=1)
m.b95 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b96 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b97 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b98 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b99 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b100 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b101 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b102 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b103 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b104 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b105 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b106 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b107 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b108 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b109 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b110 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b111 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b112 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b113 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b114 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b115 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b116 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b117 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b118 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b119 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b120 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b121 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b122 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b123 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b124 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b125 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b126 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b127 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b128 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b129 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b130 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b131 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b132 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b133 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b134 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b135 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b136 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b137 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b138 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b139 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b140 = Var(within=Binary, bounds=(0,1), initialize=1)
m.b141 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b142 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b143 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b144 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b145 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b146 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b147 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b148 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b149 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b150 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b151 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b152 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b153 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b154 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b155 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b156 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b157 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b158 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b159 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b160 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b161 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b162 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b163 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b164 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b165 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b166 = Var(within=Binary, bounds=(0,1), initialize=1)
m.b167 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b168 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b169 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b170 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b171 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b172 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b173 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b174 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b175 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b176 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b177 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b178 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b179 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b180 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b181 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b182 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b183 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b184 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b185 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b186 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b187 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b188 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b189 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b190 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b191 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b192 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b193 = Var(within=Binary, bounds=(0,1), initialize=1)
m.b194 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b195 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b196 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b197 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b198 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b199 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b200 = Var(within=Binary, bounds=(0,1), initialize=0)
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
m.x211 = Var(within=Reals, bounds=(0,10), initialize=7.55187424652185)
m.x212 = Var(within=Reals, bounds=(0,10), initialize=8.6263106159384)
m.x213 = Var(within=Reals, bounds=(0,10), initialize=1.07443636941655)
m.x214 = Var(within=Reals, bounds=(0,10), initialize=3.96699202270076)
m.x215 = Var(within=Reals, bounds=(0,10), initialize=3.96699202270076)
m.x216 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x217 = Var(within=Reals, bounds=(0,10), initialize=8.6263106159384)
m.x218 = Var(within=Reals, bounds=(0,10), initialize=1.07443636941655)
m.x219 = Var(within=Reals, bounds=(0,10), initialize=2.74682490676783)
m.x220 = Var(within=Reals, bounds=(0,10), initialize=1.22016711593293)
m.x221 = Var(within=Reals, bounds=(0,10), initialize=8.6263106159384)
m.x222 = Var(within=Reals, bounds=(0,10), initialize=1.07443636941655)
m.x223 = Var(within=Reals, bounds=(0,10), initialize=3.96699202270076)
m.x224 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x225 = Var(within=Reals, bounds=(0,10), initialize=8.6263106159384)
m.x226 = Var(within=Reals, bounds=(0,10), initialize=1.07443636941655)
m.x227 = Var(within=Reals, bounds=(0,10), initialize=3.96699202270076)
m.x228 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x229 = Var(within=Reals, bounds=(0,10), initialize=8.6263106159384)
m.x230 = Var(within=Reals, bounds=(0,10), initialize=1.07443636941655)
m.x231 = Var(within=Reals, bounds=(0,10), initialize=3.96699202270076)
m.x232 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x233 = Var(within=Reals, bounds=(0,10), initialize=8.65390008276914)
m.x234 = Var(within=Reals, bounds=(0,10), initialize=1.10202583624729)
m.x235 = Var(within=Reals, bounds=(0,10), initialize=3.96699202270076)
m.x236 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x237 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x238 = Var(within=Reals, bounds=(0,10), initialize=1.22016711593293)
m.x239 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x240 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x241 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x242 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x243 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x244 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x245 = Var(within=Reals, bounds=(0,10), initialize=0.0275894668307384)
m.x246 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x247 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x248 = Var(within=Reals, bounds=(0,10), initialize=1.22016711593293)
m.x249 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x250 = Var(within=Reals, bounds=(0,10), initialize=1.22016711593293)
m.x251 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x252 = Var(within=Reals, bounds=(0,10), initialize=1.22016711593293)
m.x253 = Var(within=Reals, bounds=(0,10), initialize=0.0275894668307384)
m.x254 = Var(within=Reals, bounds=(0,10), initialize=1.22016711593293)
m.x255 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x256 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x257 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x258 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x259 = Var(within=Reals, bounds=(0,10), initialize=0.0275894668307384)
m.x260 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x261 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x262 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x263 = Var(within=Reals, bounds=(0,10), initialize=0.0275894668307384)
m.x264 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x265 = Var(within=Reals, bounds=(0,10), initialize=0.0275894668307384)
m.x266 = Var(within=Reals, bounds=(0,10), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x213 + m.x216 + m.x218 + m.x220 +
    m.x222 + m.x224 + m.x226 + m.x228 + m.x230 + m.x232 + m.x234 + m.x236 +
    m.x237 + m.x238 + m.x239 + m.x240 + m.x241 + m.x242 + m.x243 + m.x244 +
    m.x245 + m.x246 + m.x247 + m.x248 + m.x249 + m.x250 + m.x251 + m.x252 +
    m.x253 + m.x254 + m.x255 + m.x256 + m.x257 + m.x258 + m.x259 + m.x260 +
    m.x261 + m.x262 + m.x263 + m.x264 + m.x265 + m.x266)

m.e1 = Constraint(expr= m.x211 - m.x212 - m.x213 <= 0)
m.e2 = Constraint(expr= -m.x211 + m.x212 - m.x213 <= 0)
m.e3 = Constraint(expr= m.x214 - m.x215 - m.x216 <= 0)
m.e4 = Constraint(expr= -m.x214 + m.x215 - m.x216 <= 0)
m.e5 = Constraint(expr= m.x211 - m.x217 - m.x218 <= 0)
m.e6 = Constraint(expr= -m.x211 + m.x217 - m.x218 <= 0)
m.e7 = Constraint(expr= m.x214 - m.x219 - m.x220 <= 0)
m.e8 = Constraint(expr= -m.x214 + m.x219 - m.x220 <= 0)
m.e9 = Constraint(expr= m.x211 - m.x221 - m.x222 <= 0)
m.e10 = Constraint(expr= -m.x211 + m.x221 - m.x222 <= 0)
m.e11 = Constraint(expr= m.x214 - m.x223 - m.x224 <= 0)
m.e12 = Constraint(expr= -m.x214 + m.x223 - m.x224 <= 0)
m.e13 = Constraint(expr= m.x211 - m.x225 - m.x226 <= 0)
m.e14 = Constraint(expr= -m.x211 + m.x225 - m.x226 <= 0)
m.e15 = Constraint(expr= m.x214 - m.x227 - m.x228 <= 0)
m.e16 = Constraint(expr= -m.x214 + m.x227 - m.x228 <= 0)
m.e17 = Constraint(expr= m.x211 - m.x229 - m.x230 <= 0)
m.e18 = Constraint(expr= -m.x211 + m.x229 - m.x230 <= 0)
m.e19 = Constraint(expr= m.x214 - m.x231 - m.x232 <= 0)
m.e20 = Constraint(expr= -m.x214 + m.x231 - m.x232 <= 0)
m.e21 = Constraint(expr= m.x211 - m.x233 - m.x234 <= 0)
m.e22 = Constraint(expr= -m.x211 + m.x233 - m.x234 <= 0)
m.e23 = Constraint(expr= m.x214 - m.x235 - m.x236 <= 0)
m.e24 = Constraint(expr= -m.x214 + m.x235 - m.x236 <= 0)
m.e25 = Constraint(expr= m.x212 - m.x217 - m.x237 <= 0)
m.e26 = Constraint(expr= -m.x212 + m.x217 - m.x237 <= 0)
m.e27 = Constraint(expr= m.x215 - m.x219 - m.x238 <= 0)
m.e28 = Constraint(expr= -m.x215 + m.x219 - m.x238 <= 0)
m.e29 = Constraint(expr= m.x212 - m.x221 - m.x239 <= 0)
m.e30 = Constraint(expr= -m.x212 + m.x221 - m.x239 <= 0)
m.e31 = Constraint(expr= m.x215 - m.x223 - m.x240 <= 0)
m.e32 = Constraint(expr= -m.x215 + m.x223 - m.x240 <= 0)
m.e33 = Constraint(expr= m.x212 - m.x225 - m.x241 <= 0)
m.e34 = Constraint(expr= -m.x212 + m.x225 - m.x241 <= 0)
m.e35 = Constraint(expr= m.x215 - m.x227 - m.x242 <= 0)
m.e36 = Constraint(expr= -m.x215 + m.x227 - m.x242 <= 0)
m.e37 = Constraint(expr= m.x212 - m.x229 - m.x243 <= 0)
m.e38 = Constraint(expr= -m.x212 + m.x229 - m.x243 <= 0)
m.e39 = Constraint(expr= m.x215 - m.x231 - m.x244 <= 0)
m.e40 = Constraint(expr= -m.x215 + m.x231 - m.x244 <= 0)
m.e41 = Constraint(expr= m.x212 - m.x233 - m.x245 <= 0)
m.e42 = Constraint(expr= -m.x212 + m.x233 - m.x245 <= 0)
m.e43 = Constraint(expr= m.x215 - m.x235 - m.x246 <= 0)
m.e44 = Constraint(expr= -m.x215 + m.x235 - m.x246 <= 0)
m.e45 = Constraint(expr= m.x217 - m.x221 - m.x247 <= 0)
m.e46 = Constraint(expr= -m.x217 + m.x221 - m.x247 <= 0)
m.e47 = Constraint(expr= m.x219 - m.x223 - m.x248 <= 0)
m.e48 = Constraint(expr= -m.x219 + m.x223 - m.x248 <= 0)
m.e49 = Constraint(expr= m.x217 - m.x225 - m.x249 <= 0)
m.e50 = Constraint(expr= -m.x217 + m.x225 - m.x249 <= 0)
m.e51 = Constraint(expr= m.x219 - m.x227 - m.x250 <= 0)
m.e52 = Constraint(expr= -m.x219 + m.x227 - m.x250 <= 0)
m.e53 = Constraint(expr= m.x217 - m.x229 - m.x251 <= 0)
m.e54 = Constraint(expr= -m.x217 + m.x229 - m.x251 <= 0)
m.e55 = Constraint(expr= m.x219 - m.x231 - m.x252 <= 0)
m.e56 = Constraint(expr= -m.x219 + m.x231 - m.x252 <= 0)
m.e57 = Constraint(expr= m.x217 - m.x233 - m.x253 <= 0)
m.e58 = Constraint(expr= -m.x217 + m.x233 - m.x253 <= 0)
m.e59 = Constraint(expr= m.x219 - m.x235 - m.x254 <= 0)
m.e60 = Constraint(expr= -m.x219 + m.x235 - m.x254 <= 0)
m.e61 = Constraint(expr= m.x221 - m.x225 - m.x255 <= 0)
m.e62 = Constraint(expr= -m.x221 + m.x225 - m.x255 <= 0)
m.e63 = Constraint(expr= m.x223 - m.x227 - m.x256 <= 0)
m.e64 = Constraint(expr= -m.x223 + m.x227 - m.x256 <= 0)
m.e65 = Constraint(expr= m.x221 - m.x229 - m.x257 <= 0)
m.e66 = Constraint(expr= -m.x221 + m.x229 - m.x257 <= 0)
m.e67 = Constraint(expr= m.x223 - m.x231 - m.x258 <= 0)
m.e68 = Constraint(expr= -m.x223 + m.x231 - m.x258 <= 0)
m.e69 = Constraint(expr= m.x221 - m.x233 - m.x259 <= 0)
m.e70 = Constraint(expr= -m.x221 + m.x233 - m.x259 <= 0)
m.e71 = Constraint(expr= m.x223 - m.x235 - m.x260 <= 0)
m.e72 = Constraint(expr= -m.x223 + m.x235 - m.x260 <= 0)
m.e73 = Constraint(expr= m.x225 - m.x229 - m.x261 <= 0)
m.e74 = Constraint(expr= -m.x225 + m.x229 - m.x261 <= 0)
m.e75 = Constraint(expr= m.x227 - m.x231 - m.x262 <= 0)
m.e76 = Constraint(expr= -m.x227 + m.x231 - m.x262 <= 0)
m.e77 = Constraint(expr= m.x225 - m.x233 - m.x263 <= 0)
m.e78 = Constraint(expr= -m.x225 + m.x233 - m.x263 <= 0)
m.e79 = Constraint(expr= m.x227 - m.x235 - m.x264 <= 0)
m.e80 = Constraint(expr= -m.x227 + m.x235 - m.x264 <= 0)
m.e81 = Constraint(expr= m.x229 - m.x233 - m.x265 <= 0)
m.e82 = Constraint(expr= -m.x229 + m.x233 - m.x265 <= 0)
m.e83 = Constraint(expr= m.x231 - m.x235 - m.x266 <= 0)
m.e84 = Constraint(expr= -m.x231 + m.x235 - m.x266 <= 0)
m.e85 = Constraint(expr= (3.23329980692027 - m.x211)**2 + (4.28386868469468 -
    m.x214)**2 + 70.3380399508289 * m.b1 <= 71.3380399508289)
m.e86 = Constraint(expr= (4.76698640779873 - m.x211)**2 + (2.08930775599057 -
    m.x214)**2 + 88.6345879922179 * m.b2 <= 89.6345879922179)
m.e87 = Constraint(expr= (0.0267350511843534 - m.x211)**2 + (0.782551987461116
    - m.x214)**2 + 173.07608146417 * m.b3 <= 174.07608146417)
m.e88 = Constraint(expr= (8.87351634308632 - m.x211)**2 + (3.10477334960963 -
    m.x214)**2 + 119.189765523566 * m.b4 <= 120.189765523566)
m.e89 = Constraint(expr= (1.91447038389767 - m.x211)**2 + (7.96663059311099 -
    m.x214)**2 + 130.724980923409 * m.b5 <= 131.724980923409)
m.e90 = Constraint(expr= (8.55222670865358 - m.x211)**2 + (0.438866978243134 -
    m.x214)**2 + 152.289257045603 * m.b6 <= 153.289257045603)
m.e91 = Constraint(expr= (1.98863408000317 - m.x211)**2 + (8.96632330014267 -
    m.x214)**2 + 146.275833327099 * m.b7 <= 147.275833327099)
m.e92 = Constraint(expr= (6.95896277872403 - m.x211)**2 + (8.84303759003159 -
    m.x214)**2 + 134.290060533636 * m.b8 <= 135.290060533636)
m.e93 = Constraint(expr= (3.61145308049351 - m.x211)**2 + (6.96757527234085 -
    m.x214)**2 + 90.4153493760657 * m.b9 <= 91.4153493760657)
m.e94 = Constraint(expr= (2.68339142719956 - m.x211)**2 + (9.93756308393997 -
    m.x214)**2 + 155.435876865509 * m.b10 <= 156.435876865509)
m.e95 = Constraint(expr= (3.65720962255625 - m.x211)**2 + (1.74396350476612 -
    m.x214)**2 + 104.574248000865 * m.b11 <= 105.574248000865)
m.e96 = Constraint(expr= (2.58228242210245 - m.x211)**2 + (2.69819914741465 -
    m.x214)**2 + 100.597041943368 * m.b12 <= 101.597041943368)
m.e97 = Constraint(expr= (9.48301079077753 - m.x211)**2 + (4.52610831509011 -
    m.x214)**2 + 123.776000509032 * m.b13 <= 124.776000509032)
m.e98 = Constraint(expr= (0.434598155960523 - m.x211)**2 + (8.14106643299414 -
    m.x214)**2 + 161.401265156826 * m.b14 <= 162.401265156826)
m.e99 = Constraint(expr= (9.02424243556911 - m.x211)**2 + (0.334718733138226 -
    m.x214)**2 + 162.651829944844 * m.b15 <= 163.651829944844)
m.e100 = Constraint(expr= (7.73517137689675 - m.x211)**2 + (3.51323083446602 -
    m.x214)**2 + 94.7869069625255 * m.b16 <= 95.7869069625255)
m.e101 = Constraint(expr= (4.40833475926247 - m.x211)**2 + (4.2821399703396 -
    m.x214)**2 + 58.6043091351014 * m.b17 <= 59.6043091351014)
m.e102 = Constraint(expr= (3.67998758525487 - m.x211)**2 + (5.08335062067947 -
    m.x214)**2 + 68.4616343579277 * m.b18 <= 69.4616343579277)
m.e103 = Constraint(expr= (5.99800586943544 - m.x211)**2 + (0.0322978360521831
    - m.x214)**2 + 129.991228427538 * m.b19 <= 130.991228427538)
m.e104 = Constraint(expr= (8.17580946692085 - m.x211)**2 + (4.02617412348302 -
    m.x214)**2 + 96.803038566953 * m.b20 <= 97.803038566953)
m.e105 = Constraint(expr= (0.174684355003035 - m.x211)**2 + (1.65622387552164
    - m.x214)**2 + 154.161526075002 * m.b21 <= 155.161526075002)
m.e106 = Constraint(expr= (7.75085767529561 - m.x211)**2 + (3.63307602514509 -
    m.x214)**2 + 93.7411075777765 * m.b22 <= 94.7411075777765)
m.e107 = Constraint(expr= (9.9148364830655 - m.x211)**2 + (5.51483189629837 -
    m.x214)**2 + 142.093349557565 * m.b23 <= 143.093349557565)
m.e108 = Constraint(expr= (9.03591083549967 - m.x211)**2 + (1.83449511612235 -
    m.x214)**2 + 138.847878702949 * m.b24 <= 139.847878702949)
m.e109 = Constraint(expr= (8.20421763287616 - m.x211)**2 + (9.82784253465657 -
    m.x214)**2 + 173.07608146417 * m.b25 <= 174.07608146417)
m.e110 = Constraint(expr= (1.03248567695818 - m.x211)**2 + (7.16096452869944 -
    m.x214)**2 + 135.619467005275 * m.b26 <= 136.619467005275)
m.e111 = Constraint(expr= (9.86920389752062 - m.x211)**2 + (1.14806073691438 -
    m.x214)**2 + 165.534538704689 * m.b27 <= 166.534538704689)
m.e112 = Constraint(expr= (0.817141349526822 - m.x211)**2 + (4.89037331555712
    - m.x214)**2 + 115.535016969841 * m.b28 <= 116.535016969841)
m.e113 = Constraint(expr= (0.460831329101329 - m.x211)**2 + (8.44240182853681
    - m.x214)**2 + 165.534538704689 * m.b29 <= 166.534538704689)
m.e114 = Constraint(expr= (6.67410747219087 - m.x211)**2 + (4.4461134165398 -
    m.x214)**2 + 72.7893929676281 * m.b30 <= 73.7893929676281)
m.e115 = Constraint(expr= m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8
    + m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17 +
    m.b18 + m.b19 + m.b20 + m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 +
    m.b27 + m.b28 + m.b29 + m.b30 == 1)
m.e116 = Constraint(expr= (3.23329980692027 - m.x212)**2 + (4.28386868469468 -
    m.x215)**2 + 70.3380399508289 * m.b31 <= 71.3380399508289)
m.e117 = Constraint(expr= (4.76698640779873 - m.x212)**2 + (2.08930775599057 -
    m.x215)**2 + 88.6345879922179 * m.b32 <= 89.6345879922179)
m.e118 = Constraint(expr= (0.0267350511843534 - m.x212)**2 + (0.782551987461116
    - m.x215)**2 + 173.07608146417 * m.b33 <= 174.07608146417)
m.e119 = Constraint(expr= (8.87351634308632 - m.x212)**2 + (3.10477334960963 -
    m.x215)**2 + 119.189765523566 * m.b34 <= 120.189765523566)
m.e120 = Constraint(expr= (1.91447038389767 - m.x212)**2 + (7.96663059311099 -
    m.x215)**2 + 130.724980923409 * m.b35 <= 131.724980923409)
m.e121 = Constraint(expr= (8.55222670865358 - m.x212)**2 + (0.438866978243134
    - m.x215)**2 + 152.289257045603 * m.b36 <= 153.289257045603)
m.e122 = Constraint(expr= (1.98863408000317 - m.x212)**2 + (8.96632330014267 -
    m.x215)**2 + 146.275833327099 * m.b37 <= 147.275833327099)
m.e123 = Constraint(expr= (6.95896277872403 - m.x212)**2 + (8.84303759003159 -
    m.x215)**2 + 134.290060533636 * m.b38 <= 135.290060533636)
m.e124 = Constraint(expr= (3.61145308049351 - m.x212)**2 + (6.96757527234085 -
    m.x215)**2 + 90.4153493760657 * m.b39 <= 91.4153493760657)
m.e125 = Constraint(expr= (2.68339142719956 - m.x212)**2 + (9.93756308393997 -
    m.x215)**2 + 155.435876865509 * m.b40 <= 156.435876865509)
m.e126 = Constraint(expr= (3.65720962255625 - m.x212)**2 + (1.74396350476612 -
    m.x215)**2 + 104.574248000865 * m.b41 <= 105.574248000865)
m.e127 = Constraint(expr= (2.58228242210245 - m.x212)**2 + (2.69819914741465 -
    m.x215)**2 + 100.597041943368 * m.b42 <= 101.597041943368)
m.e128 = Constraint(expr= (9.48301079077753 - m.x212)**2 + (4.52610831509011 -
    m.x215)**2 + 123.776000509032 * m.b43 <= 124.776000509032)
m.e129 = Constraint(expr= (0.434598155960523 - m.x212)**2 + (8.14106643299414
    - m.x215)**2 + 161.401265156826 * m.b44 <= 162.401265156826)
m.e130 = Constraint(expr= (9.02424243556911 - m.x212)**2 + (0.334718733138226
    - m.x215)**2 + 162.651829944844 * m.b45 <= 163.651829944844)
m.e131 = Constraint(expr= (7.73517137689675 - m.x212)**2 + (3.51323083446602 -
    m.x215)**2 + 94.7869069625255 * m.b46 <= 95.7869069625255)
m.e132 = Constraint(expr= (4.40833475926247 - m.x212)**2 + (4.2821399703396 -
    m.x215)**2 + 58.6043091351014 * m.b47 <= 59.6043091351014)
m.e133 = Constraint(expr= (3.67998758525487 - m.x212)**2 + (5.08335062067947 -
    m.x215)**2 + 68.4616343579277 * m.b48 <= 69.4616343579277)
m.e134 = Constraint(expr= (5.99800586943544 - m.x212)**2 + (0.0322978360521831
    - m.x215)**2 + 129.991228427538 * m.b49 <= 130.991228427538)
m.e135 = Constraint(expr= (8.17580946692085 - m.x212)**2 + (4.02617412348302 -
    m.x215)**2 + 96.803038566953 * m.b50 <= 97.803038566953)
m.e136 = Constraint(expr= (0.174684355003035 - m.x212)**2 + (1.65622387552164
    - m.x215)**2 + 154.161526075002 * m.b51 <= 155.161526075002)
m.e137 = Constraint(expr= (7.75085767529561 - m.x212)**2 + (3.63307602514509 -
    m.x215)**2 + 93.7411075777765 * m.b52 <= 94.7411075777765)
m.e138 = Constraint(expr= (9.9148364830655 - m.x212)**2 + (5.51483189629837 -
    m.x215)**2 + 142.093349557565 * m.b53 <= 143.093349557565)
m.e139 = Constraint(expr= (9.03591083549967 - m.x212)**2 + (1.83449511612235 -
    m.x215)**2 + 138.847878702949 * m.b54 <= 139.847878702949)
m.e140 = Constraint(expr= (8.20421763287616 - m.x212)**2 + (9.82784253465657 -
    m.x215)**2 + 173.07608146417 * m.b55 <= 174.07608146417)
m.e141 = Constraint(expr= (1.03248567695818 - m.x212)**2 + (7.16096452869944 -
    m.x215)**2 + 135.619467005275 * m.b56 <= 136.619467005275)
m.e142 = Constraint(expr= (9.86920389752062 - m.x212)**2 + (1.14806073691438 -
    m.x215)**2 + 165.534538704689 * m.b57 <= 166.534538704689)
m.e143 = Constraint(expr= (0.817141349526822 - m.x212)**2 + (4.89037331555712
    - m.x215)**2 + 115.535016969841 * m.b58 <= 116.535016969841)
m.e144 = Constraint(expr= (0.460831329101329 - m.x212)**2 + (8.44240182853681
    - m.x215)**2 + 165.534538704689 * m.b59 <= 166.534538704689)
m.e145 = Constraint(expr= (6.67410747219087 - m.x212)**2 + (4.4461134165398 -
    m.x215)**2 + 72.7893929676281 * m.b60 <= 73.7893929676281)
m.e146 = Constraint(expr= m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 + m.b37
    + m.b38 + m.b39 + m.b40 + m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 +
    m.b47 + m.b48 + m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 +
    m.b56 + m.b57 + m.b58 + m.b59 + m.b60 == 1)
m.e147 = Constraint(expr= (3.23329980692027 - m.x217)**2 + (4.28386868469468 -
    m.x219)**2 + 70.3380399508289 * m.b61 <= 71.3380399508289)
m.e148 = Constraint(expr= (4.76698640779873 - m.x217)**2 + (2.08930775599057 -
    m.x219)**2 + 88.6345879922179 * m.b62 <= 89.6345879922179)
m.e149 = Constraint(expr= (0.0267350511843534 - m.x217)**2 + (0.782551987461116
    - m.x219)**2 + 173.07608146417 * m.b63 <= 174.07608146417)
m.e150 = Constraint(expr= (8.87351634308632 - m.x217)**2 + (3.10477334960963 -
    m.x219)**2 + 119.189765523566 * m.b64 <= 120.189765523566)
m.e151 = Constraint(expr= (1.91447038389767 - m.x217)**2 + (7.96663059311099 -
    m.x219)**2 + 130.724980923409 * m.b65 <= 131.724980923409)
m.e152 = Constraint(expr= (8.55222670865358 - m.x217)**2 + (0.438866978243134
    - m.x219)**2 + 152.289257045603 * m.b66 <= 153.289257045603)
m.e153 = Constraint(expr= (1.98863408000317 - m.x217)**2 + (8.96632330014267 -
    m.x219)**2 + 146.275833327099 * m.b67 <= 147.275833327099)
m.e154 = Constraint(expr= (6.95896277872403 - m.x217)**2 + (8.84303759003159 -
    m.x219)**2 + 134.290060533636 * m.b68 <= 135.290060533636)
m.e155 = Constraint(expr= (3.61145308049351 - m.x217)**2 + (6.96757527234085 -
    m.x219)**2 + 90.4153493760657 * m.b69 <= 91.4153493760657)
m.e156 = Constraint(expr= (2.68339142719956 - m.x217)**2 + (9.93756308393997 -
    m.x219)**2 + 155.435876865509 * m.b70 <= 156.435876865509)
m.e157 = Constraint(expr= (3.65720962255625 - m.x217)**2 + (1.74396350476612 -
    m.x219)**2 + 104.574248000865 * m.b71 <= 105.574248000865)
m.e158 = Constraint(expr= (2.58228242210245 - m.x217)**2 + (2.69819914741465 -
    m.x219)**2 + 100.597041943368 * m.b72 <= 101.597041943368)
m.e159 = Constraint(expr= (9.48301079077753 - m.x217)**2 + (4.52610831509011 -
    m.x219)**2 + 123.776000509032 * m.b73 <= 124.776000509032)
m.e160 = Constraint(expr= (0.434598155960523 - m.x217)**2 + (8.14106643299414
    - m.x219)**2 + 161.401265156826 * m.b74 <= 162.401265156826)
m.e161 = Constraint(expr= (9.02424243556911 - m.x217)**2 + (0.334718733138226
    - m.x219)**2 + 162.651829944844 * m.b75 <= 163.651829944844)
m.e162 = Constraint(expr= (7.73517137689675 - m.x217)**2 + (3.51323083446602 -
    m.x219)**2 + 94.7869069625255 * m.b76 <= 95.7869069625255)
m.e163 = Constraint(expr= (4.40833475926247 - m.x217)**2 + (4.2821399703396 -
    m.x219)**2 + 58.6043091351014 * m.b77 <= 59.6043091351014)
m.e164 = Constraint(expr= (3.67998758525487 - m.x217)**2 + (5.08335062067947 -
    m.x219)**2 + 68.4616343579277 * m.b78 <= 69.4616343579277)
m.e165 = Constraint(expr= (5.99800586943544 - m.x217)**2 + (0.0322978360521831
    - m.x219)**2 + 129.991228427538 * m.b79 <= 130.991228427538)
m.e166 = Constraint(expr= (8.17580946692085 - m.x217)**2 + (4.02617412348302 -
    m.x219)**2 + 96.803038566953 * m.b80 <= 97.803038566953)
m.e167 = Constraint(expr= (0.174684355003035 - m.x217)**2 + (1.65622387552164
    - m.x219)**2 + 154.161526075002 * m.b81 <= 155.161526075002)
m.e168 = Constraint(expr= (7.75085767529561 - m.x217)**2 + (3.63307602514509 -
    m.x219)**2 + 93.7411075777765 * m.b82 <= 94.7411075777765)
m.e169 = Constraint(expr= (9.9148364830655 - m.x217)**2 + (5.51483189629837 -
    m.x219)**2 + 142.093349557565 * m.b83 <= 143.093349557565)
m.e170 = Constraint(expr= (9.03591083549967 - m.x217)**2 + (1.83449511612235 -
    m.x219)**2 + 138.847878702949 * m.b84 <= 139.847878702949)
m.e171 = Constraint(expr= (8.20421763287616 - m.x217)**2 + (9.82784253465657 -
    m.x219)**2 + 173.07608146417 * m.b85 <= 174.07608146417)
m.e172 = Constraint(expr= (1.03248567695818 - m.x217)**2 + (7.16096452869944 -
    m.x219)**2 + 135.619467005275 * m.b86 <= 136.619467005275)
m.e173 = Constraint(expr= (9.86920389752062 - m.x217)**2 + (1.14806073691438 -
    m.x219)**2 + 165.534538704689 * m.b87 <= 166.534538704689)
m.e174 = Constraint(expr= (0.817141349526822 - m.x217)**2 + (4.89037331555712
    - m.x219)**2 + 115.535016969841 * m.b88 <= 116.535016969841)
m.e175 = Constraint(expr= (0.460831329101329 - m.x217)**2 + (8.44240182853681
    - m.x219)**2 + 165.534538704689 * m.b89 <= 166.534538704689)
m.e176 = Constraint(expr= (6.67410747219087 - m.x217)**2 + (4.4461134165398 -
    m.x219)**2 + 72.7893929676281 * m.b90 <= 73.7893929676281)
m.e177 = Constraint(expr= m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b66 + m.b67
    + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 + m.b73 + m.b74 + m.b75 + m.b76 +
    m.b77 + m.b78 + m.b79 + m.b80 + m.b81 + m.b82 + m.b83 + m.b84 + m.b85 +
    m.b86 + m.b87 + m.b88 + m.b89 + m.b90 == 1)
m.e178 = Constraint(expr= (3.23329980692027 - m.x221)**2 + (4.28386868469468 -
    m.x223)**2 + 70.3380399508289 * m.b91 <= 71.3380399508289)
m.e179 = Constraint(expr= (4.76698640779873 - m.x221)**2 + (2.08930775599057 -
    m.x223)**2 + 88.6345879922179 * m.b92 <= 89.6345879922179)
m.e180 = Constraint(expr= (0.0267350511843534 - m.x221)**2 + (0.782551987461116
    - m.x223)**2 + 173.07608146417 * m.b93 <= 174.07608146417)
m.e181 = Constraint(expr= (8.87351634308632 - m.x221)**2 + (3.10477334960963 -
    m.x223)**2 + 119.189765523566 * m.b94 <= 120.189765523566)
m.e182 = Constraint(expr= (1.91447038389767 - m.x221)**2 + (7.96663059311099 -
    m.x223)**2 + 130.724980923409 * m.b95 <= 131.724980923409)
m.e183 = Constraint(expr= (8.55222670865358 - m.x221)**2 + (0.438866978243134
    - m.x223)**2 + 152.289257045603 * m.b96 <= 153.289257045603)
m.e184 = Constraint(expr= (1.98863408000317 - m.x221)**2 + (8.96632330014267 -
    m.x223)**2 + 146.275833327099 * m.b97 <= 147.275833327099)
m.e185 = Constraint(expr= (6.95896277872403 - m.x221)**2 + (8.84303759003159 -
    m.x223)**2 + 134.290060533636 * m.b98 <= 135.290060533636)
m.e186 = Constraint(expr= (3.61145308049351 - m.x221)**2 + (6.96757527234085 -
    m.x223)**2 + 90.4153493760657 * m.b99 <= 91.4153493760657)
m.e187 = Constraint(expr= (2.68339142719956 - m.x221)**2 + (9.93756308393997 -
    m.x223)**2 + 155.435876865509 * m.b100 <= 156.435876865509)
m.e188 = Constraint(expr= (3.65720962255625 - m.x221)**2 + (1.74396350476612 -
    m.x223)**2 + 104.574248000865 * m.b101 <= 105.574248000865)
m.e189 = Constraint(expr= (2.58228242210245 - m.x221)**2 + (2.69819914741465 -
    m.x223)**2 + 100.597041943368 * m.b102 <= 101.597041943368)
m.e190 = Constraint(expr= (9.48301079077753 - m.x221)**2 + (4.52610831509011 -
    m.x223)**2 + 123.776000509032 * m.b103 <= 124.776000509032)
m.e191 = Constraint(expr= (0.434598155960523 - m.x221)**2 + (8.14106643299414
    - m.x223)**2 + 161.401265156826 * m.b104 <= 162.401265156826)
m.e192 = Constraint(expr= (9.02424243556911 - m.x221)**2 + (0.334718733138226
    - m.x223)**2 + 162.651829944844 * m.b105 <= 163.651829944844)
m.e193 = Constraint(expr= (7.73517137689675 - m.x221)**2 + (3.51323083446602 -
    m.x223)**2 + 94.7869069625255 * m.b106 <= 95.7869069625255)
m.e194 = Constraint(expr= (4.40833475926247 - m.x221)**2 + (4.2821399703396 -
    m.x223)**2 + 58.6043091351014 * m.b107 <= 59.6043091351014)
m.e195 = Constraint(expr= (3.67998758525487 - m.x221)**2 + (5.08335062067947 -
    m.x223)**2 + 68.4616343579277 * m.b108 <= 69.4616343579277)
m.e196 = Constraint(expr= (5.99800586943544 - m.x221)**2 + (0.0322978360521831
    - m.x223)**2 + 129.991228427538 * m.b109 <= 130.991228427538)
m.e197 = Constraint(expr= (8.17580946692085 - m.x221)**2 + (4.02617412348302 -
    m.x223)**2 + 96.803038566953 * m.b110 <= 97.803038566953)
m.e198 = Constraint(expr= (0.174684355003035 - m.x221)**2 + (1.65622387552164
    - m.x223)**2 + 154.161526075002 * m.b111 <= 155.161526075002)
m.e199 = Constraint(expr= (7.75085767529561 - m.x221)**2 + (3.63307602514509 -
    m.x223)**2 + 93.7411075777765 * m.b112 <= 94.7411075777765)
m.e200 = Constraint(expr= (9.9148364830655 - m.x221)**2 + (5.51483189629837 -
    m.x223)**2 + 142.093349557565 * m.b113 <= 143.093349557565)
m.e201 = Constraint(expr= (9.03591083549967 - m.x221)**2 + (1.83449511612235 -
    m.x223)**2 + 138.847878702949 * m.b114 <= 139.847878702949)
m.e202 = Constraint(expr= (8.20421763287616 - m.x221)**2 + (9.82784253465657 -
    m.x223)**2 + 173.07608146417 * m.b115 <= 174.07608146417)
m.e203 = Constraint(expr= (1.03248567695818 - m.x221)**2 + (7.16096452869944 -
    m.x223)**2 + 135.619467005275 * m.b116 <= 136.619467005275)
m.e204 = Constraint(expr= (9.86920389752062 - m.x221)**2 + (1.14806073691438 -
    m.x223)**2 + 165.534538704689 * m.b117 <= 166.534538704689)
m.e205 = Constraint(expr= (0.817141349526822 - m.x221)**2 + (4.89037331555712
    - m.x223)**2 + 115.535016969841 * m.b118 <= 116.535016969841)
m.e206 = Constraint(expr= (0.460831329101329 - m.x221)**2 + (8.44240182853681
    - m.x223)**2 + 165.534538704689 * m.b119 <= 166.534538704689)
m.e207 = Constraint(expr= (6.67410747219087 - m.x221)**2 + (4.4461134165398 -
    m.x223)**2 + 72.7893929676281 * m.b120 <= 73.7893929676281)
m.e208 = Constraint(expr= m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b96 + m.b97
    + m.b98 + m.b99 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104 + m.b105 +
    m.b106 + m.b107 + m.b108 + m.b109 + m.b110 + m.b111 + m.b112 + m.b113 +
    m.b114 + m.b115 + m.b116 + m.b117 + m.b118 + m.b119 + m.b120 == 1)
m.e209 = Constraint(expr= (3.23329980692027 - m.x225)**2 + (4.28386868469468 -
    m.x227)**2 + 70.3380399508289 * m.b121 <= 71.3380399508289)
m.e210 = Constraint(expr= (4.76698640779873 - m.x225)**2 + (2.08930775599057 -
    m.x227)**2 + 88.6345879922179 * m.b122 <= 89.6345879922179)
m.e211 = Constraint(expr= (0.0267350511843534 - m.x225)**2 + (0.782551987461116
    - m.x227)**2 + 173.07608146417 * m.b123 <= 174.07608146417)
m.e212 = Constraint(expr= (8.87351634308632 - m.x225)**2 + (3.10477334960963 -
    m.x227)**2 + 119.189765523566 * m.b124 <= 120.189765523566)
m.e213 = Constraint(expr= (1.91447038389767 - m.x225)**2 + (7.96663059311099 -
    m.x227)**2 + 130.724980923409 * m.b125 <= 131.724980923409)
m.e214 = Constraint(expr= (8.55222670865358 - m.x225)**2 + (0.438866978243134
    - m.x227)**2 + 152.289257045603 * m.b126 <= 153.289257045603)
m.e215 = Constraint(expr= (1.98863408000317 - m.x225)**2 + (8.96632330014267 -
    m.x227)**2 + 146.275833327099 * m.b127 <= 147.275833327099)
m.e216 = Constraint(expr= (6.95896277872403 - m.x225)**2 + (8.84303759003159 -
    m.x227)**2 + 134.290060533636 * m.b128 <= 135.290060533636)
m.e217 = Constraint(expr= (3.61145308049351 - m.x225)**2 + (6.96757527234085 -
    m.x227)**2 + 90.4153493760657 * m.b129 <= 91.4153493760657)
m.e218 = Constraint(expr= (2.68339142719956 - m.x225)**2 + (9.93756308393997 -
    m.x227)**2 + 155.435876865509 * m.b130 <= 156.435876865509)
m.e219 = Constraint(expr= (3.65720962255625 - m.x225)**2 + (1.74396350476612 -
    m.x227)**2 + 104.574248000865 * m.b131 <= 105.574248000865)
m.e220 = Constraint(expr= (2.58228242210245 - m.x225)**2 + (2.69819914741465 -
    m.x227)**2 + 100.597041943368 * m.b132 <= 101.597041943368)
m.e221 = Constraint(expr= (9.48301079077753 - m.x225)**2 + (4.52610831509011 -
    m.x227)**2 + 123.776000509032 * m.b133 <= 124.776000509032)
m.e222 = Constraint(expr= (0.434598155960523 - m.x225)**2 + (8.14106643299414
    - m.x227)**2 + 161.401265156826 * m.b134 <= 162.401265156826)
m.e223 = Constraint(expr= (9.02424243556911 - m.x225)**2 + (0.334718733138226
    - m.x227)**2 + 162.651829944844 * m.b135 <= 163.651829944844)
m.e224 = Constraint(expr= (7.73517137689675 - m.x225)**2 + (3.51323083446602 -
    m.x227)**2 + 94.7869069625255 * m.b136 <= 95.7869069625255)
m.e225 = Constraint(expr= (4.40833475926247 - m.x225)**2 + (4.2821399703396 -
    m.x227)**2 + 58.6043091351014 * m.b137 <= 59.6043091351014)
m.e226 = Constraint(expr= (3.67998758525487 - m.x225)**2 + (5.08335062067947 -
    m.x227)**2 + 68.4616343579277 * m.b138 <= 69.4616343579277)
m.e227 = Constraint(expr= (5.99800586943544 - m.x225)**2 + (0.0322978360521831
    - m.x227)**2 + 129.991228427538 * m.b139 <= 130.991228427538)
m.e228 = Constraint(expr= (8.17580946692085 - m.x225)**2 + (4.02617412348302 -
    m.x227)**2 + 96.803038566953 * m.b140 <= 97.803038566953)
m.e229 = Constraint(expr= (0.174684355003035 - m.x225)**2 + (1.65622387552164
    - m.x227)**2 + 154.161526075002 * m.b141 <= 155.161526075002)
m.e230 = Constraint(expr= (7.75085767529561 - m.x225)**2 + (3.63307602514509 -
    m.x227)**2 + 93.7411075777765 * m.b142 <= 94.7411075777765)
m.e231 = Constraint(expr= (9.9148364830655 - m.x225)**2 + (5.51483189629837 -
    m.x227)**2 + 142.093349557565 * m.b143 <= 143.093349557565)
m.e232 = Constraint(expr= (9.03591083549967 - m.x225)**2 + (1.83449511612235 -
    m.x227)**2 + 138.847878702949 * m.b144 <= 139.847878702949)
m.e233 = Constraint(expr= (8.20421763287616 - m.x225)**2 + (9.82784253465657 -
    m.x227)**2 + 173.07608146417 * m.b145 <= 174.07608146417)
m.e234 = Constraint(expr= (1.03248567695818 - m.x225)**2 + (7.16096452869944 -
    m.x227)**2 + 135.619467005275 * m.b146 <= 136.619467005275)
m.e235 = Constraint(expr= (9.86920389752062 - m.x225)**2 + (1.14806073691438 -
    m.x227)**2 + 165.534538704689 * m.b147 <= 166.534538704689)
m.e236 = Constraint(expr= (0.817141349526822 - m.x225)**2 + (4.89037331555712
    - m.x227)**2 + 115.535016969841 * m.b148 <= 116.535016969841)
m.e237 = Constraint(expr= (0.460831329101329 - m.x225)**2 + (8.44240182853681
    - m.x227)**2 + 165.534538704689 * m.b149 <= 166.534538704689)
m.e238 = Constraint(expr= (6.67410747219087 - m.x225)**2 + (4.4461134165398 -
    m.x227)**2 + 72.7893929676281 * m.b150 <= 73.7893929676281)
m.e239 = Constraint(expr= m.b121 + m.b122 + m.b123 + m.b124 + m.b125 + m.b126
    + m.b127 + m.b128 + m.b129 + m.b130 + m.b131 + m.b132 + m.b133 + m.b134 +
    m.b135 + m.b136 + m.b137 + m.b138 + m.b139 + m.b140 + m.b141 + m.b142 +
    m.b143 + m.b144 + m.b145 + m.b146 + m.b147 + m.b148 + m.b149 + m.b150 == 1)
m.e240 = Constraint(expr= (3.23329980692027 - m.x229)**2 + (4.28386868469468 -
    m.x231)**2 + 70.3380399508289 * m.b151 <= 71.3380399508289)
m.e241 = Constraint(expr= (4.76698640779873 - m.x229)**2 + (2.08930775599057 -
    m.x231)**2 + 88.6345879922179 * m.b152 <= 89.6345879922179)
m.e242 = Constraint(expr= (0.0267350511843534 - m.x229)**2 + (0.782551987461116
    - m.x231)**2 + 173.07608146417 * m.b153 <= 174.07608146417)
m.e243 = Constraint(expr= (8.87351634308632 - m.x229)**2 + (3.10477334960963 -
    m.x231)**2 + 119.189765523566 * m.b154 <= 120.189765523566)
m.e244 = Constraint(expr= (1.91447038389767 - m.x229)**2 + (7.96663059311099 -
    m.x231)**2 + 130.724980923409 * m.b155 <= 131.724980923409)
m.e245 = Constraint(expr= (8.55222670865358 - m.x229)**2 + (0.438866978243134
    - m.x231)**2 + 152.289257045603 * m.b156 <= 153.289257045603)
m.e246 = Constraint(expr= (1.98863408000317 - m.x229)**2 + (8.96632330014267 -
    m.x231)**2 + 146.275833327099 * m.b157 <= 147.275833327099)
m.e247 = Constraint(expr= (6.95896277872403 - m.x229)**2 + (8.84303759003159 -
    m.x231)**2 + 134.290060533636 * m.b158 <= 135.290060533636)
m.e248 = Constraint(expr= (3.61145308049351 - m.x229)**2 + (6.96757527234085 -
    m.x231)**2 + 90.4153493760657 * m.b159 <= 91.4153493760657)
m.e249 = Constraint(expr= (2.68339142719956 - m.x229)**2 + (9.93756308393997 -
    m.x231)**2 + 155.435876865509 * m.b160 <= 156.435876865509)
m.e250 = Constraint(expr= (3.65720962255625 - m.x229)**2 + (1.74396350476612 -
    m.x231)**2 + 104.574248000865 * m.b161 <= 105.574248000865)
m.e251 = Constraint(expr= (2.58228242210245 - m.x229)**2 + (2.69819914741465 -
    m.x231)**2 + 100.597041943368 * m.b162 <= 101.597041943368)
m.e252 = Constraint(expr= (9.48301079077753 - m.x229)**2 + (4.52610831509011 -
    m.x231)**2 + 123.776000509032 * m.b163 <= 124.776000509032)
m.e253 = Constraint(expr= (0.434598155960523 - m.x229)**2 + (8.14106643299414
    - m.x231)**2 + 161.401265156826 * m.b164 <= 162.401265156826)
m.e254 = Constraint(expr= (9.02424243556911 - m.x229)**2 + (0.334718733138226
    - m.x231)**2 + 162.651829944844 * m.b165 <= 163.651829944844)
m.e255 = Constraint(expr= (7.73517137689675 - m.x229)**2 + (3.51323083446602 -
    m.x231)**2 + 94.7869069625255 * m.b166 <= 95.7869069625255)
m.e256 = Constraint(expr= (4.40833475926247 - m.x229)**2 + (4.2821399703396 -
    m.x231)**2 + 58.6043091351014 * m.b167 <= 59.6043091351014)
m.e257 = Constraint(expr= (3.67998758525487 - m.x229)**2 + (5.08335062067947 -
    m.x231)**2 + 68.4616343579277 * m.b168 <= 69.4616343579277)
m.e258 = Constraint(expr= (5.99800586943544 - m.x229)**2 + (0.0322978360521831
    - m.x231)**2 + 129.991228427538 * m.b169 <= 130.991228427538)
m.e259 = Constraint(expr= (8.17580946692085 - m.x229)**2 + (4.02617412348302 -
    m.x231)**2 + 96.803038566953 * m.b170 <= 97.803038566953)
m.e260 = Constraint(expr= (0.174684355003035 - m.x229)**2 + (1.65622387552164
    - m.x231)**2 + 154.161526075002 * m.b171 <= 155.161526075002)
m.e261 = Constraint(expr= (7.75085767529561 - m.x229)**2 + (3.63307602514509 -
    m.x231)**2 + 93.7411075777765 * m.b172 <= 94.7411075777765)
m.e262 = Constraint(expr= (9.9148364830655 - m.x229)**2 + (5.51483189629837 -
    m.x231)**2 + 142.093349557565 * m.b173 <= 143.093349557565)
m.e263 = Constraint(expr= (9.03591083549967 - m.x229)**2 + (1.83449511612235 -
    m.x231)**2 + 138.847878702949 * m.b174 <= 139.847878702949)
m.e264 = Constraint(expr= (8.20421763287616 - m.x229)**2 + (9.82784253465657 -
    m.x231)**2 + 173.07608146417 * m.b175 <= 174.07608146417)
m.e265 = Constraint(expr= (1.03248567695818 - m.x229)**2 + (7.16096452869944 -
    m.x231)**2 + 135.619467005275 * m.b176 <= 136.619467005275)
m.e266 = Constraint(expr= (9.86920389752062 - m.x229)**2 + (1.14806073691438 -
    m.x231)**2 + 165.534538704689 * m.b177 <= 166.534538704689)
m.e267 = Constraint(expr= (0.817141349526822 - m.x229)**2 + (4.89037331555712
    - m.x231)**2 + 115.535016969841 * m.b178 <= 116.535016969841)
m.e268 = Constraint(expr= (0.460831329101329 - m.x229)**2 + (8.44240182853681
    - m.x231)**2 + 165.534538704689 * m.b179 <= 166.534538704689)
m.e269 = Constraint(expr= (6.67410747219087 - m.x229)**2 + (4.4461134165398 -
    m.x231)**2 + 72.7893929676281 * m.b180 <= 73.7893929676281)
m.e270 = Constraint(expr= m.b151 + m.b152 + m.b153 + m.b154 + m.b155 + m.b156
    + m.b157 + m.b158 + m.b159 + m.b160 + m.b161 + m.b162 + m.b163 + m.b164 +
    m.b165 + m.b166 + m.b167 + m.b168 + m.b169 + m.b170 + m.b171 + m.b172 +
    m.b173 + m.b174 + m.b175 + m.b176 + m.b177 + m.b178 + m.b179 + m.b180 == 1)
m.e271 = Constraint(expr= (3.23329980692027 - m.x233)**2 + (4.28386868469468 -
    m.x235)**2 + 70.3380399508289 * m.b181 <= 71.3380399508289)
m.e272 = Constraint(expr= (4.76698640779873 - m.x233)**2 + (2.08930775599057 -
    m.x235)**2 + 88.6345879922179 * m.b182 <= 89.6345879922179)
m.e273 = Constraint(expr= (0.0267350511843534 - m.x233)**2 + (0.782551987461116
    - m.x235)**2 + 173.07608146417 * m.b183 <= 174.07608146417)
m.e274 = Constraint(expr= (8.87351634308632 - m.x233)**2 + (3.10477334960963 -
    m.x235)**2 + 119.189765523566 * m.b184 <= 120.189765523566)
m.e275 = Constraint(expr= (1.91447038389767 - m.x233)**2 + (7.96663059311099 -
    m.x235)**2 + 130.724980923409 * m.b185 <= 131.724980923409)
m.e276 = Constraint(expr= (8.55222670865358 - m.x233)**2 + (0.438866978243134
    - m.x235)**2 + 152.289257045603 * m.b186 <= 153.289257045603)
m.e277 = Constraint(expr= (1.98863408000317 - m.x233)**2 + (8.96632330014267 -
    m.x235)**2 + 146.275833327099 * m.b187 <= 147.275833327099)
m.e278 = Constraint(expr= (6.95896277872403 - m.x233)**2 + (8.84303759003159 -
    m.x235)**2 + 134.290060533636 * m.b188 <= 135.290060533636)
m.e279 = Constraint(expr= (3.61145308049351 - m.x233)**2 + (6.96757527234085 -
    m.x235)**2 + 90.4153493760657 * m.b189 <= 91.4153493760657)
m.e280 = Constraint(expr= (2.68339142719956 - m.x233)**2 + (9.93756308393997 -
    m.x235)**2 + 155.435876865509 * m.b190 <= 156.435876865509)
m.e281 = Constraint(expr= (3.65720962255625 - m.x233)**2 + (1.74396350476612 -
    m.x235)**2 + 104.574248000865 * m.b191 <= 105.574248000865)
m.e282 = Constraint(expr= (2.58228242210245 - m.x233)**2 + (2.69819914741465 -
    m.x235)**2 + 100.597041943368 * m.b192 <= 101.597041943368)
m.e283 = Constraint(expr= (9.48301079077753 - m.x233)**2 + (4.52610831509011 -
    m.x235)**2 + 123.776000509032 * m.b193 <= 124.776000509032)
m.e284 = Constraint(expr= (0.434598155960523 - m.x233)**2 + (8.14106643299414
    - m.x235)**2 + 161.401265156826 * m.b194 <= 162.401265156826)
m.e285 = Constraint(expr= (9.02424243556911 - m.x233)**2 + (0.334718733138226
    - m.x235)**2 + 162.651829944844 * m.b195 <= 163.651829944844)
m.e286 = Constraint(expr= (7.73517137689675 - m.x233)**2 + (3.51323083446602 -
    m.x235)**2 + 94.7869069625255 * m.b196 <= 95.7869069625255)
m.e287 = Constraint(expr= (4.40833475926247 - m.x233)**2 + (4.2821399703396 -
    m.x235)**2 + 58.6043091351014 * m.b197 <= 59.6043091351014)
m.e288 = Constraint(expr= (3.67998758525487 - m.x233)**2 + (5.08335062067947 -
    m.x235)**2 + 68.4616343579277 * m.b198 <= 69.4616343579277)
m.e289 = Constraint(expr= (5.99800586943544 - m.x233)**2 + (0.0322978360521831
    - m.x235)**2 + 129.991228427538 * m.b199 <= 130.991228427538)
m.e290 = Constraint(expr= (8.17580946692085 - m.x233)**2 + (4.02617412348302 -
    m.x235)**2 + 96.803038566953 * m.b200 <= 97.803038566953)
m.e291 = Constraint(expr= (0.174684355003035 - m.x233)**2 + (1.65622387552164
    - m.x235)**2 + 154.161526075002 * m.b201 <= 155.161526075002)
m.e292 = Constraint(expr= (7.75085767529561 - m.x233)**2 + (3.63307602514509 -
    m.x235)**2 + 93.7411075777765 * m.b202 <= 94.7411075777765)
m.e293 = Constraint(expr= (9.9148364830655 - m.x233)**2 + (5.51483189629837 -
    m.x235)**2 + 142.093349557565 * m.b203 <= 143.093349557565)
m.e294 = Constraint(expr= (9.03591083549967 - m.x233)**2 + (1.83449511612235 -
    m.x235)**2 + 138.847878702949 * m.b204 <= 139.847878702949)
m.e295 = Constraint(expr= (8.20421763287616 - m.x233)**2 + (9.82784253465657 -
    m.x235)**2 + 173.07608146417 * m.b205 <= 174.07608146417)
m.e296 = Constraint(expr= (1.03248567695818 - m.x233)**2 + (7.16096452869944 -
    m.x235)**2 + 135.619467005275 * m.b206 <= 136.619467005275)
m.e297 = Constraint(expr= (9.86920389752062 - m.x233)**2 + (1.14806073691438 -
    m.x235)**2 + 165.534538704689 * m.b207 <= 166.534538704689)
m.e298 = Constraint(expr= (0.817141349526822 - m.x233)**2 + (4.89037331555712
    - m.x235)**2 + 115.535016969841 * m.b208 <= 116.535016969841)
m.e299 = Constraint(expr= (0.460831329101329 - m.x233)**2 + (8.44240182853681
    - m.x235)**2 + 165.534538704689 * m.b209 <= 166.534538704689)
m.e300 = Constraint(expr= (6.67410747219087 - m.x233)**2 + (4.4461134165398 -
    m.x235)**2 + 72.7893929676281 * m.b210 <= 73.7893929676281)
m.e301 = Constraint(expr= m.b181 + m.b182 + m.b183 + m.b184 + m.b185 + m.b186
    + m.b187 + m.b188 + m.b189 + m.b190 + m.b191 + m.b192 + m.b193 + m.b194 +
    m.b195 + m.b196 + m.b197 + m.b198 + m.b199 + m.b200 + m.b201 + m.b202 +
    m.b203 + m.b204 + m.b205 + m.b206 + m.b207 + m.b208 + m.b209 + m.b210 == 1)
m.e302 = Constraint(expr= m.b1 + m.b31 + m.b61 + m.b91 + m.b121 + m.b151 +
    m.b181 <= 1)
m.e303 = Constraint(expr= m.b2 + m.b32 + m.b62 + m.b92 + m.b122 + m.b152 +
    m.b182 <= 1)
m.e304 = Constraint(expr= m.b3 + m.b33 + m.b63 + m.b93 + m.b123 + m.b153 +
    m.b183 <= 1)
m.e305 = Constraint(expr= m.b4 + m.b34 + m.b64 + m.b94 + m.b124 + m.b154 +
    m.b184 <= 1)
m.e306 = Constraint(expr= m.b5 + m.b35 + m.b65 + m.b95 + m.b125 + m.b155 +
    m.b185 <= 1)
m.e307 = Constraint(expr= m.b6 + m.b36 + m.b66 + m.b96 + m.b126 + m.b156 +
    m.b186 <= 1)
m.e308 = Constraint(expr= m.b7 + m.b37 + m.b67 + m.b97 + m.b127 + m.b157 +
    m.b187 <= 1)
m.e309 = Constraint(expr= m.b8 + m.b38 + m.b68 + m.b98 + m.b128 + m.b158 +
    m.b188 <= 1)
m.e310 = Constraint(expr= m.b9 + m.b39 + m.b69 + m.b99 + m.b129 + m.b159 +
    m.b189 <= 1)
m.e311 = Constraint(expr= m.b10 + m.b40 + m.b70 + m.b100 + m.b130 + m.b160 +
    m.b190 <= 1)
m.e312 = Constraint(expr= m.b11 + m.b41 + m.b71 + m.b101 + m.b131 + m.b161 +
    m.b191 <= 1)
m.e313 = Constraint(expr= m.b12 + m.b42 + m.b72 + m.b102 + m.b132 + m.b162 +
    m.b192 <= 1)
m.e314 = Constraint(expr= m.b13 + m.b43 + m.b73 + m.b103 + m.b133 + m.b163 +
    m.b193 <= 1)
m.e315 = Constraint(expr= m.b14 + m.b44 + m.b74 + m.b104 + m.b134 + m.b164 +
    m.b194 <= 1)
m.e316 = Constraint(expr= m.b15 + m.b45 + m.b75 + m.b105 + m.b135 + m.b165 +
    m.b195 <= 1)
m.e317 = Constraint(expr= m.b16 + m.b46 + m.b76 + m.b106 + m.b136 + m.b166 +
    m.b196 <= 1)
m.e318 = Constraint(expr= m.b17 + m.b47 + m.b77 + m.b107 + m.b137 + m.b167 +
    m.b197 <= 1)
m.e319 = Constraint(expr= m.b18 + m.b48 + m.b78 + m.b108 + m.b138 + m.b168 +
    m.b198 <= 1)
m.e320 = Constraint(expr= m.b19 + m.b49 + m.b79 + m.b109 + m.b139 + m.b169 +
    m.b199 <= 1)
m.e321 = Constraint(expr= m.b20 + m.b50 + m.b80 + m.b110 + m.b140 + m.b170 +
    m.b200 <= 1)
m.e322 = Constraint(expr= m.b21 + m.b51 + m.b81 + m.b111 + m.b141 + m.b171 +
    m.b201 <= 1)
m.e323 = Constraint(expr= m.b22 + m.b52 + m.b82 + m.b112 + m.b142 + m.b172 +
    m.b202 <= 1)
m.e324 = Constraint(expr= m.b23 + m.b53 + m.b83 + m.b113 + m.b143 + m.b173 +
    m.b203 <= 1)
m.e325 = Constraint(expr= m.b24 + m.b54 + m.b84 + m.b114 + m.b144 + m.b174 +
    m.b204 <= 1)
m.e326 = Constraint(expr= m.b25 + m.b55 + m.b85 + m.b115 + m.b145 + m.b175 +
    m.b205 <= 1)
m.e327 = Constraint(expr= m.b26 + m.b56 + m.b86 + m.b116 + m.b146 + m.b176 +
    m.b206 <= 1)
m.e328 = Constraint(expr= m.b27 + m.b57 + m.b87 + m.b117 + m.b147 + m.b177 +
    m.b207 <= 1)
m.e329 = Constraint(expr= m.b28 + m.b58 + m.b88 + m.b118 + m.b148 + m.b178 +
    m.b208 <= 1)
m.e330 = Constraint(expr= m.b29 + m.b59 + m.b89 + m.b119 + m.b149 + m.b179 +
    m.b209 <= 1)
m.e331 = Constraint(expr= m.b30 + m.b60 + m.b90 + m.b120 + m.b150 + m.b180 +
    m.b210 <= 1)
m.e332 = Constraint(expr= m.x211 - m.x212 <= 0)
m.e333 = Constraint(expr= m.x212 - m.x217 <= 0)
m.e334 = Constraint(expr= m.x217 - m.x221 <= 0)
m.e335 = Constraint(expr= m.x221 - m.x225 <= 0)
m.e336 = Constraint(expr= m.x225 - m.x229 <= 0)
m.e337 = Constraint(expr= m.x229 - m.x233 <= 0)
