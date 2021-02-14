#  MINLP written by GAMS Convert at 01/15/21 11:37:19
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       2449      931       99     1419        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#       1468     1156      312        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       5833     5707      126        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x141 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x142 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x143 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x144 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x145 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x146 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x147 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x148 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x149 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x150 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x151 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x152 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x153 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x154 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x155 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x156 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x157 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x158 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x159 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x201 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x202 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x203 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x204 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x205 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x206 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x207 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x217 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x218 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x219 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x220 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x221 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x222 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x223 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x231 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x232 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x233 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x234 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x235 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x267 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x268 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x269 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x270 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x271 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x272 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x273 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x274 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x275 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x276 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x277 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x278 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x279 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x280 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x281 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x282 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x283 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x284 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x285 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x286 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x287 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x288 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x289 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x290 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x291 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x295 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x298 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x301 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x302 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x303 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x304 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x305 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x315 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x316 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x317 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x318 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x319 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x320 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x321 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x322 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x323 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x324 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x325 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x326 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x327 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x328 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x329 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x330 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x331 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x332 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x333 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x334 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x335 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x336 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x337 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x338 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x339 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x340 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x341 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x342 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x343 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x345 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x346 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x347 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x349 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x350 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x351 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x352 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x353 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x354 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x355 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x356 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x357 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x358 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x359 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x360 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x361 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x362 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x363 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x364 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x365 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x366 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x367 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x368 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x369 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x370 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x371 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x372 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x373 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x374 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x375 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x376 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x377 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x378 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x379 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x380 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x381 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x382 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x383 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x384 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x385 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x386 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x387 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x388 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x389 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x390 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x391 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x392 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x393 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x394 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x395 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x396 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x397 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x398 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x399 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x400 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x401 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x402 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x403 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x404 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x405 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x406 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x407 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x408 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x409 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x410 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x411 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x412 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x413 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x414 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x415 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x416 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x417 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x418 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x419 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x420 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x421 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x422 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x423 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x424 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x425 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x426 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x427 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x428 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x429 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x430 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x431 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x432 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x433 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x434 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x435 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x436 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x437 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x438 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x439 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x440 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x441 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x442 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x443 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x444 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x445 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x446 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x447 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x448 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x449 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x450 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x451 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x452 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x453 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x454 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x455 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x456 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x457 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x458 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x459 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x460 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x461 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x462 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x463 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x464 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x465 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x466 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x467 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x468 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x469 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x470 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x471 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x472 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x473 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x474 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x475 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x476 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x477 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x478 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x479 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x480 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x481 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x482 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x483 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x484 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x485 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x486 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x487 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x488 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x489 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x490 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x491 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x492 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x493 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x494 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x495 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x496 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x497 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x498 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x499 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x500 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x501 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x502 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x503 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x504 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x505 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x506 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x507 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x508 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x509 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x510 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x511 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x512 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x513 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x514 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x515 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x516 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x517 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x518 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x519 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x520 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x521 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x522 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x523 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x524 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x525 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x526 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x527 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x528 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x529 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x530 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x531 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x532 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x533 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x534 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x535 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x536 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x537 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x538 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x539 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x540 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x541 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x542 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x543 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x544 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x545 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x546 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x547 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x548 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x549 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x550 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x551 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x552 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x553 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x554 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x555 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x556 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x557 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x558 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x559 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x560 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x561 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x562 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x563 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x564 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x565 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x566 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x567 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x568 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x569 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x570 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x571 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x572 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x573 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x574 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x575 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x576 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x577 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x578 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x579 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x580 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x581 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x582 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x583 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x584 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x585 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x586 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x587 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x588 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x589 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x590 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x591 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x592 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x593 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x594 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x595 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x596 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x597 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x598 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x599 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x600 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x601 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x602 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x603 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x604 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x605 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x606 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x607 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x608 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x609 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x610 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x611 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x612 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x613 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x614 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x615 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x616 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x617 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x618 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x619 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x620 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x621 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x622 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x623 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x624 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x625 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x626 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x627 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x628 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x629 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x630 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x631 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x632 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x633 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x634 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x635 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x636 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x637 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x638 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x639 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x640 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x641 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x642 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x643 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x644 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x645 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x646 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x647 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x648 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x649 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x650 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x651 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x652 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x653 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x654 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x655 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x656 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x657 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x658 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x659 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x660 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x661 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x662 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x663 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x664 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x665 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x666 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x667 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x668 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x669 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x670 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x671 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x672 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x673 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x674 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x675 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x676 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x677 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x678 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x679 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x680 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x681 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x682 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x683 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x684 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x685 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x686 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x687 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x688 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x689 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x690 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x691 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x692 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x693 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x694 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x695 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x696 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x697 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x698 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x699 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x700 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x701 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x702 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x703 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x704 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x705 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x706 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x707 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x708 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x709 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x710 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x711 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x712 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x713 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x714 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x715 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x716 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x717 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x718 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x719 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x720 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x721 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x722 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x723 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x724 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x725 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x726 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x727 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x728 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x729 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x730 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x731 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x732 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x733 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x734 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x735 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x736 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x737 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x738 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x739 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x740 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x741 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x742 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x743 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x744 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x745 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x746 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x747 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x748 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x749 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x750 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x751 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x752 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x753 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x754 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x755 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x756 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x757 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x758 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x759 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x760 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x761 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x762 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x763 = Var(within=Reals,bounds=(None,None),initialize=0)
m.b764 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b765 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b766 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b767 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b768 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b769 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b770 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b771 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b772 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b773 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b774 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b775 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b776 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b777 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b778 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b779 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b780 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b781 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b782 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b783 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b784 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b785 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b786 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b787 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b788 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b789 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b790 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b791 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b792 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b793 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b794 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b795 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b796 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b797 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b798 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b799 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b800 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b801 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b802 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b803 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b804 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b805 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b806 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b807 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b808 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b809 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b810 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b811 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b812 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b813 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b814 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b815 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b816 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b817 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b818 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b819 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b820 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b821 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b822 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b823 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b824 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b825 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b826 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b827 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b828 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b829 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b830 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b831 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b832 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b833 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b834 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b835 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b836 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b837 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b838 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b839 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b840 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b841 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b842 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b843 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b844 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b845 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b846 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b847 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b848 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b849 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b850 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b851 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b852 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b853 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b854 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b855 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b856 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b857 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b858 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b859 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b860 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b861 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b862 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b863 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b864 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b865 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b866 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b867 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b868 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b869 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b870 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b871 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b872 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b873 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b874 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b875 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b876 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b877 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b878 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b879 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b880 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b881 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b882 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b883 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b884 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b885 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b886 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b887 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b888 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b889 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b890 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b891 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b892 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b893 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b894 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b895 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b896 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b897 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b898 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b899 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b900 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b901 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b902 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b903 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b904 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b905 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b906 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b907 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b908 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b909 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b910 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b911 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b912 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b913 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b914 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b915 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b916 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b917 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b918 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b919 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b920 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b921 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b922 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b923 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b924 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b925 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b926 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b927 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b928 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b929 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b930 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b931 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b932 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b933 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b934 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b935 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b936 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b937 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b938 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b939 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b940 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b941 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b942 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b943 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b944 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b945 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b946 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b947 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b948 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b949 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b950 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b951 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b952 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b953 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b954 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b955 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x956 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x957 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x958 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x959 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x960 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x961 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x962 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x963 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x964 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x965 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x966 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x967 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x968 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x969 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x970 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x971 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x972 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x973 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x974 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x975 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x976 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x977 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x978 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x979 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x980 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x981 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x982 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x983 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x984 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x985 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x986 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x987 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x988 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x989 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x990 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x991 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x992 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x993 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x994 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x995 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x996 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x997 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x998 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x999 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1000 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1001 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1002 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1003 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1004 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1005 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1006 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1007 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1008 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1009 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1010 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1011 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1012 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1013 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1014 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1015 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1016 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1017 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1018 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1019 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1020 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1021 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1022 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1023 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1024 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1025 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1026 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1027 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1028 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1029 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1030 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1031 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1032 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1033 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1034 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1035 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1036 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1037 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1038 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1039 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1040 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x1041 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x1042 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x1043 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x1044 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x1045 = Var(within=Reals,bounds=(0,20),initialize=0)
m.x1046 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1047 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1048 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1049 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1050 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1051 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1052 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1053 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1054 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1055 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1056 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1057 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1058 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1059 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1060 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1061 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1062 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1063 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1064 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1065 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1066 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1067 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1068 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1069 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1070 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1071 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1072 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1073 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1074 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1075 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1076 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1077 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1078 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1079 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1080 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1081 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1082 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1083 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1084 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1085 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1086 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1087 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1088 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1089 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1090 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1091 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1092 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1093 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1094 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1095 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1096 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1097 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1098 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1099 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1100 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1101 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1102 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1103 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1104 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1105 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1106 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1107 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1108 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1109 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1110 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1111 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1112 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1113 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1114 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1115 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1116 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1117 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1118 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1119 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1120 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1121 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1122 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1123 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1124 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1125 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1126 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1127 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1128 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1129 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1130 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1131 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1132 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1133 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1134 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1135 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1136 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1137 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1138 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1139 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1140 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1141 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1142 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1143 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1144 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1145 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1146 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1147 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1148 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1149 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1150 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1151 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1152 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1153 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1154 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1155 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1156 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1157 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1158 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1159 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1160 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1161 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1162 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1163 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1164 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1165 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1166 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1167 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1168 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1169 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1170 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1171 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1172 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1173 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1174 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1175 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1176 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1177 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1178 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1179 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1180 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1181 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1182 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1183 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1184 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1185 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1186 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1187 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1188 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1189 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1190 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1191 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1192 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1193 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1194 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1195 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1196 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1197 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1198 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1199 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1200 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1201 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1202 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1203 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1204 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1205 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1206 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1207 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1208 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1209 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1210 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1211 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1212 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1213 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1214 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1215 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1216 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1217 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1218 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1219 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1220 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1221 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1222 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1223 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1224 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1225 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1226 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1227 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1228 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1229 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1230 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1231 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1232 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1233 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1234 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1235 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1236 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1237 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1238 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1239 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1240 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1241 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1242 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1243 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1244 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1245 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1246 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1247 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1248 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1249 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1250 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1251 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1252 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1253 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1254 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1255 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1256 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1257 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1258 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1259 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1260 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1261 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1262 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1263 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1264 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1265 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1266 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1267 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1268 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1269 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1270 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1271 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1272 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1273 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1274 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1275 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1276 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1277 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1278 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1279 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1280 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1281 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1282 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1283 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1284 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1285 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1286 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1287 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1288 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1289 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1290 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1291 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1292 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1293 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1294 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1295 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1296 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1297 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1298 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1299 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1300 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1301 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1302 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1303 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1304 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1305 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1306 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1307 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1308 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1309 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1310 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1311 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1312 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1313 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1314 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1315 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1316 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1317 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1318 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1319 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1320 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1321 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1322 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1323 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1324 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1325 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1326 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1327 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1328 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1329 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1330 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1331 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1332 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1333 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1334 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1335 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1336 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1337 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1338 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1339 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1340 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1341 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1342 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1343 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1344 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1345 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1346 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1347 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x1348 = Var(within=Reals,bounds=(0,None),initialize=0)
m.b1349 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1350 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1351 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1352 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1353 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1354 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1355 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1356 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1357 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1358 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1359 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1360 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1361 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1362 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1363 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1364 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1365 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1366 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1367 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1368 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1369 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1370 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1371 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1372 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1373 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1374 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1375 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1376 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1377 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1378 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1379 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1380 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1381 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1382 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1383 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1384 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1385 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1386 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1387 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1388 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1389 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1390 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1391 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1392 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1393 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1394 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1395 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1396 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1397 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1398 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1399 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1400 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1401 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1402 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1403 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1404 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1405 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1406 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1407 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1408 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1409 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1410 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1411 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1412 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1413 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1414 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1415 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1416 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1417 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1418 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1419 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1420 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1421 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1422 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1423 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1424 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1425 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1426 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1427 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1428 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1429 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1430 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1431 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1432 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1433 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1434 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1435 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1436 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1437 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1438 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1439 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1440 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1441 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1442 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1443 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1444 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1445 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1446 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1447 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1448 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1449 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1450 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1451 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1452 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1453 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1454 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1455 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1456 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1457 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1458 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1459 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1460 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1461 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1462 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1463 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1464 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1465 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1466 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1467 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1468 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr= - 20*m.x2 - 17*m.x3 - 15*m.x4 - 20*m.x17 - 21*m.x18 - 19*m.x19 - 18*m.x29 - 20*m.x30 - 20*m.x31
                        - 16*m.x65 - 19*m.x66 - 17*m.x67 + 26*m.x77 + 31*m.x78 + 31*m.x79 + 30*m.x83 + 29*m.x84
                        + 37*m.x85 - 20*m.x86 - 18*m.x87 - 21*m.x88 + 2*m.x95 + 2*m.x96 + 2*m.x97 + 3*m.x98 + 2*m.x99
                        + 2*m.x100 + 3*m.x101 + 3*m.x102 + 3*m.x103 + 2*m.x104 + 2*m.x105 + 2*m.x106 - 6*m.b863
                        - 4*m.b864 - 3*m.b865 - 40*m.b866 - 35*m.b867 - 20*m.b868 - 46*m.b869 - 39*m.b870 - 23*m.b871
                        - 7*m.b875 - 4*m.b876 - 4*m.b877 - 30*m.b878 - 25*m.b879 - 20*m.b880 - 37*m.b881 - 29*m.b882
                        - 22*m.b883 - 7*m.b887 - 5*m.b888 - 3*m.b889 - 15*m.b890 - 5*m.b891 - 2*m.b892 - 22*m.b893
                        - 10*m.b894 - 5*m.b895 - 11*m.b899 - 8*m.b900 - 6*m.b901 - 13*m.b902 - 8*m.b903 - 3*m.b904
                        - 24*m.b905 - 16*m.b906 - 9*m.b907 - 10*m.b911 - 7*m.b912 - 6*m.b913 - 13*m.b914 - 8*m.b915
                        - 3*m.b916 - 23*m.b917 - 15*m.b918 - 9*m.b919 - 9*m.b923 - 9*m.b924 - 7*m.b925 - 30*m.b926
                        - 30*m.b927 - 25*m.b928 - 39*m.b929 - 39*m.b930 - 32*m.b931 - 8*m.b935 - 7*m.b936 - 7*m.b937
                        - 20*m.b938 - 15*m.b939 - 10*m.b940 - 28*m.b941 - 22*m.b942 - 17*m.b943 - 8*m.b947 - 6*m.b948
                        - 5*m.b949 - 15*m.b950 - 10*m.b951 - 6*m.b952 - 23*m.b953 - 16*m.b954 - 11*m.b955 - m.x956
                        - m.x957 - m.x958 + 5*m.x974 + 10*m.x975 + 5*m.x976 - 2*m.x989 - m.x990 - 2*m.x991 - 10*m.x1040
                        - 5*m.x1041 - 5*m.x1042 - 5*m.x1043 - 5*m.x1044 - 5*m.x1045 + 80*m.x1064 + 130*m.x1065
                        + 215*m.x1066 + 110*m.x1067 + 120*m.x1068 + 125*m.x1069 + 110*m.x1070 + 130*m.x1071
                        + 140*m.x1072 + 80*m.x1073 + 90*m.x1074 + 120*m.x1075 + 285*m.x1076 + 390*m.x1077 + 350*m.x1078
                        + 290*m.x1079 + 405*m.x1080 + 190*m.x1081 + 280*m.x1082 + 400*m.x1083 + 430*m.x1084
                        + 290*m.x1085 + 300*m.x1086 + 240*m.x1087 + 350*m.x1088 + 250*m.x1089 + 300*m.x1090 - 5*m.b1409
                        - 4*m.b1410 - 6*m.b1411 - 8*m.b1412 - 7*m.b1413 - 6*m.b1414 - 6*m.b1415 - 9*m.b1416 - 4*m.b1417
                        - 10*m.b1418 - 9*m.b1419 - 5*m.b1420 - 6*m.b1421 - 10*m.b1422 - 6*m.b1423 - 7*m.b1424
                        - 7*m.b1425 - 4*m.b1426 - 4*m.b1427 - 3*m.b1428 - 2*m.b1429 - 5*m.b1430 - 6*m.b1431 - 7*m.b1432
                        - 2*m.b1433 - 5*m.b1434 - 2*m.b1435 - 4*m.b1436 - 7*m.b1437 - 4*m.b1438 - 3*m.b1439 - 9*m.b1440
                        - 3*m.b1441 - 7*m.b1442 - 2*m.b1443 - 9*m.b1444 - 3*m.b1445 - m.b1446 - 9*m.b1447 - 2*m.b1448
                        - 6*m.b1449 - 3*m.b1450 - 4*m.b1451 - 8*m.b1452 - m.b1453 - 2*m.b1454 - 5*m.b1455 - 2*m.b1456
                        - 3*m.b1457 - 4*m.b1458 - 3*m.b1459 - 5*m.b1460 - 7*m.b1461 - 6*m.b1462 - 2*m.b1463 - 8*m.b1464
                        - 4*m.b1465 - m.b1466 - 4*m.b1467 - m.b1468, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - 0.2*m.x107 == 0)

m.c3 = Constraint(expr=   m.x3 - 0.2*m.x108 == 0)

m.c4 = Constraint(expr=   m.x4 - 0.2*m.x109 == 0)

m.c5 = Constraint(expr=   m.x5 - 0.2*m.x110 == 0)

m.c6 = Constraint(expr=   m.x6 - 0.2*m.x111 == 0)

m.c7 = Constraint(expr=   m.x7 - 0.2*m.x112 == 0)

m.c8 = Constraint(expr=   m.x8 - 0.2*m.x113 == 0)

m.c9 = Constraint(expr=   m.x9 - 0.2*m.x114 == 0)

m.c10 = Constraint(expr=   m.x10 - 0.2*m.x115 == 0)

m.c11 = Constraint(expr=   m.x11 - 0.2*m.x116 == 0)

m.c12 = Constraint(expr=   m.x12 - 0.2*m.x117 == 0)

m.c13 = Constraint(expr=   m.x13 - 0.2*m.x118 == 0)

m.c14 = Constraint(expr=   m.x14 - 0.2*m.x119 == 0)

m.c15 = Constraint(expr=   m.x15 - 0.2*m.x120 == 0)

m.c16 = Constraint(expr=   m.x16 - 0.2*m.x121 == 0)

m.c17 = Constraint(expr=   m.x17 - 0.5*m.x122 == 0)

m.c18 = Constraint(expr=   m.x18 - 0.5*m.x123 == 0)

m.c19 = Constraint(expr=   m.x19 - 0.5*m.x124 == 0)

m.c20 = Constraint(expr=   m.x20 - 0.5*m.x125 == 0)

m.c21 = Constraint(expr=   m.x21 - 0.5*m.x126 == 0)

m.c22 = Constraint(expr=   m.x22 - 0.5*m.x127 == 0)

m.c23 = Constraint(expr=   m.x23 - 0.7*m.x128 == 0)

m.c24 = Constraint(expr=   m.x24 - 0.7*m.x129 == 0)

m.c25 = Constraint(expr=   m.x25 - 0.7*m.x130 == 0)

m.c26 = Constraint(expr=   m.x26 - 0.7*m.x131 == 0)

m.c27 = Constraint(expr=   m.x27 - 0.7*m.x132 == 0)

m.c28 = Constraint(expr=   m.x28 - 0.7*m.x133 == 0)

m.c29 = Constraint(expr=   m.x29 - 1.2*m.x134 == 0)

m.c30 = Constraint(expr=   m.x30 - 1.2*m.x135 == 0)

m.c31 = Constraint(expr=   m.x31 - 1.2*m.x136 == 0)

m.c32 = Constraint(expr=   m.x32 - 1.2*m.x137 == 0)

m.c33 = Constraint(expr=   m.x33 - 1.2*m.x138 == 0)

m.c34 = Constraint(expr=   m.x34 - 1.2*m.x139 == 0)

m.c35 = Constraint(expr=   m.x35 - 0.5*m.x140 == 0)

m.c36 = Constraint(expr=   m.x36 - 0.5*m.x141 == 0)

m.c37 = Constraint(expr=   m.x37 - 0.5*m.x142 == 0)

m.c38 = Constraint(expr=   m.x38 - 0.7*m.x143 == 0)

m.c39 = Constraint(expr=   m.x39 - 0.7*m.x144 == 0)

m.c40 = Constraint(expr=   m.x40 - 0.7*m.x145 == 0)

m.c41 = Constraint(expr=   m.x41 - 1.2*m.x146 == 0)

m.c42 = Constraint(expr=   m.x42 - 1.2*m.x147 == 0)

m.c43 = Constraint(expr=   m.x43 - 1.2*m.x148 == 0)

m.c44 = Constraint(expr=   m.x44 - 1.2*m.x149 == 0)

m.c45 = Constraint(expr=   m.x45 - 1.2*m.x150 == 0)

m.c46 = Constraint(expr=   m.x46 - 1.2*m.x151 == 0)

m.c47 = Constraint(expr=   m.x47 - 1.2*m.x152 == 0)

m.c48 = Constraint(expr=   m.x48 - 1.2*m.x153 == 0)

m.c49 = Constraint(expr=   m.x49 - 1.2*m.x154 == 0)

m.c50 = Constraint(expr=   m.x50 - 1.2*m.x155 == 0)

m.c51 = Constraint(expr=   m.x51 - 1.2*m.x156 == 0)

m.c52 = Constraint(expr=   m.x52 - 1.2*m.x157 == 0)

m.c53 = Constraint(expr=   m.x53 - 0.3*m.x158 == 0)

m.c54 = Constraint(expr=   m.x54 - 0.3*m.x159 == 0)

m.c55 = Constraint(expr=   m.x55 - 0.3*m.x160 == 0)

m.c56 = Constraint(expr=   m.x56 - 0.9*m.x161 == 0)

m.c57 = Constraint(expr=   m.x57 - 0.9*m.x162 == 0)

m.c58 = Constraint(expr=   m.x58 - 0.9*m.x163 == 0)

m.c59 = Constraint(expr=   m.x59 - 0.3*m.x164 == 0)

m.c60 = Constraint(expr=   m.x60 - 0.3*m.x165 == 0)

m.c61 = Constraint(expr=   m.x61 - 0.3*m.x166 == 0)

m.c62 = Constraint(expr=   m.x62 - 0.9*m.x167 == 0)

m.c63 = Constraint(expr=   m.x63 - 0.9*m.x168 == 0)

m.c64 = Constraint(expr=   m.x64 - 0.9*m.x169 == 0)

m.c65 = Constraint(expr=   m.x65 - 0.4*m.x170 == 0)

m.c66 = Constraint(expr=   m.x66 - 0.4*m.x171 == 0)

m.c67 = Constraint(expr=   m.x67 - 0.4*m.x172 == 0)

m.c68 = Constraint(expr=   m.x68 - 0.4*m.x173 == 0)

m.c69 = Constraint(expr=   m.x69 - 0.4*m.x174 == 0)

m.c70 = Constraint(expr=   m.x70 - 0.4*m.x175 == 0)

m.c71 = Constraint(expr=   m.x71 - 0.4*m.x176 == 0)

m.c72 = Constraint(expr=   m.x72 - 0.4*m.x177 == 0)

m.c73 = Constraint(expr=   m.x73 - 0.4*m.x178 == 0)

m.c74 = Constraint(expr=   m.x74 - 1.6*m.x179 == 0)

m.c75 = Constraint(expr=   m.x75 - 1.6*m.x180 == 0)

m.c76 = Constraint(expr=   m.x76 - 1.6*m.x181 == 0)

m.c77 = Constraint(expr=   m.x77 - 1.6*m.x182 == 0)

m.c78 = Constraint(expr=   m.x78 - 1.6*m.x183 == 0)

m.c79 = Constraint(expr=   m.x79 - 1.6*m.x184 == 0)

m.c80 = Constraint(expr=   m.x80 - 1.1*m.x185 == 0)

m.c81 = Constraint(expr=   m.x81 - 1.1*m.x186 == 0)

m.c82 = Constraint(expr=   m.x82 - 1.1*m.x187 == 0)

m.c83 = Constraint(expr=   m.x83 - 1.1*m.x188 == 0)

m.c84 = Constraint(expr=   m.x84 - 1.1*m.x189 == 0)

m.c85 = Constraint(expr=   m.x85 - 1.1*m.x190 == 0)

m.c86 = Constraint(expr=   m.x86 - 0.7*m.x191 == 0)

m.c87 = Constraint(expr=   m.x87 - 0.7*m.x192 == 0)

m.c88 = Constraint(expr=   m.x88 - 0.7*m.x193 == 0)

m.c89 = Constraint(expr=   m.x89 - 0.7*m.x194 == 0)

m.c90 = Constraint(expr=   m.x90 - 0.7*m.x195 == 0)

m.c91 = Constraint(expr=   m.x91 - 0.7*m.x196 == 0)

m.c92 = Constraint(expr=   m.x92 - 0.7*m.x197 == 0)

m.c93 = Constraint(expr=   m.x93 - 0.7*m.x198 == 0)

m.c94 = Constraint(expr=   m.x94 - 0.7*m.x199 == 0)

m.c95 = Constraint(expr=   m.x95 - 0.2*m.x200 == 0)

m.c96 = Constraint(expr=   m.x96 - 0.2*m.x201 == 0)

m.c97 = Constraint(expr=   m.x97 - 0.2*m.x202 == 0)

m.c98 = Constraint(expr=   m.x98 - 0.7*m.x203 == 0)

m.c99 = Constraint(expr=   m.x99 - 0.7*m.x204 == 0)

m.c100 = Constraint(expr=   m.x100 - 0.7*m.x205 == 0)

m.c101 = Constraint(expr=   m.x101 - 0.3*m.x206 == 0)

m.c102 = Constraint(expr=   m.x102 - 0.3*m.x207 == 0)

m.c103 = Constraint(expr=   m.x103 - 0.3*m.x208 == 0)

m.c104 = Constraint(expr=   m.x104 - 0.9*m.x209 == 0)

m.c105 = Constraint(expr=   m.x105 - 0.9*m.x210 == 0)

m.c106 = Constraint(expr=   m.x106 - 0.9*m.x211 == 0)

m.c107 = Constraint(expr=   m.x77 >= 0.2)

m.c108 = Constraint(expr=   m.x78 >= 0.1)

m.c109 = Constraint(expr=   m.x79 >= 0.1)

m.c110 = Constraint(expr=   m.x83 >= 0.2)

m.c111 = Constraint(expr=   m.x84 >= 0.1)

m.c112 = Constraint(expr=   m.x85 >= 0.1)

m.c113 = Constraint(expr=   m.x95 >= 0.1)

m.c114 = Constraint(expr=   m.x96 >= 0.1)

m.c115 = Constraint(expr=   m.x97 >= 0.1)

m.c116 = Constraint(expr=   m.x98 >= 0.1)

m.c117 = Constraint(expr=   m.x99 >= 0.1)

m.c118 = Constraint(expr=   m.x100 >= 0.1)

m.c119 = Constraint(expr=   m.x101 >= 0.4)

m.c120 = Constraint(expr=   m.x102 >= 0.3)

m.c121 = Constraint(expr=   m.x103 >= 0.2)

m.c122 = Constraint(expr=   m.x104 >= 0.3)

m.c123 = Constraint(expr=   m.x105 >= 0.2)

m.c124 = Constraint(expr=   m.x106 >= 0.1)

m.c125 = Constraint(expr=   m.x2 <= 35)

m.c126 = Constraint(expr=   m.x3 <= 30)

m.c127 = Constraint(expr=   m.x4 <= 30)

m.c128 = Constraint(expr=   m.x17 <= 36)

m.c129 = Constraint(expr=   m.x18 <= 31)

m.c130 = Constraint(expr=   m.x19 <= 30)

m.c131 = Constraint(expr=   m.x29 <= 25)

m.c132 = Constraint(expr=   m.x30 <= 22)

m.c133 = Constraint(expr=   m.x31 <= 22)

m.c134 = Constraint(expr=   m.x65 <= 24)

m.c135 = Constraint(expr=   m.x66 <= 21)

m.c136 = Constraint(expr=   m.x67 <= 20)

m.c137 = Constraint(expr=   m.x86 <= 30)

m.c138 = Constraint(expr=   m.x87 <= 25)

m.c139 = Constraint(expr=   m.x88 <= 21)

m.c140 = Constraint(expr=   m.x2 - m.x5 - m.x8 == 0)

m.c141 = Constraint(expr=   m.x3 - m.x6 - m.x9 == 0)

m.c142 = Constraint(expr=   m.x4 - m.x7 - m.x10 == 0)

m.c143 = Constraint(expr=   m.x11 - m.x14 == 0)

m.c144 = Constraint(expr=   m.x12 - m.x15 == 0)

m.c145 = Constraint(expr=   m.x13 - m.x16 == 0)

m.c146 = Constraint(expr=   m.x17 - m.x20 + m.x35 == 0)

m.c147 = Constraint(expr=   m.x18 - m.x21 + m.x36 == 0)

m.c148 = Constraint(expr=   m.x19 - m.x22 + m.x37 == 0)

m.c149 = Constraint(expr=   m.x23 - m.x26 + m.x38 == 0)

m.c150 = Constraint(expr=   m.x24 - m.x27 + m.x39 == 0)

m.c151 = Constraint(expr=   m.x25 - m.x28 + m.x40 == 0)

m.c152 = Constraint(expr=   m.x29 - m.x32 - m.x41 == 0)

m.c153 = Constraint(expr=   m.x30 - m.x33 - m.x42 == 0)

m.c154 = Constraint(expr=   m.x31 - m.x34 - m.x43 == 0)

m.c155 = Constraint(expr=   m.x44 - m.x47 - m.x50 == 0)

m.c156 = Constraint(expr=   m.x45 - m.x48 - m.x51 == 0)

m.c157 = Constraint(expr=   m.x46 - m.x49 - m.x52 == 0)

m.c158 = Constraint(expr=   m.x53 - m.x59 == 0)

m.c159 = Constraint(expr=   m.x54 - m.x60 == 0)

m.c160 = Constraint(expr=   m.x55 - m.x61 == 0)

m.c161 = Constraint(expr=   m.x56 - m.x62 == 0)

m.c162 = Constraint(expr=   m.x57 - m.x63 == 0)

m.c163 = Constraint(expr=   m.x58 - m.x64 == 0)

m.c164 = Constraint(expr=   m.x65 - m.x68 - m.x71 == 0)

m.c165 = Constraint(expr=   m.x66 - m.x69 - m.x72 == 0)

