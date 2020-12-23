#  MINLP written by GAMS Convert at 08/20/20 01:30:51
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        468       72       24      372        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        216      144       72        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1790     1278      512        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x74 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x75 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x76 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x77 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x78 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x82 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x83 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x84 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x85 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x86 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.b90 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b91 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b92 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b93 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b94 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b95 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b96 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b97 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b98 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b99 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b147 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b150 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b152 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x160 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x161 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x162 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x163 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x164 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x165 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x166 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x167 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x168 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x169 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x170 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x171 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x172 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x173 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,2),initialize=0)
m.b183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x185 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x186 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x187 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x188 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x189 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x190 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x191 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x192 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x193 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x197 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x198 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x199 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x200 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x201 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x202 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x203 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x204 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x205 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x206 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x207 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x208 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x209 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x215 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x216 = Var(within=Reals,bounds=(0,0.92),initialize=0)

m.obj = Objective(expr= - 0.45*m.x2 - 0.45*m.x3 - 0.45*m.x4 - 0.67*m.x5 - 0.67*m.x6 - 0.67*m.x7 - 1.03*m.x8 - 1.03*m.x9
                        - 1.03*m.x10 - 1.75*m.x11 - 1.75*m.x12 - 1.75*m.x13 - 1.57*m.x14 - 1.57*m.x15 - 1.57*m.x16
                        - 1.05*m.x17 - 1.05*m.x18 - 1.05*m.x19 - 0.13*m.x20 - 0.13*m.x21 - 0.13*m.x22 - 0.47*m.x23
                        - 0.47*m.x24 - 0.47*m.x25 - 0.34*m.x26 - 0.34*m.x27 - 0.34*m.x28 + 8.81*m.x29 + 8.81*m.x30
                        + 9.07*m.x31 + 9.07*m.x32 - 0.6*m.x33 - 0.6*m.x34 - 0.6*m.x35 - 0.65*m.x36 - 0.65*m.x37
                        - 0.65*m.x38 - 0.75*m.x39 - 0.75*m.x40 - 0.75*m.x41 + 9.52*m.x42 + 9.52*m.x43 + 9.52*m.x44
                        + 8.69*m.x45 + 8.69*m.x46 - 0.83*m.x47 - 0.83*m.x48 - 0.83*m.x49 - m.x50 - m.x51 - m.x52
                        - 0.44*m.x53 - 0.44*m.x54 - 0.44*m.x55 + 8.64*m.x56 + 8.64*m.x57 + 8.64*m.x58 + 8.83*m.x59
                        + 8.83*m.x60 - 0.87*m.x61 - 0.87*m.x62 - 0.87*m.x63 - 0.4*m.x64 - 0.4*m.x65 - 0.4*m.x66
                        - 0.8*m.x67 - 0.8*m.x68 - 0.8*m.x69 + 8.69*m.x70 + 8.69*m.x71 + 9.34*m.x72 + 9.34*m.x73
                        - 0.2*m.b90 - 0.2*m.b91 - 0.2*m.b92 - 0.62*m.b93 - 0.62*m.b94 - 0.62*m.b95 - 0.35*m.b96
                        - 0.35*m.b97 - 0.35*m.b98 - 0.76*m.b99 - 0.76*m.b100 - 0.76*m.b101 - 0.38*m.b102 - 0.38*m.b103
                        - 0.38*m.b104 - 0.08*m.b105 - 0.08*m.b106 - 0.08*m.b107 - 0.93*m.b108 - 0.93*m.b109
                        - 0.93*m.b110 - 0.57*m.b111 - 0.57*m.b112 - 0.57*m.b113 - 0.01*m.b114 - 0.01*m.b115
                        - 0.01*m.b116 - 0.16*m.b117 - 0.16*m.b118 - 0.31*m.b119 - 0.31*m.b120 - 0.17*m.b121
                        - 0.17*m.b122 - 0.17*m.b123 - 0.26*m.b124 - 0.26*m.b125 - 0.26*m.b126 - 0.69*m.b127
                        - 0.69*m.b128 - 0.69*m.b129 - 0.45*m.b130 - 0.45*m.b131 - 0.45*m.b132 - 0.23*m.b133
                        - 0.23*m.b134 - 0.15*m.b135 - 0.15*m.b136 - 0.15*m.b137 - 0.54*m.b138 - 0.54*m.b139
                        - 0.54*m.b140 - 0.08*m.b141 - 0.08*m.b142 - 0.08*m.b143 - 0.11*m.b144 - 0.11*m.b145
                        - 0.11*m.b146 - 0.82*m.b147 - 0.82*m.b148 - 0.82*m.b149 - 0.08*m.b150 - 0.08*m.b151
                        - 0.08*m.b152 - 0.26*m.b153 - 0.26*m.b154 - 0.26*m.b155 - 0.43*m.b156 - 0.43*m.b157
                        - 0.18*m.b158 - 0.18*m.b159, sense=maximize)

m.c2 = Constraint(expr=   m.x2 + m.x5 + m.x8 + m.x160 == 1.9)

m.c3 = Constraint(expr=   m.x11 + m.x14 + m.x17 + m.x161 == 1.8)

m.c4 = Constraint(expr= - m.x11 + m.x20 + m.x23 + m.x26 - m.x33 - m.x47 - m.x61 + m.x162 == 0.3)

m.c5 = Constraint(expr= - m.x2 - m.x14 - m.x20 + m.x33 + m.x36 + m.x39 + m.x42 - m.x50 - m.x64 + m.x163 == 1.8)

m.c6 = Constraint(expr= - m.x5 - m.x17 - m.x23 - m.x36 + m.x47 + m.x50 + m.x53 + m.x56 - m.x67 + m.x164 == 1.3)

m.c7 = Constraint(expr= - m.x8 - m.x26 - m.x39 - m.x53 + m.x61 + m.x64 + m.x67 + m.x165 == 0.2)

m.c8 = Constraint(expr= - m.x42 - m.x56 + m.x166 == -0.35)

m.c9 = Constraint(expr=   m.x3 + m.x6 + m.x9 - m.x160 + m.x167 == 0.1)

m.c10 = Constraint(expr=   m.x4 + m.x7 + m.x10 - m.x167 + m.x168 == 0.7)

m.c11 = Constraint(expr=   m.x12 + m.x15 + m.x18 - m.x161 + m.x169 == 0.8)

m.c12 = Constraint(expr=   m.x13 + m.x16 + m.x19 - m.x169 + m.x170 == 0.3)

m.c13 = Constraint(expr= - m.x12 + m.x21 + m.x24 + m.x27 + m.x29 + m.x31 - m.x34 - m.x48 - m.x62 - m.x162 + m.x171 == 0)

m.c14 = Constraint(expr= - m.x13 + m.x22 + m.x25 + m.x28 + m.x30 + m.x32 - m.x35 - m.x49 - m.x63 - m.x171 + m.x172 == 0)

m.c15 = Constraint(expr= - m.x3 - m.x15 - m.x21 + m.x34 + m.x37 + m.x40 + m.x43 + m.x45 - m.x51 - m.x65 - m.x163
                         + m.x173 == 0)

