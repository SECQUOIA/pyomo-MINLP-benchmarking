# MINLP written by GAMS Convert at 05/07/21 17:13:01
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       234       42       24      168        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       164      132       32        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       640      544       96
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.x1 = Var(within=Reals, bounds=(11.5,57.5), initialize=11.5)
m.x2 = Var(within=Reals, bounds=(12.5,56.5), initialize=12.5)
m.x3 = Var(within=Reals, bounds=(10.5,58.5), initialize=10.5)
m.x4 = Var(within=Reals, bounds=(10,59), initialize=10)
m.x5 = Var(within=Reals, bounds=(7,87), initialize=7)
m.x6 = Var(within=Reals, bounds=(6.5,87.5), initialize=6.5)
m.x7 = Var(within=Reals, bounds=(5.5,88.5), initialize=5.5)
m.x8 = Var(within=Reals, bounds=(5.5,88.5), initialize=5.5)
m.x9 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x10 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x11 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x12 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x13 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x14 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x15 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x16 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x17 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x18 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x19 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x20 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x21 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x22 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x23 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x24 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x25 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x26 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x27 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x28 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x29 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x30 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x31 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x32 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x33 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x34 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x35 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x36 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x37 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x38 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x39 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x40 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x41 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x42 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x43 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x44 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x45 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x46 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x47 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x48 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x49 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x50 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x51 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x52 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x53 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x54 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x55 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x56 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x57 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x58 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x59 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x60 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x61 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x62 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x63 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x64 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x65 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x66 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x67 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x68 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x69 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x70 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x71 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x72 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x73 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x74 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x75 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x76 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x77 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x78 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x79 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x80 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x81 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x82 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x83 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x84 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x85 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x86 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x87 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x88 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x89 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x90 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x91 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x92 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x93 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x94 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x95 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x96 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x97 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x98 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x99 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x100 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x101 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x102 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x103 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x104 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x105 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x106 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x107 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x108 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x109 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x110 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x111 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x112 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x113 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x114 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x115 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x116 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x117 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x118 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x119 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x120 = Var(within=Reals, bounds=(0,None), initialize=0)
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
m.x153 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x154 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x155 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x156 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x157 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x158 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x159 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x160 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x161 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x162 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x163 = Var(within=Reals, bounds=(0,None), initialize=0)
m.x164 = Var(within=Reals, bounds=(0,None), initialize=0)

m.obj = Objective(sense=minimize, expr= 300 * m.x153 + 240 * m.x154 + 210 *
    m.x155 + 100 * m.x156 + 150 * m.x157 + 120 * m.x158 + 300 * m.x159 + 240 *
    m.x160 + 210 * m.x161 + 100 * m.x162 + 150 * m.x163 + 120 * m.x164)