m.c166 = Constraint(expr=   m.x67 - m.x70 - m.x73 == 0)

m.c167 = Constraint(expr=   m.x74 - m.x77 == 0)

m.c168 = Constraint(expr=   m.x75 - m.x78 == 0)

m.c169 = Constraint(expr=   m.x76 - m.x79 == 0)

m.c170 = Constraint(expr=   m.x80 - m.x83 == 0)

m.c171 = Constraint(expr=   m.x81 - m.x84 == 0)

m.c172 = Constraint(expr=   m.x82 - m.x85 == 0)

m.c173 = Constraint(expr=   m.x86 - m.x89 == 0)

m.c174 = Constraint(expr=   m.x87 - m.x90 == 0)

m.c175 = Constraint(expr=   m.x88 - m.x91 == 0)

m.c176 = Constraint(expr=   m.x5 - m.x11 - m.x212 == 0)

m.c177 = Constraint(expr=   m.x6 - m.x12 - m.x213 == 0)

m.c178 = Constraint(expr=   m.x7 - m.x13 - m.x214 == 0)

m.c179 = Constraint(expr=   m.x8 + m.x20 - m.x23 - m.x215 == 0)

m.c180 = Constraint(expr=   m.x9 + m.x21 - m.x24 - m.x216 == 0)

m.c181 = Constraint(expr=   m.x10 + m.x22 - m.x25 - m.x217 == 0)

m.c182 = Constraint(expr=   m.x32 - m.x35 - m.x38 - m.x218 == 0)

m.c183 = Constraint(expr=   m.x33 - m.x36 - m.x39 - m.x219 == 0)

m.c184 = Constraint(expr=   m.x34 - m.x37 - m.x40 - m.x220 == 0)

m.c185 = Constraint(expr=   m.x41 - m.x44 - m.x221 == 0)

m.c186 = Constraint(expr=   m.x42 - m.x45 - m.x222 == 0)

m.c187 = Constraint(expr=   m.x43 - m.x46 - m.x223 == 0)

m.c188 = Constraint(expr=   m.x50 - m.x53 - m.x56 - m.x224 == 0)

m.c189 = Constraint(expr=   m.x51 - m.x54 - m.x57 - m.x225 == 0)

m.c190 = Constraint(expr=   m.x52 - m.x55 - m.x58 - m.x226 == 0)

m.c191 = Constraint(expr=   m.x47 + m.x68 - m.x74 - m.x227 == 0)

m.c192 = Constraint(expr=   m.x48 + m.x69 - m.x75 - m.x228 == 0)

m.c193 = Constraint(expr=   m.x49 + m.x70 - m.x76 - m.x229 == 0)

m.c194 = Constraint(expr=   m.x71 - m.x80 + m.x92 - m.x230 == 0)

m.c195 = Constraint(expr=   m.x72 - m.x81 + m.x93 - m.x231 == 0)

m.c196 = Constraint(expr=   m.x73 - m.x82 + m.x94 - m.x232 == 0)

m.c197 = Constraint(expr=   m.x89 - m.x92 - m.x233 == 0)

m.c198 = Constraint(expr=   m.x90 - m.x93 - m.x234 == 0)

m.c199 = Constraint(expr=   m.x91 - m.x94 - m.x235 == 0)

m.c200 = Constraint(expr=   m.x113 - m.x125 <= 0)

m.c201 = Constraint(expr=   m.x114 - m.x126 <= 0)

m.c202 = Constraint(expr=   m.x115 - m.x127 <= 0)

m.c203 = Constraint(expr=   m.x152 - m.x173 <= 0)

m.c204 = Constraint(expr=   m.x153 - m.x174 <= 0)

m.c205 = Constraint(expr=   m.x154 - m.x175 <= 0)

m.c206 = Constraint(expr=   m.x176 - m.x197 <= 0)

m.c207 = Constraint(expr=   m.x177 - m.x198 <= 0)

m.c208 = Constraint(expr=   m.x178 - m.x199 <= 0)

m.c209 = Constraint(expr=   m.x116 - m.x416 - m.x419 - m.x422 - m.x425 == 0)

m.c210 = Constraint(expr=   m.x117 - m.x417 - m.x420 - m.x423 - m.x426 == 0)

m.c211 = Constraint(expr=   m.x118 - m.x418 - m.x421 - m.x424 - m.x427 == 0)

m.c212 = Constraint(expr=   m.x110 - m.x392 - m.x395 - m.x398 - m.x401 == 0)

m.c213 = Constraint(expr=   m.x111 - m.x393 - m.x396 - m.x399 - m.x402 == 0)

m.c214 = Constraint(expr=   m.x112 - m.x394 - m.x397 - m.x400 - m.x403 == 0)

m.c215 = Constraint(expr=   m.x128 - m.x428 - m.x431 - m.x434 - m.x437 == 0)

m.c216 = Constraint(expr=   m.x129 - m.x429 - m.x432 - m.x435 - m.x438 == 0)

m.c217 = Constraint(expr=   m.x130 - m.x430 - m.x433 - m.x436 - m.x439 == 0)

m.c218 = Constraint(expr=   m.x113 - m.x404 - m.x407 - m.x410 - m.x413 == 0)

m.c219 = Constraint(expr=   m.x114 - m.x405 - m.x408 - m.x411 - m.x414 == 0)

m.c220 = Constraint(expr=   m.x115 - m.x406 - m.x409 - m.x412 - m.x415 == 0)

m.c221 = Constraint(expr=   m.x140 - m.x452 - m.x455 - m.x458 - m.x461 == 0)

m.c222 = Constraint(expr=   m.x141 - m.x453 - m.x456 - m.x459 - m.x462 == 0)

m.c223 = Constraint(expr=   m.x142 - m.x454 - m.x457 - m.x460 - m.x463 == 0)

m.c224 = Constraint(expr=   m.x143 - m.x464 - m.x467 - m.x470 - m.x473 == 0)

m.c225 = Constraint(expr=   m.x144 - m.x465 - m.x468 - m.x471 - m.x474 == 0)

m.c226 = Constraint(expr=   m.x145 - m.x466 - m.x469 - m.x472 - m.x475 == 0)

m.c227 = Constraint(expr=   m.x137 - m.x440 - m.x443 - m.x446 - m.x449 == 0)

m.c228 = Constraint(expr=   m.x138 - m.x441 - m.x444 - m.x447 - m.x450 == 0)

m.c229 = Constraint(expr=   m.x139 - m.x442 - m.x445 - m.x448 - m.x451 == 0)

m.c230 = Constraint(expr=   m.x149 - m.x488 - m.x491 - m.x494 - m.x497 == 0)

m.c231 = Constraint(expr=   m.x150 - m.x489 - m.x492 - m.x495 - m.x498 == 0)

m.c232 = Constraint(expr=   m.x151 - m.x490 - m.x493 - m.x496 - m.x499 == 0)

m.c233 = Constraint(expr=   m.x146 - m.x476 - m.x479 - m.x482 - m.x485 == 0)

m.c234 = Constraint(expr=   m.x147 - m.x477 - m.x480 - m.x483 - m.x486 == 0)

m.c235 = Constraint(expr=   m.x148 - m.x478 - m.x481 - m.x484 - m.x487 == 0)

m.c236 = Constraint(expr=   m.x158 - m.x524 - m.x527 - m.x530 - m.x533 == 0)

m.c237 = Constraint(expr=   m.x159 - m.x525 - m.x528 - m.x531 - m.x534 == 0)

m.c238 = Constraint(expr=   m.x160 - m.x526 - m.x529 - m.x532 - m.x535 == 0)

m.c239 = Constraint(expr=   m.x161 - m.x536 - m.x539 - m.x542 - m.x545 == 0)

m.c240 = Constraint(expr=   m.x162 - m.x537 - m.x540 - m.x543 - m.x546 == 0)

m.c241 = Constraint(expr=   m.x163 - m.x538 - m.x541 - m.x544 - m.x547 == 0)

m.c242 = Constraint(expr=   m.x155 - m.x512 - m.x515 - m.x518 - m.x521 == 0)

m.c243 = Constraint(expr=   m.x156 - m.x513 - m.x516 - m.x519 - m.x522 == 0)

m.c244 = Constraint(expr=   m.x157 - m.x514 - m.x517 - m.x520 - m.x523 == 0)

m.c245 = Constraint(expr=   m.x179 - m.x560 - m.x563 - m.x566 - m.x569 == 0)

m.c246 = Constraint(expr=   m.x180 - m.x561 - m.x564 - m.x567 - m.x570 == 0)

m.c247 = Constraint(expr=   m.x181 - m.x562 - m.x565 - m.x568 - m.x571 == 0)

m.c248 = Constraint(expr=   m.x152 - m.x500 - m.x503 - m.x506 - m.x509 == 0)

m.c249 = Constraint(expr=   m.x153 - m.x501 - m.x504 - m.x507 - m.x510 == 0)

m.c250 = Constraint(expr=   m.x154 - m.x502 - m.x505 - m.x508 - m.x511 == 0)

m.c251 = Constraint(expr=   m.x185 - m.x572 - m.x575 - m.x578 - m.x581 == 0)

m.c252 = Constraint(expr=   m.x186 - m.x573 - m.x576 - m.x579 - m.x582 == 0)

m.c253 = Constraint(expr=   m.x187 - m.x574 - m.x577 - m.x580 - m.x583 == 0)

m.c254 = Constraint(expr=   m.x176 - m.x548 - m.x551 - m.x554 - m.x557 == 0)

m.c255 = Constraint(expr=   m.x177 - m.x549 - m.x552 - m.x555 - m.x558 == 0)

m.c256 = Constraint(expr=   m.x178 - m.x550 - m.x553 - m.x556 - m.x559 == 0)

m.c257 = Constraint(expr=   m.x197 - m.x596 - m.x599 - m.x602 - m.x605 == 0)

m.c258 = Constraint(expr=   m.x198 - m.x597 - m.x600 - m.x603 - m.x606 == 0)

m.c259 = Constraint(expr=   m.x199 - m.x598 - m.x601 - m.x604 - m.x607 == 0)

m.c260 = Constraint(expr=   m.x194 - m.x584 - m.x587 - m.x590 - m.x593 == 0)

m.c261 = Constraint(expr=   m.x195 - m.x585 - m.x588 - m.x591 - m.x594 == 0)

m.c262 = Constraint(expr=   m.x196 - m.x586 - m.x589 - m.x592 - m.x595 == 0)

m.c263 = Constraint(expr=   m.x416 - 148.75*m.b764 <= 0)

m.c264 = Constraint(expr=   m.x417 - 127.5*m.b765 <= 0)

m.c265 = Constraint(expr=   m.x418 - 127.5*m.b766 <= 0)

m.c266 = Constraint(expr=   m.x419 - 148.75*m.b767 <= 0)

m.c267 = Constraint(expr=   m.x420 - 127.5*m.b768 <= 0)

m.c268 = Constraint(expr=   m.x421 - 127.5*m.b769 <= 0)

m.c269 = Constraint(expr=   m.x422 - 148.75*m.b770 <= 0)

m.c270 = Constraint(expr=   m.x423 - 127.5*m.b771 <= 0)

m.c271 = Constraint(expr=   m.x424 - 127.5*m.b772 <= 0)

m.c272 = Constraint(expr=   m.x425 - 148.75*m.b773 <= 0)

m.c273 = Constraint(expr=   m.x426 - 127.5*m.b774 <= 0)

m.c274 = Constraint(expr=   m.x427 - 127.5*m.b775 <= 0)

m.c275 = Constraint(expr=   m.x428 - 254.045833333333*m.b776 <= 0)

m.c276 = Constraint(expr=   m.x429 - 218.468333333333*m.b777 <= 0)

m.c277 = Constraint(expr=   m.x430 - 216.568333333333*m.b778 <= 0)

m.c278 = Constraint(expr=   m.x431 - 254.045833333333*m.b779 <= 0)

m.c279 = Constraint(expr=   m.x432 - 218.468333333333*m.b780 <= 0)

m.c280 = Constraint(expr=   m.x433 - 216.568333333333*m.b781 <= 0)

m.c281 = Constraint(expr=   m.x434 - 254.045833333333*m.b782 <= 0)

m.c282 = Constraint(expr=   m.x435 - 218.468333333333*m.b783 <= 0)

m.c283 = Constraint(expr=   m.x436 - 216.568333333333*m.b784 <= 0)

m.c284 = Constraint(expr=   m.x437 - 254.045833333333*m.b785 <= 0)

m.c285 = Constraint(expr=   m.x438 - 218.468333333333*m.b786 <= 0)

m.c286 = Constraint(expr=   m.x439 - 216.568333333333*m.b787 <= 0)

m.c287 = Constraint(expr=   m.x452 - 20.4166666666667*m.b788 <= 0)

m.c288 = Constraint(expr=   m.x453 - 17.9666666666667*m.b789 <= 0)

m.c289 = Constraint(expr=   m.x454 - 17.9666666666667*m.b790 <= 0)

m.c290 = Constraint(expr=   m.x455 - 20.4166666666667*m.b791 <= 0)

m.c291 = Constraint(expr=   m.x456 - 17.9666666666667*m.b792 <= 0)

m.c292 = Constraint(expr=   m.x457 - 17.9666666666667*m.b793 <= 0)

m.c293 = Constraint(expr=   m.x458 - 20.4166666666667*m.b794 <= 0)

m.c294 = Constraint(expr=   m.x459 - 17.9666666666667*m.b795 <= 0)

m.c295 = Constraint(expr=   m.x460 - 17.9666666666667*m.b796 <= 0)

m.c296 = Constraint(expr=   m.x461 - 20.4166666666667*m.b797 <= 0)

m.c297 = Constraint(expr=   m.x462 - 17.9666666666667*m.b798 <= 0)

m.c298 = Constraint(expr=   m.x463 - 17.9666666666667*m.b799 <= 0)

m.c299 = Constraint(expr=   m.x464 - 20.4166666666667*m.b788 <= 0)

m.c300 = Constraint(expr=   m.x465 - 17.9666666666667*m.b789 <= 0)

m.c301 = Constraint(expr=   m.x466 - 17.9666666666667*m.b790 <= 0)

m.c302 = Constraint(expr=   m.x467 - 20.4166666666667*m.b791 <= 0)

m.c303 = Constraint(expr=   m.x468 - 17.9666666666667*m.b792 <= 0)

m.c304 = Constraint(expr=   m.x469 - 17.9666666666667*m.b793 <= 0)

m.c305 = Constraint(expr=   m.x470 - 20.4166666666667*m.b794 <= 0)

m.c306 = Constraint(expr=   m.x471 - 17.9666666666667*m.b795 <= 0)

m.c307 = Constraint(expr=   m.x472 - 17.9666666666667*m.b796 <= 0)

m.c308 = Constraint(expr=   m.x473 - 20.4166666666667*m.b797 <= 0)

m.c309 = Constraint(expr=   m.x474 - 17.9666666666667*m.b798 <= 0)

m.c310 = Constraint(expr=   m.x475 - 17.9666666666667*m.b799 <= 0)

m.c311 = Constraint(expr=   m.x488 - 18.75*m.b800 <= 0)

m.c312 = Constraint(expr=   m.x489 - 16.5*m.b801 <= 0)

m.c313 = Constraint(expr=   m.x490 - 16.5*m.b802 <= 0)

m.c314 = Constraint(expr=   m.x491 - 18.75*m.b803 <= 0)

m.c315 = Constraint(expr=   m.x492 - 16.5*m.b804 <= 0)

m.c316 = Constraint(expr=   m.x493 - 16.5*m.b805 <= 0)

m.c317 = Constraint(expr=   m.x494 - 18.75*m.b806 <= 0)

m.c318 = Constraint(expr=   m.x495 - 16.5*m.b807 <= 0)

m.c319 = Constraint(expr=   m.x496 - 16.5*m.b808 <= 0)

m.c320 = Constraint(expr=   m.x497 - 18.75*m.b809 <= 0)

m.c321 = Constraint(expr=   m.x498 - 16.5*m.b810 <= 0)

m.c322 = Constraint(expr=   m.x499 - 16.5*m.b811 <= 0)

m.c323 = Constraint(expr=   m.x524 - 17.8125*m.b812 <= 0)

m.c324 = Constraint(expr=   m.x525 - 15.675*m.b813 <= 0)

m.c325 = Constraint(expr=   m.x526 - 15.675*m.b814 <= 0)

m.c326 = Constraint(expr=   m.x527 - 17.8125*m.b815 <= 0)

m.c327 = Constraint(expr=   m.x528 - 15.675*m.b816 <= 0)

m.c328 = Constraint(expr=   m.x529 - 15.675*m.b817 <= 0)

m.c329 = Constraint(expr=   m.x530 - 17.8125*m.b818 <= 0)

m.c330 = Constraint(expr=   m.x531 - 15.675*m.b819 <= 0)

m.c331 = Constraint(expr=   m.x532 - 15.675*m.b820 <= 0)

m.c332 = Constraint(expr=   m.x533 - 17.8125*m.b821 <= 0)

m.c333 = Constraint(expr=   m.x534 - 15.675*m.b822 <= 0)

m.c334 = Constraint(expr=   m.x535 - 15.675*m.b823 <= 0)

m.c335 = Constraint(expr=   m.x536 - 17.8125*m.b812 <= 0)

m.c336 = Constraint(expr=   m.x537 - 15.675*m.b813 <= 0)

m.c337 = Constraint(expr=   m.x538 - 15.675*m.b814 <= 0)

m.c338 = Constraint(expr=   m.x539 - 17.8125*m.b815 <= 0)

m.c339 = Constraint(expr=   m.x540 - 15.675*m.b816 <= 0)

m.c340 = Constraint(expr=   m.x541 - 15.675*m.b817 <= 0)

m.c341 = Constraint(expr=   m.x542 - 17.8125*m.b818 <= 0)

m.c342 = Constraint(expr=   m.x543 - 15.675*m.b819 <= 0)

m.c343 = Constraint(expr=   m.x544 - 15.675*m.b820 <= 0)

m.c344 = Constraint(expr=   m.x545 - 17.8125*m.b821 <= 0)

m.c345 = Constraint(expr=   m.x546 - 15.675*m.b822 <= 0)

m.c346 = Constraint(expr=   m.x547 - 15.675*m.b823 <= 0)

m.c347 = Constraint(expr=   m.x560 - 66.9375*m.b824 <= 0)

m.c348 = Constraint(expr=   m.x561 - 58.65*m.b825 <= 0)

m.c349 = Constraint(expr=   m.x562 - 56.525*m.b826 <= 0)

m.c350 = Constraint(expr=   m.x563 - 66.9375*m.b827 <= 0)

m.c351 = Constraint(expr=   m.x564 - 58.65*m.b828 <= 0)

m.c352 = Constraint(expr=   m.x565 - 56.525*m.b829 <= 0)

m.c353 = Constraint(expr=   m.x566 - 66.9375*m.b830 <= 0)

m.c354 = Constraint(expr=   m.x567 - 58.65*m.b831 <= 0)

m.c355 = Constraint(expr=   m.x568 - 56.525*m.b832 <= 0)

m.c356 = Constraint(expr=   m.x569 - 66.9375*m.b833 <= 0)

m.c357 = Constraint(expr=   m.x570 - 58.65*m.b834 <= 0)

m.c358 = Constraint(expr=   m.x571 - 56.525*m.b835 <= 0)

m.c359 = Constraint(expr=   m.x572 - 94.4571428571429*m.b836 <= 0)

m.c360 = Constraint(expr=   m.x573 - 81.0892857142857*m.b837 <= 0)

m.c361 = Constraint(expr=   m.x574 - 73.72*m.b838 <= 0)

m.c362 = Constraint(expr=   m.x575 - 94.4571428571429*m.b839 <= 0)

m.c363 = Constraint(expr=   m.x576 - 81.0892857142857*m.b840 <= 0)

m.c364 = Constraint(expr=   m.x577 - 73.72*m.b841 <= 0)

m.c365 = Constraint(expr=   m.x578 - 94.4571428571429*m.b842 <= 0)

m.c366 = Constraint(expr=   m.x579 - 81.0892857142857*m.b843 <= 0)

m.c367 = Constraint(expr=   m.x580 - 73.72*m.b844 <= 0)

m.c368 = Constraint(expr=   m.x581 - 94.4571428571429*m.b845 <= 0)

m.c369 = Constraint(expr=   m.x582 - 81.0892857142857*m.b846 <= 0)

m.c370 = Constraint(expr=   m.x583 - 73.72*m.b847 <= 0)

m.c371 = Constraint(expr=   m.x596 - 39.4285714285714*m.b848 <= 0)

m.c372 = Constraint(expr=   m.x597 - 32.8571428571429*m.b849 <= 0)

m.c373 = Constraint(expr=   m.x598 - 27.6*m.b850 <= 0)

m.c374 = Constraint(expr=   m.x599 - 39.4285714285714*m.b851 <= 0)

m.c375 = Constraint(expr=   m.x600 - 32.8571428571429*m.b852 <= 0)

m.c376 = Constraint(expr=   m.x601 - 27.6*m.b853 <= 0)

m.c377 = Constraint(expr=   m.x602 - 39.4285714285714*m.b854 <= 0)

m.c378 = Constraint(expr=   m.x603 - 32.8571428571429*m.b855 <= 0)

m.c379 = Constraint(expr=   m.x604 - 27.6*m.b856 <= 0)

m.c380 = Constraint(expr=   m.x605 - 39.4285714285714*m.b857 <= 0)

m.c381 = Constraint(expr=   m.x606 - 32.8571428571429*m.b858 <= 0)

m.c382 = Constraint(expr=   m.x607 - 27.6*m.b859 <= 0)

m.c383 = Constraint(expr=   m.x392 - 175*m.b764 <= 0)

m.c384 = Constraint(expr=   m.x393 - 150*m.b765 <= 0)

m.c385 = Constraint(expr=   m.x394 - 150*m.b766 <= 0)

m.c386 = Constraint(expr=   m.x395 - 175*m.b767 <= 0)

m.c387 = Constraint(expr=   m.x396 - 150*m.b768 <= 0)

m.c388 = Constraint(expr=   m.x397 - 150*m.b769 <= 0)

m.c389 = Constraint(expr=   m.x398 - 175*m.b770 <= 0)

m.c390 = Constraint(expr=   m.x399 - 150*m.b771 <= 0)

m.c391 = Constraint(expr=   m.x400 - 150*m.b772 <= 0)

m.c392 = Constraint(expr=   m.x401 - 175*m.b773 <= 0)

m.c393 = Constraint(expr=   m.x402 - 150*m.b774 <= 0)

m.c394 = Constraint(expr=   m.x403 - 150*m.b775 <= 0)

m.c395 = Constraint(expr=   m.x404 - 175*m.b776 <= 0)

m.c396 = Constraint(expr=   m.x405 - 150*m.b777 <= 0)

m.c397 = Constraint(expr=   m.x406 - 150*m.b778 <= 0)

m.c398 = Constraint(expr=   m.x407 - 175*m.b779 <= 0)

m.c399 = Constraint(expr=   m.x408 - 150*m.b780 <= 0)

m.c400 = Constraint(expr=   m.x409 - 150*m.b781 <= 0)

m.c401 = Constraint(expr=   m.x410 - 175*m.b782 <= 0)

m.c402 = Constraint(expr=   m.x411 - 150*m.b783 <= 0)

m.c403 = Constraint(expr=   m.x412 - 150*m.b784 <= 0)

m.c404 = Constraint(expr=   m.x413 - 175*m.b785 <= 0)

m.c405 = Constraint(expr=   m.x414 - 150*m.b786 <= 0)

m.c406 = Constraint(expr=   m.x415 - 150*m.b787 <= 0)

m.c407 = Constraint(expr=   m.x440 - 20.8333333333333*m.b788 <= 0)

m.c408 = Constraint(expr=   m.x441 - 18.3333333333333*m.b789 <= 0)

m.c409 = Constraint(expr=   m.x442 - 18.3333333333333*m.b790 <= 0)

m.c410 = Constraint(expr=   m.x443 - 20.8333333333333*m.b791 <= 0)

m.c411 = Constraint(expr=   m.x444 - 18.3333333333333*m.b792 <= 0)

m.c412 = Constraint(expr=   m.x445 - 18.3333333333333*m.b793 <= 0)

m.c413 = Constraint(expr=   m.x446 - 20.8333333333333*m.b794 <= 0)

m.c414 = Constraint(expr=   m.x447 - 18.3333333333333*m.b795 <= 0)

m.c415 = Constraint(expr=   m.x448 - 18.3333333333333*m.b796 <= 0)

m.c416 = Constraint(expr=   m.x449 - 20.8333333333333*m.b797 <= 0)

m.c417 = Constraint(expr=   m.x450 - 18.3333333333333*m.b798 <= 0)

m.c418 = Constraint(expr=   m.x451 - 18.3333333333333*m.b799 <= 0)

m.c419 = Constraint(expr=   m.x476 - 20.8333333333333*m.b800 <= 0)

m.c420 = Constraint(expr=   m.x477 - 18.3333333333333*m.b801 <= 0)

m.c421 = Constraint(expr=   m.x478 - 18.3333333333333*m.b802 <= 0)

m.c422 = Constraint(expr=   m.x479 - 20.8333333333333*m.b803 <= 0)

m.c423 = Constraint(expr=   m.x480 - 18.3333333333333*m.b804 <= 0)

m.c424 = Constraint(expr=   m.x481 - 18.3333333333333*m.b805 <= 0)

m.c425 = Constraint(expr=   m.x482 - 20.8333333333333*m.b806 <= 0)

m.c426 = Constraint(expr=   m.x483 - 18.3333333333333*m.b807 <= 0)

m.c427 = Constraint(expr=   m.x484 - 18.3333333333333*m.b808 <= 0)

m.c428 = Constraint(expr=   m.x485 - 20.8333333333333*m.b809 <= 0)

m.c429 = Constraint(expr=   m.x486 - 18.3333333333333*m.b810 <= 0)

m.c430 = Constraint(expr=   m.x487 - 18.3333333333333*m.b811 <= 0)

m.c431 = Constraint(expr=   m.x512 - 18.75*m.b812 <= 0)

m.c432 = Constraint(expr=   m.x513 - 16.5*m.b813 <= 0)

m.c433 = Constraint(expr=   m.x514 - 16.5*m.b814 <= 0)

m.c434 = Constraint(expr=   m.x515 - 18.75*m.b815 <= 0)

m.c435 = Constraint(expr=   m.x516 - 16.5*m.b816 <= 0)

m.c436 = Constraint(expr=   m.x517 - 16.5*m.b817 <= 0)

m.c437 = Constraint(expr=   m.x518 - 18.75*m.b818 <= 0)

m.c438 = Constraint(expr=   m.x519 - 16.5*m.b819 <= 0)

m.c439 = Constraint(expr=   m.x520 - 16.5*m.b820 <= 0)

m.c440 = Constraint(expr=   m.x521 - 18.75*m.b821 <= 0)

m.c441 = Constraint(expr=   m.x522 - 16.5*m.b822 <= 0)

m.c442 = Constraint(expr=   m.x523 - 16.5*m.b823 <= 0)

m.c443 = Constraint(expr=   m.x500 - 18.75*m.b824 <= 0)

m.c444 = Constraint(expr=   m.x501 - 16.5*m.b825 <= 0)

m.c445 = Constraint(expr=   m.x502 - 16.5*m.b826 <= 0)

m.c446 = Constraint(expr=   m.x503 - 18.75*m.b827 <= 0)

m.c447 = Constraint(expr=   m.x504 - 16.5*m.b828 <= 0)

m.c448 = Constraint(expr=   m.x505 - 16.5*m.b829 <= 0)

m.c449 = Constraint(expr=   m.x506 - 18.75*m.b830 <= 0)

m.c450 = Constraint(expr=   m.x507 - 16.5*m.b831 <= 0)

m.c451 = Constraint(expr=   m.x508 - 16.5*m.b832 <= 0)

m.c452 = Constraint(expr=   m.x509 - 18.75*m.b833 <= 0)

m.c453 = Constraint(expr=   m.x510 - 16.5*m.b834 <= 0)

m.c454 = Constraint(expr=   m.x511 - 16.5*m.b835 <= 0)

m.c455 = Constraint(expr=   m.x548 - 60*m.b836 <= 0)

m.c456 = Constraint(expr=   m.x549 - 52.5*m.b837 <= 0)

m.c457 = Constraint(expr=   m.x550 - 50*m.b838 <= 0)

m.c458 = Constraint(expr=   m.x551 - 60*m.b839 <= 0)

m.c459 = Constraint(expr=   m.x552 - 52.5*m.b840 <= 0)

m.c460 = Constraint(expr=   m.x553 - 50*m.b841 <= 0)

m.c461 = Constraint(expr=   m.x554 - 60*m.b842 <= 0)

m.c462 = Constraint(expr=   m.x555 - 52.5*m.b843 <= 0)

m.c463 = Constraint(expr=   m.x556 - 50*m.b844 <= 0)

m.c464 = Constraint(expr=   m.x557 - 60*m.b845 <= 0)

m.c465 = Constraint(expr=   m.x558 - 52.5*m.b846 <= 0)

m.c466 = Constraint(expr=   m.x559 - 50*m.b847 <= 0)

m.c467 = Constraint(expr=   m.x584 - 42.8571428571429*m.b848 <= 0)

m.c468 = Constraint(expr=   m.x585 - 35.7142857142857*m.b849 <= 0)

m.c469 = Constraint(expr=   m.x586 - 30*m.b850 <= 0)

m.c470 = Constraint(expr=   m.x587 - 42.8571428571429*m.b851 <= 0)

m.c471 = Constraint(expr=   m.x588 - 35.7142857142857*m.b852 <= 0)

m.c472 = Constraint(expr=   m.x589 - 30*m.b853 <= 0)

m.c473 = Constraint(expr=   m.x590 - 42.8571428571429*m.b854 <= 0)

m.c474 = Constraint(expr=   m.x591 - 35.7142857142857*m.b855 <= 0)

m.c475 = Constraint(expr=   m.x592 - 30*m.b856 <= 0)

m.c476 = Constraint(expr=   m.x593 - 42.8571428571429*m.b857 <= 0)

m.c477 = Constraint(expr=   m.x594 - 35.7142857142857*m.b858 <= 0)

m.c478 = Constraint(expr=   m.x595 - 30*m.b859 <= 0)

m.c479 = Constraint(expr= - 0.8*m.x392 + m.x416 == 0)

m.c480 = Constraint(expr= - 0.8*m.x393 + m.x417 == 0)

m.c481 = Constraint(expr= - 0.8*m.x394 + m.x418 == 0)

m.c482 = Constraint(expr= - 0.85*m.x395 + m.x419 == 0)

