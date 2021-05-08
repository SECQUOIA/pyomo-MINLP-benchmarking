# MINLP written by GAMS Convert at 05/07/21 17:13:00
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       450       28        0      422        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       364      294       70        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      1461     1181      280
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
m.x331 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x332 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x333 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x334 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x335 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x336 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x337 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x338 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x339 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x340 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x341 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x342 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x343 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x344 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x345 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x346 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x347 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x348 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x349 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x350 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x351 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x352 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x353 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x354 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x355 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x356 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x357 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x358 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x359 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x360 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x361 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x362 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x363 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x364 = Var(within=Reals, bounds=(0,10), initialize=0)

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
m.e127 = Constraint(expr= ((-m.x155 / (0.0001 + 0.9999 * m.b1) +
    4.13263517293428)**2 + (-m.x156 / (0.0001 + 0.9999 * m.b1) +
    9.89321475687716)**2 + (-m.x157 / (0.0001 + 0.9999 * m.b1) +
    7.00543632985936)**2 - 1) * (0.0001 + 0.9999 * m.b1) + 0.0163030509869979 *
    m.b1 <= 0.0163030509869979)
m.e128 = Constraint(expr= ((-m.x158 / (0.0001 + 0.9999 * m.b2) +
    5.36782363621885)**2 + (-m.x159 / (0.0001 + 0.9999 * m.b2) +
    1.51651713640814)**2 + (-m.x160 / (0.0001 + 0.9999 * m.b2) +
    6.16125243380265)**2 - 1) * (0.0001 + 0.9999 * m.b2) + 0.00680743863676083
    * m.b2 <= 0.00680743863676083)
m.e129 = Constraint(expr= ((-m.x161 / (0.0001 + 0.9999 * m.b3) +
    8.2275592328595)**2 + (-m.x162 / (0.0001 + 0.9999 * m.b3) +
    4.51338886533517)**2 + (-m.x163 / (0.0001 + 0.9999 * m.b3) +
    3.02091680975325)**2 - 1) * (0.0001 + 0.9999 * m.b3) + 0.00961893483513928
    * m.b3 <= 0.00961893483513928)
m.e130 = Constraint(expr= ((-m.x164 / (0.0001 + 0.9999 * m.b4) +
    4.45787019759725)**2 + (-m.x165 / (0.0001 + 0.9999 * m.b4) + 8.176601080562)
    **2 + (-m.x166 / (0.0001 + 0.9999 * m.b4) + 2.1384293807986)**2 - 1) * (
    0.0001 + 0.9999 * m.b4) + 0.00903022921459361 * m.b4
    <= 0.00903022921459361)
m.e131 = Constraint(expr= ((-m.x167 / (0.0001 + 0.9999 * m.b5) + 8.002643257644)
    **2 + (-m.x168 / (0.0001 + 0.9999 * m.b5) + 5.28236491095606)**2 + (-m.x169
    / (0.0001 + 0.9999 * m.b5) + 5.11938934174774)**2 - 1) * (0.0001 + 0.9999
    * m.b5) + 0.0117153825394015 * m.b5 <= 0.0117153825394015)
m.e132 = Constraint(expr= ((-m.x170 / (0.0001 + 0.9999 * m.b6) +
    6.24049438612365)**2 + (-m.x171 / (0.0001 + 0.9999 * m.b6) +
    3.8120863088984)**2 + (-m.x172 / (0.0001 + 0.9999 * m.b6) +
    9.50984985922338)**2 - 1) * (0.0001 + 0.9999 * m.b6) + 0.0142913016554702 *
    m.b6 <= 0.0142913016554702)
m.e133 = Constraint(expr= ((-m.x173 / (0.0001 + 0.9999 * m.b7) +
    4.54775219913353)**2 + (-m.x174 / (0.0001 + 0.9999 * m.b7) +
    5.50227429055218)**2 + (-m.x175 / (0.0001 + 0.9999 * m.b7) +
    3.5032816165688)**2 - 1) * (0.0001 + 0.9999 * m.b7) + 0.00622300545181842 *
    m.b7 <= 0.00622300545181842)
m.e134 = Constraint(expr= ((-m.x176 / (0.0001 + 0.9999 * m.b8) + 1.674156677828)
    **2 + (-m.x177 / (0.0001 + 0.9999 * m.b8) + 4.99633600480765)**2 + (-m.x178
    / (0.0001 + 0.9999 * m.b8) + 1.42648309916894)**2 - 1) * (0.0001 + 0.9999
    * m.b8) + 0.0028801028087068 * m.b8 <= 0.0028801028087068)
m.e135 = Constraint(expr= ((-m.x179 / (0.0001 + 0.9999 * m.b9) +
    1.82060210212647)**2 + (-m.x180 / (0.0001 + 0.9999 * m.b9) +
    8.61550724971434)**2 + (-m.x181 / (0.0001 + 0.9999 * m.b9) +
    4.93467653333678)**2 - 1) * (0.0001 + 0.9999 * m.b9) + 0.0100892589672812 *
    m.b9 <= 0.0100892589672812)
m.e136 = Constraint(expr= ((-m.x182 / (0.0001 + 0.9999 * m.b10) +
    6.61159251106337)**2 + (-m.x183 / (0.0001 + 0.9999 * m.b10) +
    9.89217063451911)**2 + (-m.x184 / (0.0001 + 0.9999 * m.b10) +
    4.74850918126831)**2 - 1) * (0.0001 + 0.9999 * m.b10) + 0.0163116534839381
    * m.b10 <= 0.0163116534839381)
m.e137 = Constraint(expr= m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8
    + m.b9 + m.b10 == 1)
m.e138 = Constraint(expr= ((-m.x185 / (0.0001 + 0.9999 * m.b11) +
    4.13263517293428)**2 + (-m.x186 / (0.0001 + 0.9999 * m.b11) +
    9.89321475687716)**2 + (-m.x187 / (0.0001 + 0.9999 * m.b11) +
    7.00543632985936)**2 - 1) * (0.0001 + 0.9999 * m.b11) + 0.0163030509869979
    * m.b11 <= 0.0163030509869979)
m.e139 = Constraint(expr= ((-m.x188 / (0.0001 + 0.9999 * m.b12) +
    5.36782363621885)**2 + (-m.x189 / (0.0001 + 0.9999 * m.b12) +
    1.51651713640814)**2 + (-m.x190 / (0.0001 + 0.9999 * m.b12) +
    6.16125243380265)**2 - 1) * (0.0001 + 0.9999 * m.b12) + 0.00680743863676083
    * m.b12 <= 0.00680743863676083)
m.e140 = Constraint(expr= ((-m.x191 / (0.0001 + 0.9999 * m.b13) +
    8.2275592328595)**2 + (-m.x192 / (0.0001 + 0.9999 * m.b13) +
    4.51338886533517)**2 + (-m.x193 / (0.0001 + 0.9999 * m.b13) +
    3.02091680975325)**2 - 1) * (0.0001 + 0.9999 * m.b13) + 0.00961893483513928
    * m.b13 <= 0.00961893483513928)
m.e141 = Constraint(expr= ((-m.x194 / (0.0001 + 0.9999 * m.b14) +
    4.45787019759725)**2 + (-m.x195 / (0.0001 + 0.9999 * m.b14) +
    8.176601080562)**2 + (-m.x196 / (0.0001 + 0.9999 * m.b14) + 2.1384293807986)
    **2 - 1) * (0.0001 + 0.9999 * m.b14) + 0.00903022921459361 * m.b14
    <= 0.00903022921459361)
