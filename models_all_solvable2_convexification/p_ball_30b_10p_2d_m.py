# MINLP written by GAMS Convert at 05/07/21 17:13:00
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       529       10        0      519        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       410      110      300        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      2058     1458      600
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
m.b256 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b257 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b258 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b259 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b260 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b261 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b262 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b263 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b264 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b265 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b266 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b267 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b268 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b269 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b270 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b271 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b272 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b273 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b274 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b275 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b276 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b277 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b278 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b279 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b280 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b281 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b282 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b283 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b284 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b285 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b286 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b287 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b288 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b289 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b290 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b291 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b292 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b293 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b294 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b295 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b296 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b297 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b298 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b299 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b300 = Var(within=Binary, bounds=(0,1), initialize=0)
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
m.x365 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x366 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x367 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x368 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x369 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x370 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x371 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x372 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x373 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x374 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x375 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x376 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x377 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x378 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x379 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x380 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x381 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x382 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x383 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x384 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x385 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x386 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x387 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x388 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x389 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x390 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x391 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x392 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x393 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x394 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x395 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x396 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x397 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x398 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x399 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x400 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x401 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x402 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x403 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x404 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x405 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x406 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x407 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x408 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x409 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x410 = Var(within=Reals, bounds=(0,10), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x303 + m.x306 + m.x308 + m.x310 +
    m.x312 + m.x314 + m.x316 + m.x318 + m.x320 + m.x322 + m.x324 + m.x326 +
    m.x328 + m.x330 + m.x332 + m.x334 + m.x336 + m.x338 + m.x339 + m.x340 +
    m.x341 + m.x342 + m.x343 + m.x344 + m.x345 + m.x346 + m.x347 + m.x348 +
    m.x349 + m.x350 + m.x351 + m.x352 + m.x353 + m.x354 + m.x355 + m.x356 +
    m.x357 + m.x358 + m.x359 + m.x360 + m.x361 + m.x362 + m.x363 + m.x364 +
    m.x365 + m.x366 + m.x367 + m.x368 + m.x369 + m.x370 + m.x371 + m.x372 +
    m.x373 + m.x374 + m.x375 + m.x376 + m.x377 + m.x378 + m.x379 + m.x380 +
    m.x381 + m.x382 + m.x383 + m.x384 + m.x385 + m.x386 + m.x387 + m.x388 +
    m.x389 + m.x390 + m.x391 + m.x392 + m.x393 + m.x394 + m.x395 + m.x396 +
    m.x397 + m.x398 + m.x399 + m.x400 + m.x401 + m.x402 + m.x403 + m.x404 +
    m.x405 + m.x406 + m.x407 + m.x408 + m.x409 + m.x410)

m.e1 = Constraint(expr= m.x301 - m.x302 - m.x303 <= 0)
m.e2 = Constraint(expr= -m.x301 + m.x302 - m.x303 <= 0)
m.e3 = Constraint(expr= m.x304 - m.x305 - m.x306 <= 0)
m.e4 = Constraint(expr= -m.x304 + m.x305 - m.x306 <= 0)
m.e5 = Constraint(expr= m.x301 - m.x307 - m.x308 <= 0)
m.e6 = Constraint(expr= -m.x301 + m.x307 - m.x308 <= 0)
m.e7 = Constraint(expr= m.x304 - m.x309 - m.x310 <= 0)
m.e8 = Constraint(expr= -m.x304 + m.x309 - m.x310 <= 0)
m.e9 = Constraint(expr= m.x301 - m.x311 - m.x312 <= 0)
m.e10 = Constraint(expr= -m.x301 + m.x311 - m.x312 <= 0)
m.e11 = Constraint(expr= m.x304 - m.x313 - m.x314 <= 0)
m.e12 = Constraint(expr= -m.x304 + m.x313 - m.x314 <= 0)
m.e13 = Constraint(expr= m.x301 - m.x315 - m.x316 <= 0)
m.e14 = Constraint(expr= -m.x301 + m.x315 - m.x316 <= 0)
m.e15 = Constraint(expr= m.x304 - m.x317 - m.x318 <= 0)
m.e16 = Constraint(expr= -m.x304 + m.x317 - m.x318 <= 0)
m.e17 = Constraint(expr= m.x301 - m.x319 - m.x320 <= 0)
m.e18 = Constraint(expr= -m.x301 + m.x319 - m.x320 <= 0)
m.e19 = Constraint(expr= m.x304 - m.x321 - m.x322 <= 0)
m.e20 = Constraint(expr= -m.x304 + m.x321 - m.x322 <= 0)
m.e21 = Constraint(expr= m.x301 - m.x323 - m.x324 <= 0)
m.e22 = Constraint(expr= -m.x301 + m.x323 - m.x324 <= 0)
m.e23 = Constraint(expr= m.x304 - m.x325 - m.x326 <= 0)
m.e24 = Constraint(expr= -m.x304 + m.x325 - m.x326 <= 0)
m.e25 = Constraint(expr= m.x301 - m.x327 - m.x328 <= 0)
m.e26 = Constraint(expr= -m.x301 + m.x327 - m.x328 <= 0)
m.e27 = Constraint(expr= m.x304 - m.x329 - m.x330 <= 0)
m.e28 = Constraint(expr= -m.x304 + m.x329 - m.x330 <= 0)
m.e29 = Constraint(expr= m.x301 - m.x331 - m.x332 <= 0)
m.e30 = Constraint(expr= -m.x301 + m.x331 - m.x332 <= 0)
m.e31 = Constraint(expr= m.x304 - m.x333 - m.x334 <= 0)
m.e32 = Constraint(expr= -m.x304 + m.x333 - m.x334 <= 0)
m.e33 = Constraint(expr= m.x301 - m.x335 - m.x336 <= 0)
m.e34 = Constraint(expr= -m.x301 + m.x335 - m.x336 <= 0)
m.e35 = Constraint(expr= m.x304 - m.x337 - m.x338 <= 0)
m.e36 = Constraint(expr= -m.x304 + m.x337 - m.x338 <= 0)
m.e37 = Constraint(expr= m.x302 - m.x307 - m.x339 <= 0)
m.e38 = Constraint(expr= -m.x302 + m.x307 - m.x339 <= 0)
m.e39 = Constraint(expr= m.x305 - m.x309 - m.x340 <= 0)
m.e40 = Constraint(expr= -m.x305 + m.x309 - m.x340 <= 0)
m.e41 = Constraint(expr= m.x302 - m.x311 - m.x341 <= 0)
m.e42 = Constraint(expr= -m.x302 + m.x311 - m.x341 <= 0)
m.e43 = Constraint(expr= m.x305 - m.x313 - m.x342 <= 0)
m.e44 = Constraint(expr= -m.x305 + m.x313 - m.x342 <= 0)
m.e45 = Constraint(expr= m.x302 - m.x315 - m.x343 <= 0)
m.e46 = Constraint(expr= -m.x302 + m.x315 - m.x343 <= 0)
m.e47 = Constraint(expr= m.x305 - m.x317 - m.x344 <= 0)
m.e48 = Constraint(expr= -m.x305 + m.x317 - m.x344 <= 0)
m.e49 = Constraint(expr= m.x302 - m.x319 - m.x345 <= 0)
m.e50 = Constraint(expr= -m.x302 + m.x319 - m.x345 <= 0)
m.e51 = Constraint(expr= m.x305 - m.x321 - m.x346 <= 0)
m.e52 = Constraint(expr= -m.x305 + m.x321 - m.x346 <= 0)
m.e53 = Constraint(expr= m.x302 - m.x323 - m.x347 <= 0)
m.e54 = Constraint(expr= -m.x302 + m.x323 - m.x347 <= 0)
m.e55 = Constraint(expr= m.x305 - m.x325 - m.x348 <= 0)
m.e56 = Constraint(expr= -m.x305 + m.x325 - m.x348 <= 0)
m.e57 = Constraint(expr= m.x302 - m.x327 - m.x349 <= 0)
m.e58 = Constraint(expr= -m.x302 + m.x327 - m.x349 <= 0)
m.e59 = Constraint(expr= m.x305 - m.x329 - m.x350 <= 0)
m.e60 = Constraint(expr= -m.x305 + m.x329 - m.x350 <= 0)
m.e61 = Constraint(expr= m.x302 - m.x331 - m.x351 <= 0)
m.e62 = Constraint(expr= -m.x302 + m.x331 - m.x351 <= 0)
m.e63 = Constraint(expr= m.x305 - m.x333 - m.x352 <= 0)
m.e64 = Constraint(expr= -m.x305 + m.x333 - m.x352 <= 0)
m.e65 = Constraint(expr= m.x302 - m.x335 - m.x353 <= 0)
m.e66 = Constraint(expr= -m.x302 + m.x335 - m.x353 <= 0)
m.e67 = Constraint(expr= m.x305 - m.x337 - m.x354 <= 0)
m.e68 = Constraint(expr= -m.x305 + m.x337 - m.x354 <= 0)
m.e69 = Constraint(expr= m.x307 - m.x311 - m.x355 <= 0)
m.e70 = Constraint(expr= -m.x307 + m.x311 - m.x355 <= 0)
m.e71 = Constraint(expr= m.x309 - m.x313 - m.x356 <= 0)
m.e72 = Constraint(expr= -m.x309 + m.x313 - m.x356 <= 0)
m.e73 = Constraint(expr= m.x307 - m.x315 - m.x357 <= 0)
m.e74 = Constraint(expr= -m.x307 + m.x315 - m.x357 <= 0)
m.e75 = Constraint(expr= m.x309 - m.x317 - m.x358 <= 0)
m.e76 = Constraint(expr= -m.x309 + m.x317 - m.x358 <= 0)
m.e77 = Constraint(expr= m.x307 - m.x319 - m.x359 <= 0)
m.e78 = Constraint(expr= -m.x307 + m.x319 - m.x359 <= 0)
m.e79 = Constraint(expr= m.x309 - m.x321 - m.x360 <= 0)
m.e80 = Constraint(expr= -m.x309 + m.x321 - m.x360 <= 0)
m.e81 = Constraint(expr= m.x307 - m.x323 - m.x361 <= 0)
m.e82 = Constraint(expr= -m.x307 + m.x323 - m.x361 <= 0)
m.e83 = Constraint(expr= m.x309 - m.x325 - m.x362 <= 0)
m.e84 = Constraint(expr= -m.x309 + m.x325 - m.x362 <= 0)
m.e85 = Constraint(expr= m.x307 - m.x327 - m.x363 <= 0)
m.e86 = Constraint(expr= -m.x307 + m.x327 - m.x363 <= 0)
m.e87 = Constraint(expr= m.x309 - m.x329 - m.x364 <= 0)
m.e88 = Constraint(expr= -m.x309 + m.x329 - m.x364 <= 0)
m.e89 = Constraint(expr= m.x307 - m.x331 - m.x365 <= 0)
m.e90 = Constraint(expr= -m.x307 + m.x331 - m.x365 <= 0)
m.e91 = Constraint(expr= m.x309 - m.x333 - m.x366 <= 0)
m.e92 = Constraint(expr= -m.x309 + m.x333 - m.x366 <= 0)
m.e93 = Constraint(expr= m.x307 - m.x335 - m.x367 <= 0)
m.e94 = Constraint(expr= -m.x307 + m.x335 - m.x367 <= 0)
m.e95 = Constraint(expr= m.x309 - m.x337 - m.x368 <= 0)
m.e96 = Constraint(expr= -m.x309 + m.x337 - m.x368 <= 0)
m.e97 = Constraint(expr= m.x311 - m.x315 - m.x369 <= 0)
m.e98 = Constraint(expr= -m.x311 + m.x315 - m.x369 <= 0)
m.e99 = Constraint(expr= m.x313 - m.x317 - m.x370 <= 0)
m.e100 = Constraint(expr= -m.x313 + m.x317 - m.x370 <= 0)
m.e101 = Constraint(expr= m.x311 - m.x319 - m.x371 <= 0)
m.e102 = Constraint(expr= -m.x311 + m.x319 - m.x371 <= 0)
m.e103 = Constraint(expr= m.x313 - m.x321 - m.x372 <= 0)
m.e104 = Constraint(expr= -m.x313 + m.x321 - m.x372 <= 0)
m.e105 = Constraint(expr= m.x311 - m.x323 - m.x373 <= 0)
m.e106 = Constraint(expr= -m.x311 + m.x323 - m.x373 <= 0)
m.e107 = Constraint(expr= m.x313 - m.x325 - m.x374 <= 0)
m.e108 = Constraint(expr= -m.x313 + m.x325 - m.x374 <= 0)
m.e109 = Constraint(expr= m.x311 - m.x327 - m.x375 <= 0)
m.e110 = Constraint(expr= -m.x311 + m.x327 - m.x375 <= 0)
m.e111 = Constraint(expr= m.x313 - m.x329 - m.x376 <= 0)
m.e112 = Constraint(expr= -m.x313 + m.x329 - m.x376 <= 0)
m.e113 = Constraint(expr= m.x311 - m.x331 - m.x377 <= 0)
m.e114 = Constraint(expr= -m.x311 + m.x331 - m.x377 <= 0)
m.e115 = Constraint(expr= m.x313 - m.x333 - m.x378 <= 0)
m.e116 = Constraint(expr= -m.x313 + m.x333 - m.x378 <= 0)
m.e117 = Constraint(expr= m.x311 - m.x335 - m.x379 <= 0)
m.e118 = Constraint(expr= -m.x311 + m.x335 - m.x379 <= 0)
m.e119 = Constraint(expr= m.x313 - m.x337 - m.x380 <= 0)
m.e120 = Constraint(expr= -m.x313 + m.x337 - m.x380 <= 0)
m.e121 = Constraint(expr= m.x315 - m.x319 - m.x381 <= 0)
m.e122 = Constraint(expr= -m.x315 + m.x319 - m.x381 <= 0)
m.e123 = Constraint(expr= m.x317 - m.x321 - m.x382 <= 0)
m.e124 = Constraint(expr= -m.x317 + m.x321 - m.x382 <= 0)
m.e125 = Constraint(expr= m.x315 - m.x323 - m.x383 <= 0)
m.e126 = Constraint(expr= -m.x315 + m.x323 - m.x383 <= 0)
m.e127 = Constraint(expr= m.x317 - m.x325 - m.x384 <= 0)
m.e128 = Constraint(expr= -m.x317 + m.x325 - m.x384 <= 0)
m.e129 = Constraint(expr= m.x315 - m.x327 - m.x385 <= 0)
m.e130 = Constraint(expr= -m.x315 + m.x327 - m.x385 <= 0)
m.e131 = Constraint(expr= m.x317 - m.x329 - m.x386 <= 0)
m.e132 = Constraint(expr= -m.x317 + m.x329 - m.x386 <= 0)
m.e133 = Constraint(expr= m.x315 - m.x331 - m.x387 <= 0)
m.e134 = Constraint(expr= -m.x315 + m.x331 - m.x387 <= 0)
m.e135 = Constraint(expr= m.x317 - m.x333 - m.x388 <= 0)
m.e136 = Constraint(expr= -m.x317 + m.x333 - m.x388 <= 0)
m.e137 = Constraint(expr= m.x315 - m.x335 - m.x389 <= 0)
m.e138 = Constraint(expr= -m.x315 + m.x335 - m.x389 <= 0)
m.e139 = Constraint(expr= m.x317 - m.x337 - m.x390 <= 0)
m.e140 = Constraint(expr= -m.x317 + m.x337 - m.x390 <= 0)
m.e141 = Constraint(expr= m.x319 - m.x323 - m.x391 <= 0)
m.e142 = Constraint(expr= -m.x319 + m.x323 - m.x391 <= 0)
m.e143 = Constraint(expr= m.x321 - m.x325 - m.x392 <= 0)
m.e144 = Constraint(expr= -m.x321 + m.x325 - m.x392 <= 0)
m.e145 = Constraint(expr= m.x319 - m.x327 - m.x393 <= 0)
m.e146 = Constraint(expr= -m.x319 + m.x327 - m.x393 <= 0)
m.e147 = Constraint(expr= m.x321 - m.x329 - m.x394 <= 0)
m.e148 = Constraint(expr= -m.x321 + m.x329 - m.x394 <= 0)
m.e149 = Constraint(expr= m.x319 - m.x331 - m.x395 <= 0)
m.e150 = Constraint(expr= -m.x319 + m.x331 - m.x395 <= 0)
m.e151 = Constraint(expr= m.x321 - m.x333 - m.x396 <= 0)
m.e152 = Constraint(expr= -m.x321 + m.x333 - m.x396 <= 0)
m.e153 = Constraint(expr= m.x319 - m.x335 - m.x397 <= 0)
m.e154 = Constraint(expr= -m.x319 + m.x335 - m.x397 <= 0)
m.e155 = Constraint(expr= m.x321 - m.x337 - m.x398 <= 0)
m.e156 = Constraint(expr= -m.x321 + m.x337 - m.x398 <= 0)
m.e157 = Constraint(expr= m.x323 - m.x327 - m.x399 <= 0)
m.e158 = Constraint(expr= -m.x323 + m.x327 - m.x399 <= 0)
m.e159 = Constraint(expr= m.x325 - m.x329 - m.x400 <= 0)
m.e160 = Constraint(expr= -m.x325 + m.x329 - m.x400 <= 0)
m.e161 = Constraint(expr= m.x323 - m.x331 - m.x401 <= 0)
m.e162 = Constraint(expr= -m.x323 + m.x331 - m.x401 <= 0)
m.e163 = Constraint(expr= m.x325 - m.x333 - m.x402 <= 0)
m.e164 = Constraint(expr= -m.x325 + m.x333 - m.x402 <= 0)
m.e165 = Constraint(expr= m.x323 - m.x335 - m.x403 <= 0)
m.e166 = Constraint(expr= -m.x323 + m.x335 - m.x403 <= 0)
m.e167 = Constraint(expr= m.x325 - m.x337 - m.x404 <= 0)
m.e168 = Constraint(expr= -m.x325 + m.x337 - m.x404 <= 0)
m.e169 = Constraint(expr= m.x327 - m.x331 - m.x405 <= 0)
m.e170 = Constraint(expr= -m.x327 + m.x331 - m.x405 <= 0)
m.e171 = Constraint(expr= m.x329 - m.x333 - m.x406 <= 0)
m.e172 = Constraint(expr= -m.x329 + m.x333 - m.x406 <= 0)
m.e173 = Constraint(expr= m.x327 - m.x335 - m.x407 <= 0)
m.e174 = Constraint(expr= -m.x327 + m.x335 - m.x407 <= 0)
m.e175 = Constraint(expr= m.x329 - m.x337 - m.x408 <= 0)
m.e176 = Constraint(expr= -m.x329 + m.x337 - m.x408 <= 0)
m.e177 = Constraint(expr= m.x331 - m.x335 - m.x409 <= 0)
m.e178 = Constraint(expr= -m.x331 + m.x335 - m.x409 <= 0)
m.e179 = Constraint(expr= m.x333 - m.x337 - m.x410 <= 0)
m.e180 = Constraint(expr= -m.x333 + m.x337 - m.x410 <= 0)
m.e181 = Constraint(expr= (2.84746945184196 - m.x301)**2 + (6.74779851669768 -
    m.x304)**2 + 67.42707737338 * m.b1 <= 68.42707737338)
