# MINLP written by GAMS Convert at 05/07/21 17:13:01
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       309        5        0      304        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       245       45      200        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      1388      788      600
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

m.obj = Objective(sense=minimize, expr= m.x203 + m.x206 + m.x209 + m.x211 +
    m.x213 + m.x215 + m.x217 + m.x219 + m.x221 + m.x223 + m.x225 + m.x227 +
    m.x228 + m.x229 + m.x230 + m.x231 + m.x232 + m.x233 + m.x234 + m.x235 +
    m.x236 + m.x237 + m.x238 + m.x239 + m.x240 + m.x241 + m.x242 + m.x243 +
    m.x244 + m.x245)

m.e1 = Constraint(expr= m.x201 - m.x202 - m.x203 <= 0)
m.e2 = Constraint(expr= -m.x201 + m.x202 - m.x203 <= 0)
m.e3 = Constraint(expr= m.x204 - m.x205 - m.x206 <= 0)
m.e4 = Constraint(expr= -m.x204 + m.x205 - m.x206 <= 0)
m.e5 = Constraint(expr= m.x207 - m.x208 - m.x209 <= 0)
m.e6 = Constraint(expr= -m.x207 + m.x208 - m.x209 <= 0)
m.e7 = Constraint(expr= m.x201 - m.x210 - m.x211 <= 0)
m.e8 = Constraint(expr= -m.x201 + m.x210 - m.x211 <= 0)
m.e9 = Constraint(expr= m.x204 - m.x212 - m.x213 <= 0)
m.e10 = Constraint(expr= -m.x204 + m.x212 - m.x213 <= 0)
m.e11 = Constraint(expr= m.x207 - m.x214 - m.x215 <= 0)
m.e12 = Constraint(expr= -m.x207 + m.x214 - m.x215 <= 0)
m.e13 = Constraint(expr= m.x201 - m.x216 - m.x217 <= 0)
m.e14 = Constraint(expr= -m.x201 + m.x216 - m.x217 <= 0)
m.e15 = Constraint(expr= m.x204 - m.x218 - m.x219 <= 0)
m.e16 = Constraint(expr= -m.x204 + m.x218 - m.x219 <= 0)
m.e17 = Constraint(expr= m.x207 - m.x220 - m.x221 <= 0)
m.e18 = Constraint(expr= -m.x207 + m.x220 - m.x221 <= 0)
m.e19 = Constraint(expr= m.x201 - m.x222 - m.x223 <= 0)
m.e20 = Constraint(expr= -m.x201 + m.x222 - m.x223 <= 0)
m.e21 = Constraint(expr= m.x204 - m.x224 - m.x225 <= 0)
m.e22 = Constraint(expr= -m.x204 + m.x224 - m.x225 <= 0)
m.e23 = Constraint(expr= m.x207 - m.x226 - m.x227 <= 0)
m.e24 = Constraint(expr= -m.x207 + m.x226 - m.x227 <= 0)
m.e25 = Constraint(expr= m.x202 - m.x210 - m.x228 <= 0)
m.e26 = Constraint(expr= -m.x202 + m.x210 - m.x228 <= 0)
m.e27 = Constraint(expr= m.x205 - m.x212 - m.x229 <= 0)
m.e28 = Constraint(expr= -m.x205 + m.x212 - m.x229 <= 0)
m.e29 = Constraint(expr= m.x208 - m.x214 - m.x230 <= 0)
m.e30 = Constraint(expr= -m.x208 + m.x214 - m.x230 <= 0)
m.e31 = Constraint(expr= m.x202 - m.x216 - m.x231 <= 0)
m.e32 = Constraint(expr= -m.x202 + m.x216 - m.x231 <= 0)
m.e33 = Constraint(expr= m.x205 - m.x218 - m.x232 <= 0)
m.e34 = Constraint(expr= -m.x205 + m.x218 - m.x232 <= 0)
m.e35 = Constraint(expr= m.x208 - m.x220 - m.x233 <= 0)
m.e36 = Constraint(expr= -m.x208 + m.x220 - m.x233 <= 0)
m.e37 = Constraint(expr= m.x202 - m.x222 - m.x234 <= 0)
m.e38 = Constraint(expr= -m.x202 + m.x222 - m.x234 <= 0)
m.e39 = Constraint(expr= m.x205 - m.x224 - m.x235 <= 0)
m.e40 = Constraint(expr= -m.x205 + m.x224 - m.x235 <= 0)
m.e41 = Constraint(expr= m.x208 - m.x226 - m.x236 <= 0)
m.e42 = Constraint(expr= -m.x208 + m.x226 - m.x236 <= 0)
m.e43 = Constraint(expr= m.x210 - m.x216 - m.x237 <= 0)
m.e44 = Constraint(expr= -m.x210 + m.x216 - m.x237 <= 0)
m.e45 = Constraint(expr= m.x212 - m.x218 - m.x238 <= 0)
m.e46 = Constraint(expr= -m.x212 + m.x218 - m.x238 <= 0)
m.e47 = Constraint(expr= m.x214 - m.x220 - m.x239 <= 0)
m.e48 = Constraint(expr= -m.x214 + m.x220 - m.x239 <= 0)
m.e49 = Constraint(expr= m.x210 - m.x222 - m.x240 <= 0)
m.e50 = Constraint(expr= -m.x210 + m.x222 - m.x240 <= 0)
m.e51 = Constraint(expr= m.x212 - m.x224 - m.x241 <= 0)
m.e52 = Constraint(expr= -m.x212 + m.x224 - m.x241 <= 0)
m.e53 = Constraint(expr= m.x214 - m.x226 - m.x242 <= 0)
m.e54 = Constraint(expr= -m.x214 + m.x226 - m.x242 <= 0)
m.e55 = Constraint(expr= m.x216 - m.x222 - m.x243 <= 0)
m.e56 = Constraint(expr= -m.x216 + m.x222 - m.x243 <= 0)
m.e57 = Constraint(expr= m.x218 - m.x224 - m.x244 <= 0)
m.e58 = Constraint(expr= -m.x218 + m.x224 - m.x244 <= 0)
m.e59 = Constraint(expr= m.x220 - m.x226 - m.x245 <= 0)
m.e60 = Constraint(expr= -m.x220 + m.x226 - m.x245 <= 0)
m.e61 = Constraint(expr= (0.557503724665912 - m.x201)**2 + (6.89699967309171 -
    m.x204)**2 + (6.29939235997553 - m.x207)**2 + 139.882673685049 * m.b1
    <= 140.882673685049)
m.e62 = Constraint(expr= (3.39267738551004 - m.x201)**2 + (1.30003653355443 -
    m.x204)**2 + (1.26479284348393 - m.x207)**2 + 182.66284317326 * m.b2
    <= 183.66284317326)
m.e63 = Constraint(expr= (2.47527631721708 - m.x201)**2 + (3.36800564923427 -
    m.x204)**2 + (0.112146679619735 - m.x207)**2 + 174.174595766023 * m.b3
    <= 175.174595766023)
m.e64 = Constraint(expr= (4.23965937962997 - m.x201)**2 + (5.8354548549987 -
    m.x204)**2 + (5.21703959205437 - m.x207)**2 + 84.8069562114188 * m.b4
    <= 85.8069562114188)
m.e65 = Constraint(expr= (1.90787026471349 - m.x201)**2 + (5.05450580331505 -
    m.x204)**2 + (7.01165798298937 - m.x207)**2 + 105.666658166239 * m.b5
    <= 106.666658166239)
m.e66 = Constraint(expr= (9.92968197439359 - m.x201)**2 + (6.1106118319625 -
    m.x204)**2 + (4.29775190508136 - m.x207)**2 + 161.436709465448 * m.b6
    <= 162.436709465448)
m.e67 = Constraint(expr= (4.89615150940308 - m.x201)**2 + (9.57707230097383 -
    m.x204)**2 + (9.8722129175456 - m.x207)**2 + 224.632211642245 * m.b7
    <= 225.632211642245)
