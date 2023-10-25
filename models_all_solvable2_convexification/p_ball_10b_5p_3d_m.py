# MINLP written by GAMS Convert at 05/07/21 17:12:59
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       129        5        0      124        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        95       45       50        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       488      338      150
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

m.obj = Objective(sense=minimize, expr= m.x53 + m.x56 + m.x59 + m.x61 + m.x63
    + m.x65 + m.x67 + m.x69 + m.x71 + m.x73 + m.x75 + m.x77 + m.x78 + m.x79 +
    m.x80 + m.x81 + m.x82 + m.x83 + m.x84 + m.x85 + m.x86 + m.x87 + m.x88 +
    m.x89 + m.x90 + m.x91 + m.x92 + m.x93 + m.x94 + m.x95)

m.e1 = Constraint(expr= m.x51 - m.x52 - m.x53 <= 0)
m.e2 = Constraint(expr= -m.x51 + m.x52 - m.x53 <= 0)
m.e3 = Constraint(expr= m.x54 - m.x55 - m.x56 <= 0)
m.e4 = Constraint(expr= -m.x54 + m.x55 - m.x56 <= 0)
m.e5 = Constraint(expr= m.x57 - m.x58 - m.x59 <= 0)
m.e6 = Constraint(expr= -m.x57 + m.x58 - m.x59 <= 0)
m.e7 = Constraint(expr= m.x51 - m.x60 - m.x61 <= 0)
m.e8 = Constraint(expr= -m.x51 + m.x60 - m.x61 <= 0)
m.e9 = Constraint(expr= m.x54 - m.x62 - m.x63 <= 0)
m.e10 = Constraint(expr= -m.x54 + m.x62 - m.x63 <= 0)
m.e11 = Constraint(expr= m.x57 - m.x64 - m.x65 <= 0)
m.e12 = Constraint(expr= -m.x57 + m.x64 - m.x65 <= 0)
m.e13 = Constraint(expr= m.x51 - m.x66 - m.x67 <= 0)
m.e14 = Constraint(expr= -m.x51 + m.x66 - m.x67 <= 0)
m.e15 = Constraint(expr= m.x54 - m.x68 - m.x69 <= 0)
m.e16 = Constraint(expr= -m.x54 + m.x68 - m.x69 <= 0)
m.e17 = Constraint(expr= m.x57 - m.x70 - m.x71 <= 0)
m.e18 = Constraint(expr= -m.x57 + m.x70 - m.x71 <= 0)
m.e19 = Constraint(expr= m.x51 - m.x72 - m.x73 <= 0)
m.e20 = Constraint(expr= -m.x51 + m.x72 - m.x73 <= 0)
m.e21 = Constraint(expr= m.x54 - m.x74 - m.x75 <= 0)
m.e22 = Constraint(expr= -m.x54 + m.x74 - m.x75 <= 0)
m.e23 = Constraint(expr= m.x57 - m.x76 - m.x77 <= 0)
m.e24 = Constraint(expr= -m.x57 + m.x76 - m.x77 <= 0)
m.e25 = Constraint(expr= m.x52 - m.x60 - m.x78 <= 0)
m.e26 = Constraint(expr= -m.x52 + m.x60 - m.x78 <= 0)
m.e27 = Constraint(expr= m.x55 - m.x62 - m.x79 <= 0)
m.e28 = Constraint(expr= -m.x55 + m.x62 - m.x79 <= 0)
m.e29 = Constraint(expr= m.x58 - m.x64 - m.x80 <= 0)
m.e30 = Constraint(expr= -m.x58 + m.x64 - m.x80 <= 0)
m.e31 = Constraint(expr= m.x52 - m.x66 - m.x81 <= 0)
m.e32 = Constraint(expr= -m.x52 + m.x66 - m.x81 <= 0)
m.e33 = Constraint(expr= m.x55 - m.x68 - m.x82 <= 0)
m.e34 = Constraint(expr= -m.x55 + m.x68 - m.x82 <= 0)
m.e35 = Constraint(expr= m.x58 - m.x70 - m.x83 <= 0)
m.e36 = Constraint(expr= -m.x58 + m.x70 - m.x83 <= 0)
m.e37 = Constraint(expr= m.x52 - m.x72 - m.x84 <= 0)
m.e38 = Constraint(expr= -m.x52 + m.x72 - m.x84 <= 0)
m.e39 = Constraint(expr= m.x55 - m.x74 - m.x85 <= 0)
m.e40 = Constraint(expr= -m.x55 + m.x74 - m.x85 <= 0)
m.e41 = Constraint(expr= m.x58 - m.x76 - m.x86 <= 0)
m.e42 = Constraint(expr= -m.x58 + m.x76 - m.x86 <= 0)
m.e43 = Constraint(expr= m.x60 - m.x66 - m.x87 <= 0)
m.e44 = Constraint(expr= -m.x60 + m.x66 - m.x87 <= 0)
m.e45 = Constraint(expr= m.x62 - m.x68 - m.x88 <= 0)
m.e46 = Constraint(expr= -m.x62 + m.x68 - m.x88 <= 0)
m.e47 = Constraint(expr= m.x64 - m.x70 - m.x89 <= 0)
m.e48 = Constraint(expr= -m.x64 + m.x70 - m.x89 <= 0)
m.e49 = Constraint(expr= m.x60 - m.x72 - m.x90 <= 0)
m.e50 = Constraint(expr= -m.x60 + m.x72 - m.x90 <= 0)
m.e51 = Constraint(expr= m.x62 - m.x74 - m.x91 <= 0)
m.e52 = Constraint(expr= -m.x62 + m.x74 - m.x91 <= 0)
m.e53 = Constraint(expr= m.x64 - m.x76 - m.x92 <= 0)
m.e54 = Constraint(expr= -m.x64 + m.x76 - m.x92 <= 0)
m.e55 = Constraint(expr= m.x66 - m.x72 - m.x93 <= 0)
m.e56 = Constraint(expr= -m.x66 + m.x72 - m.x93 <= 0)
m.e57 = Constraint(expr= m.x68 - m.x74 - m.x94 <= 0)
m.e58 = Constraint(expr= -m.x68 + m.x74 - m.x94 <= 0)
m.e59 = Constraint(expr= m.x70 - m.x76 - m.x95 <= 0)
m.e60 = Constraint(expr= -m.x70 + m.x76 - m.x95 <= 0)
m.e61 = Constraint(expr= (3.55441530772447 - m.x51)**2 + (2.6588399811956 -
    m.x54)**2 + (5.16713392802669 - m.x57)**2 + 128.415159268527 * m.b1
    <= 129.415159268527)