m.e182 = Constraint(expr= (6.63261133839597 - m.x301)**2 + (7.58930814907984 -
    m.x304)**2 + 100.27903396698 * m.b2 <= 101.27903396698)
m.e183 = Constraint(expr= (2.78008351564232 - m.x301)**2 + (5.62089512941063 -
    m.x304)**2 + 62.225162895805 * m.b3 <= 63.225162895805)
m.e184 = Constraint(expr= (3.36345404799715 - m.x301)**2 + (5.61693710344635 -
    m.x304)**2 + 54.3423498257743 * m.b4 <= 55.3423498257743)
m.e185 = Constraint(expr= (1.46574263591158 - m.x301)**2 + (0.14249643071642 -
    m.x304)**2 + 153.854418335954 * m.b5 <= 154.854418335954)
m.e186 = Constraint(expr= (6.59824950993792 - m.x301)**2 + (1.91438252349491 -
    m.x304)**2 + 115.729330039997 * m.b6 <= 116.729330039997)
m.e187 = Constraint(expr= (2.02515523263325 - m.x301)**2 + (3.62141731303869 -
    m.x304)**2 + 92.1830734090453 * m.b7 <= 93.1830734090453)
m.e188 = Constraint(expr= (8.97152199819966 - m.x301)**2 + (8.78133845105015 -
    m.x304)**2 + 153.854418335954 * m.b8 <= 154.854418335954)
m.e189 = Constraint(expr= (1.87485423601802 - m.x301)**2 + (8.96274662253461 -
    m.x304)**2 + 106.113667406259 * m.b9 <= 107.113667406259)
m.e190 = Constraint(expr= (7.52025674966412 - m.x301)**2 + (8.80268658264247 -
    m.x304)**2 + 132.789518443852 * m.b10 <= 133.789518443852)
m.e191 = Constraint(expr= (3.85704114235832 - m.x301)**2 + (6.36674450874035 -
    m.x304)**2 + 57.7951750598727 * m.b11 <= 58.7951750598727)
m.e192 = Constraint(expr= (8.48963678940351 - m.x301)**2 + (5.48402210821562 -
    m.x304)**2 + 102.926783859086 * m.b12 <= 103.926783859086)
m.e193 = Constraint(expr= (6.03160481727421 - m.x301)**2 + (1.276552921829 -
    m.x304)**2 + 118.75213232131 * m.b13 <= 119.75213232131)
m.e194 = Constraint(expr= (6.90662266429413 - m.x301)**2 + (8.78931785429954 -
    m.x304)**2 + 124.803091689871 * m.b14 <= 125.803091689871)
m.e195 = Constraint(expr= (3.71078725250056 - m.x301)**2 + (4.66415664133948 -
    m.x304)**2 + 57.9871322900609 * m.b15 <= 58.9871322900609)