m.c483 = Constraint(expr= - 0.85*m.x396 + m.x420 == 0)

m.c484 = Constraint(expr= - 0.85*m.x397 + m.x421 == 0)

m.c485 = Constraint(expr= - 0.8*m.x398 + m.x422 == 0)

m.c486 = Constraint(expr= - 0.8*m.x399 + m.x423 == 0)

m.c487 = Constraint(expr= - 0.8*m.x400 + m.x424 == 0)

m.c488 = Constraint(expr= - 0.85*m.x401 + m.x425 == 0)

m.c489 = Constraint(expr= - 0.85*m.x402 + m.x426 == 0)

m.c490 = Constraint(expr= - 0.85*m.x403 + m.x427 == 0)

m.c491 = Constraint(expr= - 0.9*m.x404 + m.x428 == 0)

m.c492 = Constraint(expr= - 0.9*m.x405 + m.x429 == 0)

m.c493 = Constraint(expr= - 0.9*m.x406 + m.x430 == 0)

m.c494 = Constraint(expr= - 0.95*m.x407 + m.x431 == 0)

m.c495 = Constraint(expr= - 0.95*m.x408 + m.x432 == 0)

m.c496 = Constraint(expr= - 0.95*m.x409 + m.x433 == 0)

m.c497 = Constraint(expr= - 0.9*m.x410 + m.x434 == 0)

m.c498 = Constraint(expr= - 0.9*m.x411 + m.x435 == 0)

m.c499 = Constraint(expr= - 0.9*m.x412 + m.x436 == 0)

m.c500 = Constraint(expr= - 0.95*m.x413 + m.x437 == 0)

m.c501 = Constraint(expr= - 0.95*m.x414 + m.x438 == 0)

m.c502 = Constraint(expr= - 0.95*m.x415 + m.x439 == 0)

m.c503 = Constraint(expr= - 0.85*m.x440 + m.x452 == 0)

m.c504 = Constraint(expr= - 0.85*m.x441 + m.x453 == 0)

m.c505 = Constraint(expr= - 0.85*m.x442 + m.x454 == 0)

m.c506 = Constraint(expr= - 0.98*m.x443 + m.x455 == 0)

m.c507 = Constraint(expr= - 0.98*m.x444 + m.x456 == 0)

m.c508 = Constraint(expr= - 0.98*m.x445 + m.x457 == 0)

m.c509 = Constraint(expr= - 0.85*m.x446 + m.x458 == 0)

m.c510 = Constraint(expr= - 0.85*m.x447 + m.x459 == 0)

m.c511 = Constraint(expr= - 0.85*m.x448 + m.x460 == 0)

m.c512 = Constraint(expr= - 0.98*m.x449 + m.x461 == 0)

m.c513 = Constraint(expr= - 0.98*m.x450 + m.x462 == 0)

m.c514 = Constraint(expr= - 0.98*m.x451 + m.x463 == 0)

m.c515 = Constraint(expr= - 0.85*m.x440 + m.x464 == 0)

m.c516 = Constraint(expr= - 0.85*m.x441 + m.x465 == 0)

m.c517 = Constraint(expr= - 0.85*m.x442 + m.x466 == 0)

m.c518 = Constraint(expr= - 0.98*m.x443 + m.x467 == 0)

m.c519 = Constraint(expr= - 0.98*m.x444 + m.x468 == 0)

m.c520 = Constraint(expr= - 0.98*m.x445 + m.x469 == 0)

m.c521 = Constraint(expr= - 0.85*m.x446 + m.x470 == 0)

m.c522 = Constraint(expr= - 0.85*m.x447 + m.x471 == 0)

m.c523 = Constraint(expr= - 0.85*m.x448 + m.x472 == 0)

m.c524 = Constraint(expr= - 0.98*m.x449 + m.x473 == 0)

m.c525 = Constraint(expr= - 0.98*m.x450 + m.x474 == 0)

m.c526 = Constraint(expr= - 0.98*m.x451 + m.x475 == 0)

m.c527 = Constraint(expr= - 0.85*m.x476 + m.x488 == 0)

m.c528 = Constraint(expr= - 0.85*m.x477 + m.x489 == 0)

m.c529 = Constraint(expr= - 0.85*m.x478 + m.x490 == 0)

m.c530 = Constraint(expr= - 0.9*m.x479 + m.x491 == 0)

m.c531 = Constraint(expr= - 0.9*m.x480 + m.x492 == 0)

m.c532 = Constraint(expr= - 0.9*m.x481 + m.x493 == 0)

m.c533 = Constraint(expr= - 0.85*m.x482 + m.x494 == 0)

m.c534 = Constraint(expr= - 0.85*m.x483 + m.x495 == 0)

m.c535 = Constraint(expr= - 0.85*m.x484 + m.x496 == 0)

m.c536 = Constraint(expr= - 0.9*m.x485 + m.x497 == 0)

m.c537 = Constraint(expr= - 0.9*m.x486 + m.x498 == 0)

m.c538 = Constraint(expr= - 0.9*m.x487 + m.x499 == 0)

m.c539 = Constraint(expr= - 0.75*m.x512 + m.x524 == 0)

m.c540 = Constraint(expr= - 0.75*m.x513 + m.x525 == 0)

m.c541 = Constraint(expr= - 0.75*m.x514 + m.x526 == 0)

m.c542 = Constraint(expr= - 0.95*m.x515 + m.x527 == 0)

m.c543 = Constraint(expr= - 0.95*m.x516 + m.x528 == 0)

m.c544 = Constraint(expr= - 0.95*m.x517 + m.x529 == 0)

m.c545 = Constraint(expr= - 0.9*m.x518 + m.x530 == 0)

m.c546 = Constraint(expr= - 0.9*m.x519 + m.x531 == 0)

m.c547 = Constraint(expr= - 0.9*m.x520 + m.x532 == 0)

m.c548 = Constraint(expr= - 0.95*m.x521 + m.x533 == 0)

m.c549 = Constraint(expr= - 0.95*m.x522 + m.x534 == 0)

m.c550 = Constraint(expr= - 0.95*m.x523 + m.x535 == 0)

m.c551 = Constraint(expr= - 0.75*m.x512 + m.x536 == 0)

m.c552 = Constraint(expr= - 0.75*m.x513 + m.x537 == 0)

m.c553 = Constraint(expr= - 0.75*m.x514 + m.x538 == 0)

m.c554 = Constraint(expr= - 0.95*m.x515 + m.x539 == 0)

m.c555 = Constraint(expr= - 0.95*m.x516 + m.x540 == 0)

m.c556 = Constraint(expr= - 0.95*m.x517 + m.x541 == 0)

m.c557 = Constraint(expr= - 0.9*m.x518 + m.x542 == 0)

m.c558 = Constraint(expr= - 0.9*m.x519 + m.x543 == 0)

m.c559 = Constraint(expr= - 0.9*m.x520 + m.x544 == 0)

m.c560 = Constraint(expr= - 0.95*m.x521 + m.x545 == 0)

m.c561 = Constraint(expr= - 0.95*m.x522 + m.x546 == 0)

m.c562 = Constraint(expr= - 0.95*m.x523 + m.x547 == 0)

m.c563 = Constraint(expr= - 0.8*m.x500 + m.x560 == 0)

m.c564 = Constraint(expr= - 0.8*m.x501 + m.x561 == 0)

m.c565 = Constraint(expr= - 0.8*m.x502 + m.x562 == 0)

m.c566 = Constraint(expr= - 0.85*m.x503 + m.x563 == 0)

m.c567 = Constraint(expr= - 0.85*m.x504 + m.x564 == 0)

m.c568 = Constraint(expr= - 0.85*m.x505 + m.x565 == 0)

m.c569 = Constraint(expr= - 0.8*m.x506 + m.x566 == 0)

m.c570 = Constraint(expr= - 0.8*m.x507 + m.x567 == 0)

m.c571 = Constraint(expr= - 0.8*m.x508 + m.x568 == 0)

m.c572 = Constraint(expr= - 0.85*m.x509 + m.x569 == 0)

m.c573 = Constraint(expr= - 0.85*m.x510 + m.x570 == 0)

m.c574 = Constraint(expr= - 0.85*m.x511 + m.x571 == 0)

m.c575 = Constraint(expr= - 0.85*m.x548 + m.x572 == 0)

m.c576 = Constraint(expr= - 0.85*m.x549 + m.x573 == 0)

m.c577 = Constraint(expr= - 0.85*m.x550 + m.x574 == 0)

m.c578 = Constraint(expr= - 0.95*m.x551 + m.x575 == 0)

m.c579 = Constraint(expr= - 0.95*m.x552 + m.x576 == 0)

m.c580 = Constraint(expr= - 0.95*m.x553 + m.x577 == 0)

m.c581 = Constraint(expr= - 0.85*m.x554 + m.x578 == 0)

m.c582 = Constraint(expr= - 0.85*m.x555 + m.x579 == 0)

m.c583 = Constraint(expr= - 0.85*m.x556 + m.x580 == 0)

m.c584 = Constraint(expr= - 0.95*m.x557 + m.x581 == 0)

m.c585 = Constraint(expr= - 0.95*m.x558 + m.x582 == 0)

m.c586 = Constraint(expr= - 0.95*m.x559 + m.x583 == 0)

m.c587 = Constraint(expr= - 0.8*m.x584 + m.x596 == 0)

m.c588 = Constraint(expr= - 0.8*m.x585 + m.x597 == 0)

m.c589 = Constraint(expr= - 0.8*m.x586 + m.x598 == 0)

m.c590 = Constraint(expr= - 0.92*m.x587 + m.x599 == 0)

m.c591 = Constraint(expr= - 0.92*m.x588 + m.x600 == 0)

m.c592 = Constraint(expr= - 0.92*m.x589 + m.x601 == 0)

m.c593 = Constraint(expr= - 0.8*m.x590 + m.x602 == 0)

m.c594 = Constraint(expr= - 0.8*m.x591 + m.x603 == 0)

m.c595 = Constraint(expr= - 0.8*m.x592 + m.x604 == 0)

m.c596 = Constraint(expr= - 0.92*m.x593 + m.x605 == 0)

m.c597 = Constraint(expr= - 0.92*m.x594 + m.x606 == 0)

m.c598 = Constraint(expr= - 0.92*m.x595 + m.x607 == 0)

m.c599 = Constraint(expr=   m.x5 - m.x260 - m.x263 - m.x266 - m.x269 == 0)

m.c600 = Constraint(expr=   m.x6 - m.x261 - m.x264 - m.x267 - m.x270 == 0)

m.c601 = Constraint(expr=   m.x7 - m.x262 - m.x265 - m.x268 - m.x271 == 0)

m.c602 = Constraint(expr=   m.x8 - m.x272 - m.x275 - m.x278 - m.x281 == 0)

m.c603 = Constraint(expr=   m.x9 - m.x273 - m.x276 - m.x279 - m.x282 == 0)

m.c604 = Constraint(expr=   m.x10 - m.x274 - m.x277 - m.x280 - m.x283 == 0)

m.c605 = Constraint(expr=   m.x20 - m.x284 - m.x287 - m.x290 - m.x293 == 0)

m.c606 = Constraint(expr=   m.x21 - m.x285 - m.x288 - m.x291 - m.x294 == 0)

m.c607 = Constraint(expr=   m.x22 - m.x286 - m.x289 - m.x292 - m.x295 == 0)

m.c608 = Constraint(expr=   m.x32 - m.x296 - m.x299 - m.x302 - m.x305 == 0)

m.c609 = Constraint(expr=   m.x33 - m.x297 - m.x300 - m.x303 - m.x306 == 0)

m.c610 = Constraint(expr=   m.x34 - m.x298 - m.x301 - m.x304 - m.x307 == 0)

m.c611 = Constraint(expr=   m.x41 - m.x308 - m.x311 - m.x314 - m.x317 == 0)

m.c612 = Constraint(expr=   m.x42 - m.x309 - m.x312 - m.x315 - m.x318 == 0)

m.c613 = Constraint(expr=   m.x43 - m.x310 - m.x313 - m.x316 - m.x319 == 0)

m.c614 = Constraint(expr=   m.x50 - m.x332 - m.x335 - m.x338 - m.x341 == 0)

m.c615 = Constraint(expr=   m.x51 - m.x333 - m.x336 - m.x339 - m.x342 == 0)

m.c616 = Constraint(expr=   m.x52 - m.x334 - m.x337 - m.x340 - m.x343 == 0)

m.c617 = Constraint(expr=   m.x47 - m.x320 - m.x323 - m.x326 - m.x329 == 0)

m.c618 = Constraint(expr=   m.x48 - m.x321 - m.x324 - m.x327 - m.x330 == 0)

m.c619 = Constraint(expr=   m.x49 - m.x322 - m.x325 - m.x328 - m.x331 == 0)

m.c620 = Constraint(expr=   m.x68 - m.x344 - m.x347 - m.x350 - m.x353 == 0)

m.c621 = Constraint(expr=   m.x69 - m.x345 - m.x348 - m.x351 - m.x354 == 0)

m.c622 = Constraint(expr=   m.x70 - m.x346 - m.x349 - m.x352 - m.x355 == 0)

m.c623 = Constraint(expr=   m.x71 - m.x356 - m.x359 - m.x362 - m.x365 == 0)

m.c624 = Constraint(expr=   m.x72 - m.x357 - m.x360 - m.x363 - m.x366 == 0)

m.c625 = Constraint(expr=   m.x73 - m.x358 - m.x361 - m.x364 - m.x367 == 0)

m.c626 = Constraint(expr=   m.x92 - m.x380 - m.x383 - m.x386 - m.x389 == 0)

m.c627 = Constraint(expr=   m.x93 - m.x381 - m.x384 - m.x387 - m.x390 == 0)

m.c628 = Constraint(expr=   m.x94 - m.x382 - m.x385 - m.x388 - m.x391 == 0)

m.c629 = Constraint(expr=   m.x89 - m.x368 - m.x371 - m.x374 - m.x377 == 0)

m.c630 = Constraint(expr=   m.x90 - m.x369 - m.x372 - m.x375 - m.x378 == 0)

m.c631 = Constraint(expr=   m.x91 - m.x370 - m.x373 - m.x376 - m.x379 == 0)

m.c632 = Constraint(expr=   m.x260 - 35*m.b764 <= 0)

m.c633 = Constraint(expr=   m.x261 - 30*m.b765 <= 0)

m.c634 = Constraint(expr=   m.x262 - 30*m.b766 <= 0)

m.c635 = Constraint(expr=   m.x263 - 35*m.b767 <= 0)

m.c636 = Constraint(expr=   m.x264 - 30*m.b768 <= 0)

m.c637 = Constraint(expr=   m.x265 - 30*m.b769 <= 0)

m.c638 = Constraint(expr=   m.x266 - 35*m.b770 <= 0)

m.c639 = Constraint(expr=   m.x267 - 30*m.b771 <= 0)

m.c640 = Constraint(expr=   m.x268 - 30*m.b772 <= 0)

m.c641 = Constraint(expr=   m.x269 - 35*m.b773 <= 0)

m.c642 = Constraint(expr=   m.x270 - 30*m.b774 <= 0)

m.c643 = Constraint(expr=   m.x271 - 30*m.b775 <= 0)

m.c644 = Constraint(expr=   m.x272 - 35*m.b776 <= 0)

m.c645 = Constraint(expr=   m.x273 - 30*m.b777 <= 0)

m.c646 = Constraint(expr=   m.x274 - 30*m.b778 <= 0)

m.c647 = Constraint(expr=   m.x275 - 35*m.b779 <= 0)

m.c648 = Constraint(expr=   m.x276 - 30*m.b780 <= 0)

m.c649 = Constraint(expr=   m.x277 - 30*m.b781 <= 0)

m.c650 = Constraint(expr=   m.x278 - 35*m.b782 <= 0)

m.c651 = Constraint(expr=   m.x279 - 30*m.b783 <= 0)

m.c652 = Constraint(expr=   m.x280 - 30*m.b784 <= 0)

m.c653 = Constraint(expr=   m.x281 - 35*m.b785 <= 0)

m.c654 = Constraint(expr=   m.x282 - 30*m.b786 <= 0)

m.c655 = Constraint(expr=   m.x283 - 30*m.b787 <= 0)

m.c656 = Constraint(expr=   m.x284 - 61*m.b776 <= 0)

m.c657 = Constraint(expr=   m.x285 - 53*m.b777 <= 0)

m.c658 = Constraint(expr=   m.x286 - 52*m.b778 <= 0)

m.c659 = Constraint(expr=   m.x287 - 61*m.b779 <= 0)

m.c660 = Constraint(expr=   m.x288 - 53*m.b780 <= 0)

m.c661 = Constraint(expr=   m.x289 - 52*m.b781 <= 0)

m.c662 = Constraint(expr=   m.x290 - 61*m.b782 <= 0)

m.c663 = Constraint(expr=   m.x291 - 53*m.b783 <= 0)

m.c664 = Constraint(expr=   m.x292 - 52*m.b784 <= 0)

m.c665 = Constraint(expr=   m.x293 - 61*m.b785 <= 0)

m.c666 = Constraint(expr=   m.x294 - 53*m.b786 <= 0)

m.c667 = Constraint(expr=   m.x295 - 52*m.b787 <= 0)

m.c668 = Constraint(expr=   m.x296 - 25*m.b788 <= 0)

m.c669 = Constraint(expr=   m.x297 - 22*m.b789 <= 0)

m.c670 = Constraint(expr=   m.x298 - 22*m.b790 <= 0)

m.c671 = Constraint(expr=   m.x299 - 25*m.b791 <= 0)

m.c672 = Constraint(expr=   m.x300 - 22*m.b792 <= 0)

m.c673 = Constraint(expr=   m.x301 - 22*m.b793 <= 0)

m.c674 = Constraint(expr=   m.x302 - 25*m.b794 <= 0)

m.c675 = Constraint(expr=   m.x303 - 22*m.b795 <= 0)

m.c676 = Constraint(expr=   m.x304 - 22*m.b796 <= 0)

m.c677 = Constraint(expr=   m.x305 - 25*m.b797 <= 0)

m.c678 = Constraint(expr=   m.x306 - 22*m.b798 <= 0)

m.c679 = Constraint(expr=   m.x307 - 22*m.b799 <= 0)

m.c680 = Constraint(expr=   m.x308 - 25*m.b800 <= 0)

m.c681 = Constraint(expr=   m.x309 - 22*m.b801 <= 0)

m.c682 = Constraint(expr=   m.x310 - 22*m.b802 <= 0)

m.c683 = Constraint(expr=   m.x311 - 25*m.b803 <= 0)

m.c684 = Constraint(expr=   m.x312 - 22*m.b804 <= 0)

m.c685 = Constraint(expr=   m.x313 - 22*m.b805 <= 0)

m.c686 = Constraint(expr=   m.x314 - 25*m.b806 <= 0)

m.c687 = Constraint(expr=   m.x315 - 22*m.b807 <= 0)

m.c688 = Constraint(expr=   m.x316 - 22*m.b808 <= 0)

m.c689 = Constraint(expr=   m.x317 - 25*m.b809 <= 0)

m.c690 = Constraint(expr=   m.x318 - 22*m.b810 <= 0)

m.c691 = Constraint(expr=   m.x319 - 22*m.b811 <= 0)

m.c692 = Constraint(expr=   m.x332 - 25*m.b812 <= 0)

m.c693 = Constraint(expr=   m.x333 - 22*m.b813 <= 0)

m.c694 = Constraint(expr=   m.x334 - 22*m.b814 <= 0)

m.c695 = Constraint(expr=   m.x335 - 25*m.b815 <= 0)

m.c696 = Constraint(expr=   m.x336 - 22*m.b816 <= 0)

m.c697 = Constraint(expr=   m.x337 - 22*m.b817 <= 0)

m.c698 = Constraint(expr=   m.x338 - 25*m.b818 <= 0)

m.c699 = Constraint(expr=   m.x339 - 22*m.b819 <= 0)

m.c700 = Constraint(expr=   m.x340 - 22*m.b820 <= 0)

m.c701 = Constraint(expr=   m.x341 - 25*m.b821 <= 0)

m.c702 = Constraint(expr=   m.x342 - 22*m.b822 <= 0)

m.c703 = Constraint(expr=   m.x343 - 22*m.b823 <= 0)

m.c704 = Constraint(expr=   m.x320 - 25*m.b824 <= 0)

m.c705 = Constraint(expr=   m.x321 - 22*m.b825 <= 0)

m.c706 = Constraint(expr=   m.x322 - 22*m.b826 <= 0)

m.c707 = Constraint(expr=   m.x323 - 25*m.b827 <= 0)

m.c708 = Constraint(expr=   m.x324 - 22*m.b828 <= 0)

m.c709 = Constraint(expr=   m.x325 - 22*m.b829 <= 0)

m.c710 = Constraint(expr=   m.x326 - 25*m.b830 <= 0)

m.c711 = Constraint(expr=   m.x327 - 22*m.b831 <= 0)

m.c712 = Constraint(expr=   m.x328 - 22*m.b832 <= 0)

m.c713 = Constraint(expr=   m.x329 - 25*m.b833 <= 0)

m.c714 = Constraint(expr=   m.x330 - 22*m.b834 <= 0)

m.c715 = Constraint(expr=   m.x331 - 22*m.b835 <= 0)

m.c716 = Constraint(expr=   m.x344 - 24*m.b824 <= 0)

m.c717 = Constraint(expr=   m.x345 - 21*m.b825 <= 0)

m.c718 = Constraint(expr=   m.x346 - 20*m.b826 <= 0)

m.c719 = Constraint(expr=   m.x347 - 24*m.b827 <= 0)

m.c720 = Constraint(expr=   m.x348 - 21*m.b828 <= 0)

m.c721 = Constraint(expr=   m.x349 - 20*m.b829 <= 0)

m.c722 = Constraint(expr=   m.x350 - 24*m.b830 <= 0)

m.c723 = Constraint(expr=   m.x351 - 21*m.b831 <= 0)

m.c724 = Constraint(expr=   m.x352 - 20*m.b832 <= 0)

m.c725 = Constraint(expr=   m.x353 - 24*m.b833 <= 0)

m.c726 = Constraint(expr=   m.x354 - 21*m.b834 <= 0)

m.c727 = Constraint(expr=   m.x355 - 20*m.b835 <= 0)

m.c728 = Constraint(expr=   m.x356 - 24*m.b836 <= 0)

m.c729 = Constraint(expr=   m.x357 - 21*m.b837 <= 0)

m.c730 = Constraint(expr=   m.x358 - 20*m.b838 <= 0)

m.c731 = Constraint(expr=   m.x359 - 24*m.b839 <= 0)

m.c732 = Constraint(expr=   m.x360 - 21*m.b840 <= 0)

m.c733 = Constraint(expr=   m.x361 - 20*m.b841 <= 0)

m.c734 = Constraint(expr=   m.x362 - 24*m.b842 <= 0)

m.c735 = Constraint(expr=   m.x363 - 21*m.b843 <= 0)

m.c736 = Constraint(expr=   m.x364 - 20*m.b844 <= 0)

m.c737 = Constraint(expr=   m.x365 - 24*m.b845 <= 0)

m.c738 = Constraint(expr=   m.x366 - 21*m.b846 <= 0)

m.c739 = Constraint(expr=   m.x367 - 20*m.b847 <= 0)

m.c740 = Constraint(expr=   m.x380 - 30*m.b836 <= 0)

m.c741 = Constraint(expr=   m.x381 - 25*m.b837 <= 0)

m.c742 = Constraint(expr=   m.x382 - 21*m.b838 <= 0)

m.c743 = Constraint(expr=   m.x383 - 30*m.b839 <= 0)

m.c744 = Constraint(expr=   m.x384 - 25*m.b840 <= 0)

m.c745 = Constraint(expr=   m.x385 - 21*m.b841 <= 0)

m.c746 = Constraint(expr=   m.x386 - 30*m.b842 <= 0)

m.c747 = Constraint(expr=   m.x387 - 25*m.b843 <= 0)

m.c748 = Constraint(expr=   m.x388 - 21*m.b844 <= 0)

m.c749 = Constraint(expr=   m.x389 - 30*m.b845 <= 0)

m.c750 = Constraint(expr=   m.x390 - 25*m.b846 <= 0)

m.c751 = Constraint(expr=   m.x391 - 21*m.b847 <= 0)

m.c752 = Constraint(expr=   m.x368 - 30*m.b848 <= 0)

m.c753 = Constraint(expr=   m.x369 - 25*m.b849 <= 0)

m.c754 = Constraint(expr=   m.x370 - 21*m.b850 <= 0)

m.c755 = Constraint(expr=   m.x371 - 30*m.b851 <= 0)

m.c756 = Constraint(expr=   m.x372 - 25*m.b852 <= 0)

m.c757 = Constraint(expr=   m.x373 - 21*m.b853 <= 0)

m.c758 = Constraint(expr=   m.x374 - 30*m.b854 <= 0)

m.c759 = Constraint(expr=   m.x375 - 25*m.b855 <= 0)

m.c760 = Constraint(expr=   m.x376 - 21*m.b856 <= 0)

m.c761 = Constraint(expr=   m.x377 - 30*m.b857 <= 0)

m.c762 = Constraint(expr=   m.x378 - 25*m.b858 <= 0)

m.c763 = Constraint(expr=   m.x379 - 21*m.b859 <= 0)

m.c764 = Constraint(expr=   m.x260 - 10*m.b764 <= 0)

m.c765 = Constraint(expr=   m.x261 - 10*m.b765 <= 0)

m.c766 = Constraint(expr=   m.x262 - 10*m.b766 <= 0)

m.c767 = Constraint(expr=   m.x263 - 10*m.b767 <= 0)

m.c768 = Constraint(expr=   m.x264 - 10*m.b768 <= 0)

m.c769 = Constraint(expr=   m.x265 - 10*m.b769 <= 0)

m.c770 = Constraint(expr=   m.x266 - 50*m.b770 <= 0)

m.c771 = Constraint(expr=   m.x267 - 50*m.b771 <= 0)

m.c772 = Constraint(expr=   m.x268 - 50*m.b772 <= 0)

m.c773 = Constraint(expr=   m.x269 - 50*m.b773 <= 0)

m.c774 = Constraint(expr=   m.x270 - 50*m.b774 <= 0)

m.c775 = Constraint(expr=   m.x271 - 50*m.b775 <= 0)

m.c776 = Constraint(expr=   m.x272 + m.x284 - 40*m.b776 <= 0)

m.c777 = Constraint(expr=   m.x273 + m.x285 - 40*m.b777 <= 0)

m.c778 = Constraint(expr=   m.x274 + m.x286 - 40*m.b778 <= 0)

m.c779 = Constraint(expr=   m.x275 + m.x287 - 40*m.b779 <= 0)

m.c780 = Constraint(expr=   m.x276 + m.x288 - 40*m.b780 <= 0)

m.c781 = Constraint(expr=   m.x277 + m.x289 - 40*m.b781 <= 0)

m.c782 = Constraint(expr=   m.x278 + m.x290 - 60*m.b782 <= 0)

m.c783 = Constraint(expr=   m.x279 + m.x291 - 60*m.b783 <= 0)

m.c784 = Constraint(expr=   m.x280 + m.x292 - 60*m.b784 <= 0)

m.c785 = Constraint(expr=   m.x281 + m.x293 - 60*m.b785 <= 0)

m.c786 = Constraint(expr=   m.x282 + m.x294 - 60*m.b786 <= 0)

m.c787 = Constraint(expr=   m.x283 + m.x295 - 60*m.b787 <= 0)

m.c788 = Constraint(expr=   m.x296 - 15*m.b788 <= 0)

m.c789 = Constraint(expr=   m.x297 - 15*m.b789 <= 0)

m.c790 = Constraint(expr=   m.x298 - 15*m.b790 <= 0)

m.c791 = Constraint(expr=   m.x299 - 15*m.b791 <= 0)

m.c792 = Constraint(expr=   m.x300 - 15*m.b792 <= 0)

m.c793 = Constraint(expr=   m.x301 - 15*m.b793 <= 0)

m.c794 = Constraint(expr=   m.x302 - 25*m.b794 <= 0)

m.c795 = Constraint(expr=   m.x303 - 25*m.b795 <= 0)

m.c796 = Constraint(expr=   m.x304 - 25*m.b796 <= 0)

m.c797 = Constraint(expr=   m.x305 - 25*m.b797 <= 0)

m.c798 = Constraint(expr=   m.x306 - 25*m.b798 <= 0)

m.c799 = Constraint(expr=   m.x307 - 25*m.b799 <= 0)

m.c800 = Constraint(expr=   m.x308 - 15*m.b800 <= 0)

m.c801 = Constraint(expr=   m.x309 - 15*m.b801 <= 0)

m.c802 = Constraint(expr=   m.x310 - 15*m.b802 <= 0)

m.c803 = Constraint(expr=   m.x311 - 15*m.b803 <= 0)

m.c804 = Constraint(expr=   m.x312 - 15*m.b804 <= 0)

m.c805 = Constraint(expr=   m.x313 - 15*m.b805 <= 0)

m.c806 = Constraint(expr=   m.x314 - 20*m.b806 <= 0)

m.c807 = Constraint(expr=   m.x315 - 20*m.b807 <= 0)

m.c808 = Constraint(expr=   m.x316 - 20*m.b808 <= 0)

m.c809 = Constraint(expr=   m.x317 - 20*m.b809 <= 0)

m.c810 = Constraint(expr=   m.x318 - 20*m.b810 <= 0)

m.c811 = Constraint(expr=   m.x319 - 20*m.b811 <= 0)

m.c812 = Constraint(expr=   m.x332 - 10*m.b812 <= 0)

m.c813 = Constraint(expr=   m.x333 - 10*m.b813 <= 0)

m.c814 = Constraint(expr=   m.x334 - 10*m.b814 <= 0)

m.c815 = Constraint(expr=   m.x335 - 10*m.b815 <= 0)

m.c816 = Constraint(expr=   m.x336 - 10*m.b816 <= 0)

m.c817 = Constraint(expr=   m.x337 - 10*m.b817 <= 0)

m.c818 = Constraint(expr=   m.x338 - 20*m.b818 <= 0)

m.c819 = Constraint(expr=   m.x339 - 20*m.b819 <= 0)

m.c820 = Constraint(expr=   m.x340 - 20*m.b820 <= 0)

m.c821 = Constraint(expr=   m.x341 - 20*m.b821 <= 0)

m.c822 = Constraint(expr=   m.x342 - 20*m.b822 <= 0)

m.c823 = Constraint(expr=   m.x343 - 20*m.b823 <= 0)

m.c824 = Constraint(expr=   m.x320 + m.x344 - 20*m.b824 <= 0)

