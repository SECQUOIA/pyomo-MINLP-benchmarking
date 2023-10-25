# MINLP written by GAMS Convert at 05/07/21 17:12:59
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       149        5        0      144        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       110       60       50        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       598      398      200
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

m.obj = Objective(sense=minimize, expr= m.x53 + m.x56 + m.x59 + m.x62 + m.x64
    + m.x66 + m.x68 + m.x70 + m.x72 + m.x74 + m.x76 + m.x78 + m.x80 + m.x82 +
    m.x84 + m.x86 + m.x87 + m.x88 + m.x89 + m.x90 + m.x91 + m.x92 + m.x93 +
    m.x94 + m.x95 + m.x96 + m.x97 + m.x98 + m.x99 + m.x100 + m.x101 + m.x102 +
    m.x103 + m.x104 + m.x105 + m.x106 + m.x107 + m.x108 + m.x109 + m.x110)

m.e1 = Constraint(expr= m.x51 - m.x52 - m.x53 <= 0)
m.e2 = Constraint(expr= -m.x51 + m.x52 - m.x53 <= 0)
m.e3 = Constraint(expr= m.x54 - m.x55 - m.x56 <= 0)
m.e4 = Constraint(expr= -m.x54 + m.x55 - m.x56 <= 0)
m.e5 = Constraint(expr= m.x57 - m.x58 - m.x59 <= 0)
m.e6 = Constraint(expr= -m.x57 + m.x58 - m.x59 <= 0)
m.e7 = Constraint(expr= m.x60 - m.x61 - m.x62 <= 0)
m.e8 = Constraint(expr= -m.x60 + m.x61 - m.x62 <= 0)
m.e9 = Constraint(expr= m.x51 - m.x63 - m.x64 <= 0)
m.e10 = Constraint(expr= -m.x51 + m.x63 - m.x64 <= 0)
m.e11 = Constraint(expr= m.x54 - m.x65 - m.x66 <= 0)
m.e12 = Constraint(expr= -m.x54 + m.x65 - m.x66 <= 0)
m.e13 = Constraint(expr= m.x57 - m.x67 - m.x68 <= 0)
m.e14 = Constraint(expr= -m.x57 + m.x67 - m.x68 <= 0)
m.e15 = Constraint(expr= m.x60 - m.x69 - m.x70 <= 0)
m.e16 = Constraint(expr= -m.x60 + m.x69 - m.x70 <= 0)
m.e17 = Constraint(expr= m.x51 - m.x71 - m.x72 <= 0)
m.e18 = Constraint(expr= -m.x51 + m.x71 - m.x72 <= 0)
m.e19 = Constraint(expr= m.x54 - m.x73 - m.x74 <= 0)
m.e20 = Constraint(expr= -m.x54 + m.x73 - m.x74 <= 0)
m.e21 = Constraint(expr= m.x57 - m.x75 - m.x76 <= 0)
m.e22 = Constraint(expr= -m.x57 + m.x75 - m.x76 <= 0)
m.e23 = Constraint(expr= m.x60 - m.x77 - m.x78 <= 0)
m.e24 = Constraint(expr= -m.x60 + m.x77 - m.x78 <= 0)
m.e25 = Constraint(expr= m.x51 - m.x79 - m.x80 <= 0)
m.e26 = Constraint(expr= -m.x51 + m.x79 - m.x80 <= 0)
m.e27 = Constraint(expr= m.x54 - m.x81 - m.x82 <= 0)
m.e28 = Constraint(expr= -m.x54 + m.x81 - m.x82 <= 0)
m.e29 = Constraint(expr= m.x57 - m.x83 - m.x84 <= 0)
m.e30 = Constraint(expr= -m.x57 + m.x83 - m.x84 <= 0)
m.e31 = Constraint(expr= m.x60 - m.x85 - m.x86 <= 0)
m.e32 = Constraint(expr= -m.x60 + m.x85 - m.x86 <= 0)
m.e33 = Constraint(expr= m.x52 - m.x63 - m.x87 <= 0)
m.e34 = Constraint(expr= -m.x52 + m.x63 - m.x87 <= 0)
m.e35 = Constraint(expr= m.x55 - m.x65 - m.x88 <= 0)
m.e36 = Constraint(expr= -m.x55 + m.x65 - m.x88 <= 0)
m.e37 = Constraint(expr= m.x58 - m.x67 - m.x89 <= 0)
m.e38 = Constraint(expr= -m.x58 + m.x67 - m.x89 <= 0)
m.e39 = Constraint(expr= m.x61 - m.x69 - m.x90 <= 0)
m.e40 = Constraint(expr= -m.x61 + m.x69 - m.x90 <= 0)
m.e41 = Constraint(expr= m.x52 - m.x71 - m.x91 <= 0)
m.e42 = Constraint(expr= -m.x52 + m.x71 - m.x91 <= 0)
m.e43 = Constraint(expr= m.x55 - m.x73 - m.x92 <= 0)
m.e44 = Constraint(expr= -m.x55 + m.x73 - m.x92 <= 0)
m.e45 = Constraint(expr= m.x58 - m.x75 - m.x93 <= 0)
m.e46 = Constraint(expr= -m.x58 + m.x75 - m.x93 <= 0)
m.e47 = Constraint(expr= m.x61 - m.x77 - m.x94 <= 0)
m.e48 = Constraint(expr= -m.x61 + m.x77 - m.x94 <= 0)
m.e49 = Constraint(expr= m.x52 - m.x79 - m.x95 <= 0)
m.e50 = Constraint(expr= -m.x52 + m.x79 - m.x95 <= 0)
m.e51 = Constraint(expr= m.x55 - m.x81 - m.x96 <= 0)
m.e52 = Constraint(expr= -m.x55 + m.x81 - m.x96 <= 0)
m.e53 = Constraint(expr= m.x58 - m.x83 - m.x97 <= 0)
m.e54 = Constraint(expr= -m.x58 + m.x83 - m.x97 <= 0)
m.e55 = Constraint(expr= m.x61 - m.x85 - m.x98 <= 0)
m.e56 = Constraint(expr= -m.x61 + m.x85 - m.x98 <= 0)
m.e57 = Constraint(expr= m.x63 - m.x71 - m.x99 <= 0)
m.e58 = Constraint(expr= -m.x63 + m.x71 - m.x99 <= 0)
m.e59 = Constraint(expr= m.x65 - m.x73 - m.x100 <= 0)
m.e60 = Constraint(expr= -m.x65 + m.x73 - m.x100 <= 0)
m.e61 = Constraint(expr= m.x67 - m.x75 - m.x101 <= 0)
m.e62 = Constraint(expr= -m.x67 + m.x75 - m.x101 <= 0)
m.e63 = Constraint(expr= m.x69 - m.x77 - m.x102 <= 0)
m.e64 = Constraint(expr= -m.x69 + m.x77 - m.x102 <= 0)
m.e65 = Constraint(expr= m.x63 - m.x79 - m.x103 <= 0)
m.e66 = Constraint(expr= -m.x63 + m.x79 - m.x103 <= 0)
m.e67 = Constraint(expr= m.x65 - m.x81 - m.x104 <= 0)
m.e68 = Constraint(expr= -m.x65 + m.x81 - m.x104 <= 0)
m.e69 = Constraint(expr= m.x67 - m.x83 - m.x105 <= 0)
m.e70 = Constraint(expr= -m.x67 + m.x83 - m.x105 <= 0)
m.e71 = Constraint(expr= m.x69 - m.x85 - m.x106 <= 0)
m.e72 = Constraint(expr= -m.x69 + m.x85 - m.x106 <= 0)
m.e73 = Constraint(expr= m.x71 - m.x79 - m.x107 <= 0)
m.e74 = Constraint(expr= -m.x71 + m.x79 - m.x107 <= 0)
m.e75 = Constraint(expr= m.x73 - m.x81 - m.x108 <= 0)
m.e76 = Constraint(expr= -m.x73 + m.x81 - m.x108 <= 0)
m.e77 = Constraint(expr= m.x75 - m.x83 - m.x109 <= 0)
m.e78 = Constraint(expr= -m.x75 + m.x83 - m.x109 <= 0)
m.e79 = Constraint(expr= m.x77 - m.x85 - m.x110 <= 0)
m.e80 = Constraint(expr= -m.x77 + m.x85 - m.x110 <= 0)
m.e81 = Constraint(expr= (0.305036966445776 - m.x51)**2 + (0.634555091335016 -
    m.x54)**2 + (6.814471824267 - m.x57)**2 + (9.81321087468808 - m.x60)**2 +
    238.813652394403 * m.b1 <= 239.813652394403)