m.e142 = Constraint(expr= ((-m.x197 / (0.0001 + 0.9999 * m.b15) +
    8.002643257644)**2 + (-m.x198 / (0.0001 + 0.9999 * m.b15) +
    5.28236491095606)**2 + (-m.x199 / (0.0001 + 0.9999 * m.b15) +
    5.11938934174774)**2 - 1) * (0.0001 + 0.9999 * m.b15) + 0.0117153825394015
    * m.b15 <= 0.0117153825394015)
m.e143 = Constraint(expr= ((-m.x200 / (0.0001 + 0.9999 * m.b16) +
    6.24049438612365)**2 + (-m.x201 / (0.0001 + 0.9999 * m.b16) +
    3.8120863088984)**2 + (-m.x202 / (0.0001 + 0.9999 * m.b16) +
    9.50984985922338)**2 - 1) * (0.0001 + 0.9999 * m.b16) + 0.0142913016554702
    * m.b16 <= 0.0142913016554702)
m.e144 = Constraint(expr= ((-m.x203 / (0.0001 + 0.9999 * m.b17) +
    4.54775219913353)**2 + (-m.x204 / (0.0001 + 0.9999 * m.b17) +
    5.50227429055218)**2 + (-m.x205 / (0.0001 + 0.9999 * m.b17) +
    3.5032816165688)**2 - 1) * (0.0001 + 0.9999 * m.b17) + 0.00622300545181842
    * m.b17 <= 0.00622300545181842)
m.e145 = Constraint(expr= ((-m.x206 / (0.0001 + 0.9999 * m.b18) +
    1.674156677828)**2 + (-m.x207 / (0.0001 + 0.9999 * m.b18) +
    4.99633600480765)**2 + (-m.x208 / (0.0001 + 0.9999 * m.b18) +
    1.42648309916894)**2 - 1) * (0.0001 + 0.9999 * m.b18) + 0.0028801028087068
    * m.b18 <= 0.0028801028087068)
m.e146 = Constraint(expr= ((-m.x209 / (0.0001 + 0.9999 * m.b19) +
    1.82060210212647)**2 + (-m.x210 / (0.0001 + 0.9999 * m.b19) +
    8.61550724971434)**2 + (-m.x211 / (0.0001 + 0.9999 * m.b19) +
    4.93467653333678)**2 - 1) * (0.0001 + 0.9999 * m.b19) + 0.0100892589672812
    * m.b19 <= 0.0100892589672812)
m.e147 = Constraint(expr= ((-m.x212 / (0.0001 + 0.9999 * m.b20) +
    6.61159251106337)**2 + (-m.x213 / (0.0001 + 0.9999 * m.b20) +
    9.89217063451911)**2 + (-m.x214 / (0.0001 + 0.9999 * m.b20) +
    4.74850918126831)**2 - 1) * (0.0001 + 0.9999 * m.b20) + 0.0163116534839381
    * m.b20 <= 0.0163116534839381)
m.e148 = Constraint(expr= m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17
    + m.b18 + m.b19 + m.b20 == 1)
m.e149 = Constraint(expr= ((-m.x215 / (0.0001 + 0.9999 * m.b21) +
    4.13263517293428)**2 + (-m.x216 / (0.0001 + 0.9999 * m.b21) +
    9.89321475687716)**2 + (-m.x217 / (0.0001 + 0.9999 * m.b21) +
    7.00543632985936)**2 - 1) * (0.0001 + 0.9999 * m.b21) + 0.0163030509869979
    * m.b21 <= 0.0163030509869979)
m.e150 = Constraint(expr= ((-m.x218 / (0.0001 + 0.9999 * m.b22) +
    5.36782363621885)**2 + (-m.x219 / (0.0001 + 0.9999 * m.b22) +
    1.51651713640814)**2 + (-m.x220 / (0.0001 + 0.9999 * m.b22) +
    6.16125243380265)**2 - 1) * (0.0001 + 0.9999 * m.b22) + 0.00680743863676083
    * m.b22 <= 0.00680743863676083)
m.e151 = Constraint(expr= ((-m.x221 / (0.0001 + 0.9999 * m.b23) +
    8.2275592328595)**2 + (-m.x222 / (0.0001 + 0.9999 * m.b23) +
    4.51338886533517)**2 + (-m.x223 / (0.0001 + 0.9999 * m.b23) +
    3.02091680975325)**2 - 1) * (0.0001 + 0.9999 * m.b23) + 0.00961893483513928
    * m.b23 <= 0.00961893483513928)
m.e152 = Constraint(expr= ((-m.x224 / (0.0001 + 0.9999 * m.b24) +
    4.45787019759725)**2 + (-m.x225 / (0.0001 + 0.9999 * m.b24) +
    8.176601080562)**2 + (-m.x226 / (0.0001 + 0.9999 * m.b24) + 2.1384293807986)
    **2 - 1) * (0.0001 + 0.9999 * m.b24) + 0.00903022921459361 * m.b24
    <= 0.00903022921459361)
m.e153 = Constraint(expr= ((-m.x227 / (0.0001 + 0.9999 * m.b25) +
    8.002643257644)**2 + (-m.x228 / (0.0001 + 0.9999 * m.b25) +
    5.28236491095606)**2 + (-m.x229 / (0.0001 + 0.9999 * m.b25) +
    5.11938934174774)**2 - 1) * (0.0001 + 0.9999 * m.b25) + 0.0117153825394015
    * m.b25 <= 0.0117153825394015)
m.e154 = Constraint(expr= ((-m.x230 / (0.0001 + 0.9999 * m.b26) +
    6.24049438612365)**2 + (-m.x231 / (0.0001 + 0.9999 * m.b26) +
    3.8120863088984)**2 + (-m.x232 / (0.0001 + 0.9999 * m.b26) +
    9.50984985922338)**2 - 1) * (0.0001 + 0.9999 * m.b26) + 0.0142913016554702
    * m.b26 <= 0.0142913016554702)
m.e155 = Constraint(expr= ((-m.x233 / (0.0001 + 0.9999 * m.b27) +
    4.54775219913353)**2 + (-m.x234 / (0.0001 + 0.9999 * m.b27) +
    5.50227429055218)**2 + (-m.x235 / (0.0001 + 0.9999 * m.b27) +
    3.5032816165688)**2 - 1) * (0.0001 + 0.9999 * m.b27) + 0.00622300545181842
    * m.b27 <= 0.00622300545181842)
m.e156 = Constraint(expr= ((-m.x236 / (0.0001 + 0.9999 * m.b28) +
    1.674156677828)**2 + (-m.x237 / (0.0001 + 0.9999 * m.b28) +
    4.99633600480765)**2 + (-m.x238 / (0.0001 + 0.9999 * m.b28) +
    1.42648309916894)**2 - 1) * (0.0001 + 0.9999 * m.b28) + 0.0028801028087068
    * m.b28 <= 0.0028801028087068)