m.c16 = Constraint(expr= - m.x4 - m.x16 - m.x22 + m.x35 + m.x38 + m.x41 + m.x44 + m.x46 - m.x52 - m.x66 - m.x173
                         + m.x174 == 0)

m.c17 = Constraint(expr= - m.x6 - m.x18 - m.x24 - m.x37 + m.x48 + m.x51 + m.x54 + m.x57 + m.x59 - m.x68 - m.x164
                         + m.x175 == 0)

m.c18 = Constraint(expr= - m.x7 - m.x19 - m.x25 - m.x38 + m.x49 + m.x52 + m.x55 + m.x58 + m.x60 - m.x69 - m.x175
                         + m.x176 == 0)

m.c19 = Constraint(expr= - m.x9 - m.x27 - m.x40 - m.x54 + m.x62 + m.x65 + m.x68 + m.x70 + m.x72 - m.x165 + m.x177 == 0)

m.c20 = Constraint(expr= - m.x10 - m.x28 - m.x41 - m.x55 + m.x63 + m.x66 + m.x69 + m.x71 + m.x73 - m.x177 + m.x178 == 0)

m.c21 = Constraint(expr= - m.x29 - m.x43 - m.x57 - m.x70 - m.x166 + m.x179 == -0.44)

m.c22 = Constraint(expr= - m.x30 - m.x44 - m.x58 - m.x71 - m.x179 + m.x180 == -0.77)

m.c23 = Constraint(expr= - m.x31 - m.x45 - m.x59 - m.x72 + m.x181 == 0.69)

m.c24 = Constraint(expr= - m.x32 - m.x46 - m.x60 - m.x73 - m.x181 + m.x182 == -0.8)

m.c25 = Constraint(expr=   m.x2 - m.b90 <= 0)

m.c26 = Constraint(expr=   m.x3 - m.b91 <= 0)

m.c27 = Constraint(expr=   m.x4 - m.b92 <= 0)

m.c28 = Constraint(expr=   m.x5 - m.b93 <= 0)

m.c29 = Constraint(expr=   m.x6 - m.b94 <= 0)

m.c30 = Constraint(expr=   m.x7 - m.b95 <= 0)

m.c31 = Constraint(expr=   m.x8 - m.b96 <= 0)

m.c32 = Constraint(expr=   m.x9 - m.b97 <= 0)

m.c33 = Constraint(expr=   m.x10 - m.b98 <= 0)

m.c34 = Constraint(expr=   m.x11 - m.b99 <= 0)

m.c35 = Constraint(expr=   m.x12 - m.b100 <= 0)

m.c36 = Constraint(expr=   m.x13 - m.b101 <= 0)

m.c37 = Constraint(expr=   m.x14 - m.b102 <= 0)

m.c38 = Constraint(expr=   m.x15 - m.b103 <= 0)

m.c39 = Constraint(expr=   m.x16 - m.b104 <= 0)

m.c40 = Constraint(expr=   m.x17 - m.b105 <= 0)

m.c41 = Constraint(expr=   m.x18 - m.b106 <= 0)

m.c42 = Constraint(expr=   m.x19 - m.b107 <= 0)

m.c43 = Constraint(expr=   m.x20 - m.b108 <= 0)

m.c44 = Constraint(expr=   m.x21 - m.b109 <= 0)

m.c45 = Constraint(expr=   m.x22 - m.b110 <= 0)

m.c46 = Constraint(expr=   m.x23 - m.b111 <= 0)

m.c47 = Constraint(expr=   m.x24 - m.b112 <= 0)

m.c48 = Constraint(expr=   m.x25 - m.b113 <= 0)

m.c49 = Constraint(expr=   m.x26 - m.b114 <= 0)

m.c50 = Constraint(expr=   m.x27 - m.b115 <= 0)

m.c51 = Constraint(expr=   m.x28 - m.b116 <= 0)

m.c52 = Constraint(expr=   m.x29 - m.b117 <= 0)

m.c53 = Constraint(expr=   m.x30 - m.b118 <= 0)

m.c54 = Constraint(expr=   m.x31 - m.b119 <= 0)

m.c55 = Constraint(expr=   m.x32 - m.b120 <= 0)

m.c56 = Constraint(expr=   m.x33 - m.b121 <= 0)

m.c57 = Constraint(expr=   m.x34 - m.b122 <= 0)

m.c58 = Constraint(expr=   m.x35 - m.b123 <= 0)

m.c59 = Constraint(expr=   m.x36 - m.b124 <= 0)

m.c60 = Constraint(expr=   m.x37 - m.b125 <= 0)

m.c61 = Constraint(expr=   m.x38 - m.b126 <= 0)

m.c62 = Constraint(expr=   m.x39 - m.b127 <= 0)

m.c63 = Constraint(expr=   m.x40 - m.b128 <= 0)

m.c64 = Constraint(expr=   m.x41 - m.b129 <= 0)

m.c65 = Constraint(expr=   m.x42 - m.b130 <= 0)

m.c66 = Constraint(expr=   m.x43 - m.b131 <= 0)

m.c67 = Constraint(expr=   m.x44 - m.b132 <= 0)

m.c68 = Constraint(expr=   m.x45 - m.b133 <= 0)

m.c69 = Constraint(expr=   m.x46 - m.b134 <= 0)

m.c70 = Constraint(expr=   m.x47 - m.b135 <= 0)

m.c71 = Constraint(expr=   m.x48 - m.b136 <= 0)

m.c72 = Constraint(expr=   m.x49 - m.b137 <= 0)

m.c73 = Constraint(expr=   m.x50 - m.b138 <= 0)

m.c74 = Constraint(expr=   m.x51 - m.b139 <= 0)

m.c75 = Constraint(expr=   m.x52 - m.b140 <= 0)

m.c76 = Constraint(expr=   m.x53 - m.b141 <= 0)

m.c77 = Constraint(expr=   m.x54 - m.b142 <= 0)

m.c78 = Constraint(expr=   m.x55 - m.b143 <= 0)

m.c79 = Constraint(expr=   m.x56 - m.b144 <= 0)

m.c80 = Constraint(expr=   m.x57 - m.b145 <= 0)

m.c81 = Constraint(expr=   m.x58 - m.b146 <= 0)

m.c82 = Constraint(expr=   m.x59 - m.b183 <= 0)

m.c83 = Constraint(expr=   m.x60 - m.b184 <= 0)

m.c84 = Constraint(expr=   m.x61 - m.b147 <= 0)

m.c85 = Constraint(expr=   m.x62 - m.b148 <= 0)

m.c86 = Constraint(expr=   m.x63 - m.b149 <= 0)

m.c87 = Constraint(expr=   m.x64 - m.b150 <= 0)

m.c88 = Constraint(expr=   m.x65 - m.b151 <= 0)

m.c89 = Constraint(expr=   m.x66 - m.b152 <= 0)

m.c90 = Constraint(expr=   m.x67 - m.b153 <= 0)

m.c91 = Constraint(expr=   m.x68 - m.b154 <= 0)

m.c92 = Constraint(expr=   m.x69 - m.b155 <= 0)

m.c93 = Constraint(expr=   m.x70 - m.b156 <= 0)

m.c94 = Constraint(expr=   m.x71 - m.b157 <= 0)

m.c95 = Constraint(expr=   m.x72 - m.b158 <= 0)