m.e62 = Constraint(expr= (8.82094045941646 - m.x51)**2 + (9.51816335093057 -
    m.x54)**2 + (0.894770759747333 - m.x57)**2 + 136.27463320812 * m.b2
    <= 137.27463320812)
m.e63 = Constraint(expr= (6.86229591973038 - m.x51)**2 + (4.74665709736901 -
    m.x54)**2 + (1.14651582775383 - m.x57)**2 + 79.4930138069821 * m.b3
    <= 80.4930138069821)
m.e64 = Constraint(expr= (7.13880287505566 - m.x51)**2 + (0.923639199248324 -
    m.x54)**2 + (5.06906794010293 - m.x57)**2 + 124.602073729487 * m.b4
    <= 125.602073729487)
m.e65 = Constraint(expr= (9.54873475130122 - m.x51)**2 + (9.730708594994 -
    m.x54)**2 + (0.506682101270036 - m.x57)**2 + 152.575845479968 * m.b5
    <= 153.575845479968)
m.e66 = Constraint(expr= (2.60295575976191 - m.x51)**2 + (9.60525309364094 -
    m.x54)**2 + (5.33059723504087 - m.x57)**2 + 115.609943222472 * m.b6
    <= 116.609943222472)
m.e67 = Constraint(expr= (8.7489239697277 - m.x51)**2 + (6.42418905563567 -
    m.x54)**2 + (6.53764526999883 - m.x57)**2 + 102.276439512632 * m.b7
    <= 103.276439512632)
m.e68 = Constraint(expr= (2.98069751112782 - m.x51)**2 + (1.4913715136506 -
    m.x54)**2 + (2.04987567063475 - m.x57)**2 + 134.705801750617 * m.b8
    <= 135.705801750617)