m.c825 = Constraint(expr=   m.x321 + m.x345 - 20*m.b825 <= 0)

m.c826 = Constraint(expr=   m.x322 + m.x346 - 20*m.b826 <= 0)

m.c827 = Constraint(expr=   m.x323 + m.x347 - 20*m.b827 <= 0)

m.c828 = Constraint(expr=   m.x324 + m.x348 - 20*m.b828 <= 0)

m.c829 = Constraint(expr=   m.x325 + m.x349 - 20*m.b829 <= 0)

m.c830 = Constraint(expr=   m.x326 + m.x350 - 55*m.b830 <= 0)

m.c831 = Constraint(expr=   m.x327 + m.x351 - 55*m.b831 <= 0)

m.c832 = Constraint(expr=   m.x328 + m.x352 - 55*m.b832 <= 0)

m.c833 = Constraint(expr=   m.x329 + m.x353 - 55*m.b833 <= 0)

m.c834 = Constraint(expr=   m.x330 + m.x354 - 55*m.b834 <= 0)

m.c835 = Constraint(expr=   m.x331 + m.x355 - 55*m.b835 <= 0)

m.c836 = Constraint(expr=   m.x356 + m.x380 - 25*m.b836 <= 0)

m.c837 = Constraint(expr=   m.x357 + m.x381 - 25*m.b837 <= 0)

m.c838 = Constraint(expr=   m.x358 + m.x382 - 25*m.b838 <= 0)

m.c839 = Constraint(expr=   m.x359 + m.x383 - 25*m.b839 <= 0)

m.c840 = Constraint(expr=   m.x360 + m.x384 - 25*m.b840 <= 0)

m.c841 = Constraint(expr=   m.x361 + m.x385 - 25*m.b841 <= 0)

m.c842 = Constraint(expr=   m.x362 + m.x386 - 50*m.b842 <= 0)

m.c843 = Constraint(expr=   m.x363 + m.x387 - 50*m.b843 <= 0)

m.c844 = Constraint(expr=   m.x364 + m.x388 - 50*m.b844 <= 0)

m.c845 = Constraint(expr=   m.x365 + m.x389 - 50*m.b845 <= 0)

m.c846 = Constraint(expr=   m.x366 + m.x390 - 50*m.b846 <= 0)

m.c847 = Constraint(expr=   m.x367 + m.x391 - 50*m.b847 <= 0)

m.c848 = Constraint(expr=   m.x368 - 15*m.b848 <= 0)

m.c849 = Constraint(expr=   m.x369 - 15*m.b849 <= 0)

m.c850 = Constraint(expr=   m.x370 - 15*m.b850 <= 0)

m.c851 = Constraint(expr=   m.x371 - 15*m.b851 <= 0)

m.c852 = Constraint(expr=   m.x372 - 15*m.b852 <= 0)

m.c853 = Constraint(expr=   m.x373 - 15*m.b853 <= 0)

m.c854 = Constraint(expr=   m.x374 - 35*m.b854 <= 0)

m.c855 = Constraint(expr=   m.x375 - 35*m.b855 <= 0)

m.c856 = Constraint(expr=   m.x376 - 35*m.b856 <= 0)

m.c857 = Constraint(expr=   m.x377 - 35*m.b857 <= 0)

m.c858 = Constraint(expr=   m.x378 - 35*m.b858 <= 0)

m.c859 = Constraint(expr=   m.x379 - 35*m.b859 <= 0)

m.c860 = Constraint(expr=   m.x236 - m.x608 - m.x611 - m.x614 - m.x617 == 0)

m.c861 = Constraint(expr=   m.x237 - m.x609 - m.x612 - m.x615 - m.x618 == 0)

m.c862 = Constraint(expr=   m.x238 - m.x610 - m.x613 - m.x616 - m.x619 == 0)

m.c863 = Constraint(expr=   m.x239 - m.x620 - m.x623 - m.x626 - m.x629 == 0)

m.c864 = Constraint(expr=   m.x240 - m.x621 - m.x624 - m.x627 - m.x630 == 0)

m.c865 = Constraint(expr=   m.x241 - m.x622 - m.x625 - m.x628 - m.x631 == 0)

m.c866 = Constraint(expr=   m.x242 - m.x632 - m.x635 - m.x638 - m.x641 == 0)

m.c867 = Constraint(expr=   m.x243 - m.x633 - m.x636 - m.x639 - m.x642 == 0)

m.c868 = Constraint(expr=   m.x244 - m.x634 - m.x637 - m.x640 - m.x643 == 0)

m.c869 = Constraint(expr=   m.x245 - m.x644 - m.x647 - m.x650 - m.x653 == 0)

m.c870 = Constraint(expr=   m.x246 - m.x645 - m.x648 - m.x651 - m.x654 == 0)

m.c871 = Constraint(expr=   m.x247 - m.x646 - m.x649 - m.x652 - m.x655 == 0)

m.c872 = Constraint(expr=   m.x248 - m.x656 - m.x659 - m.x662 - m.x665 == 0)

m.c873 = Constraint(expr=   m.x249 - m.x657 - m.x660 - m.x663 - m.x666 == 0)

m.c874 = Constraint(expr=   m.x250 - m.x658 - m.x661 - m.x664 - m.x667 == 0)

m.c875 = Constraint(expr=   m.x251 - m.x668 - m.x671 - m.x674 - m.x677 == 0)

m.c876 = Constraint(expr=   m.x252 - m.x669 - m.x672 - m.x675 - m.x678 == 0)

m.c877 = Constraint(expr=   m.x253 - m.x670 - m.x673 - m.x676 - m.x679 == 0)

m.c878 = Constraint(expr=   m.x254 - m.x680 - m.x683 - m.x686 - m.x689 == 0)

m.c879 = Constraint(expr=   m.x255 - m.x681 - m.x684 - m.x687 - m.x690 == 0)

m.c880 = Constraint(expr=   m.x256 - m.x682 - m.x685 - m.x688 - m.x691 == 0)

m.c881 = Constraint(expr=   m.x257 - m.x692 - m.x695 - m.x698 - m.x701 == 0)

m.c882 = Constraint(expr=   m.x258 - m.x693 - m.x696 - m.x699 - m.x702 == 0)

m.c883 = Constraint(expr=   m.x259 - m.x694 - m.x697 - m.x700 - m.x703 == 0)

m.c884 = Constraint(expr=   m.x608 <= 0)

m.c885 = Constraint(expr=   m.x609 <= 0)

m.c886 = Constraint(expr=   m.x610 <= 0)

m.c887 = Constraint(expr=   m.x611 - 6*m.b863 <= 0)

m.c888 = Constraint(expr=   m.x612 - 4*m.b864 <= 0)

m.c889 = Constraint(expr=   m.x613 - 3*m.b865 <= 0)

m.c890 = Constraint(expr=   m.x614 - 40*m.b866 <= 0)

m.c891 = Constraint(expr=   m.x615 - 35*m.b867 <= 0)

m.c892 = Constraint(expr=   m.x616 - 20*m.b868 <= 0)

m.c893 = Constraint(expr=   m.x617 - 46*m.b869 <= 0)

m.c894 = Constraint(expr=   m.x618 - 39*m.b870 <= 0)

m.c895 = Constraint(expr=   m.x619 - 23*m.b871 <= 0)

m.c896 = Constraint(expr=   m.x620 <= 0)

m.c897 = Constraint(expr=   m.x621 <= 0)

m.c898 = Constraint(expr=   m.x622 <= 0)

m.c899 = Constraint(expr=   m.x623 - 7*m.b875 <= 0)

m.c900 = Constraint(expr=   m.x624 - 4*m.b876 <= 0)

m.c901 = Constraint(expr=   m.x625 - 4*m.b877 <= 0)

m.c902 = Constraint(expr=   m.x626 - 30*m.b878 <= 0)

m.c903 = Constraint(expr=   m.x627 - 25*m.b879 <= 0)

m.c904 = Constraint(expr=   m.x628 - 20*m.b880 <= 0)

m.c905 = Constraint(expr=   m.x629 - 37*m.b881 <= 0)

m.c906 = Constraint(expr=   m.x630 - 29*m.b882 <= 0)

m.c907 = Constraint(expr=   m.x631 - 22*m.b883 <= 0)

m.c908 = Constraint(expr=   m.x632 <= 0)

m.c909 = Constraint(expr=   m.x633 <= 0)

m.c910 = Constraint(expr=   m.x634 <= 0)

m.c911 = Constraint(expr=   m.x635 - 7*m.b887 <= 0)

m.c912 = Constraint(expr=   m.x636 - 5*m.b888 <= 0)

m.c913 = Constraint(expr=   m.x637 - 3*m.b889 <= 0)

m.c914 = Constraint(expr=   m.x638 - 15*m.b890 <= 0)

m.c915 = Constraint(expr=   m.x639 - 5*m.b891 <= 0)

m.c916 = Constraint(expr=   m.x640 - 2*m.b892 <= 0)

m.c917 = Constraint(expr=   m.x641 - 22*m.b893 <= 0)

m.c918 = Constraint(expr=   m.x642 - 10*m.b894 <= 0)

m.c919 = Constraint(expr=   m.x643 - 5*m.b895 <= 0)

m.c920 = Constraint(expr=   m.x644 <= 0)

m.c921 = Constraint(expr=   m.x645 <= 0)

m.c922 = Constraint(expr=   m.x646 <= 0)

m.c923 = Constraint(expr=   m.x647 - 11*m.b899 <= 0)

m.c924 = Constraint(expr=   m.x648 - 8*m.b900 <= 0)

m.c925 = Constraint(expr=   m.x649 - 6*m.b901 <= 0)

m.c926 = Constraint(expr=   m.x650 - 13*m.b902 <= 0)

m.c927 = Constraint(expr=   m.x651 - 8*m.b903 <= 0)

m.c928 = Constraint(expr=   m.x652 - 3*m.b904 <= 0)

m.c929 = Constraint(expr=   m.x653 - 24*m.b905 <= 0)

m.c930 = Constraint(expr=   m.x654 - 16*m.b906 <= 0)

m.c931 = Constraint(expr=   m.x655 - 9*m.b907 <= 0)

m.c932 = Constraint(expr=   m.x656 <= 0)

m.c933 = Constraint(expr=   m.x657 <= 0)

m.c934 = Constraint(expr=   m.x658 <= 0)

m.c935 = Constraint(expr=   m.x659 - 10*m.b911 <= 0)

m.c936 = Constraint(expr=   m.x660 - 7*m.b912 <= 0)

m.c937 = Constraint(expr=   m.x661 - 6*m.b913 <= 0)

m.c938 = Constraint(expr=   m.x662 - 13*m.b914 <= 0)

m.c939 = Constraint(expr=   m.x663 - 8*m.b915 <= 0)

m.c940 = Constraint(expr=   m.x664 - 3*m.b916 <= 0)

m.c941 = Constraint(expr=   m.x665 - 23*m.b917 <= 0)

m.c942 = Constraint(expr=   m.x666 - 15*m.b918 <= 0)

m.c943 = Constraint(expr=   m.x667 - 9*m.b919 <= 0)

m.c944 = Constraint(expr=   m.x668 <= 0)

m.c945 = Constraint(expr=   m.x669 <= 0)

m.c946 = Constraint(expr=   m.x670 <= 0)

m.c947 = Constraint(expr=   m.x671 - 9*m.b923 <= 0)

m.c948 = Constraint(expr=   m.x672 - 9*m.b924 <= 0)

m.c949 = Constraint(expr=   m.x673 - 7*m.b925 <= 0)

m.c950 = Constraint(expr=   m.x674 - 30*m.b926 <= 0)

m.c951 = Constraint(expr=   m.x675 - 30*m.b927 <= 0)

m.c952 = Constraint(expr=   m.x676 - 25*m.b928 <= 0)

m.c953 = Constraint(expr=   m.x677 - 39*m.b929 <= 0)

m.c954 = Constraint(expr=   m.x678 - 39*m.b930 <= 0)

m.c955 = Constraint(expr=   m.x679 - 32*m.b931 <= 0)

m.c956 = Constraint(expr=   m.x680 <= 0)

m.c957 = Constraint(expr=   m.x681 <= 0)

m.c958 = Constraint(expr=   m.x682 <= 0)

m.c959 = Constraint(expr=   m.x683 - 8*m.b935 <= 0)

m.c960 = Constraint(expr=   m.x684 - 7*m.b936 <= 0)

m.c961 = Constraint(expr=   m.x685 - 7*m.b937 <= 0)

m.c962 = Constraint(expr=   m.x686 - 20*m.b938 <= 0)

m.c963 = Constraint(expr=   m.x687 - 15*m.b939 <= 0)

m.c964 = Constraint(expr=   m.x688 - 10*m.b940 <= 0)

m.c965 = Constraint(expr=   m.x689 - 28*m.b941 <= 0)

m.c966 = Constraint(expr=   m.x690 - 22*m.b942 <= 0)

m.c967 = Constraint(expr=   m.x691 - 17*m.b943 <= 0)

m.c968 = Constraint(expr=   m.x692 <= 0)

m.c969 = Constraint(expr=   m.x693 <= 0)

m.c970 = Constraint(expr=   m.x694 <= 0)

m.c971 = Constraint(expr=   m.x695 - 8*m.b947 <= 0)

m.c972 = Constraint(expr=   m.x696 - 6*m.b948 <= 0)

m.c973 = Constraint(expr=   m.x697 - 5*m.b949 <= 0)

m.c974 = Constraint(expr=   m.x698 - 15*m.b950 <= 0)

m.c975 = Constraint(expr=   m.x699 - 10*m.b951 <= 0)

m.c976 = Constraint(expr=   m.x700 - 6*m.b952 <= 0)

m.c977 = Constraint(expr=   m.x701 - 23*m.b953 <= 0)

m.c978 = Constraint(expr=   m.x702 - 16*m.b954 <= 0)

m.c979 = Constraint(expr=   m.x703 - 11*m.b955 <= 0)

m.c980 = Constraint(expr=   m.x608 == 0)

m.c981 = Constraint(expr=   m.x609 == 0)

m.c982 = Constraint(expr=   m.x610 == 0)

m.c983 = Constraint(expr=   m.x611 - 6*m.b863 == 0)

m.c984 = Constraint(expr=   m.x612 - 4*m.b864 == 0)

m.c985 = Constraint(expr=   m.x613 - 3*m.b865 == 0)

m.c986 = Constraint(expr=   m.x614 - 40*m.b866 == 0)

m.c987 = Constraint(expr=   m.x615 - 35*m.b867 == 0)

m.c988 = Constraint(expr=   m.x616 - 20*m.b868 == 0)

m.c989 = Constraint(expr=   m.x617 - 46*m.b869 == 0)

m.c990 = Constraint(expr=   m.x618 - 39*m.b870 == 0)

m.c991 = Constraint(expr=   m.x619 - 23*m.b871 == 0)

m.c992 = Constraint(expr=   m.x620 == 0)

m.c993 = Constraint(expr=   m.x621 == 0)

m.c994 = Constraint(expr=   m.x622 == 0)

m.c995 = Constraint(expr=   m.x623 - 7*m.b875 == 0)

m.c996 = Constraint(expr=   m.x624 - 4*m.b876 == 0)

m.c997 = Constraint(expr=   m.x625 - 4*m.b877 == 0)

m.c998 = Constraint(expr=   m.x626 - 30*m.b878 == 0)

m.c999 = Constraint(expr=   m.x627 - 25*m.b879 == 0)

m.c1000 = Constraint(expr=   m.x628 - 20*m.b880 == 0)

m.c1001 = Constraint(expr=   m.x629 - 37*m.b881 == 0)

m.c1002 = Constraint(expr=   m.x630 - 29*m.b882 == 0)

m.c1003 = Constraint(expr=   m.x631 - 22*m.b883 == 0)

m.c1004 = Constraint(expr=   m.x632 == 0)

m.c1005 = Constraint(expr=   m.x633 == 0)

m.c1006 = Constraint(expr=   m.x634 == 0)

m.c1007 = Constraint(expr=   m.x635 - 7*m.b887 == 0)

m.c1008 = Constraint(expr=   m.x636 - 5*m.b888 == 0)

m.c1009 = Constraint(expr=   m.x637 - 3*m.b889 == 0)

m.c1010 = Constraint(expr=   m.x638 - 15*m.b890 == 0)

m.c1011 = Constraint(expr=   m.x639 - 5*m.b891 == 0)

m.c1012 = Constraint(expr=   m.x640 - 2*m.b892 == 0)

m.c1013 = Constraint(expr=   m.x641 - 22*m.b893 == 0)

m.c1014 = Constraint(expr=   m.x642 - 10*m.b894 == 0)

m.c1015 = Constraint(expr=   m.x643 - 5*m.b895 == 0)

m.c1016 = Constraint(expr=   m.x644 == 0)

m.c1017 = Constraint(expr=   m.x645 == 0)

m.c1018 = Constraint(expr=   m.x646 == 0)

m.c1019 = Constraint(expr=   m.x647 - 11*m.b899 == 0)

m.c1020 = Constraint(expr=   m.x648 - 8*m.b900 == 0)

m.c1021 = Constraint(expr=   m.x649 - 6*m.b901 == 0)

m.c1022 = Constraint(expr=   m.x650 - 13*m.b902 == 0)

m.c1023 = Constraint(expr=   m.x651 - 8*m.b903 == 0)

m.c1024 = Constraint(expr=   m.x652 - 3*m.b904 == 0)

m.c1025 = Constraint(expr=   m.x653 - 24*m.b905 == 0)

m.c1026 = Constraint(expr=   m.x654 - 16*m.b906 == 0)

m.c1027 = Constraint(expr=   m.x655 - 9*m.b907 == 0)

m.c1028 = Constraint(expr=   m.x656 == 0)

m.c1029 = Constraint(expr=   m.x657 == 0)

m.c1030 = Constraint(expr=   m.x658 == 0)

m.c1031 = Constraint(expr=   m.x659 - 10*m.b911 == 0)

m.c1032 = Constraint(expr=   m.x660 - 7*m.b912 == 0)

m.c1033 = Constraint(expr=   m.x661 - 6*m.b913 == 0)

m.c1034 = Constraint(expr=   m.x662 - 13*m.b914 == 0)

m.c1035 = Constraint(expr=   m.x663 - 8*m.b915 == 0)

m.c1036 = Constraint(expr=   m.x664 - 3*m.b916 == 0)

m.c1037 = Constraint(expr=   m.x665 - 23*m.b917 == 0)

m.c1038 = Constraint(expr=   m.x666 - 15*m.b918 == 0)

m.c1039 = Constraint(expr=   m.x667 - 9*m.b919 == 0)

m.c1040 = Constraint(expr=   m.x668 == 0)

m.c1041 = Constraint(expr=   m.x669 == 0)

m.c1042 = Constraint(expr=   m.x670 == 0)

m.c1043 = Constraint(expr=   m.x671 - 9*m.b923 == 0)

m.c1044 = Constraint(expr=   m.x672 - 9*m.b924 == 0)

m.c1045 = Constraint(expr=   m.x673 - 7*m.b925 == 0)

m.c1046 = Constraint(expr=   m.x674 - 30*m.b926 == 0)

m.c1047 = Constraint(expr=   m.x675 - 30*m.b927 == 0)

m.c1048 = Constraint(expr=   m.x676 - 25*m.b928 == 0)

m.c1049 = Constraint(expr=   m.x677 - 39*m.b929 == 0)

m.c1050 = Constraint(expr=   m.x678 - 39*m.b930 == 0)

m.c1051 = Constraint(expr=   m.x679 - 32*m.b931 == 0)

m.c1052 = Constraint(expr=   m.x680 == 0)

m.c1053 = Constraint(expr=   m.x681 == 0)

m.c1054 = Constraint(expr=   m.x682 == 0)

m.c1055 = Constraint(expr=   m.x683 - 8*m.b935 == 0)

m.c1056 = Constraint(expr=   m.x684 - 7*m.b936 == 0)

m.c1057 = Constraint(expr=   m.x685 - 7*m.b937 == 0)

m.c1058 = Constraint(expr=   m.x686 - 20*m.b938 == 0)

m.c1059 = Constraint(expr=   m.x687 - 15*m.b939 == 0)

m.c1060 = Constraint(expr=   m.x688 - 10*m.b940 == 0)

m.c1061 = Constraint(expr=   m.x689 - 28*m.b941 == 0)

m.c1062 = Constraint(expr=   m.x690 - 22*m.b942 == 0)

m.c1063 = Constraint(expr=   m.x691 - 17*m.b943 == 0)

m.c1064 = Constraint(expr=   m.x692 == 0)

m.c1065 = Constraint(expr=   m.x693 == 0)

m.c1066 = Constraint(expr=   m.x694 == 0)

m.c1067 = Constraint(expr=   m.x695 - 8*m.b947 == 0)

m.c1068 = Constraint(expr=   m.x696 - 6*m.b948 == 0)

m.c1069 = Constraint(expr=   m.x697 - 5*m.b949 == 0)

m.c1070 = Constraint(expr=   m.x698 - 15*m.b950 == 0)

m.c1071 = Constraint(expr=   m.x699 - 10*m.b951 == 0)

m.c1072 = Constraint(expr=   m.x700 - 6*m.b952 == 0)

m.c1073 = Constraint(expr=   m.x701 - 23*m.b953 == 0)

m.c1074 = Constraint(expr=   m.x702 - 16*m.b954 == 0)

m.c1075 = Constraint(expr=   m.x703 - 11*m.b955 == 0)

m.c1076 = Constraint(expr=   20*m.x2 + 20*m.x17 + 18*m.x29 + 16*m.x65 + 20*m.x86 + m.x236 + m.x239 + m.x242 + m.x245
                           + m.x248 + m.x251 + m.x254 + m.x257 <= 4000)

m.c1077 = Constraint(expr=   17*m.x3 + 21*m.x18 + 20*m.x30 + 19*m.x66 + 18*m.x87 + m.x237 + m.x240 + m.x243 + m.x246
                           + m.x249 + m.x252 + m.x255 + m.x258 <= 3800)

m.c1078 = Constraint(expr=   15*m.x4 + 19*m.x19 + 20*m.x31 + 17*m.x67 + 21*m.x88 + m.x238 + m.x241 + m.x244 + m.x247
                           + m.x250 + m.x253 + m.x256 + m.x259 <= 3600)

m.c1079 = Constraint(expr=   m.b764 + m.b767 + m.b770 + m.b773 == 1)

m.c1080 = Constraint(expr=   m.b765 + m.b768 + m.b771 + m.b774 == 1)

m.c1081 = Constraint(expr=   m.b766 + m.b769 + m.b772 + m.b775 == 1)

m.c1082 = Constraint(expr=   m.b776 + m.b779 + m.b782 + m.b785 == 1)

m.c1083 = Constraint(expr=   m.b777 + m.b780 + m.b783 + m.b786 == 1)

m.c1084 = Constraint(expr=   m.b778 + m.b781 + m.b784 + m.b787 == 1)

m.c1085 = Constraint(expr=   m.b788 + m.b791 + m.b794 + m.b797 == 1)

m.c1086 = Constraint(expr=   m.b789 + m.b792 + m.b795 + m.b798 == 1)

m.c1087 = Constraint(expr=   m.b790 + m.b793 + m.b796 + m.b799 == 1)

m.c1088 = Constraint(expr=   m.b800 + m.b803 + m.b806 + m.b809 == 1)

m.c1089 = Constraint(expr=   m.b801 + m.b804 + m.b807 + m.b810 == 1)

m.c1090 = Constraint(expr=   m.b802 + m.b805 + m.b808 + m.b811 == 1)

m.c1091 = Constraint(expr=   m.b812 + m.b815 + m.b818 + m.b821 == 1)

m.c1092 = Constraint(expr=   m.b813 + m.b816 + m.b819 + m.b822 == 1)

m.c1093 = Constraint(expr=   m.b814 + m.b817 + m.b820 + m.b823 == 1)

m.c1094 = Constraint(expr=   m.b824 + m.b827 + m.b830 + m.b833 == 1)

m.c1095 = Constraint(expr=   m.b825 + m.b828 + m.b831 + m.b834 == 1)

m.c1096 = Constraint(expr=   m.b826 + m.b829 + m.b832 + m.b835 == 1)

m.c1097 = Constraint(expr=   m.b836 + m.b839 + m.b842 + m.b845 == 1)

m.c1098 = Constraint(expr=   m.b837 + m.b840 + m.b843 + m.b846 == 1)

m.c1099 = Constraint(expr=   m.b838 + m.b841 + m.b844 + m.b847 == 1)

m.c1100 = Constraint(expr=   m.b848 + m.b851 + m.b854 + m.b857 == 1)

m.c1101 = Constraint(expr=   m.b849 + m.b852 + m.b855 + m.b858 == 1)

m.c1102 = Constraint(expr=   m.b850 + m.b853 + m.b856 + m.b859 == 1)

m.c1103 = Constraint(expr=   m.b860 + m.b863 + m.b866 + m.b869 == 1)

m.c1104 = Constraint(expr=   m.b861 + m.b864 + m.b867 + m.b870 == 1)

m.c1105 = Constraint(expr=   m.b862 + m.b865 + m.b868 + m.b871 == 1)

m.c1106 = Constraint(expr=   m.b872 + m.b875 + m.b878 + m.b881 == 1)

m.c1107 = Constraint(expr=   m.b873 + m.b876 + m.b879 + m.b882 == 1)

m.c1108 = Constraint(expr=   m.b874 + m.b877 + m.b880 + m.b883 == 1)

m.c1109 = Constraint(expr=   m.b884 + m.b887 + m.b890 + m.b893 == 1)

m.c1110 = Constraint(expr=   m.b885 + m.b888 + m.b891 + m.b894 == 1)

m.c1111 = Constraint(expr=   m.b886 + m.b889 + m.b892 + m.b895 == 1)

m.c1112 = Constraint(expr=   m.b896 + m.b899 + m.b902 + m.b905 == 1)

m.c1113 = Constraint(expr=   m.b897 + m.b900 + m.b903 + m.b906 == 1)

m.c1114 = Constraint(expr=   m.b898 + m.b901 + m.b904 + m.b907 == 1)

m.c1115 = Constraint(expr=   m.b908 + m.b911 + m.b914 + m.b917 == 1)

m.c1116 = Constraint(expr=   m.b909 + m.b912 + m.b915 + m.b918 == 1)

m.c1117 = Constraint(expr=   m.b910 + m.b913 + m.b916 + m.b919 == 1)

m.c1118 = Constraint(expr=   m.b920 + m.b923 + m.b926 + m.b929 == 1)

m.c1119 = Constraint(expr=   m.b921 + m.b924 + m.b927 + m.b930 == 1)

m.c1120 = Constraint(expr=   m.b922 + m.b925 + m.b928 + m.b931 == 1)

m.c1121 = Constraint(expr=   m.b932 + m.b935 + m.b938 + m.b941 == 1)

m.c1122 = Constraint(expr=   m.b933 + m.b936 + m.b939 + m.b942 == 1)

m.c1123 = Constraint(expr=   m.b934 + m.b937 + m.b940 + m.b943 == 1)

m.c1124 = Constraint(expr=   m.b944 + m.b947 + m.b950 + m.b953 == 1)

m.c1125 = Constraint(expr=   m.b945 + m.b948 + m.b951 + m.b954 == 1)

m.c1126 = Constraint(expr=   m.b946 + m.b949 + m.b952 + m.b955 == 1)

m.c1127 = Constraint(expr=   m.b767 - m.b768 <= 0)

m.c1128 = Constraint(expr=   m.b767 - m.b769 <= 0)

m.c1129 = Constraint(expr=   m.b768 - m.b769 <= 0)

m.c1130 = Constraint(expr=   m.b770 - m.b771 <= 0)

m.c1131 = Constraint(expr=   m.b770 - m.b772 <= 0)

m.c1132 = Constraint(expr=   m.b771 - m.b772 <= 0)

m.c1133 = Constraint(expr=   m.b773 - m.b774 <= 0)

m.c1134 = Constraint(expr=   m.b773 - m.b775 <= 0)

m.c1135 = Constraint(expr=   m.b774 - m.b775 <= 0)

m.c1136 = Constraint(expr=   m.b779 - m.b780 <= 0)

m.c1137 = Constraint(expr=   m.b779 - m.b781 <= 0)

m.c1138 = Constraint(expr=   m.b780 - m.b781 <= 0)

m.c1139 = Constraint(expr=   m.b782 - m.b783 <= 0)

m.c1140 = Constraint(expr=   m.b782 - m.b784 <= 0)

m.c1141 = Constraint(expr=   m.b783 - m.b784 <= 0)

m.c1142 = Constraint(expr=   m.b785 - m.b786 <= 0)

m.c1143 = Constraint(expr=   m.b785 - m.b787 <= 0)

m.c1144 = Constraint(expr=   m.b786 - m.b787 <= 0)

m.c1145 = Constraint(expr=   m.b791 - m.b792 <= 0)

m.c1146 = Constraint(expr=   m.b791 - m.b793 <= 0)

m.c1147 = Constraint(expr=   m.b792 - m.b793 <= 0)

m.c1148 = Constraint(expr=   m.b794 - m.b795 <= 0)

m.c1149 = Constraint(expr=   m.b794 - m.b796 <= 0)

m.c1150 = Constraint(expr=   m.b795 - m.b796 <= 0)

m.c1151 = Constraint(expr=   m.b797 - m.b798 <= 0)

m.c1152 = Constraint(expr=   m.b797 - m.b799 <= 0)

m.c1153 = Constraint(expr=   m.b798 - m.b799 <= 0)

m.c1154 = Constraint(expr=   m.b803 - m.b804 <= 0)

m.c1155 = Constraint(expr=   m.b803 - m.b805 <= 0)

m.c1156 = Constraint(expr=   m.b804 - m.b805 <= 0)

m.c1157 = Constraint(expr=   m.b806 - m.b807 <= 0)

m.c1158 = Constraint(expr=   m.b806 - m.b808 <= 0)

m.c1159 = Constraint(expr=   m.b807 - m.b808 <= 0)

m.c1160 = Constraint(expr=   m.b809 - m.b810 <= 0)

m.c1161 = Constraint(expr=   m.b809 - m.b811 <= 0)

m.c1162 = Constraint(expr=   m.b810 - m.b811 <= 0)

m.c1163 = Constraint(expr=   m.b815 - m.b816 <= 0)

m.c1164 = Constraint(expr=   m.b815 - m.b817 <= 0)

m.c1165 = Constraint(expr=   m.b816 - m.b817 <= 0)

m.c1166 = Constraint(expr=   m.b818 - m.b819 <= 0)

