# MINLP written by GAMS Convert at 05/07/21 17:13:01
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       329        5        0      324        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       260       60      200        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      1648      848      800
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
m.b76 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b77 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b78 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b79 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b80 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b81 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b82 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b83 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b84 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b85 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b86 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b87 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b88 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b89 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b90 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b91 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b92 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b93 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b94 = Var(within=Binary, bounds=(0,1), initialize=0)
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
m.b140 = Var(within=Binary, bounds=(0,1), initialize=0)
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
m.b166 = Var(within=Binary, bounds=(0,1), initialize=0)
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
m.b193 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b194 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b195 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b196 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b197 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b198 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b199 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b200 = Var(within=Binary, bounds=(0,1), initialize=0)
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
m.x256 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x257 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x258 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x259 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x260 = Var(within=Reals, bounds=(0,10), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x203 + m.x206 + m.x209 + m.x212 +
    m.x214 + m.x216 + m.x218 + m.x220 + m.x222 + m.x224 + m.x226 + m.x228 +
    m.x230 + m.x232 + m.x234 + m.x236 + m.x237 + m.x238 + m.x239 + m.x240 +
    m.x241 + m.x242 + m.x243 + m.x244 + m.x245 + m.x246 + m.x247 + m.x248 +
    m.x249 + m.x250 + m.x251 + m.x252 + m.x253 + m.x254 + m.x255 + m.x256 +
    m.x257 + m.x258 + m.x259 + m.x260)

m.e1 = Constraint(expr= m.x201 - m.x202 - m.x203 <= 0)
m.e2 = Constraint(expr= -m.x201 + m.x202 - m.x203 <= 0)
m.e3 = Constraint(expr= m.x204 - m.x205 - m.x206 <= 0)
m.e4 = Constraint(expr= -m.x204 + m.x205 - m.x206 <= 0)
m.e5 = Constraint(expr= m.x207 - m.x208 - m.x209 <= 0)
m.e6 = Constraint(expr= -m.x207 + m.x208 - m.x209 <= 0)
m.e7 = Constraint(expr= m.x210 - m.x211 - m.x212 <= 0)
m.e8 = Constraint(expr= -m.x210 + m.x211 - m.x212 <= 0)
m.e9 = Constraint(expr= m.x201 - m.x213 - m.x214 <= 0)
m.e10 = Constraint(expr= -m.x201 + m.x213 - m.x214 <= 0)
m.e11 = Constraint(expr= m.x204 - m.x215 - m.x216 <= 0)
m.e12 = Constraint(expr= -m.x204 + m.x215 - m.x216 <= 0)
m.e13 = Constraint(expr= m.x207 - m.x217 - m.x218 <= 0)
m.e14 = Constraint(expr= -m.x207 + m.x217 - m.x218 <= 0)
m.e15 = Constraint(expr= m.x210 - m.x219 - m.x220 <= 0)
m.e16 = Constraint(expr= -m.x210 + m.x219 - m.x220 <= 0)
m.e17 = Constraint(expr= m.x201 - m.x221 - m.x222 <= 0)
m.e18 = Constraint(expr= -m.x201 + m.x221 - m.x222 <= 0)
m.e19 = Constraint(expr= m.x204 - m.x223 - m.x224 <= 0)
m.e20 = Constraint(expr= -m.x204 + m.x223 - m.x224 <= 0)
m.e21 = Constraint(expr= m.x207 - m.x225 - m.x226 <= 0)
m.e22 = Constraint(expr= -m.x207 + m.x225 - m.x226 <= 0)
m.e23 = Constraint(expr= m.x210 - m.x227 - m.x228 <= 0)
m.e24 = Constraint(expr= -m.x210 + m.x227 - m.x228 <= 0)
m.e25 = Constraint(expr= m.x201 - m.x229 - m.x230 <= 0)
m.e26 = Constraint(expr= -m.x201 + m.x229 - m.x230 <= 0)
m.e27 = Constraint(expr= m.x204 - m.x231 - m.x232 <= 0)
m.e28 = Constraint(expr= -m.x204 + m.x231 - m.x232 <= 0)
m.e29 = Constraint(expr= m.x207 - m.x233 - m.x234 <= 0)
m.e30 = Constraint(expr= -m.x207 + m.x233 - m.x234 <= 0)
m.e31 = Constraint(expr= m.x210 - m.x235 - m.x236 <= 0)
m.e32 = Constraint(expr= -m.x210 + m.x235 - m.x236 <= 0)
m.e33 = Constraint(expr= m.x202 - m.x213 - m.x237 <= 0)
m.e34 = Constraint(expr= -m.x202 + m.x213 - m.x237 <= 0)
m.e35 = Constraint(expr= m.x205 - m.x215 - m.x238 <= 0)
m.e36 = Constraint(expr= -m.x205 + m.x215 - m.x238 <= 0)
m.e37 = Constraint(expr= m.x208 - m.x217 - m.x239 <= 0)
m.e38 = Constraint(expr= -m.x208 + m.x217 - m.x239 <= 0)
m.e39 = Constraint(expr= m.x211 - m.x219 - m.x240 <= 0)
m.e40 = Constraint(expr= -m.x211 + m.x219 - m.x240 <= 0)
m.e41 = Constraint(expr= m.x202 - m.x221 - m.x241 <= 0)
m.e42 = Constraint(expr= -m.x202 + m.x221 - m.x241 <= 0)
m.e43 = Constraint(expr= m.x205 - m.x223 - m.x242 <= 0)
m.e44 = Constraint(expr= -m.x205 + m.x223 - m.x242 <= 0)
m.e45 = Constraint(expr= m.x208 - m.x225 - m.x243 <= 0)
m.e46 = Constraint(expr= -m.x208 + m.x225 - m.x243 <= 0)
m.e47 = Constraint(expr= m.x211 - m.x227 - m.x244 <= 0)
m.e48 = Constraint(expr= -m.x211 + m.x227 - m.x244 <= 0)
m.e49 = Constraint(expr= m.x202 - m.x229 - m.x245 <= 0)
m.e50 = Constraint(expr= -m.x202 + m.x229 - m.x245 <= 0)
m.e51 = Constraint(expr= m.x205 - m.x231 - m.x246 <= 0)
m.e52 = Constraint(expr= -m.x205 + m.x231 - m.x246 <= 0)
m.e53 = Constraint(expr= m.x208 - m.x233 - m.x247 <= 0)
m.e54 = Constraint(expr= -m.x208 + m.x233 - m.x247 <= 0)
m.e55 = Constraint(expr= m.x211 - m.x235 - m.x248 <= 0)
m.e56 = Constraint(expr= -m.x211 + m.x235 - m.x248 <= 0)
m.e57 = Constraint(expr= m.x213 - m.x221 - m.x249 <= 0)
m.e58 = Constraint(expr= -m.x213 + m.x221 - m.x249 <= 0)
m.e59 = Constraint(expr= m.x215 - m.x223 - m.x250 <= 0)
m.e60 = Constraint(expr= -m.x215 + m.x223 - m.x250 <= 0)
m.e61 = Constraint(expr= m.x217 - m.x225 - m.x251 <= 0)
m.e62 = Constraint(expr= -m.x217 + m.x225 - m.x251 <= 0)
m.e63 = Constraint(expr= m.x219 - m.x227 - m.x252 <= 0)
m.e64 = Constraint(expr= -m.x219 + m.x227 - m.x252 <= 0)
m.e65 = Constraint(expr= m.x213 - m.x229 - m.x253 <= 0)
m.e66 = Constraint(expr= -m.x213 + m.x229 - m.x253 <= 0)
m.e67 = Constraint(expr= m.x215 - m.x231 - m.x254 <= 0)
m.e68 = Constraint(expr= -m.x215 + m.x231 - m.x254 <= 0)
m.e69 = Constraint(expr= m.x217 - m.x233 - m.x255 <= 0)
m.e70 = Constraint(expr= -m.x217 + m.x233 - m.x255 <= 0)
m.e71 = Constraint(expr= m.x219 - m.x235 - m.x256 <= 0)
m.e72 = Constraint(expr= -m.x219 + m.x235 - m.x256 <= 0)
m.e73 = Constraint(expr= m.x221 - m.x229 - m.x257 <= 0)
m.e74 = Constraint(expr= -m.x221 + m.x229 - m.x257 <= 0)
m.e75 = Constraint(expr= m.x223 - m.x231 - m.x258 <= 0)
m.e76 = Constraint(expr= -m.x223 + m.x231 - m.x258 <= 0)
m.e77 = Constraint(expr= m.x225 - m.x233 - m.x259 <= 0)
m.e78 = Constraint(expr= -m.x225 + m.x233 - m.x259 <= 0)
m.e79 = Constraint(expr= m.x227 - m.x235 - m.x260 <= 0)
m.e80 = Constraint(expr= -m.x227 + m.x235 - m.x260 <= 0)
m.e81 = Constraint(expr= (4.04180710023322 - m.x201)**2 + (0.0638120906615358
    - m.x204)**2 + (9.31163964055327 - m.x207)**2 + (9.59399362610548 - m.x210)
    **2 + 247.918202243131 * m.b1 <= 248.918202243131)
m.e82 = Constraint(expr= (7.58630473662528 - m.x201)**2 + (9.81696808234314 -
    m.x204)**2 + (6.80594062551012 - m.x207)**2 + (5.73941560922778 - m.x210)**
    2 + 172.97632549661 * m.b2 <= 173.97632549661)