m.c96 = Constraint(expr=   m.x73 - m.b159 <= 0)

m.c97 = Constraint(expr=   0.1*m.b119 - m.x185 <= -0.7)

m.c98 = Constraint(expr=   0.1*m.b120 - m.x186 <= -0.7)

m.c99 = Constraint(expr=   0.1*m.b133 - m.x187 <= -0.7)

m.c100 = Constraint(expr=   0.1*m.b134 - m.x188 <= -0.7)

m.c101 = Constraint(expr=   0.1*m.b183 - m.x189 <= -0.7)

m.c102 = Constraint(expr=   0.1*m.b184 - m.x190 <= -0.7)

m.c103 = Constraint(expr=   0.1*m.b158 - m.x191 <= -0.7)

m.c104 = Constraint(expr=   0.1*m.b159 - m.x192 <= -0.7)

m.c105 = Constraint(expr=   0.5*m.b117 - m.x193 <= 0)

m.c106 = Constraint(expr=   0.5*m.b118 - m.x194 <= 0)

m.c107 = Constraint(expr=   0.1*m.b119 - m.x193 <= 0)

m.c108 = Constraint(expr=   0.1*m.b120 - m.x194 <= 0)

m.c109 = Constraint(expr=   0.5*m.b131 - m.x195 <= 0)

m.c110 = Constraint(expr=   0.5*m.b132 - m.x196 <= 0)

m.c111 = Constraint(expr=   0.1*m.b133 - m.x195 <= 0)

m.c112 = Constraint(expr=   0.1*m.b134 - m.x196 <= 0)

m.c113 = Constraint(expr=   0.5*m.b145 - m.x197 <= 0)

m.c114 = Constraint(expr=   0.5*m.b146 - m.x198 <= 0)

m.c115 = Constraint(expr=   0.1*m.b183 - m.x197 <= 0)

m.c116 = Constraint(expr=   0.1*m.b184 - m.x198 <= 0)

m.c117 = Constraint(expr=   0.5*m.b156 - m.x199 <= 0)

m.c118 = Constraint(expr=   0.5*m.b157 - m.x200 <= 0)

m.c119 = Constraint(expr=   0.1*m.b158 - m.x199 <= 0)

m.c120 = Constraint(expr=   0.1*m.b159 - m.x200 <= 0)

m.c121 = Constraint(expr=   0.05*m.b117 - m.x201 <= -0.66)

m.c122 = Constraint(expr=   0.05*m.b118 - m.x202 <= -0.66)

m.c123 = Constraint(expr=   0.13*m.b119 - m.x201 <= -0.66)

m.c124 = Constraint(expr=   0.13*m.b120 - m.x202 <= -0.66)

m.c125 = Constraint(expr=   0.05*m.b131 - m.x203 <= -0.66)

m.c126 = Constraint(expr=   0.05*m.b132 - m.x204 <= -0.66)

m.c127 = Constraint(expr=   0.13*m.b133 - m.x203 <= -0.66)

m.c128 = Constraint(expr=   0.13*m.b134 - m.x204 <= -0.66)

m.c129 = Constraint(expr=   0.05*m.b145 - m.x205 <= -0.66)

m.c130 = Constraint(expr=   0.05*m.b146 - m.x206 <= -0.66)

m.c131 = Constraint(expr=   0.13*m.b183 - m.x205 <= -0.66)

m.c132 = Constraint(expr=   0.13*m.b184 - m.x206 <= -0.66)

m.c133 = Constraint(expr=   0.05*m.b156 - m.x207 <= -0.66)

m.c134 = Constraint(expr=   0.05*m.b157 - m.x208 <= -0.66)

m.c135 = Constraint(expr=   0.13*m.b158 - m.x207 <= -0.66)

m.c136 = Constraint(expr=   0.13*m.b159 - m.x208 <= -0.66)

m.c137 = Constraint(expr=   0.48*m.b117 - m.x209 <= 0)

m.c138 = Constraint(expr=   0.48*m.b118 - m.x210 <= 0)

m.c139 = Constraint(expr=   0.09*m.b119 - m.x209 <= 0)

m.c140 = Constraint(expr=   0.09*m.b120 - m.x210 <= 0)

m.c141 = Constraint(expr=   0.48*m.b131 - m.x211 <= 0)

m.c142 = Constraint(expr=   0.48*m.b132 - m.x212 <= 0)

m.c143 = Constraint(expr=   0.09*m.b133 - m.x211 <= 0)

m.c144 = Constraint(expr=   0.09*m.b134 - m.x212 <= 0)

m.c145 = Constraint(expr=   0.48*m.b145 - m.x213 <= 0)

m.c146 = Constraint(expr=   0.48*m.b146 - m.x214 <= 0)

m.c147 = Constraint(expr=   0.09*m.b183 - m.x213 <= 0)

m.c148 = Constraint(expr=   0.09*m.b184 - m.x214 <= 0)

m.c149 = Constraint(expr=   0.48*m.b156 - m.x215 <= 0)

m.c150 = Constraint(expr=   0.48*m.b157 - m.x216 <= 0)

m.c151 = Constraint(expr=   0.09*m.b158 - m.x215 <= 0)

m.c152 = Constraint(expr=   0.09*m.b159 - m.x216 <= 0)

m.c153 = Constraint(expr= - 0.2*m.b119 - m.x193 >= -0.9)

m.c154 = Constraint(expr= - 0.2*m.b120 - m.x194 >= -0.9)

m.c155 = Constraint(expr= - 0.2*m.b133 - m.x195 >= -0.9)

m.c156 = Constraint(expr= - 0.2*m.b134 - m.x196 >= -0.9)

m.c157 = Constraint(expr= - 0.2*m.b183 - m.x197 >= -0.9)

m.c158 = Constraint(expr= - 0.2*m.b184 - m.x198 >= -0.9)

m.c159 = Constraint(expr= - 0.2*m.b158 - m.x199 >= -0.9)

m.c160 = Constraint(expr= - 0.2*m.b159 - m.x200 >= -0.9)

m.c161 = Constraint(expr= - 0.05*m.b117 - m.x201 >= -1)

m.c162 = Constraint(expr= - 0.05*m.b118 - m.x202 >= -1)

m.c163 = Constraint(expr= - 0.05*m.b131 - m.x203 >= -1)

m.c164 = Constraint(expr= - 0.05*m.b132 - m.x204 >= -1)

m.c165 = Constraint(expr= - 0.05*m.b145 - m.x205 >= -1)

m.c166 = Constraint(expr= - 0.05*m.b146 - m.x206 >= -1)

m.c167 = Constraint(expr= - 0.05*m.b156 - m.x207 >= -1)

m.c168 = Constraint(expr= - 0.05*m.b157 - m.x208 >= -1)

m.c169 = Constraint(expr= - 0.12*m.b119 - m.x209 >= -0.92)

m.c170 = Constraint(expr= - 0.12*m.b120 - m.x210 >= -0.92)

m.c171 = Constraint(expr= - 0.12*m.b133 - m.x211 >= -0.92)

m.c172 = Constraint(expr= - 0.12*m.b134 - m.x212 >= -0.92)

m.c173 = Constraint(expr= - 0.12*m.b183 - m.x213 >= -0.92)