m.e157 = Constraint(expr= ((-m.x239 / (0.0001 + 0.9999 * m.b29) +
    1.82060210212647)**2 + (-m.x240 / (0.0001 + 0.9999 * m.b29) +
    8.61550724971434)**2 + (-m.x241 / (0.0001 + 0.9999 * m.b29) +
    4.93467653333678)**2 - 1) * (0.0001 + 0.9999 * m.b29) + 0.0100892589672812
    * m.b29 <= 0.0100892589672812)
m.e158 = Constraint(expr= ((-m.x242 / (0.0001 + 0.9999 * m.b30) +
    6.61159251106337)**2 + (-m.x243 / (0.0001 + 0.9999 * m.b30) +
    9.89217063451911)**2 + (-m.x244 / (0.0001 + 0.9999 * m.b30) +
    4.74850918126831)**2 - 1) * (0.0001 + 0.9999 * m.b30) + 0.0163116534839381
    * m.b30 <= 0.0163116534839381)
m.e159 = Constraint(expr= m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 + m.b27
    + m.b28 + m.b29 + m.b30 == 1)
m.e160 = Constraint(expr= ((-m.x245 / (0.0001 + 0.9999 * m.b31) +
    4.13263517293428)**2 + (-m.x246 / (0.0001 + 0.9999 * m.b31) +
    9.89321475687716)**2 + (-m.x247 / (0.0001 + 0.9999 * m.b31) +
    7.00543632985936)**2 - 1) * (0.0001 + 0.9999 * m.b31) + 0.0163030509869979
    * m.b31 <= 0.0163030509869979)
m.e161 = Constraint(expr= ((-m.x248 / (0.0001 + 0.9999 * m.b32) +
    5.36782363621885)**2 + (-m.x249 / (0.0001 + 0.9999 * m.b32) +
    1.51651713640814)**2 + (-m.x250 / (0.0001 + 0.9999 * m.b32) +
    6.16125243380265)**2 - 1) * (0.0001 + 0.9999 * m.b32) + 0.00680743863676083
    * m.b32 <= 0.00680743863676083)
m.e162 = Constraint(expr= ((-m.x251 / (0.0001 + 0.9999 * m.b33) +
    8.2275592328595)**2 + (-m.x252 / (0.0001 + 0.9999 * m.b33) +
    4.51338886533517)**2 + (-m.x253 / (0.0001 + 0.9999 * m.b33) +
    3.02091680975325)**2 - 1) * (0.0001 + 0.9999 * m.b33) + 0.00961893483513928
    * m.b33 <= 0.00961893483513928)
m.e163 = Constraint(expr= ((-m.x254 / (0.0001 + 0.9999 * m.b34) +
    4.45787019759725)**2 + (-m.x255 / (0.0001 + 0.9999 * m.b34) +
    8.176601080562)**2 + (-m.x256 / (0.0001 + 0.9999 * m.b34) + 2.1384293807986)
    **2 - 1) * (0.0001 + 0.9999 * m.b34) + 0.00903022921459361 * m.b34
    <= 0.00903022921459361)
m.e164 = Constraint(expr= ((-m.x257 / (0.0001 + 0.9999 * m.b35) +
    8.002643257644)**2 + (-m.x258 / (0.0001 + 0.9999 * m.b35) +
    5.28236491095606)**2 + (-m.x259 / (0.0001 + 0.9999 * m.b35) +
    5.11938934174774)**2 - 1) * (0.0001 + 0.9999 * m.b35) + 0.0117153825394015
    * m.b35 <= 0.0117153825394015)
m.e165 = Constraint(expr= ((-m.x260 / (0.0001 + 0.9999 * m.b36) +
    6.24049438612365)**2 + (-m.x261 / (0.0001 + 0.9999 * m.b36) +
    3.8120863088984)**2 + (-m.x262 / (0.0001 + 0.9999 * m.b36) +
    9.50984985922338)**2 - 1) * (0.0001 + 0.9999 * m.b36) + 0.0142913016554702
    * m.b36 <= 0.0142913016554702)
m.e166 = Constraint(expr= ((-m.x263 / (0.0001 + 0.9999 * m.b37) +
    4.54775219913353)**2 + (-m.x264 / (0.0001 + 0.9999 * m.b37) +
    5.50227429055218)**2 + (-m.x265 / (0.0001 + 0.9999 * m.b37) +
    3.5032816165688)**2 - 1) * (0.0001 + 0.9999 * m.b37) + 0.00622300545181842
    * m.b37 <= 0.00622300545181842)
m.e167 = Constraint(expr= ((-m.x266 / (0.0001 + 0.9999 * m.b38) +
    1.674156677828)**2 + (-m.x267 / (0.0001 + 0.9999 * m.b38) +
    4.99633600480765)**2 + (-m.x268 / (0.0001 + 0.9999 * m.b38) +
    1.42648309916894)**2 - 1) * (0.0001 + 0.9999 * m.b38) + 0.0028801028087068
    * m.b38 <= 0.0028801028087068)
m.e168 = Constraint(expr= ((-m.x269 / (0.0001 + 0.9999 * m.b39) +
    1.82060210212647)**2 + (-m.x270 / (0.0001 + 0.9999 * m.b39) +
    8.61550724971434)**2 + (-m.x271 / (0.0001 + 0.9999 * m.b39) +
    4.93467653333678)**2 - 1) * (0.0001 + 0.9999 * m.b39) + 0.0100892589672812
    * m.b39 <= 0.0100892589672812)
m.e169 = Constraint(expr= ((-m.x272 / (0.0001 + 0.9999 * m.b40) +
    6.61159251106337)**2 + (-m.x273 / (0.0001 + 0.9999 * m.b40) +
    9.89217063451911)**2 + (-m.x274 / (0.0001 + 0.9999 * m.b40) +
    4.74850918126831)**2 - 1) * (0.0001 + 0.9999 * m.b40) + 0.0163116534839381
    * m.b40 <= 0.0163116534839381)
m.e170 = Constraint(expr= m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 + m.b37
    + m.b38 + m.b39 + m.b40 == 1)
m.e171 = Constraint(expr= ((-m.x275 / (0.0001 + 0.9999 * m.b41) +
    4.13263517293428)**2 + (-m.x276 / (0.0001 + 0.9999 * m.b41) +
    9.89321475687716)**2 + (-m.x277 / (0.0001 + 0.9999 * m.b41) +
    7.00543632985936)**2 - 1) * (0.0001 + 0.9999 * m.b41) + 0.0163030509869979
    * m.b41 <= 0.0163030509869979)
m.e172 = Constraint(expr= ((-m.x278 / (0.0001 + 0.9999 * m.b42) +
    5.36782363621885)**2 + (-m.x279 / (0.0001 + 0.9999 * m.b42) +
    1.51651713640814)**2 + (-m.x280 / (0.0001 + 0.9999 * m.b42) +
    6.16125243380265)**2 - 1) * (0.0001 + 0.9999 * m.b42) + 0.00680743863676083
    * m.b42 <= 0.00680743863676083)
m.e173 = Constraint(expr= ((-m.x281 / (0.0001 + 0.9999 * m.b43) +
    8.2275592328595)**2 + (-m.x282 / (0.0001 + 0.9999 * m.b43) +
    4.51338886533517)**2 + (-m.x283 / (0.0001 + 0.9999 * m.b43) +
    3.02091680975325)**2 - 1) * (0.0001 + 0.9999 * m.b43) + 0.00961893483513928
    * m.b43 <= 0.00961893483513928)