m.e68 = Constraint(expr= (5.20264655365834 - m.x201)**2 + (8.59934712303968 -
    m.x204)**2 + (4.8989755362197 - m.x207)**2 + 130.523019355742 * m.b8
    <= 131.523019355742)
m.e69 = Constraint(expr= (8.39650557858195 - m.x201)**2 + (6.50351197563982 -
    m.x204)**2 + (8.43657893923448 - m.x207)**2 + 194.220103883022 * m.b9
    <= 195.220103883022)
m.e70 = Constraint(expr= (7.9208870726961 - m.x201)**2 + (1.65574071738905 -
    m.x204)**2 + (8.95324220467027 - m.x207)**2 + 167.608109542354 * m.b10
    <= 168.608109542354)
m.e71 = Constraint(expr= (2.94356057833666 - m.x201)**2 + (9.50387320454974 -
    m.x204)**2 + (4.84216900165818 - m.x207)**2 + 155.944984455397 * m.b11
    <= 156.944984455397)
m.e72 = Constraint(expr= (5.67716909075113 - m.x201)**2 + (7.95494912869701 -
    m.x204)**2 + (1.8188252408716 - m.x207)**2 + 143.8265902598 * m.b12
    <= 144.8265902598)
m.e73 = Constraint(expr= (3.47632791977689 - m.x201)**2 + (9.89858036195079 -
    m.x204)**2 + (2.48936743461692 - m.x207)**2 + 187.205465302945 * m.b13
    <= 188.205465302945)
m.e74 = Constraint(expr= (7.19323345684947 - m.x201)**2 + (7.58674836824772 -
    m.x204)**2 + (4.37799217085148 - m.x207)**2 + 133.784100223376 * m.b14
    <= 134.784100223376)
m.e75 = Constraint(expr= (3.68794135627274 - m.x201)**2 + (0.764460460651244 -
    m.x204)**2 + (8.93159332921224 - m.x207)**2 + 161.150526627374 * m.b15
    <= 162.150526627374)
m.e76 = Constraint(expr= (6.09046032874766 - m.x201)**2 + (9.81520631625049 -
    m.x204)**2 + (8.68956765296896 - m.x207)**2 + 218.65758210219 * m.b16
    <= 219.65758210219)
m.e77 = Constraint(expr= (0.159435608071623 - m.x201)**2 + (7.8621329842116 -
    m.x204)**2 + (4.34112712391974 - m.x207)**2 + 176.061078593341 * m.b17
    <= 177.061078593341)
m.e78 = Constraint(expr= (9.30382494051085 - m.x201)**2 + (4.35265929316925 -
    m.x204)**2 + (9.41314719714275 - m.x207)**2 + 207.228588657402 * m.b18
    <= 208.228588657402)
m.e79 = Constraint(expr= (7.06044667279098 - m.x201)**2 + (0.119983022609481 -
    m.x204)**2 + (5.21799013159819 - m.x207)**2 + 187.373869370395 * m.b19
    <= 188.373869370395)
m.e80 = Constraint(expr= (1.28474203481519 - m.x201)**2 + (4.30839167378493 -
    m.x204)**2 + (5.07455099451718 - m.x207)**2 + 117.707087109112 * m.b20
    <= 118.707087109112)
m.e81 = Constraint(expr= (3.95046309105854 - m.x201)**2 + (7.84827364227855 -
    m.x204)**2 + (3.43912750809001 - m.x207)**2 + 131.403806640396 * m.b21
    <= 132.403806640396)
m.e82 = Constraint(expr= (8.86004297095793 - m.x201)**2 + (2.42401020162253 -
    m.x204)**2 + (6.97541890071488 - m.x207)**2 + 158.947259740156 * m.b22
    <= 159.947259740156)
m.e83 = Constraint(expr= (9.70133006466227 - m.x201)**2 + (2.47779846426131 -
    m.x204)**2 + (9.94553704882512 - m.x207)**2 + 214.875303499993 * m.b23
    <= 215.875303499993)
m.e84 = Constraint(expr= (1.26080108706515 - m.x201)**2 + (1.75121375015014 -
    m.x204)**2 + (9.30622186756532 - m.x207)**2 + 184.764129697819 * m.b24
    <= 185.764129697819)
m.e85 = Constraint(expr= (8.34389861976271 - m.x201)**2 + (0.398421020867703 -
    m.x204)**2 + (9.40468332550345 - m.x207)**2 + 200.398945392818 * m.b25
    <= 201.398945392818)
m.e86 = Constraint(expr= (0.458699783921438 - m.x201)**2 + (9.95271170285553 -
    m.x204)**2 + (9.87184681196407 - m.x207)**2 + 219.689414889155 * m.b26
    <= 220.689414889155)
m.e87 = Constraint(expr= (1.6117537168338 - m.x201)**2 + (6.32876332917705 -
    m.x204)**2 + (0.253813032788369 - m.x207)**2 + 200.5977121042 * m.b27
    <= 201.5977121042)
m.e88 = Constraint(expr= (3.46648532406983 - m.x201)**2 + (4.00972468964353 -
    m.x204)**2 + (3.47940856689719 - m.x207)**2 + 103.693060602793 * m.b28
    <= 104.693060602793)
m.e89 = Constraint(expr= (9.24571897700111 - m.x201)**2 + (0.559109940924647 -
    m.x204)**2 + (4.72143745016658 - m.x207)**2 + 219.689414889155 * m.b29
    <= 220.689414889155)
m.e90 = Constraint(expr= (1.80747416465249 - m.x201)**2 + (5.58858387120364 -
    m.x204)**2 + (8.71378289454331 - m.x207)**2 + 123.893230383562 * m.b30
    <= 124.893230383562)
m.e91 = Constraint(expr= (1.41393713125356 - m.x201)**2 + (7.94458518662143 -
    m.x204)**2 + (1.0952329046171 - m.x207)**2 + 203.494862154236 * m.b31
    <= 204.494862154236)
m.e92 = Constraint(expr= (7.85751206293337 - m.x201)**2 + (2.34992401729597 -
    m.x204)**2 + (5.94661276765362 - m.x207)**2 + 150.575463512564 * m.b32
    <= 151.575463512564)
m.e93 = Constraint(expr= (5.76996561939867 - m.x201)**2 + (3.13220421841133 -
    m.x204)**2 + (7.32413956683818 - m.x207)**2 + 106.602252199094 * m.b33
    <= 107.602252199094)
m.e94 = Constraint(expr= (5.03675100106706 - m.x201)**2 + (3.8492948064408 -
    m.x204)**2 + (8.26500796855089 - m.x207)**2 + 119.242421179142 * m.b34
    <= 120.242421179142)
m.e95 = Constraint(expr= (9.18783741616912 - m.x201)**2 + (2.86959611527789 -
    m.x204)**2 + (9.55868938722983 - m.x207)**2 + 198.559992859524 * m.b35
    <= 199.559992859524)
m.e96 = Constraint(expr= (9.72963694557713 - m.x201)**2 + (4.95412136849809 -
    m.x204)**2 + (7.88965319296968 - m.x207)**2 + 192.395482422753 * m.b36
    <= 193.395482422753)
m.e97 = Constraint(expr= (4.44990459463169 - m.x201)**2 + (7.37342841442893 -
    m.x204)**2 + (5.84940769948895 - m.x207)**2 + 114.723635769507 * m.b37
    <= 115.723635769507)
m.e98 = Constraint(expr= (0.453871807006551 - m.x201)**2 + (0.651328833092699
    - m.x204)**2 + (0.013848532114219 - m.x207)**2 + 224.632211642245 * m.b38
    <= 225.632211642245)
m.e99 = Constraint(expr= (7.68086203645083 - m.x201)**2 + (1.90461809371178 -
    m.x204)**2 + (2.73211644708798 - m.x207)**2 + 193.822989231709 * m.b39
    <= 194.822989231709)