m.e1 = Constraint(expr= -m.x1 + m.x2 + m.x153 >= 0)
m.e2 = Constraint(expr= -m.x1 + m.x3 + m.x154 >= 0)
m.e3 = Constraint(expr= -m.x1 + m.x4 + m.x155 >= 0)
m.e4 = Constraint(expr= -m.x2 + m.x3 + m.x156 >= 0)
m.e5 = Constraint(expr= -m.x2 + m.x4 + m.x157 >= 0)
m.e6 = Constraint(expr= -m.x3 + m.x4 + m.x158 >= 0)
m.e7 = Constraint(expr= m.x1 - m.x2 + m.x153 >= 0)
m.e8 = Constraint(expr= m.x1 - m.x3 + m.x154 >= 0)
m.e9 = Constraint(expr= m.x1 - m.x4 + m.x155 >= 0)
m.e10 = Constraint(expr= m.x2 - m.x3 + m.x156 >= 0)
m.e11 = Constraint(expr= m.x2 - m.x4 + m.x157 >= 0)
m.e12 = Constraint(expr= m.x3 - m.x4 + m.x158 >= 0)
m.e13 = Constraint(expr= -m.x5 + m.x6 + m.x159 >= 0)
m.e14 = Constraint(expr= -m.x5 + m.x7 + m.x160 >= 0)
m.e15 = Constraint(expr= -m.x5 + m.x8 + m.x161 >= 0)
m.e16 = Constraint(expr= -m.x6 + m.x7 + m.x162 >= 0)
m.e17 = Constraint(expr= -m.x6 + m.x8 + m.x163 >= 0)
m.e18 = Constraint(expr= -m.x7 + m.x8 + m.x164 >= 0)
m.e19 = Constraint(expr= m.x5 - m.x6 + m.x159 >= 0)
m.e20 = Constraint(expr= m.x5 - m.x7 + m.x160 >= 0)
m.e21 = Constraint(expr= m.x5 - m.x8 + m.x161 >= 0)
m.e22 = Constraint(expr= m.x6 - m.x7 + m.x162 >= 0)
m.e23 = Constraint(expr= m.x6 - m.x8 + m.x163 >= 0)
m.e24 = Constraint(expr= m.x7 - m.x8 + m.x164 >= 0)
m.e25 = Constraint(expr= m.x1 - m.x9 - m.x12 - m.x15 - m.x18 == 0)
m.e26 = Constraint(expr= m.x1 - m.x10 - m.x13 - m.x16 - m.x19 == 0)
m.e27 = Constraint(expr= m.x1 - m.x11 - m.x14 - m.x17 - m.x20 == 0)
m.e28 = Constraint(expr= m.x2 - m.x21 - m.x24 - m.x27 - m.x30 == 0)
m.e29 = Constraint(expr= m.x2 - m.x22 - m.x25 - m.x28 - m.x31 == 0)
m.e30 = Constraint(expr= m.x2 - m.x23 - m.x26 - m.x29 - m.x32 == 0)
m.e31 = Constraint(expr= m.x3 - m.x33 - m.x36 - m.x39 - m.x42 == 0)
m.e32 = Constraint(expr= m.x3 - m.x34 - m.x37 - m.x40 - m.x43 == 0)
m.e33 = Constraint(expr= m.x3 - m.x35 - m.x38 - m.x41 - m.x44 == 0)
m.e34 = Constraint(expr= m.x4 - m.x45 - m.x48 - m.x51 - m.x54 == 0)
m.e35 = Constraint(expr= m.x4 - m.x46 - m.x49 - m.x52 - m.x55 == 0)
m.e36 = Constraint(expr= m.x4 - m.x47 - m.x50 - m.x53 - m.x56 == 0)
m.e37 = Constraint(expr= m.x5 - m.x57 - m.x60 - m.x63 - m.x66 == 0)
m.e38 = Constraint(expr= m.x5 - m.x58 - m.x61 - m.x64 - m.x67 == 0)
m.e39 = Constraint(expr= m.x5 - m.x59 - m.x62 - m.x65 - m.x68 == 0)
m.e40 = Constraint(expr= m.x6 - m.x69 - m.x72 - m.x75 - m.x78 == 0)
m.e41 = Constraint(expr= m.x6 - m.x70 - m.x73 - m.x76 - m.x79 == 0)
m.e42 = Constraint(expr= m.x6 - m.x71 - m.x74 - m.x77 - m.x80 == 0)
m.e43 = Constraint(expr= m.x7 - m.x81 - m.x84 - m.x87 - m.x90 == 0)
m.e44 = Constraint(expr= m.x7 - m.x82 - m.x85 - m.x88 - m.x91 == 0)
m.e45 = Constraint(expr= m.x7 - m.x83 - m.x86 - m.x89 - m.x92 == 0)
m.e46 = Constraint(expr= m.x8 - m.x93 - m.x96 - m.x99 - m.x102 == 0)
m.e47 = Constraint(expr= m.x8 - m.x94 - m.x97 - m.x100 - m.x103 == 0)
m.e48 = Constraint(expr= m.x8 - m.x95 - m.x98 - m.x101 - m.x104 == 0)
m.e49 = Constraint(expr= m.x9 - 57.5 * m.b121 <= 0)
m.e50 = Constraint(expr= m.x10 - 57.5 * m.b122 <= 0)
m.e51 = Constraint(expr= m.x11 - 57.5 * m.b123 <= 0)
m.e52 = Constraint(expr= m.x12 - 57.5 * m.b127 <= 0)
m.e53 = Constraint(expr= m.x13 - 57.5 * m.b128 <= 0)
m.e54 = Constraint(expr= m.x14 - 57.5 * m.b129 <= 0)
m.e55 = Constraint(expr= m.x15 - 57.5 * m.b133 <= 0)
m.e56 = Constraint(expr= m.x16 - 57.5 * m.b134 <= 0)
m.e57 = Constraint(expr= m.x17 - 57.5 * m.b135 <= 0)
m.e58 = Constraint(expr= m.x18 - 57.5 * m.b139 <= 0)
m.e59 = Constraint(expr= m.x19 - 57.5 * m.b140 <= 0)
m.e60 = Constraint(expr= m.x20 - 57.5 * m.b141 <= 0)
m.e61 = Constraint(expr= m.x21 - 57.5 * m.b121 <= 0)
m.e62 = Constraint(expr= m.x22 - 56.5 * m.b124 <= 0)
m.e63 = Constraint(expr= m.x23 - 56.5 * m.b125 <= 0)
m.e64 = Constraint(expr= m.x24 - 57.5 * m.b127 <= 0)
m.e65 = Constraint(expr= m.x25 - 56.5 * m.b130 <= 0)
m.e66 = Constraint(expr= m.x26 - 56.5 * m.b131 <= 0)
m.e67 = Constraint(expr= m.x27 - 57.5 * m.b133 <= 0)
m.e68 = Constraint(expr= m.x28 - 56.5 * m.b136 <= 0)
m.e69 = Constraint(expr= m.x29 - 56.5 * m.b137 <= 0)
m.e70 = Constraint(expr= m.x30 - 57.5 * m.b139 <= 0)
m.e71 = Constraint(expr= m.x31 - 56.5 * m.b142 <= 0)
m.e72 = Constraint(expr= m.x32 - 56.5 * m.b143 <= 0)
m.e73 = Constraint(expr= m.x33 - 57.5 * m.b122 <= 0)
m.e74 = Constraint(expr= m.x34 - 56.5 * m.b124 <= 0)
m.e75 = Constraint(expr= m.x35 - 58.5 * m.b126 <= 0)
m.e76 = Constraint(expr= m.x36 - 57.5 * m.b128 <= 0)
m.e77 = Constraint(expr= m.x37 - 56.5 * m.b130 <= 0)
m.e78 = Constraint(expr= m.x38 - 58.5 * m.b132 <= 0)
m.e79 = Constraint(expr= m.x39 - 57.5 * m.b134 <= 0)
m.e80 = Constraint(expr= m.x40 - 56.5 * m.b136 <= 0)
m.e81 = Constraint(expr= m.x41 - 58.5 * m.b138 <= 0)
m.e82 = Constraint(expr= m.x42 - 57.5 * m.b140 <= 0)
m.e83 = Constraint(expr= m.x43 - 56.5 * m.b142 <= 0)
m.e84 = Constraint(expr= m.x44 - 58.5 * m.b144 <= 0)
m.e85 = Constraint(expr= m.x45 - 57.5 * m.b123 <= 0)
m.e86 = Constraint(expr= m.x46 - 56.5 * m.b125 <= 0)
m.e87 = Constraint(expr= m.x47 - 58.5 * m.b126 <= 0)
m.e88 = Constraint(expr= m.x48 - 57.5 * m.b129 <= 0)
m.e89 = Constraint(expr= m.x49 - 56.5 * m.b131 <= 0)
m.e90 = Constraint(expr= m.x50 - 58.5 * m.b132 <= 0)
m.e91 = Constraint(expr= m.x51 - 57.5 * m.b135 <= 0)
m.e92 = Constraint(expr= m.x52 - 56.5 * m.b137 <= 0)
m.e93 = Constraint(expr= m.x53 - 58.5 * m.b138 <= 0)
m.e94 = Constraint(expr= m.x54 - 57.5 * m.b141 <= 0)
m.e95 = Constraint(expr= m.x55 - 56.5 * m.b143 <= 0)
m.e96 = Constraint(expr= m.x56 - 58.5 * m.b144 <= 0)
m.e97 = Constraint(expr= m.x57 - 87 * m.b121 <= 0)
m.e98 = Constraint(expr= m.x58 - 87 * m.b122 <= 0)
m.e99 = Constraint(expr= m.x59 - 87 * m.b123 <= 0)
m.e100 = Constraint(expr= m.x60 - 87 * m.b127 <= 0)
m.e101 = Constraint(expr= m.x61 - 87 * m.b128 <= 0)
m.e102 = Constraint(expr= m.x62 - 87 * m.b129 <= 0)
m.e103 = Constraint(expr= m.x63 - 87 * m.b133 <= 0)
m.e104 = Constraint(expr= m.x64 - 87 * m.b134 <= 0)
m.e105 = Constraint(expr= m.x65 - 87 * m.b135 <= 0)
m.e106 = Constraint(expr= m.x66 - 87 * m.b139 <= 0)
m.e107 = Constraint(expr= m.x67 - 87 * m.b140 <= 0)
m.e108 = Constraint(expr= m.x68 - 87 * m.b141 <= 0)
m.e109 = Constraint(expr= m.x69 - 87 * m.b121 <= 0)
m.e110 = Constraint(expr= m.x70 - 87.5 * m.b124 <= 0)
m.e111 = Constraint(expr= m.x71 - 87.5 * m.b125 <= 0)
m.e112 = Constraint(expr= m.x72 - 87 * m.b127 <= 0)
m.e113 = Constraint(expr= m.x73 - 87.5 * m.b130 <= 0)
m.e114 = Constraint(expr= m.x74 - 87.5 * m.b131 <= 0)
m.e115 = Constraint(expr= m.x75 - 87 * m.b133 <= 0)
m.e116 = Constraint(expr= m.x76 - 87.5 * m.b136 <= 0)
m.e117 = Constraint(expr= m.x77 - 87.5 * m.b137 <= 0)
m.e118 = Constraint(expr= m.x78 - 87 * m.b139 <= 0)
m.e119 = Constraint(expr= m.x79 - 87.5 * m.b142 <= 0)
m.e120 = Constraint(expr= m.x80 - 87.5 * m.b143 <= 0)
m.e121 = Constraint(expr= m.x81 - 87 * m.b122 <= 0)
m.e122 = Constraint(expr= m.x82 - 87.5 * m.b124 <= 0)
m.e123 = Constraint(expr= m.x83 - 88.5 * m.b126 <= 0)
m.e124 = Constraint(expr= m.x84 - 87 * m.b128 <= 0)
m.e125 = Constraint(expr= m.x85 - 87.5 * m.b130 <= 0)
m.e126 = Constraint(expr= m.x86 - 88.5 * m.b132 <= 0)
m.e127 = Constraint(expr= m.x87 - 87 * m.b134 <= 0)
m.e128 = Constraint(expr= m.x88 - 87.5 * m.b136 <= 0)
m.e129 = Constraint(expr= m.x89 - 88.5 * m.b138 <= 0)
m.e130 = Constraint(expr= m.x90 - 87 * m.b140 <= 0)
m.e131 = Constraint(expr= m.x91 - 87.5 * m.b142 <= 0)
m.e132 = Constraint(expr= m.x92 - 88.5 * m.b144 <= 0)
m.e133 = Constraint(expr= m.x93 - 87 * m.b123 <= 0)
m.e134 = Constraint(expr= m.x94 - 87.5 * m.b125 <= 0)
m.e135 = Constraint(expr= m.x95 - 88.5 * m.b126 <= 0)
m.e136 = Constraint(expr= m.x96 - 87 * m.b129 <= 0)
m.e137 = Constraint(expr= m.x97 - 87.5 * m.b131 <= 0)
m.e138 = Constraint(expr= m.x98 - 88.5 * m.b132 <= 0)
m.e139 = Constraint(expr= m.x99 - 87 * m.b135 <= 0)
m.e140 = Constraint(expr= m.x100 - 87.5 * m.b137 <= 0)
m.e141 = Constraint(expr= m.x101 - 88.5 * m.b138 <= 0)
m.e142 = Constraint(expr= m.x102 - 87 * m.b141 <= 0)
m.e143 = Constraint(expr= m.x103 - 87.5 * m.b143 <= 0)
m.e144 = Constraint(expr= m.x104 - 88.5 * m.b144 <= 0)
m.e145 = Constraint(expr= m.x9 - m.x21 + 6 * m.b121 <= 0)
m.e146 = Constraint(expr= m.x10 - m.x33 + 4 * m.b122 <= 0)
m.e147 = Constraint(expr= m.x11 - m.x45 + 3.5 * m.b123 <= 0)
m.e148 = Constraint(expr= m.x22 - m.x34 + 5 * m.b124 <= 0)
m.e149 = Constraint(expr= m.x23 - m.x46 + 4.5 * m.b125 <= 0)
m.e150 = Constraint(expr= m.x35 - m.x47 + 2.5 * m.b126 <= 0)
m.e151 = Constraint(expr= -m.x12 + m.x24 + 6 * m.b127 <= 0)
m.e152 = Constraint(expr= -m.x13 + m.x36 + 4 * m.b128 <= 0)
m.e153 = Constraint(expr= -m.x14 + m.x48 + 3.5 * m.b129 <= 0)
m.e154 = Constraint(expr= -m.x25 + m.x37 + 5 * m.b130 <= 0)
m.e155 = Constraint(expr= -m.x26 + m.x49 + 4.5 * m.b131 <= 0)
m.e156 = Constraint(expr= -m.x38 + m.x50 + 2.5 * m.b132 <= 0)
m.e157 = Constraint(expr= m.x63 - m.x75 + 5.5 * m.b133 <= 0)
m.e158 = Constraint(expr= m.x64 - m.x87 + 4.5 * m.b134 <= 0)
m.e159 = Constraint(expr= m.x65 - m.x99 + 4.5 * m.b135 <= 0)
m.e160 = Constraint(expr= m.x76 - m.x88 + 4 * m.b136 <= 0)
m.e161 = Constraint(expr= m.x77 - m.x100 + 4 * m.b137 <= 0)
m.e162 = Constraint(expr= m.x89 - m.x101 + 3 * m.b138 <= 0)
m.e163 = Constraint(expr= -m.x66 + m.x78 + 5.5 * m.b139 <= 0)
m.e164 = Constraint(expr= -m.x67 + m.x90 + 4.5 * m.b140 <= 0)
m.e165 = Constraint(expr= -m.x68 + m.x102 + 4.5 * m.b141 <= 0)
m.e166 = Constraint(expr= -m.x79 + m.x91 + 4 * m.b142 <= 0)
m.e167 = Constraint(expr= -m.x80 + m.x103 + 4 * m.b143 <= 0)
m.e168 = Constraint(expr= -m.x92 + m.x104 + 3 * m.b144 <= 0)
m.e169 = Constraint(expr= m.b121 + m.b127 + m.b133 + m.b139 == 1)
m.e170 = Constraint(expr= m.b122 + m.b128 + m.b134 + m.b140 == 1)
m.e171 = Constraint(expr= m.b123 + m.b129 + m.b135 + m.b141 == 1)
m.e172 = Constraint(expr= m.b124 + m.b130 + m.b136 + m.b142 == 1)
m.e173 = Constraint(expr= m.b125 + m.b131 + m.b137 + m.b143 == 1)
m.e174 = Constraint(expr= m.b126 + m.b132 + m.b138 + m.b144 == 1)
m.e175 = Constraint(expr= m.x1 - m.x105 - m.x109 == 0)
m.e176 = Constraint(expr= m.x2 - m.x106 - m.x110 == 0)
m.e177 = Constraint(expr= m.x3 - m.x107 - m.x111 == 0)
m.e178 = Constraint(expr= m.x4 - m.x108 - m.x112 == 0)
m.e179 = Constraint(expr= m.x5 - m.x113 - m.x117 == 0)
m.e180 = Constraint(expr= m.x6 - m.x114 - m.x118 == 0)
m.e181 = Constraint(expr= m.x7 - m.x115 - m.x119 == 0)
m.e182 = Constraint(expr= m.x8 - m.x116 - m.x120 == 0)
m.e183 = Constraint(expr= m.x105 - 18.5 * m.b145 <= 0)
m.e184 = Constraint(expr= m.x106 - 17.5 * m.b146 <= 0)
m.e185 = Constraint(expr= m.x107 - 19.5 * m.b147 <= 0)
m.e186 = Constraint(expr= m.x108 - 20 * m.b148 <= 0)
m.e187 = Constraint(expr= m.x109 - 57.5 * m.b149 <= 0)
m.e188 = Constraint(expr= m.x110 - 56.5 * m.b150 <= 0)
m.e189 = Constraint(expr= m.x111 - 58.5 * m.b151 <= 0)
m.e190 = Constraint(expr= m.x112 - 59 * m.b152 <= 0)
m.e191 = Constraint(expr= m.x113 - 13 * m.b145 <= 0)
m.e192 = Constraint(expr= m.x114 - 13.5 * m.b146 <= 0)
m.e193 = Constraint(expr= m.x115 - 14.5 * m.b147 <= 0)
m.e194 = Constraint(expr= m.x116 - 14.5 * m.b148 <= 0)
m.e195 = Constraint(expr= m.x117 - 87 * m.b149 <= 0)
m.e196 = Constraint(expr= m.x118 - 87.5 * m.b150 <= 0)
m.e197 = Constraint(expr= m.x119 - 88.5 * m.b151 <= 0)
m.e198 = Constraint(expr= m.x120 - 88.5 * m.b152 <= 0)
m.e199 = Constraint(expr= ((m.x105 / (0.001 + 0.999 * m.b145))**2 - (35 *
    m.x105) / (0.001 + 0.999 * m.b145) + (m.x113 / (0.001 + 0.999 * m.b145))**2
    - (14 * m.x113) / (0.001 + 0.999 * m.b145)) * (0.001 + 0.999 * m.b145) +
    306.25 * m.b145 + 49 * m.b145 - 36 * m.b145 <= 0)
