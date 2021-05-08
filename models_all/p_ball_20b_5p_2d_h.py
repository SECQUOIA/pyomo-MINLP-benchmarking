# MINLP written by GAMS Convert at 05/07/21 17:13:00
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       379       15        0      364        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       330      230      100        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      1238      938      300
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
m.x256 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x257 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x258 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x259 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x260 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x261 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x262 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x263 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x264 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x265 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x266 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x267 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x268 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x269 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x270 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x271 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x272 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x273 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x274 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x275 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x276 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x277 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x278 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x279 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x280 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x281 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x282 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x283 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x284 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x285 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x286 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x287 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x288 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x289 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x290 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x291 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x292 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x293 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x294 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x295 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x296 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x297 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x298 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x299 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x300 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x301 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x302 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x303 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x304 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x305 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x306 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x307 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x308 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x309 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x310 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x311 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x312 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x313 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x314 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x315 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x316 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x317 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x318 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x319 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x320 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x321 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x322 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x323 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x324 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x325 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x326 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x327 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x328 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x329 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x330 = Var(within=Reals, bounds=(0,10), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x103 + m.x106 + m.x108 + m.x110 +
    m.x112 + m.x114 + m.x116 + m.x118 + m.x119 + m.x120 + m.x121 + m.x122 +
    m.x123 + m.x124 + m.x125 + m.x126 + m.x127 + m.x128 + m.x129 + m.x130)

m.e1 = Constraint(expr= m.x101 - m.x102 - m.x103 <= 0)
m.e2 = Constraint(expr= -m.x101 + m.x102 - m.x103 <= 0)
m.e3 = Constraint(expr= m.x104 - m.x105 - m.x106 <= 0)
m.e4 = Constraint(expr= -m.x104 + m.x105 - m.x106 <= 0)
m.e5 = Constraint(expr= m.x101 - m.x107 - m.x108 <= 0)
m.e6 = Constraint(expr= -m.x101 + m.x107 - m.x108 <= 0)
m.e7 = Constraint(expr= m.x104 - m.x109 - m.x110 <= 0)
m.e8 = Constraint(expr= -m.x104 + m.x109 - m.x110 <= 0)
m.e9 = Constraint(expr= m.x101 - m.x111 - m.x112 <= 0)
m.e10 = Constraint(expr= -m.x101 + m.x111 - m.x112 <= 0)
m.e11 = Constraint(expr= m.x104 - m.x113 - m.x114 <= 0)
m.e12 = Constraint(expr= -m.x104 + m.x113 - m.x114 <= 0)
m.e13 = Constraint(expr= m.x101 - m.x115 - m.x116 <= 0)
m.e14 = Constraint(expr= -m.x101 + m.x115 - m.x116 <= 0)
m.e15 = Constraint(expr= m.x104 - m.x117 - m.x118 <= 0)
m.e16 = Constraint(expr= -m.x104 + m.x117 - m.x118 <= 0)
m.e17 = Constraint(expr= m.x102 - m.x107 - m.x119 <= 0)
m.e18 = Constraint(expr= -m.x102 + m.x107 - m.x119 <= 0)
m.e19 = Constraint(expr= m.x105 - m.x109 - m.x120 <= 0)
m.e20 = Constraint(expr= -m.x105 + m.x109 - m.x120 <= 0)
m.e21 = Constraint(expr= m.x102 - m.x111 - m.x121 <= 0)
m.e22 = Constraint(expr= -m.x102 + m.x111 - m.x121 <= 0)
m.e23 = Constraint(expr= m.x105 - m.x113 - m.x122 <= 0)
m.e24 = Constraint(expr= -m.x105 + m.x113 - m.x122 <= 0)
m.e25 = Constraint(expr= m.x102 - m.x115 - m.x123 <= 0)
m.e26 = Constraint(expr= -m.x102 + m.x115 - m.x123 <= 0)
m.e27 = Constraint(expr= m.x105 - m.x117 - m.x124 <= 0)
m.e28 = Constraint(expr= -m.x105 + m.x117 - m.x124 <= 0)
m.e29 = Constraint(expr= m.x107 - m.x111 - m.x125 <= 0)
m.e30 = Constraint(expr= -m.x107 + m.x111 - m.x125 <= 0)
m.e31 = Constraint(expr= m.x109 - m.x113 - m.x126 <= 0)
m.e32 = Constraint(expr= -m.x109 + m.x113 - m.x126 <= 0)
m.e33 = Constraint(expr= m.x107 - m.x115 - m.x127 <= 0)
m.e34 = Constraint(expr= -m.x107 + m.x115 - m.x127 <= 0)
m.e35 = Constraint(expr= m.x109 - m.x117 - m.x128 <= 0)
m.e36 = Constraint(expr= -m.x109 + m.x117 - m.x128 <= 0)
m.e37 = Constraint(expr= m.x111 - m.x115 - m.x129 <= 0)
m.e38 = Constraint(expr= -m.x111 + m.x115 - m.x129 <= 0)
m.e39 = Constraint(expr= m.x113 - m.x117 - m.x130 <= 0)
m.e40 = Constraint(expr= -m.x113 + m.x117 - m.x130 <= 0)
m.e41 = Constraint(expr= ((-m.x131 / (0.0001 + 0.9999 * m.b1) +
    0.0236753863366035)**2 + (-m.x132 / (0.0001 + 0.9999 * m.b1) +
    0.861938468195851)**2 - 1) * (0.0001 + 0.9999 * m.b1) -
    2.56501553126003e-10 * m.b1 <= -2.56501553126003e-10)
m.e42 = Constraint(expr= ((-m.x133 / (0.0001 + 0.9999 * m.b2) +
    1.43095891437813)**2 + (-m.x134 / (0.0001 + 0.9999 * m.b2) +
    5.10831625828775)**2 - 1) * (0.0001 + 0.9999 * m.b2) + 0.00271425384093252
    * m.b2 <= 0.00271425384093252)
m.e43 = Constraint(expr= ((-m.x135 / (0.0001 + 0.9999 * m.b3) +
    1.21379363277567)**2 + (-m.x136 / (0.0001 + 0.9999 * m.b3) +
    3.00432848540233)**2 - 1) * (0.0001 + 0.9999 * m.b3) + 0.000949928463116658
    * m.b3 <= 0.000949928463116658)
m.e44 = Constraint(expr= ((-m.x137 / (0.0001 + 0.9999 * m.b4) +
    8.84443217821809)**2 + (-m.x138 / (0.0001 + 0.9999 * m.b4) +
    0.384566405581435)**2 - 1) * (0.0001 + 0.9999 * m.b4) + 0.00773718718754014
    * m.b4 <= 0.00773718718754014)
m.e45 = Constraint(expr= ((-m.x139 / (0.0001 + 0.9999 * m.b5) +
    5.88364087295228)**2 + (-m.x140 / (0.0001 + 0.9999 * m.b5) +
    7.44470191338639)**2 - 1) * (0.0001 + 0.9999 * m.b5) + 0.00890408165010537
    * m.b5 <= 0.00890408165010537)
m.e46 = Constraint(expr= ((-m.x141 / (0.0001 + 0.9999 * m.b6) +
    8.07096798042338)**2 + (-m.x142 / (0.0001 + 0.9999 * m.b6) +
    5.55715186969177)**2 - 1) * (0.0001 + 0.9999 * m.b6) + 0.00950224610438383
    * m.b6 <= 0.00950224610438383)
m.e47 = Constraint(expr= ((-m.x143 / (0.0001 + 0.9999 * m.b7) +
    9.60611615222079)**2 + (-m.x144 / (0.0001 + 0.9999 * m.b7) +
    3.49008429472371)**2 - 1) * (0.0001 + 0.9999 * m.b7) + 0.0103458155914234 *
    m.b7 <= 0.0103458155914234)
m.e48 = Constraint(expr= ((-m.x145 / (0.0001 + 0.9999 * m.b8) + 3.8828653966979)
    **2 + (-m.x146 / (0.0001 + 0.9999 * m.b8) + 5.56627471425883)**2 - 1) * (
    0.0001 + 0.9999 * m.b8) + 0.00450600578834712 * m.b8
    <= 0.00450600578834712)
m.e49 = Constraint(expr= ((-m.x147 / (0.0001 + 0.9999 * m.b9) +
    3.47709171076729)**2 + (-m.x148 / (0.0001 + 0.9999 * m.b9) +
    1.01589173470293)**2 - 1) * (0.0001 + 0.9999 * m.b9) + 0.00121222027817244
    * m.b9 <= 0.00121222027817244)