m.c174 = Constraint(expr= - 0.12*m.b184 - m.x214 >= -0.92)

m.c175 = Constraint(expr= - 0.12*m.b158 - m.x215 >= -0.92)

m.c176 = Constraint(expr= - 0.12*m.b159 - m.x216 >= -0.92)

m.c177 = Constraint(expr=   m.b99 + m.b108 <= 1)

m.c178 = Constraint(expr=   m.b100 + m.b109 <= 1)

m.c179 = Constraint(expr=   m.b101 + m.b110 <= 1)

m.c180 = Constraint(expr=   m.b99 + m.b111 <= 1)

m.c181 = Constraint(expr=   m.b100 + m.b112 <= 1)

m.c182 = Constraint(expr=   m.b101 + m.b113 <= 1)

m.c183 = Constraint(expr=   m.b99 + m.b114 <= 1)

m.c184 = Constraint(expr=   m.b100 + m.b115 <= 1)

m.c185 = Constraint(expr=   m.b101 + m.b116 <= 1)

m.c186 = Constraint(expr=   m.b100 + m.b117 <= 1)

m.c187 = Constraint(expr=   m.b101 + m.b118 <= 1)

m.c188 = Constraint(expr=   m.b100 + m.b119 <= 1)

m.c189 = Constraint(expr=   m.b101 + m.b120 <= 1)

m.c190 = Constraint(expr=   m.b108 + m.b121 <= 1)

m.c191 = Constraint(expr=   m.b109 + m.b122 <= 1)

m.c192 = Constraint(expr=   m.b110 + m.b123 <= 1)

m.c193 = Constraint(expr=   m.b111 + m.b121 <= 1)

m.c194 = Constraint(expr=   m.b112 + m.b122 <= 1)

m.c195 = Constraint(expr=   m.b113 + m.b123 <= 1)

m.c196 = Constraint(expr=   m.b114 + m.b121 <= 1)

m.c197 = Constraint(expr=   m.b115 + m.b122 <= 1)

m.c198 = Constraint(expr=   m.b116 + m.b123 <= 1)

m.c199 = Constraint(expr=   m.b117 + m.b122 <= 1)

m.c200 = Constraint(expr=   m.b118 + m.b123 <= 1)

m.c201 = Constraint(expr=   m.b119 + m.b122 <= 1)

m.c202 = Constraint(expr=   m.b120 + m.b123 <= 1)

m.c203 = Constraint(expr=   m.b108 + m.b135 <= 1)

m.c204 = Constraint(expr=   m.b109 + m.b136 <= 1)

m.c205 = Constraint(expr=   m.b110 + m.b137 <= 1)

m.c206 = Constraint(expr=   m.b111 + m.b135 <= 1)

m.c207 = Constraint(expr=   m.b112 + m.b136 <= 1)

m.c208 = Constraint(expr=   m.b113 + m.b137 <= 1)

m.c209 = Constraint(expr=   m.b114 + m.b135 <= 1)

m.c210 = Constraint(expr=   m.b115 + m.b136 <= 1)

m.c211 = Constraint(expr=   m.b116 + m.b137 <= 1)

m.c212 = Constraint(expr=   m.b117 + m.b136 <= 1)

m.c213 = Constraint(expr=   m.b118 + m.b137 <= 1)

m.c214 = Constraint(expr=   m.b119 + m.b136 <= 1)

m.c215 = Constraint(expr=   m.b120 + m.b137 <= 1)

m.c216 = Constraint(expr=   m.b108 + m.b147 <= 1)

m.c217 = Constraint(expr=   m.b109 + m.b148 <= 1)

m.c218 = Constraint(expr=   m.b110 + m.b149 <= 1)

m.c219 = Constraint(expr=   m.b111 + m.b147 <= 1)

m.c220 = Constraint(expr=   m.b112 + m.b148 <= 1)

m.c221 = Constraint(expr=   m.b113 + m.b149 <= 1)

m.c222 = Constraint(expr=   m.b114 + m.b147 <= 1)

m.c223 = Constraint(expr=   m.b115 + m.b148 <= 1)

m.c224 = Constraint(expr=   m.b116 + m.b149 <= 1)

m.c225 = Constraint(expr=   m.b117 + m.b148 <= 1)

m.c226 = Constraint(expr=   m.b118 + m.b149 <= 1)

m.c227 = Constraint(expr=   m.b119 + m.b148 <= 1)

m.c228 = Constraint(expr=   m.b120 + m.b149 <= 1)

m.c229 = Constraint(expr=   m.b90 + m.b121 <= 1)

m.c230 = Constraint(expr=   m.b91 + m.b122 <= 1)

m.c231 = Constraint(expr=   m.b92 + m.b123 <= 1)

m.c232 = Constraint(expr=   m.b90 + m.b124 <= 1)

m.c233 = Constraint(expr=   m.b91 + m.b125 <= 1)

m.c234 = Constraint(expr=   m.b92 + m.b126 <= 1)

m.c235 = Constraint(expr=   m.b90 + m.b127 <= 1)

m.c236 = Constraint(expr=   m.b91 + m.b128 <= 1)

m.c237 = Constraint(expr=   m.b92 + m.b129 <= 1)

m.c238 = Constraint(expr=   m.b90 + m.b130 <= 1)

m.c239 = Constraint(expr=   m.b91 + m.b131 <= 1)

m.c240 = Constraint(expr=   m.b92 + m.b132 <= 1)

m.c241 = Constraint(expr=   m.b91 + m.b133 <= 1)

m.c242 = Constraint(expr=   m.b92 + m.b134 <= 1)

m.c243 = Constraint(expr=   m.b102 + m.b121 <= 1)

m.c244 = Constraint(expr=   m.b103 + m.b122 <= 1)

m.c245 = Constraint(expr=   m.b104 + m.b123 <= 1)

m.c246 = Constraint(expr=   m.b102 + m.b124 <= 1)

m.c247 = Constraint(expr=   m.b103 + m.b125 <= 1)

m.c248 = Constraint(expr=   m.b104 + m.b126 <= 1)

m.c249 = Constraint(expr=   m.b102 + m.b127 <= 1)

m.c250 = Constraint(expr=   m.b103 + m.b128 <= 1)

m.c251 = Constraint(expr=   m.b104 + m.b129 <= 1)

m.c252 = Constraint(expr=   m.b102 + m.b130 <= 1)

m.c253 = Constraint(expr=   m.b103 + m.b131 <= 1)

m.c254 = Constraint(expr=   m.b104 + m.b132 <= 1)

m.c255 = Constraint(expr=   m.b103 + m.b133 <= 1)

m.c256 = Constraint(expr=   m.b104 + m.b134 <= 1)

m.c257 = Constraint(expr=   m.b108 + m.b121 <= 1)

m.c258 = Constraint(expr=   m.b109 + m.b122 <= 1)

m.c259 = Constraint(expr=   m.b110 + m.b123 <= 1)

m.c260 = Constraint(expr=   m.b108 + m.b124 <= 1)

m.c261 = Constraint(expr=   m.b109 + m.b125 <= 1)

m.c262 = Constraint(expr=   m.b110 + m.b126 <= 1)

m.c263 = Constraint(expr=   m.b108 + m.b127 <= 1)