m.e200 = Constraint(expr= ((m.x106 / (0.001 + 0.999 * m.b146))**2 - (37 *
    m.x106) / (0.001 + 0.999 * m.b146) + (m.x114 / (0.001 + 0.999 * m.b146))**2
    - (15 * m.x114) / (0.001 + 0.999 * m.b146)) * (0.001 + 0.999 * m.b146) +
    342.25 * m.b146 + 56.25 * m.b146 - 36 * m.b146 <= 0)
m.e201 = Constraint(expr= ((m.x107 / (0.001 + 0.999 * m.b147))**2 - (33 *
    m.x107) / (0.001 + 0.999 * m.b147) + (m.x115 / (0.001 + 0.999 * m.b147))**2
    - (17 * m.x115) / (0.001 + 0.999 * m.b147)) * (0.001 + 0.999 * m.b147) +
    272.25 * m.b147 + 72.25 * m.b147 - 36 * m.b147 <= 0)
m.e202 = Constraint(expr= ((m.x108 / (0.001 + 0.999 * m.b148))**2 - (32 *
    m.x108) / (0.001 + 0.999 * m.b148) + (m.x116 / (0.001 + 0.999 * m.b148))**2
    - (17 * m.x116) / (0.001 + 0.999 * m.b148)) * (0.001 + 0.999 * m.b148) +
    256 * m.b148 + 72.25 * m.b148 - 36 * m.b148 <= 0)