m.e196 = Constraint(expr= (0.107239833314705 - m.x301)**2 + (9.26202525440128
    - m.x304)**2 + 141.568883438575 * m.b16 <= 142.568883438575)
m.e197 = Constraint(expr= (8.04739319923014 - m.x301)**2 + (3.59305161391794 -
    m.x304)**2 + 114.695683175902 * m.b17 <= 115.695683175902)
m.e198 = Constraint(expr= (5.28411061001579 - m.x301)**2 + (9.36648183133357 -
    m.x304)**2 + 119.627996085735 * m.b18 <= 120.627996085735)
m.e199 = Constraint(expr= (1.06171481272944 - m.x301)**2 + (3.65844432398946 -
    m.x304)**2 + 107.656809348234 * m.b19 <= 108.656809348234)
m.e200 = Constraint(expr= (9.05099582793631 - m.x301)**2 + (3.98215513024397 -
    m.x304)**2 + 128.639684646565 * m.b20 <= 129.639684646565)
m.e201 = Constraint(expr= (9.08772707393705 - m.x301)**2 + (3.01388234113091 -
    m.x304)**2 + 141.568883438575 * m.b21 <= 142.568883438575)
m.e202 = Constraint(expr= (8.83910845171846 - m.x301)**2 + (8.26686922455514 -
    m.x304)**2 + 142.314787626056 * m.b22 <= 143.314787626056)
m.e203 = Constraint(expr= (3.41090111187451 - m.x301)**2 + (6.48985541572597 -
    m.x304)**2 + 57.6217041967589 * m.b23 <= 58.6217041967589)
m.e204 = Constraint(expr= (1.22004189182266 - m.x301)**2 + (2.52276995748249 -
    m.x304)**2 + 119.180496541755 * m.b24 <= 120.180496541755)
m.e205 = Constraint(expr= (3.94802045665365 - m.x301)**2 + (6.40339456473198 -
    m.x304)**2 + 58.8305966748386 * m.b25 <= 59.8305966748386)
m.e206 = Constraint(expr= (4.9104301706676 - m.x301)**2 + (3.1538945754034 -
    m.x304)**2 + 75.9207984013209 * m.b26 <= 76.9207984013209)
m.e207 = Constraint(expr= (3.23176530143453 - m.x301)**2 + (7.03644502956294 -
    m.x304)**2 + 64.8784745008497 * m.b27 <= 65.8784745008497)
m.e208 = Constraint(expr= (0.39249886515424 - m.x301)**2 + (1.58871179600639 -
    m.x304)**2 + 147.724006608004 * m.b28 <= 148.724006608004)
m.e209 = Constraint(expr= (4.42690021019308 - m.x301)**2 + (8.74244441962606 -
    m.x304)**2 + 100.918497950284 * m.b29 <= 101.918497950284)
m.e210 = Constraint(expr= (2.59382124128511 - m.x301)**2 + (9.98780114819833 -
    m.x304)**2 + 118.022029936783 * m.b30 <= 119.022029936783)
m.e211 = Constraint(expr= m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8
    + m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17 +
    m.b18 + m.b19 + m.b20 + m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 +
    m.b27 + m.b28 + m.b29 + m.b30 == 1)
m.e212 = Constraint(expr= (2.84746945184196 - m.x302)**2 + (6.74779851669768 -
    m.x305)**2 + 67.42707737338 * m.b31 <= 68.42707737338)
m.e213 = Constraint(expr= (6.63261133839597 - m.x302)**2 + (7.58930814907984 -
    m.x305)**2 + 100.27903396698 * m.b32 <= 101.27903396698)
m.e214 = Constraint(expr= (2.78008351564232 - m.x302)**2 + (5.62089512941063 -
    m.x305)**2 + 62.225162895805 * m.b33 <= 63.225162895805)
m.e215 = Constraint(expr= (3.36345404799715 - m.x302)**2 + (5.61693710344635 -
    m.x305)**2 + 54.3423498257743 * m.b34 <= 55.3423498257743)
m.e216 = Constraint(expr= (1.46574263591158 - m.x302)**2 + (0.14249643071642 -
    m.x305)**2 + 153.854418335954 * m.b35 <= 154.854418335954)
m.e217 = Constraint(expr= (6.59824950993792 - m.x302)**2 + (1.91438252349491 -
    m.x305)**2 + 115.729330039997 * m.b36 <= 116.729330039997)
m.e218 = Constraint(expr= (2.02515523263325 - m.x302)**2 + (3.62141731303869 -
    m.x305)**2 + 92.1830734090453 * m.b37 <= 93.1830734090453)
m.e219 = Constraint(expr= (8.97152199819966 - m.x302)**2 + (8.78133845105015 -
    m.x305)**2 + 153.854418335954 * m.b38 <= 154.854418335954)
m.e220 = Constraint(expr= (1.87485423601802 - m.x302)**2 + (8.96274662253461 -
    m.x305)**2 + 106.113667406259 * m.b39 <= 107.113667406259)
m.e221 = Constraint(expr= (7.52025674966412 - m.x302)**2 + (8.80268658264247 -
    m.x305)**2 + 132.789518443852 * m.b40 <= 133.789518443852)
m.e222 = Constraint(expr= (3.85704114235832 - m.x302)**2 + (6.36674450874035 -
    m.x305)**2 + 57.7951750598727 * m.b41 <= 58.7951750598727)
m.e223 = Constraint(expr= (8.48963678940351 - m.x302)**2 + (5.48402210821562 -
    m.x305)**2 + 102.926783859086 * m.b42 <= 103.926783859086)
m.e224 = Constraint(expr= (6.03160481727421 - m.x302)**2 + (1.276552921829 -
    m.x305)**2 + 118.75213232131 * m.b43 <= 119.75213232131)
m.e225 = Constraint(expr= (6.90662266429413 - m.x302)**2 + (8.78931785429954 -
    m.x305)**2 + 124.803091689871 * m.b44 <= 125.803091689871)
m.e226 = Constraint(expr= (3.71078725250056 - m.x302)**2 + (4.66415664133948 -
    m.x305)**2 + 57.9871322900609 * m.b45 <= 58.9871322900609)
m.e227 = Constraint(expr= (0.107239833314705 - m.x302)**2 + (9.26202525440128
    - m.x305)**2 + 141.568883438575 * m.b46 <= 142.568883438575)
m.e228 = Constraint(expr= (8.04739319923014 - m.x302)**2 + (3.59305161391794 -
    m.x305)**2 + 114.695683175902 * m.b47 <= 115.695683175902)
m.e229 = Constraint(expr= (5.28411061001579 - m.x302)**2 + (9.36648183133357 -
    m.x305)**2 + 119.627996085735 * m.b48 <= 120.627996085735)
m.e230 = Constraint(expr= (1.06171481272944 - m.x302)**2 + (3.65844432398946 -
    m.x305)**2 + 107.656809348234 * m.b49 <= 108.656809348234)
m.e231 = Constraint(expr= (9.05099582793631 - m.x302)**2 + (3.98215513024397 -
    m.x305)**2 + 128.639684646565 * m.b50 <= 129.639684646565)
m.e232 = Constraint(expr= (9.08772707393705 - m.x302)**2 + (3.01388234113091 -
    m.x305)**2 + 141.568883438575 * m.b51 <= 142.568883438575)
m.e233 = Constraint(expr= (8.83910845171846 - m.x302)**2 + (8.26686922455514 -
    m.x305)**2 + 142.314787626056 * m.b52 <= 143.314787626056)
m.e234 = Constraint(expr= (3.41090111187451 - m.x302)**2 + (6.48985541572597 -
    m.x305)**2 + 57.6217041967589 * m.b53 <= 58.6217041967589)
m.e235 = Constraint(expr= (1.22004189182266 - m.x302)**2 + (2.52276995748249 -
    m.x305)**2 + 119.180496541755 * m.b54 <= 120.180496541755)
m.e236 = Constraint(expr= (3.94802045665365 - m.x302)**2 + (6.40339456473198 -
    m.x305)**2 + 58.8305966748386 * m.b55 <= 59.8305966748386)
m.e237 = Constraint(expr= (4.9104301706676 - m.x302)**2 + (3.1538945754034 -
    m.x305)**2 + 75.9207984013209 * m.b56 <= 76.9207984013209)
m.e238 = Constraint(expr= (3.23176530143453 - m.x302)**2 + (7.03644502956294 -
    m.x305)**2 + 64.8784745008497 * m.b57 <= 65.8784745008497)
m.e239 = Constraint(expr= (0.39249886515424 - m.x302)**2 + (1.58871179600639 -
    m.x305)**2 + 147.724006608004 * m.b58 <= 148.724006608004)
m.e240 = Constraint(expr= (4.42690021019308 - m.x302)**2 + (8.74244441962606 -
    m.x305)**2 + 100.918497950284 * m.b59 <= 101.918497950284)
m.e241 = Constraint(expr= (2.59382124128511 - m.x302)**2 + (9.98780114819833 -
    m.x305)**2 + 118.022029936783 * m.b60 <= 119.022029936783)
m.e242 = Constraint(expr= m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 + m.b37
    + m.b38 + m.b39 + m.b40 + m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 +
    m.b47 + m.b48 + m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 +
    m.b56 + m.b57 + m.b58 + m.b59 + m.b60 == 1)
m.e243 = Constraint(expr= (2.84746945184196 - m.x307)**2 + (6.74779851669768 -
    m.x309)**2 + 67.42707737338 * m.b61 <= 68.42707737338)
m.e244 = Constraint(expr= (6.63261133839597 - m.x307)**2 + (7.58930814907984 -
    m.x309)**2 + 100.27903396698 * m.b62 <= 101.27903396698)
m.e245 = Constraint(expr= (2.78008351564232 - m.x307)**2 + (5.62089512941063 -
    m.x309)**2 + 62.225162895805 * m.b63 <= 63.225162895805)
m.e246 = Constraint(expr= (3.36345404799715 - m.x307)**2 + (5.61693710344635 -
    m.x309)**2 + 54.3423498257743 * m.b64 <= 55.3423498257743)
m.e247 = Constraint(expr= (1.46574263591158 - m.x307)**2 + (0.14249643071642 -
    m.x309)**2 + 153.854418335954 * m.b65 <= 154.854418335954)
m.e248 = Constraint(expr= (6.59824950993792 - m.x307)**2 + (1.91438252349491 -
    m.x309)**2 + 115.729330039997 * m.b66 <= 116.729330039997)
m.e249 = Constraint(expr= (2.02515523263325 - m.x307)**2 + (3.62141731303869 -
    m.x309)**2 + 92.1830734090453 * m.b67 <= 93.1830734090453)
m.e250 = Constraint(expr= (8.97152199819966 - m.x307)**2 + (8.78133845105015 -
    m.x309)**2 + 153.854418335954 * m.b68 <= 154.854418335954)
m.e251 = Constraint(expr= (1.87485423601802 - m.x307)**2 + (8.96274662253461 -
    m.x309)**2 + 106.113667406259 * m.b69 <= 107.113667406259)
m.e252 = Constraint(expr= (7.52025674966412 - m.x307)**2 + (8.80268658264247 -
    m.x309)**2 + 132.789518443852 * m.b70 <= 133.789518443852)