m.c1167 = Constraint(expr=   m.b818 - m.b820 <= 0)

m.c1168 = Constraint(expr=   m.b819 - m.b820 <= 0)

m.c1169 = Constraint(expr=   m.b821 - m.b822 <= 0)

m.c1170 = Constraint(expr=   m.b821 - m.b823 <= 0)

m.c1171 = Constraint(expr=   m.b822 - m.b823 <= 0)

m.c1172 = Constraint(expr=   m.b827 - m.b828 <= 0)

m.c1173 = Constraint(expr=   m.b827 - m.b829 <= 0)

m.c1174 = Constraint(expr=   m.b828 - m.b829 <= 0)

m.c1175 = Constraint(expr=   m.b830 - m.b831 <= 0)

m.c1176 = Constraint(expr=   m.b830 - m.b832 <= 0)

m.c1177 = Constraint(expr=   m.b831 - m.b832 <= 0)

m.c1178 = Constraint(expr=   m.b833 - m.b834 <= 0)

m.c1179 = Constraint(expr=   m.b833 - m.b835 <= 0)

m.c1180 = Constraint(expr=   m.b834 - m.b835 <= 0)

m.c1181 = Constraint(expr=   m.b839 - m.b840 <= 0)

m.c1182 = Constraint(expr=   m.b839 - m.b841 <= 0)

m.c1183 = Constraint(expr=   m.b840 - m.b841 <= 0)

m.c1184 = Constraint(expr=   m.b842 - m.b843 <= 0)

m.c1185 = Constraint(expr=   m.b842 - m.b844 <= 0)

m.c1186 = Constraint(expr=   m.b843 - m.b844 <= 0)

m.c1187 = Constraint(expr=   m.b845 - m.b846 <= 0)

m.c1188 = Constraint(expr=   m.b845 - m.b847 <= 0)

m.c1189 = Constraint(expr=   m.b846 - m.b847 <= 0)

m.c1190 = Constraint(expr=   m.b851 - m.b852 <= 0)

m.c1191 = Constraint(expr=   m.b851 - m.b853 <= 0)

m.c1192 = Constraint(expr=   m.b852 - m.b853 <= 0)

m.c1193 = Constraint(expr=   m.b854 - m.b855 <= 0)

m.c1194 = Constraint(expr=   m.b854 - m.b856 <= 0)

m.c1195 = Constraint(expr=   m.b855 - m.b856 <= 0)

m.c1196 = Constraint(expr=   m.b857 - m.b858 <= 0)

m.c1197 = Constraint(expr=   m.b857 - m.b859 <= 0)

m.c1198 = Constraint(expr=   m.b858 - m.b859 <= 0)

m.c1199 = Constraint(expr= - m.b861 + m.b863 <= 0)

m.c1200 = Constraint(expr= - m.b862 + m.b863 <= 0)

m.c1201 = Constraint(expr= - m.b860 + m.b864 <= 0)

m.c1202 = Constraint(expr= - m.b862 + m.b864 <= 0)

m.c1203 = Constraint(expr= - m.b860 + m.b865 <= 0)

m.c1204 = Constraint(expr= - m.b861 + m.b865 <= 0)

m.c1205 = Constraint(expr= - m.b861 + m.b866 <= 0)

m.c1206 = Constraint(expr= - m.b862 + m.b866 <= 0)

m.c1207 = Constraint(expr= - m.b860 + m.b867 <= 0)

m.c1208 = Constraint(expr= - m.b862 + m.b867 <= 0)

m.c1209 = Constraint(expr= - m.b860 + m.b868 <= 0)

m.c1210 = Constraint(expr= - m.b861 + m.b868 <= 0)

m.c1211 = Constraint(expr= - m.b861 + m.b869 <= 0)

m.c1212 = Constraint(expr= - m.b862 + m.b869 <= 0)

m.c1213 = Constraint(expr= - m.b860 + m.b870 <= 0)

m.c1214 = Constraint(expr= - m.b862 + m.b870 <= 0)

m.c1215 = Constraint(expr= - m.b860 + m.b871 <= 0)

m.c1216 = Constraint(expr= - m.b861 + m.b871 <= 0)

m.c1217 = Constraint(expr= - m.b873 + m.b875 <= 0)

m.c1218 = Constraint(expr= - m.b874 + m.b875 <= 0)

m.c1219 = Constraint(expr= - m.b872 + m.b876 <= 0)

m.c1220 = Constraint(expr= - m.b874 + m.b876 <= 0)

m.c1221 = Constraint(expr= - m.b872 + m.b877 <= 0)

m.c1222 = Constraint(expr= - m.b873 + m.b877 <= 0)

m.c1223 = Constraint(expr= - m.b873 + m.b878 <= 0)

m.c1224 = Constraint(expr= - m.b874 + m.b878 <= 0)

m.c1225 = Constraint(expr= - m.b872 + m.b879 <= 0)

m.c1226 = Constraint(expr= - m.b874 + m.b879 <= 0)

m.c1227 = Constraint(expr= - m.b872 + m.b880 <= 0)

m.c1228 = Constraint(expr= - m.b873 + m.b880 <= 0)

m.c1229 = Constraint(expr= - m.b873 + m.b881 <= 0)

m.c1230 = Constraint(expr= - m.b874 + m.b881 <= 0)

m.c1231 = Constraint(expr= - m.b872 + m.b882 <= 0)

m.c1232 = Constraint(expr= - m.b874 + m.b882 <= 0)

m.c1233 = Constraint(expr= - m.b872 + m.b883 <= 0)

m.c1234 = Constraint(expr= - m.b873 + m.b883 <= 0)

m.c1235 = Constraint(expr= - m.b885 + m.b887 <= 0)

m.c1236 = Constraint(expr= - m.b886 + m.b887 <= 0)

m.c1237 = Constraint(expr= - m.b884 + m.b888 <= 0)

m.c1238 = Constraint(expr= - m.b886 + m.b888 <= 0)

m.c1239 = Constraint(expr= - m.b884 + m.b889 <= 0)

m.c1240 = Constraint(expr= - m.b885 + m.b889 <= 0)

m.c1241 = Constraint(expr= - m.b885 + m.b890 <= 0)

m.c1242 = Constraint(expr= - m.b886 + m.b890 <= 0)

m.c1243 = Constraint(expr= - m.b884 + m.b891 <= 0)

m.c1244 = Constraint(expr= - m.b886 + m.b891 <= 0)

m.c1245 = Constraint(expr= - m.b884 + m.b892 <= 0)

m.c1246 = Constraint(expr= - m.b885 + m.b892 <= 0)

m.c1247 = Constraint(expr= - m.b885 + m.b893 <= 0)

m.c1248 = Constraint(expr= - m.b886 + m.b893 <= 0)

m.c1249 = Constraint(expr= - m.b884 + m.b894 <= 0)

m.c1250 = Constraint(expr= - m.b886 + m.b894 <= 0)

m.c1251 = Constraint(expr= - m.b884 + m.b895 <= 0)

m.c1252 = Constraint(expr= - m.b885 + m.b895 <= 0)

m.c1253 = Constraint(expr= - m.b897 + m.b899 <= 0)

m.c1254 = Constraint(expr= - m.b898 + m.b899 <= 0)

m.c1255 = Constraint(expr= - m.b896 + m.b900 <= 0)

m.c1256 = Constraint(expr= - m.b898 + m.b900 <= 0)

m.c1257 = Constraint(expr= - m.b896 + m.b901 <= 0)

m.c1258 = Constraint(expr= - m.b897 + m.b901 <= 0)

m.c1259 = Constraint(expr= - m.b897 + m.b902 <= 0)

m.c1260 = Constraint(expr= - m.b898 + m.b902 <= 0)

m.c1261 = Constraint(expr= - m.b896 + m.b903 <= 0)

m.c1262 = Constraint(expr= - m.b898 + m.b903 <= 0)

m.c1263 = Constraint(expr= - m.b896 + m.b904 <= 0)

m.c1264 = Constraint(expr= - m.b897 + m.b904 <= 0)

m.c1265 = Constraint(expr= - m.b897 + m.b905 <= 0)

m.c1266 = Constraint(expr= - m.b898 + m.b905 <= 0)

m.c1267 = Constraint(expr= - m.b896 + m.b906 <= 0)

m.c1268 = Constraint(expr= - m.b898 + m.b906 <= 0)

m.c1269 = Constraint(expr= - m.b896 + m.b907 <= 0)

m.c1270 = Constraint(expr= - m.b897 + m.b907 <= 0)

m.c1271 = Constraint(expr= - m.b909 + m.b911 <= 0)

m.c1272 = Constraint(expr= - m.b910 + m.b911 <= 0)

m.c1273 = Constraint(expr= - m.b908 + m.b912 <= 0)

m.c1274 = Constraint(expr= - m.b910 + m.b912 <= 0)

m.c1275 = Constraint(expr= - m.b908 + m.b913 <= 0)

m.c1276 = Constraint(expr= - m.b909 + m.b913 <= 0)

m.c1277 = Constraint(expr= - m.b909 + m.b914 <= 0)

m.c1278 = Constraint(expr= - m.b910 + m.b914 <= 0)

m.c1279 = Constraint(expr= - m.b908 + m.b915 <= 0)

m.c1280 = Constraint(expr= - m.b910 + m.b915 <= 0)

m.c1281 = Constraint(expr= - m.b908 + m.b916 <= 0)

m.c1282 = Constraint(expr= - m.b909 + m.b916 <= 0)

m.c1283 = Constraint(expr= - m.b909 + m.b917 <= 0)

m.c1284 = Constraint(expr= - m.b910 + m.b917 <= 0)

m.c1285 = Constraint(expr= - m.b908 + m.b918 <= 0)

m.c1286 = Constraint(expr= - m.b910 + m.b918 <= 0)

m.c1287 = Constraint(expr= - m.b908 + m.b919 <= 0)

m.c1288 = Constraint(expr= - m.b909 + m.b919 <= 0)

m.c1289 = Constraint(expr= - m.b921 + m.b923 <= 0)

m.c1290 = Constraint(expr= - m.b922 + m.b923 <= 0)

m.c1291 = Constraint(expr= - m.b920 + m.b924 <= 0)

m.c1292 = Constraint(expr= - m.b922 + m.b924 <= 0)

m.c1293 = Constraint(expr= - m.b920 + m.b925 <= 0)

m.c1294 = Constraint(expr= - m.b921 + m.b925 <= 0)

m.c1295 = Constraint(expr= - m.b921 + m.b926 <= 0)

m.c1296 = Constraint(expr= - m.b922 + m.b926 <= 0)

m.c1297 = Constraint(expr= - m.b920 + m.b927 <= 0)

m.c1298 = Constraint(expr= - m.b922 + m.b927 <= 0)

m.c1299 = Constraint(expr= - m.b920 + m.b928 <= 0)

m.c1300 = Constraint(expr= - m.b921 + m.b928 <= 0)

m.c1301 = Constraint(expr= - m.b921 + m.b929 <= 0)

m.c1302 = Constraint(expr= - m.b922 + m.b929 <= 0)

m.c1303 = Constraint(expr= - m.b920 + m.b930 <= 0)

m.c1304 = Constraint(expr= - m.b922 + m.b930 <= 0)

m.c1305 = Constraint(expr= - m.b920 + m.b931 <= 0)

m.c1306 = Constraint(expr= - m.b921 + m.b931 <= 0)

m.c1307 = Constraint(expr= - m.b933 + m.b935 <= 0)

m.c1308 = Constraint(expr= - m.b934 + m.b935 <= 0)

m.c1309 = Constraint(expr= - m.b932 + m.b936 <= 0)

m.c1310 = Constraint(expr= - m.b934 + m.b936 <= 0)

m.c1311 = Constraint(expr= - m.b932 + m.b937 <= 0)

m.c1312 = Constraint(expr= - m.b933 + m.b937 <= 0)

m.c1313 = Constraint(expr= - m.b933 + m.b938 <= 0)

m.c1314 = Constraint(expr= - m.b934 + m.b938 <= 0)

m.c1315 = Constraint(expr= - m.b932 + m.b939 <= 0)

m.c1316 = Constraint(expr= - m.b934 + m.b939 <= 0)

m.c1317 = Constraint(expr= - m.b932 + m.b940 <= 0)

m.c1318 = Constraint(expr= - m.b933 + m.b940 <= 0)

m.c1319 = Constraint(expr= - m.b933 + m.b941 <= 0)

m.c1320 = Constraint(expr= - m.b934 + m.b941 <= 0)

m.c1321 = Constraint(expr= - m.b932 + m.b942 <= 0)

m.c1322 = Constraint(expr= - m.b934 + m.b942 <= 0)

m.c1323 = Constraint(expr= - m.b932 + m.b943 <= 0)

m.c1324 = Constraint(expr= - m.b933 + m.b943 <= 0)

m.c1325 = Constraint(expr= - m.b945 + m.b947 <= 0)

m.c1326 = Constraint(expr= - m.b946 + m.b947 <= 0)

m.c1327 = Constraint(expr= - m.b944 + m.b948 <= 0)

m.c1328 = Constraint(expr= - m.b946 + m.b948 <= 0)

m.c1329 = Constraint(expr= - m.b944 + m.b949 <= 0)

m.c1330 = Constraint(expr= - m.b945 + m.b949 <= 0)

m.c1331 = Constraint(expr= - m.b945 + m.b950 <= 0)

m.c1332 = Constraint(expr= - m.b946 + m.b950 <= 0)

m.c1333 = Constraint(expr= - m.b944 + m.b951 <= 0)

m.c1334 = Constraint(expr= - m.b946 + m.b951 <= 0)

m.c1335 = Constraint(expr= - m.b944 + m.b952 <= 0)

m.c1336 = Constraint(expr= - m.b945 + m.b952 <= 0)

m.c1337 = Constraint(expr= - m.b945 + m.b953 <= 0)

m.c1338 = Constraint(expr= - m.b946 + m.b953 <= 0)

m.c1339 = Constraint(expr= - m.b944 + m.b954 <= 0)

m.c1340 = Constraint(expr= - m.b946 + m.b954 <= 0)

m.c1341 = Constraint(expr= - m.b944 + m.b955 <= 0)

m.c1342 = Constraint(expr= - m.b945 + m.b955 <= 0)

m.c1343 = Constraint(expr=   m.b764 - m.b860 <= 0)

m.c1344 = Constraint(expr=   m.b765 - m.b861 <= 0)

m.c1345 = Constraint(expr=   m.b766 - m.b862 <= 0)

m.c1346 = Constraint(expr=   m.b776 - m.b872 <= 0)

m.c1347 = Constraint(expr=   m.b777 - m.b873 <= 0)

m.c1348 = Constraint(expr=   m.b778 - m.b874 <= 0)

m.c1349 = Constraint(expr=   m.b788 - m.b884 <= 0)

m.c1350 = Constraint(expr=   m.b789 - m.b885 <= 0)

m.c1351 = Constraint(expr=   m.b790 - m.b886 <= 0)

m.c1352 = Constraint(expr=   m.b800 - m.b896 <= 0)

m.c1353 = Constraint(expr=   m.b801 - m.b897 <= 0)

m.c1354 = Constraint(expr=   m.b802 - m.b898 <= 0)

m.c1355 = Constraint(expr=   m.b812 - m.b908 <= 0)

m.c1356 = Constraint(expr=   m.b813 - m.b909 <= 0)

m.c1357 = Constraint(expr=   m.b814 - m.b910 <= 0)

m.c1358 = Constraint(expr=   m.b824 - m.b920 <= 0)

m.c1359 = Constraint(expr=   m.b825 - m.b921 <= 0)

m.c1360 = Constraint(expr=   m.b826 - m.b922 <= 0)

m.c1361 = Constraint(expr=   m.b836 - m.b932 <= 0)

m.c1362 = Constraint(expr=   m.b837 - m.b933 <= 0)

m.c1363 = Constraint(expr=   m.b838 - m.b934 <= 0)

m.c1364 = Constraint(expr=   m.b848 - m.b944 <= 0)

m.c1365 = Constraint(expr=   m.b849 - m.b945 <= 0)

m.c1366 = Constraint(expr=   m.b850 - m.b946 <= 0)

m.c1367 = Constraint(expr=   m.b767 - m.b863 <= 0)

m.c1368 = Constraint(expr= - m.b767 + m.b768 - m.b864 <= 0)

m.c1369 = Constraint(expr= - m.b767 - m.b768 + m.b769 - m.b865 <= 0)

m.c1370 = Constraint(expr=   m.b770 - m.b866 <= 0)

m.c1371 = Constraint(expr= - m.b770 + m.b771 - m.b867 <= 0)

m.c1372 = Constraint(expr= - m.b770 - m.b771 + m.b772 - m.b868 <= 0)

m.c1373 = Constraint(expr=   m.b773 - m.b869 <= 0)

m.c1374 = Constraint(expr= - m.b773 + m.b774 - m.b870 <= 0)

m.c1375 = Constraint(expr= - m.b773 - m.b774 + m.b775 - m.b871 <= 0)

m.c1376 = Constraint(expr=   m.b779 - m.b875 <= 0)

m.c1377 = Constraint(expr= - m.b779 + m.b780 - m.b876 <= 0)

m.c1378 = Constraint(expr= - m.b779 - m.b780 + m.b781 - m.b877 <= 0)

m.c1379 = Constraint(expr=   m.b782 - m.b878 <= 0)

m.c1380 = Constraint(expr= - m.b782 + m.b783 - m.b879 <= 0)

m.c1381 = Constraint(expr= - m.b782 - m.b783 + m.b784 - m.b880 <= 0)

m.c1382 = Constraint(expr=   m.b785 - m.b881 <= 0)

m.c1383 = Constraint(expr= - m.b785 + m.b786 - m.b882 <= 0)

m.c1384 = Constraint(expr= - m.b785 - m.b786 + m.b787 - m.b883 <= 0)

m.c1385 = Constraint(expr=   m.b791 - m.b887 <= 0)

m.c1386 = Constraint(expr= - m.b791 + m.b792 - m.b888 <= 0)

m.c1387 = Constraint(expr= - m.b791 - m.b792 + m.b793 - m.b889 <= 0)

m.c1388 = Constraint(expr=   m.b794 - m.b890 <= 0)

m.c1389 = Constraint(expr= - m.b794 + m.b795 - m.b891 <= 0)

m.c1390 = Constraint(expr= - m.b794 - m.b795 + m.b796 - m.b892 <= 0)

m.c1391 = Constraint(expr=   m.b797 - m.b893 <= 0)

m.c1392 = Constraint(expr= - m.b797 + m.b798 - m.b894 <= 0)

m.c1393 = Constraint(expr= - m.b797 - m.b798 + m.b799 - m.b895 <= 0)

m.c1394 = Constraint(expr=   m.b803 - m.b899 <= 0)

m.c1395 = Constraint(expr= - m.b803 + m.b804 - m.b900 <= 0)

m.c1396 = Constraint(expr= - m.b803 - m.b804 + m.b805 - m.b901 <= 0)

m.c1397 = Constraint(expr=   m.b806 - m.b902 <= 0)

m.c1398 = Constraint(expr= - m.b806 + m.b807 - m.b903 <= 0)

m.c1399 = Constraint(expr= - m.b806 - m.b807 + m.b808 - m.b904 <= 0)

m.c1400 = Constraint(expr=   m.b809 - m.b905 <= 0)

m.c1401 = Constraint(expr= - m.b809 + m.b810 - m.b906 <= 0)

m.c1402 = Constraint(expr= - m.b809 - m.b810 + m.b811 - m.b907 <= 0)

m.c1403 = Constraint(expr=   m.b815 - m.b911 <= 0)

m.c1404 = Constraint(expr= - m.b815 + m.b816 - m.b912 <= 0)

m.c1405 = Constraint(expr= - m.b815 - m.b816 + m.b817 - m.b913 <= 0)

m.c1406 = Constraint(expr=   m.b818 - m.b914 <= 0)

m.c1407 = Constraint(expr= - m.b818 + m.b819 - m.b915 <= 0)

m.c1408 = Constraint(expr= - m.b818 - m.b819 + m.b820 - m.b916 <= 0)

m.c1409 = Constraint(expr=   m.b821 - m.b917 <= 0)

m.c1410 = Constraint(expr= - m.b821 + m.b822 - m.b918 <= 0)

m.c1411 = Constraint(expr= - m.b821 - m.b822 + m.b823 - m.b919 <= 0)

m.c1412 = Constraint(expr=   m.b827 - m.b923 <= 0)

m.c1413 = Constraint(expr= - m.b827 + m.b828 - m.b924 <= 0)

m.c1414 = Constraint(expr= - m.b827 - m.b828 + m.b829 - m.b925 <= 0)

m.c1415 = Constraint(expr=   m.b830 - m.b926 <= 0)

m.c1416 = Constraint(expr= - m.b830 + m.b831 - m.b927 <= 0)

m.c1417 = Constraint(expr= - m.b830 - m.b831 + m.b832 - m.b928 <= 0)

m.c1418 = Constraint(expr=   m.b833 - m.b929 <= 0)

m.c1419 = Constraint(expr= - m.b833 + m.b834 - m.b930 <= 0)

m.c1420 = Constraint(expr= - m.b833 - m.b834 + m.b835 - m.b931 <= 0)

m.c1421 = Constraint(expr=   m.b839 - m.b935 <= 0)

m.c1422 = Constraint(expr= - m.b839 + m.b840 - m.b936 <= 0)

m.c1423 = Constraint(expr= - m.b839 - m.b840 + m.b841 - m.b937 <= 0)

m.c1424 = Constraint(expr=   m.b842 - m.b938 <= 0)

m.c1425 = Constraint(expr= - m.b842 + m.b843 - m.b939 <= 0)

m.c1426 = Constraint(expr= - m.b842 - m.b843 + m.b844 - m.b940 <= 0)

m.c1427 = Constraint(expr=   m.b845 - m.b941 <= 0)

m.c1428 = Constraint(expr= - m.b845 + m.b846 - m.b942 <= 0)

m.c1429 = Constraint(expr= - m.b845 - m.b846 + m.b847 - m.b943 <= 0)

m.c1430 = Constraint(expr=   m.b851 - m.b947 <= 0)

m.c1431 = Constraint(expr= - m.b851 + m.b852 - m.b948 <= 0)

m.c1432 = Constraint(expr= - m.b851 - m.b852 + m.b853 - m.b949 <= 0)

m.c1433 = Constraint(expr=   m.b854 - m.b950 <= 0)

m.c1434 = Constraint(expr= - m.b854 + m.b855 - m.b951 <= 0)

m.c1435 = Constraint(expr= - m.b854 - m.b855 + m.b856 - m.b952 <= 0)

m.c1436 = Constraint(expr=   m.b857 - m.b953 <= 0)

m.c1437 = Constraint(expr= - m.b857 + m.b858 - m.b954 <= 0)

m.c1438 = Constraint(expr= - m.b857 - m.b858 + m.b859 - m.b955 <= 0)

m.c1439 = Constraint(expr=   m.x14 - m.x95 - m.x956 == 0)

m.c1440 = Constraint(expr=   m.x15 - m.x96 - m.x957 == 0)

m.c1441 = Constraint(expr=   m.x16 - m.x97 - m.x958 == 0)

m.c1442 = Constraint(expr=   m.x26 - m.x98 - m.x989 == 0)

m.c1443 = Constraint(expr=   m.x27 - m.x99 - m.x990 == 0)

m.c1444 = Constraint(expr=   m.x28 - m.x100 - m.x991 == 0)

m.c1445 = Constraint(expr=   m.x59 - m.x101 - m.x1040 == 0)

m.c1446 = Constraint(expr=   m.x60 - m.x102 - m.x1041 == 0)

m.c1447 = Constraint(expr=   m.x61 - m.x103 - m.x1042 == 0)

m.c1448 = Constraint(expr=   m.x62 - m.x104 - m.x1043 == 0)

m.c1449 = Constraint(expr=   m.x63 - m.x105 - m.x1044 == 0)

m.c1450 = Constraint(expr=   m.x64 - m.x106 - m.x1045 == 0)

m.c1451 = Constraint(expr=   m.x956 - m.x959 - m.x962 == 0)

m.c1452 = Constraint(expr=   m.x957 - m.x960 - m.x963 == 0)

m.c1453 = Constraint(expr=   m.x958 - m.x961 - m.x964 == 0)

m.c1454 = Constraint(expr= - m.x965 - m.x968 + m.x971 == 0)

m.c1455 = Constraint(expr= - m.x966 - m.x969 + m.x972 == 0)

m.c1456 = Constraint(expr= - m.x967 - m.x970 + m.x973 == 0)

m.c1457 = Constraint(expr=   m.x971 - m.x974 - m.x977 == 0)

m.c1458 = Constraint(expr=   m.x972 - m.x975 - m.x978 == 0)

m.c1459 = Constraint(expr=   m.x973 - m.x976 - m.x979 == 0)

m.c1460 = Constraint(expr=   m.x977 - m.x980 - m.x983 - m.x986 == 0)

m.c1461 = Constraint(expr=   m.x978 - m.x981 - m.x984 - m.x987 == 0)

m.c1462 = Constraint(expr=   m.x979 - m.x982 - m.x985 - m.x988 == 0)

m.c1463 = Constraint(expr=   m.x992 - m.x1001 - m.x1004 == 0)

m.c1464 = Constraint(expr=   m.x993 - m.x1002 - m.x1005 == 0)

m.c1465 = Constraint(expr=   m.x994 - m.x1003 - m.x1006 == 0)

m.c1466 = Constraint(expr=   m.x998 - m.x1007 - m.x1010 - m.x1013 == 0)

m.c1467 = Constraint(expr=   m.x999 - m.x1008 - m.x1011 - m.x1014 == 0)

m.c1468 = Constraint(expr=   m.x1000 - m.x1009 - m.x1012 - m.x1015 == 0)

m.c1469 = Constraint(expr=   m.x1022 - m.x1034 - m.x1037 == 0)

m.c1470 = Constraint(expr=   m.x1023 - m.x1035 - m.x1038 == 0)

m.c1471 = Constraint(expr=   m.x1024 - m.x1036 - m.x1039 == 0)

m.c1472 = Constraint(expr= - m.x1025 - m.x1043 + m.x1046 == 0)

m.c1473 = Constraint(expr= - m.x1026 - m.x1044 + m.x1047 == 0)

m.c1474 = Constraint(expr= - m.x1027 - m.x1045 + m.x1048 == 0)

m.c1475 = Constraint(expr=   m.x1028 - m.x1049 - m.x1052 == 0)

m.c1476 = Constraint(expr=   m.x1029 - m.x1050 - m.x1053 == 0)

m.c1477 = Constraint(expr=   m.x1030 - m.x1051 - m.x1054 == 0)

m.c1478 = Constraint(expr=   m.x1031 - m.x1055 - m.x1058 - m.x1061 == 0)

m.c1479 = Constraint(expr=   m.x1032 - m.x1056 - m.x1059 - m.x1062 == 0)

m.c1480 = Constraint(expr=   m.x1033 - m.x1057 - m.x1060 - m.x1063 == 0)

m.c1481 = Constraint(expr=(m.x1103/(0.001 + 0.999*m.b1349) - log(1 + m.x1091/(0.001 + 0.999*m.b1349)))*(0.001 + 0.999*
                          m.b1349) <= 0)

m.c1482 = Constraint(expr=(m.x1104/(0.001 + 0.999*m.b1350) - log(1 + m.x1092/(0.001 + 0.999*m.b1350)))*(0.001 + 0.999*
                          m.b1350) <= 0)

m.c1483 = Constraint(expr=(m.x1105/(0.001 + 0.999*m.b1351) - log(1 + m.x1093/(0.001 + 0.999*m.b1351)))*(0.001 + 0.999*
                          m.b1351) <= 0)

m.c1484 = Constraint(expr=   m.x1094 == 0)

m.c1485 = Constraint(expr=   m.x1095 == 0)

m.c1486 = Constraint(expr=   m.x1096 == 0)

m.c1487 = Constraint(expr=   m.x1106 == 0)

m.c1488 = Constraint(expr=   m.x1107 == 0)

m.c1489 = Constraint(expr=   m.x1108 == 0)

m.c1490 = Constraint(expr=   m.x959 - m.x1091 - m.x1094 == 0)

m.c1491 = Constraint(expr=   m.x960 - m.x1092 - m.x1095 == 0)

m.c1492 = Constraint(expr=   m.x961 - m.x1093 - m.x1096 == 0)

m.c1493 = Constraint(expr=   m.x965 - m.x1103 - m.x1106 == 0)

m.c1494 = Constraint(expr=   m.x966 - m.x1104 - m.x1107 == 0)

m.c1495 = Constraint(expr=   m.x967 - m.x1105 - m.x1108 == 0)

m.c1496 = Constraint(expr=   m.x1091 - 40*m.b1349 <= 0)

m.c1497 = Constraint(expr=   m.x1092 - 40*m.b1350 <= 0)

m.c1498 = Constraint(expr=   m.x1093 - 40*m.b1351 <= 0)

m.c1499 = Constraint(expr=   m.x1094 + 40*m.b1349 <= 40)

m.c1500 = Constraint(expr=   m.x1095 + 40*m.b1350 <= 40)

m.c1501 = Constraint(expr=   m.x1096 + 40*m.b1351 <= 40)

m.c1502 = Constraint(expr=   m.x1103 - 3.71357206670431*m.b1349 <= 0)

m.c1503 = Constraint(expr=   m.x1104 - 3.71357206670431*m.b1350 <= 0)

m.c1504 = Constraint(expr=   m.x1105 - 3.71357206670431*m.b1351 <= 0)

m.c1505 = Constraint(expr=   m.x1106 + 3.71357206670431*m.b1349 <= 3.71357206670431)

m.c1506 = Constraint(expr=   m.x1107 + 3.71357206670431*m.b1350 <= 3.71357206670431)

m.c1507 = Constraint(expr=   m.x1108 + 3.71357206670431*m.b1351 <= 3.71357206670431)

m.c1508 = Constraint(expr=(m.x1109/(0.001 + 0.999*m.b1352) - 1.2*log(1 + m.x1097/(0.001 + 0.999*m.b1352)))*(0.001 + 
                          0.999*m.b1352) <= 0)

m.c1509 = Constraint(expr=(m.x1110/(0.001 + 0.999*m.b1353) - 1.2*log(1 + m.x1098/(0.001 + 0.999*m.b1353)))*(0.001 + 
                          0.999*m.b1353) <= 0)

m.c1510 = Constraint(expr=(m.x1111/(0.001 + 0.999*m.b1354) - 1.2*log(1 + m.x1099/(0.001 + 0.999*m.b1354)))*(0.001 + 
                          0.999*m.b1354) <= 0)