m.e203 = Constraint(expr= ((m.x109 / (0.001 + 0.999 * m.b149))**2 - (105 *
    m.x109) / (0.001 + 0.999 * m.b149) + (m.x117 / (0.001 + 0.999 * m.b149))**2
    - (154 * m.x117) / (0.001 + 0.999 * m.b149)) * (0.001 + 0.999 * m.b149) +
    2756.25 * m.b149 + 5929 * m.b149 - 100 * m.b149 <= 0)
m.e204 = Constraint(expr= ((m.x110 / (0.001 + 0.999 * m.b150))**2 - (107 *
    m.x110) / (0.001 + 0.999 * m.b150) + (m.x118 / (0.001 + 0.999 * m.b150))**2
    - (155 * m.x118) / (0.001 + 0.999 * m.b150)) * (0.001 + 0.999 * m.b150) +
    2862.25 * m.b150 + 6006.25 * m.b150 - 100 * m.b150 <= 0)
m.e205 = Constraint(expr= ((m.x111 / (0.001 + 0.999 * m.b151))**2 - (103 *
    m.x111) / (0.001 + 0.999 * m.b151) + (m.x119 / (0.001 + 0.999 * m.b151))**2
    - (157 * m.x119) / (0.001 + 0.999 * m.b151)) * (0.001 + 0.999 * m.b151) +
    2652.25 * m.b151 + 6162.25 * m.b151 - 100 * m.b151 <= 0)