m.e100 = Constraint(expr= (9.01196046905024 - m.x201)**2 + (8.86318587386137 -
    m.x204)**2 + (2.31734160055559 - m.x207)**2 + 184.764129697819 * m.b40
    <= 185.764129697819)
m.e101 = Constraint(expr= m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8
    + m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17 +
    m.b18 + m.b19 + m.b20 + m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 +
    m.b27 + m.b28 + m.b29 + m.b30 + m.b31 + m.b32 + m.b33 + m.b34 + m.b35 +
    m.b36 + m.b37 + m.b38 + m.b39 + m.b40 == 1)
m.e102 = Constraint(expr= (0.557503724665912 - m.x202)**2 + (6.89699967309171
    - m.x205)**2 + (6.29939235997553 - m.x208)**2 + 139.882673685049 * m.b41
    <= 140.882673685049)
m.e103 = Constraint(expr= (3.39267738551004 - m.x202)**2 + (1.30003653355443 -
    m.x205)**2 + (1.26479284348393 - m.x208)**2 + 182.66284317326 * m.b42
    <= 183.66284317326)
m.e104 = Constraint(expr= (2.47527631721708 - m.x202)**2 + (3.36800564923427 -
    m.x205)**2 + (0.112146679619735 - m.x208)**2 + 174.174595766023 * m.b43
    <= 175.174595766023)
m.e105 = Constraint(expr= (4.23965937962997 - m.x202)**2 + (5.8354548549987 -
    m.x205)**2 + (5.21703959205437 - m.x208)**2 + 84.8069562114188 * m.b44
    <= 85.8069562114188)
m.e106 = Constraint(expr= (1.90787026471349 - m.x202)**2 + (5.05450580331505 -
    m.x205)**2 + (7.01165798298937 - m.x208)**2 + 105.666658166239 * m.b45
    <= 106.666658166239)
m.e107 = Constraint(expr= (9.92968197439359 - m.x202)**2 + (6.1106118319625 -
    m.x205)**2 + (4.29775190508136 - m.x208)**2 + 161.436709465448 * m.b46
    <= 162.436709465448)
m.e108 = Constraint(expr= (4.89615150940308 - m.x202)**2 + (9.57707230097383 -
    m.x205)**2 + (9.8722129175456 - m.x208)**2 + 224.632211642245 * m.b47
    <= 225.632211642245)
m.e109 = Constraint(expr= (5.20264655365834 - m.x202)**2 + (8.59934712303968 -
    m.x205)**2 + (4.8989755362197 - m.x208)**2 + 130.523019355742 * m.b48
    <= 131.523019355742)
m.e110 = Constraint(expr= (8.39650557858195 - m.x202)**2 + (6.50351197563982 -
    m.x205)**2 + (8.43657893923448 - m.x208)**2 + 194.220103883022 * m.b49
    <= 195.220103883022)
m.e111 = Constraint(expr= (7.9208870726961 - m.x202)**2 + (1.65574071738905 -
    m.x205)**2 + (8.95324220467027 - m.x208)**2 + 167.608109542354 * m.b50
    <= 168.608109542354)
m.e112 = Constraint(expr= (2.94356057833666 - m.x202)**2 + (9.50387320454974 -
    m.x205)**2 + (4.84216900165818 - m.x208)**2 + 155.944984455397 * m.b51
    <= 156.944984455397)
m.e113 = Constraint(expr= (5.67716909075113 - m.x202)**2 + (7.95494912869701 -
    m.x205)**2 + (1.8188252408716 - m.x208)**2 + 143.8265902598 * m.b52
    <= 144.8265902598)
m.e114 = Constraint(expr= (3.47632791977689 - m.x202)**2 + (9.89858036195079 -
    m.x205)**2 + (2.48936743461692 - m.x208)**2 + 187.205465302945 * m.b53
    <= 188.205465302945)
m.e115 = Constraint(expr= (7.19323345684947 - m.x202)**2 + (7.58674836824772 -
    m.x205)**2 + (4.37799217085148 - m.x208)**2 + 133.784100223376 * m.b54
    <= 134.784100223376)
m.e116 = Constraint(expr= (3.68794135627274 - m.x202)**2 + (0.764460460651244
    - m.x205)**2 + (8.93159332921224 - m.x208)**2 + 161.150526627374 * m.b55
    <= 162.150526627374)
m.e117 = Constraint(expr= (6.09046032874766 - m.x202)**2 + (9.81520631625049 -
    m.x205)**2 + (8.68956765296896 - m.x208)**2 + 218.65758210219 * m.b56
    <= 219.65758210219)
m.e118 = Constraint(expr= (0.159435608071623 - m.x202)**2 + (7.8621329842116 -
    m.x205)**2 + (4.34112712391974 - m.x208)**2 + 176.061078593341 * m.b57
    <= 177.061078593341)
m.e119 = Constraint(expr= (9.30382494051085 - m.x202)**2 + (4.35265929316925 -
    m.x205)**2 + (9.41314719714275 - m.x208)**2 + 207.228588657402 * m.b58
    <= 208.228588657402)
m.e120 = Constraint(expr= (7.06044667279098 - m.x202)**2 + (0.119983022609481
    - m.x205)**2 + (5.21799013159819 - m.x208)**2 + 187.373869370395 * m.b59
    <= 188.373869370395)
m.e121 = Constraint(expr= (1.28474203481519 - m.x202)**2 + (4.30839167378493 -
    m.x205)**2 + (5.07455099451718 - m.x208)**2 + 117.707087109112 * m.b60
    <= 118.707087109112)
m.e122 = Constraint(expr= (3.95046309105854 - m.x202)**2 + (7.84827364227855 -
    m.x205)**2 + (3.43912750809001 - m.x208)**2 + 131.403806640396 * m.b61
    <= 132.403806640396)
m.e123 = Constraint(expr= (8.86004297095793 - m.x202)**2 + (2.42401020162253 -
    m.x205)**2 + (6.97541890071488 - m.x208)**2 + 158.947259740156 * m.b62
    <= 159.947259740156)
m.e124 = Constraint(expr= (9.70133006466227 - m.x202)**2 + (2.47779846426131 -
    m.x205)**2 + (9.94553704882512 - m.x208)**2 + 214.875303499993 * m.b63
    <= 215.875303499993)
m.e125 = Constraint(expr= (1.26080108706515 - m.x202)**2 + (1.75121375015014 -
    m.x205)**2 + (9.30622186756532 - m.x208)**2 + 184.764129697819 * m.b64
    <= 185.764129697819)
m.e126 = Constraint(expr= (8.34389861976271 - m.x202)**2 + (0.398421020867703
    - m.x205)**2 + (9.40468332550345 - m.x208)**2 + 200.398945392818 * m.b65
    <= 201.398945392818)
m.e127 = Constraint(expr= (0.458699783921438 - m.x202)**2 + (9.95271170285553
    - m.x205)**2 + (9.87184681196407 - m.x208)**2 + 219.689414889155 * m.b66
    <= 220.689414889155)
m.e128 = Constraint(expr= (1.6117537168338 - m.x202)**2 + (6.32876332917705 -
    m.x205)**2 + (0.253813032788369 - m.x208)**2 + 200.5977121042 * m.b67
    <= 201.5977121042)
m.e129 = Constraint(expr= (3.46648532406983 - m.x202)**2 + (4.00972468964353 -
    m.x205)**2 + (3.47940856689719 - m.x208)**2 + 103.693060602793 * m.b68
    <= 104.693060602793)
m.e130 = Constraint(expr= (9.24571897700111 - m.x202)**2 + (0.559109940924647
    - m.x205)**2 + (4.72143745016658 - m.x208)**2 + 219.689414889155 * m.b69
    <= 220.689414889155)