m.e82 = Constraint(expr= (9.87450535964623 - m.x51)**2 + (8.74510685597449 -
    m.x54)**2 + (6.66545658580281 - m.x57)**2 + (2.5700184949339 - m.x60)**2 +
    238.813652394403 * m.b2 <= 239.813652394403)
m.e83 = Constraint(expr= (2.82885264202444 - m.x51)**2 + (8.4688333544494 -
    m.x54)**2 + (5.84225640580202 - m.x57)**2 + (1.07461001324769 - m.x60)**2
    + 169.141574969208 * m.b3 <= 170.141574969208)
m.e84 = Constraint(expr= (0.650176203261921 - m.x51)**2 + (3.12451267411524 -
    m.x54)**2 + (7.75486658597646 - m.x57)**2 + (3.46468314918323 - m.x60)**2
    + 152.543792630283 * m.b4 <= 153.543792630283)
m.e85 = Constraint(expr= (2.16828333327622 - m.x51)**2 + (4.30483407264652 -
    m.x54)**2 + (6.42640527388037 - m.x57)**2 + (4.13540922307827 - m.x60)**2
    + 111.116543819038 * m.b5 <= 112.116543819038)
m.e86 = Constraint(expr= (6.57828234352298 - m.x51)**2 + (9.35099743244299 -
    m.x54)**2 + (8.54696402332509 - m.x57)**2 + (5.04321305427267 - m.x60)**2
    + 164.840172521363 * m.b6 <= 165.840172521363)