m.e206 = Constraint(expr= ((m.x112 / (0.001 + 0.999 * m.b152))**2 - (102 *
    m.x112) / (0.001 + 0.999 * m.b152) + (m.x120 / (0.001 + 0.999 * m.b152))**2
    - (157 * m.x120) / (0.001 + 0.999 * m.b152)) * (0.001 + 0.999 * m.b152) +
    2601 * m.b152 + 6162.25 * m.b152 - 100 * m.b152 <= 0)
m.e207 = Constraint(expr= ((m.x105 / (0.001 + 0.999 * m.b145))**2 - (35 *
    m.x105) / (0.001 + 0.999 * m.b145) + (m.x113 / (0.001 + 0.999 * m.b145))**2
    - (26 * m.x113) / (0.001 + 0.999 * m.b145)) * (0.001 + 0.999 * m.b145) +
    306.25 * m.b145 + 169 * m.b145 - 36 * m.b145 <= 0)
m.e208 = Constraint(expr= ((m.x106 / (0.001 + 0.999 * m.b146))**2 - (37 *
    m.x106) / (0.001 + 0.999 * m.b146) + (m.x114 / (0.001 + 0.999 * m.b146))**2
    - (25 * m.x114) / (0.001 + 0.999 * m.b146)) * (0.001 + 0.999 * m.b146) +
    342.25 * m.b146 + 156.25 * m.b146 - 36 * m.b146 <= 0)