m.c264 = Constraint(expr=   m.b109 + m.b128 <= 1)

m.c265 = Constraint(expr=   m.b110 + m.b129 <= 1)

m.c266 = Constraint(expr=   m.b108 + m.b130 <= 1)

m.c267 = Constraint(expr=   m.b109 + m.b131 <= 1)

m.c268 = Constraint(expr=   m.b110 + m.b132 <= 1)

m.c269 = Constraint(expr=   m.b109 + m.b133 <= 1)

m.c270 = Constraint(expr=   m.b110 + m.b134 <= 1)

m.c271 = Constraint(expr=   m.b121 + m.b138 <= 1)

m.c272 = Constraint(expr=   m.b122 + m.b139 <= 1)

m.c273 = Constraint(expr=   m.b123 + m.b140 <= 1)

m.c274 = Constraint(expr=   m.b124 + m.b138 <= 1)

m.c275 = Constraint(expr=   m.b125 + m.b139 <= 1)

m.c276 = Constraint(expr=   m.b126 + m.b140 <= 1)

m.c277 = Constraint(expr=   m.b127 + m.b138 <= 1)

m.c278 = Constraint(expr=   m.b128 + m.b139 <= 1)

m.c279 = Constraint(expr=   m.b129 + m.b140 <= 1)

m.c280 = Constraint(expr=   m.b130 + m.b138 <= 1)

m.c281 = Constraint(expr=   m.b131 + m.b139 <= 1)

m.c282 = Constraint(expr=   m.b132 + m.b140 <= 1)

m.c283 = Constraint(expr=   m.b133 + m.b139 <= 1)

m.c284 = Constraint(expr=   m.b134 + m.b140 <= 1)

m.c285 = Constraint(expr=   m.b121 + m.b150 <= 1)

m.c286 = Constraint(expr=   m.b122 + m.b151 <= 1)

m.c287 = Constraint(expr=   m.b123 + m.b152 <= 1)

m.c288 = Constraint(expr=   m.b124 + m.b150 <= 1)

m.c289 = Constraint(expr=   m.b125 + m.b151 <= 1)

m.c290 = Constraint(expr=   m.b126 + m.b152 <= 1)

m.c291 = Constraint(expr=   m.b127 + m.b150 <= 1)

m.c292 = Constraint(expr=   m.b128 + m.b151 <= 1)

m.c293 = Constraint(expr=   m.b129 + m.b152 <= 1)

m.c294 = Constraint(expr=   m.b130 + m.b150 <= 1)

m.c295 = Constraint(expr=   m.b131 + m.b151 <= 1)

m.c296 = Constraint(expr=   m.b132 + m.b152 <= 1)

m.c297 = Constraint(expr=   m.b133 + m.b151 <= 1)

m.c298 = Constraint(expr=   m.b134 + m.b152 <= 1)

m.c299 = Constraint(expr=   m.b93 + m.b135 <= 1)

m.c300 = Constraint(expr=   m.b94 + m.b136 <= 1)

m.c301 = Constraint(expr=   m.b95 + m.b137 <= 1)

m.c302 = Constraint(expr=   m.b93 + m.b138 <= 1)

m.c303 = Constraint(expr=   m.b94 + m.b139 <= 1)

m.c304 = Constraint(expr=   m.b95 + m.b140 <= 1)

m.c305 = Constraint(expr=   m.b93 + m.b141 <= 1)

m.c306 = Constraint(expr=   m.b94 + m.b142 <= 1)

m.c307 = Constraint(expr=   m.b95 + m.b143 <= 1)

m.c308 = Constraint(expr=   m.b93 + m.b144 <= 1)

m.c309 = Constraint(expr=   m.b94 + m.b145 <= 1)

m.c310 = Constraint(expr=   m.b95 + m.b146 <= 1)

m.c311 = Constraint(expr=   m.b94 + m.b183 <= 1)

m.c312 = Constraint(expr=   m.b95 + m.b184 <= 1)

m.c313 = Constraint(expr=   m.b105 + m.b135 <= 1)

m.c314 = Constraint(expr=   m.b106 + m.b136 <= 1)

m.c315 = Constraint(expr=   m.b107 + m.b137 <= 1)

m.c316 = Constraint(expr=   m.b105 + m.b138 <= 1)

m.c317 = Constraint(expr=   m.b106 + m.b139 <= 1)

m.c318 = Constraint(expr=   m.b107 + m.b140 <= 1)

m.c319 = Constraint(expr=   m.b105 + m.b141 <= 1)

m.c320 = Constraint(expr=   m.b106 + m.b142 <= 1)

m.c321 = Constraint(expr=   m.b107 + m.b143 <= 1)

m.c322 = Constraint(expr=   m.b105 + m.b144 <= 1)

m.c323 = Constraint(expr=   m.b106 + m.b145 <= 1)

m.c324 = Constraint(expr=   m.b107 + m.b146 <= 1)

m.c325 = Constraint(expr=   m.b106 + m.b183 <= 1)

m.c326 = Constraint(expr=   m.b107 + m.b184 <= 1)

m.c327 = Constraint(expr=   m.b111 + m.b135 <= 1)

m.c328 = Constraint(expr=   m.b112 + m.b136 <= 1)

m.c329 = Constraint(expr=   m.b113 + m.b137 <= 1)

m.c330 = Constraint(expr=   m.b111 + m.b138 <= 1)

m.c331 = Constraint(expr=   m.b112 + m.b139 <= 1)

m.c332 = Constraint(expr=   m.b113 + m.b140 <= 1)

m.c333 = Constraint(expr=   m.b111 + m.b141 <= 1)

m.c334 = Constraint(expr=   m.b112 + m.b142 <= 1)

m.c335 = Constraint(expr=   m.b113 + m.b143 <= 1)

m.c336 = Constraint(expr=   m.b111 + m.b144 <= 1)

m.c337 = Constraint(expr=   m.b112 + m.b145 <= 1)

m.c338 = Constraint(expr=   m.b113 + m.b146 <= 1)

m.c339 = Constraint(expr=   m.b112 + m.b183 <= 1)

m.c340 = Constraint(expr=   m.b113 + m.b184 <= 1)

m.c341 = Constraint(expr=   m.b124 + m.b135 <= 1)

m.c342 = Constraint(expr=   m.b125 + m.b136 <= 1)

m.c343 = Constraint(expr=   m.b126 + m.b137 <= 1)

m.c344 = Constraint(expr=   m.b124 + m.b138 <= 1)

m.c345 = Constraint(expr=   m.b125 + m.b139 <= 1)

m.c346 = Constraint(expr=   m.b126 + m.b140 <= 1)

m.c347 = Constraint(expr=   m.b124 + m.b141 <= 1)

m.c348 = Constraint(expr=   m.b125 + m.b142 <= 1)

m.c349 = Constraint(expr=   m.b126 + m.b143 <= 1)

m.c350 = Constraint(expr=   m.b124 + m.b144 <= 1)

m.c351 = Constraint(expr=   m.b125 + m.b145 <= 1)

m.c352 = Constraint(expr=   m.b126 + m.b146 <= 1)

m.c353 = Constraint(expr=   m.b125 + m.b183 <= 1)