m.e131 = Constraint(expr= (1.80747416465249 - m.x202)**2 + (5.58858387120364 -
    m.x205)**2 + (8.71378289454331 - m.x208)**2 + 123.893230383562 * m.b70
    <= 124.893230383562)
m.e132 = Constraint(expr= (1.41393713125356 - m.x202)**2 + (7.94458518662143 -
    m.x205)**2 + (1.0952329046171 - m.x208)**2 + 203.494862154236 * m.b71
    <= 204.494862154236)
m.e133 = Constraint(expr= (7.85751206293337 - m.x202)**2 + (2.34992401729597 -
    m.x205)**2 + (5.94661276765362 - m.x208)**2 + 150.575463512564 * m.b72
    <= 151.575463512564)
m.e134 = Constraint(expr= (5.76996561939867 - m.x202)**2 + (3.13220421841133 -
    m.x205)**2 + (7.32413956683818 - m.x208)**2 + 106.602252199094 * m.b73
    <= 107.602252199094)
m.e135 = Constraint(expr= (5.03675100106706 - m.x202)**2 + (3.8492948064408 -
    m.x205)**2 + (8.26500796855089 - m.x208)**2 + 119.242421179142 * m.b74
    <= 120.242421179142)
m.e136 = Constraint(expr= (9.18783741616912 - m.x202)**2 + (2.86959611527789 -
    m.x205)**2 + (9.55868938722983 - m.x208)**2 + 198.559992859524 * m.b75
    <= 199.559992859524)
m.e137 = Constraint(expr= (9.72963694557713 - m.x202)**2 + (4.95412136849809 -
    m.x205)**2 + (7.88965319296968 - m.x208)**2 + 192.395482422753 * m.b76
    <= 193.395482422753)
m.e138 = Constraint(expr= (4.44990459463169 - m.x202)**2 + (7.37342841442893 -
    m.x205)**2 + (5.84940769948895 - m.x208)**2 + 114.723635769507 * m.b77
    <= 115.723635769507)
m.e139 = Constraint(expr= (0.453871807006551 - m.x202)**2 + (0.651328833092699
    - m.x205)**2 + (0.013848532114219 - m.x208)**2 + 224.632211642245 * m.b78
    <= 225.632211642245)
m.e140 = Constraint(expr= (7.68086203645083 - m.x202)**2 + (1.90461809371178 -
    m.x205)**2 + (2.73211644708798 - m.x208)**2 + 193.822989231709 * m.b79
    <= 194.822989231709)
m.e141 = Constraint(expr= (9.01196046905024 - m.x202)**2 + (8.86318587386137 -
    m.x205)**2 + (2.31734160055559 - m.x208)**2 + 184.764129697819 * m.b80
    <= 185.764129697819)
m.e142 = Constraint(expr= m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47
    + m.b48 + m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 +
    m.b57 + m.b58 + m.b59 + m.b60 + m.b61 + m.b62 + m.b63 + m.b64 + m.b65 +
    m.b66 + m.b67 + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 + m.b73 + m.b74 +
    m.b75 + m.b76 + m.b77 + m.b78 + m.b79 + m.b80 == 1)
m.e143 = Constraint(expr= (0.557503724665912 - m.x210)**2 + (6.89699967309171
    - m.x212)**2 + (6.29939235997553 - m.x214)**2 + 139.882673685049 * m.b81
    <= 140.882673685049)
m.e144 = Constraint(expr= (3.39267738551004 - m.x210)**2 + (1.30003653355443 -
    m.x212)**2 + (1.26479284348393 - m.x214)**2 + 182.66284317326 * m.b82
    <= 183.66284317326)
m.e145 = Constraint(expr= (2.47527631721708 - m.x210)**2 + (3.36800564923427 -
    m.x212)**2 + (0.112146679619735 - m.x214)**2 + 174.174595766023 * m.b83
    <= 175.174595766023)
m.e146 = Constraint(expr= (4.23965937962997 - m.x210)**2 + (5.8354548549987 -
    m.x212)**2 + (5.21703959205437 - m.x214)**2 + 84.8069562114188 * m.b84
    <= 85.8069562114188)
m.e147 = Constraint(expr= (1.90787026471349 - m.x210)**2 + (5.05450580331505 -
    m.x212)**2 + (7.01165798298937 - m.x214)**2 + 105.666658166239 * m.b85
    <= 106.666658166239)
m.e148 = Constraint(expr= (9.92968197439359 - m.x210)**2 + (6.1106118319625 -
    m.x212)**2 + (4.29775190508136 - m.x214)**2 + 161.436709465448 * m.b86
    <= 162.436709465448)
m.e149 = Constraint(expr= (4.89615150940308 - m.x210)**2 + (9.57707230097383 -
    m.x212)**2 + (9.8722129175456 - m.x214)**2 + 224.632211642245 * m.b87
    <= 225.632211642245)
m.e150 = Constraint(expr= (5.20264655365834 - m.x210)**2 + (8.59934712303968 -
    m.x212)**2 + (4.8989755362197 - m.x214)**2 + 130.523019355742 * m.b88
    <= 131.523019355742)
m.e151 = Constraint(expr= (8.39650557858195 - m.x210)**2 + (6.50351197563982 -
    m.x212)**2 + (8.43657893923448 - m.x214)**2 + 194.220103883022 * m.b89
    <= 195.220103883022)
m.e152 = Constraint(expr= (7.9208870726961 - m.x210)**2 + (1.65574071738905 -
    m.x212)**2 + (8.95324220467027 - m.x214)**2 + 167.608109542354 * m.b90
    <= 168.608109542354)
m.e153 = Constraint(expr= (2.94356057833666 - m.x210)**2 + (9.50387320454974 -
    m.x212)**2 + (4.84216900165818 - m.x214)**2 + 155.944984455397 * m.b91
    <= 156.944984455397)
m.e154 = Constraint(expr= (5.67716909075113 - m.x210)**2 + (7.95494912869701 -
    m.x212)**2 + (1.8188252408716 - m.x214)**2 + 143.8265902598 * m.b92
    <= 144.8265902598)
m.e155 = Constraint(expr= (3.47632791977689 - m.x210)**2 + (9.89858036195079 -
    m.x212)**2 + (2.48936743461692 - m.x214)**2 + 187.205465302945 * m.b93
    <= 188.205465302945)
m.e156 = Constraint(expr= (7.19323345684947 - m.x210)**2 + (7.58674836824772 -
    m.x212)**2 + (4.37799217085148 - m.x214)**2 + 133.784100223376 * m.b94
    <= 134.784100223376)
m.e157 = Constraint(expr= (3.68794135627274 - m.x210)**2 + (0.764460460651244
    - m.x212)**2 + (8.93159332921224 - m.x214)**2 + 161.150526627374 * m.b95
    <= 162.150526627374)
m.e158 = Constraint(expr= (6.09046032874766 - m.x210)**2 + (9.81520631625049 -
    m.x212)**2 + (8.68956765296896 - m.x214)**2 + 218.65758210219 * m.b96
    <= 219.65758210219)
m.e159 = Constraint(expr= (0.159435608071623 - m.x210)**2 + (7.8621329842116 -
    m.x212)**2 + (4.34112712391974 - m.x214)**2 + 176.061078593341 * m.b97
    <= 177.061078593341)
m.e160 = Constraint(expr= (9.30382494051085 - m.x210)**2 + (4.35265929316925 -
    m.x212)**2 + (9.41314719714275 - m.x214)**2 + 207.228588657402 * m.b98
    <= 208.228588657402)
m.e161 = Constraint(expr= (7.06044667279098 - m.x210)**2 + (0.119983022609481
    - m.x212)**2 + (5.21799013159819 - m.x214)**2 + 187.373869370395 * m.b99
    <= 188.373869370395)
m.e162 = Constraint(expr= (1.28474203481519 - m.x210)**2 + (4.30839167378493 -
    m.x212)**2 + (5.07455099451718 - m.x214)**2 + 117.707087109112 * m.b100
    <= 118.707087109112)