m.e87 = Constraint(expr= (0.121730249080358 - m.x51)**2 + (5.5819132952254 -
    m.x54)**2 + (1.11962957591948 - m.x57)**2 + (8.91043826758874 - m.x60)**2
    + 202.618528872578 * m.b7 <= 203.618528872578)
m.e88 = Constraint(expr= (8.98297692267813 - m.x51)**2 + (1.57278944121016 -
    m.x54)**2 + (0.373424527008207 - m.x57)**2 + (5.31728541389757 - m.x60)**2
    + 161.372451489157 * m.b8 <= 162.372451489157)
m.e89 = Constraint(expr= (3.80876590973847 - m.x51)**2 + (4.52554072865087 -
    m.x54)**2 + (2.95832977799596 - m.x57)**2 + (2.45196796627015 - m.x60)**2
    + 116.117810910536 * m.b9 <= 117.117810910536)
m.e90 = Constraint(expr= (1.8357554909519 - m.x51)**2 + (7.66347281114004 -
    m.x54)**2 + (6.23276665994841 - m.x57)**2 + (9.07661262817776 - m.x60)**2
    + 160.022562645954 * m.b10 <= 161.022562645954)
m.e91 = Constraint(expr= m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8
    + m.b9 + m.b10 == 1)
m.e92 = Constraint(expr= (0.305036966445776 - m.x52)**2 + (0.634555091335016 -
    m.x55)**2 + (6.814471824267 - m.x58)**2 + (9.81321087468808 - m.x61)**2 +
    238.813652394403 * m.b11 <= 239.813652394403)
m.e93 = Constraint(expr= (9.87450535964623 - m.x52)**2 + (8.74510685597449 -
    m.x55)**2 + (6.66545658580281 - m.x58)**2 + (2.5700184949339 - m.x61)**2 +
    238.813652394403 * m.b12 <= 239.813652394403)
m.e94 = Constraint(expr= (2.82885264202444 - m.x52)**2 + (8.4688333544494 -
    m.x55)**2 + (5.84225640580202 - m.x58)**2 + (1.07461001324769 - m.x61)**2
    + 169.141574969208 * m.b13 <= 170.141574969208)
m.e95 = Constraint(expr= (0.650176203261921 - m.x52)**2 + (3.12451267411524 -
    m.x55)**2 + (7.75486658597646 - m.x58)**2 + (3.46468314918323 - m.x61)**2
    + 152.543792630283 * m.b14 <= 153.543792630283)