m.e174 = Constraint(expr= ((-m.x284 / (0.0001 + 0.9999 * m.b44) +
    4.45787019759725)**2 + (-m.x285 / (0.0001 + 0.9999 * m.b44) +
    8.176601080562)**2 + (-m.x286 / (0.0001 + 0.9999 * m.b44) + 2.1384293807986)
    **2 - 1) * (0.0001 + 0.9999 * m.b44) + 0.00903022921459361 * m.b44
    <= 0.00903022921459361)
m.e175 = Constraint(expr= ((-m.x287 / (0.0001 + 0.9999 * m.b45) +
    8.002643257644)**2 + (-m.x288 / (0.0001 + 0.9999 * m.b45) +
    5.28236491095606)**2 + (-m.x289 / (0.0001 + 0.9999 * m.b45) +
    5.11938934174774)**2 - 1) * (0.0001 + 0.9999 * m.b45) + 0.0117153825394015
    * m.b45 <= 0.0117153825394015)
m.e176 = Constraint(expr= ((-m.x290 / (0.0001 + 0.9999 * m.b46) +
    6.24049438612365)**2 + (-m.x291 / (0.0001 + 0.9999 * m.b46) +
    3.8120863088984)**2 + (-m.x292 / (0.0001 + 0.9999 * m.b46) +
    9.50984985922338)**2 - 1) * (0.0001 + 0.9999 * m.b46) + 0.0142913016554702
    * m.b46 <= 0.0142913016554702)
m.e177 = Constraint(expr= ((-m.x293 / (0.0001 + 0.9999 * m.b47) +
    4.54775219913353)**2 + (-m.x294 / (0.0001 + 0.9999 * m.b47) +
    5.50227429055218)**2 + (-m.x295 / (0.0001 + 0.9999 * m.b47) +
    3.5032816165688)**2 - 1) * (0.0001 + 0.9999 * m.b47) + 0.00622300545181842
    * m.b47 <= 0.00622300545181842)
m.e178 = Constraint(expr= ((-m.x296 / (0.0001 + 0.9999 * m.b48) +
    1.674156677828)**2 + (-m.x297 / (0.0001 + 0.9999 * m.b48) +
    4.99633600480765)**2 + (-m.x298 / (0.0001 + 0.9999 * m.b48) +
    1.42648309916894)**2 - 1) * (0.0001 + 0.9999 * m.b48) + 0.0028801028087068
    * m.b48 <= 0.0028801028087068)
m.e179 = Constraint(expr= ((-m.x299 / (0.0001 + 0.9999 * m.b49) +
    1.82060210212647)**2 + (-m.x300 / (0.0001 + 0.9999 * m.b49) +
    8.61550724971434)**2 + (-m.x301 / (0.0001 + 0.9999 * m.b49) +
    4.93467653333678)**2 - 1) * (0.0001 + 0.9999 * m.b49) + 0.0100892589672812
    * m.b49 <= 0.0100892589672812)
m.e180 = Constraint(expr= ((-m.x302 / (0.0001 + 0.9999 * m.b50) +
    6.61159251106337)**2 + (-m.x303 / (0.0001 + 0.9999 * m.b50) +
    9.89217063451911)**2 + (-m.x304 / (0.0001 + 0.9999 * m.b50) +
    4.74850918126831)**2 - 1) * (0.0001 + 0.9999 * m.b50) + 0.0163116534839381
    * m.b50 <= 0.0163116534839381)
m.e181 = Constraint(expr= m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47
    + m.b48 + m.b49 + m.b50 == 1)
m.e182 = Constraint(expr= ((-m.x305 / (0.0001 + 0.9999 * m.b51) +
    4.13263517293428)**2 + (-m.x306 / (0.0001 + 0.9999 * m.b51) +
    9.89321475687716)**2 + (-m.x307 / (0.0001 + 0.9999 * m.b51) +
    7.00543632985936)**2 - 1) * (0.0001 + 0.9999 * m.b51) + 0.0163030509869979
    * m.b51 <= 0.0163030509869979)
m.e183 = Constraint(expr= ((-m.x308 / (0.0001 + 0.9999 * m.b52) +
    5.36782363621885)**2 + (-m.x309 / (0.0001 + 0.9999 * m.b52) +
    1.51651713640814)**2 + (-m.x310 / (0.0001 + 0.9999 * m.b52) +
    6.16125243380265)**2 - 1) * (0.0001 + 0.9999 * m.b52) + 0.00680743863676083
    * m.b52 <= 0.00680743863676083)
m.e184 = Constraint(expr= ((-m.x311 / (0.0001 + 0.9999 * m.b53) +
    8.2275592328595)**2 + (-m.x312 / (0.0001 + 0.9999 * m.b53) +
    4.51338886533517)**2 + (-m.x313 / (0.0001 + 0.9999 * m.b53) +
    3.02091680975325)**2 - 1) * (0.0001 + 0.9999 * m.b53) + 0.00961893483513928
    * m.b53 <= 0.00961893483513928)
m.e185 = Constraint(expr= ((-m.x314 / (0.0001 + 0.9999 * m.b54) +
    4.45787019759725)**2 + (-m.x315 / (0.0001 + 0.9999 * m.b54) +
    8.176601080562)**2 + (-m.x316 / (0.0001 + 0.9999 * m.b54) + 2.1384293807986)
    **2 - 1) * (0.0001 + 0.9999 * m.b54) + 0.00903022921459361 * m.b54
    <= 0.00903022921459361)
m.e186 = Constraint(expr= ((-m.x317 / (0.0001 + 0.9999 * m.b55) +
    8.002643257644)**2 + (-m.x318 / (0.0001 + 0.9999 * m.b55) +
    5.28236491095606)**2 + (-m.x319 / (0.0001 + 0.9999 * m.b55) +
    5.11938934174774)**2 - 1) * (0.0001 + 0.9999 * m.b55) + 0.0117153825394015
    * m.b55 <= 0.0117153825394015)
m.e187 = Constraint(expr= ((-m.x320 / (0.0001 + 0.9999 * m.b56) +
    6.24049438612365)**2 + (-m.x321 / (0.0001 + 0.9999 * m.b56) +
    3.8120863088984)**2 + (-m.x322 / (0.0001 + 0.9999 * m.b56) +
    9.50984985922338)**2 - 1) * (0.0001 + 0.9999 * m.b56) + 0.0142913016554702
    * m.b56 <= 0.0142913016554702)
m.e188 = Constraint(expr= ((-m.x323 / (0.0001 + 0.9999 * m.b57) +
    4.54775219913353)**2 + (-m.x324 / (0.0001 + 0.9999 * m.b57) +
    5.50227429055218)**2 + (-m.x325 / (0.0001 + 0.9999 * m.b57) +
    3.5032816165688)**2 - 1) * (0.0001 + 0.9999 * m.b57) + 0.00622300545181842
    * m.b57 <= 0.00622300545181842)
m.e189 = Constraint(expr= ((-m.x326 / (0.0001 + 0.9999 * m.b58) +
    1.674156677828)**2 + (-m.x327 / (0.0001 + 0.9999 * m.b58) +
    4.99633600480765)**2 + (-m.x328 / (0.0001 + 0.9999 * m.b58) +
    1.42648309916894)**2 - 1) * (0.0001 + 0.9999 * m.b58) + 0.0028801028087068
    * m.b58 <= 0.0028801028087068)