m.c354 = Constraint(expr=   m.b126 + m.b184 <= 1)

m.c355 = Constraint(expr=   m.b135 + m.b153 <= 1)

m.c356 = Constraint(expr=   m.b136 + m.b154 <= 1)

m.c357 = Constraint(expr=   m.b137 + m.b155 <= 1)

m.c358 = Constraint(expr=   m.b138 + m.b153 <= 1)

m.c359 = Constraint(expr=   m.b139 + m.b154 <= 1)

m.c360 = Constraint(expr=   m.b140 + m.b155 <= 1)

m.c361 = Constraint(expr=   m.b141 + m.b153 <= 1)

m.c362 = Constraint(expr=   m.b142 + m.b154 <= 1)

m.c363 = Constraint(expr=   m.b143 + m.b155 <= 1)

m.c364 = Constraint(expr=   m.b144 + m.b153 <= 1)

m.c365 = Constraint(expr=   m.b145 + m.b154 <= 1)

m.c366 = Constraint(expr=   m.b146 + m.b155 <= 1)

m.c367 = Constraint(expr=   m.b154 + m.b183 <= 1)

m.c368 = Constraint(expr=   m.b155 + m.b184 <= 1)

m.c369 = Constraint(expr=   m.b96 + m.b147 <= 1)

m.c370 = Constraint(expr=   m.b97 + m.b148 <= 1)

m.c371 = Constraint(expr=   m.b98 + m.b149 <= 1)

m.c372 = Constraint(expr=   m.b96 + m.b150 <= 1)

m.c373 = Constraint(expr=   m.b97 + m.b151 <= 1)

m.c374 = Constraint(expr=   m.b98 + m.b152 <= 1)

m.c375 = Constraint(expr=   m.b96 + m.b153 <= 1)

m.c376 = Constraint(expr=   m.b97 + m.b154 <= 1)

m.c377 = Constraint(expr=   m.b98 + m.b155 <= 1)

m.c378 = Constraint(expr=   m.b97 + m.b156 <= 1)

m.c379 = Constraint(expr=   m.b98 + m.b157 <= 1)

m.c380 = Constraint(expr=   m.b97 + m.b158 <= 1)

m.c381 = Constraint(expr=   m.b98 + m.b159 <= 1)

m.c382 = Constraint(expr=   m.b114 + m.b147 <= 1)

m.c383 = Constraint(expr=   m.b115 + m.b148 <= 1)

m.c384 = Constraint(expr=   m.b116 + m.b149 <= 1)

m.c385 = Constraint(expr=   m.b114 + m.b150 <= 1)

m.c386 = Constraint(expr=   m.b115 + m.b151 <= 1)

m.c387 = Constraint(expr=   m.b116 + m.b152 <= 1)

m.c388 = Constraint(expr=   m.b114 + m.b153 <= 1)

m.c389 = Constraint(expr=   m.b115 + m.b154 <= 1)

m.c390 = Constraint(expr=   m.b116 + m.b155 <= 1)

m.c391 = Constraint(expr=   m.b115 + m.b156 <= 1)

m.c392 = Constraint(expr=   m.b116 + m.b157 <= 1)

m.c393 = Constraint(expr=   m.b115 + m.b158 <= 1)

m.c394 = Constraint(expr=   m.b116 + m.b159 <= 1)

m.c395 = Constraint(expr=   m.b127 + m.b147 <= 1)

m.c396 = Constraint(expr=   m.b128 + m.b148 <= 1)

m.c397 = Constraint(expr=   m.b129 + m.b149 <= 1)

m.c398 = Constraint(expr=   m.b127 + m.b150 <= 1)

m.c399 = Constraint(expr=   m.b128 + m.b151 <= 1)

m.c400 = Constraint(expr=   m.b129 + m.b152 <= 1)

m.c401 = Constraint(expr=   m.b127 + m.b153 <= 1)

m.c402 = Constraint(expr=   m.b128 + m.b154 <= 1)

m.c403 = Constraint(expr=   m.b129 + m.b155 <= 1)

m.c404 = Constraint(expr=   m.b128 + m.b156 <= 1)

m.c405 = Constraint(expr=   m.b129 + m.b157 <= 1)

m.c406 = Constraint(expr=   m.b128 + m.b158 <= 1)

m.c407 = Constraint(expr=   m.b129 + m.b159 <= 1)

m.c408 = Constraint(expr=   m.b141 + m.b147 <= 1)

m.c409 = Constraint(expr=   m.b142 + m.b148 <= 1)

m.c410 = Constraint(expr=   m.b143 + m.b149 <= 1)

m.c411 = Constraint(expr=   m.b141 + m.b150 <= 1)

m.c412 = Constraint(expr=   m.b142 + m.b151 <= 1)

m.c413 = Constraint(expr=   m.b143 + m.b152 <= 1)

m.c414 = Constraint(expr=   m.b141 + m.b153 <= 1)

m.c415 = Constraint(expr=   m.b142 + m.b154 <= 1)

m.c416 = Constraint(expr=   m.b143 + m.b155 <= 1)

m.c417 = Constraint(expr=   m.b142 + m.b156 <= 1)

m.c418 = Constraint(expr=   m.b143 + m.b157 <= 1)

m.c419 = Constraint(expr=   m.b142 + m.b158 <= 1)

m.c420 = Constraint(expr=   m.b143 + m.b159 <= 1)

m.c421 = Constraint(expr=m.x185*m.x162 - 0.9*m.x11 + 0.7*m.x20 + 0.7*m.x23 + 0.7*m.x26 - 0.8*m.x33 - 0.7*m.x47
                          - 0.7*m.x61 == 0.21)

m.c422 = Constraint(expr=m.x187*m.x163 - 0.7*m.x2 - 0.9*m.x14 - 0.7*m.x20 + 0.8*m.x33 + 0.8*m.x36 + 0.8*m.x39
                          + 0.8*m.x42 - 0.7*m.x50 - 0.7*m.x64 == 1.44)

m.c423 = Constraint(expr=m.x189*m.x164 - 0.7*m.x5 - 0.9*m.x17 - 0.7*m.x23 - 0.8*m.x36 + 0.7*m.x47 + 0.7*m.x50
                          + 0.7*m.x53 + 0.7*m.x56 - 0.7*m.x67 == 0.91)

m.c424 = Constraint(expr=m.x191*m.x165 - 0.7*m.x8 - 0.7*m.x26 - 0.8*m.x39 - 0.7*m.x53 + 0.7*m.x61 + 0.7*m.x64
                          + 0.7*m.x67 == 0.14)

m.c425 = Constraint(expr=m.x193*m.x162 - 0.01*m.x11 - 0.9*m.x33 - 0.8*m.x47 - 0.3*m.x61 == 0)

m.c426 = Constraint(expr=m.x195*m.x163 - 0.2*m.x2 - 0.01*m.x14 + 0.9*m.x33 + 0.9*m.x36 + 0.9*m.x39 + 0.9*m.x42
                          - 0.8*m.x50 - 0.3*m.x64 == 1.62)

m.c427 = Constraint(expr=m.x197*m.x164 - 0.2*m.x5 - 0.01*m.x17 - 0.9*m.x36 + 0.8*m.x47 + 0.8*m.x50 + 0.8*m.x53
                          + 0.8*m.x56 - 0.3*m.x67 == 1.04)