m.e83 = Constraint(expr= (4.73576208695481 - m.x201)**2 + (2.81737915136856 -
    m.x204)**2 + (0.919919756378161 - m.x207)**2 + (0.427396562561213 - m.x210)
    **2 + 192.870854266185 * m.b3 <= 193.870854266185)
m.e84 = Constraint(expr= (0.428853030190813 - m.x201)**2 + (5.71294529671424 -
    m.x204)**2 + (2.06079707847737 - m.x207)**2 + (3.87755584734058 - m.x210)**
    2 + 168.997467410559 * m.b4 <= 169.997467410559)
m.e85 = Constraint(expr= (1.0774677742481 - m.x201)**2 + (0.802343324640142 -
    m.x204)**2 + (5.05560926630768 - m.x207)**2 + (6.38583388950109 - m.x210)**
    2 + 160.592363348786 * m.b5 <= 161.592363348786)
m.e86 = Constraint(expr= (1.12638621393495 - m.x201)**2 + (1.60465763780203 -
    m.x204)**2 + (4.07986801140447 - m.x207)**2 + (2.17037731980447 - m.x210)**
    2 + 165.579518594568 * m.b6 <= 166.579518594568)
m.e87 = Constraint(expr= (1.82688019388165 - m.x201)**2 + (4.63411239877442 -
    m.x204)**2 + (5.05145431164509 - m.x207)**2 + (3.74855986966667 - m.x210)**
    2 + 104.866109371321 * m.b7 <= 105.866109371321)
m.e88 = Constraint(expr= (8.44017389324234 - m.x201)**2 + (3.82403068466693 -
    m.x204)**2 + (8.92353737043929 - m.x207)**2 + (4.64273943517454 - m.x210)**
    2 + 167.587335871824 * m.b8 <= 168.587335871824)
m.e89 = Constraint(expr= (5.87176386853829 - m.x201)**2 + (1.44175632208916 -
    m.x204)**2 + (3.18165222878213 - m.x207)**2 + (5.19789554578514 - m.x210)**
    2 + 128.282182640462 * m.b9 <= 129.282182640462)
m.e90 = Constraint(expr= (6.76013297629122 - m.x201)**2 + (3.21254997009641 -
    m.x204)**2 + (9.46706727409796 - m.x207)**2 + (0.816604516799142 - m.x210)
    **2 + 226.736334872871 * m.b10 <= 227.736334872871)
m.e91 = Constraint(expr= (3.24901644799959 - m.x201)**2 + (7.51480516788174 -
    m.x204)**2 + (4.01508707364147 - m.x207)**2 + (4.50822439140953 - m.x210)**
    2 + 131.046642602757 * m.b11 <= 132.046642602757)
m.e92 = Constraint(expr= (0.388900076234485 - m.x201)**2 + (5.87163371055414 -
    m.x204)**2 + (3.83580726436302 - m.x207)**2 + (3.02326353201313 - m.x210)**
    2 + 152.01486044439 * m.b12 <= 153.01486044439)
m.e93 = Constraint(expr= (0.790446136347066 - m.x201)**2 + (8.25540861746511 -
    m.x204)**2 + (8.76325441282356 - m.x207)**2 + (3.16275732090416 - m.x210)**
    2 + 202.990878768535 * m.b13 <= 203.990878768535)
m.e94 = Constraint(expr= (2.24835841067941 - m.x201)**2 + (1.49328376014994 -
    m.x204)**2 + (6.05269717076173 - m.x207)**2 + (9.30035396512944 - m.x210)**
    2 + 187.279582970004 * m.b14 <= 188.279582970004)
m.e95 = Constraint(expr= (9.00506853532299 - m.x201)**2 + (4.84258207392989 -
    m.x204)**2 + (5.30242448190069 - m.x207)**2 + (1.96947429895047 - m.x210)**
    2 + 158.002379384289 * m.b15 <= 159.002379384289)
m.e96 = Constraint(expr= (7.06852474736736 - m.x201)**2 + (0.403068662414334 -
    m.x204)**2 + (0.20219913526021 - m.x207)**2 + (1.72727050657669 - m.x210)**
    2 + 229.407479988904 * m.b16 <= 230.407479988904)
m.e97 = Constraint(expr= (2.04415436610942 - m.x201)**2 + (9.79340385699591 -
    m.x204)**2 + (1.37229670501157 - m.x207)**2 + (6.1403045098624 - m.x210)**2
    + 215.942963749551 * m.b17 <= 216.942963749551)
m.e98 = Constraint(expr= (7.57624032466962 - m.x201)**2 + (7.76217255967217 -
    m.x204)**2 + (0.355128375706556 - m.x207)**2 + (1.44611951386816 - m.x210)
    **2 + 247.918202243131 * m.b18 <= 248.918202243131)
m.e99 = Constraint(expr= (5.27432353822418 - m.x201)**2 + (8.94703040209787 -
    m.x204)**2 + (6.2373757380993 - m.x207)**2 + (9.23461806871597 - m.x210)**2
    + 195.00222302105 * m.b19 <= 196.00222302105)
m.e100 = Constraint(expr= (0.996186045951476 - m.x201)**2 + (1.36457455477018
    - m.x204)**2 + (1.56471044095596 - m.x207)**2 + (3.36816773533039 - m.x210)
    **2 + 172.294180536922 * m.b20 <= 173.294180536922)
m.e101 = Constraint(expr= (4.02233509809877 - m.x201)**2 + (8.45745652401958 -
    m.x204)**2 + (9.01254148426443 - m.x207)**2 + (8.74685412361603 - m.x210)**
    2 + 229.407479988904 * m.b21 <= 230.407479988904)
m.e102 = Constraint(expr= (8.70857268900905 - m.x201)**2 + (1.11796994384596 -
    m.x204)**2 + (5.00432053303839 - m.x207)**2 + (2.40385817397397 - m.x210)**
    2 + 180.771322437022 * m.b22 <= 181.771322437022)
m.e103 = Constraint(expr= (7.54765700959199 - m.x201)**2 + (4.80143075267339 -
    m.x204)**2 + (8.40046817462899 - m.x207)**2 + (8.29113964786696 - m.x210)**
    2 + 152.663354968323 * m.b23 <= 153.663354968323)
m.e104 = Constraint(expr= (0.966865551002543 - m.x201)**2 + (9.92855620143344
    - m.x204)**2 + (5.74951319729978 - m.x207)**2 + (3.53637928232447 - m.x210)
    **2 + 188.008216290247 * m.b24 <= 189.008216290247)
m.e105 = Constraint(expr= (0.45538917132773 - m.x201)**2 + (1.48603663213761 -
    m.x204)**2 + (9.82188246465487 - m.x207)**2 + (7.4461736036308 - m.x210)**2
    + 245.091065242949 * m.b25 <= 246.091065242949)
m.e106 = Constraint(expr= (6.75415604579508 - m.x201)**2 + (4.56383909220998 -
    m.x204)**2 + (5.80815448731129 - m.x207)**2 + (1.39230685391611 - m.x210)**
    2 + 140.463739979998 * m.b26 <= 141.463739979998)
m.e107 = Constraint(expr= (8.85890029315383 - m.x201)**2 + (6.16141864425327 -
    m.x204)**2 + (2.25373679776979 - m.x207)**2 + (2.60508233041854 - m.x210)**
    2 + 199.511614429278 * m.b27 <= 200.511614429278)
m.e108 = Constraint(expr= (5.3549498366276 - m.x201)**2 + (6.5028620799581 -
    m.x204)**2 + (3.77860881416883 - m.x207)**2 + (3.88773754222155 - m.x210)**
    2 + 126.987839343492 * m.b28 <= 127.987839343492)
m.e109 = Constraint(expr= (0.113259012567859 - m.x201)**2 + (4.95866301539607
    - m.x204)**2 + (8.39278608004883 - m.x207)**2 + (2.33998997152253 - m.x210)
    **2 + 181.595796730204 * m.b29 <= 182.595796730204)
m.e110 = Constraint(expr= (4.01186017931937 - m.x201)**2 + (1.58505280271348 -
    m.x204)**2 + (6.66701704740187 - m.x207)**2 + (6.15579863983494 - m.x210)**
    2 + 140.650077775347 * m.b30 <= 141.650077775347)
m.e111 = Constraint(expr= (6.96869478428464 - m.x201)**2 + (4.10398909952988 -
    m.x204)**2 + (6.0102827867986 - m.x207)**2 + (2.74411959285283 - m.x210)**2
    + 129.582385211462 * m.b31 <= 130.582385211462)
m.e112 = Constraint(expr= (4.87285195085022 - m.x201)**2 + (9.86295765077007 -
    m.x204)**2 + (0.143489359365916 - m.x207)**2 + (8.80632332989694 - m.x210)
    **2 + 226.736334872871 * m.b32 <= 227.736334872871)
m.e113 = Constraint(expr= (7.83131209913544 - m.x201)**2 + (1.43609337392774 -
    m.x204)**2 + (3.30054263355244 - m.x207)**2 + (0.00125718557078214 - m.x210)
    **2 + 199.220071314074 * m.b33 <= 200.220071314074)
m.e114 = Constraint(expr= (5.66454764000128 - m.x201)**2 + (5.56331545204103 -
    m.x204)**2 + (1.14993711831163 - m.x207)**2 + (4.5715891663462 - m.x210)**2
    + 149.784254351217 * m.b34 <= 150.784254351217)