m.e253 = Constraint(expr= (3.85704114235832 - m.x307)**2 + (6.36674450874035 -
    m.x309)**2 + 57.7951750598727 * m.b71 <= 58.7951750598727)
m.e254 = Constraint(expr= (8.48963678940351 - m.x307)**2 + (5.48402210821562 -
    m.x309)**2 + 102.926783859086 * m.b72 <= 103.926783859086)
m.e255 = Constraint(expr= (6.03160481727421 - m.x307)**2 + (1.276552921829 -
    m.x309)**2 + 118.75213232131 * m.b73 <= 119.75213232131)
m.e256 = Constraint(expr= (6.90662266429413 - m.x307)**2 + (8.78931785429954 -
    m.x309)**2 + 124.803091689871 * m.b74 <= 125.803091689871)
m.e257 = Constraint(expr= (3.71078725250056 - m.x307)**2 + (4.66415664133948 -
    m.x309)**2 + 57.9871322900609 * m.b75 <= 58.9871322900609)
m.e258 = Constraint(expr= (0.107239833314705 - m.x307)**2 + (9.26202525440128
    - m.x309)**2 + 141.568883438575 * m.b76 <= 142.568883438575)
m.e259 = Constraint(expr= (8.04739319923014 - m.x307)**2 + (3.59305161391794 -
    m.x309)**2 + 114.695683175902 * m.b77 <= 115.695683175902)
m.e260 = Constraint(expr= (5.28411061001579 - m.x307)**2 + (9.36648183133357 -
    m.x309)**2 + 119.627996085735 * m.b78 <= 120.627996085735)
m.e261 = Constraint(expr= (1.06171481272944 - m.x307)**2 + (3.65844432398946 -
    m.x309)**2 + 107.656809348234 * m.b79 <= 108.656809348234)
m.e262 = Constraint(expr= (9.05099582793631 - m.x307)**2 + (3.98215513024397 -
    m.x309)**2 + 128.639684646565 * m.b80 <= 129.639684646565)
m.e263 = Constraint(expr= (9.08772707393705 - m.x307)**2 + (3.01388234113091 -
    m.x309)**2 + 141.568883438575 * m.b81 <= 142.568883438575)
m.e264 = Constraint(expr= (8.83910845171846 - m.x307)**2 + (8.26686922455514 -
    m.x309)**2 + 142.314787626056 * m.b82 <= 143.314787626056)
m.e265 = Constraint(expr= (3.41090111187451 - m.x307)**2 + (6.48985541572597 -
    m.x309)**2 + 57.6217041967589 * m.b83 <= 58.6217041967589)
m.e266 = Constraint(expr= (1.22004189182266 - m.x307)**2 + (2.52276995748249 -
    m.x309)**2 + 119.180496541755 * m.b84 <= 120.180496541755)
m.e267 = Constraint(expr= (3.94802045665365 - m.x307)**2 + (6.40339456473198 -
    m.x309)**2 + 58.8305966748386 * m.b85 <= 59.8305966748386)
m.e268 = Constraint(expr= (4.9104301706676 - m.x307)**2 + (3.1538945754034 -
    m.x309)**2 + 75.9207984013209 * m.b86 <= 76.9207984013209)
m.e269 = Constraint(expr= (3.23176530143453 - m.x307)**2 + (7.03644502956294 -
    m.x309)**2 + 64.8784745008497 * m.b87 <= 65.8784745008497)
m.e270 = Constraint(expr= (0.39249886515424 - m.x307)**2 + (1.58871179600639 -
    m.x309)**2 + 147.724006608004 * m.b88 <= 148.724006608004)
m.e271 = Constraint(expr= (4.42690021019308 - m.x307)**2 + (8.74244441962606 -
    m.x309)**2 + 100.918497950284 * m.b89 <= 101.918497950284)
m.e272 = Constraint(expr= (2.59382124128511 - m.x307)**2 + (9.98780114819833 -
    m.x309)**2 + 118.022029936783 * m.b90 <= 119.022029936783)
m.e273 = Constraint(expr= m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b66 + m.b67
    + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 + m.b73 + m.b74 + m.b75 + m.b76 +
    m.b77 + m.b78 + m.b79 + m.b80 + m.b81 + m.b82 + m.b83 + m.b84 + m.b85 +
    m.b86 + m.b87 + m.b88 + m.b89 + m.b90 == 1)
m.e274 = Constraint(expr= (2.84746945184196 - m.x311)**2 + (6.74779851669768 -
    m.x313)**2 + 67.42707737338 * m.b91 <= 68.42707737338)
m.e275 = Constraint(expr= (6.63261133839597 - m.x311)**2 + (7.58930814907984 -
    m.x313)**2 + 100.27903396698 * m.b92 <= 101.27903396698)
m.e276 = Constraint(expr= (2.78008351564232 - m.x311)**2 + (5.62089512941063 -
    m.x313)**2 + 62.225162895805 * m.b93 <= 63.225162895805)
m.e277 = Constraint(expr= (3.36345404799715 - m.x311)**2 + (5.61693710344635 -
    m.x313)**2 + 54.3423498257743 * m.b94 <= 55.3423498257743)
m.e278 = Constraint(expr= (1.46574263591158 - m.x311)**2 + (0.14249643071642 -
    m.x313)**2 + 153.854418335954 * m.b95 <= 154.854418335954)
m.e279 = Constraint(expr= (6.59824950993792 - m.x311)**2 + (1.91438252349491 -
    m.x313)**2 + 115.729330039997 * m.b96 <= 116.729330039997)
m.e280 = Constraint(expr= (2.02515523263325 - m.x311)**2 + (3.62141731303869 -
    m.x313)**2 + 92.1830734090453 * m.b97 <= 93.1830734090453)
m.e281 = Constraint(expr= (8.97152199819966 - m.x311)**2 + (8.78133845105015 -
    m.x313)**2 + 153.854418335954 * m.b98 <= 154.854418335954)
m.e282 = Constraint(expr= (1.87485423601802 - m.x311)**2 + (8.96274662253461 -
    m.x313)**2 + 106.113667406259 * m.b99 <= 107.113667406259)
m.e283 = Constraint(expr= (7.52025674966412 - m.x311)**2 + (8.80268658264247 -
    m.x313)**2 + 132.789518443852 * m.b100 <= 133.789518443852)
m.e284 = Constraint(expr= (3.85704114235832 - m.x311)**2 + (6.36674450874035 -
    m.x313)**2 + 57.7951750598727 * m.b101 <= 58.7951750598727)
m.e285 = Constraint(expr= (8.48963678940351 - m.x311)**2 + (5.48402210821562 -
    m.x313)**2 + 102.926783859086 * m.b102 <= 103.926783859086)
m.e286 = Constraint(expr= (6.03160481727421 - m.x311)**2 + (1.276552921829 -
    m.x313)**2 + 118.75213232131 * m.b103 <= 119.75213232131)
m.e287 = Constraint(expr= (6.90662266429413 - m.x311)**2 + (8.78931785429954 -
    m.x313)**2 + 124.803091689871 * m.b104 <= 125.803091689871)
m.e288 = Constraint(expr= (3.71078725250056 - m.x311)**2 + (4.66415664133948 -
    m.x313)**2 + 57.9871322900609 * m.b105 <= 58.9871322900609)
m.e289 = Constraint(expr= (0.107239833314705 - m.x311)**2 + (9.26202525440128
    - m.x313)**2 + 141.568883438575 * m.b106 <= 142.568883438575)
m.e290 = Constraint(expr= (8.04739319923014 - m.x311)**2 + (3.59305161391794 -
    m.x313)**2 + 114.695683175902 * m.b107 <= 115.695683175902)
m.e291 = Constraint(expr= (5.28411061001579 - m.x311)**2 + (9.36648183133357 -
    m.x313)**2 + 119.627996085735 * m.b108 <= 120.627996085735)
m.e292 = Constraint(expr= (1.06171481272944 - m.x311)**2 + (3.65844432398946 -
    m.x313)**2 + 107.656809348234 * m.b109 <= 108.656809348234)
m.e293 = Constraint(expr= (9.05099582793631 - m.x311)**2 + (3.98215513024397 -
    m.x313)**2 + 128.639684646565 * m.b110 <= 129.639684646565)
m.e294 = Constraint(expr= (9.08772707393705 - m.x311)**2 + (3.01388234113091 -
    m.x313)**2 + 141.568883438575 * m.b111 <= 142.568883438575)
m.e295 = Constraint(expr= (8.83910845171846 - m.x311)**2 + (8.26686922455514 -
    m.x313)**2 + 142.314787626056 * m.b112 <= 143.314787626056)
m.e296 = Constraint(expr= (3.41090111187451 - m.x311)**2 + (6.48985541572597 -
    m.x313)**2 + 57.6217041967589 * m.b113 <= 58.6217041967589)
m.e297 = Constraint(expr= (1.22004189182266 - m.x311)**2 + (2.52276995748249 -
    m.x313)**2 + 119.180496541755 * m.b114 <= 120.180496541755)
m.e298 = Constraint(expr= (3.94802045665365 - m.x311)**2 + (6.40339456473198 -
    m.x313)**2 + 58.8305966748386 * m.b115 <= 59.8305966748386)
m.e299 = Constraint(expr= (4.9104301706676 - m.x311)**2 + (3.1538945754034 -
    m.x313)**2 + 75.9207984013209 * m.b116 <= 76.9207984013209)
m.e300 = Constraint(expr= (3.23176530143453 - m.x311)**2 + (7.03644502956294 -
    m.x313)**2 + 64.8784745008497 * m.b117 <= 65.8784745008497)
m.e301 = Constraint(expr= (0.39249886515424 - m.x311)**2 + (1.58871179600639 -
    m.x313)**2 + 147.724006608004 * m.b118 <= 148.724006608004)
m.e302 = Constraint(expr= (4.42690021019308 - m.x311)**2 + (8.74244441962606 -
    m.x313)**2 + 100.918497950284 * m.b119 <= 101.918497950284)
m.e303 = Constraint(expr= (2.59382124128511 - m.x311)**2 + (9.98780114819833 -
    m.x313)**2 + 118.022029936783 * m.b120 <= 119.022029936783)
m.e304 = Constraint(expr= m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b96 + m.b97
    + m.b98 + m.b99 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104 + m.b105 +
    m.b106 + m.b107 + m.b108 + m.b109 + m.b110 + m.b111 + m.b112 + m.b113 +
    m.b114 + m.b115 + m.b116 + m.b117 + m.b118 + m.b119 + m.b120 == 1)
m.e305 = Constraint(expr= (2.84746945184196 - m.x315)**2 + (6.74779851669768 -
    m.x317)**2 + 67.42707737338 * m.b121 <= 68.42707737338)
m.e306 = Constraint(expr= (6.63261133839597 - m.x315)**2 + (7.58930814907984 -
    m.x317)**2 + 100.27903396698 * m.b122 <= 101.27903396698)
m.e307 = Constraint(expr= (2.78008351564232 - m.x315)**2 + (5.62089512941063 -
    m.x317)**2 + 62.225162895805 * m.b123 <= 63.225162895805)