m.e190 = Constraint(expr= ((-m.x329 / (0.0001 + 0.9999 * m.b59) +
    1.82060210212647)**2 + (-m.x330 / (0.0001 + 0.9999 * m.b59) +
    8.61550724971434)**2 + (-m.x331 / (0.0001 + 0.9999 * m.b59) +
    4.93467653333678)**2 - 1) * (0.0001 + 0.9999 * m.b59) + 0.0100892589672812
    * m.b59 <= 0.0100892589672812)
m.e191 = Constraint(expr= ((-m.x332 / (0.0001 + 0.9999 * m.b60) +
    6.61159251106337)**2 + (-m.x333 / (0.0001 + 0.9999 * m.b60) +
    9.89217063451911)**2 + (-m.x334 / (0.0001 + 0.9999 * m.b60) +
    4.74850918126831)**2 - 1) * (0.0001 + 0.9999 * m.b60) + 0.0163116534839381
    * m.b60 <= 0.0163116534839381)
m.e192 = Constraint(expr= m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 + m.b57
    + m.b58 + m.b59 + m.b60 == 1)
m.e193 = Constraint(expr= ((-m.x335 / (0.0001 + 0.9999 * m.b61) +
    4.13263517293428)**2 + (-m.x336 / (0.0001 + 0.9999 * m.b61) +
    9.89321475687716)**2 + (-m.x337 / (0.0001 + 0.9999 * m.b61) +
    7.00543632985936)**2 - 1) * (0.0001 + 0.9999 * m.b61) + 0.0163030509869979
    * m.b61 <= 0.0163030509869979)
m.e194 = Constraint(expr= ((-m.x338 / (0.0001 + 0.9999 * m.b62) +
    5.36782363621885)**2 + (-m.x339 / (0.0001 + 0.9999 * m.b62) +
    1.51651713640814)**2 + (-m.x340 / (0.0001 + 0.9999 * m.b62) +
    6.16125243380265)**2 - 1) * (0.0001 + 0.9999 * m.b62) + 0.00680743863676083
    * m.b62 <= 0.00680743863676083)
m.e195 = Constraint(expr= ((-m.x341 / (0.0001 + 0.9999 * m.b63) +
    8.2275592328595)**2 + (-m.x342 / (0.0001 + 0.9999 * m.b63) +
    4.51338886533517)**2 + (-m.x343 / (0.0001 + 0.9999 * m.b63) +
    3.02091680975325)**2 - 1) * (0.0001 + 0.9999 * m.b63) + 0.00961893483513928
    * m.b63 <= 0.00961893483513928)
m.e196 = Constraint(expr= ((-m.x344 / (0.0001 + 0.9999 * m.b64) +
    4.45787019759725)**2 + (-m.x345 / (0.0001 + 0.9999 * m.b64) +
    8.176601080562)**2 + (-m.x346 / (0.0001 + 0.9999 * m.b64) + 2.1384293807986)
    **2 - 1) * (0.0001 + 0.9999 * m.b64) + 0.00903022921459361 * m.b64
    <= 0.00903022921459361)
m.e197 = Constraint(expr= ((-m.x347 / (0.0001 + 0.9999 * m.b65) +
    8.002643257644)**2 + (-m.x348 / (0.0001 + 0.9999 * m.b65) +
    5.28236491095606)**2 + (-m.x349 / (0.0001 + 0.9999 * m.b65) +
    5.11938934174774)**2 - 1) * (0.0001 + 0.9999 * m.b65) + 0.0117153825394015
    * m.b65 <= 0.0117153825394015)
m.e198 = Constraint(expr= ((-m.x350 / (0.0001 + 0.9999 * m.b66) +
    6.24049438612365)**2 + (-m.x351 / (0.0001 + 0.9999 * m.b66) +
    3.8120863088984)**2 + (-m.x352 / (0.0001 + 0.9999 * m.b66) +
    9.50984985922338)**2 - 1) * (0.0001 + 0.9999 * m.b66) + 0.0142913016554702
    * m.b66 <= 0.0142913016554702)
m.e199 = Constraint(expr= ((-m.x353 / (0.0001 + 0.9999 * m.b67) +
    4.54775219913353)**2 + (-m.x354 / (0.0001 + 0.9999 * m.b67) +
    5.50227429055218)**2 + (-m.x355 / (0.0001 + 0.9999 * m.b67) +
    3.5032816165688)**2 - 1) * (0.0001 + 0.9999 * m.b67) + 0.00622300545181842
    * m.b67 <= 0.00622300545181842)
m.e200 = Constraint(expr= ((-m.x356 / (0.0001 + 0.9999 * m.b68) +
    1.674156677828)**2 + (-m.x357 / (0.0001 + 0.9999 * m.b68) +
    4.99633600480765)**2 + (-m.x358 / (0.0001 + 0.9999 * m.b68) +
    1.42648309916894)**2 - 1) * (0.0001 + 0.9999 * m.b68) + 0.0028801028087068
    * m.b68 <= 0.0028801028087068)
m.e201 = Constraint(expr= ((-m.x359 / (0.0001 + 0.9999 * m.b69) +
    1.82060210212647)**2 + (-m.x360 / (0.0001 + 0.9999 * m.b69) +
    8.61550724971434)**2 + (-m.x361 / (0.0001 + 0.9999 * m.b69) +
    4.93467653333678)**2 - 1) * (0.0001 + 0.9999 * m.b69) + 0.0100892589672812
    * m.b69 <= 0.0100892589672812)
m.e202 = Constraint(expr= ((-m.x362 / (0.0001 + 0.9999 * m.b70) +
    6.61159251106337)**2 + (-m.x363 / (0.0001 + 0.9999 * m.b70) +
    9.89217063451911)**2 + (-m.x364 / (0.0001 + 0.9999 * m.b70) +
    4.74850918126831)**2 - 1) * (0.0001 + 0.9999 * m.b70) + 0.0163116534839381
    * m.b70 <= 0.0163116534839381)
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
m.e214 = Constraint(expr= -m.x71 + m.x155 + m.x158 + m.x161 + m.x164 + m.x167
    + m.x170 + m.x173 + m.x176 + m.x179 + m.x182 == 0)
m.e215 = Constraint(expr= -m.x74 + m.x156 + m.x159 + m.x162 + m.x165 + m.x168
    + m.x171 + m.x174 + m.x177 + m.x180 + m.x183 == 0)
m.e216 = Constraint(expr= -m.x77 + m.x157 + m.x160 + m.x163 + m.x166 + m.x169
    + m.x172 + m.x175 + m.x178 + m.x181 + m.x184 == 0)
m.e217 = Constraint(expr= -m.x72 + m.x185 + m.x188 + m.x191 + m.x194 + m.x197
    + m.x200 + m.x203 + m.x206 + m.x209 + m.x212 == 0)
m.e218 = Constraint(expr= -m.x75 + m.x186 + m.x189 + m.x192 + m.x195 + m.x198
    + m.x201 + m.x204 + m.x207 + m.x210 + m.x213 == 0)
m.e219 = Constraint(expr= -m.x78 + m.x187 + m.x190 + m.x193 + m.x196 + m.x199
    + m.x202 + m.x205 + m.x208 + m.x211 + m.x214 == 0)