m.e96 = Constraint(expr= (2.16828333327622 - m.x52)**2 + (4.30483407264652 -
    m.x55)**2 + (6.42640527388037 - m.x58)**2 + (4.13540922307827 - m.x61)**2
    + 111.116543819038 * m.b15 <= 112.116543819038)
m.e97 = Constraint(expr= (6.57828234352298 - m.x52)**2 + (9.35099743244299 -
    m.x55)**2 + (8.54696402332509 - m.x58)**2 + (5.04321305427267 - m.x61)**2
    + 164.840172521363 * m.b16 <= 165.840172521363)
m.e98 = Constraint(expr= (0.121730249080358 - m.x52)**2 + (5.5819132952254 -
    m.x55)**2 + (1.11962957591948 - m.x58)**2 + (8.91043826758874 - m.x61)**2
    + 202.618528872578 * m.b17 <= 203.618528872578)
m.e99 = Constraint(expr= (8.98297692267813 - m.x52)**2 + (1.57278944121016 -
    m.x55)**2 + (0.373424527008207 - m.x58)**2 + (5.31728541389757 - m.x61)**2
    + 161.372451489157 * m.b18 <= 162.372451489157)
m.e100 = Constraint(expr= (3.80876590973847 - m.x52)**2 + (4.52554072865087 -
    m.x55)**2 + (2.95832977799596 - m.x58)**2 + (2.45196796627015 - m.x61)**2
    + 116.117810910536 * m.b19 <= 117.117810910536)
m.e101 = Constraint(expr= (1.8357554909519 - m.x52)**2 + (7.66347281114004 -
    m.x55)**2 + (6.23276665994841 - m.x58)**2 + (9.07661262817776 - m.x61)**2
    + 160.022562645954 * m.b20 <= 161.022562645954)
m.e102 = Constraint(expr= m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17
    + m.b18 + m.b19 + m.b20 == 1)
m.e103 = Constraint(expr= (0.305036966445776 - m.x63)**2 + (0.634555091335016
    - m.x65)**2 + (6.814471824267 - m.x67)**2 + (9.81321087468808 - m.x69)**2
    + 238.813652394403 * m.b21 <= 239.813652394403)
m.e104 = Constraint(expr= (9.87450535964623 - m.x63)**2 + (8.74510685597449 -
    m.x65)**2 + (6.66545658580281 - m.x67)**2 + (2.5700184949339 - m.x69)**2 +
    238.813652394403 * m.b22 <= 239.813652394403)
m.e105 = Constraint(expr= (2.82885264202444 - m.x63)**2 + (8.4688333544494 -
    m.x65)**2 + (5.84225640580202 - m.x67)**2 + (1.07461001324769 - m.x69)**2
    + 169.141574969208 * m.b23 <= 170.141574969208)
m.e106 = Constraint(expr= (0.650176203261921 - m.x63)**2 + (3.12451267411524 -
    m.x65)**2 + (7.75486658597646 - m.x67)**2 + (3.46468314918323 - m.x69)**2
    + 152.543792630283 * m.b24 <= 153.543792630283)
m.e107 = Constraint(expr= (2.16828333327622 - m.x63)**2 + (4.30483407264652 -
    m.x65)**2 + (6.42640527388037 - m.x67)**2 + (4.13540922307827 - m.x69)**2
    + 111.116543819038 * m.b25 <= 112.116543819038)
m.e108 = Constraint(expr= (6.57828234352298 - m.x63)**2 + (9.35099743244299 -
    m.x65)**2 + (8.54696402332509 - m.x67)**2 + (5.04321305427267 - m.x69)**2
    + 164.840172521363 * m.b26 <= 165.840172521363)
m.e109 = Constraint(expr= (0.121730249080358 - m.x63)**2 + (5.5819132952254 -
    m.x65)**2 + (1.11962957591948 - m.x67)**2 + (8.91043826758874 - m.x69)**2
    + 202.618528872578 * m.b27 <= 203.618528872578)
m.e110 = Constraint(expr= (8.98297692267813 - m.x63)**2 + (1.57278944121016 -
    m.x65)**2 + (0.373424527008207 - m.x67)**2 + (5.31728541389757 - m.x69)**2
    + 161.372451489157 * m.b28 <= 162.372451489157)