m.e163 = Constraint(expr= (3.95046309105854 - m.x210)**2 + (7.84827364227855 -
    m.x212)**2 + (3.43912750809001 - m.x214)**2 + 131.403806640396 * m.b101
    <= 132.403806640396)
m.e164 = Constraint(expr= (8.86004297095793 - m.x210)**2 + (2.42401020162253 -
    m.x212)**2 + (6.97541890071488 - m.x214)**2 + 158.947259740156 * m.b102
    <= 159.947259740156)
m.e165 = Constraint(expr= (9.70133006466227 - m.x210)**2 + (2.47779846426131 -
    m.x212)**2 + (9.94553704882512 - m.x214)**2 + 214.875303499993 * m.b103
    <= 215.875303499993)
m.e166 = Constraint(expr= (1.26080108706515 - m.x210)**2 + (1.75121375015014 -
    m.x212)**2 + (9.30622186756532 - m.x214)**2 + 184.764129697819 * m.b104
    <= 185.764129697819)
m.e167 = Constraint(expr= (8.34389861976271 - m.x210)**2 + (0.398421020867703
    - m.x212)**2 + (9.40468332550345 - m.x214)**2 + 200.398945392818 * m.b105
    <= 201.398945392818)
m.e168 = Constraint(expr= (0.458699783921438 - m.x210)**2 + (9.95271170285553
    - m.x212)**2 + (9.87184681196407 - m.x214)**2 + 219.689414889155 * m.b106
    <= 220.689414889155)
m.e169 = Constraint(expr= (1.6117537168338 - m.x210)**2 + (6.32876332917705 -
    m.x212)**2 + (0.253813032788369 - m.x214)**2 + 200.5977121042 * m.b107
    <= 201.5977121042)
m.e170 = Constraint(expr= (3.46648532406983 - m.x210)**2 + (4.00972468964353 -
    m.x212)**2 + (3.47940856689719 - m.x214)**2 + 103.693060602793 * m.b108
    <= 104.693060602793)
m.e171 = Constraint(expr= (9.24571897700111 - m.x210)**2 + (0.559109940924647
    - m.x212)**2 + (4.72143745016658 - m.x214)**2 + 219.689414889155 * m.b109
    <= 220.689414889155)
m.e172 = Constraint(expr= (1.80747416465249 - m.x210)**2 + (5.58858387120364 -
    m.x212)**2 + (8.71378289454331 - m.x214)**2 + 123.893230383562 * m.b110
    <= 124.893230383562)
m.e173 = Constraint(expr= (1.41393713125356 - m.x210)**2 + (7.94458518662143 -
    m.x212)**2 + (1.0952329046171 - m.x214)**2 + 203.494862154236 * m.b111
    <= 204.494862154236)
m.e174 = Constraint(expr= (7.85751206293337 - m.x210)**2 + (2.34992401729597 -
    m.x212)**2 + (5.94661276765362 - m.x214)**2 + 150.575463512564 * m.b112
    <= 151.575463512564)
m.e175 = Constraint(expr= (5.76996561939867 - m.x210)**2 + (3.13220421841133 -
    m.x212)**2 + (7.32413956683818 - m.x214)**2 + 106.602252199094 * m.b113
    <= 107.602252199094)
m.e176 = Constraint(expr= (5.03675100106706 - m.x210)**2 + (3.8492948064408 -
    m.x212)**2 + (8.26500796855089 - m.x214)**2 + 119.242421179142 * m.b114
    <= 120.242421179142)
m.e177 = Constraint(expr= (9.18783741616912 - m.x210)**2 + (2.86959611527789 -
    m.x212)**2 + (9.55868938722983 - m.x214)**2 + 198.559992859524 * m.b115
    <= 199.559992859524)
m.e178 = Constraint(expr= (9.72963694557713 - m.x210)**2 + (4.95412136849809 -
    m.x212)**2 + (7.88965319296968 - m.x214)**2 + 192.395482422753 * m.b116
    <= 193.395482422753)
m.e179 = Constraint(expr= (4.44990459463169 - m.x210)**2 + (7.37342841442893 -
    m.x212)**2 + (5.84940769948895 - m.x214)**2 + 114.723635769507 * m.b117
    <= 115.723635769507)
m.e180 = Constraint(expr= (0.453871807006551 - m.x210)**2 + (0.651328833092699
    - m.x212)**2 + (0.013848532114219 - m.x214)**2 + 224.632211642245 * m.b118
    <= 225.632211642245)
m.e181 = Constraint(expr= (7.68086203645083 - m.x210)**2 + (1.90461809371178 -
    m.x212)**2 + (2.73211644708798 - m.x214)**2 + 193.822989231709 * m.b119
    <= 194.822989231709)
m.e182 = Constraint(expr= (9.01196046905024 - m.x210)**2 + (8.86318587386137 -
    m.x212)**2 + (2.31734160055559 - m.x214)**2 + 184.764129697819 * m.b120
    <= 185.764129697819)
m.e183 = Constraint(expr= m.b81 + m.b82 + m.b83 + m.b84 + m.b85 + m.b86 + m.b87
    + m.b88 + m.b89 + m.b90 + m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b96 +
    m.b97 + m.b98 + m.b99 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104 + m.b105
    + m.b106 + m.b107 + m.b108 + m.b109 + m.b110 + m.b111 + m.b112 + m.b113 +
    m.b114 + m.b115 + m.b116 + m.b117 + m.b118 + m.b119 + m.b120 == 1)
m.e184 = Constraint(expr= (0.557503724665912 - m.x216)**2 + (6.89699967309171
    - m.x218)**2 + (6.29939235997553 - m.x220)**2 + 139.882673685049 * m.b121
    <= 140.882673685049)
m.e185 = Constraint(expr= (3.39267738551004 - m.x216)**2 + (1.30003653355443 -
    m.x218)**2 + (1.26479284348393 - m.x220)**2 + 182.66284317326 * m.b122
    <= 183.66284317326)
m.e186 = Constraint(expr= (2.47527631721708 - m.x216)**2 + (3.36800564923427 -
    m.x218)**2 + (0.112146679619735 - m.x220)**2 + 174.174595766023 * m.b123
    <= 175.174595766023)
m.e187 = Constraint(expr= (4.23965937962997 - m.x216)**2 + (5.8354548549987 -
    m.x218)**2 + (5.21703959205437 - m.x220)**2 + 84.8069562114188 * m.b124
    <= 85.8069562114188)
m.e188 = Constraint(expr= (1.90787026471349 - m.x216)**2 + (5.05450580331505 -
    m.x218)**2 + (7.01165798298937 - m.x220)**2 + 105.666658166239 * m.b125
    <= 106.666658166239)
m.e189 = Constraint(expr= (9.92968197439359 - m.x216)**2 + (6.1106118319625 -
    m.x218)**2 + (4.29775190508136 - m.x220)**2 + 161.436709465448 * m.b126
    <= 162.436709465448)
m.e190 = Constraint(expr= (4.89615150940308 - m.x216)**2 + (9.57707230097383 -
    m.x218)**2 + (9.8722129175456 - m.x220)**2 + 224.632211642245 * m.b127
    <= 225.632211642245)
m.e191 = Constraint(expr= (5.20264655365834 - m.x216)**2 + (8.59934712303968 -
    m.x218)**2 + (4.8989755362197 - m.x220)**2 + 130.523019355742 * m.b128
    <= 131.523019355742)
m.e192 = Constraint(expr= (8.39650557858195 - m.x216)**2 + (6.50351197563982 -
    m.x218)**2 + (8.43657893923448 - m.x220)**2 + 194.220103883022 * m.b129
    <= 195.220103883022)
m.e193 = Constraint(expr= (7.9208870726961 - m.x216)**2 + (1.65574071738905 -
    m.x218)**2 + (8.95324220467027 - m.x220)**2 + 167.608109542354 * m.b130
    <= 168.608109542354)