m.e308 = Constraint(expr= (3.36345404799715 - m.x315)**2 + (5.61693710344635 -
    m.x317)**2 + 54.3423498257743 * m.b124 <= 55.3423498257743)
m.e309 = Constraint(expr= (1.46574263591158 - m.x315)**2 + (0.14249643071642 -
    m.x317)**2 + 153.854418335954 * m.b125 <= 154.854418335954)
m.e310 = Constraint(expr= (6.59824950993792 - m.x315)**2 + (1.91438252349491 -
    m.x317)**2 + 115.729330039997 * m.b126 <= 116.729330039997)
m.e311 = Constraint(expr= (2.02515523263325 - m.x315)**2 + (3.62141731303869 -
    m.x317)**2 + 92.1830734090453 * m.b127 <= 93.1830734090453)
m.e312 = Constraint(expr= (8.97152199819966 - m.x315)**2 + (8.78133845105015 -
    m.x317)**2 + 153.854418335954 * m.b128 <= 154.854418335954)
m.e313 = Constraint(expr= (1.87485423601802 - m.x315)**2 + (8.96274662253461 -
    m.x317)**2 + 106.113667406259 * m.b129 <= 107.113667406259)
m.e314 = Constraint(expr= (7.52025674966412 - m.x315)**2 + (8.80268658264247 -
    m.x317)**2 + 132.789518443852 * m.b130 <= 133.789518443852)
m.e315 = Constraint(expr= (3.85704114235832 - m.x315)**2 + (6.36674450874035 -
    m.x317)**2 + 57.7951750598727 * m.b131 <= 58.7951750598727)
m.e316 = Constraint(expr= (8.48963678940351 - m.x315)**2 + (5.48402210821562 -
    m.x317)**2 + 102.926783859086 * m.b132 <= 103.926783859086)
m.e317 = Constraint(expr= (6.03160481727421 - m.x315)**2 + (1.276552921829 -
    m.x317)**2 + 118.75213232131 * m.b133 <= 119.75213232131)
m.e318 = Constraint(expr= (6.90662266429413 - m.x315)**2 + (8.78931785429954 -
    m.x317)**2 + 124.803091689871 * m.b134 <= 125.803091689871)
m.e319 = Constraint(expr= (3.71078725250056 - m.x315)**2 + (4.66415664133948 -
    m.x317)**2 + 57.9871322900609 * m.b135 <= 58.9871322900609)
m.e320 = Constraint(expr= (0.107239833314705 - m.x315)**2 + (9.26202525440128
    - m.x317)**2 + 141.568883438575 * m.b136 <= 142.568883438575)
m.e321 = Constraint(expr= (8.04739319923014 - m.x315)**2 + (3.59305161391794 -
    m.x317)**2 + 114.695683175902 * m.b137 <= 115.695683175902)
m.e322 = Constraint(expr= (5.28411061001579 - m.x315)**2 + (9.36648183133357 -
    m.x317)**2 + 119.627996085735 * m.b138 <= 120.627996085735)
m.e323 = Constraint(expr= (1.06171481272944 - m.x315)**2 + (3.65844432398946 -
    m.x317)**2 + 107.656809348234 * m.b139 <= 108.656809348234)
m.e324 = Constraint(expr= (9.05099582793631 - m.x315)**2 + (3.98215513024397 -
    m.x317)**2 + 128.639684646565 * m.b140 <= 129.639684646565)
m.e325 = Constraint(expr= (9.08772707393705 - m.x315)**2 + (3.01388234113091 -
    m.x317)**2 + 141.568883438575 * m.b141 <= 142.568883438575)
m.e326 = Constraint(expr= (8.83910845171846 - m.x315)**2 + (8.26686922455514 -
    m.x317)**2 + 142.314787626056 * m.b142 <= 143.314787626056)
m.e327 = Constraint(expr= (3.41090111187451 - m.x315)**2 + (6.48985541572597 -
    m.x317)**2 + 57.6217041967589 * m.b143 <= 58.6217041967589)
m.e328 = Constraint(expr= (1.22004189182266 - m.x315)**2 + (2.52276995748249 -
    m.x317)**2 + 119.180496541755 * m.b144 <= 120.180496541755)
m.e329 = Constraint(expr= (3.94802045665365 - m.x315)**2 + (6.40339456473198 -
    m.x317)**2 + 58.8305966748386 * m.b145 <= 59.8305966748386)
m.e330 = Constraint(expr= (4.9104301706676 - m.x315)**2 + (3.1538945754034 -
    m.x317)**2 + 75.9207984013209 * m.b146 <= 76.9207984013209)
m.e331 = Constraint(expr= (3.23176530143453 - m.x315)**2 + (7.03644502956294 -
    m.x317)**2 + 64.8784745008497 * m.b147 <= 65.8784745008497)
m.e332 = Constraint(expr= (0.39249886515424 - m.x315)**2 + (1.58871179600639 -
    m.x317)**2 + 147.724006608004 * m.b148 <= 148.724006608004)
m.e333 = Constraint(expr= (4.42690021019308 - m.x315)**2 + (8.74244441962606 -
    m.x317)**2 + 100.918497950284 * m.b149 <= 101.918497950284)
m.e334 = Constraint(expr= (2.59382124128511 - m.x315)**2 + (9.98780114819833 -
    m.x317)**2 + 118.022029936783 * m.b150 <= 119.022029936783)
m.e335 = Constraint(expr= m.b121 + m.b122 + m.b123 + m.b124 + m.b125 + m.b126
    + m.b127 + m.b128 + m.b129 + m.b130 + m.b131 + m.b132 + m.b133 + m.b134 +
    m.b135 + m.b136 + m.b137 + m.b138 + m.b139 + m.b140 + m.b141 + m.b142 +
    m.b143 + m.b144 + m.b145 + m.b146 + m.b147 + m.b148 + m.b149 + m.b150 == 1)
m.e336 = Constraint(expr= (2.84746945184196 - m.x319)**2 + (6.74779851669768 -
    m.x321)**2 + 67.42707737338 * m.b151 <= 68.42707737338)
m.e337 = Constraint(expr= (6.63261133839597 - m.x319)**2 + (7.58930814907984 -
    m.x321)**2 + 100.27903396698 * m.b152 <= 101.27903396698)
m.e338 = Constraint(expr= (2.78008351564232 - m.x319)**2 + (5.62089512941063 -
    m.x321)**2 + 62.225162895805 * m.b153 <= 63.225162895805)
m.e339 = Constraint(expr= (3.36345404799715 - m.x319)**2 + (5.61693710344635 -
    m.x321)**2 + 54.3423498257743 * m.b154 <= 55.3423498257743)
m.e340 = Constraint(expr= (1.46574263591158 - m.x319)**2 + (0.14249643071642 -
    m.x321)**2 + 153.854418335954 * m.b155 <= 154.854418335954)
m.e341 = Constraint(expr= (6.59824950993792 - m.x319)**2 + (1.91438252349491 -
    m.x321)**2 + 115.729330039997 * m.b156 <= 116.729330039997)
m.e342 = Constraint(expr= (2.02515523263325 - m.x319)**2 + (3.62141731303869 -
    m.x321)**2 + 92.1830734090453 * m.b157 <= 93.1830734090453)
m.e343 = Constraint(expr= (8.97152199819966 - m.x319)**2 + (8.78133845105015 -
    m.x321)**2 + 153.854418335954 * m.b158 <= 154.854418335954)
m.e344 = Constraint(expr= (1.87485423601802 - m.x319)**2 + (8.96274662253461 -
    m.x321)**2 + 106.113667406259 * m.b159 <= 107.113667406259)
m.e345 = Constraint(expr= (7.52025674966412 - m.x319)**2 + (8.80268658264247 -
    m.x321)**2 + 132.789518443852 * m.b160 <= 133.789518443852)
m.e346 = Constraint(expr= (3.85704114235832 - m.x319)**2 + (6.36674450874035 -
    m.x321)**2 + 57.7951750598727 * m.b161 <= 58.7951750598727)
m.e347 = Constraint(expr= (8.48963678940351 - m.x319)**2 + (5.48402210821562 -
    m.x321)**2 + 102.926783859086 * m.b162 <= 103.926783859086)
m.e348 = Constraint(expr= (6.03160481727421 - m.x319)**2 + (1.276552921829 -
    m.x321)**2 + 118.75213232131 * m.b163 <= 119.75213232131)
m.e349 = Constraint(expr= (6.90662266429413 - m.x319)**2 + (8.78931785429954 -
    m.x321)**2 + 124.803091689871 * m.b164 <= 125.803091689871)
m.e350 = Constraint(expr= (3.71078725250056 - m.x319)**2 + (4.66415664133948 -
    m.x321)**2 + 57.9871322900609 * m.b165 <= 58.9871322900609)
m.e351 = Constraint(expr= (0.107239833314705 - m.x319)**2 + (9.26202525440128
    - m.x321)**2 + 141.568883438575 * m.b166 <= 142.568883438575)
m.e352 = Constraint(expr= (8.04739319923014 - m.x319)**2 + (3.59305161391794 -
    m.x321)**2 + 114.695683175902 * m.b167 <= 115.695683175902)
m.e353 = Constraint(expr= (5.28411061001579 - m.x319)**2 + (9.36648183133357 -
    m.x321)**2 + 119.627996085735 * m.b168 <= 120.627996085735)
m.e354 = Constraint(expr= (1.06171481272944 - m.x319)**2 + (3.65844432398946 -
    m.x321)**2 + 107.656809348234 * m.b169 <= 108.656809348234)
m.e355 = Constraint(expr= (9.05099582793631 - m.x319)**2 + (3.98215513024397 -
    m.x321)**2 + 128.639684646565 * m.b170 <= 129.639684646565)
m.e356 = Constraint(expr= (9.08772707393705 - m.x319)**2 + (3.01388234113091 -
    m.x321)**2 + 141.568883438575 * m.b171 <= 142.568883438575)
m.e357 = Constraint(expr= (8.83910845171846 - m.x319)**2 + (8.26686922455514 -
    m.x321)**2 + 142.314787626056 * m.b172 <= 143.314787626056)
m.e358 = Constraint(expr= (3.41090111187451 - m.x319)**2 + (6.48985541572597 -
    m.x321)**2 + 57.6217041967589 * m.b173 <= 58.6217041967589)
m.e359 = Constraint(expr= (1.22004189182266 - m.x319)**2 + (2.52276995748249 -
    m.x321)**2 + 119.180496541755 * m.b174 <= 120.180496541755)
m.e360 = Constraint(expr= (3.94802045665365 - m.x319)**2 + (6.40339456473198 -
    m.x321)**2 + 58.8305966748386 * m.b175 <= 59.8305966748386)
m.e361 = Constraint(expr= (4.9104301706676 - m.x319)**2 + (3.1538945754034 -
    m.x321)**2 + 75.9207984013209 * m.b176 <= 76.9207984013209)
m.e362 = Constraint(expr= (3.23176530143453 - m.x319)**2 + (7.03644502956294 -
    m.x321)**2 + 64.8784745008497 * m.b177 <= 65.8784745008497)