m.e111 = Constraint(expr= (3.80876590973847 - m.x63)**2 + (4.52554072865087 -
    m.x65)**2 + (2.95832977799596 - m.x67)**2 + (2.45196796627015 - m.x69)**2
    + 116.117810910536 * m.b29 <= 117.117810910536)
m.e112 = Constraint(expr= (1.8357554909519 - m.x63)**2 + (7.66347281114004 -
    m.x65)**2 + (6.23276665994841 - m.x67)**2 + (9.07661262817776 - m.x69)**2
    + 160.022562645954 * m.b30 <= 161.022562645954)
m.e113 = Constraint(expr= m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 + m.b27
    + m.b28 + m.b29 + m.b30 == 1)
m.e114 = Constraint(expr= (0.305036966445776 - m.x71)**2 + (0.634555091335016
    - m.x73)**2 + (6.814471824267 - m.x75)**2 + (9.81321087468808 - m.x77)**2
    + 238.813652394403 * m.b31 <= 239.813652394403)
m.e115 = Constraint(expr= (9.87450535964623 - m.x71)**2 + (8.74510685597449 -
    m.x73)**2 + (6.66545658580281 - m.x75)**2 + (2.5700184949339 - m.x77)**2 +
    238.813652394403 * m.b32 <= 239.813652394403)
m.e116 = Constraint(expr= (2.82885264202444 - m.x71)**2 + (8.4688333544494 -
    m.x73)**2 + (5.84225640580202 - m.x75)**2 + (1.07461001324769 - m.x77)**2
    + 169.141574969208 * m.b33 <= 170.141574969208)
m.e117 = Constraint(expr= (0.650176203261921 - m.x71)**2 + (3.12451267411524 -
    m.x73)**2 + (7.75486658597646 - m.x75)**2 + (3.46468314918323 - m.x77)**2
    + 152.543792630283 * m.b34 <= 153.543792630283)
m.e118 = Constraint(expr= (2.16828333327622 - m.x71)**2 + (4.30483407264652 -
    m.x73)**2 + (6.42640527388037 - m.x75)**2 + (4.13540922307827 - m.x77)**2
    + 111.116543819038 * m.b35 <= 112.116543819038)
m.e119 = Constraint(expr= (6.57828234352298 - m.x71)**2 + (9.35099743244299 -
    m.x73)**2 + (8.54696402332509 - m.x75)**2 + (5.04321305427267 - m.x77)**2
    + 164.840172521363 * m.b36 <= 165.840172521363)
m.e120 = Constraint(expr= (0.121730249080358 - m.x71)**2 + (5.5819132952254 -
    m.x73)**2 + (1.11962957591948 - m.x75)**2 + (8.91043826758874 - m.x77)**2
    + 202.618528872578 * m.b37 <= 203.618528872578)
m.e121 = Constraint(expr= (8.98297692267813 - m.x71)**2 + (1.57278944121016 -
    m.x73)**2 + (0.373424527008207 - m.x75)**2 + (5.31728541389757 - m.x77)**2
    + 161.372451489157 * m.b38 <= 162.372451489157)
m.e122 = Constraint(expr= (3.80876590973847 - m.x71)**2 + (4.52554072865087 -
    m.x73)**2 + (2.95832977799596 - m.x75)**2 + (2.45196796627015 - m.x77)**2
    + 116.117810910536 * m.b39 <= 117.117810910536)
m.e123 = Constraint(expr= (1.8357554909519 - m.x71)**2 + (7.66347281114004 -
    m.x73)**2 + (6.23276665994841 - m.x75)**2 + (9.07661262817776 - m.x77)**2
    + 160.022562645954 * m.b40 <= 161.022562645954)
m.e124 = Constraint(expr= m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 + m.b37
    + m.b38 + m.b39 + m.b40 == 1)
m.e125 = Constraint(expr= (0.305036966445776 - m.x79)**2 + (0.634555091335016
    - m.x81)**2 + (6.814471824267 - m.x83)**2 + (9.81321087468808 - m.x85)**2
    + 238.813652394403 * m.b41 <= 239.813652394403)