m.c428 = Constraint(expr=m.x199*m.x165 - 0.2*m.x8 - 0.9*m.x39 - 0.8*m.x53 + 0.3*m.x61 + 0.3*m.x64 + 0.3*m.x67 == 0.06)

m.c429 = Constraint(expr=m.x201*m.x162 - 0.88*m.x11 + 0.68*m.x20 + 0.68*m.x23 + 0.68*m.x26 - 0.81*m.x33 - 0.71*m.x47
                          - 0.66*m.x61 == 0.204)

m.c430 = Constraint(expr=m.x203*m.x163 - 0.69*m.x2 - 0.88*m.x14 - 0.68*m.x20 + 0.81*m.x33 + 0.81*m.x36 + 0.81*m.x39
                          + 0.81*m.x42 - 0.71*m.x50 - 0.66*m.x64 == 1.458)

m.c431 = Constraint(expr=m.x205*m.x164 - 0.69*m.x5 - 0.88*m.x17 - 0.68*m.x23 - 0.81*m.x36 + 0.71*m.x47 + 0.71*m.x50
                          + 0.71*m.x53 + 0.71*m.x56 - 0.66*m.x67 == 0.923)

m.c432 = Constraint(expr=m.x207*m.x165 - 0.69*m.x8 - 0.68*m.x26 - 0.81*m.x39 - 0.71*m.x53 + 0.66*m.x61 + 0.66*m.x64
                          + 0.66*m.x67 == 0.132)

m.c433 = Constraint(expr=m.x209*m.x162 + 0.01*m.x20 + 0.01*m.x23 + 0.01*m.x26 - 0.9*m.x33 - 0.8*m.x47 - 0.4*m.x61
                          == 0.003)

m.c434 = Constraint(expr=m.x211*m.x163 - 0.18*m.x2 - 0.01*m.x20 + 0.9*m.x33 + 0.9*m.x36 + 0.9*m.x39 + 0.9*m.x42
                          - 0.8*m.x50 - 0.4*m.x64 == 1.62)

m.c435 = Constraint(expr=m.x213*m.x164 - 0.18*m.x5 - 0.01*m.x23 - 0.9*m.x36 + 0.8*m.x47 + 0.8*m.x50 + 0.8*m.x53
                          + 0.8*m.x56 - 0.4*m.x67 == 1.04)

m.c436 = Constraint(expr=m.x215*m.x165 - 0.18*m.x8 - 0.01*m.x26 - 0.9*m.x39 - 0.8*m.x53 + 0.4*m.x61 + 0.4*m.x64
                          + 0.4*m.x67 == 0.08)

m.c437 = Constraint(expr=m.x185*m.x21 + m.x185*m.x24 + m.x185*m.x27 + m.x185*m.x29 + m.x185*m.x31 - m.x187*m.x34 - 
                         m.x189*m.x48 - m.x191*m.x62 - m.x185*m.x162 + m.x186*m.x171 - 0.9*m.x12 == 0)

m.c438 = Constraint(expr=m.x186*m.x22 + m.x186*m.x25 + m.x186*m.x28 + m.x186*m.x30 + m.x186*m.x32 - m.x188*m.x35 - 
                         m.x190*m.x49 - m.x192*m.x63 + m.x172*m.x74 - m.x186*m.x171 - 0.9*m.x13 == 0)

m.c439 = Constraint(expr=m.x187*m.x34 - m.x185*m.x21 + m.x187*m.x37 + m.x187*m.x40 + m.x187*m.x43 + m.x187*m.x45 - 
                         m.x189*m.x51 - m.x191*m.x65 - m.x187*m.x163 + m.x188*m.x173 - 0.7*m.x3 - 0.9*m.x15 == 0)

m.c440 = Constraint(expr=m.x188*m.x35 - m.x186*m.x22 + m.x188*m.x38 + m.x188*m.x41 + m.x188*m.x44 + m.x188*m.x46 - 
                         m.x190*m.x52 - m.x192*m.x66 + m.x174*m.x75 - m.x188*m.x173 - 0.7*m.x4 - 0.9*m.x16 == 0)

m.c441 = Constraint(expr=(-m.x185*m.x24) - m.x187*m.x37 + m.x189*m.x48 + m.x189*m.x51 + m.x189*m.x54 + m.x189*m.x57 + 
                         m.x189*m.x59 - m.x191*m.x68 - m.x189*m.x164 + m.x190*m.x175 - 0.7*m.x6 - 0.9*m.x18 == 0)

m.c442 = Constraint(expr=(-m.x186*m.x25) - m.x188*m.x38 + m.x190*m.x49 + m.x190*m.x52 + m.x190*m.x55 + m.x190*m.x58 + 
                         m.x190*m.x60 - m.x192*m.x69 + m.x176*m.x76 - m.x190*m.x175 - 0.7*m.x7 - 0.9*m.x19 == 0)

m.c443 = Constraint(expr=(-m.x185*m.x27) - m.x187*m.x40 - m.x189*m.x54 + m.x191*m.x62 + m.x191*m.x65 + m.x191*m.x68 + 
                         m.x191*m.x70 + m.x191*m.x72 - m.x191*m.x165 + m.x192*m.x177 - 0.7*m.x9 == 0)

m.c444 = Constraint(expr=(-m.x186*m.x28) - m.x188*m.x41 - m.x190*m.x55 + m.x192*m.x63 + m.x192*m.x66 + m.x192*m.x69 + 
                         m.x192*m.x71 + m.x192*m.x73 + m.x178*m.x77 - m.x192*m.x177 - 0.7*m.x10 == 0)

m.c445 = Constraint(expr=m.x193*m.x21 + m.x193*m.x24 + m.x193*m.x27 + m.x193*m.x29 + m.x193*m.x31 - m.x195*m.x34 - 
                         m.x197*m.x48 - m.x199*m.x62 - m.x193*m.x162 + m.x194*m.x171 - 0.01*m.x12 == 0)

m.c446 = Constraint(expr=m.x194*m.x22 + m.x194*m.x25 + m.x194*m.x28 + m.x194*m.x30 + m.x194*m.x32 - m.x196*m.x35 - 
                         m.x198*m.x49 - m.x200*m.x63 + m.x172*m.x78 - m.x194*m.x171 - 0.01*m.x13 == 0)

m.c447 = Constraint(expr=m.x195*m.x34 - m.x193*m.x21 + m.x195*m.x37 + m.x195*m.x40 + m.x195*m.x43 + m.x195*m.x45 - 
                         m.x197*m.x51 - m.x199*m.x65 - m.x195*m.x163 + m.x196*m.x173 - 0.2*m.x3 - 0.01*m.x15 == 0)

m.c448 = Constraint(expr=m.x196*m.x35 - m.x194*m.x22 + m.x196*m.x38 + m.x196*m.x41 + m.x196*m.x44 + m.x196*m.x46 - 
                         m.x198*m.x52 - m.x200*m.x66 + m.x174*m.x79 - m.x196*m.x173 - 0.2*m.x4 - 0.01*m.x16 == 0)