m.e69 = Constraint(expr= (1.65791995565741 - m.x51)**2 + (6.17322651944292 -
    m.x54)**2 + (7.01412219987569 - m.x57)**2 + 138.925429422844 * m.b9
    <= 139.925429422844)
m.e70 = Constraint(expr= (2.41953526971379 - m.x51)**2 + (1.09500973629707 -
    m.x54)**2 + (2.60189595048839 - m.x57)**2 + 152.575845479968 * m.b10
    <= 153.575845479968)
m.e71 = Constraint(expr= m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8
    + m.b9 + m.b10 == 1)
m.e72 = Constraint(expr= (3.55441530772447 - m.x52)**2 + (2.6588399811956 -
    m.x55)**2 + (5.16713392802669 - m.x58)**2 + 128.415159268527 * m.b11
    <= 129.415159268527)
m.e73 = Constraint(expr= (8.82094045941646 - m.x52)**2 + (9.51816335093057 -
    m.x55)**2 + (0.894770759747333 - m.x58)**2 + 136.27463320812 * m.b12
    <= 137.27463320812)
m.e74 = Constraint(expr= (6.86229591973038 - m.x52)**2 + (4.74665709736901 -
    m.x55)**2 + (1.14651582775383 - m.x58)**2 + 79.4930138069821 * m.b13
    <= 80.4930138069821)
m.e75 = Constraint(expr= (7.13880287505566 - m.x52)**2 + (0.923639199248324 -
    m.x55)**2 + (5.06906794010293 - m.x58)**2 + 124.602073729487 * m.b14
    <= 125.602073729487)
m.e76 = Constraint(expr= (9.54873475130122 - m.x52)**2 + (9.730708594994 -
    m.x55)**2 + (0.506682101270036 - m.x58)**2 + 152.575845479968 * m.b15
    <= 153.575845479968)
m.e77 = Constraint(expr= (2.60295575976191 - m.x52)**2 + (9.60525309364094 -
    m.x55)**2 + (5.33059723504087 - m.x58)**2 + 115.609943222472 * m.b16
    <= 116.609943222472)
m.e78 = Constraint(expr= (8.7489239697277 - m.x52)**2 + (6.42418905563567 -
    m.x55)**2 + (6.53764526999883 - m.x58)**2 + 102.276439512632 * m.b17
    <= 103.276439512632)
m.e79 = Constraint(expr= (2.98069751112782 - m.x52)**2 + (1.4913715136506 -
    m.x55)**2 + (2.04987567063475 - m.x58)**2 + 134.705801750617 * m.b18
    <= 135.705801750617)
m.e80 = Constraint(expr= (1.65791995565741 - m.x52)**2 + (6.17322651944292 -
    m.x55)**2 + (7.01412219987569 - m.x58)**2 + 138.925429422844 * m.b19
    <= 139.925429422844)
m.e81 = Constraint(expr= (2.41953526971379 - m.x52)**2 + (1.09500973629707 -
    m.x55)**2 + (2.60189595048839 - m.x58)**2 + 152.575845479968 * m.b20
    <= 153.575845479968)
m.e82 = Constraint(expr= m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17
    + m.b18 + m.b19 + m.b20 == 1)
m.e83 = Constraint(expr= (3.55441530772447 - m.x60)**2 + (2.6588399811956 -
    m.x62)**2 + (5.16713392802669 - m.x64)**2 + 128.415159268527 * m.b21
    <= 129.415159268527)
m.e84 = Constraint(expr= (8.82094045941646 - m.x60)**2 + (9.51816335093057 -
    m.x62)**2 + (0.894770759747333 - m.x64)**2 + 136.27463320812 * m.b22
    <= 137.27463320812)
m.e85 = Constraint(expr= (6.86229591973038 - m.x60)**2 + (4.74665709736901 -
    m.x62)**2 + (1.14651582775383 - m.x64)**2 + 79.4930138069821 * m.b23
    <= 80.4930138069821)
m.e86 = Constraint(expr= (7.13880287505566 - m.x60)**2 + (0.923639199248324 -
    m.x62)**2 + (5.06906794010293 - m.x64)**2 + 124.602073729487 * m.b24
    <= 125.602073729487)