m.e194 = Constraint(expr= (2.94356057833666 - m.x216)**2 + (9.50387320454974 -
    m.x218)**2 + (4.84216900165818 - m.x220)**2 + 155.944984455397 * m.b131
    <= 156.944984455397)
m.e195 = Constraint(expr= (5.67716909075113 - m.x216)**2 + (7.95494912869701 -
    m.x218)**2 + (1.8188252408716 - m.x220)**2 + 143.8265902598 * m.b132
    <= 144.8265902598)
m.e196 = Constraint(expr= (3.47632791977689 - m.x216)**2 + (9.89858036195079 -
    m.x218)**2 + (2.48936743461692 - m.x220)**2 + 187.205465302945 * m.b133
    <= 188.205465302945)
m.e197 = Constraint(expr= (7.19323345684947 - m.x216)**2 + (7.58674836824772 -
    m.x218)**2 + (4.37799217085148 - m.x220)**2 + 133.784100223376 * m.b134
    <= 134.784100223376)
m.e198 = Constraint(expr= (3.68794135627274 - m.x216)**2 + (0.764460460651244
    - m.x218)**2 + (8.93159332921224 - m.x220)**2 + 161.150526627374 * m.b135
    <= 162.150526627374)
m.e199 = Constraint(expr= (6.09046032874766 - m.x216)**2 + (9.81520631625049 -
    m.x218)**2 + (8.68956765296896 - m.x220)**2 + 218.65758210219 * m.b136
    <= 219.65758210219)
m.e200 = Constraint(expr= (0.159435608071623 - m.x216)**2 + (7.8621329842116 -
    m.x218)**2 + (4.34112712391974 - m.x220)**2 + 176.061078593341 * m.b137
    <= 177.061078593341)
m.e201 = Constraint(expr= (9.30382494051085 - m.x216)**2 + (4.35265929316925 -
    m.x218)**2 + (9.41314719714275 - m.x220)**2 + 207.228588657402 * m.b138
    <= 208.228588657402)
m.e202 = Constraint(expr= (7.06044667279098 - m.x216)**2 + (0.119983022609481
    - m.x218)**2 + (5.21799013159819 - m.x220)**2 + 187.373869370395 * m.b139
    <= 188.373869370395)
m.e203 = Constraint(expr= (1.28474203481519 - m.x216)**2 + (4.30839167378493 -
    m.x218)**2 + (5.07455099451718 - m.x220)**2 + 117.707087109112 * m.b140
    <= 118.707087109112)
m.e204 = Constraint(expr= (3.95046309105854 - m.x216)**2 + (7.84827364227855 -
    m.x218)**2 + (3.43912750809001 - m.x220)**2 + 131.403806640396 * m.b141
    <= 132.403806640396)
m.e205 = Constraint(expr= (8.86004297095793 - m.x216)**2 + (2.42401020162253 -
    m.x218)**2 + (6.97541890071488 - m.x220)**2 + 158.947259740156 * m.b142
    <= 159.947259740156)
m.e206 = Constraint(expr= (9.70133006466227 - m.x216)**2 + (2.47779846426131 -
    m.x218)**2 + (9.94553704882512 - m.x220)**2 + 214.875303499993 * m.b143
    <= 215.875303499993)
m.e207 = Constraint(expr= (1.26080108706515 - m.x216)**2 + (1.75121375015014 -
    m.x218)**2 + (9.30622186756532 - m.x220)**2 + 184.764129697819 * m.b144
    <= 185.764129697819)
m.e208 = Constraint(expr= (8.34389861976271 - m.x216)**2 + (0.398421020867703
    - m.x218)**2 + (9.40468332550345 - m.x220)**2 + 200.398945392818 * m.b145
    <= 201.398945392818)
m.e209 = Constraint(expr= (0.458699783921438 - m.x216)**2 + (9.95271170285553
    - m.x218)**2 + (9.87184681196407 - m.x220)**2 + 219.689414889155 * m.b146
    <= 220.689414889155)
m.e210 = Constraint(expr= (1.6117537168338 - m.x216)**2 + (6.32876332917705 -
    m.x218)**2 + (0.253813032788369 - m.x220)**2 + 200.5977121042 * m.b147
    <= 201.5977121042)
m.e211 = Constraint(expr= (3.46648532406983 - m.x216)**2 + (4.00972468964353 -
    m.x218)**2 + (3.47940856689719 - m.x220)**2 + 103.693060602793 * m.b148
    <= 104.693060602793)
m.e212 = Constraint(expr= (9.24571897700111 - m.x216)**2 + (0.559109940924647
    - m.x218)**2 + (4.72143745016658 - m.x220)**2 + 219.689414889155 * m.b149
    <= 220.689414889155)
m.e213 = Constraint(expr= (1.80747416465249 - m.x216)**2 + (5.58858387120364 -
    m.x218)**2 + (8.71378289454331 - m.x220)**2 + 123.893230383562 * m.b150
    <= 124.893230383562)
m.e214 = Constraint(expr= (1.41393713125356 - m.x216)**2 + (7.94458518662143 -
    m.x218)**2 + (1.0952329046171 - m.x220)**2 + 203.494862154236 * m.b151
    <= 204.494862154236)
m.e215 = Constraint(expr= (7.85751206293337 - m.x216)**2 + (2.34992401729597 -
    m.x218)**2 + (5.94661276765362 - m.x220)**2 + 150.575463512564 * m.b152
    <= 151.575463512564)
m.e216 = Constraint(expr= (5.76996561939867 - m.x216)**2 + (3.13220421841133 -
    m.x218)**2 + (7.32413956683818 - m.x220)**2 + 106.602252199094 * m.b153
    <= 107.602252199094)
m.e217 = Constraint(expr= (5.03675100106706 - m.x216)**2 + (3.8492948064408 -
    m.x218)**2 + (8.26500796855089 - m.x220)**2 + 119.242421179142 * m.b154
    <= 120.242421179142)
m.e218 = Constraint(expr= (9.18783741616912 - m.x216)**2 + (2.86959611527789 -
    m.x218)**2 + (9.55868938722983 - m.x220)**2 + 198.559992859524 * m.b155
    <= 199.559992859524)
m.e219 = Constraint(expr= (9.72963694557713 - m.x216)**2 + (4.95412136849809 -
    m.x218)**2 + (7.88965319296968 - m.x220)**2 + 192.395482422753 * m.b156
    <= 193.395482422753)
m.e220 = Constraint(expr= (4.44990459463169 - m.x216)**2 + (7.37342841442893 -
    m.x218)**2 + (5.84940769948895 - m.x220)**2 + 114.723635769507 * m.b157
    <= 115.723635769507)
m.e221 = Constraint(expr= (0.453871807006551 - m.x216)**2 + (0.651328833092699
    - m.x218)**2 + (0.013848532114219 - m.x220)**2 + 224.632211642245 * m.b158
    <= 225.632211642245)
m.e222 = Constraint(expr= (7.68086203645083 - m.x216)**2 + (1.90461809371178 -
    m.x218)**2 + (2.73211644708798 - m.x220)**2 + 193.822989231709 * m.b159
    <= 194.822989231709)
m.e223 = Constraint(expr= (9.01196046905024 - m.x216)**2 + (8.86318587386137 -
    m.x218)**2 + (2.31734160055559 - m.x220)**2 + 184.764129697819 * m.b160
    <= 185.764129697819)
m.e224 = Constraint(expr= m.b121 + m.b122 + m.b123 + m.b124 + m.b125 + m.b126
    + m.b127 + m.b128 + m.b129 + m.b130 + m.b131 + m.b132 + m.b133 + m.b134 +
    m.b135 + m.b136 + m.b137 + m.b138 + m.b139 + m.b140 + m.b141 + m.b142 +
    m.b143 + m.b144 + m.b145 + m.b146 + m.b147 + m.b148 + m.b149 + m.b150 +
    m.b151 + m.b152 + m.b153 + m.b154 + m.b155 + m.b156 + m.b157 + m.b158 +
    m.b159 + m.b160 == 1)