m.e220 = Constraint(expr= -m.x80 + m.x215 + m.x218 + m.x221 + m.x224 + m.x227
    + m.x230 + m.x233 + m.x236 + m.x239 + m.x242 == 0)
m.e221 = Constraint(expr= -m.x82 + m.x216 + m.x219 + m.x222 + m.x225 + m.x228
    + m.x231 + m.x234 + m.x237 + m.x240 + m.x243 == 0)
m.e222 = Constraint(expr= -m.x84 + m.x217 + m.x220 + m.x223 + m.x226 + m.x229
    + m.x232 + m.x235 + m.x238 + m.x241 + m.x244 == 0)
m.e223 = Constraint(expr= -m.x86 + m.x245 + m.x248 + m.x251 + m.x254 + m.x257
    + m.x260 + m.x263 + m.x266 + m.x269 + m.x272 == 0)
m.e224 = Constraint(expr= -m.x88 + m.x246 + m.x249 + m.x252 + m.x255 + m.x258
    + m.x261 + m.x264 + m.x267 + m.x270 + m.x273 == 0)
m.e225 = Constraint(expr= -m.x90 + m.x247 + m.x250 + m.x253 + m.x256 + m.x259
    + m.x262 + m.x265 + m.x268 + m.x271 + m.x274 == 0)
m.e226 = Constraint(expr= -m.x92 + m.x275 + m.x278 + m.x281 + m.x284 + m.x287
    + m.x290 + m.x293 + m.x296 + m.x299 + m.x302 == 0)
m.e227 = Constraint(expr= -m.x94 + m.x276 + m.x279 + m.x282 + m.x285 + m.x288
    + m.x291 + m.x294 + m.x297 + m.x300 + m.x303 == 0)
m.e228 = Constraint(expr= -m.x96 + m.x277 + m.x280 + m.x283 + m.x286 + m.x289
    + m.x292 + m.x295 + m.x298 + m.x301 + m.x304 == 0)
m.e229 = Constraint(expr= -m.x98 + m.x305 + m.x308 + m.x311 + m.x314 + m.x317
    + m.x320 + m.x323 + m.x326 + m.x329 + m.x332 == 0)
m.e230 = Constraint(expr= -m.x100 + m.x306 + m.x309 + m.x312 + m.x315 + m.x318
    + m.x321 + m.x324 + m.x327 + m.x330 + m.x333 == 0)
m.e231 = Constraint(expr= -m.x102 + m.x307 + m.x310 + m.x313 + m.x316 + m.x319
    + m.x322 + m.x325 + m.x328 + m.x331 + m.x334 == 0)
m.e232 = Constraint(expr= -m.x104 + m.x335 + m.x338 + m.x341 + m.x344 + m.x347
    + m.x350 + m.x353 + m.x356 + m.x359 + m.x362 == 0)
m.e233 = Constraint(expr= -m.x106 + m.x336 + m.x339 + m.x342 + m.x345 + m.x348
    + m.x351 + m.x354 + m.x357 + m.x360 + m.x363 == 0)
m.e234 = Constraint(expr= -m.x108 + m.x337 + m.x340 + m.x343 + m.x346 + m.x349
    + m.x352 + m.x355 + m.x358 + m.x361 + m.x364 == 0)