m.e87 = Constraint(expr= (9.54873475130122 - m.x60)**2 + (9.730708594994 -
    m.x62)**2 + (0.506682101270036 - m.x64)**2 + 152.575845479968 * m.b25
    <= 153.575845479968)
m.e88 = Constraint(expr= (2.60295575976191 - m.x60)**2 + (9.60525309364094 -
    m.x62)**2 + (5.33059723504087 - m.x64)**2 + 115.609943222472 * m.b26
    <= 116.609943222472)
m.e89 = Constraint(expr= (8.7489239697277 - m.x60)**2 + (6.42418905563567 -
    m.x62)**2 + (6.53764526999883 - m.x64)**2 + 102.276439512632 * m.b27
    <= 103.276439512632)
m.e90 = Constraint(expr= (2.98069751112782 - m.x60)**2 + (1.4913715136506 -
    m.x62)**2 + (2.04987567063475 - m.x64)**2 + 134.705801750617 * m.b28
    <= 135.705801750617)
m.e91 = Constraint(expr= (1.65791995565741 - m.x60)**2 + (6.17322651944292 -
    m.x62)**2 + (7.01412219987569 - m.x64)**2 + 138.925429422844 * m.b29
    <= 139.925429422844)
m.e92 = Constraint(expr= (2.41953526971379 - m.x60)**2 + (1.09500973629707 -
    m.x62)**2 + (2.60189595048839 - m.x64)**2 + 152.575845479968 * m.b30
    <= 153.575845479968)
m.e93 = Constraint(expr= m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 + m.b27
    + m.b28 + m.b29 + m.b30 == 1)
m.e94 = Constraint(expr= (3.55441530772447 - m.x66)**2 + (2.6588399811956 -
    m.x68)**2 + (5.16713392802669 - m.x70)**2 + 128.415159268527 * m.b31
    <= 129.415159268527)
m.e95 = Constraint(expr= (8.82094045941646 - m.x66)**2 + (9.51816335093057 -
    m.x68)**2 + (0.894770759747333 - m.x70)**2 + 136.27463320812 * m.b32
    <= 137.27463320812)
m.e96 = Constraint(expr= (6.86229591973038 - m.x66)**2 + (4.74665709736901 -
    m.x68)**2 + (1.14651582775383 - m.x70)**2 + 79.4930138069821 * m.b33
    <= 80.4930138069821)
m.e97 = Constraint(expr= (7.13880287505566 - m.x66)**2 + (0.923639199248324 -
    m.x68)**2 + (5.06906794010293 - m.x70)**2 + 124.602073729487 * m.b34
    <= 125.602073729487)
m.e98 = Constraint(expr= (9.54873475130122 - m.x66)**2 + (9.730708594994 -
    m.x68)**2 + (0.506682101270036 - m.x70)**2 + 152.575845479968 * m.b35
    <= 153.575845479968)
m.e99 = Constraint(expr= (2.60295575976191 - m.x66)**2 + (9.60525309364094 -
    m.x68)**2 + (5.33059723504087 - m.x70)**2 + 115.609943222472 * m.b36
    <= 116.609943222472)
m.e100 = Constraint(expr= (8.7489239697277 - m.x66)**2 + (6.42418905563567 -
    m.x68)**2 + (6.53764526999883 - m.x70)**2 + 102.276439512632 * m.b37
    <= 103.276439512632)
m.e101 = Constraint(expr= (2.98069751112782 - m.x66)**2 + (1.4913715136506 -
    m.x68)**2 + (2.04987567063475 - m.x70)**2 + 134.705801750617 * m.b38
    <= 135.705801750617)
m.e102 = Constraint(expr= (1.65791995565741 - m.x66)**2 + (6.17322651944292 -
    m.x68)**2 + (7.01412219987569 - m.x70)**2 + 138.925429422844 * m.b39
    <= 139.925429422844)
m.e103 = Constraint(expr= (2.41953526971379 - m.x66)**2 + (1.09500973629707 -
    m.x68)**2 + (2.60189595048839 - m.x70)**2 + 152.575845479968 * m.b40
    <= 153.575845479968)
m.e104 = Constraint(expr= m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 + m.b37
    + m.b38 + m.b39 + m.b40 == 1)