m.e50 = Constraint(expr= ((-m.x149 / (0.0001 + 0.9999 * m.b10) +
    3.29737974336435)**2 + (-m.x150 / (0.0001 + 0.9999 * m.b10) +
    4.14110922298337)**2 - 1) * (0.0001 + 0.9999 * m.b10) + 0.00270214987686275
    * m.b10 <= 0.00270214987686275)
m.e51 = Constraint(expr= ((-m.x151 / (0.0001 + 0.9999 * m.b11) +
    8.28345883424477)**2 + (-m.x152 / (0.0001 + 0.9999 * m.b11) +
    7.50806458757389)**2 - 1) * (0.0001 + 0.9999 * m.b11) + 0.0123986724109809
    * m.b11 <= 0.0123986724109809)
m.e52 = Constraint(expr= ((-m.x153 / (0.0001 + 0.9999 * m.b12) +
    5.4084966970588)**2 + (-m.x154 / (0.0001 + 0.9999 * m.b12) +
    7.74684442267358)**2 - 1) * (0.0001 + 0.9999 * m.b12) + 0.00882654350312048
    * m.b12 <= 0.00882654350312048)
m.e53 = Constraint(expr= ((-m.x155 / (0.0001 + 0.9999 * m.b13) +
    3.43292425314245)**2 + (-m.x156 / (0.0001 + 0.9999 * m.b13) +
    7.8299358039566)**2 - 1) * (0.0001 + 0.9999 * m.b13) + 0.00720928636218951
    * m.b13 <= 0.00720928636218951)
m.e54 = Constraint(expr= ((-m.x157 / (0.0001 + 0.9999 * m.b14) +
    8.35004447905012)**2 + (-m.x158 / (0.0001 + 0.9999 * m.b14) +
    1.33263454148094)**2 - 1) * (0.0001 + 0.9999 * m.b14) + 0.00704991576232635
    * m.b14 <= 0.00704991576232635)
m.e55 = Constraint(expr= ((-m.x159 / (0.0001 + 0.9999 * m.b15) +
    2.65420450303518)**2 + (-m.x160 / (0.0001 + 0.9999 * m.b15) +
    6.31096321892449)**2 - 1) * (0.0001 + 0.9999 * m.b15) + 0.004587305829455 *
    m.b15 <= 0.004587305829455)
m.e56 = Constraint(expr= ((-m.x161 / (0.0001 + 0.9999 * m.b16) +
    5.8344315991351)**2 + (-m.x162 / (0.0001 + 0.9999 * m.b16) +
    8.56684140863644)**2 - 1) * (0.0001 + 0.9999 * m.b16) + 0.0106431363805714
    * m.b16 <= 0.0106431363805714)
m.e57 = Constraint(expr= ((-m.x163 / (0.0001 + 0.9999 * m.b17) +
    4.10957657319824)**2 + (-m.x164 / (0.0001 + 0.9999 * m.b17) +
    7.8233834211224)**2 - 1) * (0.0001 + 0.9999 * m.b17) + 0.00770939477648726
    * m.b17 <= 0.00770939477648726)
m.e58 = Constraint(expr= ((-m.x165 / (0.0001 + 0.9999 * m.b18) +
    7.39474057003054)**2 + (-m.x166 / (0.0001 + 0.9999 * m.b18) +
    2.49738552645804)**2 - 1) * (0.0001 + 0.9999 * m.b18) + 0.00599191225658178
    * m.b18 <= 0.00599191225658178)
m.e59 = Constraint(expr= ((-m.x167 / (0.0001 + 0.9999 * m.b19) +
    6.14221519240217)**2 + (-m.x168 / (0.0001 + 0.9999 * m.b19) +
    3.03591203112434)**2 - 1) * (0.0001 + 0.9999 * m.b19) + 0.00459435693305015
    * m.b19 <= 0.00459435693305015)
m.e60 = Constraint(expr= ((-m.x169 / (0.0001 + 0.9999 * m.b20) +
    8.26974385940666)**2 + (-m.x170 / (0.0001 + 0.9999 * m.b20) +
    4.22323814320874)**2 - 1) * (0.0001 + 0.9999 * m.b20) + 0.00852244039144474
    * m.b20 <= 0.00852244039144474)
m.e61 = Constraint(expr= m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8
    + m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17 +
    m.b18 + m.b19 + m.b20 == 1)
m.e62 = Constraint(expr= ((-m.x171 / (0.0001 + 0.9999 * m.b21) +
    0.0236753863366035)**2 + (-m.x172 / (0.0001 + 0.9999 * m.b21) +
    0.861938468195851)**2 - 1) * (0.0001 + 0.9999 * m.b21) -
    2.56501553126003e-10 * m.b21 <= -2.56501553126003e-10)
m.e63 = Constraint(expr= ((-m.x173 / (0.0001 + 0.9999 * m.b22) +
    1.43095891437813)**2 + (-m.x174 / (0.0001 + 0.9999 * m.b22) +
    5.10831625828775)**2 - 1) * (0.0001 + 0.9999 * m.b22) + 0.00271425384093252
    * m.b22 <= 0.00271425384093252)
m.e64 = Constraint(expr= ((-m.x175 / (0.0001 + 0.9999 * m.b23) +
    1.21379363277567)**2 + (-m.x176 / (0.0001 + 0.9999 * m.b23) +
    3.00432848540233)**2 - 1) * (0.0001 + 0.9999 * m.b23) +
    0.000949928463116658 * m.b23 <= 0.000949928463116658)
m.e65 = Constraint(expr= ((-m.x177 / (0.0001 + 0.9999 * m.b24) +
    8.84443217821809)**2 + (-m.x178 / (0.0001 + 0.9999 * m.b24) +
    0.384566405581435)**2 - 1) * (0.0001 + 0.9999 * m.b24) +
    0.00773718718754014 * m.b24 <= 0.00773718718754014)
m.e66 = Constraint(expr= ((-m.x179 / (0.0001 + 0.9999 * m.b25) +
    5.88364087295228)**2 + (-m.x180 / (0.0001 + 0.9999 * m.b25) +
    7.44470191338639)**2 - 1) * (0.0001 + 0.9999 * m.b25) + 0.00890408165010537
    * m.b25 <= 0.00890408165010537)
m.e67 = Constraint(expr= ((-m.x181 / (0.0001 + 0.9999 * m.b26) +
    8.07096798042338)**2 + (-m.x182 / (0.0001 + 0.9999 * m.b26) +
    5.55715186969177)**2 - 1) * (0.0001 + 0.9999 * m.b26) + 0.00950224610438383
    * m.b26 <= 0.00950224610438383)
m.e68 = Constraint(expr= ((-m.x183 / (0.0001 + 0.9999 * m.b27) +
    9.60611615222079)**2 + (-m.x184 / (0.0001 + 0.9999 * m.b27) +
    3.49008429472371)**2 - 1) * (0.0001 + 0.9999 * m.b27) + 0.0103458155914234
    * m.b27 <= 0.0103458155914234)
m.e69 = Constraint(expr= ((-m.x185 / (0.0001 + 0.9999 * m.b28) +
    3.8828653966979)**2 + (-m.x186 / (0.0001 + 0.9999 * m.b28) +
    5.56627471425883)**2 - 1) * (0.0001 + 0.9999 * m.b28) + 0.00450600578834712
    * m.b28 <= 0.00450600578834712)
m.e70 = Constraint(expr= ((-m.x187 / (0.0001 + 0.9999 * m.b29) +
    3.47709171076729)**2 + (-m.x188 / (0.0001 + 0.9999 * m.b29) +
    1.01589173470293)**2 - 1) * (0.0001 + 0.9999 * m.b29) + 0.00121222027817244
    * m.b29 <= 0.00121222027817244)
m.e71 = Constraint(expr= ((-m.x189 / (0.0001 + 0.9999 * m.b30) +
    3.29737974336435)**2 + (-m.x190 / (0.0001 + 0.9999 * m.b30) +
    4.14110922298337)**2 - 1) * (0.0001 + 0.9999 * m.b30) + 0.00270214987686275
    * m.b30 <= 0.00270214987686275)
m.e72 = Constraint(expr= ((-m.x191 / (0.0001 + 0.9999 * m.b31) +
    8.28345883424477)**2 + (-m.x192 / (0.0001 + 0.9999 * m.b31) +
    7.50806458757389)**2 - 1) * (0.0001 + 0.9999 * m.b31) + 0.0123986724109809
    * m.b31 <= 0.0123986724109809)