m.e363 = Constraint(expr= (0.39249886515424 - m.x319)**2 + (1.58871179600639 -
    m.x321)**2 + 147.724006608004 * m.b178 <= 148.724006608004)
m.e364 = Constraint(expr= (4.42690021019308 - m.x319)**2 + (8.74244441962606 -
    m.x321)**2 + 100.918497950284 * m.b179 <= 101.918497950284)
m.e365 = Constraint(expr= (2.59382124128511 - m.x319)**2 + (9.98780114819833 -
    m.x321)**2 + 118.022029936783 * m.b180 <= 119.022029936783)
m.e366 = Constraint(expr= m.b151 + m.b152 + m.b153 + m.b154 + m.b155 + m.b156
    + m.b157 + m.b158 + m.b159 + m.b160 + m.b161 + m.b162 + m.b163 + m.b164 +
    m.b165 + m.b166 + m.b167 + m.b168 + m.b169 + m.b170 + m.b171 + m.b172 +
    m.b173 + m.b174 + m.b175 + m.b176 + m.b177 + m.b178 + m.b179 + m.b180 == 1)
m.e367 = Constraint(expr= (2.84746945184196 - m.x323)**2 + (6.74779851669768 -
    m.x325)**2 + 67.42707737338 * m.b181 <= 68.42707737338)
m.e368 = Constraint(expr= (6.63261133839597 - m.x323)**2 + (7.58930814907984 -
    m.x325)**2 + 100.27903396698 * m.b182 <= 101.27903396698)
m.e369 = Constraint(expr= (2.78008351564232 - m.x323)**2 + (5.62089512941063 -
    m.x325)**2 + 62.225162895805 * m.b183 <= 63.225162895805)
m.e370 = Constraint(expr= (3.36345404799715 - m.x323)**2 + (5.61693710344635 -
    m.x325)**2 + 54.3423498257743 * m.b184 <= 55.3423498257743)
m.e371 = Constraint(expr= (1.46574263591158 - m.x323)**2 + (0.14249643071642 -
    m.x325)**2 + 153.854418335954 * m.b185 <= 154.854418335954)
m.e372 = Constraint(expr= (6.59824950993792 - m.x323)**2 + (1.91438252349491 -
    m.x325)**2 + 115.729330039997 * m.b186 <= 116.729330039997)
m.e373 = Constraint(expr= (2.02515523263325 - m.x323)**2 + (3.62141731303869 -
    m.x325)**2 + 92.1830734090453 * m.b187 <= 93.1830734090453)
m.e374 = Constraint(expr= (8.97152199819966 - m.x323)**2 + (8.78133845105015 -
    m.x325)**2 + 153.854418335954 * m.b188 <= 154.854418335954)
m.e375 = Constraint(expr= (1.87485423601802 - m.x323)**2 + (8.96274662253461 -
    m.x325)**2 + 106.113667406259 * m.b189 <= 107.113667406259)
m.e376 = Constraint(expr= (7.52025674966412 - m.x323)**2 + (8.80268658264247 -
    m.x325)**2 + 132.789518443852 * m.b190 <= 133.789518443852)
m.e377 = Constraint(expr= (3.85704114235832 - m.x323)**2 + (6.36674450874035 -
    m.x325)**2 + 57.7951750598727 * m.b191 <= 58.7951750598727)
m.e378 = Constraint(expr= (8.48963678940351 - m.x323)**2 + (5.48402210821562 -
    m.x325)**2 + 102.926783859086 * m.b192 <= 103.926783859086)
m.e379 = Constraint(expr= (6.03160481727421 - m.x323)**2 + (1.276552921829 -
    m.x325)**2 + 118.75213232131 * m.b193 <= 119.75213232131)
m.e380 = Constraint(expr= (6.90662266429413 - m.x323)**2 + (8.78931785429954 -
    m.x325)**2 + 124.803091689871 * m.b194 <= 125.803091689871)
m.e381 = Constraint(expr= (3.71078725250056 - m.x323)**2 + (4.66415664133948 -
    m.x325)**2 + 57.9871322900609 * m.b195 <= 58.9871322900609)
m.e382 = Constraint(expr= (0.107239833314705 - m.x323)**2 + (9.26202525440128
    - m.x325)**2 + 141.568883438575 * m.b196 <= 142.568883438575)
m.e383 = Constraint(expr= (8.04739319923014 - m.x323)**2 + (3.59305161391794 -
    m.x325)**2 + 114.695683175902 * m.b197 <= 115.695683175902)
m.e384 = Constraint(expr= (5.28411061001579 - m.x323)**2 + (9.36648183133357 -
    m.x325)**2 + 119.627996085735 * m.b198 <= 120.627996085735)
m.e385 = Constraint(expr= (1.06171481272944 - m.x323)**2 + (3.65844432398946 -
    m.x325)**2 + 107.656809348234 * m.b199 <= 108.656809348234)
m.e386 = Constraint(expr= (9.05099582793631 - m.x323)**2 + (3.98215513024397 -
    m.x325)**2 + 128.639684646565 * m.b200 <= 129.639684646565)
m.e387 = Constraint(expr= (9.08772707393705 - m.x323)**2 + (3.01388234113091 -
    m.x325)**2 + 141.568883438575 * m.b201 <= 142.568883438575)
m.e388 = Constraint(expr= (8.83910845171846 - m.x323)**2 + (8.26686922455514 -
    m.x325)**2 + 142.314787626056 * m.b202 <= 143.314787626056)
m.e389 = Constraint(expr= (3.41090111187451 - m.x323)**2 + (6.48985541572597 -
    m.x325)**2 + 57.6217041967589 * m.b203 <= 58.6217041967589)
m.e390 = Constraint(expr= (1.22004189182266 - m.x323)**2 + (2.52276995748249 -
    m.x325)**2 + 119.180496541755 * m.b204 <= 120.180496541755)
m.e391 = Constraint(expr= (3.94802045665365 - m.x323)**2 + (6.40339456473198 -
    m.x325)**2 + 58.8305966748386 * m.b205 <= 59.8305966748386)
m.e392 = Constraint(expr= (4.9104301706676 - m.x323)**2 + (3.1538945754034 -
    m.x325)**2 + 75.9207984013209 * m.b206 <= 76.9207984013209)
m.e393 = Constraint(expr= (3.23176530143453 - m.x323)**2 + (7.03644502956294 -
    m.x325)**2 + 64.8784745008497 * m.b207 <= 65.8784745008497)
m.e394 = Constraint(expr= (0.39249886515424 - m.x323)**2 + (1.58871179600639 -
    m.x325)**2 + 147.724006608004 * m.b208 <= 148.724006608004)
m.e395 = Constraint(expr= (4.42690021019308 - m.x323)**2 + (8.74244441962606 -
    m.x325)**2 + 100.918497950284 * m.b209 <= 101.918497950284)
m.e396 = Constraint(expr= (2.59382124128511 - m.x323)**2 + (9.98780114819833 -
    m.x325)**2 + 118.022029936783 * m.b210 <= 119.022029936783)
m.e397 = Constraint(expr= m.b181 + m.b182 + m.b183 + m.b184 + m.b185 + m.b186
    + m.b187 + m.b188 + m.b189 + m.b190 + m.b191 + m.b192 + m.b193 + m.b194 +
    m.b195 + m.b196 + m.b197 + m.b198 + m.b199 + m.b200 + m.b201 + m.b202 +
    m.b203 + m.b204 + m.b205 + m.b206 + m.b207 + m.b208 + m.b209 + m.b210 == 1)
m.e398 = Constraint(expr= (2.84746945184196 - m.x327)**2 + (6.74779851669768 -
    m.x329)**2 + 67.42707737338 * m.b211 <= 68.42707737338)
m.e399 = Constraint(expr= (6.63261133839597 - m.x327)**2 + (7.58930814907984 -
    m.x329)**2 + 100.27903396698 * m.b212 <= 101.27903396698)
m.e400 = Constraint(expr= (2.78008351564232 - m.x327)**2 + (5.62089512941063 -
    m.x329)**2 + 62.225162895805 * m.b213 <= 63.225162895805)
m.e401 = Constraint(expr= (3.36345404799715 - m.x327)**2 + (5.61693710344635 -
    m.x329)**2 + 54.3423498257743 * m.b214 <= 55.3423498257743)
m.e402 = Constraint(expr= (1.46574263591158 - m.x327)**2 + (0.14249643071642 -
    m.x329)**2 + 153.854418335954 * m.b215 <= 154.854418335954)
m.e403 = Constraint(expr= (6.59824950993792 - m.x327)**2 + (1.91438252349491 -
    m.x329)**2 + 115.729330039997 * m.b216 <= 116.729330039997)
m.e404 = Constraint(expr= (2.02515523263325 - m.x327)**2 + (3.62141731303869 -
    m.x329)**2 + 92.1830734090453 * m.b217 <= 93.1830734090453)
m.e405 = Constraint(expr= (8.97152199819966 - m.x327)**2 + (8.78133845105015 -
    m.x329)**2 + 153.854418335954 * m.b218 <= 154.854418335954)
m.e406 = Constraint(expr= (1.87485423601802 - m.x327)**2 + (8.96274662253461 -
    m.x329)**2 + 106.113667406259 * m.b219 <= 107.113667406259)
m.e407 = Constraint(expr= (7.52025674966412 - m.x327)**2 + (8.80268658264247 -
    m.x329)**2 + 132.789518443852 * m.b220 <= 133.789518443852)
m.e408 = Constraint(expr= (3.85704114235832 - m.x327)**2 + (6.36674450874035 -
    m.x329)**2 + 57.7951750598727 * m.b221 <= 58.7951750598727)
m.e409 = Constraint(expr= (8.48963678940351 - m.x327)**2 + (5.48402210821562 -
    m.x329)**2 + 102.926783859086 * m.b222 <= 103.926783859086)
m.e410 = Constraint(expr= (6.03160481727421 - m.x327)**2 + (1.276552921829 -
    m.x329)**2 + 118.75213232131 * m.b223 <= 119.75213232131)
m.e411 = Constraint(expr= (6.90662266429413 - m.x327)**2 + (8.78931785429954 -
    m.x329)**2 + 124.803091689871 * m.b224 <= 125.803091689871)
m.e412 = Constraint(expr= (3.71078725250056 - m.x327)**2 + (4.66415664133948 -
    m.x329)**2 + 57.9871322900609 * m.b225 <= 58.9871322900609)
m.e413 = Constraint(expr= (0.107239833314705 - m.x327)**2 + (9.26202525440128
    - m.x329)**2 + 141.568883438575 * m.b226 <= 142.568883438575)
m.e414 = Constraint(expr= (8.04739319923014 - m.x327)**2 + (3.59305161391794 -
    m.x329)**2 + 114.695683175902 * m.b227 <= 115.695683175902)
m.e415 = Constraint(expr= (5.28411061001579 - m.x327)**2 + (9.36648183133357 -
    m.x329)**2 + 119.627996085735 * m.b228 <= 120.627996085735)