m.e209 = Constraint(expr= ((m.x107 / (0.001 + 0.999 * m.b147))**2 - (33 *
    m.x107) / (0.001 + 0.999 * m.b147) + (m.x115 / (0.001 + 0.999 * m.b147))**2
    - (23 * m.x115) / (0.001 + 0.999 * m.b147)) * (0.001 + 0.999 * m.b147) +
    272.25 * m.b147 + 132.25 * m.b147 - 36 * m.b147 <= 0)
m.e210 = Constraint(expr= ((m.x108 / (0.001 + 0.999 * m.b148))**2 - (32 *
    m.x108) / (0.001 + 0.999 * m.b148) + (m.x116 / (0.001 + 0.999 * m.b148))**2
    - (23 * m.x116) / (0.001 + 0.999 * m.b148)) * (0.001 + 0.999 * m.b148) +
    256 * m.b148 + 132.25 * m.b148 - 36 * m.b148 <= 0)
m.e211 = Constraint(expr= ((m.x109 / (0.001 + 0.999 * m.b149))**2 - (105 *
    m.x109) / (0.001 + 0.999 * m.b149) + (m.x117 / (0.001 + 0.999 * m.b149))**2
    - (166 * m.x117) / (0.001 + 0.999 * m.b149)) * (0.001 + 0.999 * m.b149) +
    2756.25 * m.b149 + 6889 * m.b149 - 100 * m.b149 <= 0)