m.e225 = Constraint(expr= (0.557503724665912 - m.x222)**2 + (6.89699967309171
    - m.x224)**2 + (6.29939235997553 - m.x226)**2 + 139.882673685049 * m.b161
    <= 140.882673685049)
m.e226 = Constraint(expr= (3.39267738551004 - m.x222)**2 + (1.30003653355443 -
    m.x224)**2 + (1.26479284348393 - m.x226)**2 + 182.66284317326 * m.b162
    <= 183.66284317326)
m.e227 = Constraint(expr= (2.47527631721708 - m.x222)**2 + (3.36800564923427 -
    m.x224)**2 + (0.112146679619735 - m.x226)**2 + 174.174595766023 * m.b163
    <= 175.174595766023)
m.e228 = Constraint(expr= (4.23965937962997 - m.x222)**2 + (5.8354548549987 -
    m.x224)**2 + (5.21703959205437 - m.x226)**2 + 84.8069562114188 * m.b164
    <= 85.8069562114188)
m.e229 = Constraint(expr= (1.90787026471349 - m.x222)**2 + (5.05450580331505 -
    m.x224)**2 + (7.01165798298937 - m.x226)**2 + 105.666658166239 * m.b165
    <= 106.666658166239)
m.e230 = Constraint(expr= (9.92968197439359 - m.x222)**2 + (6.1106118319625 -
    m.x224)**2 + (4.29775190508136 - m.x226)**2 + 161.436709465448 * m.b166
    <= 162.436709465448)
m.e231 = Constraint(expr= (4.89615150940308 - m.x222)**2 + (9.57707230097383 -
    m.x224)**2 + (9.8722129175456 - m.x226)**2 + 224.632211642245 * m.b167
    <= 225.632211642245)
m.e232 = Constraint(expr= (5.20264655365834 - m.x222)**2 + (8.59934712303968 -
    m.x224)**2 + (4.8989755362197 - m.x226)**2 + 130.523019355742 * m.b168
    <= 131.523019355742)
m.e233 = Constraint(expr= (8.39650557858195 - m.x222)**2 + (6.50351197563982 -
    m.x224)**2 + (8.43657893923448 - m.x226)**2 + 194.220103883022 * m.b169
    <= 195.220103883022)
m.e234 = Constraint(expr= (7.9208870726961 - m.x222)**2 + (1.65574071738905 -
    m.x224)**2 + (8.95324220467027 - m.x226)**2 + 167.608109542354 * m.b170
    <= 168.608109542354)
m.e235 = Constraint(expr= (2.94356057833666 - m.x222)**2 + (9.50387320454974 -
    m.x224)**2 + (4.84216900165818 - m.x226)**2 + 155.944984455397 * m.b171
    <= 156.944984455397)
m.e236 = Constraint(expr= (5.67716909075113 - m.x222)**2 + (7.95494912869701 -
    m.x224)**2 + (1.8188252408716 - m.x226)**2 + 143.8265902598 * m.b172
    <= 144.8265902598)
m.e237 = Constraint(expr= (3.47632791977689 - m.x222)**2 + (9.89858036195079 -
    m.x224)**2 + (2.48936743461692 - m.x226)**2 + 187.205465302945 * m.b173
    <= 188.205465302945)
m.e238 = Constraint(expr= (7.19323345684947 - m.x222)**2 + (7.58674836824772 -
    m.x224)**2 + (4.37799217085148 - m.x226)**2 + 133.784100223376 * m.b174
    <= 134.784100223376)
m.e239 = Constraint(expr= (3.68794135627274 - m.x222)**2 + (0.764460460651244
    - m.x224)**2 + (8.93159332921224 - m.x226)**2 + 161.150526627374 * m.b175
    <= 162.150526627374)
m.e240 = Constraint(expr= (6.09046032874766 - m.x222)**2 + (9.81520631625049 -
    m.x224)**2 + (8.68956765296896 - m.x226)**2 + 218.65758210219 * m.b176
    <= 219.65758210219)
m.e241 = Constraint(expr= (0.159435608071623 - m.x222)**2 + (7.8621329842116 -
    m.x224)**2 + (4.34112712391974 - m.x226)**2 + 176.061078593341 * m.b177
    <= 177.061078593341)
m.e242 = Constraint(expr= (9.30382494051085 - m.x222)**2 + (4.35265929316925 -
    m.x224)**2 + (9.41314719714275 - m.x226)**2 + 207.228588657402 * m.b178
    <= 208.228588657402)
m.e243 = Constraint(expr= (7.06044667279098 - m.x222)**2 + (0.119983022609481
    - m.x224)**2 + (5.21799013159819 - m.x226)**2 + 187.373869370395 * m.b179
    <= 188.373869370395)
m.e244 = Constraint(expr= (1.28474203481519 - m.x222)**2 + (4.30839167378493 -
    m.x224)**2 + (5.07455099451718 - m.x226)**2 + 117.707087109112 * m.b180
    <= 118.707087109112)
m.e245 = Constraint(expr= (3.95046309105854 - m.x222)**2 + (7.84827364227855 -
    m.x224)**2 + (3.43912750809001 - m.x226)**2 + 131.403806640396 * m.b181
    <= 132.403806640396)
m.e246 = Constraint(expr= (8.86004297095793 - m.x222)**2 + (2.42401020162253 -
    m.x224)**2 + (6.97541890071488 - m.x226)**2 + 158.947259740156 * m.b182
    <= 159.947259740156)
m.e247 = Constraint(expr= (9.70133006466227 - m.x222)**2 + (2.47779846426131 -
    m.x224)**2 + (9.94553704882512 - m.x226)**2 + 214.875303499993 * m.b183
    <= 215.875303499993)
m.e248 = Constraint(expr= (1.26080108706515 - m.x222)**2 + (1.75121375015014 -
    m.x224)**2 + (9.30622186756532 - m.x226)**2 + 184.764129697819 * m.b184
    <= 185.764129697819)
m.e249 = Constraint(expr= (8.34389861976271 - m.x222)**2 + (0.398421020867703
    - m.x224)**2 + (9.40468332550345 - m.x226)**2 + 200.398945392818 * m.b185
    <= 201.398945392818)
m.e250 = Constraint(expr= (0.458699783921438 - m.x222)**2 + (9.95271170285553
    - m.x224)**2 + (9.87184681196407 - m.x226)**2 + 219.689414889155 * m.b186
    <= 220.689414889155)
m.e251 = Constraint(expr= (1.6117537168338 - m.x222)**2 + (6.32876332917705 -
    m.x224)**2 + (0.253813032788369 - m.x226)**2 + 200.5977121042 * m.b187
    <= 201.5977121042)
m.e252 = Constraint(expr= (3.46648532406983 - m.x222)**2 + (4.00972468964353 -
    m.x224)**2 + (3.47940856689719 - m.x226)**2 + 103.693060602793 * m.b188
    <= 104.693060602793)
m.e253 = Constraint(expr= (9.24571897700111 - m.x222)**2 + (0.559109940924647
    - m.x224)**2 + (4.72143745016658 - m.x226)**2 + 219.689414889155 * m.b189
    <= 220.689414889155)
m.e254 = Constraint(expr= (1.80747416465249 - m.x222)**2 + (5.58858387120364 -
    m.x224)**2 + (8.71378289454331 - m.x226)**2 + 123.893230383562 * m.b190
    <= 124.893230383562)
m.e255 = Constraint(expr= (1.41393713125356 - m.x222)**2 + (7.94458518662143 -
    m.x224)**2 + (1.0952329046171 - m.x226)**2 + 203.494862154236 * m.b191
    <= 204.494862154236)
m.e256 = Constraint(expr= (7.85751206293337 - m.x222)**2 + (2.34992401729597 -
    m.x224)**2 + (5.94661276765362 - m.x226)**2 + 150.575463512564 * m.b192
    <= 151.575463512564)