m.e416 = Constraint(expr= (1.06171481272944 - m.x327)**2 + (3.65844432398946 -
    m.x329)**2 + 107.656809348234 * m.b229 <= 108.656809348234)
m.e417 = Constraint(expr= (9.05099582793631 - m.x327)**2 + (3.98215513024397 -
    m.x329)**2 + 128.639684646565 * m.b230 <= 129.639684646565)
m.e418 = Constraint(expr= (9.08772707393705 - m.x327)**2 + (3.01388234113091 -
    m.x329)**2 + 141.568883438575 * m.b231 <= 142.568883438575)
m.e419 = Constraint(expr= (8.83910845171846 - m.x327)**2 + (8.26686922455514 -
    m.x329)**2 + 142.314787626056 * m.b232 <= 143.314787626056)
m.e420 = Constraint(expr= (3.41090111187451 - m.x327)**2 + (6.48985541572597 -
    m.x329)**2 + 57.6217041967589 * m.b233 <= 58.6217041967589)
m.e421 = Constraint(expr= (1.22004189182266 - m.x327)**2 + (2.52276995748249 -
    m.x329)**2 + 119.180496541755 * m.b234 <= 120.180496541755)
m.e422 = Constraint(expr= (3.94802045665365 - m.x327)**2 + (6.40339456473198 -
    m.x329)**2 + 58.8305966748386 * m.b235 <= 59.8305966748386)
m.e423 = Constraint(expr= (4.9104301706676 - m.x327)**2 + (3.1538945754034 -
    m.x329)**2 + 75.9207984013209 * m.b236 <= 76.9207984013209)
m.e424 = Constraint(expr= (3.23176530143453 - m.x327)**2 + (7.03644502956294 -
    m.x329)**2 + 64.8784745008497 * m.b237 <= 65.8784745008497)
m.e425 = Constraint(expr= (0.39249886515424 - m.x327)**2 + (1.58871179600639 -
    m.x329)**2 + 147.724006608004 * m.b238 <= 148.724006608004)
m.e426 = Constraint(expr= (4.42690021019308 - m.x327)**2 + (8.74244441962606 -
    m.x329)**2 + 100.918497950284 * m.b239 <= 101.918497950284)
m.e427 = Constraint(expr= (2.59382124128511 - m.x327)**2 + (9.98780114819833 -
    m.x329)**2 + 118.022029936783 * m.b240 <= 119.022029936783)
m.e428 = Constraint(expr= m.b211 + m.b212 + m.b213 + m.b214 + m.b215 + m.b216
    + m.b217 + m.b218 + m.b219 + m.b220 + m.b221 + m.b222 + m.b223 + m.b224 +
    m.b225 + m.b226 + m.b227 + m.b228 + m.b229 + m.b230 + m.b231 + m.b232 +
    m.b233 + m.b234 + m.b235 + m.b236 + m.b237 + m.b238 + m.b239 + m.b240 == 1)
m.e429 = Constraint(expr= (2.84746945184196 - m.x331)**2 + (6.74779851669768 -
    m.x333)**2 + 67.42707737338 * m.b241 <= 68.42707737338)
m.e430 = Constraint(expr= (6.63261133839597 - m.x331)**2 + (7.58930814907984 -
    m.x333)**2 + 100.27903396698 * m.b242 <= 101.27903396698)
m.e431 = Constraint(expr= (2.78008351564232 - m.x331)**2 + (5.62089512941063 -
    m.x333)**2 + 62.225162895805 * m.b243 <= 63.225162895805)
m.e432 = Constraint(expr= (3.36345404799715 - m.x331)**2 + (5.61693710344635 -
    m.x333)**2 + 54.3423498257743 * m.b244 <= 55.3423498257743)
m.e433 = Constraint(expr= (1.46574263591158 - m.x331)**2 + (0.14249643071642 -
    m.x333)**2 + 153.854418335954 * m.b245 <= 154.854418335954)
m.e434 = Constraint(expr= (6.59824950993792 - m.x331)**2 + (1.91438252349491 -
    m.x333)**2 + 115.729330039997 * m.b246 <= 116.729330039997)
m.e435 = Constraint(expr= (2.02515523263325 - m.x331)**2 + (3.62141731303869 -
    m.x333)**2 + 92.1830734090453 * m.b247 <= 93.1830734090453)
m.e436 = Constraint(expr= (8.97152199819966 - m.x331)**2 + (8.78133845105015 -
    m.x333)**2 + 153.854418335954 * m.b248 <= 154.854418335954)
m.e437 = Constraint(expr= (1.87485423601802 - m.x331)**2 + (8.96274662253461 -
    m.x333)**2 + 106.113667406259 * m.b249 <= 107.113667406259)
m.e438 = Constraint(expr= (7.52025674966412 - m.x331)**2 + (8.80268658264247 -
    m.x333)**2 + 132.789518443852 * m.b250 <= 133.789518443852)
m.e439 = Constraint(expr= (3.85704114235832 - m.x331)**2 + (6.36674450874035 -
    m.x333)**2 + 57.7951750598727 * m.b251 <= 58.7951750598727)
m.e440 = Constraint(expr= (8.48963678940351 - m.x331)**2 + (5.48402210821562 -
    m.x333)**2 + 102.926783859086 * m.b252 <= 103.926783859086)
m.e441 = Constraint(expr= (6.03160481727421 - m.x331)**2 + (1.276552921829 -
    m.x333)**2 + 118.75213232131 * m.b253 <= 119.75213232131)
m.e442 = Constraint(expr= (6.90662266429413 - m.x331)**2 + (8.78931785429954 -
    m.x333)**2 + 124.803091689871 * m.b254 <= 125.803091689871)
m.e443 = Constraint(expr= (3.71078725250056 - m.x331)**2 + (4.66415664133948 -
    m.x333)**2 + 57.9871322900609 * m.b255 <= 58.9871322900609)
m.e444 = Constraint(expr= (0.107239833314705 - m.x331)**2 + (9.26202525440128
    - m.x333)**2 + 141.568883438575 * m.b256 <= 142.568883438575)
m.e445 = Constraint(expr= (8.04739319923014 - m.x331)**2 + (3.59305161391794 -
    m.x333)**2 + 114.695683175902 * m.b257 <= 115.695683175902)
m.e446 = Constraint(expr= (5.28411061001579 - m.x331)**2 + (9.36648183133357 -
    m.x333)**2 + 119.627996085735 * m.b258 <= 120.627996085735)
m.e447 = Constraint(expr= (1.06171481272944 - m.x331)**2 + (3.65844432398946 -
    m.x333)**2 + 107.656809348234 * m.b259 <= 108.656809348234)
m.e448 = Constraint(expr= (9.05099582793631 - m.x331)**2 + (3.98215513024397 -
    m.x333)**2 + 128.639684646565 * m.b260 <= 129.639684646565)
m.e449 = Constraint(expr= (9.08772707393705 - m.x331)**2 + (3.01388234113091 -
    m.x333)**2 + 141.568883438575 * m.b261 <= 142.568883438575)
m.e450 = Constraint(expr= (8.83910845171846 - m.x331)**2 + (8.26686922455514 -
    m.x333)**2 + 142.314787626056 * m.b262 <= 143.314787626056)
m.e451 = Constraint(expr= (3.41090111187451 - m.x331)**2 + (6.48985541572597 -
    m.x333)**2 + 57.6217041967589 * m.b263 <= 58.6217041967589)
m.e452 = Constraint(expr= (1.22004189182266 - m.x331)**2 + (2.52276995748249 -
    m.x333)**2 + 119.180496541755 * m.b264 <= 120.180496541755)
m.e453 = Constraint(expr= (3.94802045665365 - m.x331)**2 + (6.40339456473198 -
    m.x333)**2 + 58.8305966748386 * m.b265 <= 59.8305966748386)
m.e454 = Constraint(expr= (4.9104301706676 - m.x331)**2 + (3.1538945754034 -
    m.x333)**2 + 75.9207984013209 * m.b266 <= 76.9207984013209)
m.e455 = Constraint(expr= (3.23176530143453 - m.x331)**2 + (7.03644502956294 -
    m.x333)**2 + 64.8784745008497 * m.b267 <= 65.8784745008497)
m.e456 = Constraint(expr= (0.39249886515424 - m.x331)**2 + (1.58871179600639 -
    m.x333)**2 + 147.724006608004 * m.b268 <= 148.724006608004)
m.e457 = Constraint(expr= (4.42690021019308 - m.x331)**2 + (8.74244441962606 -
    m.x333)**2 + 100.918497950284 * m.b269 <= 101.918497950284)
m.e458 = Constraint(expr= (2.59382124128511 - m.x331)**2 + (9.98780114819833 -
    m.x333)**2 + 118.022029936783 * m.b270 <= 119.022029936783)
m.e459 = Constraint(expr= m.b241 + m.b242 + m.b243 + m.b244 + m.b245 + m.b246
    + m.b247 + m.b248 + m.b249 + m.b250 + m.b251 + m.b252 + m.b253 + m.b254 +
    m.b255 + m.b256 + m.b257 + m.b258 + m.b259 + m.b260 + m.b261 + m.b262 +
    m.b263 + m.b264 + m.b265 + m.b266 + m.b267 + m.b268 + m.b269 + m.b270 == 1)
m.e460 = Constraint(expr= (2.84746945184196 - m.x335)**2 + (6.74779851669768 -
    m.x337)**2 + 67.42707737338 * m.b271 <= 68.42707737338)
m.e461 = Constraint(expr= (6.63261133839597 - m.x335)**2 + (7.58930814907984 -
    m.x337)**2 + 100.27903396698 * m.b272 <= 101.27903396698)
m.e462 = Constraint(expr= (2.78008351564232 - m.x335)**2 + (5.62089512941063 -
    m.x337)**2 + 62.225162895805 * m.b273 <= 63.225162895805)
m.e463 = Constraint(expr= (3.36345404799715 - m.x335)**2 + (5.61693710344635 -
    m.x337)**2 + 54.3423498257743 * m.b274 <= 55.3423498257743)
m.e464 = Constraint(expr= (1.46574263591158 - m.x335)**2 + (0.14249643071642 -
    m.x337)**2 + 153.854418335954 * m.b275 <= 154.854418335954)
m.e465 = Constraint(expr= (6.59824950993792 - m.x335)**2 + (1.91438252349491 -
    m.x337)**2 + 115.729330039997 * m.b276 <= 116.729330039997)
m.e466 = Constraint(expr= (2.02515523263325 - m.x335)**2 + (3.62141731303869 -
    m.x337)**2 + 92.1830734090453 * m.b277 <= 93.1830734090453)
m.e467 = Constraint(expr= (8.97152199819966 - m.x335)**2 + (8.78133845105015 -
    m.x337)**2 + 153.854418335954 * m.b278 <= 154.854418335954)
m.e468 = Constraint(expr= (1.87485423601802 - m.x335)**2 + (8.96274662253461 -
    m.x337)**2 + 106.113667406259 * m.b279 <= 107.113667406259)
m.e469 = Constraint(expr= (7.52025674966412 - m.x335)**2 + (8.80268658264247 -
    m.x337)**2 + 132.789518443852 * m.b280 <= 133.789518443852)