m.c1511 = Constraint(expr=   m.x1100 == 0)

m.c1512 = Constraint(expr=   m.x1101 == 0)

m.c1513 = Constraint(expr=   m.x1102 == 0)

m.c1514 = Constraint(expr=   m.x1112 == 0)

m.c1515 = Constraint(expr=   m.x1113 == 0)

m.c1516 = Constraint(expr=   m.x1114 == 0)

m.c1517 = Constraint(expr=   m.x962 - m.x1097 - m.x1100 == 0)

m.c1518 = Constraint(expr=   m.x963 - m.x1098 - m.x1101 == 0)

m.c1519 = Constraint(expr=   m.x964 - m.x1099 - m.x1102 == 0)

m.c1520 = Constraint(expr=   m.x968 - m.x1109 - m.x1112 == 0)

m.c1521 = Constraint(expr=   m.x969 - m.x1110 - m.x1113 == 0)

m.c1522 = Constraint(expr=   m.x970 - m.x1111 - m.x1114 == 0)

m.c1523 = Constraint(expr=   m.x1097 - 40*m.b1352 <= 0)

m.c1524 = Constraint(expr=   m.x1098 - 40*m.b1353 <= 0)

m.c1525 = Constraint(expr=   m.x1099 - 40*m.b1354 <= 0)

m.c1526 = Constraint(expr=   m.x1100 + 40*m.b1352 <= 40)

m.c1527 = Constraint(expr=   m.x1101 + 40*m.b1353 <= 40)

m.c1528 = Constraint(expr=   m.x1102 + 40*m.b1354 <= 40)

m.c1529 = Constraint(expr=   m.x1109 - 4.45628648004517*m.b1352 <= 0)

m.c1530 = Constraint(expr=   m.x1110 - 4.45628648004517*m.b1353 <= 0)

m.c1531 = Constraint(expr=   m.x1111 - 4.45628648004517*m.b1354 <= 0)

m.c1532 = Constraint(expr=   m.x1112 + 4.45628648004517*m.b1352 <= 4.45628648004517)

m.c1533 = Constraint(expr=   m.x1113 + 4.45628648004517*m.b1353 <= 4.45628648004517)

m.c1534 = Constraint(expr=   m.x1114 + 4.45628648004517*m.b1354 <= 4.45628648004517)

m.c1535 = Constraint(expr= - 0.75*m.x1115 + m.x1139 == 0)

m.c1536 = Constraint(expr= - 0.75*m.x1116 + m.x1140 == 0)

m.c1537 = Constraint(expr= - 0.75*m.x1117 + m.x1141 == 0)

m.c1538 = Constraint(expr=   m.x1118 == 0)

m.c1539 = Constraint(expr=   m.x1119 == 0)

m.c1540 = Constraint(expr=   m.x1120 == 0)

m.c1541 = Constraint(expr=   m.x1142 == 0)

m.c1542 = Constraint(expr=   m.x1143 == 0)

m.c1543 = Constraint(expr=   m.x1144 == 0)

m.c1544 = Constraint(expr=   m.x980 - m.x1115 - m.x1118 == 0)

m.c1545 = Constraint(expr=   m.x981 - m.x1116 - m.x1119 == 0)

m.c1546 = Constraint(expr=   m.x982 - m.x1117 - m.x1120 == 0)

m.c1547 = Constraint(expr=   m.x992 - m.x1139 - m.x1142 == 0)

m.c1548 = Constraint(expr=   m.x993 - m.x1140 - m.x1143 == 0)

m.c1549 = Constraint(expr=   m.x994 - m.x1141 - m.x1144 == 0)

m.c1550 = Constraint(expr=   m.x1115 - 4.45628648004517*m.b1355 <= 0)

m.c1551 = Constraint(expr=   m.x1116 - 4.45628648004517*m.b1356 <= 0)

m.c1552 = Constraint(expr=   m.x1117 - 4.45628648004517*m.b1357 <= 0)

m.c1553 = Constraint(expr=   m.x1118 + 4.45628648004517*m.b1355 <= 4.45628648004517)

m.c1554 = Constraint(expr=   m.x1119 + 4.45628648004517*m.b1356 <= 4.45628648004517)

m.c1555 = Constraint(expr=   m.x1120 + 4.45628648004517*m.b1357 <= 4.45628648004517)

m.c1556 = Constraint(expr=   m.x1139 - 3.34221486003388*m.b1355 <= 0)

m.c1557 = Constraint(expr=   m.x1140 - 3.34221486003388*m.b1356 <= 0)

m.c1558 = Constraint(expr=   m.x1141 - 3.34221486003388*m.b1357 <= 0)

m.c1559 = Constraint(expr=   m.x1142 + 3.34221486003388*m.b1355 <= 3.34221486003388)

m.c1560 = Constraint(expr=   m.x1143 + 3.34221486003388*m.b1356 <= 3.34221486003388)

m.c1561 = Constraint(expr=   m.x1144 + 3.34221486003388*m.b1357 <= 3.34221486003388)

m.c1562 = Constraint(expr=(m.x1145/(0.001 + 0.999*m.b1358) - 1.5*log(1 + m.x1121/(0.001 + 0.999*m.b1358)))*(0.001 + 
                          0.999*m.b1358) <= 0)

m.c1563 = Constraint(expr=(m.x1146/(0.001 + 0.999*m.b1359) - 1.5*log(1 + m.x1122/(0.001 + 0.999*m.b1359)))*(0.001 + 
                          0.999*m.b1359) <= 0)

m.c1564 = Constraint(expr=(m.x1147/(0.001 + 0.999*m.b1360) - 1.5*log(1 + m.x1123/(0.001 + 0.999*m.b1360)))*(0.001 + 
                          0.999*m.b1360) <= 0)

m.c1565 = Constraint(expr=   m.x1124 == 0)

m.c1566 = Constraint(expr=   m.x1125 == 0)

m.c1567 = Constraint(expr=   m.x1126 == 0)

m.c1568 = Constraint(expr=   m.x1151 == 0)

m.c1569 = Constraint(expr=   m.x1152 == 0)

m.c1570 = Constraint(expr=   m.x1153 == 0)

m.c1571 = Constraint(expr=   m.x983 - m.x1121 - m.x1124 == 0)

m.c1572 = Constraint(expr=   m.x984 - m.x1122 - m.x1125 == 0)

m.c1573 = Constraint(expr=   m.x985 - m.x1123 - m.x1126 == 0)

m.c1574 = Constraint(expr=   m.x995 - m.x1145 - m.x1151 == 0)

m.c1575 = Constraint(expr=   m.x996 - m.x1146 - m.x1152 == 0)

m.c1576 = Constraint(expr=   m.x997 - m.x1147 - m.x1153 == 0)

m.c1577 = Constraint(expr=   m.x1121 - 4.45628648004517*m.b1358 <= 0)

m.c1578 = Constraint(expr=   m.x1122 - 4.45628648004517*m.b1359 <= 0)

m.c1579 = Constraint(expr=   m.x1123 - 4.45628648004517*m.b1360 <= 0)

m.c1580 = Constraint(expr=   m.x1124 + 4.45628648004517*m.b1358 <= 4.45628648004517)

m.c1581 = Constraint(expr=   m.x1125 + 4.45628648004517*m.b1359 <= 4.45628648004517)

m.c1582 = Constraint(expr=   m.x1126 + 4.45628648004517*m.b1360 <= 4.45628648004517)

m.c1583 = Constraint(expr=   m.x1145 - 2.54515263975353*m.b1358 <= 0)

m.c1584 = Constraint(expr=   m.x1146 - 2.54515263975353*m.b1359 <= 0)

m.c1585 = Constraint(expr=   m.x1147 - 2.54515263975353*m.b1360 <= 0)

m.c1586 = Constraint(expr=   m.x1151 + 2.54515263975353*m.b1358 <= 2.54515263975353)

m.c1587 = Constraint(expr=   m.x1152 + 2.54515263975353*m.b1359 <= 2.54515263975353)

m.c1588 = Constraint(expr=   m.x1153 + 2.54515263975353*m.b1360 <= 2.54515263975353)

m.c1589 = Constraint(expr= - m.x1127 + m.x1157 == 0)

m.c1590 = Constraint(expr= - m.x1128 + m.x1158 == 0)

m.c1591 = Constraint(expr= - m.x1129 + m.x1159 == 0)

m.c1592 = Constraint(expr= - 0.5*m.x1133 + m.x1157 == 0)

m.c1593 = Constraint(expr= - 0.5*m.x1134 + m.x1158 == 0)

m.c1594 = Constraint(expr= - 0.5*m.x1135 + m.x1159 == 0)

m.c1595 = Constraint(expr=   m.x1130 == 0)

m.c1596 = Constraint(expr=   m.x1131 == 0)

m.c1597 = Constraint(expr=   m.x1132 == 0)

m.c1598 = Constraint(expr=   m.x1136 == 0)

m.c1599 = Constraint(expr=   m.x1137 == 0)

m.c1600 = Constraint(expr=   m.x1138 == 0)

m.c1601 = Constraint(expr=   m.x1160 == 0)

m.c1602 = Constraint(expr=   m.x1161 == 0)

m.c1603 = Constraint(expr=   m.x1162 == 0)

m.c1604 = Constraint(expr=   m.x986 - m.x1127 - m.x1130 == 0)

m.c1605 = Constraint(expr=   m.x987 - m.x1128 - m.x1131 == 0)

m.c1606 = Constraint(expr=   m.x988 - m.x1129 - m.x1132 == 0)

m.c1607 = Constraint(expr=   m.x989 - m.x1133 - m.x1136 == 0)

m.c1608 = Constraint(expr=   m.x990 - m.x1134 - m.x1137 == 0)

m.c1609 = Constraint(expr=   m.x991 - m.x1135 - m.x1138 == 0)

m.c1610 = Constraint(expr=   m.x998 - m.x1157 - m.x1160 == 0)

m.c1611 = Constraint(expr=   m.x999 - m.x1158 - m.x1161 == 0)

m.c1612 = Constraint(expr=   m.x1000 - m.x1159 - m.x1162 == 0)

m.c1613 = Constraint(expr=   m.x1127 - 4.45628648004517*m.b1361 <= 0)

m.c1614 = Constraint(expr=   m.x1128 - 4.45628648004517*m.b1362 <= 0)

m.c1615 = Constraint(expr=   m.x1129 - 4.45628648004517*m.b1363 <= 0)

m.c1616 = Constraint(expr=   m.x1130 + 4.45628648004517*m.b1361 <= 4.45628648004517)

m.c1617 = Constraint(expr=   m.x1131 + 4.45628648004517*m.b1362 <= 4.45628648004517)

m.c1618 = Constraint(expr=   m.x1132 + 4.45628648004517*m.b1363 <= 4.45628648004517)

m.c1619 = Constraint(expr=   m.x1133 - 30*m.b1361 <= 0)

m.c1620 = Constraint(expr=   m.x1134 - 30*m.b1362 <= 0)

m.c1621 = Constraint(expr=   m.x1135 - 30*m.b1363 <= 0)

m.c1622 = Constraint(expr=   m.x1136 + 30*m.b1361 <= 30)

m.c1623 = Constraint(expr=   m.x1137 + 30*m.b1362 <= 30)

m.c1624 = Constraint(expr=   m.x1138 + 30*m.b1363 <= 30)

m.c1625 = Constraint(expr=   m.x1157 - 15*m.b1361 <= 0)

m.c1626 = Constraint(expr=   m.x1158 - 15*m.b1362 <= 0)

m.c1627 = Constraint(expr=   m.x1159 - 15*m.b1363 <= 0)

m.c1628 = Constraint(expr=   m.x1160 + 15*m.b1361 <= 15)

m.c1629 = Constraint(expr=   m.x1161 + 15*m.b1362 <= 15)

m.c1630 = Constraint(expr=   m.x1162 + 15*m.b1363 <= 15)

m.c1631 = Constraint(expr=(m.x1193/(0.001 + 0.999*m.b1364) - 1.25*log(1 + m.x1163/(0.001 + 0.999*m.b1364)))*(0.001 + 
                          0.999*m.b1364) <= 0)

m.c1632 = Constraint(expr=(m.x1194/(0.001 + 0.999*m.b1365) - 1.25*log(1 + m.x1164/(0.001 + 0.999*m.b1365)))*(0.001 + 
                          0.999*m.b1365) <= 0)

m.c1633 = Constraint(expr=(m.x1195/(0.001 + 0.999*m.b1366) - 1.25*log(1 + m.x1165/(0.001 + 0.999*m.b1366)))*(0.001 + 
                          0.999*m.b1366) <= 0)

m.c1634 = Constraint(expr=   m.x1166 == 0)

m.c1635 = Constraint(expr=   m.x1167 == 0)

m.c1636 = Constraint(expr=   m.x1168 == 0)

m.c1637 = Constraint(expr=   m.x1199 == 0)

m.c1638 = Constraint(expr=   m.x1200 == 0)

m.c1639 = Constraint(expr=   m.x1201 == 0)

m.c1640 = Constraint(expr=   m.x1001 - m.x1163 - m.x1166 == 0)

m.c1641 = Constraint(expr=   m.x1002 - m.x1164 - m.x1167 == 0)

m.c1642 = Constraint(expr=   m.x1003 - m.x1165 - m.x1168 == 0)

m.c1643 = Constraint(expr=   m.x1016 - m.x1193 - m.x1199 == 0)

m.c1644 = Constraint(expr=   m.x1017 - m.x1194 - m.x1200 == 0)

m.c1645 = Constraint(expr=   m.x1018 - m.x1195 - m.x1201 == 0)

m.c1646 = Constraint(expr=   m.x1163 - 3.34221486003388*m.b1364 <= 0)

m.c1647 = Constraint(expr=   m.x1164 - 3.34221486003388*m.b1365 <= 0)

m.c1648 = Constraint(expr=   m.x1165 - 3.34221486003388*m.b1366 <= 0)

m.c1649 = Constraint(expr=   m.x1166 + 3.34221486003388*m.b1364 <= 3.34221486003388)

m.c1650 = Constraint(expr=   m.x1167 + 3.34221486003388*m.b1365 <= 3.34221486003388)

m.c1651 = Constraint(expr=   m.x1168 + 3.34221486003388*m.b1366 <= 3.34221486003388)

m.c1652 = Constraint(expr=   m.x1193 - 1.83548069293539*m.b1364 <= 0)

m.c1653 = Constraint(expr=   m.x1194 - 1.83548069293539*m.b1365 <= 0)

m.c1654 = Constraint(expr=   m.x1195 - 1.83548069293539*m.b1366 <= 0)

m.c1655 = Constraint(expr=   m.x1199 + 1.83548069293539*m.b1364 <= 1.83548069293539)

m.c1656 = Constraint(expr=   m.x1200 + 1.83548069293539*m.b1365 <= 1.83548069293539)

m.c1657 = Constraint(expr=   m.x1201 + 1.83548069293539*m.b1366 <= 1.83548069293539)

m.c1658 = Constraint(expr=(m.x1205/(0.001 + 0.999*m.b1367) - 0.9*log(1 + m.x1169/(0.001 + 0.999*m.b1367)))*(0.001 + 
                          0.999*m.b1367) <= 0)

m.c1659 = Constraint(expr=(m.x1206/(0.001 + 0.999*m.b1368) - 0.9*log(1 + m.x1170/(0.001 + 0.999*m.b1368)))*(0.001 + 
                          0.999*m.b1368) <= 0)

m.c1660 = Constraint(expr=(m.x1207/(0.001 + 0.999*m.b1369) - 0.9*log(1 + m.x1171/(0.001 + 0.999*m.b1369)))*(0.001 + 
                          0.999*m.b1369) <= 0)

m.c1661 = Constraint(expr=   m.x1172 == 0)

m.c1662 = Constraint(expr=   m.x1173 == 0)

m.c1663 = Constraint(expr=   m.x1174 == 0)

m.c1664 = Constraint(expr=   m.x1211 == 0)

m.c1665 = Constraint(expr=   m.x1212 == 0)

m.c1666 = Constraint(expr=   m.x1213 == 0)

m.c1667 = Constraint(expr=   m.x1004 - m.x1169 - m.x1172 == 0)

m.c1668 = Constraint(expr=   m.x1005 - m.x1170 - m.x1173 == 0)

m.c1669 = Constraint(expr=   m.x1006 - m.x1171 - m.x1174 == 0)

m.c1670 = Constraint(expr=   m.x1019 - m.x1205 - m.x1211 == 0)

m.c1671 = Constraint(expr=   m.x1020 - m.x1206 - m.x1212 == 0)

m.c1672 = Constraint(expr=   m.x1021 - m.x1207 - m.x1213 == 0)

m.c1673 = Constraint(expr=   m.x1169 - 3.34221486003388*m.b1367 <= 0)

m.c1674 = Constraint(expr=   m.x1170 - 3.34221486003388*m.b1368 <= 0)

m.c1675 = Constraint(expr=   m.x1171 - 3.34221486003388*m.b1369 <= 0)

m.c1676 = Constraint(expr=   m.x1172 + 3.34221486003388*m.b1367 <= 3.34221486003388)

m.c1677 = Constraint(expr=   m.x1173 + 3.34221486003388*m.b1368 <= 3.34221486003388)

m.c1678 = Constraint(expr=   m.x1174 + 3.34221486003388*m.b1369 <= 3.34221486003388)

m.c1679 = Constraint(expr=   m.x1205 - 1.32154609891348*m.b1367 <= 0)

m.c1680 = Constraint(expr=   m.x1206 - 1.32154609891348*m.b1368 <= 0)

m.c1681 = Constraint(expr=   m.x1207 - 1.32154609891348*m.b1369 <= 0)

m.c1682 = Constraint(expr=   m.x1211 + 1.32154609891348*m.b1367 <= 1.32154609891348)

m.c1683 = Constraint(expr=   m.x1212 + 1.32154609891348*m.b1368 <= 1.32154609891348)

m.c1684 = Constraint(expr=   m.x1213 + 1.32154609891348*m.b1369 <= 1.32154609891348)

m.c1685 = Constraint(expr=(m.x1217/(0.001 + 0.999*m.b1370) - log(1 + m.x1148/(0.001 + 0.999*m.b1370)))*(0.001 + 0.999*
                          m.b1370) <= 0)

m.c1686 = Constraint(expr=(m.x1218/(0.001 + 0.999*m.b1371) - log(1 + m.x1149/(0.001 + 0.999*m.b1371)))*(0.001 + 0.999*
                          m.b1371) <= 0)

m.c1687 = Constraint(expr=(m.x1219/(0.001 + 0.999*m.b1372) - log(1 + m.x1150/(0.001 + 0.999*m.b1372)))*(0.001 + 0.999*
                          m.b1372) <= 0)

m.c1688 = Constraint(expr=   m.x1154 == 0)

m.c1689 = Constraint(expr=   m.x1155 == 0)

m.c1690 = Constraint(expr=   m.x1156 == 0)

m.c1691 = Constraint(expr=   m.x1220 == 0)

m.c1692 = Constraint(expr=   m.x1221 == 0)

m.c1693 = Constraint(expr=   m.x1222 == 0)

m.c1694 = Constraint(expr=   m.x995 - m.x1148 - m.x1154 == 0)

m.c1695 = Constraint(expr=   m.x996 - m.x1149 - m.x1155 == 0)

m.c1696 = Constraint(expr=   m.x997 - m.x1150 - m.x1156 == 0)

m.c1697 = Constraint(expr=   m.x1022 - m.x1217 - m.x1220 == 0)

m.c1698 = Constraint(expr=   m.x1023 - m.x1218 - m.x1221 == 0)

m.c1699 = Constraint(expr=   m.x1024 - m.x1219 - m.x1222 == 0)

m.c1700 = Constraint(expr=   m.x1148 - 2.54515263975353*m.b1370 <= 0)

m.c1701 = Constraint(expr=   m.x1149 - 2.54515263975353*m.b1371 <= 0)

m.c1702 = Constraint(expr=   m.x1150 - 2.54515263975353*m.b1372 <= 0)

m.c1703 = Constraint(expr=   m.x1154 + 2.54515263975353*m.b1370 <= 2.54515263975353)

m.c1704 = Constraint(expr=   m.x1155 + 2.54515263975353*m.b1371 <= 2.54515263975353)

m.c1705 = Constraint(expr=   m.x1156 + 2.54515263975353*m.b1372 <= 2.54515263975353)

m.c1706 = Constraint(expr=   m.x1217 - 1.26558121681553*m.b1370 <= 0)

m.c1707 = Constraint(expr=   m.x1218 - 1.26558121681553*m.b1371 <= 0)

m.c1708 = Constraint(expr=   m.x1219 - 1.26558121681553*m.b1372 <= 0)

m.c1709 = Constraint(expr=   m.x1220 + 1.26558121681553*m.b1370 <= 1.26558121681553)

m.c1710 = Constraint(expr=   m.x1221 + 1.26558121681553*m.b1371 <= 1.26558121681553)

m.c1711 = Constraint(expr=   m.x1222 + 1.26558121681553*m.b1372 <= 1.26558121681553)

m.c1712 = Constraint(expr= - 0.9*m.x1175 + m.x1223 == 0)

m.c1713 = Constraint(expr= - 0.9*m.x1176 + m.x1224 == 0)

m.c1714 = Constraint(expr= - 0.9*m.x1177 + m.x1225 == 0)

m.c1715 = Constraint(expr=   m.x1178 == 0)

m.c1716 = Constraint(expr=   m.x1179 == 0)

m.c1717 = Constraint(expr=   m.x1180 == 0)

m.c1718 = Constraint(expr=   m.x1226 == 0)

m.c1719 = Constraint(expr=   m.x1227 == 0)

m.c1720 = Constraint(expr=   m.x1228 == 0)

m.c1721 = Constraint(expr=   m.x1007 - m.x1175 - m.x1178 == 0)

m.c1722 = Constraint(expr=   m.x1008 - m.x1176 - m.x1179 == 0)

m.c1723 = Constraint(expr=   m.x1009 - m.x1177 - m.x1180 == 0)

m.c1724 = Constraint(expr=   m.x1025 - m.x1223 - m.x1226 == 0)

m.c1725 = Constraint(expr=   m.x1026 - m.x1224 - m.x1227 == 0)

m.c1726 = Constraint(expr=   m.x1027 - m.x1225 - m.x1228 == 0)

m.c1727 = Constraint(expr=   m.x1175 - 15*m.b1373 <= 0)

m.c1728 = Constraint(expr=   m.x1176 - 15*m.b1374 <= 0)

m.c1729 = Constraint(expr=   m.x1177 - 15*m.b1375 <= 0)

m.c1730 = Constraint(expr=   m.x1178 + 15*m.b1373 <= 15)

m.c1731 = Constraint(expr=   m.x1179 + 15*m.b1374 <= 15)

m.c1732 = Constraint(expr=   m.x1180 + 15*m.b1375 <= 15)

m.c1733 = Constraint(expr=   m.x1223 - 13.5*m.b1373 <= 0)

m.c1734 = Constraint(expr=   m.x1224 - 13.5*m.b1374 <= 0)

m.c1735 = Constraint(expr=   m.x1225 - 13.5*m.b1375 <= 0)

m.c1736 = Constraint(expr=   m.x1226 + 13.5*m.b1373 <= 13.5)

m.c1737 = Constraint(expr=   m.x1227 + 13.5*m.b1374 <= 13.5)

m.c1738 = Constraint(expr=   m.x1228 + 13.5*m.b1375 <= 13.5)

m.c1739 = Constraint(expr= - 0.6*m.x1181 + m.x1229 == 0)

m.c1740 = Constraint(expr= - 0.6*m.x1182 + m.x1230 == 0)

m.c1741 = Constraint(expr= - 0.6*m.x1183 + m.x1231 == 0)

m.c1742 = Constraint(expr=   m.x1184 == 0)

m.c1743 = Constraint(expr=   m.x1185 == 0)

m.c1744 = Constraint(expr=   m.x1186 == 0)

m.c1745 = Constraint(expr=   m.x1232 == 0)

m.c1746 = Constraint(expr=   m.x1233 == 0)

m.c1747 = Constraint(expr=   m.x1234 == 0)

m.c1748 = Constraint(expr=   m.x1010 - m.x1181 - m.x1184 == 0)

m.c1749 = Constraint(expr=   m.x1011 - m.x1182 - m.x1185 == 0)

m.c1750 = Constraint(expr=   m.x1012 - m.x1183 - m.x1186 == 0)

m.c1751 = Constraint(expr=   m.x1028 - m.x1229 - m.x1232 == 0)

m.c1752 = Constraint(expr=   m.x1029 - m.x1230 - m.x1233 == 0)

m.c1753 = Constraint(expr=   m.x1030 - m.x1231 - m.x1234 == 0)

m.c1754 = Constraint(expr=   m.x1181 - 15*m.b1376 <= 0)

m.c1755 = Constraint(expr=   m.x1182 - 15*m.b1377 <= 0)

m.c1756 = Constraint(expr=   m.x1183 - 15*m.b1378 <= 0)

m.c1757 = Constraint(expr=   m.x1184 + 15*m.b1376 <= 15)

m.c1758 = Constraint(expr=   m.x1185 + 15*m.b1377 <= 15)

m.c1759 = Constraint(expr=   m.x1186 + 15*m.b1378 <= 15)

m.c1760 = Constraint(expr=   m.x1229 - 9*m.b1376 <= 0)

m.c1761 = Constraint(expr=   m.x1230 - 9*m.b1377 <= 0)

m.c1762 = Constraint(expr=   m.x1231 - 9*m.b1378 <= 0)

m.c1763 = Constraint(expr=   m.x1232 + 9*m.b1376 <= 9)

m.c1764 = Constraint(expr=   m.x1233 + 9*m.b1377 <= 9)

m.c1765 = Constraint(expr=   m.x1234 + 9*m.b1378 <= 9)

m.c1766 = Constraint(expr=(m.x1235/(0.001 + 0.999*m.b1379) - 1.1*log(1 + m.x1187/(0.001 + 0.999*m.b1379)))*(0.001 + 
                          0.999*m.b1379) <= 0)

m.c1767 = Constraint(expr=(m.x1236/(0.001 + 0.999*m.b1380) - 1.1*log(1 + m.x1188/(0.001 + 0.999*m.b1380)))*(0.001 + 
                          0.999*m.b1380) <= 0)

m.c1768 = Constraint(expr=(m.x1237/(0.001 + 0.999*m.b1381) - 1.1*log(1 + m.x1189/(0.001 + 0.999*m.b1381)))*(0.001 + 
                          0.999*m.b1381) <= 0)

m.c1769 = Constraint(expr=   m.x1190 == 0)

m.c1770 = Constraint(expr=   m.x1191 == 0)

m.c1771 = Constraint(expr=   m.x1192 == 0)

m.c1772 = Constraint(expr=   m.x1238 == 0)

m.c1773 = Constraint(expr=   m.x1239 == 0)

m.c1774 = Constraint(expr=   m.x1240 == 0)

m.c1775 = Constraint(expr=   m.x1013 - m.x1187 - m.x1190 == 0)

m.c1776 = Constraint(expr=   m.x1014 - m.x1188 - m.x1191 == 0)

m.c1777 = Constraint(expr=   m.x1015 - m.x1189 - m.x1192 == 0)

m.c1778 = Constraint(expr=   m.x1031 - m.x1235 - m.x1238 == 0)

m.c1779 = Constraint(expr=   m.x1032 - m.x1236 - m.x1239 == 0)

m.c1780 = Constraint(expr=   m.x1033 - m.x1237 - m.x1240 == 0)

m.c1781 = Constraint(expr=   m.x1187 - 15*m.b1379 <= 0)

m.c1782 = Constraint(expr=   m.x1188 - 15*m.b1380 <= 0)

m.c1783 = Constraint(expr=   m.x1189 - 15*m.b1381 <= 0)

m.c1784 = Constraint(expr=   m.x1190 + 15*m.b1379 <= 15)

m.c1785 = Constraint(expr=   m.x1191 + 15*m.b1380 <= 15)

m.c1786 = Constraint(expr=   m.x1192 + 15*m.b1381 <= 15)

m.c1787 = Constraint(expr=   m.x1235 - 3.04984759446376*m.b1379 <= 0)

m.c1788 = Constraint(expr=   m.x1236 - 3.04984759446376*m.b1380 <= 0)

m.c1789 = Constraint(expr=   m.x1237 - 3.04984759446376*m.b1381 <= 0)

m.c1790 = Constraint(expr=   m.x1238 + 3.04984759446376*m.b1379 <= 3.04984759446376)

m.c1791 = Constraint(expr=   m.x1239 + 3.04984759446376*m.b1380 <= 3.04984759446376)

m.c1792 = Constraint(expr=   m.x1240 + 3.04984759446376*m.b1381 <= 3.04984759446376)

m.c1793 = Constraint(expr= - 0.9*m.x1196 + m.x1295 == 0)

m.c1794 = Constraint(expr= - 0.9*m.x1197 + m.x1296 == 0)

m.c1795 = Constraint(expr= - 0.9*m.x1198 + m.x1297 == 0)

m.c1796 = Constraint(expr= - m.x1253 + m.x1295 == 0)

m.c1797 = Constraint(expr= - m.x1254 + m.x1296 == 0)

m.c1798 = Constraint(expr= - m.x1255 + m.x1297 == 0)

m.c1799 = Constraint(expr=   m.x1202 == 0)

m.c1800 = Constraint(expr=   m.x1203 == 0)

m.c1801 = Constraint(expr=   m.x1204 == 0)

m.c1802 = Constraint(expr=   m.x1256 == 0)

m.c1803 = Constraint(expr=   m.x1257 == 0)

m.c1804 = Constraint(expr=   m.x1258 == 0)

m.c1805 = Constraint(expr=   m.x1298 == 0)

m.c1806 = Constraint(expr=   m.x1299 == 0)

m.c1807 = Constraint(expr=   m.x1300 == 0)

m.c1808 = Constraint(expr=   m.x1016 - m.x1196 - m.x1202 == 0)

m.c1809 = Constraint(expr=   m.x1017 - m.x1197 - m.x1203 == 0)

m.c1810 = Constraint(expr=   m.x1018 - m.x1198 - m.x1204 == 0)

m.c1811 = Constraint(expr=   m.x1040 - m.x1253 - m.x1256 == 0)

m.c1812 = Constraint(expr=   m.x1041 - m.x1254 - m.x1257 == 0)

m.c1813 = Constraint(expr=   m.x1042 - m.x1255 - m.x1258 == 0)

m.c1814 = Constraint(expr=   m.x1064 - m.x1295 - m.x1298 == 0)

m.c1815 = Constraint(expr=   m.x1065 - m.x1296 - m.x1299 == 0)