m.e73 = Constraint(expr= ((-m.x193 / (0.0001 + 0.9999 * m.b32) +
    5.4084966970588)**2 + (-m.x194 / (0.0001 + 0.9999 * m.b32) +
    7.74684442267358)**2 - 1) * (0.0001 + 0.9999 * m.b32) + 0.00882654350312048
    * m.b32 <= 0.00882654350312048)
m.e74 = Constraint(expr= ((-m.x195 / (0.0001 + 0.9999 * m.b33) +
    3.43292425314245)**2 + (-m.x196 / (0.0001 + 0.9999 * m.b33) +
    7.8299358039566)**2 - 1) * (0.0001 + 0.9999 * m.b33) + 0.00720928636218951
    * m.b33 <= 0.00720928636218951)
m.e75 = Constraint(expr= ((-m.x197 / (0.0001 + 0.9999 * m.b34) +
    8.35004447905012)**2 + (-m.x198 / (0.0001 + 0.9999 * m.b34) +
    1.33263454148094)**2 - 1) * (0.0001 + 0.9999 * m.b34) + 0.00704991576232635
    * m.b34 <= 0.00704991576232635)
m.e76 = Constraint(expr= ((-m.x199 / (0.0001 + 0.9999 * m.b35) +
    2.65420450303518)**2 + (-m.x200 / (0.0001 + 0.9999 * m.b35) +
    6.31096321892449)**2 - 1) * (0.0001 + 0.9999 * m.b35) + 0.004587305829455 *
    m.b35 <= 0.004587305829455)
m.e77 = Constraint(expr= ((-m.x201 / (0.0001 + 0.9999 * m.b36) +
    5.8344315991351)**2 + (-m.x202 / (0.0001 + 0.9999 * m.b36) +
    8.56684140863644)**2 - 1) * (0.0001 + 0.9999 * m.b36) + 0.0106431363805714
    * m.b36 <= 0.0106431363805714)
m.e78 = Constraint(expr= ((-m.x203 / (0.0001 + 0.9999 * m.b37) +
    4.10957657319824)**2 + (-m.x204 / (0.0001 + 0.9999 * m.b37) +
    7.8233834211224)**2 - 1) * (0.0001 + 0.9999 * m.b37) + 0.00770939477648726
    * m.b37 <= 0.00770939477648726)
m.e79 = Constraint(expr= ((-m.x205 / (0.0001 + 0.9999 * m.b38) +
    7.39474057003054)**2 + (-m.x206 / (0.0001 + 0.9999 * m.b38) +
    2.49738552645804)**2 - 1) * (0.0001 + 0.9999 * m.b38) + 0.00599191225658178
    * m.b38 <= 0.00599191225658178)
m.e80 = Constraint(expr= ((-m.x207 / (0.0001 + 0.9999 * m.b39) +
    6.14221519240217)**2 + (-m.x208 / (0.0001 + 0.9999 * m.b39) +
    3.03591203112434)**2 - 1) * (0.0001 + 0.9999 * m.b39) + 0.00459435693305015
    * m.b39 <= 0.00459435693305015)
m.e81 = Constraint(expr= ((-m.x209 / (0.0001 + 0.9999 * m.b40) +
    8.26974385940666)**2 + (-m.x210 / (0.0001 + 0.9999 * m.b40) +
    4.22323814320874)**2 - 1) * (0.0001 + 0.9999 * m.b40) + 0.00852244039144474
    * m.b40 <= 0.00852244039144474)
m.e82 = Constraint(expr= m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 + m.b27
    + m.b28 + m.b29 + m.b30 + m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 +
    m.b37 + m.b38 + m.b39 + m.b40 == 1)
m.e83 = Constraint(expr= ((-m.x211 / (0.0001 + 0.9999 * m.b41) +
    0.0236753863366035)**2 + (-m.x212 / (0.0001 + 0.9999 * m.b41) +
    0.861938468195851)**2 - 1) * (0.0001 + 0.9999 * m.b41) -
    2.56501553126003e-10 * m.b41 <= -2.56501553126003e-10)
m.e84 = Constraint(expr= ((-m.x213 / (0.0001 + 0.9999 * m.b42) +
    1.43095891437813)**2 + (-m.x214 / (0.0001 + 0.9999 * m.b42) +
    5.10831625828775)**2 - 1) * (0.0001 + 0.9999 * m.b42) + 0.00271425384093252
    * m.b42 <= 0.00271425384093252)
m.e85 = Constraint(expr= ((-m.x215 / (0.0001 + 0.9999 * m.b43) +
    1.21379363277567)**2 + (-m.x216 / (0.0001 + 0.9999 * m.b43) +
    3.00432848540233)**2 - 1) * (0.0001 + 0.9999 * m.b43) +
    0.000949928463116658 * m.b43 <= 0.000949928463116658)
m.e86 = Constraint(expr= ((-m.x217 / (0.0001 + 0.9999 * m.b44) +
    8.84443217821809)**2 + (-m.x218 / (0.0001 + 0.9999 * m.b44) +
    0.384566405581435)**2 - 1) * (0.0001 + 0.9999 * m.b44) +
    0.00773718718754014 * m.b44 <= 0.00773718718754014)
m.e87 = Constraint(expr= ((-m.x219 / (0.0001 + 0.9999 * m.b45) +
    5.88364087295228)**2 + (-m.x220 / (0.0001 + 0.9999 * m.b45) +
    7.44470191338639)**2 - 1) * (0.0001 + 0.9999 * m.b45) + 0.00890408165010537
    * m.b45 <= 0.00890408165010537)
m.e88 = Constraint(expr= ((-m.x221 / (0.0001 + 0.9999 * m.b46) +
    8.07096798042338)**2 + (-m.x222 / (0.0001 + 0.9999 * m.b46) +
    5.55715186969177)**2 - 1) * (0.0001 + 0.9999 * m.b46) + 0.00950224610438383
    * m.b46 <= 0.00950224610438383)
m.e89 = Constraint(expr= ((-m.x223 / (0.0001 + 0.9999 * m.b47) +
    9.60611615222079)**2 + (-m.x224 / (0.0001 + 0.9999 * m.b47) +
    3.49008429472371)**2 - 1) * (0.0001 + 0.9999 * m.b47) + 0.0103458155914234
    * m.b47 <= 0.0103458155914234)
m.e90 = Constraint(expr= ((-m.x225 / (0.0001 + 0.9999 * m.b48) +
    3.8828653966979)**2 + (-m.x226 / (0.0001 + 0.9999 * m.b48) +
    5.56627471425883)**2 - 1) * (0.0001 + 0.9999 * m.b48) + 0.00450600578834712
    * m.b48 <= 0.00450600578834712)
m.e91 = Constraint(expr= ((-m.x227 / (0.0001 + 0.9999 * m.b49) +
    3.47709171076729)**2 + (-m.x228 / (0.0001 + 0.9999 * m.b49) +
    1.01589173470293)**2 - 1) * (0.0001 + 0.9999 * m.b49) + 0.00121222027817244
    * m.b49 <= 0.00121222027817244)
m.e92 = Constraint(expr= ((-m.x229 / (0.0001 + 0.9999 * m.b50) +
    3.29737974336435)**2 + (-m.x230 / (0.0001 + 0.9999 * m.b50) +
    4.14110922298337)**2 - 1) * (0.0001 + 0.9999 * m.b50) + 0.00270214987686275
    * m.b50 <= 0.00270214987686275)
m.e93 = Constraint(expr= ((-m.x231 / (0.0001 + 0.9999 * m.b51) +
    8.28345883424477)**2 + (-m.x232 / (0.0001 + 0.9999 * m.b51) +
    7.50806458757389)**2 - 1) * (0.0001 + 0.9999 * m.b51) + 0.0123986724109809
    * m.b51 <= 0.0123986724109809)
m.e94 = Constraint(expr= ((-m.x233 / (0.0001 + 0.9999 * m.b52) +
    5.4084966970588)**2 + (-m.x234 / (0.0001 + 0.9999 * m.b52) +
    7.74684442267358)**2 - 1) * (0.0001 + 0.9999 * m.b52) + 0.00882654350312048
    * m.b52 <= 0.00882654350312048)
m.e95 = Constraint(expr= ((-m.x235 / (0.0001 + 0.9999 * m.b53) +
    3.43292425314245)**2 + (-m.x236 / (0.0001 + 0.9999 * m.b53) +
    7.8299358039566)**2 - 1) * (0.0001 + 0.9999 * m.b53) + 0.00720928636218951
    * m.b53 <= 0.00720928636218951)