m.e115 = Constraint(expr= (3.33190103022031 - m.x201)**2 + (4.9445883792678 -
    m.x204)**2 + (7.30728727625694 - m.x207)**2 + (8.01246235442081 - m.x210)**
    2 + 146.896187485824 * m.b35 <= 147.896187485824)
m.e116 = Constraint(expr= (9.33298244503801 - m.x201)**2 + (0.723851580512842
    - m.x204)**2 + (8.42864317892565 - m.x207)**2 + (4.32119007374061 - m.x210)
    **2 + 219.90174536577 * m.b36 <= 220.90174536577)
m.e117 = Constraint(expr= (5.08063287228698 - m.x201)**2 + (8.38761519865226 -
    m.x204)**2 + (1.4027356086197 - m.x207)**2 + (6.86412480592018 - m.x210)**2
    + 164.06318777512 * m.b37 <= 165.06318777512)
m.e118 = Constraint(expr= (2.37234068047016 - m.x201)**2 + (7.05084260559812 -
    m.x204)**2 + (9.48571415448197 - m.x207)**2 + (5.77659906719162 - m.x210)**
    2 + 194.814503184848 * m.b38 <= 195.814503184848)
m.e119 = Constraint(expr= (4.16198173364841 - m.x201)**2 + (5.45114144772148 -
    m.x204)**2 + (9.00182905163397 - m.x207)**2 + (3.4826499770368 - m.x210)**2
    + 149.300564915884 * m.b39 <= 150.300564915884)
m.e120 = Constraint(expr= (4.45933786757702 - m.x201)**2 + (4.47805189258463 -
    m.x204)**2 + (6.61692822015399 - m.x207)**2 + (5.6343120215581 - m.x210)**2
    + 99.1502941148379 * m.b40 <= 100.150294114838)
m.e121 = Constraint(expr= m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8
    + m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17 +
    m.b18 + m.b19 + m.b20 + m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 +
    m.b27 + m.b28 + m.b29 + m.b30 + m.b31 + m.b32 + m.b33 + m.b34 + m.b35 +
    m.b36 + m.b37 + m.b38 + m.b39 + m.b40 == 1)
m.e122 = Constraint(expr= (4.04180710023322 - m.x202)**2 + (0.0638120906615358
    - m.x205)**2 + (9.31163964055327 - m.x208)**2 + (9.59399362610548 - m.x211)
    **2 + 247.918202243131 * m.b41 <= 248.918202243131)
m.e123 = Constraint(expr= (7.58630473662528 - m.x202)**2 + (9.81696808234314 -
    m.x205)**2 + (6.80594062551012 - m.x208)**2 + (5.73941560922778 - m.x211)**
    2 + 172.97632549661 * m.b42 <= 173.97632549661)
m.e124 = Constraint(expr= (4.73576208695481 - m.x202)**2 + (2.81737915136856 -
    m.x205)**2 + (0.919919756378161 - m.x208)**2 + (0.427396562561213 - m.x211)
    **2 + 192.870854266185 * m.b43 <= 193.870854266185)
m.e125 = Constraint(expr= (0.428853030190813 - m.x202)**2 + (5.71294529671424
    - m.x205)**2 + (2.06079707847737 - m.x208)**2 + (3.87755584734058 - m.x211)
    **2 + 168.997467410559 * m.b44 <= 169.997467410559)
m.e126 = Constraint(expr= (1.0774677742481 - m.x202)**2 + (0.802343324640142 -
    m.x205)**2 + (5.05560926630768 - m.x208)**2 + (6.38583388950109 - m.x211)**
    2 + 160.592363348786 * m.b45 <= 161.592363348786)
m.e127 = Constraint(expr= (1.12638621393495 - m.x202)**2 + (1.60465763780203 -
    m.x205)**2 + (4.07986801140447 - m.x208)**2 + (2.17037731980447 - m.x211)**
    2 + 165.579518594568 * m.b46 <= 166.579518594568)
m.e128 = Constraint(expr= (1.82688019388165 - m.x202)**2 + (4.63411239877442 -
    m.x205)**2 + (5.05145431164509 - m.x208)**2 + (3.74855986966667 - m.x211)**
    2 + 104.866109371321 * m.b47 <= 105.866109371321)
m.e129 = Constraint(expr= (8.44017389324234 - m.x202)**2 + (3.82403068466693 -
    m.x205)**2 + (8.92353737043929 - m.x208)**2 + (4.64273943517454 - m.x211)**
    2 + 167.587335871824 * m.b48 <= 168.587335871824)
m.e130 = Constraint(expr= (5.87176386853829 - m.x202)**2 + (1.44175632208916 -
    m.x205)**2 + (3.18165222878213 - m.x208)**2 + (5.19789554578514 - m.x211)**
    2 + 128.282182640462 * m.b49 <= 129.282182640462)
m.e131 = Constraint(expr= (6.76013297629122 - m.x202)**2 + (3.21254997009641 -
    m.x205)**2 + (9.46706727409796 - m.x208)**2 + (0.816604516799142 - m.x211)
    **2 + 226.736334872871 * m.b50 <= 227.736334872871)
m.e132 = Constraint(expr= (3.24901644799959 - m.x202)**2 + (7.51480516788174 -
    m.x205)**2 + (4.01508707364147 - m.x208)**2 + (4.50822439140953 - m.x211)**
    2 + 131.046642602757 * m.b51 <= 132.046642602757)
m.e133 = Constraint(expr= (0.388900076234485 - m.x202)**2 + (5.87163371055414
    - m.x205)**2 + (3.83580726436302 - m.x208)**2 + (3.02326353201313 - m.x211)
    **2 + 152.01486044439 * m.b52 <= 153.01486044439)
m.e134 = Constraint(expr= (0.790446136347066 - m.x202)**2 + (8.25540861746511
    - m.x205)**2 + (8.76325441282356 - m.x208)**2 + (3.16275732090416 - m.x211)
    **2 + 202.990878768535 * m.b53 <= 203.990878768535)
m.e135 = Constraint(expr= (2.24835841067941 - m.x202)**2 + (1.49328376014994 -
    m.x205)**2 + (6.05269717076173 - m.x208)**2 + (9.30035396512944 - m.x211)**
    2 + 187.279582970004 * m.b54 <= 188.279582970004)
m.e136 = Constraint(expr= (9.00506853532299 - m.x202)**2 + (4.84258207392989 -
    m.x205)**2 + (5.30242448190069 - m.x208)**2 + (1.96947429895047 - m.x211)**
    2 + 158.002379384289 * m.b55 <= 159.002379384289)
m.e137 = Constraint(expr= (7.06852474736736 - m.x202)**2 + (0.403068662414334
    - m.x205)**2 + (0.20219913526021 - m.x208)**2 + (1.72727050657669 - m.x211)
    **2 + 229.407479988904 * m.b56 <= 230.407479988904)
m.e138 = Constraint(expr= (2.04415436610942 - m.x202)**2 + (9.79340385699591 -
    m.x205)**2 + (1.37229670501157 - m.x208)**2 + (6.1403045098624 - m.x211)**2
    + 215.942963749551 * m.b57 <= 216.942963749551)
m.e139 = Constraint(expr= (7.57624032466962 - m.x202)**2 + (7.76217255967217 -
    m.x205)**2 + (0.355128375706556 - m.x208)**2 + (1.44611951386816 - m.x211)
    **2 + 247.918202243131 * m.b58 <= 248.918202243131)
m.e140 = Constraint(expr= (5.27432353822418 - m.x202)**2 + (8.94703040209787 -
    m.x205)**2 + (6.2373757380993 - m.x208)**2 + (9.23461806871597 - m.x211)**2
    + 195.00222302105 * m.b59 <= 196.00222302105)
m.e141 = Constraint(expr= (0.996186045951476 - m.x202)**2 + (1.36457455477018
    - m.x205)**2 + (1.56471044095596 - m.x208)**2 + (3.36816773533039 - m.x211)
    **2 + 172.294180536922 * m.b60 <= 173.294180536922)
m.e142 = Constraint(expr= (4.02233509809877 - m.x202)**2 + (8.45745652401958 -
    m.x205)**2 + (9.01254148426443 - m.x208)**2 + (8.74685412361603 - m.x211)**
    2 + 229.407479988904 * m.b61 <= 230.407479988904)
m.e143 = Constraint(expr= (8.70857268900905 - m.x202)**2 + (1.11796994384596 -
    m.x205)**2 + (5.00432053303839 - m.x208)**2 + (2.40385817397397 - m.x211)**
    2 + 180.771322437022 * m.b62 <= 181.771322437022)
m.e144 = Constraint(expr= (7.54765700959199 - m.x202)**2 + (4.80143075267339 -
    m.x205)**2 + (8.40046817462899 - m.x208)**2 + (8.29113964786696 - m.x211)**
    2 + 152.663354968323 * m.b63 <= 153.663354968323)
m.e145 = Constraint(expr= (0.966865551002543 - m.x202)**2 + (9.92855620143344
    - m.x205)**2 + (5.74951319729978 - m.x208)**2 + (3.53637928232447 - m.x211)
    **2 + 188.008216290247 * m.b64 <= 189.008216290247)
m.e146 = Constraint(expr= (0.45538917132773 - m.x202)**2 + (1.48603663213761 -
    m.x205)**2 + (9.82188246465487 - m.x208)**2 + (7.4461736036308 - m.x211)**2
    + 245.091065242949 * m.b65 <= 246.091065242949)