m.c1816 = Constraint(expr=   m.x1066 - m.x1297 - m.x1300 == 0)

m.c1817 = Constraint(expr=   m.x1196 - 1.83548069293539*m.b1382 <= 0)

m.c1818 = Constraint(expr=   m.x1197 - 1.83548069293539*m.b1383 <= 0)

m.c1819 = Constraint(expr=   m.x1198 - 1.83548069293539*m.b1384 <= 0)

m.c1820 = Constraint(expr=   m.x1202 + 1.83548069293539*m.b1382 <= 1.83548069293539)

m.c1821 = Constraint(expr=   m.x1203 + 1.83548069293539*m.b1383 <= 1.83548069293539)

m.c1822 = Constraint(expr=   m.x1204 + 1.83548069293539*m.b1384 <= 1.83548069293539)

m.c1823 = Constraint(expr=   m.x1253 - 20*m.b1382 <= 0)

m.c1824 = Constraint(expr=   m.x1254 - 20*m.b1383 <= 0)

m.c1825 = Constraint(expr=   m.x1255 - 20*m.b1384 <= 0)

m.c1826 = Constraint(expr=   m.x1256 + 20*m.b1382 <= 20)

m.c1827 = Constraint(expr=   m.x1257 + 20*m.b1383 <= 20)

m.c1828 = Constraint(expr=   m.x1258 + 20*m.b1384 <= 20)

m.c1829 = Constraint(expr=   m.x1295 - 20*m.b1382 <= 0)

m.c1830 = Constraint(expr=   m.x1296 - 20*m.b1383 <= 0)

m.c1831 = Constraint(expr=   m.x1297 - 20*m.b1384 <= 0)

m.c1832 = Constraint(expr=   m.x1298 + 20*m.b1382 <= 20)

m.c1833 = Constraint(expr=   m.x1299 + 20*m.b1383 <= 20)

m.c1834 = Constraint(expr=   m.x1300 + 20*m.b1384 <= 20)

m.c1835 = Constraint(expr=(m.x1301/(0.001 + 0.999*m.b1385) - log(1 + m.x1208/(0.001 + 0.999*m.b1385)))*(0.001 + 0.999*
                          m.b1385) <= 0)

m.c1836 = Constraint(expr=(m.x1302/(0.001 + 0.999*m.b1386) - log(1 + m.x1209/(0.001 + 0.999*m.b1386)))*(0.001 + 0.999*
                          m.b1386) <= 0)

m.c1837 = Constraint(expr=(m.x1303/(0.001 + 0.999*m.b1387) - log(1 + m.x1210/(0.001 + 0.999*m.b1387)))*(0.001 + 0.999*
                          m.b1387) <= 0)

m.c1838 = Constraint(expr=   m.x1214 == 0)

m.c1839 = Constraint(expr=   m.x1215 == 0)

m.c1840 = Constraint(expr=   m.x1216 == 0)

m.c1841 = Constraint(expr=   m.x1304 == 0)

m.c1842 = Constraint(expr=   m.x1305 == 0)

m.c1843 = Constraint(expr=   m.x1306 == 0)

m.c1844 = Constraint(expr=   m.x1019 - m.x1208 - m.x1214 == 0)

m.c1845 = Constraint(expr=   m.x1020 - m.x1209 - m.x1215 == 0)

m.c1846 = Constraint(expr=   m.x1021 - m.x1210 - m.x1216 == 0)

m.c1847 = Constraint(expr=   m.x1067 - m.x1301 - m.x1304 == 0)

m.c1848 = Constraint(expr=   m.x1068 - m.x1302 - m.x1305 == 0)

m.c1849 = Constraint(expr=   m.x1069 - m.x1303 - m.x1306 == 0)

m.c1850 = Constraint(expr=   m.x1208 - 1.32154609891348*m.b1385 <= 0)

m.c1851 = Constraint(expr=   m.x1209 - 1.32154609891348*m.b1386 <= 0)

m.c1852 = Constraint(expr=   m.x1210 - 1.32154609891348*m.b1387 <= 0)

m.c1853 = Constraint(expr=   m.x1214 + 1.32154609891348*m.b1385 <= 1.32154609891348)

m.c1854 = Constraint(expr=   m.x1215 + 1.32154609891348*m.b1386 <= 1.32154609891348)

m.c1855 = Constraint(expr=   m.x1216 + 1.32154609891348*m.b1387 <= 1.32154609891348)

m.c1856 = Constraint(expr=   m.x1301 - 0.842233385663186*m.b1385 <= 0)

m.c1857 = Constraint(expr=   m.x1302 - 0.842233385663186*m.b1386 <= 0)

m.c1858 = Constraint(expr=   m.x1303 - 0.842233385663186*m.b1387 <= 0)

m.c1859 = Constraint(expr=   m.x1304 + 0.842233385663186*m.b1385 <= 0.842233385663186)

m.c1860 = Constraint(expr=   m.x1305 + 0.842233385663186*m.b1386 <= 0.842233385663186)

m.c1861 = Constraint(expr=   m.x1306 + 0.842233385663186*m.b1387 <= 0.842233385663186)

m.c1862 = Constraint(expr=(m.x1307/(0.001 + 0.999*m.b1388) - 0.7*log(1 + m.x1241/(0.001 + 0.999*m.b1388)))*(0.001 + 
                          0.999*m.b1388) <= 0)

m.c1863 = Constraint(expr=(m.x1308/(0.001 + 0.999*m.b1389) - 0.7*log(1 + m.x1242/(0.001 + 0.999*m.b1389)))*(0.001 + 
                          0.999*m.b1389) <= 0)

m.c1864 = Constraint(expr=(m.x1309/(0.001 + 0.999*m.b1390) - 0.7*log(1 + m.x1243/(0.001 + 0.999*m.b1390)))*(0.001 + 
                          0.999*m.b1390) <= 0)

m.c1865 = Constraint(expr=   m.x1244 == 0)

m.c1866 = Constraint(expr=   m.x1245 == 0)

m.c1867 = Constraint(expr=   m.x1246 == 0)

m.c1868 = Constraint(expr=   m.x1310 == 0)

m.c1869 = Constraint(expr=   m.x1311 == 0)

m.c1870 = Constraint(expr=   m.x1312 == 0)

m.c1871 = Constraint(expr=   m.x1034 - m.x1241 - m.x1244 == 0)

m.c1872 = Constraint(expr=   m.x1035 - m.x1242 - m.x1245 == 0)

m.c1873 = Constraint(expr=   m.x1036 - m.x1243 - m.x1246 == 0)

m.c1874 = Constraint(expr=   m.x1070 - m.x1307 - m.x1310 == 0)

m.c1875 = Constraint(expr=   m.x1071 - m.x1308 - m.x1311 == 0)

m.c1876 = Constraint(expr=   m.x1072 - m.x1309 - m.x1312 == 0)

m.c1877 = Constraint(expr=   m.x1241 - 1.26558121681553*m.b1388 <= 0)

m.c1878 = Constraint(expr=   m.x1242 - 1.26558121681553*m.b1389 <= 0)

m.c1879 = Constraint(expr=   m.x1243 - 1.26558121681553*m.b1390 <= 0)

m.c1880 = Constraint(expr=   m.x1244 + 1.26558121681553*m.b1388 <= 1.26558121681553)

m.c1881 = Constraint(expr=   m.x1245 + 1.26558121681553*m.b1389 <= 1.26558121681553)

m.c1882 = Constraint(expr=   m.x1246 + 1.26558121681553*m.b1390 <= 1.26558121681553)

m.c1883 = Constraint(expr=   m.x1307 - 0.572481933717686*m.b1388 <= 0)

m.c1884 = Constraint(expr=   m.x1308 - 0.572481933717686*m.b1389 <= 0)

m.c1885 = Constraint(expr=   m.x1309 - 0.572481933717686*m.b1390 <= 0)

m.c1886 = Constraint(expr=   m.x1310 + 0.572481933717686*m.b1388 <= 0.572481933717686)

m.c1887 = Constraint(expr=   m.x1311 + 0.572481933717686*m.b1389 <= 0.572481933717686)

m.c1888 = Constraint(expr=   m.x1312 + 0.572481933717686*m.b1390 <= 0.572481933717686)

m.c1889 = Constraint(expr=(m.x1313/(0.001 + 0.999*m.b1391) - 0.65*log(1 + m.x1247/(0.001 + 0.999*m.b1391)))*(0.001 + 
                          0.999*m.b1391) <= 0)

m.c1890 = Constraint(expr=(m.x1314/(0.001 + 0.999*m.b1392) - 0.65*log(1 + m.x1248/(0.001 + 0.999*m.b1392)))*(0.001 + 
                          0.999*m.b1392) <= 0)

m.c1891 = Constraint(expr=(m.x1315/(0.001 + 0.999*m.b1393) - 0.65*log(1 + m.x1249/(0.001 + 0.999*m.b1393)))*(0.001 + 
                          0.999*m.b1393) <= 0)

m.c1892 = Constraint(expr=(m.x1313/(0.001 + 0.999*m.b1391) - 0.65*log(1 + m.x1259/(0.001 + 0.999*m.b1391)))*(0.001 + 
                          0.999*m.b1391) <= 0)

m.c1893 = Constraint(expr=(m.x1314/(0.001 + 0.999*m.b1392) - 0.65*log(1 + m.x1260/(0.001 + 0.999*m.b1392)))*(0.001 + 
                          0.999*m.b1392) <= 0)

m.c1894 = Constraint(expr=(m.x1315/(0.001 + 0.999*m.b1393) - 0.65*log(1 + m.x1261/(0.001 + 0.999*m.b1393)))*(0.001 + 
                          0.999*m.b1393) <= 0)

m.c1895 = Constraint(expr=   m.x1250 == 0)

m.c1896 = Constraint(expr=   m.x1251 == 0)

m.c1897 = Constraint(expr=   m.x1252 == 0)

m.c1898 = Constraint(expr=   m.x1262 == 0)

m.c1899 = Constraint(expr=   m.x1263 == 0)

m.c1900 = Constraint(expr=   m.x1264 == 0)

m.c1901 = Constraint(expr=   m.x1316 == 0)

m.c1902 = Constraint(expr=   m.x1317 == 0)

m.c1903 = Constraint(expr=   m.x1318 == 0)

m.c1904 = Constraint(expr=   m.x1037 - m.x1247 - m.x1250 == 0)

m.c1905 = Constraint(expr=   m.x1038 - m.x1248 - m.x1251 == 0)

m.c1906 = Constraint(expr=   m.x1039 - m.x1249 - m.x1252 == 0)

m.c1907 = Constraint(expr=   m.x1046 - m.x1259 - m.x1262 == 0)

m.c1908 = Constraint(expr=   m.x1047 - m.x1260 - m.x1263 == 0)

m.c1909 = Constraint(expr=   m.x1048 - m.x1261 - m.x1264 == 0)

m.c1910 = Constraint(expr=   m.x1073 - m.x1313 - m.x1316 == 0)

m.c1911 = Constraint(expr=   m.x1074 - m.x1314 - m.x1317 == 0)

m.c1912 = Constraint(expr=   m.x1075 - m.x1315 - m.x1318 == 0)

m.c1913 = Constraint(expr=   m.x1247 - 1.26558121681553*m.b1391 <= 0)

m.c1914 = Constraint(expr=   m.x1248 - 1.26558121681553*m.b1392 <= 0)

m.c1915 = Constraint(expr=   m.x1249 - 1.26558121681553*m.b1393 <= 0)

m.c1916 = Constraint(expr=   m.x1250 + 1.26558121681553*m.b1391 <= 1.26558121681553)

m.c1917 = Constraint(expr=   m.x1251 + 1.26558121681553*m.b1392 <= 1.26558121681553)

m.c1918 = Constraint(expr=   m.x1252 + 1.26558121681553*m.b1393 <= 1.26558121681553)

m.c1919 = Constraint(expr=   m.x1259 - 33.5*m.b1391 <= 0)

m.c1920 = Constraint(expr=   m.x1260 - 33.5*m.b1392 <= 0)

m.c1921 = Constraint(expr=   m.x1261 - 33.5*m.b1393 <= 0)

m.c1922 = Constraint(expr=   m.x1262 + 33.5*m.b1391 <= 33.5)

m.c1923 = Constraint(expr=   m.x1263 + 33.5*m.b1392 <= 33.5)

m.c1924 = Constraint(expr=   m.x1264 + 33.5*m.b1393 <= 33.5)

m.c1925 = Constraint(expr=   m.x1313 - 2.30162356062425*m.b1391 <= 0)

m.c1926 = Constraint(expr=   m.x1314 - 2.30162356062425*m.b1392 <= 0)

m.c1927 = Constraint(expr=   m.x1315 - 2.30162356062425*m.b1393 <= 0)

m.c1928 = Constraint(expr=   m.x1316 + 2.30162356062425*m.b1391 <= 2.30162356062425)

m.c1929 = Constraint(expr=   m.x1317 + 2.30162356062425*m.b1392 <= 2.30162356062425)

m.c1930 = Constraint(expr=   m.x1318 + 2.30162356062425*m.b1393 <= 2.30162356062425)

m.c1931 = Constraint(expr= - m.x1265 + m.x1319 == 0)

m.c1932 = Constraint(expr= - m.x1266 + m.x1320 == 0)

m.c1933 = Constraint(expr= - m.x1267 + m.x1321 == 0)

m.c1934 = Constraint(expr=   m.x1268 == 0)

m.c1935 = Constraint(expr=   m.x1269 == 0)

m.c1936 = Constraint(expr=   m.x1270 == 0)

m.c1937 = Constraint(expr=   m.x1322 == 0)

m.c1938 = Constraint(expr=   m.x1323 == 0)

m.c1939 = Constraint(expr=   m.x1324 == 0)

m.c1940 = Constraint(expr=   m.x1049 - m.x1265 - m.x1268 == 0)

m.c1941 = Constraint(expr=   m.x1050 - m.x1266 - m.x1269 == 0)

m.c1942 = Constraint(expr=   m.x1051 - m.x1267 - m.x1270 == 0)

m.c1943 = Constraint(expr=   m.x1076 - m.x1319 - m.x1322 == 0)

m.c1944 = Constraint(expr=   m.x1077 - m.x1320 - m.x1323 == 0)

m.c1945 = Constraint(expr=   m.x1078 - m.x1321 - m.x1324 == 0)

m.c1946 = Constraint(expr=   m.x1265 - 9*m.b1394 <= 0)

m.c1947 = Constraint(expr=   m.x1266 - 9*m.b1395 <= 0)

m.c1948 = Constraint(expr=   m.x1267 - 9*m.b1396 <= 0)

m.c1949 = Constraint(expr=   m.x1268 + 9*m.b1394 <= 9)

m.c1950 = Constraint(expr=   m.x1269 + 9*m.b1395 <= 9)

m.c1951 = Constraint(expr=   m.x1270 + 9*m.b1396 <= 9)

m.c1952 = Constraint(expr=   m.x1319 - 9*m.b1394 <= 0)

m.c1953 = Constraint(expr=   m.x1320 - 9*m.b1395 <= 0)

m.c1954 = Constraint(expr=   m.x1321 - 9*m.b1396 <= 0)

m.c1955 = Constraint(expr=   m.x1322 + 9*m.b1394 <= 9)

m.c1956 = Constraint(expr=   m.x1323 + 9*m.b1395 <= 9)

m.c1957 = Constraint(expr=   m.x1324 + 9*m.b1396 <= 9)

m.c1958 = Constraint(expr= - m.x1271 + m.x1325 == 0)

m.c1959 = Constraint(expr= - m.x1272 + m.x1326 == 0)

m.c1960 = Constraint(expr= - m.x1273 + m.x1327 == 0)

m.c1961 = Constraint(expr=   m.x1274 == 0)

m.c1962 = Constraint(expr=   m.x1275 == 0)

m.c1963 = Constraint(expr=   m.x1276 == 0)

m.c1964 = Constraint(expr=   m.x1328 == 0)

m.c1965 = Constraint(expr=   m.x1329 == 0)

m.c1966 = Constraint(expr=   m.x1330 == 0)

m.c1967 = Constraint(expr=   m.x1052 - m.x1271 - m.x1274 == 0)

m.c1968 = Constraint(expr=   m.x1053 - m.x1272 - m.x1275 == 0)

m.c1969 = Constraint(expr=   m.x1054 - m.x1273 - m.x1276 == 0)

m.c1970 = Constraint(expr=   m.x1079 - m.x1325 - m.x1328 == 0)

m.c1971 = Constraint(expr=   m.x1080 - m.x1326 - m.x1329 == 0)

m.c1972 = Constraint(expr=   m.x1081 - m.x1327 - m.x1330 == 0)

m.c1973 = Constraint(expr=   m.x1271 - 9*m.b1397 <= 0)

m.c1974 = Constraint(expr=   m.x1272 - 9*m.b1398 <= 0)

m.c1975 = Constraint(expr=   m.x1273 - 9*m.b1399 <= 0)

m.c1976 = Constraint(expr=   m.x1274 + 9*m.b1397 <= 9)

m.c1977 = Constraint(expr=   m.x1275 + 9*m.b1398 <= 9)

m.c1978 = Constraint(expr=   m.x1276 + 9*m.b1399 <= 9)

m.c1979 = Constraint(expr=   m.x1325 - 9*m.b1397 <= 0)

m.c1980 = Constraint(expr=   m.x1326 - 9*m.b1398 <= 0)

m.c1981 = Constraint(expr=   m.x1327 - 9*m.b1399 <= 0)

m.c1982 = Constraint(expr=   m.x1328 + 9*m.b1397 <= 9)

m.c1983 = Constraint(expr=   m.x1329 + 9*m.b1398 <= 9)

m.c1984 = Constraint(expr=   m.x1330 + 9*m.b1399 <= 9)

m.c1985 = Constraint(expr=(m.x1331/(0.001 + 0.999*m.b1400) - 0.75*log(1 + m.x1277/(0.001 + 0.999*m.b1400)))*(0.001 + 
                          0.999*m.b1400) <= 0)

m.c1986 = Constraint(expr=(m.x1332/(0.001 + 0.999*m.b1401) - 0.75*log(1 + m.x1278/(0.001 + 0.999*m.b1401)))*(0.001 + 
                          0.999*m.b1401) <= 0)

m.c1987 = Constraint(expr=(m.x1333/(0.001 + 0.999*m.b1402) - 0.75*log(1 + m.x1279/(0.001 + 0.999*m.b1402)))*(0.001 + 
                          0.999*m.b1402) <= 0)

m.c1988 = Constraint(expr=   m.x1280 == 0)

m.c1989 = Constraint(expr=   m.x1281 == 0)

m.c1990 = Constraint(expr=   m.x1282 == 0)

m.c1991 = Constraint(expr=   m.x1334 == 0)

m.c1992 = Constraint(expr=   m.x1335 == 0)

m.c1993 = Constraint(expr=   m.x1336 == 0)

m.c1994 = Constraint(expr=   m.x1055 - m.x1277 - m.x1280 == 0)

m.c1995 = Constraint(expr=   m.x1056 - m.x1278 - m.x1281 == 0)

m.c1996 = Constraint(expr=   m.x1057 - m.x1279 - m.x1282 == 0)

m.c1997 = Constraint(expr=   m.x1082 - m.x1331 - m.x1334 == 0)

m.c1998 = Constraint(expr=   m.x1083 - m.x1332 - m.x1335 == 0)

m.c1999 = Constraint(expr=   m.x1084 - m.x1333 - m.x1336 == 0)

m.c2000 = Constraint(expr=   m.x1277 - 3.04984759446376*m.b1400 <= 0)

m.c2001 = Constraint(expr=   m.x1278 - 3.04984759446376*m.b1401 <= 0)

m.c2002 = Constraint(expr=   m.x1279 - 3.04984759446376*m.b1402 <= 0)

m.c2003 = Constraint(expr=   m.x1280 + 3.04984759446376*m.b1400 <= 3.04984759446376)

m.c2004 = Constraint(expr=   m.x1281 + 3.04984759446376*m.b1401 <= 3.04984759446376)

m.c2005 = Constraint(expr=   m.x1282 + 3.04984759446376*m.b1402 <= 3.04984759446376)

m.c2006 = Constraint(expr=   m.x1331 - 1.04900943706034*m.b1400 <= 0)

m.c2007 = Constraint(expr=   m.x1332 - 1.04900943706034*m.b1401 <= 0)

m.c2008 = Constraint(expr=   m.x1333 - 1.04900943706034*m.b1402 <= 0)

m.c2009 = Constraint(expr=   m.x1334 + 1.04900943706034*m.b1400 <= 1.04900943706034)

m.c2010 = Constraint(expr=   m.x1335 + 1.04900943706034*m.b1401 <= 1.04900943706034)

m.c2011 = Constraint(expr=   m.x1336 + 1.04900943706034*m.b1402 <= 1.04900943706034)

m.c2012 = Constraint(expr=(m.x1337/(0.001 + 0.999*m.b1403) - 0.8*log(1 + m.x1283/(0.001 + 0.999*m.b1403)))*(0.001 + 
                          0.999*m.b1403) <= 0)

m.c2013 = Constraint(expr=(m.x1338/(0.001 + 0.999*m.b1404) - 0.8*log(1 + m.x1284/(0.001 + 0.999*m.b1404)))*(0.001 + 
                          0.999*m.b1404) <= 0)

m.c2014 = Constraint(expr=(m.x1339/(0.001 + 0.999*m.b1405) - 0.8*log(1 + m.x1285/(0.001 + 0.999*m.b1405)))*(0.001 + 
                          0.999*m.b1405) <= 0)

m.c2015 = Constraint(expr=   m.x1286 == 0)

m.c2016 = Constraint(expr=   m.x1287 == 0)

m.c2017 = Constraint(expr=   m.x1288 == 0)

m.c2018 = Constraint(expr=   m.x1340 == 0)

m.c2019 = Constraint(expr=   m.x1341 == 0)

m.c2020 = Constraint(expr=   m.x1342 == 0)

m.c2021 = Constraint(expr=   m.x1058 - m.x1283 - m.x1286 == 0)

m.c2022 = Constraint(expr=   m.x1059 - m.x1284 - m.x1287 == 0)

m.c2023 = Constraint(expr=   m.x1060 - m.x1285 - m.x1288 == 0)

m.c2024 = Constraint(expr=   m.x1085 - m.x1337 - m.x1340 == 0)

m.c2025 = Constraint(expr=   m.x1086 - m.x1338 - m.x1341 == 0)

m.c2026 = Constraint(expr=   m.x1087 - m.x1339 - m.x1342 == 0)

m.c2027 = Constraint(expr=   m.x1283 - 3.04984759446376*m.b1403 <= 0)

m.c2028 = Constraint(expr=   m.x1284 - 3.04984759446376*m.b1404 <= 0)

m.c2029 = Constraint(expr=   m.x1285 - 3.04984759446376*m.b1405 <= 0)

m.c2030 = Constraint(expr=   m.x1286 + 3.04984759446376*m.b1403 <= 3.04984759446376)

m.c2031 = Constraint(expr=   m.x1287 + 3.04984759446376*m.b1404 <= 3.04984759446376)

m.c2032 = Constraint(expr=   m.x1288 + 3.04984759446376*m.b1405 <= 3.04984759446376)

m.c2033 = Constraint(expr=   m.x1337 - 1.11894339953103*m.b1403 <= 0)

m.c2034 = Constraint(expr=   m.x1338 - 1.11894339953103*m.b1404 <= 0)

m.c2035 = Constraint(expr=   m.x1339 - 1.11894339953103*m.b1405 <= 0)

m.c2036 = Constraint(expr=   m.x1340 + 1.11894339953103*m.b1403 <= 1.11894339953103)

m.c2037 = Constraint(expr=   m.x1341 + 1.11894339953103*m.b1404 <= 1.11894339953103)

m.c2038 = Constraint(expr=   m.x1342 + 1.11894339953103*m.b1405 <= 1.11894339953103)

m.c2039 = Constraint(expr=(m.x1343/(0.001 + 0.999*m.b1406) - 0.85*log(1 + m.x1289/(0.001 + 0.999*m.b1406)))*(0.001 + 
                          0.999*m.b1406) <= 0)

m.c2040 = Constraint(expr=(m.x1344/(0.001 + 0.999*m.b1407) - 0.85*log(1 + m.x1290/(0.001 + 0.999*m.b1407)))*(0.001 + 
                          0.999*m.b1407) <= 0)

m.c2041 = Constraint(expr=(m.x1345/(0.001 + 0.999*m.b1408) - 0.85*log(1 + m.x1291/(0.001 + 0.999*m.b1408)))*(0.001 + 
                          0.999*m.b1408) <= 0)

m.c2042 = Constraint(expr=   m.x1292 == 0)

m.c2043 = Constraint(expr=   m.x1293 == 0)

m.c2044 = Constraint(expr=   m.x1294 == 0)

m.c2045 = Constraint(expr=   m.x1346 == 0)

m.c2046 = Constraint(expr=   m.x1347 == 0)

m.c2047 = Constraint(expr=   m.x1348 == 0)

m.c2048 = Constraint(expr=   m.x1061 - m.x1289 - m.x1292 == 0)

m.c2049 = Constraint(expr=   m.x1062 - m.x1290 - m.x1293 == 0)

m.c2050 = Constraint(expr=   m.x1063 - m.x1291 - m.x1294 == 0)

m.c2051 = Constraint(expr=   m.x1088 - m.x1343 - m.x1346 == 0)

m.c2052 = Constraint(expr=   m.x1089 - m.x1344 - m.x1347 == 0)

m.c2053 = Constraint(expr=   m.x1090 - m.x1345 - m.x1348 == 0)

m.c2054 = Constraint(expr=   m.x1289 - 3.04984759446376*m.b1406 <= 0)

m.c2055 = Constraint(expr=   m.x1290 - 3.04984759446376*m.b1407 <= 0)

m.c2056 = Constraint(expr=   m.x1291 - 3.04984759446376*m.b1408 <= 0)

m.c2057 = Constraint(expr=   m.x1292 + 3.04984759446376*m.b1406 <= 3.04984759446376)

m.c2058 = Constraint(expr=   m.x1293 + 3.04984759446376*m.b1407 <= 3.04984759446376)

m.c2059 = Constraint(expr=   m.x1294 + 3.04984759446376*m.b1408 <= 3.04984759446376)

m.c2060 = Constraint(expr=   m.x1343 - 1.18887736200171*m.b1406 <= 0)

m.c2061 = Constraint(expr=   m.x1344 - 1.18887736200171*m.b1407 <= 0)

m.c2062 = Constraint(expr=   m.x1345 - 1.18887736200171*m.b1408 <= 0)

m.c2063 = Constraint(expr=   m.x1346 + 1.18887736200171*m.b1406 <= 1.18887736200171)

m.c2064 = Constraint(expr=   m.x1347 + 1.18887736200171*m.b1407 <= 1.18887736200171)

m.c2065 = Constraint(expr=   m.x1348 + 1.18887736200171*m.b1408 <= 1.18887736200171)

m.c2066 = Constraint(expr=   m.x704 + 5*m.b1409 == 0)

m.c2067 = Constraint(expr=   m.x705 + 4*m.b1410 == 0)

m.c2068 = Constraint(expr=   m.x706 + 6*m.b1411 == 0)

m.c2069 = Constraint(expr=   m.x707 + 8*m.b1412 == 0)

m.c2070 = Constraint(expr=   m.x708 + 7*m.b1413 == 0)

m.c2071 = Constraint(expr=   m.x709 + 6*m.b1414 == 0)

m.c2072 = Constraint(expr=   m.x710 + 6*m.b1415 == 0)

m.c2073 = Constraint(expr=   m.x711 + 9*m.b1416 == 0)

m.c2074 = Constraint(expr=   m.x712 + 4*m.b1417 == 0)

m.c2075 = Constraint(expr=   m.x713 + 10*m.b1418 == 0)

m.c2076 = Constraint(expr=   m.x714 + 9*m.b1419 == 0)

m.c2077 = Constraint(expr=   m.x715 + 5*m.b1420 == 0)

m.c2078 = Constraint(expr=   m.x716 + 6*m.b1421 == 0)

m.c2079 = Constraint(expr=   m.x717 + 10*m.b1422 == 0)

m.c2080 = Constraint(expr=   m.x718 + 6*m.b1423 == 0)

m.c2081 = Constraint(expr=   m.x719 + 7*m.b1424 == 0)

m.c2082 = Constraint(expr=   m.x720 + 7*m.b1425 == 0)

m.c2083 = Constraint(expr=   m.x721 + 4*m.b1426 == 0)

m.c2084 = Constraint(expr=   m.x722 + 4*m.b1427 == 0)

m.c2085 = Constraint(expr=   m.x723 + 3*m.b1428 == 0)

m.c2086 = Constraint(expr=   m.x724 + 2*m.b1429 == 0)

m.c2087 = Constraint(expr=   m.x725 + 5*m.b1430 == 0)

m.c2088 = Constraint(expr=   m.x726 + 6*m.b1431 == 0)

m.c2089 = Constraint(expr=   m.x727 + 7*m.b1432 == 0)

m.c2090 = Constraint(expr=   m.x728 + 2*m.b1433 == 0)

m.c2091 = Constraint(expr=   m.x729 + 5*m.b1434 == 0)

m.c2092 = Constraint(expr=   m.x730 + 2*m.b1435 == 0)

m.c2093 = Constraint(expr=   m.x731 + 4*m.b1436 == 0)

m.c2094 = Constraint(expr=   m.x732 + 7*m.b1437 == 0)

m.c2095 = Constraint(expr=   m.x733 + 4*m.b1438 == 0)

m.c2096 = Constraint(expr=   m.x734 + 3*m.b1439 == 0)

m.c2097 = Constraint(expr=   m.x735 + 9*m.b1440 == 0)

m.c2098 = Constraint(expr=   m.x736 + 3*m.b1441 == 0)

m.c2099 = Constraint(expr=   m.x737 + 7*m.b1442 == 0)

m.c2100 = Constraint(expr=   m.x738 + 2*m.b1443 == 0)

m.c2101 = Constraint(expr=   m.x739 + 9*m.b1444 == 0)

m.c2102 = Constraint(expr=   m.x740 + 3*m.b1445 == 0)

m.c2103 = Constraint(expr=   m.x741 + m.b1446 == 0)

m.c2104 = Constraint(expr=   m.x742 + 9*m.b1447 == 0)

m.c2105 = Constraint(expr=   m.x743 + 2*m.b1448 == 0)

m.c2106 = Constraint(expr=   m.x744 + 6*m.b1449 == 0)

m.c2107 = Constraint(expr=   m.x745 + 3*m.b1450 == 0)