m.e470 = Constraint(expr= (3.85704114235832 - m.x335)**2 + (6.36674450874035 -
    m.x337)**2 + 57.7951750598727 * m.b281 <= 58.7951750598727)
m.e471 = Constraint(expr= (8.48963678940351 - m.x335)**2 + (5.48402210821562 -
    m.x337)**2 + 102.926783859086 * m.b282 <= 103.926783859086)
m.e472 = Constraint(expr= (6.03160481727421 - m.x335)**2 + (1.276552921829 -
    m.x337)**2 + 118.75213232131 * m.b283 <= 119.75213232131)
m.e473 = Constraint(expr= (6.90662266429413 - m.x335)**2 + (8.78931785429954 -
    m.x337)**2 + 124.803091689871 * m.b284 <= 125.803091689871)
m.e474 = Constraint(expr= (3.71078725250056 - m.x335)**2 + (4.66415664133948 -
    m.x337)**2 + 57.9871322900609 * m.b285 <= 58.9871322900609)
m.e475 = Constraint(expr= (0.107239833314705 - m.x335)**2 + (9.26202525440128
    - m.x337)**2 + 141.568883438575 * m.b286 <= 142.568883438575)
m.e476 = Constraint(expr= (8.04739319923014 - m.x335)**2 + (3.59305161391794 -
    m.x337)**2 + 114.695683175902 * m.b287 <= 115.695683175902)
m.e477 = Constraint(expr= (5.28411061001579 - m.x335)**2 + (9.36648183133357 -
    m.x337)**2 + 119.627996085735 * m.b288 <= 120.627996085735)
m.e478 = Constraint(expr= (1.06171481272944 - m.x335)**2 + (3.65844432398946 -
    m.x337)**2 + 107.656809348234 * m.b289 <= 108.656809348234)
m.e479 = Constraint(expr= (9.05099582793631 - m.x335)**2 + (3.98215513024397 -
    m.x337)**2 + 128.639684646565 * m.b290 <= 129.639684646565)
m.e480 = Constraint(expr= (9.08772707393705 - m.x335)**2 + (3.01388234113091 -
    m.x337)**2 + 141.568883438575 * m.b291 <= 142.568883438575)
m.e481 = Constraint(expr= (8.83910845171846 - m.x335)**2 + (8.26686922455514 -
    m.x337)**2 + 142.314787626056 * m.b292 <= 143.314787626056)
m.e482 = Constraint(expr= (3.41090111187451 - m.x335)**2 + (6.48985541572597 -
    m.x337)**2 + 57.6217041967589 * m.b293 <= 58.6217041967589)
m.e483 = Constraint(expr= (1.22004189182266 - m.x335)**2 + (2.52276995748249 -
    m.x337)**2 + 119.180496541755 * m.b294 <= 120.180496541755)
m.e484 = Constraint(expr= (3.94802045665365 - m.x335)**2 + (6.40339456473198 -
    m.x337)**2 + 58.8305966748386 * m.b295 <= 59.8305966748386)
m.e485 = Constraint(expr= (4.9104301706676 - m.x335)**2 + (3.1538945754034 -
    m.x337)**2 + 75.9207984013209 * m.b296 <= 76.9207984013209)
m.e486 = Constraint(expr= (3.23176530143453 - m.x335)**2 + (7.03644502956294 -
    m.x337)**2 + 64.8784745008497 * m.b297 <= 65.8784745008497)
m.e487 = Constraint(expr= (0.39249886515424 - m.x335)**2 + (1.58871179600639 -
    m.x337)**2 + 147.724006608004 * m.b298 <= 148.724006608004)
m.e488 = Constraint(expr= (4.42690021019308 - m.x335)**2 + (8.74244441962606 -
    m.x337)**2 + 100.918497950284 * m.b299 <= 101.918497950284)
m.e489 = Constraint(expr= (2.59382124128511 - m.x335)**2 + (9.98780114819833 -
    m.x337)**2 + 118.022029936783 * m.b300 <= 119.022029936783)
m.e490 = Constraint(expr= m.b271 + m.b272 + m.b273 + m.b274 + m.b275 + m.b276
    + m.b277 + m.b278 + m.b279 + m.b280 + m.b281 + m.b282 + m.b283 + m.b284 +
    m.b285 + m.b286 + m.b287 + m.b288 + m.b289 + m.b290 + m.b291 + m.b292 +
    m.b293 + m.b294 + m.b295 + m.b296 + m.b297 + m.b298 + m.b299 + m.b300 == 1)
m.e491 = Constraint(expr= m.b1 + m.b31 + m.b61 + m.b91 + m.b121 + m.b151 +
    m.b181 + m.b211 + m.b241 + m.b271 <= 1)
m.e492 = Constraint(expr= m.b2 + m.b32 + m.b62 + m.b92 + m.b122 + m.b152 +
    m.b182 + m.b212 + m.b242 + m.b272 <= 1)
m.e493 = Constraint(expr= m.b3 + m.b33 + m.b63 + m.b93 + m.b123 + m.b153 +
    m.b183 + m.b213 + m.b243 + m.b273 <= 1)
m.e494 = Constraint(expr= m.b4 + m.b34 + m.b64 + m.b94 + m.b124 + m.b154 +
    m.b184 + m.b214 + m.b244 + m.b274 <= 1)
m.e495 = Constraint(expr= m.b5 + m.b35 + m.b65 + m.b95 + m.b125 + m.b155 +
    m.b185 + m.b215 + m.b245 + m.b275 <= 1)
m.e496 = Constraint(expr= m.b6 + m.b36 + m.b66 + m.b96 + m.b126 + m.b156 +
    m.b186 + m.b216 + m.b246 + m.b276 <= 1)
m.e497 = Constraint(expr= m.b7 + m.b37 + m.b67 + m.b97 + m.b127 + m.b157 +
    m.b187 + m.b217 + m.b247 + m.b277 <= 1)
m.e498 = Constraint(expr= m.b8 + m.b38 + m.b68 + m.b98 + m.b128 + m.b158 +
    m.b188 + m.b218 + m.b248 + m.b278 <= 1)
m.e499 = Constraint(expr= m.b9 + m.b39 + m.b69 + m.b99 + m.b129 + m.b159 +
    m.b189 + m.b219 + m.b249 + m.b279 <= 1)
m.e500 = Constraint(expr= m.b10 + m.b40 + m.b70 + m.b100 + m.b130 + m.b160 +
    m.b190 + m.b220 + m.b250 + m.b280 <= 1)
m.e501 = Constraint(expr= m.b11 + m.b41 + m.b71 + m.b101 + m.b131 + m.b161 +
    m.b191 + m.b221 + m.b251 + m.b281 <= 1)
m.e502 = Constraint(expr= m.b12 + m.b42 + m.b72 + m.b102 + m.b132 + m.b162 +
    m.b192 + m.b222 + m.b252 + m.b282 <= 1)
m.e503 = Constraint(expr= m.b13 + m.b43 + m.b73 + m.b103 + m.b133 + m.b163 +
    m.b193 + m.b223 + m.b253 + m.b283 <= 1)
m.e504 = Constraint(expr= m.b14 + m.b44 + m.b74 + m.b104 + m.b134 + m.b164 +
    m.b194 + m.b224 + m.b254 + m.b284 <= 1)
m.e505 = Constraint(expr= m.b15 + m.b45 + m.b75 + m.b105 + m.b135 + m.b165 +
    m.b195 + m.b225 + m.b255 + m.b285 <= 1)
m.e506 = Constraint(expr= m.b16 + m.b46 + m.b76 + m.b106 + m.b136 + m.b166 +
    m.b196 + m.b226 + m.b256 + m.b286 <= 1)
m.e507 = Constraint(expr= m.b17 + m.b47 + m.b77 + m.b107 + m.b137 + m.b167 +
    m.b197 + m.b227 + m.b257 + m.b287 <= 1)
m.e508 = Constraint(expr= m.b18 + m.b48 + m.b78 + m.b108 + m.b138 + m.b168 +
    m.b198 + m.b228 + m.b258 + m.b288 <= 1)
m.e509 = Constraint(expr= m.b19 + m.b49 + m.b79 + m.b109 + m.b139 + m.b169 +
    m.b199 + m.b229 + m.b259 + m.b289 <= 1)
m.e510 = Constraint(expr= m.b20 + m.b50 + m.b80 + m.b110 + m.b140 + m.b170 +
    m.b200 + m.b230 + m.b260 + m.b290 <= 1)
m.e511 = Constraint(expr= m.b21 + m.b51 + m.b81 + m.b111 + m.b141 + m.b171 +
    m.b201 + m.b231 + m.b261 + m.b291 <= 1)
m.e512 = Constraint(expr= m.b22 + m.b52 + m.b82 + m.b112 + m.b142 + m.b172 +
    m.b202 + m.b232 + m.b262 + m.b292 <= 1)
m.e513 = Constraint(expr= m.b23 + m.b53 + m.b83 + m.b113 + m.b143 + m.b173 +
    m.b203 + m.b233 + m.b263 + m.b293 <= 1)
m.e514 = Constraint(expr= m.b24 + m.b54 + m.b84 + m.b114 + m.b144 + m.b174 +
    m.b204 + m.b234 + m.b264 + m.b294 <= 1)
m.e515 = Constraint(expr= m.b25 + m.b55 + m.b85 + m.b115 + m.b145 + m.b175 +
    m.b205 + m.b235 + m.b265 + m.b295 <= 1)
m.e516 = Constraint(expr= m.b26 + m.b56 + m.b86 + m.b116 + m.b146 + m.b176 +
    m.b206 + m.b236 + m.b266 + m.b296 <= 1)
m.e517 = Constraint(expr= m.b27 + m.b57 + m.b87 + m.b117 + m.b147 + m.b177 +
    m.b207 + m.b237 + m.b267 + m.b297 <= 1)
m.e518 = Constraint(expr= m.b28 + m.b58 + m.b88 + m.b118 + m.b148 + m.b178 +
    m.b208 + m.b238 + m.b268 + m.b298 <= 1)
m.e519 = Constraint(expr= m.b29 + m.b59 + m.b89 + m.b119 + m.b149 + m.b179 +
    m.b209 + m.b239 + m.b269 + m.b299 <= 1)
m.e520 = Constraint(expr= m.b30 + m.b60 + m.b90 + m.b120 + m.b150 + m.b180 +
    m.b210 + m.b240 + m.b270 + m.b300 <= 1)
m.e521 = Constraint(expr= m.x301 - m.x302 <= 0)
m.e522 = Constraint(expr= m.x302 - m.x307 <= 0)
m.e523 = Constraint(expr= m.x307 - m.x311 <= 0)
m.e524 = Constraint(expr= m.x311 - m.x315 <= 0)
m.e525 = Constraint(expr= m.x315 - m.x319 <= 0)
m.e526 = Constraint(expr= m.x319 - m.x323 <= 0)
m.e527 = Constraint(expr= m.x323 - m.x327 <= 0)
m.e528 = Constraint(expr= m.x327 - m.x331 <= 0)
m.e529 = Constraint(expr= m.x331 - m.x335 <= 0)