m.e212 = Constraint(expr= ((m.x110 / (0.001 + 0.999 * m.b150))**2 - (107 *
    m.x110) / (0.001 + 0.999 * m.b150) + (m.x118 / (0.001 + 0.999 * m.b150))**2
    - (165 * m.x118) / (0.001 + 0.999 * m.b150)) * (0.001 + 0.999 * m.b150) +
    2862.25 * m.b150 + 6806.25 * m.b150 - 100 * m.b150 <= 0)
m.e213 = Constraint(expr= ((m.x111 / (0.001 + 0.999 * m.b151))**2 - (103 *
    m.x111) / (0.001 + 0.999 * m.b151) + (m.x119 / (0.001 + 0.999 * m.b151))**2
    - (163 * m.x119) / (0.001 + 0.999 * m.b151)) * (0.001 + 0.999 * m.b151) +
    2652.25 * m.b151 + 6642.25 * m.b151 - 100 * m.b151 <= 0)
m.e214 = Constraint(expr= ((m.x112 / (0.001 + 0.999 * m.b152))**2 - (102 *
    m.x112) / (0.001 + 0.999 * m.b152) + (m.x120 / (0.001 + 0.999 * m.b152))**2
    - (163 * m.x120) / (0.001 + 0.999 * m.b152)) * (0.001 + 0.999 * m.b152) +
    2601 * m.b152 + 6642.25 * m.b152 - 100 * m.b152 <= 0)
m.e215 = Constraint(expr= ((m.x105 / (0.001 + 0.999 * m.b145))**2 - (25 *
    m.x105) / (0.001 + 0.999 * m.b145) + (m.x113 / (0.001 + 0.999 * m.b145))**2
    - (14 * m.x113) / (0.001 + 0.999 * m.b145)) * (0.001 + 0.999 * m.b145) +
    156.25 * m.b145 + 49 * m.b145 - 36 * m.b145 <= 0)
m.e216 = Constraint(expr= ((m.x106 / (0.001 + 0.999 * m.b146))**2 - (23 *
    m.x106) / (0.001 + 0.999 * m.b146) + (m.x114 / (0.001 + 0.999 * m.b146))**2
    - (15 * m.x114) / (0.001 + 0.999 * m.b146)) * (0.001 + 0.999 * m.b146) +
    132.25 * m.b146 + 56.25 * m.b146 - 36 * m.b146 <= 0)
m.e217 = Constraint(expr= ((m.x107 / (0.001 + 0.999 * m.b147))**2 - (27 *
    m.x107) / (0.001 + 0.999 * m.b147) + (m.x115 / (0.001 + 0.999 * m.b147))**2
    - (17 * m.x115) / (0.001 + 0.999 * m.b147)) * (0.001 + 0.999 * m.b147) +
    182.25 * m.b147 + 72.25 * m.b147 - 36 * m.b147 <= 0)
m.e218 = Constraint(expr= ((m.x108 / (0.001 + 0.999 * m.b148))**2 - (28 *
    m.x108) / (0.001 + 0.999 * m.b148) + (m.x116 / (0.001 + 0.999 * m.b148))**2
    - (17 * m.x116) / (0.001 + 0.999 * m.b148)) * (0.001 + 0.999 * m.b148) +
    196 * m.b148 + 72.25 * m.b148 - 36 * m.b148 <= 0)
m.e219 = Constraint(expr= ((m.x109 / (0.001 + 0.999 * m.b149))**2 - (95 *
    m.x109) / (0.001 + 0.999 * m.b149) + (m.x117 / (0.001 + 0.999 * m.b149))**2
    - (154 * m.x117) / (0.001 + 0.999 * m.b149)) * (0.001 + 0.999 * m.b149) +
    2256.25 * m.b149 + 5929 * m.b149 - 100 * m.b149 <= 0)
m.e220 = Constraint(expr= ((m.x110 / (0.001 + 0.999 * m.b150))**2 - (93 *
    m.x110) / (0.001 + 0.999 * m.b150) + (m.x118 / (0.001 + 0.999 * m.b150))**2
    - (155 * m.x118) / (0.001 + 0.999 * m.b150)) * (0.001 + 0.999 * m.b150) +
    2162.25 * m.b150 + 6006.25 * m.b150 - 100 * m.b150 <= 0)
m.e221 = Constraint(expr= ((m.x111 / (0.001 + 0.999 * m.b151))**2 - (97 *
    m.x111) / (0.001 + 0.999 * m.b151) + (m.x119 / (0.001 + 0.999 * m.b151))**2
    - (157 * m.x119) / (0.001 + 0.999 * m.b151)) * (0.001 + 0.999 * m.b151) +
    2352.25 * m.b151 + 6162.25 * m.b151 - 100 * m.b151 <= 0)