m.e96 = Constraint(expr= ((-m.x237 / (0.0001 + 0.9999 * m.b54) +
    8.35004447905012)**2 + (-m.x238 / (0.0001 + 0.9999 * m.b54) +
    1.33263454148094)**2 - 1) * (0.0001 + 0.9999 * m.b54) + 0.00704991576232635
    * m.b54 <= 0.00704991576232635)
m.e97 = Constraint(expr= ((-m.x239 / (0.0001 + 0.9999 * m.b55) +
    2.65420450303518)**2 + (-m.x240 / (0.0001 + 0.9999 * m.b55) +
    6.31096321892449)**2 - 1) * (0.0001 + 0.9999 * m.b55) + 0.004587305829455 *
    m.b55 <= 0.004587305829455)
m.e98 = Constraint(expr= ((-m.x241 / (0.0001 + 0.9999 * m.b56) +
    5.8344315991351)**2 + (-m.x242 / (0.0001 + 0.9999 * m.b56) +
    8.56684140863644)**2 - 1) * (0.0001 + 0.9999 * m.b56) + 0.0106431363805714
    * m.b56 <= 0.0106431363805714)
m.e99 = Constraint(expr= ((-m.x243 / (0.0001 + 0.9999 * m.b57) +
    4.10957657319824)**2 + (-m.x244 / (0.0001 + 0.9999 * m.b57) +
    7.8233834211224)**2 - 1) * (0.0001 + 0.9999 * m.b57) + 0.00770939477648726
    * m.b57 <= 0.00770939477648726)
m.e100 = Constraint(expr= ((-m.x245 / (0.0001 + 0.9999 * m.b58) +
    7.39474057003054)**2 + (-m.x246 / (0.0001 + 0.9999 * m.b58) +
    2.49738552645804)**2 - 1) * (0.0001 + 0.9999 * m.b58) + 0.00599191225658178
    * m.b58 <= 0.00599191225658178)
m.e101 = Constraint(expr= ((-m.x247 / (0.0001 + 0.9999 * m.b59) +
    6.14221519240217)**2 + (-m.x248 / (0.0001 + 0.9999 * m.b59) +
    3.03591203112434)**2 - 1) * (0.0001 + 0.9999 * m.b59) + 0.00459435693305015
    * m.b59 <= 0.00459435693305015)
m.e102 = Constraint(expr= ((-m.x249 / (0.0001 + 0.9999 * m.b60) +
    8.26974385940666)**2 + (-m.x250 / (0.0001 + 0.9999 * m.b60) +
    4.22323814320874)**2 - 1) * (0.0001 + 0.9999 * m.b60) + 0.00852244039144474
    * m.b60 <= 0.00852244039144474)
m.e103 = Constraint(expr= m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47
    + m.b48 + m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 +
    m.b57 + m.b58 + m.b59 + m.b60 == 1)
m.e104 = Constraint(expr= ((-m.x251 / (0.0001 + 0.9999 * m.b61) +
    0.0236753863366035)**2 + (-m.x252 / (0.0001 + 0.9999 * m.b61) +
    0.861938468195851)**2 - 1) * (0.0001 + 0.9999 * m.b61) -
    2.56501553126003e-10 * m.b61 <= -2.56501553126003e-10)
m.e105 = Constraint(expr= ((-m.x253 / (0.0001 + 0.9999 * m.b62) +
    1.43095891437813)**2 + (-m.x254 / (0.0001 + 0.9999 * m.b62) +
    5.10831625828775)**2 - 1) * (0.0001 + 0.9999 * m.b62) + 0.00271425384093252
    * m.b62 <= 0.00271425384093252)
m.e106 = Constraint(expr= ((-m.x255 / (0.0001 + 0.9999 * m.b63) +
    1.21379363277567)**2 + (-m.x256 / (0.0001 + 0.9999 * m.b63) +
    3.00432848540233)**2 - 1) * (0.0001 + 0.9999 * m.b63) +
    0.000949928463116658 * m.b63 <= 0.000949928463116658)
m.e107 = Constraint(expr= ((-m.x257 / (0.0001 + 0.9999 * m.b64) +
    8.84443217821809)**2 + (-m.x258 / (0.0001 + 0.9999 * m.b64) +
    0.384566405581435)**2 - 1) * (0.0001 + 0.9999 * m.b64) +
    0.00773718718754014 * m.b64 <= 0.00773718718754014)
m.e108 = Constraint(expr= ((-m.x259 / (0.0001 + 0.9999 * m.b65) +
    5.88364087295228)**2 + (-m.x260 / (0.0001 + 0.9999 * m.b65) +
    7.44470191338639)**2 - 1) * (0.0001 + 0.9999 * m.b65) + 0.00890408165010537
    * m.b65 <= 0.00890408165010537)
m.e109 = Constraint(expr= ((-m.x261 / (0.0001 + 0.9999 * m.b66) +
    8.07096798042338)**2 + (-m.x262 / (0.0001 + 0.9999 * m.b66) +
    5.55715186969177)**2 - 1) * (0.0001 + 0.9999 * m.b66) + 0.00950224610438383
    * m.b66 <= 0.00950224610438383)
m.e110 = Constraint(expr= ((-m.x263 / (0.0001 + 0.9999 * m.b67) +
    9.60611615222079)**2 + (-m.x264 / (0.0001 + 0.9999 * m.b67) +
    3.49008429472371)**2 - 1) * (0.0001 + 0.9999 * m.b67) + 0.0103458155914234
    * m.b67 <= 0.0103458155914234)
m.e111 = Constraint(expr= ((-m.x265 / (0.0001 + 0.9999 * m.b68) +
    3.8828653966979)**2 + (-m.x266 / (0.0001 + 0.9999 * m.b68) +
    5.56627471425883)**2 - 1) * (0.0001 + 0.9999 * m.b68) + 0.00450600578834712
    * m.b68 <= 0.00450600578834712)
m.e112 = Constraint(expr= ((-m.x267 / (0.0001 + 0.9999 * m.b69) +
    3.47709171076729)**2 + (-m.x268 / (0.0001 + 0.9999 * m.b69) +
    1.01589173470293)**2 - 1) * (0.0001 + 0.9999 * m.b69) + 0.00121222027817244
    * m.b69 <= 0.00121222027817244)
m.e113 = Constraint(expr= ((-m.x269 / (0.0001 + 0.9999 * m.b70) +
    3.29737974336435)**2 + (-m.x270 / (0.0001 + 0.9999 * m.b70) +
    4.14110922298337)**2 - 1) * (0.0001 + 0.9999 * m.b70) + 0.00270214987686275
    * m.b70 <= 0.00270214987686275)
m.e114 = Constraint(expr= ((-m.x271 / (0.0001 + 0.9999 * m.b71) +
    8.28345883424477)**2 + (-m.x272 / (0.0001 + 0.9999 * m.b71) +
    7.50806458757389)**2 - 1) * (0.0001 + 0.9999 * m.b71) + 0.0123986724109809
    * m.b71 <= 0.0123986724109809)
m.e115 = Constraint(expr= ((-m.x273 / (0.0001 + 0.9999 * m.b72) +
    5.4084966970588)**2 + (-m.x274 / (0.0001 + 0.9999 * m.b72) +
    7.74684442267358)**2 - 1) * (0.0001 + 0.9999 * m.b72) + 0.00882654350312048
    * m.b72 <= 0.00882654350312048)
m.e116 = Constraint(expr= ((-m.x275 / (0.0001 + 0.9999 * m.b73) +
    3.43292425314245)**2 + (-m.x276 / (0.0001 + 0.9999 * m.b73) +
    7.8299358039566)**2 - 1) * (0.0001 + 0.9999 * m.b73) + 0.00720928636218951
    * m.b73 <= 0.00720928636218951)
m.e117 = Constraint(expr= ((-m.x277 / (0.0001 + 0.9999 * m.b74) +
    8.35004447905012)**2 + (-m.x278 / (0.0001 + 0.9999 * m.b74) +
    1.33263454148094)**2 - 1) * (0.0001 + 0.9999 * m.b74) + 0.00704991576232635
    * m.b74 <= 0.00704991576232635)
m.e118 = Constraint(expr= ((-m.x279 / (0.0001 + 0.9999 * m.b75) +
    2.65420450303518)**2 + (-m.x280 / (0.0001 + 0.9999 * m.b75) +
    6.31096321892449)**2 - 1) * (0.0001 + 0.9999 * m.b75) + 0.004587305829455 *
    m.b75 <= 0.004587305829455)