m.c2108 = Constraint(expr=   m.x746 + 4*m.b1451 == 0)

m.c2109 = Constraint(expr=   m.x747 + 8*m.b1452 == 0)

m.c2110 = Constraint(expr=   m.x748 + m.b1453 == 0)

m.c2111 = Constraint(expr=   m.x749 + 2*m.b1454 == 0)

m.c2112 = Constraint(expr=   m.x750 + 5*m.b1455 == 0)

m.c2113 = Constraint(expr=   m.x751 + 2*m.b1456 == 0)

m.c2114 = Constraint(expr=   m.x752 + 3*m.b1457 == 0)

m.c2115 = Constraint(expr=   m.x753 + 4*m.b1458 == 0)

m.c2116 = Constraint(expr=   m.x754 + 3*m.b1459 == 0)

m.c2117 = Constraint(expr=   m.x755 + 5*m.b1460 == 0)

m.c2118 = Constraint(expr=   m.x756 + 7*m.b1461 == 0)

m.c2119 = Constraint(expr=   m.x757 + 6*m.b1462 == 0)

m.c2120 = Constraint(expr=   m.x758 + 2*m.b1463 == 0)

m.c2121 = Constraint(expr=   m.x759 + 8*m.b1464 == 0)

m.c2122 = Constraint(expr=   m.x760 + 4*m.b1465 == 0)

m.c2123 = Constraint(expr=   m.x761 + m.b1466 == 0)

m.c2124 = Constraint(expr=   m.x762 + 4*m.b1467 == 0)

m.c2125 = Constraint(expr=   m.x763 + m.b1468 == 0)

m.c2126 = Constraint(expr=   m.b1349 - m.b1350 <= 0)

m.c2127 = Constraint(expr=   m.b1349 - m.b1351 <= 0)

m.c2128 = Constraint(expr=   m.b1350 - m.b1351 <= 0)

m.c2129 = Constraint(expr=   m.b1352 - m.b1353 <= 0)

m.c2130 = Constraint(expr=   m.b1352 - m.b1354 <= 0)

m.c2131 = Constraint(expr=   m.b1353 - m.b1354 <= 0)

m.c2132 = Constraint(expr=   m.b1355 - m.b1356 <= 0)

m.c2133 = Constraint(expr=   m.b1355 - m.b1357 <= 0)

m.c2134 = Constraint(expr=   m.b1356 - m.b1357 <= 0)

m.c2135 = Constraint(expr=   m.b1358 - m.b1359 <= 0)

m.c2136 = Constraint(expr=   m.b1358 - m.b1360 <= 0)

m.c2137 = Constraint(expr=   m.b1359 - m.b1360 <= 0)

m.c2138 = Constraint(expr=   m.b1361 - m.b1362 <= 0)

m.c2139 = Constraint(expr=   m.b1361 - m.b1363 <= 0)

m.c2140 = Constraint(expr=   m.b1362 - m.b1363 <= 0)

m.c2141 = Constraint(expr=   m.b1364 - m.b1365 <= 0)

m.c2142 = Constraint(expr=   m.b1364 - m.b1366 <= 0)

m.c2143 = Constraint(expr=   m.b1365 - m.b1366 <= 0)

m.c2144 = Constraint(expr=   m.b1367 - m.b1368 <= 0)

m.c2145 = Constraint(expr=   m.b1367 - m.b1369 <= 0)

m.c2146 = Constraint(expr=   m.b1368 - m.b1369 <= 0)

m.c2147 = Constraint(expr=   m.b1370 - m.b1371 <= 0)

m.c2148 = Constraint(expr=   m.b1370 - m.b1372 <= 0)

m.c2149 = Constraint(expr=   m.b1371 - m.b1372 <= 0)

m.c2150 = Constraint(expr=   m.b1373 - m.b1374 <= 0)

m.c2151 = Constraint(expr=   m.b1373 - m.b1375 <= 0)

m.c2152 = Constraint(expr=   m.b1374 - m.b1375 <= 0)

m.c2153 = Constraint(expr=   m.b1376 - m.b1377 <= 0)

m.c2154 = Constraint(expr=   m.b1376 - m.b1378 <= 0)

m.c2155 = Constraint(expr=   m.b1377 - m.b1378 <= 0)

m.c2156 = Constraint(expr=   m.b1379 - m.b1380 <= 0)

m.c2157 = Constraint(expr=   m.b1379 - m.b1381 <= 0)

m.c2158 = Constraint(expr=   m.b1380 - m.b1381 <= 0)

m.c2159 = Constraint(expr=   m.b1382 - m.b1383 <= 0)

m.c2160 = Constraint(expr=   m.b1382 - m.b1384 <= 0)

m.c2161 = Constraint(expr=   m.b1383 - m.b1384 <= 0)

m.c2162 = Constraint(expr=   m.b1385 - m.b1386 <= 0)

m.c2163 = Constraint(expr=   m.b1385 - m.b1387 <= 0)

m.c2164 = Constraint(expr=   m.b1386 - m.b1387 <= 0)

m.c2165 = Constraint(expr=   m.b1388 - m.b1389 <= 0)

m.c2166 = Constraint(expr=   m.b1388 - m.b1390 <= 0)

m.c2167 = Constraint(expr=   m.b1389 - m.b1390 <= 0)

m.c2168 = Constraint(expr=   m.b1391 - m.b1392 <= 0)

m.c2169 = Constraint(expr=   m.b1391 - m.b1393 <= 0)

m.c2170 = Constraint(expr=   m.b1392 - m.b1393 <= 0)

m.c2171 = Constraint(expr=   m.b1394 - m.b1395 <= 0)

m.c2172 = Constraint(expr=   m.b1394 - m.b1396 <= 0)

m.c2173 = Constraint(expr=   m.b1395 - m.b1396 <= 0)

m.c2174 = Constraint(expr=   m.b1397 - m.b1398 <= 0)

m.c2175 = Constraint(expr=   m.b1397 - m.b1399 <= 0)

m.c2176 = Constraint(expr=   m.b1398 - m.b1399 <= 0)

m.c2177 = Constraint(expr=   m.b1400 - m.b1401 <= 0)

m.c2178 = Constraint(expr=   m.b1400 - m.b1402 <= 0)

m.c2179 = Constraint(expr=   m.b1401 - m.b1402 <= 0)

m.c2180 = Constraint(expr=   m.b1403 - m.b1404 <= 0)

m.c2181 = Constraint(expr=   m.b1403 - m.b1405 <= 0)

m.c2182 = Constraint(expr=   m.b1404 - m.b1405 <= 0)

m.c2183 = Constraint(expr=   m.b1406 - m.b1407 <= 0)

m.c2184 = Constraint(expr=   m.b1406 - m.b1408 <= 0)

m.c2185 = Constraint(expr=   m.b1407 - m.b1408 <= 0)

m.c2186 = Constraint(expr=   m.b1409 + m.b1410 <= 1)

m.c2187 = Constraint(expr=   m.b1409 + m.b1411 <= 1)

m.c2188 = Constraint(expr=   m.b1409 + m.b1410 <= 1)

m.c2189 = Constraint(expr=   m.b1410 + m.b1411 <= 1)

m.c2190 = Constraint(expr=   m.b1409 + m.b1411 <= 1)

m.c2191 = Constraint(expr=   m.b1410 + m.b1411 <= 1)

m.c2192 = Constraint(expr=   m.b1412 + m.b1413 <= 1)

m.c2193 = Constraint(expr=   m.b1412 + m.b1414 <= 1)

m.c2194 = Constraint(expr=   m.b1412 + m.b1413 <= 1)

m.c2195 = Constraint(expr=   m.b1413 + m.b1414 <= 1)

m.c2196 = Constraint(expr=   m.b1412 + m.b1414 <= 1)

m.c2197 = Constraint(expr=   m.b1413 + m.b1414 <= 1)

m.c2198 = Constraint(expr=   m.b1415 + m.b1416 <= 1)

m.c2199 = Constraint(expr=   m.b1415 + m.b1417 <= 1)

m.c2200 = Constraint(expr=   m.b1415 + m.b1416 <= 1)

m.c2201 = Constraint(expr=   m.b1416 + m.b1417 <= 1)

m.c2202 = Constraint(expr=   m.b1415 + m.b1417 <= 1)

m.c2203 = Constraint(expr=   m.b1416 + m.b1417 <= 1)

m.c2204 = Constraint(expr=   m.b1418 + m.b1419 <= 1)

m.c2205 = Constraint(expr=   m.b1418 + m.b1420 <= 1)

m.c2206 = Constraint(expr=   m.b1418 + m.b1419 <= 1)

m.c2207 = Constraint(expr=   m.b1419 + m.b1420 <= 1)

m.c2208 = Constraint(expr=   m.b1418 + m.b1420 <= 1)

m.c2209 = Constraint(expr=   m.b1419 + m.b1420 <= 1)

m.c2210 = Constraint(expr=   m.b1421 + m.b1422 <= 1)

m.c2211 = Constraint(expr=   m.b1421 + m.b1423 <= 1)

m.c2212 = Constraint(expr=   m.b1421 + m.b1422 <= 1)

m.c2213 = Constraint(expr=   m.b1422 + m.b1423 <= 1)

m.c2214 = Constraint(expr=   m.b1421 + m.b1423 <= 1)

m.c2215 = Constraint(expr=   m.b1422 + m.b1423 <= 1)

m.c2216 = Constraint(expr=   m.b1424 + m.b1425 <= 1)

m.c2217 = Constraint(expr=   m.b1424 + m.b1426 <= 1)

m.c2218 = Constraint(expr=   m.b1424 + m.b1425 <= 1)

m.c2219 = Constraint(expr=   m.b1425 + m.b1426 <= 1)

m.c2220 = Constraint(expr=   m.b1424 + m.b1426 <= 1)

m.c2221 = Constraint(expr=   m.b1425 + m.b1426 <= 1)

m.c2222 = Constraint(expr=   m.b1427 + m.b1428 <= 1)

m.c2223 = Constraint(expr=   m.b1427 + m.b1429 <= 1)

m.c2224 = Constraint(expr=   m.b1427 + m.b1428 <= 1)

m.c2225 = Constraint(expr=   m.b1428 + m.b1429 <= 1)

m.c2226 = Constraint(expr=   m.b1427 + m.b1429 <= 1)

m.c2227 = Constraint(expr=   m.b1428 + m.b1429 <= 1)

m.c2228 = Constraint(expr=   m.b1430 + m.b1431 <= 1)

m.c2229 = Constraint(expr=   m.b1430 + m.b1432 <= 1)

m.c2230 = Constraint(expr=   m.b1430 + m.b1431 <= 1)

m.c2231 = Constraint(expr=   m.b1431 + m.b1432 <= 1)

m.c2232 = Constraint(expr=   m.b1430 + m.b1432 <= 1)

m.c2233 = Constraint(expr=   m.b1431 + m.b1432 <= 1)

m.c2234 = Constraint(expr=   m.b1433 + m.b1434 <= 1)

m.c2235 = Constraint(expr=   m.b1433 + m.b1435 <= 1)

m.c2236 = Constraint(expr=   m.b1433 + m.b1434 <= 1)

m.c2237 = Constraint(expr=   m.b1434 + m.b1435 <= 1)

m.c2238 = Constraint(expr=   m.b1433 + m.b1435 <= 1)

m.c2239 = Constraint(expr=   m.b1434 + m.b1435 <= 1)

m.c2240 = Constraint(expr=   m.b1436 + m.b1437 <= 1)

m.c2241 = Constraint(expr=   m.b1436 + m.b1438 <= 1)

m.c2242 = Constraint(expr=   m.b1436 + m.b1437 <= 1)

m.c2243 = Constraint(expr=   m.b1437 + m.b1438 <= 1)

m.c2244 = Constraint(expr=   m.b1436 + m.b1438 <= 1)

m.c2245 = Constraint(expr=   m.b1437 + m.b1438 <= 1)

m.c2246 = Constraint(expr=   m.b1439 + m.b1440 <= 1)

m.c2247 = Constraint(expr=   m.b1439 + m.b1441 <= 1)

m.c2248 = Constraint(expr=   m.b1439 + m.b1440 <= 1)

m.c2249 = Constraint(expr=   m.b1440 + m.b1441 <= 1)

m.c2250 = Constraint(expr=   m.b1439 + m.b1441 <= 1)

m.c2251 = Constraint(expr=   m.b1440 + m.b1441 <= 1)

m.c2252 = Constraint(expr=   m.b1442 + m.b1443 <= 1)

m.c2253 = Constraint(expr=   m.b1442 + m.b1444 <= 1)

m.c2254 = Constraint(expr=   m.b1442 + m.b1443 <= 1)

m.c2255 = Constraint(expr=   m.b1443 + m.b1444 <= 1)

m.c2256 = Constraint(expr=   m.b1442 + m.b1444 <= 1)

m.c2257 = Constraint(expr=   m.b1443 + m.b1444 <= 1)

m.c2258 = Constraint(expr=   m.b1445 + m.b1446 <= 1)

m.c2259 = Constraint(expr=   m.b1445 + m.b1447 <= 1)

m.c2260 = Constraint(expr=   m.b1445 + m.b1446 <= 1)

m.c2261 = Constraint(expr=   m.b1446 + m.b1447 <= 1)

m.c2262 = Constraint(expr=   m.b1445 + m.b1447 <= 1)

m.c2263 = Constraint(expr=   m.b1446 + m.b1447 <= 1)

m.c2264 = Constraint(expr=   m.b1448 + m.b1449 <= 1)

m.c2265 = Constraint(expr=   m.b1448 + m.b1450 <= 1)

m.c2266 = Constraint(expr=   m.b1448 + m.b1449 <= 1)

m.c2267 = Constraint(expr=   m.b1449 + m.b1450 <= 1)

m.c2268 = Constraint(expr=   m.b1448 + m.b1450 <= 1)

m.c2269 = Constraint(expr=   m.b1449 + m.b1450 <= 1)

m.c2270 = Constraint(expr=   m.b1451 + m.b1452 <= 1)

m.c2271 = Constraint(expr=   m.b1451 + m.b1453 <= 1)

m.c2272 = Constraint(expr=   m.b1451 + m.b1452 <= 1)

m.c2273 = Constraint(expr=   m.b1452 + m.b1453 <= 1)

m.c2274 = Constraint(expr=   m.b1451 + m.b1453 <= 1)

m.c2275 = Constraint(expr=   m.b1452 + m.b1453 <= 1)

m.c2276 = Constraint(expr=   m.b1454 + m.b1455 <= 1)

m.c2277 = Constraint(expr=   m.b1454 + m.b1456 <= 1)

m.c2278 = Constraint(expr=   m.b1454 + m.b1455 <= 1)

m.c2279 = Constraint(expr=   m.b1455 + m.b1456 <= 1)

m.c2280 = Constraint(expr=   m.b1454 + m.b1456 <= 1)

m.c2281 = Constraint(expr=   m.b1455 + m.b1456 <= 1)

m.c2282 = Constraint(expr=   m.b1457 + m.b1458 <= 1)

m.c2283 = Constraint(expr=   m.b1457 + m.b1459 <= 1)

m.c2284 = Constraint(expr=   m.b1457 + m.b1458 <= 1)

m.c2285 = Constraint(expr=   m.b1458 + m.b1459 <= 1)

m.c2286 = Constraint(expr=   m.b1457 + m.b1459 <= 1)

m.c2287 = Constraint(expr=   m.b1458 + m.b1459 <= 1)

m.c2288 = Constraint(expr=   m.b1460 + m.b1461 <= 1)

m.c2289 = Constraint(expr=   m.b1460 + m.b1462 <= 1)

m.c2290 = Constraint(expr=   m.b1460 + m.b1461 <= 1)

m.c2291 = Constraint(expr=   m.b1461 + m.b1462 <= 1)

m.c2292 = Constraint(expr=   m.b1460 + m.b1462 <= 1)

m.c2293 = Constraint(expr=   m.b1461 + m.b1462 <= 1)

m.c2294 = Constraint(expr=   m.b1463 + m.b1464 <= 1)

m.c2295 = Constraint(expr=   m.b1463 + m.b1465 <= 1)

m.c2296 = Constraint(expr=   m.b1463 + m.b1464 <= 1)

m.c2297 = Constraint(expr=   m.b1464 + m.b1465 <= 1)

m.c2298 = Constraint(expr=   m.b1463 + m.b1465 <= 1)

m.c2299 = Constraint(expr=   m.b1464 + m.b1465 <= 1)

m.c2300 = Constraint(expr=   m.b1466 + m.b1467 <= 1)

m.c2301 = Constraint(expr=   m.b1466 + m.b1468 <= 1)

m.c2302 = Constraint(expr=   m.b1466 + m.b1467 <= 1)

m.c2303 = Constraint(expr=   m.b1467 + m.b1468 <= 1)

m.c2304 = Constraint(expr=   m.b1466 + m.b1468 <= 1)

m.c2305 = Constraint(expr=   m.b1467 + m.b1468 <= 1)

m.c2306 = Constraint(expr=   m.b1349 - m.b1409 <= 0)

m.c2307 = Constraint(expr= - m.b1349 + m.b1350 - m.b1410 <= 0)

m.c2308 = Constraint(expr= - m.b1349 - m.b1350 + m.b1351 - m.b1411 <= 0)

m.c2309 = Constraint(expr=   m.b1352 - m.b1412 <= 0)

m.c2310 = Constraint(expr= - m.b1352 + m.b1353 - m.b1413 <= 0)

m.c2311 = Constraint(expr= - m.b1352 - m.b1353 + m.b1354 - m.b1414 <= 0)

m.c2312 = Constraint(expr=   m.b1355 - m.b1415 <= 0)

m.c2313 = Constraint(expr= - m.b1355 + m.b1356 - m.b1416 <= 0)

m.c2314 = Constraint(expr= - m.b1355 - m.b1356 + m.b1357 - m.b1417 <= 0)

m.c2315 = Constraint(expr=   m.b1358 - m.b1418 <= 0)

m.c2316 = Constraint(expr= - m.b1358 + m.b1359 - m.b1419 <= 0)

m.c2317 = Constraint(expr= - m.b1358 - m.b1359 + m.b1360 - m.b1420 <= 0)

m.c2318 = Constraint(expr=   m.b1361 - m.b1421 <= 0)

m.c2319 = Constraint(expr= - m.b1361 + m.b1362 - m.b1422 <= 0)

m.c2320 = Constraint(expr= - m.b1361 - m.b1362 + m.b1363 - m.b1423 <= 0)

m.c2321 = Constraint(expr=   m.b1364 - m.b1424 <= 0)

m.c2322 = Constraint(expr= - m.b1364 + m.b1365 - m.b1425 <= 0)

m.c2323 = Constraint(expr= - m.b1364 - m.b1365 + m.b1366 - m.b1426 <= 0)

m.c2324 = Constraint(expr=   m.b1367 - m.b1427 <= 0)

m.c2325 = Constraint(expr= - m.b1367 + m.b1368 - m.b1428 <= 0)

m.c2326 = Constraint(expr= - m.b1367 - m.b1368 + m.b1369 - m.b1429 <= 0)

m.c2327 = Constraint(expr=   m.b1370 - m.b1430 <= 0)

m.c2328 = Constraint(expr= - m.b1370 + m.b1371 - m.b1431 <= 0)

m.c2329 = Constraint(expr= - m.b1370 - m.b1371 + m.b1372 - m.b1432 <= 0)

m.c2330 = Constraint(expr=   m.b1373 - m.b1433 <= 0)

m.c2331 = Constraint(expr= - m.b1373 + m.b1374 - m.b1434 <= 0)

m.c2332 = Constraint(expr= - m.b1373 - m.b1374 + m.b1375 - m.b1435 <= 0)

m.c2333 = Constraint(expr=   m.b1376 - m.b1436 <= 0)

m.c2334 = Constraint(expr= - m.b1376 + m.b1377 - m.b1437 <= 0)

m.c2335 = Constraint(expr= - m.b1376 - m.b1377 + m.b1378 - m.b1438 <= 0)

m.c2336 = Constraint(expr=   m.b1379 - m.b1439 <= 0)

m.c2337 = Constraint(expr= - m.b1379 + m.b1380 - m.b1440 <= 0)

m.c2338 = Constraint(expr= - m.b1379 - m.b1380 + m.b1381 - m.b1441 <= 0)

m.c2339 = Constraint(expr=   m.b1382 - m.b1442 <= 0)

m.c2340 = Constraint(expr= - m.b1382 + m.b1383 - m.b1443 <= 0)

m.c2341 = Constraint(expr= - m.b1382 - m.b1383 + m.b1384 - m.b1444 <= 0)

m.c2342 = Constraint(expr=   m.b1385 - m.b1445 <= 0)

m.c2343 = Constraint(expr= - m.b1385 + m.b1386 - m.b1446 <= 0)

m.c2344 = Constraint(expr= - m.b1385 - m.b1386 + m.b1387 - m.b1447 <= 0)

m.c2345 = Constraint(expr=   m.b1388 - m.b1448 <= 0)

m.c2346 = Constraint(expr= - m.b1388 + m.b1389 - m.b1449 <= 0)

m.c2347 = Constraint(expr= - m.b1388 - m.b1389 + m.b1390 - m.b1450 <= 0)

m.c2348 = Constraint(expr=   m.b1391 - m.b1451 <= 0)

m.c2349 = Constraint(expr= - m.b1391 + m.b1392 - m.b1452 <= 0)

m.c2350 = Constraint(expr= - m.b1391 - m.b1392 + m.b1393 - m.b1453 <= 0)

m.c2351 = Constraint(expr=   m.b1394 - m.b1454 <= 0)

m.c2352 = Constraint(expr= - m.b1394 + m.b1395 - m.b1455 <= 0)

m.c2353 = Constraint(expr= - m.b1394 - m.b1395 + m.b1396 - m.b1456 <= 0)

m.c2354 = Constraint(expr=   m.b1397 - m.b1457 <= 0)

m.c2355 = Constraint(expr= - m.b1397 + m.b1398 - m.b1458 <= 0)

m.c2356 = Constraint(expr= - m.b1397 - m.b1398 + m.b1399 - m.b1459 <= 0)

m.c2357 = Constraint(expr=   m.b1400 - m.b1460 <= 0)

m.c2358 = Constraint(expr= - m.b1400 + m.b1401 - m.b1461 <= 0)

m.c2359 = Constraint(expr= - m.b1400 - m.b1401 + m.b1402 - m.b1462 <= 0)

m.c2360 = Constraint(expr=   m.b1403 - m.b1463 <= 0)

m.c2361 = Constraint(expr= - m.b1403 + m.b1404 - m.b1464 <= 0)

m.c2362 = Constraint(expr= - m.b1403 - m.b1404 + m.b1405 - m.b1465 <= 0)

m.c2363 = Constraint(expr=   m.b1406 - m.b1466 <= 0)

m.c2364 = Constraint(expr= - m.b1406 + m.b1407 - m.b1467 <= 0)

m.c2365 = Constraint(expr= - m.b1406 - m.b1407 + m.b1408 - m.b1468 <= 0)

m.c2366 = Constraint(expr=   m.b1349 + m.b1352 == 1)

m.c2367 = Constraint(expr=   m.b1350 + m.b1353 == 1)

m.c2368 = Constraint(expr=   m.b1351 + m.b1354 == 1)

m.c2369 = Constraint(expr= - m.b1355 + m.b1364 + m.b1367 >= 0)

m.c2370 = Constraint(expr= - m.b1356 + m.b1365 + m.b1368 >= 0)

m.c2371 = Constraint(expr= - m.b1357 + m.b1366 + m.b1369 >= 0)

m.c2372 = Constraint(expr= - m.b1364 + m.b1382 >= 0)

m.c2373 = Constraint(expr= - m.b1365 + m.b1383 >= 0)

m.c2374 = Constraint(expr= - m.b1366 + m.b1384 >= 0)

m.c2375 = Constraint(expr= - m.b1367 + m.b1385 >= 0)

m.c2376 = Constraint(expr= - m.b1368 + m.b1386 >= 0)

m.c2377 = Constraint(expr= - m.b1369 + m.b1387 >= 0)

m.c2378 = Constraint(expr= - m.b1358 + m.b1370 >= 0)

m.c2379 = Constraint(expr= - m.b1359 + m.b1371 >= 0)

m.c2380 = Constraint(expr= - m.b1360 + m.b1372 >= 0)

m.c2381 = Constraint(expr= - m.b1370 + m.b1388 + m.b1391 >= 0)

m.c2382 = Constraint(expr= - m.b1371 + m.b1389 + m.b1392 >= 0)

m.c2383 = Constraint(expr= - m.b1372 + m.b1390 + m.b1393 >= 0)

m.c2384 = Constraint(expr= - m.b1361 + m.b1373 + m.b1376 + m.b1379 >= 0)

m.c2385 = Constraint(expr= - m.b1362 + m.b1374 + m.b1377 + m.b1380 >= 0)

m.c2386 = Constraint(expr= - m.b1363 + m.b1375 + m.b1378 + m.b1381 >= 0)

m.c2387 = Constraint(expr= - m.b1373 + m.b1391 >= 0)

m.c2388 = Constraint(expr= - m.b1374 + m.b1392 >= 0)

m.c2389 = Constraint(expr= - m.b1375 + m.b1393 >= 0)

m.c2390 = Constraint(expr= - m.b1376 + m.b1394 + m.b1397 >= 0)

m.c2391 = Constraint(expr= - m.b1377 + m.b1395 + m.b1398 >= 0)

m.c2392 = Constraint(expr= - m.b1378 + m.b1396 + m.b1399 >= 0)

m.c2393 = Constraint(expr= - m.b1379 + m.b1400 + m.b1403 + m.b1406 >= 0)

m.c2394 = Constraint(expr= - m.b1380 + m.b1401 + m.b1404 + m.b1407 >= 0)

m.c2395 = Constraint(expr= - m.b1381 + m.b1402 + m.b1405 + m.b1408 >= 0)

m.c2396 = Constraint(expr=   m.b1349 + m.b1352 - m.b1355 >= 0)

m.c2397 = Constraint(expr=   m.b1350 + m.b1353 - m.b1356 >= 0)

m.c2398 = Constraint(expr=   m.b1351 + m.b1354 - m.b1357 >= 0)

m.c2399 = Constraint(expr=   m.b1349 + m.b1352 - m.b1358 >= 0)

m.c2400 = Constraint(expr=   m.b1350 + m.b1353 - m.b1359 >= 0)

m.c2401 = Constraint(expr=   m.b1351 + m.b1354 - m.b1360 >= 0)

m.c2402 = Constraint(expr=   m.b1349 + m.b1352 - m.b1361 >= 0)

m.c2403 = Constraint(expr=   m.b1350 + m.b1353 - m.b1362 >= 0)

m.c2404 = Constraint(expr=   m.b1351 + m.b1354 - m.b1363 >= 0)

m.c2405 = Constraint(expr=   m.b1355 - m.b1364 >= 0)

m.c2406 = Constraint(expr=   m.b1356 - m.b1365 >= 0)

m.c2407 = Constraint(expr=   m.b1357 - m.b1366 >= 0)

m.c2408 = Constraint(expr=   m.b1355 - m.b1367 >= 0)

m.c2409 = Constraint(expr=   m.b1356 - m.b1368 >= 0)

m.c2410 = Constraint(expr=   m.b1357 - m.b1369 >= 0)

m.c2411 = Constraint(expr=   m.b1358 - m.b1370 >= 0)

m.c2412 = Constraint(expr=   m.b1359 - m.b1371 >= 0)

m.c2413 = Constraint(expr=   m.b1360 - m.b1372 >= 0)

m.c2414 = Constraint(expr=   m.b1361 - m.b1373 >= 0)

m.c2415 = Constraint(expr=   m.b1362 - m.b1374 >= 0)

m.c2416 = Constraint(expr=   m.b1363 - m.b1375 >= 0)

m.c2417 = Constraint(expr=   m.b1361 - m.b1376 >= 0)

m.c2418 = Constraint(expr=   m.b1362 - m.b1377 >= 0)

m.c2419 = Constraint(expr=   m.b1363 - m.b1378 >= 0)

m.c2420 = Constraint(expr=   m.b1361 - m.b1379 >= 0)

m.c2421 = Constraint(expr=   m.b1362 - m.b1380 >= 0)

m.c2422 = Constraint(expr=   m.b1363 - m.b1381 >= 0)

m.c2423 = Constraint(expr=   m.b1364 - m.b1382 >= 0)

m.c2424 = Constraint(expr=   m.b1365 - m.b1383 >= 0)

m.c2425 = Constraint(expr=   m.b1366 - m.b1384 >= 0)

m.c2426 = Constraint(expr=   m.b1367 - m.b1385 >= 0)

m.c2427 = Constraint(expr=   m.b1368 - m.b1386 >= 0)

m.c2428 = Constraint(expr=   m.b1369 - m.b1387 >= 0)

m.c2429 = Constraint(expr=   m.b1370 - m.b1388 >= 0)

m.c2430 = Constraint(expr=   m.b1371 - m.b1389 >= 0)

m.c2431 = Constraint(expr=   m.b1372 - m.b1390 >= 0)

m.c2432 = Constraint(expr=   m.b1370 - m.b1391 >= 0)

m.c2433 = Constraint(expr=   m.b1371 - m.b1392 >= 0)

m.c2434 = Constraint(expr=   m.b1372 - m.b1393 >= 0)

m.c2435 = Constraint(expr=   m.b1376 - m.b1394 >= 0)

m.c2436 = Constraint(expr=   m.b1377 - m.b1395 >= 0)

m.c2437 = Constraint(expr=   m.b1378 - m.b1396 >= 0)

m.c2438 = Constraint(expr=   m.b1376 - m.b1397 >= 0)

m.c2439 = Constraint(expr=   m.b1377 - m.b1398 >= 0)

m.c2440 = Constraint(expr=   m.b1378 - m.b1399 >= 0)

m.c2441 = Constraint(expr=   m.b1379 - m.b1400 >= 0)

m.c2442 = Constraint(expr=   m.b1380 - m.b1401 >= 0)

m.c2443 = Constraint(expr=   m.b1381 - m.b1402 >= 0)

m.c2444 = Constraint(expr=   m.b1379 - m.b1403 >= 0)

m.c2445 = Constraint(expr=   m.b1380 - m.b1404 >= 0)

m.c2446 = Constraint(expr=   m.b1381 - m.b1405 >= 0)

m.c2447 = Constraint(expr=   m.b1379 - m.b1406 >= 0)

m.c2448 = Constraint(expr=   m.b1380 - m.b1407 >= 0)

m.c2449 = Constraint(expr=   m.b1381 - m.b1408 >= 0)