m.e257 = Constraint(expr= (5.76996561939867 - m.x222)**2 + (3.13220421841133 -
    m.x224)**2 + (7.32413956683818 - m.x226)**2 + 106.602252199094 * m.b193
    <= 107.602252199094)
m.e258 = Constraint(expr= (5.03675100106706 - m.x222)**2 + (3.8492948064408 -
    m.x224)**2 + (8.26500796855089 - m.x226)**2 + 119.242421179142 * m.b194
    <= 120.242421179142)
m.e259 = Constraint(expr= (9.18783741616912 - m.x222)**2 + (2.86959611527789 -
    m.x224)**2 + (9.55868938722983 - m.x226)**2 + 198.559992859524 * m.b195
    <= 199.559992859524)
m.e260 = Constraint(expr= (9.72963694557713 - m.x222)**2 + (4.95412136849809 -
    m.x224)**2 + (7.88965319296968 - m.x226)**2 + 192.395482422753 * m.b196
    <= 193.395482422753)
m.e261 = Constraint(expr= (4.44990459463169 - m.x222)**2 + (7.37342841442893 -
    m.x224)**2 + (5.84940769948895 - m.x226)**2 + 114.723635769507 * m.b197
    <= 115.723635769507)
m.e262 = Constraint(expr= (0.453871807006551 - m.x222)**2 + (0.651328833092699
    - m.x224)**2 + (0.013848532114219 - m.x226)**2 + 224.632211642245 * m.b198
    <= 225.632211642245)
m.e263 = Constraint(expr= (7.68086203645083 - m.x222)**2 + (1.90461809371178 -
    m.x224)**2 + (2.73211644708798 - m.x226)**2 + 193.822989231709 * m.b199
    <= 194.822989231709)
m.e264 = Constraint(expr= (9.01196046905024 - m.x222)**2 + (8.86318587386137 -
    m.x224)**2 + (2.31734160055559 - m.x226)**2 + 184.764129697819 * m.b200
    <= 185.764129697819)
m.e265 = Constraint(expr= m.b161 + m.b162 + m.b163 + m.b164 + m.b165 + m.b166
    + m.b167 + m.b168 + m.b169 + m.b170 + m.b171 + m.b172 + m.b173 + m.b174 +
    m.b175 + m.b176 + m.b177 + m.b178 + m.b179 + m.b180 + m.b181 + m.b182 +
    m.b183 + m.b184 + m.b185 + m.b186 + m.b187 + m.b188 + m.b189 + m.b190 +
    m.b191 + m.b192 + m.b193 + m.b194 + m.b195 + m.b196 + m.b197 + m.b198 +
    m.b199 + m.b200 == 1)
m.e266 = Constraint(expr= m.b1 + m.b41 + m.b81 + m.b121 + m.b161 <= 1)
m.e267 = Constraint(expr= m.b2 + m.b42 + m.b82 + m.b122 + m.b162 <= 1)
m.e268 = Constraint(expr= m.b3 + m.b43 + m.b83 + m.b123 + m.b163 <= 1)
m.e269 = Constraint(expr= m.b4 + m.b44 + m.b84 + m.b124 + m.b164 <= 1)
m.e270 = Constraint(expr= m.b5 + m.b45 + m.b85 + m.b125 + m.b165 <= 1)
m.e271 = Constraint(expr= m.b6 + m.b46 + m.b86 + m.b126 + m.b166 <= 1)
m.e272 = Constraint(expr= m.b7 + m.b47 + m.b87 + m.b127 + m.b167 <= 1)
m.e273 = Constraint(expr= m.b8 + m.b48 + m.b88 + m.b128 + m.b168 <= 1)
m.e274 = Constraint(expr= m.b9 + m.b49 + m.b89 + m.b129 + m.b169 <= 1)
m.e275 = Constraint(expr= m.b10 + m.b50 + m.b90 + m.b130 + m.b170 <= 1)
m.e276 = Constraint(expr= m.b11 + m.b51 + m.b91 + m.b131 + m.b171 <= 1)
m.e277 = Constraint(expr= m.b12 + m.b52 + m.b92 + m.b132 + m.b172 <= 1)
m.e278 = Constraint(expr= m.b13 + m.b53 + m.b93 + m.b133 + m.b173 <= 1)
m.e279 = Constraint(expr= m.b14 + m.b54 + m.b94 + m.b134 + m.b174 <= 1)
m.e280 = Constraint(expr= m.b15 + m.b55 + m.b95 + m.b135 + m.b175 <= 1)
m.e281 = Constraint(expr= m.b16 + m.b56 + m.b96 + m.b136 + m.b176 <= 1)
m.e282 = Constraint(expr= m.b17 + m.b57 + m.b97 + m.b137 + m.b177 <= 1)
m.e283 = Constraint(expr= m.b18 + m.b58 + m.b98 + m.b138 + m.b178 <= 1)
m.e284 = Constraint(expr= m.b19 + m.b59 + m.b99 + m.b139 + m.b179 <= 1)
m.e285 = Constraint(expr= m.b20 + m.b60 + m.b100 + m.b140 + m.b180 <= 1)
m.e286 = Constraint(expr= m.b21 + m.b61 + m.b101 + m.b141 + m.b181 <= 1)
m.e287 = Constraint(expr= m.b22 + m.b62 + m.b102 + m.b142 + m.b182 <= 1)
m.e288 = Constraint(expr= m.b23 + m.b63 + m.b103 + m.b143 + m.b183 <= 1)
m.e289 = Constraint(expr= m.b24 + m.b64 + m.b104 + m.b144 + m.b184 <= 1)
m.e290 = Constraint(expr= m.b25 + m.b65 + m.b105 + m.b145 + m.b185 <= 1)
m.e291 = Constraint(expr= m.b26 + m.b66 + m.b106 + m.b146 + m.b186 <= 1)
m.e292 = Constraint(expr= m.b27 + m.b67 + m.b107 + m.b147 + m.b187 <= 1)
m.e293 = Constraint(expr= m.b28 + m.b68 + m.b108 + m.b148 + m.b188 <= 1)
m.e294 = Constraint(expr= m.b29 + m.b69 + m.b109 + m.b149 + m.b189 <= 1)
m.e295 = Constraint(expr= m.b30 + m.b70 + m.b110 + m.b150 + m.b190 <= 1)
m.e296 = Constraint(expr= m.b31 + m.b71 + m.b111 + m.b151 + m.b191 <= 1)
m.e297 = Constraint(expr= m.b32 + m.b72 + m.b112 + m.b152 + m.b192 <= 1)
m.e298 = Constraint(expr= m.b33 + m.b73 + m.b113 + m.b153 + m.b193 <= 1)
m.e299 = Constraint(expr= m.b34 + m.b74 + m.b114 + m.b154 + m.b194 <= 1)
m.e300 = Constraint(expr= m.b35 + m.b75 + m.b115 + m.b155 + m.b195 <= 1)
m.e301 = Constraint(expr= m.b36 + m.b76 + m.b116 + m.b156 + m.b196 <= 1)
m.e302 = Constraint(expr= m.b37 + m.b77 + m.b117 + m.b157 + m.b197 <= 1)
m.e303 = Constraint(expr= m.b38 + m.b78 + m.b118 + m.b158 + m.b198 <= 1)
m.e304 = Constraint(expr= m.b39 + m.b79 + m.b119 + m.b159 + m.b199 <= 1)
m.e305 = Constraint(expr= m.b40 + m.b80 + m.b120 + m.b160 + m.b200 <= 1)
m.e306 = Constraint(expr= m.x201 - m.x202 <= 0)
m.e307 = Constraint(expr= m.x202 - m.x210 <= 0)
m.e308 = Constraint(expr= m.x210 - m.x216 <= 0)
m.e309 = Constraint(expr= m.x216 - m.x222 <= 0)