m.e147 = Constraint(expr= (6.75415604579508 - m.x202)**2 + (4.56383909220998 -
    m.x205)**2 + (5.80815448731129 - m.x208)**2 + (1.39230685391611 - m.x211)**
    2 + 140.463739979998 * m.b66 <= 141.463739979998)
m.e148 = Constraint(expr= (8.85890029315383 - m.x202)**2 + (6.16141864425327 -
    m.x205)**2 + (2.25373679776979 - m.x208)**2 + (2.60508233041854 - m.x211)**
    2 + 199.511614429278 * m.b67 <= 200.511614429278)
m.e149 = Constraint(expr= (5.3549498366276 - m.x202)**2 + (6.5028620799581 -
    m.x205)**2 + (3.77860881416883 - m.x208)**2 + (3.88773754222155 - m.x211)**
    2 + 126.987839343492 * m.b68 <= 127.987839343492)
m.e150 = Constraint(expr= (0.113259012567859 - m.x202)**2 + (4.95866301539607
    - m.x205)**2 + (8.39278608004883 - m.x208)**2 + (2.33998997152253 - m.x211)
    **2 + 181.595796730204 * m.b69 <= 182.595796730204)
m.e151 = Constraint(expr= (4.01186017931937 - m.x202)**2 + (1.58505280271348 -
    m.x205)**2 + (6.66701704740187 - m.x208)**2 + (6.15579863983494 - m.x211)**
    2 + 140.650077775347 * m.b70 <= 141.650077775347)
m.e152 = Constraint(expr= (6.96869478428464 - m.x202)**2 + (4.10398909952988 -
    m.x205)**2 + (6.0102827867986 - m.x208)**2 + (2.74411959285283 - m.x211)**2
    + 129.582385211462 * m.b71 <= 130.582385211462)
m.e153 = Constraint(expr= (4.87285195085022 - m.x202)**2 + (9.86295765077007 -
    m.x205)**2 + (0.143489359365916 - m.x208)**2 + (8.80632332989694 - m.x211)
    **2 + 226.736334872871 * m.b72 <= 227.736334872871)
m.e154 = Constraint(expr= (7.83131209913544 - m.x202)**2 + (1.43609337392774 -
    m.x205)**2 + (3.30054263355244 - m.x208)**2 + (0.00125718557078214 - m.x211)
    **2 + 199.220071314074 * m.b73 <= 200.220071314074)
m.e155 = Constraint(expr= (5.66454764000128 - m.x202)**2 + (5.56331545204103 -
    m.x205)**2 + (1.14993711831163 - m.x208)**2 + (4.5715891663462 - m.x211)**2
    + 149.784254351217 * m.b74 <= 150.784254351217)
m.e156 = Constraint(expr= (3.33190103022031 - m.x202)**2 + (4.9445883792678 -
    m.x205)**2 + (7.30728727625694 - m.x208)**2 + (8.01246235442081 - m.x211)**
    2 + 146.896187485824 * m.b75 <= 147.896187485824)
m.e157 = Constraint(expr= (9.33298244503801 - m.x202)**2 + (0.723851580512842
    - m.x205)**2 + (8.42864317892565 - m.x208)**2 + (4.32119007374061 - m.x211)
    **2 + 219.90174536577 * m.b76 <= 220.90174536577)
m.e158 = Constraint(expr= (5.08063287228698 - m.x202)**2 + (8.38761519865226 -
    m.x205)**2 + (1.4027356086197 - m.x208)**2 + (6.86412480592018 - m.x211)**2
    + 164.06318777512 * m.b77 <= 165.06318777512)
m.e159 = Constraint(expr= (2.37234068047016 - m.x202)**2 + (7.05084260559812 -
    m.x205)**2 + (9.48571415448197 - m.x208)**2 + (5.77659906719162 - m.x211)**
    2 + 194.814503184848 * m.b78 <= 195.814503184848)
m.e160 = Constraint(expr= (4.16198173364841 - m.x202)**2 + (5.45114144772148 -
    m.x205)**2 + (9.00182905163397 - m.x208)**2 + (3.4826499770368 - m.x211)**2
    + 149.300564915884 * m.b79 <= 150.300564915884)
m.e161 = Constraint(expr= (4.45933786757702 - m.x202)**2 + (4.47805189258463 -
    m.x205)**2 + (6.61692822015399 - m.x208)**2 + (5.6343120215581 - m.x211)**2
    + 99.1502941148379 * m.b80 <= 100.150294114838)
m.e162 = Constraint(expr= m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47
    + m.b48 + m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 +
    m.b57 + m.b58 + m.b59 + m.b60 + m.b61 + m.b62 + m.b63 + m.b64 + m.b65 +
    m.b66 + m.b67 + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 + m.b73 + m.b74 +
    m.b75 + m.b76 + m.b77 + m.b78 + m.b79 + m.b80 == 1)
m.e163 = Constraint(expr= (4.04180710023322 - m.x213)**2 + (0.0638120906615358
    - m.x215)**2 + (9.31163964055327 - m.x217)**2 + (9.59399362610548 - m.x219)
    **2 + 247.918202243131 * m.b81 <= 248.918202243131)
m.e164 = Constraint(expr= (7.58630473662528 - m.x213)**2 + (9.81696808234314 -
    m.x215)**2 + (6.80594062551012 - m.x217)**2 + (5.73941560922778 - m.x219)**
    2 + 172.97632549661 * m.b82 <= 173.97632549661)
m.e165 = Constraint(expr= (4.73576208695481 - m.x213)**2 + (2.81737915136856 -
    m.x215)**2 + (0.919919756378161 - m.x217)**2 + (0.427396562561213 - m.x219)
    **2 + 192.870854266185 * m.b83 <= 193.870854266185)
m.e166 = Constraint(expr= (0.428853030190813 - m.x213)**2 + (5.71294529671424
    - m.x215)**2 + (2.06079707847737 - m.x217)**2 + (3.87755584734058 - m.x219)
    **2 + 168.997467410559 * m.b84 <= 169.997467410559)
m.e167 = Constraint(expr= (1.0774677742481 - m.x213)**2 + (0.802343324640142 -
    m.x215)**2 + (5.05560926630768 - m.x217)**2 + (6.38583388950109 - m.x219)**
    2 + 160.592363348786 * m.b85 <= 161.592363348786)
m.e168 = Constraint(expr= (1.12638621393495 - m.x213)**2 + (1.60465763780203 -
    m.x215)**2 + (4.07986801140447 - m.x217)**2 + (2.17037731980447 - m.x219)**
    2 + 165.579518594568 * m.b86 <= 166.579518594568)
m.e169 = Constraint(expr= (1.82688019388165 - m.x213)**2 + (4.63411239877442 -
    m.x215)**2 + (5.05145431164509 - m.x217)**2 + (3.74855986966667 - m.x219)**
    2 + 104.866109371321 * m.b87 <= 105.866109371321)
m.e170 = Constraint(expr= (8.44017389324234 - m.x213)**2 + (3.82403068466693 -
    m.x215)**2 + (8.92353737043929 - m.x217)**2 + (4.64273943517454 - m.x219)**
    2 + 167.587335871824 * m.b88 <= 168.587335871824)
m.e171 = Constraint(expr= (5.87176386853829 - m.x213)**2 + (1.44175632208916 -
    m.x215)**2 + (3.18165222878213 - m.x217)**2 + (5.19789554578514 - m.x219)**
    2 + 128.282182640462 * m.b89 <= 129.282182640462)
m.e172 = Constraint(expr= (6.76013297629122 - m.x213)**2 + (3.21254997009641 -
    m.x215)**2 + (9.46706727409796 - m.x217)**2 + (0.816604516799142 - m.x219)
    **2 + 226.736334872871 * m.b90 <= 227.736334872871)
m.e173 = Constraint(expr= (3.24901644799959 - m.x213)**2 + (7.51480516788174 -
    m.x215)**2 + (4.01508707364147 - m.x217)**2 + (4.50822439140953 - m.x219)**
    2 + 131.046642602757 * m.b91 <= 132.046642602757)
m.e174 = Constraint(expr= (0.388900076234485 - m.x213)**2 + (5.87163371055414
    - m.x215)**2 + (3.83580726436302 - m.x217)**2 + (3.02326353201313 - m.x219)
    **2 + 152.01486044439 * m.b92 <= 153.01486044439)
m.e175 = Constraint(expr= (0.790446136347066 - m.x213)**2 + (8.25540861746511
    - m.x215)**2 + (8.76325441282356 - m.x217)**2 + (3.16275732090416 - m.x219)
    **2 + 202.990878768535 * m.b93 <= 203.990878768535)
m.e176 = Constraint(expr= (2.24835841067941 - m.x213)**2 + (1.49328376014994 -
    m.x215)**2 + (6.05269717076173 - m.x217)**2 + (9.30035396512944 - m.x219)**
    2 + 187.279582970004 * m.b94 <= 188.279582970004)
m.e177 = Constraint(expr= (9.00506853532299 - m.x213)**2 + (4.84258207392989 -
    m.x215)**2 + (5.30242448190069 - m.x217)**2 + (1.96947429895047 - m.x219)**
    2 + 158.002379384289 * m.b95 <= 159.002379384289)
m.e178 = Constraint(expr= (7.06852474736736 - m.x213)**2 + (0.403068662414334
    - m.x215)**2 + (0.20219913526021 - m.x217)**2 + (1.72727050657669 - m.x219)
    **2 + 229.407479988904 * m.b96 <= 230.407479988904)