m.e119 = Constraint(expr= ((-m.x281 / (0.0001 + 0.9999 * m.b76) +
    5.8344315991351)**2 + (-m.x282 / (0.0001 + 0.9999 * m.b76) +
    8.56684140863644)**2 - 1) * (0.0001 + 0.9999 * m.b76) + 0.0106431363805714
    * m.b76 <= 0.0106431363805714)
m.e120 = Constraint(expr= ((-m.x283 / (0.0001 + 0.9999 * m.b77) +
    4.10957657319824)**2 + (-m.x284 / (0.0001 + 0.9999 * m.b77) +
    7.8233834211224)**2 - 1) * (0.0001 + 0.9999 * m.b77) + 0.00770939477648726
    * m.b77 <= 0.00770939477648726)
m.e121 = Constraint(expr= ((-m.x285 / (0.0001 + 0.9999 * m.b78) +
    7.39474057003054)**2 + (-m.x286 / (0.0001 + 0.9999 * m.b78) +
    2.49738552645804)**2 - 1) * (0.0001 + 0.9999 * m.b78) + 0.00599191225658178
    * m.b78 <= 0.00599191225658178)
m.e122 = Constraint(expr= ((-m.x287 / (0.0001 + 0.9999 * m.b79) +
    6.14221519240217)**2 + (-m.x288 / (0.0001 + 0.9999 * m.b79) +
    3.03591203112434)**2 - 1) * (0.0001 + 0.9999 * m.b79) + 0.00459435693305015
    * m.b79 <= 0.00459435693305015)
m.e123 = Constraint(expr= ((-m.x289 / (0.0001 + 0.9999 * m.b80) +
    8.26974385940666)**2 + (-m.x290 / (0.0001 + 0.9999 * m.b80) +
    4.22323814320874)**2 - 1) * (0.0001 + 0.9999 * m.b80) + 0.00852244039144474
    * m.b80 <= 0.00852244039144474)
m.e124 = Constraint(expr= m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b66 + m.b67
    + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 + m.b73 + m.b74 + m.b75 + m.b76 +
    m.b77 + m.b78 + m.b79 + m.b80 == 1)
m.e125 = Constraint(expr= ((-m.x291 / (0.0001 + 0.9999 * m.b81) +
    0.0236753863366035)**2 + (-m.x292 / (0.0001 + 0.9999 * m.b81) +
    0.861938468195851)**2 - 1) * (0.0001 + 0.9999 * m.b81) -
    2.56501553126003e-10 * m.b81 <= -2.56501553126003e-10)
m.e126 = Constraint(expr= ((-m.x293 / (0.0001 + 0.9999 * m.b82) +
    1.43095891437813)**2 + (-m.x294 / (0.0001 + 0.9999 * m.b82) +
    5.10831625828775)**2 - 1) * (0.0001 + 0.9999 * m.b82) + 0.00271425384093252
    * m.b82 <= 0.00271425384093252)
m.e127 = Constraint(expr= ((-m.x295 / (0.0001 + 0.9999 * m.b83) +
    1.21379363277567)**2 + (-m.x296 / (0.0001 + 0.9999 * m.b83) +
    3.00432848540233)**2 - 1) * (0.0001 + 0.9999 * m.b83) +
    0.000949928463116658 * m.b83 <= 0.000949928463116658)
m.e128 = Constraint(expr= ((-m.x297 / (0.0001 + 0.9999 * m.b84) +
    8.84443217821809)**2 + (-m.x298 / (0.0001 + 0.9999 * m.b84) +
    0.384566405581435)**2 - 1) * (0.0001 + 0.9999 * m.b84) +
    0.00773718718754014 * m.b84 <= 0.00773718718754014)
m.e129 = Constraint(expr= ((-m.x299 / (0.0001 + 0.9999 * m.b85) +
    5.88364087295228)**2 + (-m.x300 / (0.0001 + 0.9999 * m.b85) +
    7.44470191338639)**2 - 1) * (0.0001 + 0.9999 * m.b85) + 0.00890408165010537
    * m.b85 <= 0.00890408165010537)
m.e130 = Constraint(expr= ((-m.x301 / (0.0001 + 0.9999 * m.b86) +
    8.07096798042338)**2 + (-m.x302 / (0.0001 + 0.9999 * m.b86) +
    5.55715186969177)**2 - 1) * (0.0001 + 0.9999 * m.b86) + 0.00950224610438383
    * m.b86 <= 0.00950224610438383)
m.e131 = Constraint(expr= ((-m.x303 / (0.0001 + 0.9999 * m.b87) +
    9.60611615222079)**2 + (-m.x304 / (0.0001 + 0.9999 * m.b87) +
    3.49008429472371)**2 - 1) * (0.0001 + 0.9999 * m.b87) + 0.0103458155914234
    * m.b87 <= 0.0103458155914234)
m.e132 = Constraint(expr= ((-m.x305 / (0.0001 + 0.9999 * m.b88) +
    3.8828653966979)**2 + (-m.x306 / (0.0001 + 0.9999 * m.b88) +
    5.56627471425883)**2 - 1) * (0.0001 + 0.9999 * m.b88) + 0.00450600578834712
    * m.b88 <= 0.00450600578834712)
m.e133 = Constraint(expr= ((-m.x307 / (0.0001 + 0.9999 * m.b89) +
    3.47709171076729)**2 + (-m.x308 / (0.0001 + 0.9999 * m.b89) +
    1.01589173470293)**2 - 1) * (0.0001 + 0.9999 * m.b89) + 0.00121222027817244
    * m.b89 <= 0.00121222027817244)
m.e134 = Constraint(expr= ((-m.x309 / (0.0001 + 0.9999 * m.b90) +
    3.29737974336435)**2 + (-m.x310 / (0.0001 + 0.9999 * m.b90) +
    4.14110922298337)**2 - 1) * (0.0001 + 0.9999 * m.b90) + 0.00270214987686275
    * m.b90 <= 0.00270214987686275)
m.e135 = Constraint(expr= ((-m.x311 / (0.0001 + 0.9999 * m.b91) +
    8.28345883424477)**2 + (-m.x312 / (0.0001 + 0.9999 * m.b91) +
    7.50806458757389)**2 - 1) * (0.0001 + 0.9999 * m.b91) + 0.0123986724109809
    * m.b91 <= 0.0123986724109809)
m.e136 = Constraint(expr= ((-m.x313 / (0.0001 + 0.9999 * m.b92) +
    5.4084966970588)**2 + (-m.x314 / (0.0001 + 0.9999 * m.b92) +
    7.74684442267358)**2 - 1) * (0.0001 + 0.9999 * m.b92) + 0.00882654350312048
    * m.b92 <= 0.00882654350312048)
m.e137 = Constraint(expr= ((-m.x315 / (0.0001 + 0.9999 * m.b93) +
    3.43292425314245)**2 + (-m.x316 / (0.0001 + 0.9999 * m.b93) +
    7.8299358039566)**2 - 1) * (0.0001 + 0.9999 * m.b93) + 0.00720928636218951
    * m.b93 <= 0.00720928636218951)
m.e138 = Constraint(expr= ((-m.x317 / (0.0001 + 0.9999 * m.b94) +
    8.35004447905012)**2 + (-m.x318 / (0.0001 + 0.9999 * m.b94) +
    1.33263454148094)**2 - 1) * (0.0001 + 0.9999 * m.b94) + 0.00704991576232635
    * m.b94 <= 0.00704991576232635)
m.e139 = Constraint(expr= ((-m.x319 / (0.0001 + 0.9999 * m.b95) +
    2.65420450303518)**2 + (-m.x320 / (0.0001 + 0.9999 * m.b95) +
    6.31096321892449)**2 - 1) * (0.0001 + 0.9999 * m.b95) + 0.004587305829455 *
    m.b95 <= 0.004587305829455)
m.e140 = Constraint(expr= ((-m.x321 / (0.0001 + 0.9999 * m.b96) +
    5.8344315991351)**2 + (-m.x322 / (0.0001 + 0.9999 * m.b96) +
    8.56684140863644)**2 - 1) * (0.0001 + 0.9999 * m.b96) + 0.0106431363805714
    * m.b96 <= 0.0106431363805714)