m.e222 = Constraint(expr= ((m.x112 / (0.001 + 0.999 * m.b152))**2 - (98 *
    m.x112) / (0.001 + 0.999 * m.b152) + (m.x120 / (0.001 + 0.999 * m.b152))**2
    - (157 * m.x120) / (0.001 + 0.999 * m.b152)) * (0.001 + 0.999 * m.b152) +
    2401 * m.b152 + 6162.25 * m.b152 - 100 * m.b152 <= 0)
m.e223 = Constraint(expr= ((m.x105 / (0.001 + 0.999 * m.b145))**2 - (25 *
    m.x105) / (0.001 + 0.999 * m.b145) + (m.x113 / (0.001 + 0.999 * m.b145))**2
    - (26 * m.x113) / (0.001 + 0.999 * m.b145)) * (0.001 + 0.999 * m.b145) +
    156.25 * m.b145 + 169 * m.b145 - 36 * m.b145 <= 0)
m.e224 = Constraint(expr= ((m.x106 / (0.001 + 0.999 * m.b146))**2 - (23 *
    m.x106) / (0.001 + 0.999 * m.b146) + (m.x114 / (0.001 + 0.999 * m.b146))**2
    - (25 * m.x114) / (0.001 + 0.999 * m.b146)) * (0.001 + 0.999 * m.b146) +
    132.25 * m.b146 + 156.25 * m.b146 - 36 * m.b146 <= 0)
m.e225 = Constraint(expr= ((m.x107 / (0.001 + 0.999 * m.b147))**2 - (27 *
    m.x107) / (0.001 + 0.999 * m.b147) + (m.x115 / (0.001 + 0.999 * m.b147))**2
    - (23 * m.x115) / (0.001 + 0.999 * m.b147)) * (0.001 + 0.999 * m.b147) +
    182.25 * m.b147 + 132.25 * m.b147 - 36 * m.b147 <= 0)
m.e226 = Constraint(expr= ((m.x108 / (0.001 + 0.999 * m.b148))**2 - (28 *
    m.x108) / (0.001 + 0.999 * m.b148) + (m.x116 / (0.001 + 0.999 * m.b148))**2
    - (23 * m.x116) / (0.001 + 0.999 * m.b148)) * (0.001 + 0.999 * m.b148) +
    196 * m.b148 + 132.25 * m.b148 - 36 * m.b148 <= 0)
m.e227 = Constraint(expr= ((m.x109 / (0.001 + 0.999 * m.b149))**2 - (95 *
    m.x109) / (0.001 + 0.999 * m.b149) + (m.x117 / (0.001 + 0.999 * m.b149))**2
    - (166 * m.x117) / (0.001 + 0.999 * m.b149)) * (0.001 + 0.999 * m.b149) +
    2256.25 * m.b149 + 6889 * m.b149 - 100 * m.b149 <= 0)
m.e228 = Constraint(expr= ((m.x110 / (0.001 + 0.999 * m.b150))**2 - (93 *
    m.x110) / (0.001 + 0.999 * m.b150) + (m.x118 / (0.001 + 0.999 * m.b150))**2
    - (165 * m.x118) / (0.001 + 0.999 * m.b150)) * (0.001 + 0.999 * m.b150) +
    2162.25 * m.b150 + 6806.25 * m.b150 - 100 * m.b150 <= 0)
m.e229 = Constraint(expr= ((m.x111 / (0.001 + 0.999 * m.b151))**2 - (97 *
    m.x111) / (0.001 + 0.999 * m.b151) + (m.x119 / (0.001 + 0.999 * m.b151))**2
    - (163 * m.x119) / (0.001 + 0.999 * m.b151)) * (0.001 + 0.999 * m.b151) +
    2352.25 * m.b151 + 6642.25 * m.b151 - 100 * m.b151 <= 0)
m.e230 = Constraint(expr= ((m.x112 / (0.001 + 0.999 * m.b152))**2 - (98 *
    m.x112) / (0.001 + 0.999 * m.b152) + (m.x120 / (0.001 + 0.999 * m.b152))**2
    - (163 * m.x120) / (0.001 + 0.999 * m.b152)) * (0.001 + 0.999 * m.b152) +
    2401 * m.b152 + 6642.25 * m.b152 - 100 * m.b152 <= 0)
m.e231 = Constraint(expr= m.b145 + m.b149 == 1)
m.e232 = Constraint(expr= m.b146 + m.b150 == 1)
m.e233 = Constraint(expr= m.b147 + m.b151 == 1)
m.e234 = Constraint(expr= m.b148 + m.b152 == 1)