m.e179 = Constraint(expr= (2.04415436610942 - m.x213)**2 + (9.79340385699591 -
    m.x215)**2 + (1.37229670501157 - m.x217)**2 + (6.1403045098624 - m.x219)**2
    + 215.942963749551 * m.b97 <= 216.942963749551)
m.e180 = Constraint(expr= (7.57624032466962 - m.x213)**2 + (7.76217255967217 -
    m.x215)**2 + (0.355128375706556 - m.x217)**2 + (1.44611951386816 - m.x219)
    **2 + 247.918202243131 * m.b98 <= 248.918202243131)
m.e181 = Constraint(expr= (5.27432353822418 - m.x213)**2 + (8.94703040209787 -
    m.x215)**2 + (6.2373757380993 - m.x217)**2 + (9.23461806871597 - m.x219)**2
    + 195.00222302105 * m.b99 <= 196.00222302105)
m.e182 = Constraint(expr= (0.996186045951476 - m.x213)**2 + (1.36457455477018
    - m.x215)**2 + (1.56471044095596 - m.x217)**2 + (3.36816773533039 - m.x219)
    **2 + 172.294180536922 * m.b100 <= 173.294180536922)
m.e183 = Constraint(expr= (4.02233509809877 - m.x213)**2 + (8.45745652401958 -
    m.x215)**2 + (9.01254148426443 - m.x217)**2 + (8.74685412361603 - m.x219)**
    2 + 229.407479988904 * m.b101 <= 230.407479988904)
m.e184 = Constraint(expr= (8.70857268900905 - m.x213)**2 + (1.11796994384596 -
    m.x215)**2 + (5.00432053303839 - m.x217)**2 + (2.40385817397397 - m.x219)**
    2 + 180.771322437022 * m.b102 <= 181.771322437022)
m.e185 = Constraint(expr= (7.54765700959199 - m.x213)**2 + (4.80143075267339 -
    m.x215)**2 + (8.40046817462899 - m.x217)**2 + (8.29113964786696 - m.x219)**
    2 + 152.663354968323 * m.b103 <= 153.663354968323)
m.e186 = Constraint(expr= (0.966865551002543 - m.x213)**2 + (9.92855620143344
    - m.x215)**2 + (5.74951319729978 - m.x217)**2 + (3.53637928232447 - m.x219)
    **2 + 188.008216290247 * m.b104 <= 189.008216290247)
m.e187 = Constraint(expr= (0.45538917132773 - m.x213)**2 + (1.48603663213761 -
    m.x215)**2 + (9.82188246465487 - m.x217)**2 + (7.4461736036308 - m.x219)**2
    + 245.091065242949 * m.b105 <= 246.091065242949)
m.e188 = Constraint(expr= (6.75415604579508 - m.x213)**2 + (4.56383909220998 -
    m.x215)**2 + (5.80815448731129 - m.x217)**2 + (1.39230685391611 - m.x219)**
    2 + 140.463739979998 * m.b106 <= 141.463739979998)
m.e189 = Constraint(expr= (8.85890029315383 - m.x213)**2 + (6.16141864425327 -
    m.x215)**2 + (2.25373679776979 - m.x217)**2 + (2.60508233041854 - m.x219)**
    2 + 199.511614429278 * m.b107 <= 200.511614429278)
m.e190 = Constraint(expr= (5.3549498366276 - m.x213)**2 + (6.5028620799581 -
    m.x215)**2 + (3.77860881416883 - m.x217)**2 + (3.88773754222155 - m.x219)**
    2 + 126.987839343492 * m.b108 <= 127.987839343492)
m.e191 = Constraint(expr= (0.113259012567859 - m.x213)**2 + (4.95866301539607
    - m.x215)**2 + (8.39278608004883 - m.x217)**2 + (2.33998997152253 - m.x219)
    **2 + 181.595796730204 * m.b109 <= 182.595796730204)
m.e192 = Constraint(expr= (4.01186017931937 - m.x213)**2 + (1.58505280271348 -
    m.x215)**2 + (6.66701704740187 - m.x217)**2 + (6.15579863983494 - m.x219)**
    2 + 140.650077775347 * m.b110 <= 141.650077775347)
m.e193 = Constraint(expr= (6.96869478428464 - m.x213)**2 + (4.10398909952988 -
    m.x215)**2 + (6.0102827867986 - m.x217)**2 + (2.74411959285283 - m.x219)**2
    + 129.582385211462 * m.b111 <= 130.582385211462)
m.e194 = Constraint(expr= (4.87285195085022 - m.x213)**2 + (9.86295765077007 -
    m.x215)**2 + (0.143489359365916 - m.x217)**2 + (8.80632332989694 - m.x219)
    **2 + 226.736334872871 * m.b112 <= 227.736334872871)
m.e195 = Constraint(expr= (7.83131209913544 - m.x213)**2 + (1.43609337392774 -
    m.x215)**2 + (3.30054263355244 - m.x217)**2 + (0.00125718557078214 - m.x219)
    **2 + 199.220071314074 * m.b113 <= 200.220071314074)
m.e196 = Constraint(expr= (5.66454764000128 - m.x213)**2 + (5.56331545204103 -
    m.x215)**2 + (1.14993711831163 - m.x217)**2 + (4.5715891663462 - m.x219)**2
    + 149.784254351217 * m.b114 <= 150.784254351217)
m.e197 = Constraint(expr= (3.33190103022031 - m.x213)**2 + (4.9445883792678 -
    m.x215)**2 + (7.30728727625694 - m.x217)**2 + (8.01246235442081 - m.x219)**
    2 + 146.896187485824 * m.b115 <= 147.896187485824)
m.e198 = Constraint(expr= (9.33298244503801 - m.x213)**2 + (0.723851580512842
    - m.x215)**2 + (8.42864317892565 - m.x217)**2 + (4.32119007374061 - m.x219)
    **2 + 219.90174536577 * m.b116 <= 220.90174536577)
m.e199 = Constraint(expr= (5.08063287228698 - m.x213)**2 + (8.38761519865226 -
    m.x215)**2 + (1.4027356086197 - m.x217)**2 + (6.86412480592018 - m.x219)**2
    + 164.06318777512 * m.b117 <= 165.06318777512)
m.e200 = Constraint(expr= (2.37234068047016 - m.x213)**2 + (7.05084260559812 -
    m.x215)**2 + (9.48571415448197 - m.x217)**2 + (5.77659906719162 - m.x219)**
    2 + 194.814503184848 * m.b118 <= 195.814503184848)
m.e201 = Constraint(expr= (4.16198173364841 - m.x213)**2 + (5.45114144772148 -
    m.x215)**2 + (9.00182905163397 - m.x217)**2 + (3.4826499770368 - m.x219)**2
    + 149.300564915884 * m.b119 <= 150.300564915884)
m.e202 = Constraint(expr= (4.45933786757702 - m.x213)**2 + (4.47805189258463 -
    m.x215)**2 + (6.61692822015399 - m.x217)**2 + (5.6343120215581 - m.x219)**2
    + 99.1502941148379 * m.b120 <= 100.150294114838)
m.e203 = Constraint(expr= m.b81 + m.b82 + m.b83 + m.b84 + m.b85 + m.b86 + m.b87
    + m.b88 + m.b89 + m.b90 + m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b96 +
    m.b97 + m.b98 + m.b99 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104 + m.b105
    + m.b106 + m.b107 + m.b108 + m.b109 + m.b110 + m.b111 + m.b112 + m.b113 +
    m.b114 + m.b115 + m.b116 + m.b117 + m.b118 + m.b119 + m.b120 == 1)
m.e204 = Constraint(expr= (4.04180710023322 - m.x221)**2 + (0.0638120906615358
    - m.x223)**2 + (9.31163964055327 - m.x225)**2 + (9.59399362610548 - m.x227)
    **2 + 247.918202243131 * m.b121 <= 248.918202243131)
m.e205 = Constraint(expr= (7.58630473662528 - m.x221)**2 + (9.81696808234314 -
    m.x223)**2 + (6.80594062551012 - m.x225)**2 + (5.73941560922778 - m.x227)**
    2 + 172.97632549661 * m.b122 <= 173.97632549661)
m.e206 = Constraint(expr= (4.73576208695481 - m.x221)**2 + (2.81737915136856 -
    m.x223)**2 + (0.919919756378161 - m.x225)**2 + (0.427396562561213 - m.x227)
    **2 + 192.870854266185 * m.b123 <= 193.870854266185)
m.e207 = Constraint(expr= (0.428853030190813 - m.x221)**2 + (5.71294529671424
    - m.x223)**2 + (2.06079707847737 - m.x225)**2 + (3.87755584734058 - m.x227)
    **2 + 168.997467410559 * m.b124 <= 169.997467410559)
m.e208 = Constraint(expr= (1.0774677742481 - m.x221)**2 + (0.802343324640142 -
    m.x223)**2 + (5.05560926630768 - m.x225)**2 + (6.38583388950109 - m.x227)**
    2 + 160.592363348786 * m.b125 <= 161.592363348786)
m.e209 = Constraint(expr= (1.12638621393495 - m.x221)**2 + (1.60465763780203 -
    m.x223)**2 + (4.07986801140447 - m.x225)**2 + (2.17037731980447 - m.x227)**
    2 + 165.579518594568 * m.b126 <= 166.579518594568)