m.e235 = Constraint(expr= -10 * m.b1 + m.x155 <= 0)
m.e236 = Constraint(expr= -10 * m.b2 + m.x158 <= 0)
m.e237 = Constraint(expr= -10 * m.b3 + m.x161 <= 0)
m.e238 = Constraint(expr= -10 * m.b4 + m.x164 <= 0)
m.e239 = Constraint(expr= -10 * m.b5 + m.x167 <= 0)
m.e240 = Constraint(expr= -10 * m.b6 + m.x170 <= 0)
m.e241 = Constraint(expr= -10 * m.b7 + m.x173 <= 0)
m.e242 = Constraint(expr= -10 * m.b8 + m.x176 <= 0)
m.e243 = Constraint(expr= -10 * m.b9 + m.x179 <= 0)
m.e244 = Constraint(expr= -10 * m.b10 + m.x182 <= 0)
m.e245 = Constraint(expr= -10 * m.b1 + m.x156 <= 0)
m.e246 = Constraint(expr= -10 * m.b2 + m.x159 <= 0)
m.e247 = Constraint(expr= -10 * m.b3 + m.x162 <= 0)
m.e248 = Constraint(expr= -10 * m.b4 + m.x165 <= 0)
m.e249 = Constraint(expr= -10 * m.b5 + m.x168 <= 0)
m.e250 = Constraint(expr= -10 * m.b6 + m.x171 <= 0)
m.e251 = Constraint(expr= -10 * m.b7 + m.x174 <= 0)
m.e252 = Constraint(expr= -10 * m.b8 + m.x177 <= 0)
m.e253 = Constraint(expr= -10 * m.b9 + m.x180 <= 0)
m.e254 = Constraint(expr= -10 * m.b10 + m.x183 <= 0)
m.e255 = Constraint(expr= -10 * m.b1 + m.x157 <= 0)
m.e256 = Constraint(expr= -10 * m.b2 + m.x160 <= 0)
m.e257 = Constraint(expr= -10 * m.b3 + m.x163 <= 0)
m.e258 = Constraint(expr= -10 * m.b4 + m.x166 <= 0)
m.e259 = Constraint(expr= -10 * m.b5 + m.x169 <= 0)
m.e260 = Constraint(expr= -10 * m.b6 + m.x172 <= 0)
m.e261 = Constraint(expr= -10 * m.b7 + m.x175 <= 0)
m.e262 = Constraint(expr= -10 * m.b8 + m.x178 <= 0)
m.e263 = Constraint(expr= -10 * m.b9 + m.x181 <= 0)
m.e264 = Constraint(expr= -10 * m.b10 + m.x184 <= 0)
m.e265 = Constraint(expr= -10 * m.b11 + m.x185 <= 0)
m.e266 = Constraint(expr= -10 * m.b12 + m.x188 <= 0)
m.e267 = Constraint(expr= -10 * m.b13 + m.x191 <= 0)
m.e268 = Constraint(expr= -10 * m.b14 + m.x194 <= 0)
m.e269 = Constraint(expr= -10 * m.b15 + m.x197 <= 0)
m.e270 = Constraint(expr= -10 * m.b16 + m.x200 <= 0)
m.e271 = Constraint(expr= -10 * m.b17 + m.x203 <= 0)
m.e272 = Constraint(expr= -10 * m.b18 + m.x206 <= 0)
m.e273 = Constraint(expr= -10 * m.b19 + m.x209 <= 0)
m.e274 = Constraint(expr= -10 * m.b20 + m.x212 <= 0)
m.e275 = Constraint(expr= -10 * m.b11 + m.x186 <= 0)
m.e276 = Constraint(expr= -10 * m.b12 + m.x189 <= 0)
m.e277 = Constraint(expr= -10 * m.b13 + m.x192 <= 0)
m.e278 = Constraint(expr= -10 * m.b14 + m.x195 <= 0)
m.e279 = Constraint(expr= -10 * m.b15 + m.x198 <= 0)
m.e280 = Constraint(expr= -10 * m.b16 + m.x201 <= 0)
m.e281 = Constraint(expr= -10 * m.b17 + m.x204 <= 0)
m.e282 = Constraint(expr= -10 * m.b18 + m.x207 <= 0)
m.e283 = Constraint(expr= -10 * m.b19 + m.x210 <= 0)
m.e284 = Constraint(expr= -10 * m.b20 + m.x213 <= 0)
m.e285 = Constraint(expr= -10 * m.b11 + m.x187 <= 0)
m.e286 = Constraint(expr= -10 * m.b12 + m.x190 <= 0)
m.e287 = Constraint(expr= -10 * m.b13 + m.x193 <= 0)
m.e288 = Constraint(expr= -10 * m.b14 + m.x196 <= 0)
m.e289 = Constraint(expr= -10 * m.b15 + m.x199 <= 0)
m.e290 = Constraint(expr= -10 * m.b16 + m.x202 <= 0)
m.e291 = Constraint(expr= -10 * m.b17 + m.x205 <= 0)
m.e292 = Constraint(expr= -10 * m.b18 + m.x208 <= 0)
m.e293 = Constraint(expr= -10 * m.b19 + m.x211 <= 0)
m.e294 = Constraint(expr= -10 * m.b20 + m.x214 <= 0)
m.e295 = Constraint(expr= -10 * m.b21 + m.x215 <= 0)
m.e296 = Constraint(expr= -10 * m.b22 + m.x218 <= 0)
m.e297 = Constraint(expr= -10 * m.b23 + m.x221 <= 0)
m.e298 = Constraint(expr= -10 * m.b24 + m.x224 <= 0)
m.e299 = Constraint(expr= -10 * m.b25 + m.x227 <= 0)
m.e300 = Constraint(expr= -10 * m.b26 + m.x230 <= 0)
m.e301 = Constraint(expr= -10 * m.b27 + m.x233 <= 0)
m.e302 = Constraint(expr= -10 * m.b28 + m.x236 <= 0)
m.e303 = Constraint(expr= -10 * m.b29 + m.x239 <= 0)
m.e304 = Constraint(expr= -10 * m.b30 + m.x242 <= 0)
m.e305 = Constraint(expr= -10 * m.b21 + m.x216 <= 0)
m.e306 = Constraint(expr= -10 * m.b22 + m.x219 <= 0)
m.e307 = Constraint(expr= -10 * m.b23 + m.x222 <= 0)
m.e308 = Constraint(expr= -10 * m.b24 + m.x225 <= 0)
m.e309 = Constraint(expr= -10 * m.b25 + m.x228 <= 0)
m.e310 = Constraint(expr= -10 * m.b26 + m.x231 <= 0)
m.e311 = Constraint(expr= -10 * m.b27 + m.x234 <= 0)
m.e312 = Constraint(expr= -10 * m.b28 + m.x237 <= 0)
m.e313 = Constraint(expr= -10 * m.b29 + m.x240 <= 0)
m.e314 = Constraint(expr= -10 * m.b30 + m.x243 <= 0)
m.e315 = Constraint(expr= -10 * m.b21 + m.x217 <= 0)
m.e316 = Constraint(expr= -10 * m.b22 + m.x220 <= 0)
m.e317 = Constraint(expr= -10 * m.b23 + m.x223 <= 0)
m.e318 = Constraint(expr= -10 * m.b24 + m.x226 <= 0)
m.e319 = Constraint(expr= -10 * m.b25 + m.x229 <= 0)
m.e320 = Constraint(expr= -10 * m.b26 + m.x232 <= 0)
m.e321 = Constraint(expr= -10 * m.b27 + m.x235 <= 0)
m.e322 = Constraint(expr= -10 * m.b28 + m.x238 <= 0)
m.e323 = Constraint(expr= -10 * m.b29 + m.x241 <= 0)
m.e324 = Constraint(expr= -10 * m.b30 + m.x244 <= 0)
m.e325 = Constraint(expr= -10 * m.b31 + m.x245 <= 0)
m.e326 = Constraint(expr= -10 * m.b32 + m.x248 <= 0)
m.e327 = Constraint(expr= -10 * m.b33 + m.x251 <= 0)
m.e328 = Constraint(expr= -10 * m.b34 + m.x254 <= 0)
m.e329 = Constraint(expr= -10 * m.b35 + m.x257 <= 0)
m.e330 = Constraint(expr= -10 * m.b36 + m.x260 <= 0)
m.e331 = Constraint(expr= -10 * m.b37 + m.x263 <= 0)
m.e332 = Constraint(expr= -10 * m.b38 + m.x266 <= 0)
m.e333 = Constraint(expr= -10 * m.b39 + m.x269 <= 0)
m.e334 = Constraint(expr= -10 * m.b40 + m.x272 <= 0)
m.e335 = Constraint(expr= -10 * m.b31 + m.x246 <= 0)
m.e336 = Constraint(expr= -10 * m.b32 + m.x249 <= 0)
m.e337 = Constraint(expr= -10 * m.b33 + m.x252 <= 0)
m.e338 = Constraint(expr= -10 * m.b34 + m.x255 <= 0)
m.e339 = Constraint(expr= -10 * m.b35 + m.x258 <= 0)
m.e340 = Constraint(expr= -10 * m.b36 + m.x261 <= 0)
m.e341 = Constraint(expr= -10 * m.b37 + m.x264 <= 0)
m.e342 = Constraint(expr= -10 * m.b38 + m.x267 <= 0)
m.e343 = Constraint(expr= -10 * m.b39 + m.x270 <= 0)
m.e344 = Constraint(expr= -10 * m.b40 + m.x273 <= 0)
m.e345 = Constraint(expr= -10 * m.b31 + m.x247 <= 0)
m.e346 = Constraint(expr= -10 * m.b32 + m.x250 <= 0)
m.e347 = Constraint(expr= -10 * m.b33 + m.x253 <= 0)
m.e348 = Constraint(expr= -10 * m.b34 + m.x256 <= 0)
m.e349 = Constraint(expr= -10 * m.b35 + m.x259 <= 0)
m.e350 = Constraint(expr= -10 * m.b36 + m.x262 <= 0)
m.e351 = Constraint(expr= -10 * m.b37 + m.x265 <= 0)
m.e352 = Constraint(expr= -10 * m.b38 + m.x268 <= 0)
m.e353 = Constraint(expr= -10 * m.b39 + m.x271 <= 0)
m.e354 = Constraint(expr= -10 * m.b40 + m.x274 <= 0)
m.e355 = Constraint(expr= -10 * m.b41 + m.x275 <= 0)
m.e356 = Constraint(expr= -10 * m.b42 + m.x278 <= 0)
m.e357 = Constraint(expr= -10 * m.b43 + m.x281 <= 0)
m.e358 = Constraint(expr= -10 * m.b44 + m.x284 <= 0)
m.e359 = Constraint(expr= -10 * m.b45 + m.x287 <= 0)
m.e360 = Constraint(expr= -10 * m.b46 + m.x290 <= 0)
m.e361 = Constraint(expr= -10 * m.b47 + m.x293 <= 0)
m.e362 = Constraint(expr= -10 * m.b48 + m.x296 <= 0)
m.e363 = Constraint(expr= -10 * m.b49 + m.x299 <= 0)
m.e364 = Constraint(expr= -10 * m.b50 + m.x302 <= 0)
m.e365 = Constraint(expr= -10 * m.b41 + m.x276 <= 0)
m.e366 = Constraint(expr= -10 * m.b42 + m.x279 <= 0)
m.e367 = Constraint(expr= -10 * m.b43 + m.x282 <= 0)
m.e368 = Constraint(expr= -10 * m.b44 + m.x285 <= 0)
m.e369 = Constraint(expr= -10 * m.b45 + m.x288 <= 0)
m.e370 = Constraint(expr= -10 * m.b46 + m.x291 <= 0)
m.e371 = Constraint(expr= -10 * m.b47 + m.x294 <= 0)
m.e372 = Constraint(expr= -10 * m.b48 + m.x297 <= 0)
m.e373 = Constraint(expr= -10 * m.b49 + m.x300 <= 0)
m.e374 = Constraint(expr= -10 * m.b50 + m.x303 <= 0)
m.e375 = Constraint(expr= -10 * m.b41 + m.x277 <= 0)
m.e376 = Constraint(expr= -10 * m.b42 + m.x280 <= 0)
m.e377 = Constraint(expr= -10 * m.b43 + m.x283 <= 0)
m.e378 = Constraint(expr= -10 * m.b44 + m.x286 <= 0)
m.e379 = Constraint(expr= -10 * m.b45 + m.x289 <= 0)
m.e380 = Constraint(expr= -10 * m.b46 + m.x292 <= 0)
m.e381 = Constraint(expr= -10 * m.b47 + m.x295 <= 0)
m.e382 = Constraint(expr= -10 * m.b48 + m.x298 <= 0)
m.e383 = Constraint(expr= -10 * m.b49 + m.x301 <= 0)
m.e384 = Constraint(expr= -10 * m.b50 + m.x304 <= 0)
m.e385 = Constraint(expr= -10 * m.b51 + m.x305 <= 0)
m.e386 = Constraint(expr= -10 * m.b52 + m.x308 <= 0)
m.e387 = Constraint(expr= -10 * m.b53 + m.x311 <= 0)
m.e388 = Constraint(expr= -10 * m.b54 + m.x314 <= 0)
m.e389 = Constraint(expr= -10 * m.b55 + m.x317 <= 0)
m.e390 = Constraint(expr= -10 * m.b56 + m.x320 <= 0)
m.e391 = Constraint(expr= -10 * m.b57 + m.x323 <= 0)
m.e392 = Constraint(expr= -10 * m.b58 + m.x326 <= 0)
m.e393 = Constraint(expr= -10 * m.b59 + m.x329 <= 0)
m.e394 = Constraint(expr= -10 * m.b60 + m.x332 <= 0)
m.e395 = Constraint(expr= -10 * m.b51 + m.x306 <= 0)
m.e396 = Constraint(expr= -10 * m.b52 + m.x309 <= 0)
m.e397 = Constraint(expr= -10 * m.b53 + m.x312 <= 0)
m.e398 = Constraint(expr= -10 * m.b54 + m.x315 <= 0)
m.e399 = Constraint(expr= -10 * m.b55 + m.x318 <= 0)
m.e400 = Constraint(expr= -10 * m.b56 + m.x321 <= 0)
m.e401 = Constraint(expr= -10 * m.b57 + m.x324 <= 0)
m.e402 = Constraint(expr= -10 * m.b58 + m.x327 <= 0)
m.e403 = Constraint(expr= -10 * m.b59 + m.x330 <= 0)
m.e404 = Constraint(expr= -10 * m.b60 + m.x333 <= 0)
m.e405 = Constraint(expr= -10 * m.b51 + m.x307 <= 0)
m.e406 = Constraint(expr= -10 * m.b52 + m.x310 <= 0)
m.e407 = Constraint(expr= -10 * m.b53 + m.x313 <= 0)
m.e408 = Constraint(expr= -10 * m.b54 + m.x316 <= 0)
m.e409 = Constraint(expr= -10 * m.b55 + m.x319 <= 0)
m.e410 = Constraint(expr= -10 * m.b56 + m.x322 <= 0)
m.e411 = Constraint(expr= -10 * m.b57 + m.x325 <= 0)
m.e412 = Constraint(expr= -10 * m.b58 + m.x328 <= 0)
m.e413 = Constraint(expr= -10 * m.b59 + m.x331 <= 0)
m.e414 = Constraint(expr= -10 * m.b60 + m.x334 <= 0)
m.e415 = Constraint(expr= -10 * m.b61 + m.x335 <= 0)
m.e416 = Constraint(expr= -10 * m.b62 + m.x338 <= 0)
m.e417 = Constraint(expr= -10 * m.b63 + m.x341 <= 0)
m.e418 = Constraint(expr= -10 * m.b64 + m.x344 <= 0)
m.e419 = Constraint(expr= -10 * m.b65 + m.x347 <= 0)
m.e420 = Constraint(expr= -10 * m.b66 + m.x350 <= 0)
m.e421 = Constraint(expr= -10 * m.b67 + m.x353 <= 0)
m.e422 = Constraint(expr= -10 * m.b68 + m.x356 <= 0)
m.e423 = Constraint(expr= -10 * m.b69 + m.x359 <= 0)
m.e424 = Constraint(expr= -10 * m.b70 + m.x362 <= 0)
m.e425 = Constraint(expr= -10 * m.b61 + m.x336 <= 0)
m.e426 = Constraint(expr= -10 * m.b62 + m.x339 <= 0)
m.e427 = Constraint(expr= -10 * m.b63 + m.x342 <= 0)
m.e428 = Constraint(expr= -10 * m.b64 + m.x345 <= 0)
m.e429 = Constraint(expr= -10 * m.b65 + m.x348 <= 0)
m.e430 = Constraint(expr= -10 * m.b66 + m.x351 <= 0)
m.e431 = Constraint(expr= -10 * m.b67 + m.x354 <= 0)
m.e432 = Constraint(expr= -10 * m.b68 + m.x357 <= 0)
m.e433 = Constraint(expr= -10 * m.b69 + m.x360 <= 0)
m.e434 = Constraint(expr= -10 * m.b70 + m.x363 <= 0)
m.e435 = Constraint(expr= -10 * m.b61 + m.x337 <= 0)
m.e436 = Constraint(expr= -10 * m.b62 + m.x340 <= 0)
m.e437 = Constraint(expr= -10 * m.b63 + m.x343 <= 0)
m.e438 = Constraint(expr= -10 * m.b64 + m.x346 <= 0)
m.e439 = Constraint(expr= -10 * m.b65 + m.x349 <= 0)
m.e440 = Constraint(expr= -10 * m.b66 + m.x352 <= 0)
m.e441 = Constraint(expr= -10 * m.b67 + m.x355 <= 0)
m.e442 = Constraint(expr= -10 * m.b68 + m.x358 <= 0)
m.e443 = Constraint(expr= -10 * m.b69 + m.x361 <= 0)
m.e444 = Constraint(expr= -10 * m.b70 + m.x364 <= 0)
m.e445 = Constraint(expr= m.x71 - m.x72 <= 0)
m.e446 = Constraint(expr= m.x72 - m.x80 <= 0)
m.e447 = Constraint(expr= m.x80 - m.x86 <= 0)
m.e448 = Constraint(expr= m.x86 - m.x92 <= 0)
m.e449 = Constraint(expr= m.x92 - m.x98 <= 0)
m.e450 = Constraint(expr= m.x98 - m.x104 <= 0)