m.e126 = Constraint(expr= (9.87450535964623 - m.x79)**2 + (8.74510685597449 -
    m.x81)**2 + (6.66545658580281 - m.x83)**2 + (2.5700184949339 - m.x85)**2 +
    238.813652394403 * m.b42 <= 239.813652394403)
m.e127 = Constraint(expr= (2.82885264202444 - m.x79)**2 + (8.4688333544494 -
    m.x81)**2 + (5.84225640580202 - m.x83)**2 + (1.07461001324769 - m.x85)**2
    + 169.141574969208 * m.b43 <= 170.141574969208)
m.e128 = Constraint(expr= (0.650176203261921 - m.x79)**2 + (3.12451267411524 -
    m.x81)**2 + (7.75486658597646 - m.x83)**2 + (3.46468314918323 - m.x85)**2
    + 152.543792630283 * m.b44 <= 153.543792630283)
m.e129 = Constraint(expr= (2.16828333327622 - m.x79)**2 + (4.30483407264652 -
    m.x81)**2 + (6.42640527388037 - m.x83)**2 + (4.13540922307827 - m.x85)**2
    + 111.116543819038 * m.b45 <= 112.116543819038)
m.e130 = Constraint(expr= (6.57828234352298 - m.x79)**2 + (9.35099743244299 -
    m.x81)**2 + (8.54696402332509 - m.x83)**2 + (5.04321305427267 - m.x85)**2
    + 164.840172521363 * m.b46 <= 165.840172521363)
m.e131 = Constraint(expr= (0.121730249080358 - m.x79)**2 + (5.5819132952254 -
    m.x81)**2 + (1.11962957591948 - m.x83)**2 + (8.91043826758874 - m.x85)**2
    + 202.618528872578 * m.b47 <= 203.618528872578)
m.e132 = Constraint(expr= (8.98297692267813 - m.x79)**2 + (1.57278944121016 -
    m.x81)**2 + (0.373424527008207 - m.x83)**2 + (5.31728541389757 - m.x85)**2
    + 161.372451489157 * m.b48 <= 162.372451489157)
m.e133 = Constraint(expr= (3.80876590973847 - m.x79)**2 + (4.52554072865087 -
    m.x81)**2 + (2.95832977799596 - m.x83)**2 + (2.45196796627015 - m.x85)**2
    + 116.117810910536 * m.b49 <= 117.117810910536)
m.e134 = Constraint(expr= (1.8357554909519 - m.x79)**2 + (7.66347281114004 -
    m.x81)**2 + (6.23276665994841 - m.x83)**2 + (9.07661262817776 - m.x85)**2
    + 160.022562645954 * m.b50 <= 161.022562645954)
m.e135 = Constraint(expr= m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47
    + m.b48 + m.b49 + m.b50 == 1)
m.e136 = Constraint(expr= m.b1 + m.b11 + m.b21 + m.b31 + m.b41 <= 1)
m.e137 = Constraint(expr= m.b2 + m.b12 + m.b22 + m.b32 + m.b42 <= 1)
m.e138 = Constraint(expr= m.b3 + m.b13 + m.b23 + m.b33 + m.b43 <= 1)
m.e139 = Constraint(expr= m.b4 + m.b14 + m.b24 + m.b34 + m.b44 <= 1)
m.e140 = Constraint(expr= m.b5 + m.b15 + m.b25 + m.b35 + m.b45 <= 1)
m.e141 = Constraint(expr= m.b6 + m.b16 + m.b26 + m.b36 + m.b46 <= 1)
m.e142 = Constraint(expr= m.b7 + m.b17 + m.b27 + m.b37 + m.b47 <= 1)
m.e143 = Constraint(expr= m.b8 + m.b18 + m.b28 + m.b38 + m.b48 <= 1)
m.e144 = Constraint(expr= m.b9 + m.b19 + m.b29 + m.b39 + m.b49 <= 1)
m.e145 = Constraint(expr= m.b10 + m.b20 + m.b30 + m.b40 + m.b50 <= 1)
m.e146 = Constraint(expr= m.x51 - m.x52 <= 0)
m.e147 = Constraint(expr= m.x52 - m.x63 <= 0)
m.e148 = Constraint(expr= m.x63 - m.x71 <= 0)
m.e149 = Constraint(expr= m.x71 - m.x79 <= 0)