m.e210 = Constraint(expr= (1.82688019388165 - m.x221)**2 + (4.63411239877442 -
    m.x223)**2 + (5.05145431164509 - m.x225)**2 + (3.74855986966667 - m.x227)**
    2 + 104.866109371321 * m.b127 <= 105.866109371321)
m.e211 = Constraint(expr= (8.44017389324234 - m.x221)**2 + (3.82403068466693 -
    m.x223)**2 + (8.92353737043929 - m.x225)**2 + (4.64273943517454 - m.x227)**
    2 + 167.587335871824 * m.b128 <= 168.587335871824)
m.e212 = Constraint(expr= (5.87176386853829 - m.x221)**2 + (1.44175632208916 -
    m.x223)**2 + (3.18165222878213 - m.x225)**2 + (5.19789554578514 - m.x227)**
    2 + 128.282182640462 * m.b129 <= 129.282182640462)
m.e213 = Constraint(expr= (6.76013297629122 - m.x221)**2 + (3.21254997009641 -
    m.x223)**2 + (9.46706727409796 - m.x225)**2 + (0.816604516799142 - m.x227)
    **2 + 226.736334872871 * m.b130 <= 227.736334872871)
m.e214 = Constraint(expr= (3.24901644799959 - m.x221)**2 + (7.51480516788174 -
    m.x223)**2 + (4.01508707364147 - m.x225)**2 + (4.50822439140953 - m.x227)**
    2 + 131.046642602757 * m.b131 <= 132.046642602757)
m.e215 = Constraint(expr= (0.388900076234485 - m.x221)**2 + (5.87163371055414
    - m.x223)**2 + (3.83580726436302 - m.x225)**2 + (3.02326353201313 - m.x227)
    **2 + 152.01486044439 * m.b132 <= 153.01486044439)
m.e216 = Constraint(expr= (0.790446136347066 - m.x221)**2 + (8.25540861746511
    - m.x223)**2 + (8.76325441282356 - m.x225)**2 + (3.16275732090416 - m.x227)
    **2 + 202.990878768535 * m.b133 <= 203.990878768535)
m.e217 = Constraint(expr= (2.24835841067941 - m.x221)**2 + (1.49328376014994 -
    m.x223)**2 + (6.05269717076173 - m.x225)**2 + (9.30035396512944 - m.x227)**
    2 + 187.279582970004 * m.b134 <= 188.279582970004)
m.e218 = Constraint(expr= (9.00506853532299 - m.x221)**2 + (4.84258207392989 -
    m.x223)**2 + (5.30242448190069 - m.x225)**2 + (1.96947429895047 - m.x227)**
    2 + 158.002379384289 * m.b135 <= 159.002379384289)
m.e219 = Constraint(expr= (7.06852474736736 - m.x221)**2 + (0.403068662414334
    - m.x223)**2 + (0.20219913526021 - m.x225)**2 + (1.72727050657669 - m.x227)
    **2 + 229.407479988904 * m.b136 <= 230.407479988904)
m.e220 = Constraint(expr= (2.04415436610942 - m.x221)**2 + (9.79340385699591 -
    m.x223)**2 + (1.37229670501157 - m.x225)**2 + (6.1403045098624 - m.x227)**2
    + 215.942963749551 * m.b137 <= 216.942963749551)
m.e221 = Constraint(expr= (7.57624032466962 - m.x221)**2 + (7.76217255967217 -
    m.x223)**2 + (0.355128375706556 - m.x225)**2 + (1.44611951386816 - m.x227)
    **2 + 247.918202243131 * m.b138 <= 248.918202243131)
m.e222 = Constraint(expr= (5.27432353822418 - m.x221)**2 + (8.94703040209787 -
    m.x223)**2 + (6.2373757380993 - m.x225)**2 + (9.23461806871597 - m.x227)**2
    + 195.00222302105 * m.b139 <= 196.00222302105)
m.e223 = Constraint(expr= (0.996186045951476 - m.x221)**2 + (1.36457455477018
    - m.x223)**2 + (1.56471044095596 - m.x225)**2 + (3.36816773533039 - m.x227)
    **2 + 172.294180536922 * m.b140 <= 173.294180536922)
m.e224 = Constraint(expr= (4.02233509809877 - m.x221)**2 + (8.45745652401958 -
    m.x223)**2 + (9.01254148426443 - m.x225)**2 + (8.74685412361603 - m.x227)**
    2 + 229.407479988904 * m.b141 <= 230.407479988904)
m.e225 = Constraint(expr= (8.70857268900905 - m.x221)**2 + (1.11796994384596 -
    m.x223)**2 + (5.00432053303839 - m.x225)**2 + (2.40385817397397 - m.x227)**
    2 + 180.771322437022 * m.b142 <= 181.771322437022)
m.e226 = Constraint(expr= (7.54765700959199 - m.x221)**2 + (4.80143075267339 -
    m.x223)**2 + (8.40046817462899 - m.x225)**2 + (8.29113964786696 - m.x227)**
    2 + 152.663354968323 * m.b143 <= 153.663354968323)
m.e227 = Constraint(expr= (0.966865551002543 - m.x221)**2 + (9.92855620143344
    - m.x223)**2 + (5.74951319729978 - m.x225)**2 + (3.53637928232447 - m.x227)
    **2 + 188.008216290247 * m.b144 <= 189.008216290247)
m.e228 = Constraint(expr= (0.45538917132773 - m.x221)**2 + (1.48603663213761 -
    m.x223)**2 + (9.82188246465487 - m.x225)**2 + (7.4461736036308 - m.x227)**2
    + 245.091065242949 * m.b145 <= 246.091065242949)
m.e229 = Constraint(expr= (6.75415604579508 - m.x221)**2 + (4.56383909220998 -
    m.x223)**2 + (5.80815448731129 - m.x225)**2 + (1.39230685391611 - m.x227)**
    2 + 140.463739979998 * m.b146 <= 141.463739979998)
m.e230 = Constraint(expr= (8.85890029315383 - m.x221)**2 + (6.16141864425327 -
    m.x223)**2 + (2.25373679776979 - m.x225)**2 + (2.60508233041854 - m.x227)**
    2 + 199.511614429278 * m.b147 <= 200.511614429278)
m.e231 = Constraint(expr= (5.3549498366276 - m.x221)**2 + (6.5028620799581 -
    m.x223)**2 + (3.77860881416883 - m.x225)**2 + (3.88773754222155 - m.x227)**
    2 + 126.987839343492 * m.b148 <= 127.987839343492)
m.e232 = Constraint(expr= (0.113259012567859 - m.x221)**2 + (4.95866301539607
    - m.x223)**2 + (8.39278608004883 - m.x225)**2 + (2.33998997152253 - m.x227)
    **2 + 181.595796730204 * m.b149 <= 182.595796730204)
m.e233 = Constraint(expr= (4.01186017931937 - m.x221)**2 + (1.58505280271348 -
    m.x223)**2 + (6.66701704740187 - m.x225)**2 + (6.15579863983494 - m.x227)**
    2 + 140.650077775347 * m.b150 <= 141.650077775347)
m.e234 = Constraint(expr= (6.96869478428464 - m.x221)**2 + (4.10398909952988 -
    m.x223)**2 + (6.0102827867986 - m.x225)**2 + (2.74411959285283 - m.x227)**2
    + 129.582385211462 * m.b151 <= 130.582385211462)
m.e235 = Constraint(expr= (4.87285195085022 - m.x221)**2 + (9.86295765077007 -
    m.x223)**2 + (0.143489359365916 - m.x225)**2 + (8.80632332989694 - m.x227)
    **2 + 226.736334872871 * m.b152 <= 227.736334872871)
m.e236 = Constraint(expr= (7.83131209913544 - m.x221)**2 + (1.43609337392774 -
    m.x223)**2 + (3.30054263355244 - m.x225)**2 + (0.00125718557078214 - m.x227)
    **2 + 199.220071314074 * m.b153 <= 200.220071314074)
m.e237 = Constraint(expr= (5.66454764000128 - m.x221)**2 + (5.56331545204103 -
    m.x223)**2 + (1.14993711831163 - m.x225)**2 + (4.5715891663462 - m.x227)**2
    + 149.784254351217 * m.b154 <= 150.784254351217)
m.e238 = Constraint(expr= (3.33190103022031 - m.x221)**2 + (4.9445883792678 -
    m.x223)**2 + (7.30728727625694 - m.x225)**2 + (8.01246235442081 - m.x227)**
    2 + 146.896187485824 * m.b155 <= 147.896187485824)
m.e239 = Constraint(expr= (9.33298244503801 - m.x221)**2 + (0.723851580512842
    - m.x223)**2 + (8.42864317892565 - m.x225)**2 + (4.32119007374061 - m.x227)
    **2 + 219.90174536577 * m.b156 <= 220.90174536577)
m.e240 = Constraint(expr= (5.08063287228698 - m.x221)**2 + (8.38761519865226 -
    m.x223)**2 + (1.4027356086197 - m.x225)**2 + (6.86412480592018 - m.x227)**2
    + 164.06318777512 * m.b157 <= 165.06318777512)
m.e241 = Constraint(expr= (2.37234068047016 - m.x221)**2 + (7.05084260559812 -
    m.x223)**2 + (9.48571415448197 - m.x225)**2 + (5.77659906719162 - m.x227)**
    2 + 194.814503184848 * m.b158 <= 195.814503184848)