m.e141 = Constraint(expr= ((-m.x323 / (0.0001 + 0.9999 * m.b97) +
    4.10957657319824)**2 + (-m.x324 / (0.0001 + 0.9999 * m.b97) +
    7.8233834211224)**2 - 1) * (0.0001 + 0.9999 * m.b97) + 0.00770939477648726
    * m.b97 <= 0.00770939477648726)
m.e142 = Constraint(expr= ((-m.x325 / (0.0001 + 0.9999 * m.b98) +
    7.39474057003054)**2 + (-m.x326 / (0.0001 + 0.9999 * m.b98) +
    2.49738552645804)**2 - 1) * (0.0001 + 0.9999 * m.b98) + 0.00599191225658178
    * m.b98 <= 0.00599191225658178)
m.e143 = Constraint(expr= ((-m.x327 / (0.0001 + 0.9999 * m.b99) +
    6.14221519240217)**2 + (-m.x328 / (0.0001 + 0.9999 * m.b99) +
    3.03591203112434)**2 - 1) * (0.0001 + 0.9999 * m.b99) + 0.00459435693305015
    * m.b99 <= 0.00459435693305015)
m.e144 = Constraint(expr= ((-m.x329 / (0.0001 + 0.9999 * m.b100) +
    8.26974385940666)**2 + (-m.x330 / (0.0001 + 0.9999 * m.b100) +
    4.22323814320874)**2 - 1) * (0.0001 + 0.9999 * m.b100) +
    0.00852244039144474 * m.b100 <= 0.00852244039144474)
m.e145 = Constraint(expr= m.b81 + m.b82 + m.b83 + m.b84 + m.b85 + m.b86 + m.b87
    + m.b88 + m.b89 + m.b90 + m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b96 +
    m.b97 + m.b98 + m.b99 + m.b100 == 1)
m.e146 = Constraint(expr= m.b1 + m.b21 + m.b41 + m.b61 + m.b81 <= 1)
m.e147 = Constraint(expr= m.b2 + m.b22 + m.b42 + m.b62 + m.b82 <= 1)
m.e148 = Constraint(expr= m.b3 + m.b23 + m.b43 + m.b63 + m.b83 <= 1)
m.e149 = Constraint(expr= m.b4 + m.b24 + m.b44 + m.b64 + m.b84 <= 1)
m.e150 = Constraint(expr= m.b5 + m.b25 + m.b45 + m.b65 + m.b85 <= 1)
m.e151 = Constraint(expr= m.b6 + m.b26 + m.b46 + m.b66 + m.b86 <= 1)
m.e152 = Constraint(expr= m.b7 + m.b27 + m.b47 + m.b67 + m.b87 <= 1)
m.e153 = Constraint(expr= m.b8 + m.b28 + m.b48 + m.b68 + m.b88 <= 1)
m.e154 = Constraint(expr= m.b9 + m.b29 + m.b49 + m.b69 + m.b89 <= 1)
m.e155 = Constraint(expr= m.b10 + m.b30 + m.b50 + m.b70 + m.b90 <= 1)
m.e156 = Constraint(expr= m.b11 + m.b31 + m.b51 + m.b71 + m.b91 <= 1)
m.e157 = Constraint(expr= m.b12 + m.b32 + m.b52 + m.b72 + m.b92 <= 1)
m.e158 = Constraint(expr= m.b13 + m.b33 + m.b53 + m.b73 + m.b93 <= 1)
m.e159 = Constraint(expr= m.b14 + m.b34 + m.b54 + m.b74 + m.b94 <= 1)
m.e160 = Constraint(expr= m.b15 + m.b35 + m.b55 + m.b75 + m.b95 <= 1)
m.e161 = Constraint(expr= m.b16 + m.b36 + m.b56 + m.b76 + m.b96 <= 1)
m.e162 = Constraint(expr= m.b17 + m.b37 + m.b57 + m.b77 + m.b97 <= 1)
m.e163 = Constraint(expr= m.b18 + m.b38 + m.b58 + m.b78 + m.b98 <= 1)
m.e164 = Constraint(expr= m.b19 + m.b39 + m.b59 + m.b79 + m.b99 <= 1)
m.e165 = Constraint(expr= m.b20 + m.b40 + m.b60 + m.b80 + m.b100 <= 1)
m.e166 = Constraint(expr= -m.x101 + m.x131 + m.x133 + m.x135 + m.x137 + m.x139
    + m.x141 + m.x143 + m.x145 + m.x147 + m.x149 + m.x151 + m.x153 + m.x155 +
    m.x157 + m.x159 + m.x161 + m.x163 + m.x165 + m.x167 + m.x169 == 0)
m.e167 = Constraint(expr= -m.x104 + m.x132 + m.x134 + m.x136 + m.x138 + m.x140
    + m.x142 + m.x144 + m.x146 + m.x148 + m.x150 + m.x152 + m.x154 + m.x156 +
    m.x158 + m.x160 + m.x162 + m.x164 + m.x166 + m.x168 + m.x170 == 0)
m.e168 = Constraint(expr= -m.x102 + m.x171 + m.x173 + m.x175 + m.x177 + m.x179
    + m.x181 + m.x183 + m.x185 + m.x187 + m.x189 + m.x191 + m.x193 + m.x195 +
    m.x197 + m.x199 + m.x201 + m.x203 + m.x205 + m.x207 + m.x209 == 0)
m.e169 = Constraint(expr= -m.x105 + m.x172 + m.x174 + m.x176 + m.x178 + m.x180
    + m.x182 + m.x184 + m.x186 + m.x188 + m.x190 + m.x192 + m.x194 + m.x196 +
    m.x198 + m.x200 + m.x202 + m.x204 + m.x206 + m.x208 + m.x210 == 0)
m.e170 = Constraint(expr= -m.x107 + m.x211 + m.x213 + m.x215 + m.x217 + m.x219
    + m.x221 + m.x223 + m.x225 + m.x227 + m.x229 + m.x231 + m.x233 + m.x235 +
    m.x237 + m.x239 + m.x241 + m.x243 + m.x245 + m.x247 + m.x249 == 0)
m.e171 = Constraint(expr= -m.x109 + m.x212 + m.x214 + m.x216 + m.x218 + m.x220
    + m.x222 + m.x224 + m.x226 + m.x228 + m.x230 + m.x232 + m.x234 + m.x236 +
    m.x238 + m.x240 + m.x242 + m.x244 + m.x246 + m.x248 + m.x250 == 0)
m.e172 = Constraint(expr= -m.x111 + m.x251 + m.x253 + m.x255 + m.x257 + m.x259
    + m.x261 + m.x263 + m.x265 + m.x267 + m.x269 + m.x271 + m.x273 + m.x275 +
    m.x277 + m.x279 + m.x281 + m.x283 + m.x285 + m.x287 + m.x289 == 0)
m.e173 = Constraint(expr= -m.x113 + m.x252 + m.x254 + m.x256 + m.x258 + m.x260
    + m.x262 + m.x264 + m.x266 + m.x268 + m.x270 + m.x272 + m.x274 + m.x276 +
    m.x278 + m.x280 + m.x282 + m.x284 + m.x286 + m.x288 + m.x290 == 0)
m.e174 = Constraint(expr= -m.x115 + m.x291 + m.x293 + m.x295 + m.x297 + m.x299
    + m.x301 + m.x303 + m.x305 + m.x307 + m.x309 + m.x311 + m.x313 + m.x315 +
    m.x317 + m.x319 + m.x321 + m.x323 + m.x325 + m.x327 + m.x329 == 0)
m.e175 = Constraint(expr= -m.x117 + m.x292 + m.x294 + m.x296 + m.x298 + m.x300
    + m.x302 + m.x304 + m.x306 + m.x308 + m.x310 + m.x312 + m.x314 + m.x316 +
    m.x318 + m.x320 + m.x322 + m.x324 + m.x326 + m.x328 + m.x330 == 0)