m.e105 = Constraint(expr= (3.55441530772447 - m.x72)**2 + (2.6588399811956 -
    m.x74)**2 + (5.16713392802669 - m.x76)**2 + 128.415159268527 * m.b41
    <= 129.415159268527)
m.e106 = Constraint(expr= (8.82094045941646 - m.x72)**2 + (9.51816335093057 -
    m.x74)**2 + (0.894770759747333 - m.x76)**2 + 136.27463320812 * m.b42
    <= 137.27463320812)
m.e107 = Constraint(expr= (6.86229591973038 - m.x72)**2 + (4.74665709736901 -
    m.x74)**2 + (1.14651582775383 - m.x76)**2 + 79.4930138069821 * m.b43
    <= 80.4930138069821)
m.e108 = Constraint(expr= (7.13880287505566 - m.x72)**2 + (0.923639199248324 -
    m.x74)**2 + (5.06906794010293 - m.x76)**2 + 124.602073729487 * m.b44
    <= 125.602073729487)
m.e109 = Constraint(expr= (9.54873475130122 - m.x72)**2 + (9.730708594994 -
    m.x74)**2 + (0.506682101270036 - m.x76)**2 + 152.575845479968 * m.b45
    <= 153.575845479968)
m.e110 = Constraint(expr= (2.60295575976191 - m.x72)**2 + (9.60525309364094 -
    m.x74)**2 + (5.33059723504087 - m.x76)**2 + 115.609943222472 * m.b46
    <= 116.609943222472)
m.e111 = Constraint(expr= (8.7489239697277 - m.x72)**2 + (6.42418905563567 -
    m.x74)**2 + (6.53764526999883 - m.x76)**2 + 102.276439512632 * m.b47
    <= 103.276439512632)
m.e112 = Constraint(expr= (2.98069751112782 - m.x72)**2 + (1.4913715136506 -
    m.x74)**2 + (2.04987567063475 - m.x76)**2 + 134.705801750617 * m.b48
    <= 135.705801750617)
m.e113 = Constraint(expr= (1.65791995565741 - m.x72)**2 + (6.17322651944292 -
    m.x74)**2 + (7.01412219987569 - m.x76)**2 + 138.925429422844 * m.b49
    <= 139.925429422844)
m.e114 = Constraint(expr= (2.41953526971379 - m.x72)**2 + (1.09500973629707 -
    m.x74)**2 + (2.60189595048839 - m.x76)**2 + 152.575845479968 * m.b50
    <= 153.575845479968)
m.e115 = Constraint(expr= m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47
    + m.b48 + m.b49 + m.b50 == 1)
m.e116 = Constraint(expr= m.b1 + m.b11 + m.b21 + m.b31 + m.b41 <= 1)
m.e117 = Constraint(expr= m.b2 + m.b12 + m.b22 + m.b32 + m.b42 <= 1)
m.e118 = Constraint(expr= m.b3 + m.b13 + m.b23 + m.b33 + m.b43 <= 1)
m.e119 = Constraint(expr= m.b4 + m.b14 + m.b24 + m.b34 + m.b44 <= 1)
m.e120 = Constraint(expr= m.b5 + m.b15 + m.b25 + m.b35 + m.b45 <= 1)
m.e121 = Constraint(expr= m.b6 + m.b16 + m.b26 + m.b36 + m.b46 <= 1)
m.e122 = Constraint(expr= m.b7 + m.b17 + m.b27 + m.b37 + m.b47 <= 1)
m.e123 = Constraint(expr= m.b8 + m.b18 + m.b28 + m.b38 + m.b48 <= 1)
m.e124 = Constraint(expr= m.b9 + m.b19 + m.b29 + m.b39 + m.b49 <= 1)
m.e125 = Constraint(expr= m.b10 + m.b20 + m.b30 + m.b40 + m.b50 <= 1)
m.e126 = Constraint(expr= m.x51 - m.x52 <= 0)
m.e127 = Constraint(expr= m.x52 - m.x60 <= 0)
m.e128 = Constraint(expr= m.x60 - m.x66 <= 0)
m.e129 = Constraint(expr= m.x66 - m.x72 <= 0)