m.e242 = Constraint(expr= (4.16198173364841 - m.x221)**2 + (5.45114144772148 -
    m.x223)**2 + (9.00182905163397 - m.x225)**2 + (3.4826499770368 - m.x227)**2
    + 149.300564915884 * m.b159 <= 150.300564915884)
m.e243 = Constraint(expr= (4.45933786757702 - m.x221)**2 + (4.47805189258463 -
    m.x223)**2 + (6.61692822015399 - m.x225)**2 + (5.6343120215581 - m.x227)**2
    + 99.1502941148379 * m.b160 <= 100.150294114838)
m.e244 = Constraint(expr= m.b121 + m.b122 + m.b123 + m.b124 + m.b125 + m.b126
    + m.b127 + m.b128 + m.b129 + m.b130 + m.b131 + m.b132 + m.b133 + m.b134 +
    m.b135 + m.b136 + m.b137 + m.b138 + m.b139 + m.b140 + m.b141 + m.b142 +
    m.b143 + m.b144 + m.b145 + m.b146 + m.b147 + m.b148 + m.b149 + m.b150 +
    m.b151 + m.b152 + m.b153 + m.b154 + m.b155 + m.b156 + m.b157 + m.b158 +
    m.b159 + m.b160 == 1)
m.e245 = Constraint(expr= (4.04180710023322 - m.x229)**2 + (0.0638120906615358
    - m.x231)**2 + (9.31163964055327 - m.x233)**2 + (9.59399362610548 - m.x235)
    **2 + 247.918202243131 * m.b161 <= 248.918202243131)
m.e246 = Constraint(expr= (7.58630473662528 - m.x229)**2 + (9.81696808234314 -
    m.x231)**2 + (6.80594062551012 - m.x233)**2 + (5.73941560922778 - m.x235)**
    2 + 172.97632549661 * m.b162 <= 173.97632549661)
m.e247 = Constraint(expr= (4.73576208695481 - m.x229)**2 + (2.81737915136856 -
    m.x231)**2 + (0.919919756378161 - m.x233)**2 + (0.427396562561213 - m.x235)
    **2 + 192.870854266185 * m.b163 <= 193.870854266185)
m.e248 = Constraint(expr= (0.428853030190813 - m.x229)**2 + (5.71294529671424
    - m.x231)**2 + (2.06079707847737 - m.x233)**2 + (3.87755584734058 - m.x235)
    **2 + 168.997467410559 * m.b164 <= 169.997467410559)
m.e249 = Constraint(expr= (1.0774677742481 - m.x229)**2 + (0.802343324640142 -
    m.x231)**2 + (5.05560926630768 - m.x233)**2 + (6.38583388950109 - m.x235)**
    2 + 160.592363348786 * m.b165 <= 161.592363348786)
m.e250 = Constraint(expr= (1.12638621393495 - m.x229)**2 + (1.60465763780203 -
    m.x231)**2 + (4.07986801140447 - m.x233)**2 + (2.17037731980447 - m.x235)**
    2 + 165.579518594568 * m.b166 <= 166.579518594568)
m.e251 = Constraint(expr= (1.82688019388165 - m.x229)**2 + (4.63411239877442 -
    m.x231)**2 + (5.05145431164509 - m.x233)**2 + (3.74855986966667 - m.x235)**
    2 + 104.866109371321 * m.b167 <= 105.866109371321)
m.e252 = Constraint(expr= (8.44017389324234 - m.x229)**2 + (3.82403068466693 -
    m.x231)**2 + (8.92353737043929 - m.x233)**2 + (4.64273943517454 - m.x235)**
    2 + 167.587335871824 * m.b168 <= 168.587335871824)
m.e253 = Constraint(expr= (5.87176386853829 - m.x229)**2 + (1.44175632208916 -
    m.x231)**2 + (3.18165222878213 - m.x233)**2 + (5.19789554578514 - m.x235)**
    2 + 128.282182640462 * m.b169 <= 129.282182640462)
m.e254 = Constraint(expr= (6.76013297629122 - m.x229)**2 + (3.21254997009641 -
    m.x231)**2 + (9.46706727409796 - m.x233)**2 + (0.816604516799142 - m.x235)
    **2 + 226.736334872871 * m.b170 <= 227.736334872871)
m.e255 = Constraint(expr= (3.24901644799959 - m.x229)**2 + (7.51480516788174 -
    m.x231)**2 + (4.01508707364147 - m.x233)**2 + (4.50822439140953 - m.x235)**
    2 + 131.046642602757 * m.b171 <= 132.046642602757)
m.e256 = Constraint(expr= (0.388900076234485 - m.x229)**2 + (5.87163371055414
    - m.x231)**2 + (3.83580726436302 - m.x233)**2 + (3.02326353201313 - m.x235)
    **2 + 152.01486044439 * m.b172 <= 153.01486044439)
m.e257 = Constraint(expr= (0.790446136347066 - m.x229)**2 + (8.25540861746511
    - m.x231)**2 + (8.76325441282356 - m.x233)**2 + (3.16275732090416 - m.x235)
    **2 + 202.990878768535 * m.b173 <= 203.990878768535)
m.e258 = Constraint(expr= (2.24835841067941 - m.x229)**2 + (1.49328376014994 -
    m.x231)**2 + (6.05269717076173 - m.x233)**2 + (9.30035396512944 - m.x235)**
    2 + 187.279582970004 * m.b174 <= 188.279582970004)
m.e259 = Constraint(expr= (9.00506853532299 - m.x229)**2 + (4.84258207392989 -
    m.x231)**2 + (5.30242448190069 - m.x233)**2 + (1.96947429895047 - m.x235)**
    2 + 158.002379384289 * m.b175 <= 159.002379384289)
m.e260 = Constraint(expr= (7.06852474736736 - m.x229)**2 + (0.403068662414334
    - m.x231)**2 + (0.20219913526021 - m.x233)**2 + (1.72727050657669 - m.x235)
    **2 + 229.407479988904 * m.b176 <= 230.407479988904)
m.e261 = Constraint(expr= (2.04415436610942 - m.x229)**2 + (9.79340385699591 -
    m.x231)**2 + (1.37229670501157 - m.x233)**2 + (6.1403045098624 - m.x235)**2
    + 215.942963749551 * m.b177 <= 216.942963749551)
m.e262 = Constraint(expr= (7.57624032466962 - m.x229)**2 + (7.76217255967217 -
    m.x231)**2 + (0.355128375706556 - m.x233)**2 + (1.44611951386816 - m.x235)
    **2 + 247.918202243131 * m.b178 <= 248.918202243131)
m.e263 = Constraint(expr= (5.27432353822418 - m.x229)**2 + (8.94703040209787 -
    m.x231)**2 + (6.2373757380993 - m.x233)**2 + (9.23461806871597 - m.x235)**2
    + 195.00222302105 * m.b179 <= 196.00222302105)
m.e264 = Constraint(expr= (0.996186045951476 - m.x229)**2 + (1.36457455477018
    - m.x231)**2 + (1.56471044095596 - m.x233)**2 + (3.36816773533039 - m.x235)
    **2 + 172.294180536922 * m.b180 <= 173.294180536922)
m.e265 = Constraint(expr= (4.02233509809877 - m.x229)**2 + (8.45745652401958 -
    m.x231)**2 + (9.01254148426443 - m.x233)**2 + (8.74685412361603 - m.x235)**
    2 + 229.407479988904 * m.b181 <= 230.407479988904)
m.e266 = Constraint(expr= (8.70857268900905 - m.x229)**2 + (1.11796994384596 -
    m.x231)**2 + (5.00432053303839 - m.x233)**2 + (2.40385817397397 - m.x235)**
    2 + 180.771322437022 * m.b182 <= 181.771322437022)
m.e267 = Constraint(expr= (7.54765700959199 - m.x229)**2 + (4.80143075267339 -
    m.x231)**2 + (8.40046817462899 - m.x233)**2 + (8.29113964786696 - m.x235)**
    2 + 152.663354968323 * m.b183 <= 153.663354968323)
m.e268 = Constraint(expr= (0.966865551002543 - m.x229)**2 + (9.92855620143344
    - m.x231)**2 + (5.74951319729978 - m.x233)**2 + (3.53637928232447 - m.x235)
    **2 + 188.008216290247 * m.b184 <= 189.008216290247)
m.e269 = Constraint(expr= (0.45538917132773 - m.x229)**2 + (1.48603663213761 -
    m.x231)**2 + (9.82188246465487 - m.x233)**2 + (7.4461736036308 - m.x235)**2
    + 245.091065242949 * m.b185 <= 246.091065242949)
m.e270 = Constraint(expr= (6.75415604579508 - m.x229)**2 + (4.56383909220998 -
    m.x231)**2 + (5.80815448731129 - m.x233)**2 + (1.39230685391611 - m.x235)**
    2 + 140.463739979998 * m.b186 <= 141.463739979998)
m.e271 = Constraint(expr= (8.85890029315383 - m.x229)**2 + (6.16141864425327 -
    m.x231)**2 + (2.25373679776979 - m.x233)**2 + (2.60508233041854 - m.x235)**
    2 + 199.511614429278 * m.b187 <= 200.511614429278)
m.e272 = Constraint(expr= (5.3549498366276 - m.x229)**2 + (6.5028620799581 -
    m.x231)**2 + (3.77860881416883 - m.x233)**2 + (3.88773754222155 - m.x235)**
    2 + 126.987839343492 * m.b188 <= 127.987839343492)