m.e176 = Constraint(expr= -10 * m.b1 + m.x131 <= 0)
m.e177 = Constraint(expr= -10 * m.b2 + m.x133 <= 0)
m.e178 = Constraint(expr= -10 * m.b3 + m.x135 <= 0)
m.e179 = Constraint(expr= -10 * m.b4 + m.x137 <= 0)
m.e180 = Constraint(expr= -10 * m.b5 + m.x139 <= 0)
m.e181 = Constraint(expr= -10 * m.b6 + m.x141 <= 0)
m.e182 = Constraint(expr= -10 * m.b7 + m.x143 <= 0)
m.e183 = Constraint(expr= -10 * m.b8 + m.x145 <= 0)
m.e184 = Constraint(expr= -10 * m.b9 + m.x147 <= 0)
m.e185 = Constraint(expr= -10 * m.b10 + m.x149 <= 0)
m.e186 = Constraint(expr= -10 * m.b11 + m.x151 <= 0)
m.e187 = Constraint(expr= -10 * m.b12 + m.x153 <= 0)
m.e188 = Constraint(expr= -10 * m.b13 + m.x155 <= 0)
m.e189 = Constraint(expr= -10 * m.b14 + m.x157 <= 0)
m.e190 = Constraint(expr= -10 * m.b15 + m.x159 <= 0)
m.e191 = Constraint(expr= -10 * m.b16 + m.x161 <= 0)
m.e192 = Constraint(expr= -10 * m.b17 + m.x163 <= 0)
m.e193 = Constraint(expr= -10 * m.b18 + m.x165 <= 0)
m.e194 = Constraint(expr= -10 * m.b19 + m.x167 <= 0)
m.e195 = Constraint(expr= -10 * m.b20 + m.x169 <= 0)
m.e196 = Constraint(expr= -10 * m.b1 + m.x132 <= 0)
m.e197 = Constraint(expr= -10 * m.b2 + m.x134 <= 0)
m.e198 = Constraint(expr= -10 * m.b3 + m.x136 <= 0)
m.e199 = Constraint(expr= -10 * m.b4 + m.x138 <= 0)
m.e200 = Constraint(expr= -10 * m.b5 + m.x140 <= 0)
m.e201 = Constraint(expr= -10 * m.b6 + m.x142 <= 0)
m.e202 = Constraint(expr= -10 * m.b7 + m.x144 <= 0)
m.e203 = Constraint(expr= -10 * m.b8 + m.x146 <= 0)
m.e204 = Constraint(expr= -10 * m.b9 + m.x148 <= 0)
m.e205 = Constraint(expr= -10 * m.b10 + m.x150 <= 0)
m.e206 = Constraint(expr= -10 * m.b11 + m.x152 <= 0)
m.e207 = Constraint(expr= -10 * m.b12 + m.x154 <= 0)
m.e208 = Constraint(expr= -10 * m.b13 + m.x156 <= 0)
m.e209 = Constraint(expr= -10 * m.b14 + m.x158 <= 0)
m.e210 = Constraint(expr= -10 * m.b15 + m.x160 <= 0)
m.e211 = Constraint(expr= -10 * m.b16 + m.x162 <= 0)
m.e212 = Constraint(expr= -10 * m.b17 + m.x164 <= 0)
m.e213 = Constraint(expr= -10 * m.b18 + m.x166 <= 0)
m.e214 = Constraint(expr= -10 * m.b19 + m.x168 <= 0)
m.e215 = Constraint(expr= -10 * m.b20 + m.x170 <= 0)
m.e216 = Constraint(expr= -10 * m.b21 + m.x171 <= 0)
m.e217 = Constraint(expr= -10 * m.b22 + m.x173 <= 0)
m.e218 = Constraint(expr= -10 * m.b23 + m.x175 <= 0)
m.e219 = Constraint(expr= -10 * m.b24 + m.x177 <= 0)
m.e220 = Constraint(expr= -10 * m.b25 + m.x179 <= 0)
m.e221 = Constraint(expr= -10 * m.b26 + m.x181 <= 0)
m.e222 = Constraint(expr= -10 * m.b27 + m.x183 <= 0)
m.e223 = Constraint(expr= -10 * m.b28 + m.x185 <= 0)
m.e224 = Constraint(expr= -10 * m.b29 + m.x187 <= 0)
m.e225 = Constraint(expr= -10 * m.b30 + m.x189 <= 0)
m.e226 = Constraint(expr= -10 * m.b31 + m.x191 <= 0)
m.e227 = Constraint(expr= -10 * m.b32 + m.x193 <= 0)
m.e228 = Constraint(expr= -10 * m.b33 + m.x195 <= 0)
m.e229 = Constraint(expr= -10 * m.b34 + m.x197 <= 0)
m.e230 = Constraint(expr= -10 * m.b35 + m.x199 <= 0)
m.e231 = Constraint(expr= -10 * m.b36 + m.x201 <= 0)
m.e232 = Constraint(expr= -10 * m.b37 + m.x203 <= 0)
m.e233 = Constraint(expr= -10 * m.b38 + m.x205 <= 0)
m.e234 = Constraint(expr= -10 * m.b39 + m.x207 <= 0)
m.e235 = Constraint(expr= -10 * m.b40 + m.x209 <= 0)
m.e236 = Constraint(expr= -10 * m.b21 + m.x172 <= 0)
m.e237 = Constraint(expr= -10 * m.b22 + m.x174 <= 0)
m.e238 = Constraint(expr= -10 * m.b23 + m.x176 <= 0)
m.e239 = Constraint(expr= -10 * m.b24 + m.x178 <= 0)
m.e240 = Constraint(expr= -10 * m.b25 + m.x180 <= 0)
m.e241 = Constraint(expr= -10 * m.b26 + m.x182 <= 0)
m.e242 = Constraint(expr= -10 * m.b27 + m.x184 <= 0)
m.e243 = Constraint(expr= -10 * m.b28 + m.x186 <= 0)
m.e244 = Constraint(expr= -10 * m.b29 + m.x188 <= 0)
m.e245 = Constraint(expr= -10 * m.b30 + m.x190 <= 0)
m.e246 = Constraint(expr= -10 * m.b31 + m.x192 <= 0)
m.e247 = Constraint(expr= -10 * m.b32 + m.x194 <= 0)
m.e248 = Constraint(expr= -10 * m.b33 + m.x196 <= 0)
m.e249 = Constraint(expr= -10 * m.b34 + m.x198 <= 0)
m.e250 = Constraint(expr= -10 * m.b35 + m.x200 <= 0)
m.e251 = Constraint(expr= -10 * m.b36 + m.x202 <= 0)
m.e252 = Constraint(expr= -10 * m.b37 + m.x204 <= 0)
m.e253 = Constraint(expr= -10 * m.b38 + m.x206 <= 0)
m.e254 = Constraint(expr= -10 * m.b39 + m.x208 <= 0)
m.e255 = Constraint(expr= -10 * m.b40 + m.x210 <= 0)
m.e256 = Constraint(expr= -10 * m.b41 + m.x211 <= 0)
m.e257 = Constraint(expr= -10 * m.b42 + m.x213 <= 0)
m.e258 = Constraint(expr= -10 * m.b43 + m.x215 <= 0)
m.e259 = Constraint(expr= -10 * m.b44 + m.x217 <= 0)
m.e260 = Constraint(expr= -10 * m.b45 + m.x219 <= 0)
m.e261 = Constraint(expr= -10 * m.b46 + m.x221 <= 0)
m.e262 = Constraint(expr= -10 * m.b47 + m.x223 <= 0)
m.e263 = Constraint(expr= -10 * m.b48 + m.x225 <= 0)
m.e264 = Constraint(expr= -10 * m.b49 + m.x227 <= 0)
m.e265 = Constraint(expr= -10 * m.b50 + m.x229 <= 0)
m.e266 = Constraint(expr= -10 * m.b51 + m.x231 <= 0)
m.e267 = Constraint(expr= -10 * m.b52 + m.x233 <= 0)
m.e268 = Constraint(expr= -10 * m.b53 + m.x235 <= 0)
m.e269 = Constraint(expr= -10 * m.b54 + m.x237 <= 0)
m.e270 = Constraint(expr= -10 * m.b55 + m.x239 <= 0)
m.e271 = Constraint(expr= -10 * m.b56 + m.x241 <= 0)
m.e272 = Constraint(expr= -10 * m.b57 + m.x243 <= 0)
m.e273 = Constraint(expr= -10 * m.b58 + m.x245 <= 0)
m.e274 = Constraint(expr= -10 * m.b59 + m.x247 <= 0)
m.e275 = Constraint(expr= -10 * m.b60 + m.x249 <= 0)
m.e276 = Constraint(expr= -10 * m.b41 + m.x212 <= 0)
m.e277 = Constraint(expr= -10 * m.b42 + m.x214 <= 0)
m.e278 = Constraint(expr= -10 * m.b43 + m.x216 <= 0)
m.e279 = Constraint(expr= -10 * m.b44 + m.x218 <= 0)
m.e280 = Constraint(expr= -10 * m.b45 + m.x220 <= 0)
m.e281 = Constraint(expr= -10 * m.b46 + m.x222 <= 0)
m.e282 = Constraint(expr= -10 * m.b47 + m.x224 <= 0)
m.e283 = Constraint(expr= -10 * m.b48 + m.x226 <= 0)
m.e284 = Constraint(expr= -10 * m.b49 + m.x228 <= 0)
m.e285 = Constraint(expr= -10 * m.b50 + m.x230 <= 0)
m.e286 = Constraint(expr= -10 * m.b51 + m.x232 <= 0)
m.e287 = Constraint(expr= -10 * m.b52 + m.x234 <= 0)
m.e288 = Constraint(expr= -10 * m.b53 + m.x236 <= 0)
m.e289 = Constraint(expr= -10 * m.b54 + m.x238 <= 0)
m.e290 = Constraint(expr= -10 * m.b55 + m.x240 <= 0)
m.e291 = Constraint(expr= -10 * m.b56 + m.x242 <= 0)
m.e292 = Constraint(expr= -10 * m.b57 + m.x244 <= 0)
m.e293 = Constraint(expr= -10 * m.b58 + m.x246 <= 0)
m.e294 = Constraint(expr= -10 * m.b59 + m.x248 <= 0)
m.e295 = Constraint(expr= -10 * m.b60 + m.x250 <= 0)
m.e296 = Constraint(expr= -10 * m.b61 + m.x251 <= 0)
m.e297 = Constraint(expr= -10 * m.b62 + m.x253 <= 0)
m.e298 = Constraint(expr= -10 * m.b63 + m.x255 <= 0)
m.e299 = Constraint(expr= -10 * m.b64 + m.x257 <= 0)
m.e300 = Constraint(expr= -10 * m.b65 + m.x259 <= 0)
m.e301 = Constraint(expr= -10 * m.b66 + m.x261 <= 0)
m.e302 = Constraint(expr= -10 * m.b67 + m.x263 <= 0)
m.e303 = Constraint(expr= -10 * m.b68 + m.x265 <= 0)
m.e304 = Constraint(expr= -10 * m.b69 + m.x267 <= 0)
m.e305 = Constraint(expr= -10 * m.b70 + m.x269 <= 0)
m.e306 = Constraint(expr= -10 * m.b71 + m.x271 <= 0)
m.e307 = Constraint(expr= -10 * m.b72 + m.x273 <= 0)
m.e308 = Constraint(expr= -10 * m.b73 + m.x275 <= 0)
m.e309 = Constraint(expr= -10 * m.b74 + m.x277 <= 0)
m.e310 = Constraint(expr= -10 * m.b75 + m.x279 <= 0)
m.e311 = Constraint(expr= -10 * m.b76 + m.x281 <= 0)
m.e312 = Constraint(expr= -10 * m.b77 + m.x283 <= 0)
m.e313 = Constraint(expr= -10 * m.b78 + m.x285 <= 0)
m.e314 = Constraint(expr= -10 * m.b79 + m.x287 <= 0)
m.e315 = Constraint(expr= -10 * m.b80 + m.x289 <= 0)
m.e316 = Constraint(expr= -10 * m.b61 + m.x252 <= 0)
m.e317 = Constraint(expr= -10 * m.b62 + m.x254 <= 0)
m.e318 = Constraint(expr= -10 * m.b63 + m.x256 <= 0)
m.e319 = Constraint(expr= -10 * m.b64 + m.x258 <= 0)
m.e320 = Constraint(expr= -10 * m.b65 + m.x260 <= 0)
m.e321 = Constraint(expr= -10 * m.b66 + m.x262 <= 0)
m.e322 = Constraint(expr= -10 * m.b67 + m.x264 <= 0)
m.e323 = Constraint(expr= -10 * m.b68 + m.x266 <= 0)
m.e324 = Constraint(expr= -10 * m.b69 + m.x268 <= 0)
m.e325 = Constraint(expr= -10 * m.b70 + m.x270 <= 0)
m.e326 = Constraint(expr= -10 * m.b71 + m.x272 <= 0)
m.e327 = Constraint(expr= -10 * m.b72 + m.x274 <= 0)
m.e328 = Constraint(expr= -10 * m.b73 + m.x276 <= 0)
m.e329 = Constraint(expr= -10 * m.b74 + m.x278 <= 0)
m.e330 = Constraint(expr= -10 * m.b75 + m.x280 <= 0)
m.e331 = Constraint(expr= -10 * m.b76 + m.x282 <= 0)
m.e332 = Constraint(expr= -10 * m.b77 + m.x284 <= 0)
m.e333 = Constraint(expr= -10 * m.b78 + m.x286 <= 0)
m.e334 = Constraint(expr= -10 * m.b79 + m.x288 <= 0)
m.e335 = Constraint(expr= -10 * m.b80 + m.x290 <= 0)
m.e336 = Constraint(expr= -10 * m.b81 + m.x291 <= 0)
m.e337 = Constraint(expr= -10 * m.b82 + m.x293 <= 0)
m.e338 = Constraint(expr= -10 * m.b83 + m.x295 <= 0)
m.e339 = Constraint(expr= -10 * m.b84 + m.x297 <= 0)
m.e340 = Constraint(expr= -10 * m.b85 + m.x299 <= 0)
m.e341 = Constraint(expr= -10 * m.b86 + m.x301 <= 0)
m.e342 = Constraint(expr= -10 * m.b87 + m.x303 <= 0)
m.e343 = Constraint(expr= -10 * m.b88 + m.x305 <= 0)
m.e344 = Constraint(expr= -10 * m.b89 + m.x307 <= 0)
m.e345 = Constraint(expr= -10 * m.b90 + m.x309 <= 0)
m.e346 = Constraint(expr= -10 * m.b91 + m.x311 <= 0)
m.e347 = Constraint(expr= -10 * m.b92 + m.x313 <= 0)
m.e348 = Constraint(expr= -10 * m.b93 + m.x315 <= 0)
m.e349 = Constraint(expr= -10 * m.b94 + m.x317 <= 0)
m.e350 = Constraint(expr= -10 * m.b95 + m.x319 <= 0)
m.e351 = Constraint(expr= -10 * m.b96 + m.x321 <= 0)
m.e352 = Constraint(expr= -10 * m.b97 + m.x323 <= 0)
m.e353 = Constraint(expr= -10 * m.b98 + m.x325 <= 0)
m.e354 = Constraint(expr= -10 * m.b99 + m.x327 <= 0)
m.e355 = Constraint(expr= -10 * m.b100 + m.x329 <= 0)
m.e356 = Constraint(expr= -10 * m.b81 + m.x292 <= 0)
m.e357 = Constraint(expr= -10 * m.b82 + m.x294 <= 0)
m.e358 = Constraint(expr= -10 * m.b83 + m.x296 <= 0)
m.e359 = Constraint(expr= -10 * m.b84 + m.x298 <= 0)
m.e360 = Constraint(expr= -10 * m.b85 + m.x300 <= 0)
m.e361 = Constraint(expr= -10 * m.b86 + m.x302 <= 0)
m.e362 = Constraint(expr= -10 * m.b87 + m.x304 <= 0)
m.e363 = Constraint(expr= -10 * m.b88 + m.x306 <= 0)
m.e364 = Constraint(expr= -10 * m.b89 + m.x308 <= 0)
m.e365 = Constraint(expr= -10 * m.b90 + m.x310 <= 0)
m.e366 = Constraint(expr= -10 * m.b91 + m.x312 <= 0)
m.e367 = Constraint(expr= -10 * m.b92 + m.x314 <= 0)
m.e368 = Constraint(expr= -10 * m.b93 + m.x316 <= 0)
m.e369 = Constraint(expr= -10 * m.b94 + m.x318 <= 0)
m.e370 = Constraint(expr= -10 * m.b95 + m.x320 <= 0)
m.e371 = Constraint(expr= -10 * m.b96 + m.x322 <= 0)
m.e372 = Constraint(expr= -10 * m.b97 + m.x324 <= 0)
m.e373 = Constraint(expr= -10 * m.b98 + m.x326 <= 0)
m.e374 = Constraint(expr= -10 * m.b99 + m.x328 <= 0)
m.e375 = Constraint(expr= -10 * m.b100 + m.x330 <= 0)
m.e376 = Constraint(expr= m.x101 - m.x102 <= 0)
m.e377 = Constraint(expr= m.x102 - m.x107 <= 0)
m.e378 = Constraint(expr= m.x107 - m.x111 <= 0)
m.e379 = Constraint(expr= m.x111 - m.x115 <= 0)