m.c449 = Constraint(expr=(-m.x193*m.x24) - m.x195*m.x37 + m.x197*m.x48 + m.x197*m.x51 + m.x197*m.x54 + m.x197*m.x57 + 
                         m.x197*m.x59 - m.x199*m.x68 - m.x197*m.x164 + m.x198*m.x175 - 0.2*m.x6 - 0.01*m.x18 == 0)

m.c450 = Constraint(expr=(-m.x194*m.x25) - m.x196*m.x38 + m.x198*m.x49 + m.x198*m.x52 + m.x198*m.x55 + m.x198*m.x58 + 
                         m.x198*m.x60 - m.x200*m.x69 + m.x176*m.x80 - m.x198*m.x175 - 0.2*m.x7 - 0.01*m.x19 == 0)

m.c451 = Constraint(expr=(-m.x193*m.x27) - m.x195*m.x40 - m.x197*m.x54 + m.x199*m.x62 + m.x199*m.x65 + m.x199*m.x68 + 
                         m.x199*m.x70 + m.x199*m.x72 - m.x199*m.x165 + m.x200*m.x177 - 0.2*m.x9 == 0)

m.c452 = Constraint(expr=(-m.x194*m.x28) - m.x196*m.x41 - m.x198*m.x55 + m.x200*m.x63 + m.x200*m.x66 + m.x200*m.x69 + 
                         m.x200*m.x71 + m.x200*m.x73 + m.x178*m.x81 - m.x200*m.x177 - 0.2*m.x10 == 0)

m.c453 = Constraint(expr=m.x201*m.x21 + m.x201*m.x24 + m.x201*m.x27 + m.x201*m.x29 + m.x201*m.x31 - m.x203*m.x34 - 
                         m.x205*m.x48 - m.x207*m.x62 - m.x201*m.x162 + m.x202*m.x171 - 0.88*m.x12 == 0)

m.c454 = Constraint(expr=m.x202*m.x22 + m.x202*m.x25 + m.x202*m.x28 + m.x202*m.x30 + m.x202*m.x32 - m.x204*m.x35 - 
                         m.x206*m.x49 - m.x208*m.x63 + m.x172*m.x82 - m.x202*m.x171 - 0.88*m.x13 == 0)

m.c455 = Constraint(expr=m.x203*m.x34 - m.x201*m.x21 + m.x203*m.x37 + m.x203*m.x40 + m.x203*m.x43 + m.x203*m.x45 - 
                         m.x205*m.x51 - m.x207*m.x65 - m.x203*m.x163 + m.x204*m.x173 - 0.69*m.x3 - 0.88*m.x15 == 0)

m.c456 = Constraint(expr=m.x204*m.x35 - m.x202*m.x22 + m.x204*m.x38 + m.x204*m.x41 + m.x204*m.x44 + m.x204*m.x46 - 
                         m.x206*m.x52 - m.x208*m.x66 + m.x174*m.x83 - m.x204*m.x173 - 0.69*m.x4 - 0.88*m.x16 == 0)

m.c457 = Constraint(expr=(-m.x201*m.x24) - m.x203*m.x37 + m.x205*m.x48 + m.x205*m.x51 + m.x205*m.x54 + m.x205*m.x57 + 
                         m.x205*m.x59 - m.x207*m.x68 - m.x205*m.x164 + m.x206*m.x175 - 0.69*m.x6 - 0.88*m.x18 == 0)

m.c458 = Constraint(expr=(-m.x202*m.x25) - m.x204*m.x38 + m.x206*m.x49 + m.x206*m.x52 + m.x206*m.x55 + m.x206*m.x58 + 
                         m.x206*m.x60 - m.x208*m.x69 + m.x176*m.x84 - m.x206*m.x175 - 0.69*m.x7 - 0.88*m.x19 == 0)

m.c459 = Constraint(expr=(-m.x201*m.x27) - m.x203*m.x40 - m.x205*m.x54 + m.x207*m.x62 + m.x207*m.x65 + m.x207*m.x68 + 
                         m.x207*m.x70 + m.x207*m.x72 - m.x207*m.x165 + m.x208*m.x177 - 0.69*m.x9 == 0)

m.c460 = Constraint(expr=(-m.x202*m.x28) - m.x204*m.x41 - m.x206*m.x55 + m.x208*m.x63 + m.x208*m.x66 + m.x208*m.x69 + 
                         m.x208*m.x71 + m.x208*m.x73 + m.x178*m.x85 - m.x208*m.x177 - 0.69*m.x10 == 0)

m.c461 = Constraint(expr=m.x211*m.x34 - m.x209*m.x21 + m.x211*m.x37 + m.x211*m.x40 + m.x211*m.x43 + m.x211*m.x45 - 
                         m.x213*m.x51 - m.x215*m.x65 - m.x211*m.x163 + m.x212*m.x173 - 0.18*m.x3 == 0)

m.c462 = Constraint(expr=m.x212*m.x35 - m.x210*m.x22 + m.x212*m.x38 + m.x212*m.x41 + m.x212*m.x44 + m.x212*m.x46 - 
                         m.x214*m.x52 - m.x216*m.x66 + m.x174*m.x87 - m.x212*m.x173 - 0.18*m.x4 == 0)

m.c463 = Constraint(expr=(-m.x209*m.x24) - m.x211*m.x37 + m.x213*m.x48 + m.x213*m.x51 + m.x213*m.x54 + m.x213*m.x57 + 
                         m.x213*m.x59 - m.x215*m.x68 - m.x213*m.x164 + m.x214*m.x175 - 0.18*m.x6 == 0)

m.c464 = Constraint(expr=(-m.x210*m.x25) - m.x212*m.x38 + m.x214*m.x49 + m.x214*m.x52 + m.x214*m.x55 + m.x214*m.x58 + 
                         m.x214*m.x60 - m.x216*m.x69 + m.x176*m.x88 - m.x214*m.x175 - 0.18*m.x7 == 0)

m.c465 = Constraint(expr=(-m.x209*m.x27) - m.x211*m.x40 - m.x213*m.x54 + m.x215*m.x62 + m.x215*m.x65 + m.x215*m.x68 + 
                         m.x215*m.x70 + m.x215*m.x72 - m.x215*m.x165 + m.x216*m.x177 - 0.18*m.x9 == 0)

m.c466 = Constraint(expr=(-m.x210*m.x28) - m.x212*m.x41 - m.x214*m.x55 + m.x216*m.x63 + m.x216*m.x66 + m.x216*m.x69 + 
                         m.x216*m.x71 + m.x216*m.x73 + m.x178*m.x89 - m.x216*m.x177 - 0.18*m.x10 == 0)

m.c467 = Constraint(expr=m.x209*m.x21 + m.x209*m.x24 + m.x209*m.x27 + m.x209*m.x29 + m.x209*m.x31 - m.x211*m.x34 - 
                         m.x213*m.x48 - m.x215*m.x62 - m.x209*m.x162 + m.x210*m.x171 == 0)

m.c468 = Constraint(expr=m.x210*m.x22 + m.x210*m.x25 + m.x210*m.x28 + m.x210*m.x30 + m.x210*m.x32 - m.x212*m.x35 - 
                         m.x214*m.x49 - m.x216*m.x63 + m.x172*m.x86 - m.x210*m.x171 == 0)