m.e273 = Constraint(expr= (0.113259012567859 - m.x229)**2 + (4.95866301539607
    - m.x231)**2 + (8.39278608004883 - m.x233)**2 + (2.33998997152253 - m.x235)
    **2 + 181.595796730204 * m.b189 <= 182.595796730204)
m.e274 = Constraint(expr= (4.01186017931937 - m.x229)**2 + (1.58505280271348 -
    m.x231)**2 + (6.66701704740187 - m.x233)**2 + (6.15579863983494 - m.x235)**
    2 + 140.650077775347 * m.b190 <= 141.650077775347)
m.e275 = Constraint(expr= (6.96869478428464 - m.x229)**2 + (4.10398909952988 -
    m.x231)**2 + (6.0102827867986 - m.x233)**2 + (2.74411959285283 - m.x235)**2
    + 129.582385211462 * m.b191 <= 130.582385211462)
m.e276 = Constraint(expr= (4.87285195085022 - m.x229)**2 + (9.86295765077007 -
    m.x231)**2 + (0.143489359365916 - m.x233)**2 + (8.80632332989694 - m.x235)
    **2 + 226.736334872871 * m.b192 <= 227.736334872871)
m.e277 = Constraint(expr= (7.83131209913544 - m.x229)**2 + (1.43609337392774 -
    m.x231)**2 + (3.30054263355244 - m.x233)**2 + (0.00125718557078214 - m.x235)
    **2 + 199.220071314074 * m.b193 <= 200.220071314074)
m.e278 = Constraint(expr= (5.66454764000128 - m.x229)**2 + (5.56331545204103 -
    m.x231)**2 + (1.14993711831163 - m.x233)**2 + (4.5715891663462 - m.x235)**2
    + 149.784254351217 * m.b194 <= 150.784254351217)
m.e279 = Constraint(expr= (3.33190103022031 - m.x229)**2 + (4.9445883792678 -
    m.x231)**2 + (7.30728727625694 - m.x233)**2 + (8.01246235442081 - m.x235)**
    2 + 146.896187485824 * m.b195 <= 147.896187485824)
m.e280 = Constraint(expr= (9.33298244503801 - m.x229)**2 + (0.723851580512842
    - m.x231)**2 + (8.42864317892565 - m.x233)**2 + (4.32119007374061 - m.x235)
    **2 + 219.90174536577 * m.b196 <= 220.90174536577)
m.e281 = Constraint(expr= (5.08063287228698 - m.x229)**2 + (8.38761519865226 -
    m.x231)**2 + (1.4027356086197 - m.x233)**2 + (6.86412480592018 - m.x235)**2
    + 164.06318777512 * m.b197 <= 165.06318777512)
m.e282 = Constraint(expr= (2.37234068047016 - m.x229)**2 + (7.05084260559812 -
    m.x231)**2 + (9.48571415448197 - m.x233)**2 + (5.77659906719162 - m.x235)**
    2 + 194.814503184848 * m.b198 <= 195.814503184848)
m.e283 = Constraint(expr= (4.16198173364841 - m.x229)**2 + (5.45114144772148 -
    m.x231)**2 + (9.00182905163397 - m.x233)**2 + (3.4826499770368 - m.x235)**2
    + 149.300564915884 * m.b199 <= 150.300564915884)
m.e284 = Constraint(expr= (4.45933786757702 - m.x229)**2 + (4.47805189258463 -
    m.x231)**2 + (6.61692822015399 - m.x233)**2 + (5.6343120215581 - m.x235)**2
    + 99.1502941148379 * m.b200 <= 100.150294114838)
m.e285 = Constraint(expr= m.b161 + m.b162 + m.b163 + m.b164 + m.b165 + m.b166
    + m.b167 + m.b168 + m.b169 + m.b170 + m.b171 + m.b172 + m.b173 + m.b174 +
    m.b175 + m.b176 + m.b177 + m.b178 + m.b179 + m.b180 + m.b181 + m.b182 +
    m.b183 + m.b184 + m.b185 + m.b186 + m.b187 + m.b188 + m.b189 + m.b190 +
    m.b191 + m.b192 + m.b193 + m.b194 + m.b195 + m.b196 + m.b197 + m.b198 +
    m.b199 + m.b200 == 1)
m.e286 = Constraint(expr= m.b1 + m.b41 + m.b81 + m.b121 + m.b161 <= 1)
m.e287 = Constraint(expr= m.b2 + m.b42 + m.b82 + m.b122 + m.b162 <= 1)
m.e288 = Constraint(expr= m.b3 + m.b43 + m.b83 + m.b123 + m.b163 <= 1)
m.e289 = Constraint(expr= m.b4 + m.b44 + m.b84 + m.b124 + m.b164 <= 1)
m.e290 = Constraint(expr= m.b5 + m.b45 + m.b85 + m.b125 + m.b165 <= 1)
m.e291 = Constraint(expr= m.b6 + m.b46 + m.b86 + m.b126 + m.b166 <= 1)
m.e292 = Constraint(expr= m.b7 + m.b47 + m.b87 + m.b127 + m.b167 <= 1)
m.e293 = Constraint(expr= m.b8 + m.b48 + m.b88 + m.b128 + m.b168 <= 1)
m.e294 = Constraint(expr= m.b9 + m.b49 + m.b89 + m.b129 + m.b169 <= 1)
m.e295 = Constraint(expr= m.b10 + m.b50 + m.b90 + m.b130 + m.b170 <= 1)
m.e296 = Constraint(expr= m.b11 + m.b51 + m.b91 + m.b131 + m.b171 <= 1)
m.e297 = Constraint(expr= m.b12 + m.b52 + m.b92 + m.b132 + m.b172 <= 1)
m.e298 = Constraint(expr= m.b13 + m.b53 + m.b93 + m.b133 + m.b173 <= 1)
m.e299 = Constraint(expr= m.b14 + m.b54 + m.b94 + m.b134 + m.b174 <= 1)
m.e300 = Constraint(expr= m.b15 + m.b55 + m.b95 + m.b135 + m.b175 <= 1)
m.e301 = Constraint(expr= m.b16 + m.b56 + m.b96 + m.b136 + m.b176 <= 1)
m.e302 = Constraint(expr= m.b17 + m.b57 + m.b97 + m.b137 + m.b177 <= 1)
m.e303 = Constraint(expr= m.b18 + m.b58 + m.b98 + m.b138 + m.b178 <= 1)
m.e304 = Constraint(expr= m.b19 + m.b59 + m.b99 + m.b139 + m.b179 <= 1)
m.e305 = Constraint(expr= m.b20 + m.b60 + m.b100 + m.b140 + m.b180 <= 1)
m.e306 = Constraint(expr= m.b21 + m.b61 + m.b101 + m.b141 + m.b181 <= 1)
m.e307 = Constraint(expr= m.b22 + m.b62 + m.b102 + m.b142 + m.b182 <= 1)
m.e308 = Constraint(expr= m.b23 + m.b63 + m.b103 + m.b143 + m.b183 <= 1)
m.e309 = Constraint(expr= m.b24 + m.b64 + m.b104 + m.b144 + m.b184 <= 1)
m.e310 = Constraint(expr= m.b25 + m.b65 + m.b105 + m.b145 + m.b185 <= 1)
m.e311 = Constraint(expr= m.b26 + m.b66 + m.b106 + m.b146 + m.b186 <= 1)
m.e312 = Constraint(expr= m.b27 + m.b67 + m.b107 + m.b147 + m.b187 <= 1)
m.e313 = Constraint(expr= m.b28 + m.b68 + m.b108 + m.b148 + m.b188 <= 1)
m.e314 = Constraint(expr= m.b29 + m.b69 + m.b109 + m.b149 + m.b189 <= 1)
m.e315 = Constraint(expr= m.b30 + m.b70 + m.b110 + m.b150 + m.b190 <= 1)
m.e316 = Constraint(expr= m.b31 + m.b71 + m.b111 + m.b151 + m.b191 <= 1)
m.e317 = Constraint(expr= m.b32 + m.b72 + m.b112 + m.b152 + m.b192 <= 1)
m.e318 = Constraint(expr= m.b33 + m.b73 + m.b113 + m.b153 + m.b193 <= 1)
m.e319 = Constraint(expr= m.b34 + m.b74 + m.b114 + m.b154 + m.b194 <= 1)
m.e320 = Constraint(expr= m.b35 + m.b75 + m.b115 + m.b155 + m.b195 <= 1)
m.e321 = Constraint(expr= m.b36 + m.b76 + m.b116 + m.b156 + m.b196 <= 1)
m.e322 = Constraint(expr= m.b37 + m.b77 + m.b117 + m.b157 + m.b197 <= 1)
m.e323 = Constraint(expr= m.b38 + m.b78 + m.b118 + m.b158 + m.b198 <= 1)
m.e324 = Constraint(expr= m.b39 + m.b79 + m.b119 + m.b159 + m.b199 <= 1)
m.e325 = Constraint(expr= m.b40 + m.b80 + m.b120 + m.b160 + m.b200 <= 1)
m.e326 = Constraint(expr= m.x201 - m.x202 <= 0)
m.e327 = Constraint(expr= m.x202 - m.x213 <= 0)
m.e328 = Constraint(expr= m.x213 - m.x221 <= 0)
m.e329 = Constraint(expr= m.x221 - m.x229 <= 0)
