# MINLP written by GAMS Convert at 05/07/21 17:13:01
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       249        5        0      244        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       195       45      150        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#      1088      638      450
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

m.obj = Objective(sense=minimize, expr= m.x153 + m.x156 + m.x159 + m.x161 +
    m.x163 + m.x165 + m.x167 + m.x169 + m.x171 + m.x173 + m.x175 + m.x177 +
    m.x178 + m.x179 + m.x180 + m.x181 + m.x182 + m.x183 + m.x184 + m.x185 +
    m.x186 + m.x187 + m.x188 + m.x189 + m.x190 + m.x191 + m.x192 + m.x193 +
    m.x194 + m.x195)

m.e1 = Constraint(expr= m.x151 - m.x152 - m.x153 <= 0)
m.e2 = Constraint(expr= -m.x151 + m.x152 - m.x153 <= 0)
m.e3 = Constraint(expr= m.x154 - m.x155 - m.x156 <= 0)
m.e4 = Constraint(expr= -m.x154 + m.x155 - m.x156 <= 0)
m.e5 = Constraint(expr= m.x157 - m.x158 - m.x159 <= 0)
m.e6 = Constraint(expr= -m.x157 + m.x158 - m.x159 <= 0)
m.e7 = Constraint(expr= m.x151 - m.x160 - m.x161 <= 0)
m.e8 = Constraint(expr= -m.x151 + m.x160 - m.x161 <= 0)
m.e9 = Constraint(expr= m.x154 - m.x162 - m.x163 <= 0)
m.e10 = Constraint(expr= -m.x154 + m.x162 - m.x163 <= 0)
m.e11 = Constraint(expr= m.x157 - m.x164 - m.x165 <= 0)
m.e12 = Constraint(expr= -m.x157 + m.x164 - m.x165 <= 0)
m.e13 = Constraint(expr= m.x151 - m.x166 - m.x167 <= 0)
m.e14 = Constraint(expr= -m.x151 + m.x166 - m.x167 <= 0)
m.e15 = Constraint(expr= m.x154 - m.x168 - m.x169 <= 0)
m.e16 = Constraint(expr= -m.x154 + m.x168 - m.x169 <= 0)
m.e17 = Constraint(expr= m.x157 - m.x170 - m.x171 <= 0)
m.e18 = Constraint(expr= -m.x157 + m.x170 - m.x171 <= 0)
m.e19 = Constraint(expr= m.x151 - m.x172 - m.x173 <= 0)
m.e20 = Constraint(expr= -m.x151 + m.x172 - m.x173 <= 0)
m.e21 = Constraint(expr= m.x154 - m.x174 - m.x175 <= 0)
m.e22 = Constraint(expr= -m.x154 + m.x174 - m.x175 <= 0)
m.e23 = Constraint(expr= m.x157 - m.x176 - m.x177 <= 0)
m.e24 = Constraint(expr= -m.x157 + m.x176 - m.x177 <= 0)
m.e25 = Constraint(expr= m.x152 - m.x160 - m.x178 <= 0)
m.e26 = Constraint(expr= -m.x152 + m.x160 - m.x178 <= 0)
m.e27 = Constraint(expr= m.x155 - m.x162 - m.x179 <= 0)
m.e28 = Constraint(expr= -m.x155 + m.x162 - m.x179 <= 0)
m.e29 = Constraint(expr= m.x158 - m.x164 - m.x180 <= 0)
m.e30 = Constraint(expr= -m.x158 + m.x164 - m.x180 <= 0)
m.e31 = Constraint(expr= m.x152 - m.x166 - m.x181 <= 0)
m.e32 = Constraint(expr= -m.x152 + m.x166 - m.x181 <= 0)
m.e33 = Constraint(expr= m.x155 - m.x168 - m.x182 <= 0)
m.e34 = Constraint(expr= -m.x155 + m.x168 - m.x182 <= 0)
m.e35 = Constraint(expr= m.x158 - m.x170 - m.x183 <= 0)
m.e36 = Constraint(expr= -m.x158 + m.x170 - m.x183 <= 0)
m.e37 = Constraint(expr= m.x152 - m.x172 - m.x184 <= 0)
m.e38 = Constraint(expr= -m.x152 + m.x172 - m.x184 <= 0)
m.e39 = Constraint(expr= m.x155 - m.x174 - m.x185 <= 0)
m.e40 = Constraint(expr= -m.x155 + m.x174 - m.x185 <= 0)
m.e41 = Constraint(expr= m.x158 - m.x176 - m.x186 <= 0)
m.e42 = Constraint(expr= -m.x158 + m.x176 - m.x186 <= 0)
m.e43 = Constraint(expr= m.x160 - m.x166 - m.x187 <= 0)
m.e44 = Constraint(expr= -m.x160 + m.x166 - m.x187 <= 0)
m.e45 = Constraint(expr= m.x162 - m.x168 - m.x188 <= 0)
m.e46 = Constraint(expr= -m.x162 + m.x168 - m.x188 <= 0)
m.e47 = Constraint(expr= m.x164 - m.x170 - m.x189 <= 0)
m.e48 = Constraint(expr= -m.x164 + m.x170 - m.x189 <= 0)
m.e49 = Constraint(expr= m.x160 - m.x172 - m.x190 <= 0)
m.e50 = Constraint(expr= -m.x160 + m.x172 - m.x190 <= 0)
m.e51 = Constraint(expr= m.x162 - m.x174 - m.x191 <= 0)
m.e52 = Constraint(expr= -m.x162 + m.x174 - m.x191 <= 0)
m.e53 = Constraint(expr= m.x164 - m.x176 - m.x192 <= 0)
m.e54 = Constraint(expr= -m.x164 + m.x176 - m.x192 <= 0)
m.e55 = Constraint(expr= m.x166 - m.x172 - m.x193 <= 0)
m.e56 = Constraint(expr= -m.x166 + m.x172 - m.x193 <= 0)
m.e57 = Constraint(expr= m.x168 - m.x174 - m.x194 <= 0)
m.e58 = Constraint(expr= -m.x168 + m.x174 - m.x194 <= 0)
m.e59 = Constraint(expr= m.x170 - m.x176 - m.x195 <= 0)
m.e60 = Constraint(expr= -m.x170 + m.x176 - m.x195 <= 0)
m.e61 = Constraint(expr= (4.83202054247519 - m.x151)**2 + (5.08041476544912 -
    m.x154)**2 + (6.32621379041806 - m.x157)**2 + 75.9704013248235 * m.b1
    <= 76.9704013248235)
m.e62 = Constraint(expr= (6.86422157586402 - m.x151)**2 + (7.66428209799864 -
    m.x154)**2 + (0.09709175573132 - m.x157)**2 + 140.659182931282 * m.b2
    <= 141.659182931282)
m.e63 = Constraint(expr= (4.84862000711289 - m.x151)**2 + (3.45257195120785 -
    m.x154)**2 + (7.39094773970617 - m.x157)**2 + 109.037662329134 * m.b3
    <= 110.037662329134)
m.e64 = Constraint(expr= (1.90653576175828 - m.x151)**2 + (9.06815267710453 -
    m.x154)**2 + (0.329270310437709 - m.x157)**2 + 179.094987294124 * m.b4
    <= 180.094987294124)
m.e65 = Constraint(expr= (8.91873287322862 - m.x151)**2 + (3.005493222209 -
    m.x154)**2 + (6.72603314933737 - m.x157)**2 + 149.370448589907 * m.b5
    <= 150.370448589907)
m.e66 = Constraint(expr= (2.79219011695411 - m.x151)**2 + (0.0802363505466042
    - m.x154)**2 + (5.8239689013093 - m.x157)**2 + 161.969348685106 * m.b6
    <= 162.969348685106)
m.e67 = Constraint(expr= (8.45192604487847 - m.x151)**2 + (0.960982267180915 -
    m.x154)**2 + (7.08846749273086 - m.x157)**2 + 179.094987294124 * m.b7
    <= 180.094987294124)
m.e68 = Constraint(expr= (9.76694746975659 - m.x151)**2 + (1.64767982343444 -
    m.x154)**2 + (3.89461195866276 - m.x157)**2 + 152.326136990614 * m.b8
    <= 153.326136990614)
m.e69 = Constraint(expr= (3.92650027388399 - m.x151)**2 + (8.57900429288824 -
    m.x154)**2 + (9.23525817101371 - m.x157)**2 + 147.501061227256 * m.b9
    <= 148.501061227256)
m.e70 = Constraint(expr= (0.679990404106158 - m.x151)**2 + (7.93354548453717 -
    m.x154)**2 + (6.24827514848977 - m.x157)**2 + 150.218840203818 * m.b10
    <= 151.218840203818)
m.e71 = Constraint(expr= (3.80282662917579 - m.x151)**2 + (5.00336142496769 -
    m.x154)**2 + (6.01003348085459 - m.x157)**2 + 79.871242402384 * m.b11
    <= 80.871242402384)
m.e72 = Constraint(expr= (6.54293331034743 - m.x151)**2 + (1.49363772657694 -
    m.x154)**2 + (3.58497465463316 - m.x157)**2 + 108.386687957096 * m.b12
    <= 109.386687957096)
m.e73 = Constraint(expr= (5.20241765093859 - m.x151)**2 + (5.86977990966318 -
    m.x154)**2 + (6.440337805336 - m.x157)**2 + 73.72646594677 * m.b13
    <= 74.72646594677)
m.e74 = Constraint(expr= (5.87470028021075 - m.x151)**2 + (2.67028689434427 -
    m.x154)**2 + (0.749156996429077 - m.x157)**2 + 131.767274170968 * m.b14
    <= 132.767274170968)
m.e75 = Constraint(expr= (2.89776733906328 - m.x151)**2 + (5.22108290497701 -
    m.x154)**2 + (7.57016691626461 - m.x157)**2 + 107.46773494331 * m.b15
    <= 108.46773494331)
m.e76 = Constraint(expr= (3.25002624472116 - m.x151)**2 + (6.977422017743 -
    m.x154)**2 + (0.695695115140367 - m.x157)**2 + 124.533164159302 * m.b16
    <= 125.533164159302)
m.e77 = Constraint(expr= (8.47049713128073 - m.x151)**2 + (4.20582102463618 -
    m.x154)**2 + (4.93941262529365 - m.x157)**2 + 106.740936443786 * m.b17
    <= 107.740936443786)
m.e78 = Constraint(expr= (0.786615440794736 - m.x151)**2 + (1.54813106254315 -
    m.x154)**2 + (2.98963379540322 - m.x157)**2 + 150.565522268974 * m.b18
    <= 151.565522268974)
m.e79 = Constraint(expr= (5.17568572881879 - m.x151)**2 + (2.02627806544288 -
    m.x154)**2 + (9.2740633418688 - m.x157)**2 + 163.973027168021 * m.b19
    <= 164.973027168021)
m.e80 = Constraint(expr= (9.11874181180651 - m.x151)**2 + (9.07966816070985 -
    m.x154)**2 + (1.64995049320116 - m.x157)**2 + 161.969348685106 * m.b20
    <= 162.969348685106)
m.e81 = Constraint(expr= (8.26392769674786 - m.x151)**2 + (4.29716878332203 -
    m.x154)**2 + (3.06511979366618 - m.x157)**2 + 98.8575703440414 * m.b21
    <= 99.8575703440414)
m.e82 = Constraint(expr= (2.95522257480442 - m.x151)**2 + (1.29725120442498 -
    m.x154)**2 + (0.799527585103169 - m.x157)**2 + 147.501061227256 * m.b22
    <= 148.501061227256)
m.e83 = Constraint(expr= (5.59281220526297 - m.x151)**2 + (5.08387949672858 -
    m.x154)**2 + (0.547463810150197 - m.x157)**2 + 109.493435167956 * m.b23
    <= 110.493435167956)
m.e84 = Constraint(expr= (5.5713321706538 - m.x151)**2 + (3.89813512317444 -
    m.x154)**2 + (0.378899938163517 - m.x157)**2 + 123.353905785717 * m.b24
    <= 124.353905785717)
m.e85 = Constraint(expr= (1.47483805835463 - m.x151)**2 + (0.989752492299246 -
    m.x154)**2 + (5.36717263813865 - m.x157)**2 + 161.162335824934 * m.b25
    <= 162.162335824934)
m.e86 = Constraint(expr= (4.61507078501251 - m.x151)**2 + (0.234707301612243 -
    m.x154)**2 + (3.97342857514894 - m.x157)**2 + 124.302670822369 * m.b26
    <= 125.302670822369)
m.e87 = Constraint(expr= (9.15405801517484 - m.x151)**2 + (4.26169733166395 -
    m.x154)**2 + (4.89911772871142 - m.x157)**2 + 116.160211358947 * m.b27
    <= 117.160211358947)
m.e88 = Constraint(expr= (6.23408727244271 - m.x151)**2 + (0.755925845511098 -
    m.x154)**2 + (5.40595672236618 - m.x157)**2 + 134.909618001418 * m.b28
    <= 135.909618001418)
m.e89 = Constraint(expr= (5.16744991507397 - m.x151)**2 + (5.25535097293888 -
    m.x154)**2 + (3.81062986996748 - m.x157)**2 + 54.9767406737741 * m.b29
    <= 55.9767406737741)
m.e90 = Constraint(expr= (7.23609076996082 - m.x151)**2 + (3.30048962157922 -
    m.x154)**2 + (8.05002431260521 - m.x157)**2 + 143.305588261876 * m.b30
    <= 144.305588261876)
m.e91 = Constraint(expr= m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8
    + m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17 +
    m.b18 + m.b19 + m.b20 + m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 +
    m.b27 + m.b28 + m.b29 + m.b30 == 1)
m.e92 = Constraint(expr= (4.83202054247519 - m.x152)**2 + (5.08041476544912 -
    m.x155)**2 + (6.32621379041806 - m.x158)**2 + 75.9704013248235 * m.b31
    <= 76.9704013248235)
m.e93 = Constraint(expr= (6.86422157586402 - m.x152)**2 + (7.66428209799864 -
    m.x155)**2 + (0.09709175573132 - m.x158)**2 + 140.659182931282 * m.b32
    <= 141.659182931282)
m.e94 = Constraint(expr= (4.84862000711289 - m.x152)**2 + (3.45257195120785 -
    m.x155)**2 + (7.39094773970617 - m.x158)**2 + 109.037662329134 * m.b33
    <= 110.037662329134)
m.e95 = Constraint(expr= (1.90653576175828 - m.x152)**2 + (9.06815267710453 -
    m.x155)**2 + (0.329270310437709 - m.x158)**2 + 179.094987294124 * m.b34
    <= 180.094987294124)
m.e96 = Constraint(expr= (8.91873287322862 - m.x152)**2 + (3.005493222209 -
    m.x155)**2 + (6.72603314933737 - m.x158)**2 + 149.370448589907 * m.b35
    <= 150.370448589907)
m.e97 = Constraint(expr= (2.79219011695411 - m.x152)**2 + (0.0802363505466042
    - m.x155)**2 + (5.8239689013093 - m.x158)**2 + 161.969348685106 * m.b36
    <= 162.969348685106)
m.e98 = Constraint(expr= (8.45192604487847 - m.x152)**2 + (0.960982267180915 -
    m.x155)**2 + (7.08846749273086 - m.x158)**2 + 179.094987294124 * m.b37
    <= 180.094987294124)
m.e99 = Constraint(expr= (9.76694746975659 - m.x152)**2 + (1.64767982343444 -
    m.x155)**2 + (3.89461195866276 - m.x158)**2 + 152.326136990614 * m.b38
    <= 153.326136990614)
m.e100 = Constraint(expr= (3.92650027388399 - m.x152)**2 + (8.57900429288824 -
    m.x155)**2 + (9.23525817101371 - m.x158)**2 + 147.501061227256 * m.b39
    <= 148.501061227256)
m.e101 = Constraint(expr= (0.679990404106158 - m.x152)**2 + (7.93354548453717
    - m.x155)**2 + (6.24827514848977 - m.x158)**2 + 150.218840203818 * m.b40
    <= 151.218840203818)
m.e102 = Constraint(expr= (3.80282662917579 - m.x152)**2 + (5.00336142496769 -
    m.x155)**2 + (6.01003348085459 - m.x158)**2 + 79.871242402384 * m.b41
    <= 80.871242402384)
m.e103 = Constraint(expr= (6.54293331034743 - m.x152)**2 + (1.49363772657694 -
    m.x155)**2 + (3.58497465463316 - m.x158)**2 + 108.386687957096 * m.b42
    <= 109.386687957096)
m.e104 = Constraint(expr= (5.20241765093859 - m.x152)**2 + (5.86977990966318 -
    m.x155)**2 + (6.440337805336 - m.x158)**2 + 73.72646594677 * m.b43
    <= 74.72646594677)
m.e105 = Constraint(expr= (5.87470028021075 - m.x152)**2 + (2.67028689434427 -
    m.x155)**2 + (0.749156996429077 - m.x158)**2 + 131.767274170968 * m.b44
    <= 132.767274170968)
m.e106 = Constraint(expr= (2.89776733906328 - m.x152)**2 + (5.22108290497701 -
    m.x155)**2 + (7.57016691626461 - m.x158)**2 + 107.46773494331 * m.b45
    <= 108.46773494331)
m.e107 = Constraint(expr= (3.25002624472116 - m.x152)**2 + (6.977422017743 -
    m.x155)**2 + (0.695695115140367 - m.x158)**2 + 124.533164159302 * m.b46
    <= 125.533164159302)
m.e108 = Constraint(expr= (8.47049713128073 - m.x152)**2 + (4.20582102463618 -
    m.x155)**2 + (4.93941262529365 - m.x158)**2 + 106.740936443786 * m.b47
    <= 107.740936443786)
m.e109 = Constraint(expr= (0.786615440794736 - m.x152)**2 + (1.54813106254315
    - m.x155)**2 + (2.98963379540322 - m.x158)**2 + 150.565522268974 * m.b48
    <= 151.565522268974)
m.e110 = Constraint(expr= (5.17568572881879 - m.x152)**2 + (2.02627806544288 -
    m.x155)**2 + (9.2740633418688 - m.x158)**2 + 163.973027168021 * m.b49
    <= 164.973027168021)
m.e111 = Constraint(expr= (9.11874181180651 - m.x152)**2 + (9.07966816070985 -
    m.x155)**2 + (1.64995049320116 - m.x158)**2 + 161.969348685106 * m.b50
    <= 162.969348685106)
m.e112 = Constraint(expr= (8.26392769674786 - m.x152)**2 + (4.29716878332203 -
    m.x155)**2 + (3.06511979366618 - m.x158)**2 + 98.8575703440414 * m.b51
    <= 99.8575703440414)
m.e113 = Constraint(expr= (2.95522257480442 - m.x152)**2 + (1.29725120442498 -
    m.x155)**2 + (0.799527585103169 - m.x158)**2 + 147.501061227256 * m.b52
    <= 148.501061227256)
m.e114 = Constraint(expr= (5.59281220526297 - m.x152)**2 + (5.08387949672858 -
    m.x155)**2 + (0.547463810150197 - m.x158)**2 + 109.493435167956 * m.b53
    <= 110.493435167956)
m.e115 = Constraint(expr= (5.5713321706538 - m.x152)**2 + (3.89813512317444 -
    m.x155)**2 + (0.378899938163517 - m.x158)**2 + 123.353905785717 * m.b54
    <= 124.353905785717)
m.e116 = Constraint(expr= (1.47483805835463 - m.x152)**2 + (0.989752492299246
    - m.x155)**2 + (5.36717263813865 - m.x158)**2 + 161.162335824934 * m.b55
    <= 162.162335824934)
m.e117 = Constraint(expr= (4.61507078501251 - m.x152)**2 + (0.234707301612243
    - m.x155)**2 + (3.97342857514894 - m.x158)**2 + 124.302670822369 * m.b56
    <= 125.302670822369)
m.e118 = Constraint(expr= (9.15405801517484 - m.x152)**2 + (4.26169733166395 -
    m.x155)**2 + (4.89911772871142 - m.x158)**2 + 116.160211358947 * m.b57
    <= 117.160211358947)
m.e119 = Constraint(expr= (6.23408727244271 - m.x152)**2 + (0.755925845511098
    - m.x155)**2 + (5.40595672236618 - m.x158)**2 + 134.909618001418 * m.b58
    <= 135.909618001418)
m.e120 = Constraint(expr= (5.16744991507397 - m.x152)**2 + (5.25535097293888 -
    m.x155)**2 + (3.81062986996748 - m.x158)**2 + 54.9767406737741 * m.b59
    <= 55.9767406737741)
m.e121 = Constraint(expr= (7.23609076996082 - m.x152)**2 + (3.30048962157922 -
    m.x155)**2 + (8.05002431260521 - m.x158)**2 + 143.305588261876 * m.b60
    <= 144.305588261876)
m.e122 = Constraint(expr= m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 + m.b37
    + m.b38 + m.b39 + m.b40 + m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 +
    m.b47 + m.b48 + m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 +
    m.b56 + m.b57 + m.b58 + m.b59 + m.b60 == 1)
m.e123 = Constraint(expr= (4.83202054247519 - m.x160)**2 + (5.08041476544912 -
    m.x162)**2 + (6.32621379041806 - m.x164)**2 + 75.9704013248235 * m.b61
    <= 76.9704013248235)
m.e124 = Constraint(expr= (6.86422157586402 - m.x160)**2 + (7.66428209799864 -
    m.x162)**2 + (0.09709175573132 - m.x164)**2 + 140.659182931282 * m.b62
    <= 141.659182931282)
m.e125 = Constraint(expr= (4.84862000711289 - m.x160)**2 + (3.45257195120785 -
    m.x162)**2 + (7.39094773970617 - m.x164)**2 + 109.037662329134 * m.b63
    <= 110.037662329134)
m.e126 = Constraint(expr= (1.90653576175828 - m.x160)**2 + (9.06815267710453 -
    m.x162)**2 + (0.329270310437709 - m.x164)**2 + 179.094987294124 * m.b64
    <= 180.094987294124)
m.e127 = Constraint(expr= (8.91873287322862 - m.x160)**2 + (3.005493222209 -
    m.x162)**2 + (6.72603314933737 - m.x164)**2 + 149.370448589907 * m.b65
    <= 150.370448589907)
m.e128 = Constraint(expr= (2.79219011695411 - m.x160)**2 + (0.0802363505466042
    - m.x162)**2 + (5.8239689013093 - m.x164)**2 + 161.969348685106 * m.b66
    <= 162.969348685106)
m.e129 = Constraint(expr= (8.45192604487847 - m.x160)**2 + (0.960982267180915
    - m.x162)**2 + (7.08846749273086 - m.x164)**2 + 179.094987294124 * m.b67
    <= 180.094987294124)
m.e130 = Constraint(expr= (9.76694746975659 - m.x160)**2 + (1.64767982343444 -
    m.x162)**2 + (3.89461195866276 - m.x164)**2 + 152.326136990614 * m.b68
    <= 153.326136990614)
m.e131 = Constraint(expr= (3.92650027388399 - m.x160)**2 + (8.57900429288824 -
    m.x162)**2 + (9.23525817101371 - m.x164)**2 + 147.501061227256 * m.b69
    <= 148.501061227256)
m.e132 = Constraint(expr= (0.679990404106158 - m.x160)**2 + (7.93354548453717
    - m.x162)**2 + (6.24827514848977 - m.x164)**2 + 150.218840203818 * m.b70
    <= 151.218840203818)
m.e133 = Constraint(expr= (3.80282662917579 - m.x160)**2 + (5.00336142496769 -
    m.x162)**2 + (6.01003348085459 - m.x164)**2 + 79.871242402384 * m.b71
    <= 80.871242402384)
m.e134 = Constraint(expr= (6.54293331034743 - m.x160)**2 + (1.49363772657694 -
    m.x162)**2 + (3.58497465463316 - m.x164)**2 + 108.386687957096 * m.b72
    <= 109.386687957096)
m.e135 = Constraint(expr= (5.20241765093859 - m.x160)**2 + (5.86977990966318 -
    m.x162)**2 + (6.440337805336 - m.x164)**2 + 73.72646594677 * m.b73
    <= 74.72646594677)
m.e136 = Constraint(expr= (5.87470028021075 - m.x160)**2 + (2.67028689434427 -
    m.x162)**2 + (0.749156996429077 - m.x164)**2 + 131.767274170968 * m.b74
    <= 132.767274170968)
m.e137 = Constraint(expr= (2.89776733906328 - m.x160)**2 + (5.22108290497701 -
    m.x162)**2 + (7.57016691626461 - m.x164)**2 + 107.46773494331 * m.b75
    <= 108.46773494331)
m.e138 = Constraint(expr= (3.25002624472116 - m.x160)**2 + (6.977422017743 -
    m.x162)**2 + (0.695695115140367 - m.x164)**2 + 124.533164159302 * m.b76
    <= 125.533164159302)
m.e139 = Constraint(expr= (8.47049713128073 - m.x160)**2 + (4.20582102463618 -
    m.x162)**2 + (4.93941262529365 - m.x164)**2 + 106.740936443786 * m.b77
    <= 107.740936443786)
m.e140 = Constraint(expr= (0.786615440794736 - m.x160)**2 + (1.54813106254315
    - m.x162)**2 + (2.98963379540322 - m.x164)**2 + 150.565522268974 * m.b78
    <= 151.565522268974)
m.e141 = Constraint(expr= (5.17568572881879 - m.x160)**2 + (2.02627806544288 -
    m.x162)**2 + (9.2740633418688 - m.x164)**2 + 163.973027168021 * m.b79
    <= 164.973027168021)
m.e142 = Constraint(expr= (9.11874181180651 - m.x160)**2 + (9.07966816070985 -
    m.x162)**2 + (1.64995049320116 - m.x164)**2 + 161.969348685106 * m.b80
    <= 162.969348685106)
m.e143 = Constraint(expr= (8.26392769674786 - m.x160)**2 + (4.29716878332203 -
    m.x162)**2 + (3.06511979366618 - m.x164)**2 + 98.8575703440414 * m.b81
    <= 99.8575703440414)
m.e144 = Constraint(expr= (2.95522257480442 - m.x160)**2 + (1.29725120442498 -
    m.x162)**2 + (0.799527585103169 - m.x164)**2 + 147.501061227256 * m.b82
    <= 148.501061227256)
m.e145 = Constraint(expr= (5.59281220526297 - m.x160)**2 + (5.08387949672858 -
    m.x162)**2 + (0.547463810150197 - m.x164)**2 + 109.493435167956 * m.b83
    <= 110.493435167956)
m.e146 = Constraint(expr= (5.5713321706538 - m.x160)**2 + (3.89813512317444 -
    m.x162)**2 + (0.378899938163517 - m.x164)**2 + 123.353905785717 * m.b84
    <= 124.353905785717)
m.e147 = Constraint(expr= (1.47483805835463 - m.x160)**2 + (0.989752492299246
    - m.x162)**2 + (5.36717263813865 - m.x164)**2 + 161.162335824934 * m.b85
    <= 162.162335824934)
m.e148 = Constraint(expr= (4.61507078501251 - m.x160)**2 + (0.234707301612243
    - m.x162)**2 + (3.97342857514894 - m.x164)**2 + 124.302670822369 * m.b86
    <= 125.302670822369)
m.e149 = Constraint(expr= (9.15405801517484 - m.x160)**2 + (4.26169733166395 -
    m.x162)**2 + (4.89911772871142 - m.x164)**2 + 116.160211358947 * m.b87
    <= 117.160211358947)
m.e150 = Constraint(expr= (6.23408727244271 - m.x160)**2 + (0.755925845511098
    - m.x162)**2 + (5.40595672236618 - m.x164)**2 + 134.909618001418 * m.b88
    <= 135.909618001418)
m.e151 = Constraint(expr= (5.16744991507397 - m.x160)**2 + (5.25535097293888 -
    m.x162)**2 + (3.81062986996748 - m.x164)**2 + 54.9767406737741 * m.b89
    <= 55.9767406737741)
m.e152 = Constraint(expr= (7.23609076996082 - m.x160)**2 + (3.30048962157922 -
    m.x162)**2 + (8.05002431260521 - m.x164)**2 + 143.305588261876 * m.b90
    <= 144.305588261876)
m.e153 = Constraint(expr= m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b66 + m.b67
    + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 + m.b73 + m.b74 + m.b75 + m.b76 +
    m.b77 + m.b78 + m.b79 + m.b80 + m.b81 + m.b82 + m.b83 + m.b84 + m.b85 +
    m.b86 + m.b87 + m.b88 + m.b89 + m.b90 == 1)
m.e154 = Constraint(expr= (4.83202054247519 - m.x166)**2 + (5.08041476544912 -
    m.x168)**2 + (6.32621379041806 - m.x170)**2 + 75.9704013248235 * m.b91
    <= 76.9704013248235)
m.e155 = Constraint(expr= (6.86422157586402 - m.x166)**2 + (7.66428209799864 -
    m.x168)**2 + (0.09709175573132 - m.x170)**2 + 140.659182931282 * m.b92
    <= 141.659182931282)
m.e156 = Constraint(expr= (4.84862000711289 - m.x166)**2 + (3.45257195120785 -
    m.x168)**2 + (7.39094773970617 - m.x170)**2 + 109.037662329134 * m.b93
    <= 110.037662329134)
m.e157 = Constraint(expr= (1.90653576175828 - m.x166)**2 + (9.06815267710453 -
    m.x168)**2 + (0.329270310437709 - m.x170)**2 + 179.094987294124 * m.b94
    <= 180.094987294124)
m.e158 = Constraint(expr= (8.91873287322862 - m.x166)**2 + (3.005493222209 -
    m.x168)**2 + (6.72603314933737 - m.x170)**2 + 149.370448589907 * m.b95
    <= 150.370448589907)
m.e159 = Constraint(expr= (2.79219011695411 - m.x166)**2 + (0.0802363505466042
    - m.x168)**2 + (5.8239689013093 - m.x170)**2 + 161.969348685106 * m.b96
    <= 162.969348685106)
m.e160 = Constraint(expr= (8.45192604487847 - m.x166)**2 + (0.960982267180915
    - m.x168)**2 + (7.08846749273086 - m.x170)**2 + 179.094987294124 * m.b97
    <= 180.094987294124)
m.e161 = Constraint(expr= (9.76694746975659 - m.x166)**2 + (1.64767982343444 -
    m.x168)**2 + (3.89461195866276 - m.x170)**2 + 152.326136990614 * m.b98
    <= 153.326136990614)
m.e162 = Constraint(expr= (3.92650027388399 - m.x166)**2 + (8.57900429288824 -
    m.x168)**2 + (9.23525817101371 - m.x170)**2 + 147.501061227256 * m.b99
    <= 148.501061227256)
m.e163 = Constraint(expr= (0.679990404106158 - m.x166)**2 + (7.93354548453717
    - m.x168)**2 + (6.24827514848977 - m.x170)**2 + 150.218840203818 * m.b100
    <= 151.218840203818)
m.e164 = Constraint(expr= (3.80282662917579 - m.x166)**2 + (5.00336142496769 -
    m.x168)**2 + (6.01003348085459 - m.x170)**2 + 79.871242402384 * m.b101
    <= 80.871242402384)
m.e165 = Constraint(expr= (6.54293331034743 - m.x166)**2 + (1.49363772657694 -
    m.x168)**2 + (3.58497465463316 - m.x170)**2 + 108.386687957096 * m.b102
    <= 109.386687957096)
m.e166 = Constraint(expr= (5.20241765093859 - m.x166)**2 + (5.86977990966318 -
    m.x168)**2 + (6.440337805336 - m.x170)**2 + 73.72646594677 * m.b103
    <= 74.72646594677)
m.e167 = Constraint(expr= (5.87470028021075 - m.x166)**2 + (2.67028689434427 -
    m.x168)**2 + (0.749156996429077 - m.x170)**2 + 131.767274170968 * m.b104
    <= 132.767274170968)
m.e168 = Constraint(expr= (2.89776733906328 - m.x166)**2 + (5.22108290497701 -
    m.x168)**2 + (7.57016691626461 - m.x170)**2 + 107.46773494331 * m.b105
    <= 108.46773494331)
m.e169 = Constraint(expr= (3.25002624472116 - m.x166)**2 + (6.977422017743 -
    m.x168)**2 + (0.695695115140367 - m.x170)**2 + 124.533164159302 * m.b106
    <= 125.533164159302)
m.e170 = Constraint(expr= (8.47049713128073 - m.x166)**2 + (4.20582102463618 -
    m.x168)**2 + (4.93941262529365 - m.x170)**2 + 106.740936443786 * m.b107
    <= 107.740936443786)
m.e171 = Constraint(expr= (0.786615440794736 - m.x166)**2 + (1.54813106254315
    - m.x168)**2 + (2.98963379540322 - m.x170)**2 + 150.565522268974 * m.b108
    <= 151.565522268974)
m.e172 = Constraint(expr= (5.17568572881879 - m.x166)**2 + (2.02627806544288 -
    m.x168)**2 + (9.2740633418688 - m.x170)**2 + 163.973027168021 * m.b109
    <= 164.973027168021)
m.e173 = Constraint(expr= (9.11874181180651 - m.x166)**2 + (9.07966816070985 -
    m.x168)**2 + (1.64995049320116 - m.x170)**2 + 161.969348685106 * m.b110
    <= 162.969348685106)
m.e174 = Constraint(expr= (8.26392769674786 - m.x166)**2 + (4.29716878332203 -
    m.x168)**2 + (3.06511979366618 - m.x170)**2 + 98.8575703440414 * m.b111
    <= 99.8575703440414)
m.e175 = Constraint(expr= (2.95522257480442 - m.x166)**2 + (1.29725120442498 -
    m.x168)**2 + (0.799527585103169 - m.x170)**2 + 147.501061227256 * m.b112
    <= 148.501061227256)
m.e176 = Constraint(expr= (5.59281220526297 - m.x166)**2 + (5.08387949672858 -
    m.x168)**2 + (0.547463810150197 - m.x170)**2 + 109.493435167956 * m.b113
    <= 110.493435167956)
m.e177 = Constraint(expr= (5.5713321706538 - m.x166)**2 + (3.89813512317444 -
    m.x168)**2 + (0.378899938163517 - m.x170)**2 + 123.353905785717 * m.b114
    <= 124.353905785717)
m.e178 = Constraint(expr= (1.47483805835463 - m.x166)**2 + (0.989752492299246
    - m.x168)**2 + (5.36717263813865 - m.x170)**2 + 161.162335824934 * m.b115
    <= 162.162335824934)
m.e179 = Constraint(expr= (4.61507078501251 - m.x166)**2 + (0.234707301612243
    - m.x168)**2 + (3.97342857514894 - m.x170)**2 + 124.302670822369 * m.b116
    <= 125.302670822369)
m.e180 = Constraint(expr= (9.15405801517484 - m.x166)**2 + (4.26169733166395 -
    m.x168)**2 + (4.89911772871142 - m.x170)**2 + 116.160211358947 * m.b117
    <= 117.160211358947)
m.e181 = Constraint(expr= (6.23408727244271 - m.x166)**2 + (0.755925845511098
    - m.x168)**2 + (5.40595672236618 - m.x170)**2 + 134.909618001418 * m.b118
    <= 135.909618001418)
m.e182 = Constraint(expr= (5.16744991507397 - m.x166)**2 + (5.25535097293888 -
    m.x168)**2 + (3.81062986996748 - m.x170)**2 + 54.9767406737741 * m.b119
    <= 55.9767406737741)
m.e183 = Constraint(expr= (7.23609076996082 - m.x166)**2 + (3.30048962157922 -
    m.x168)**2 + (8.05002431260521 - m.x170)**2 + 143.305588261876 * m.b120
    <= 144.305588261876)
m.e184 = Constraint(expr= m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b96 + m.b97
    + m.b98 + m.b99 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104 + m.b105 +
    m.b106 + m.b107 + m.b108 + m.b109 + m.b110 + m.b111 + m.b112 + m.b113 +
    m.b114 + m.b115 + m.b116 + m.b117 + m.b118 + m.b119 + m.b120 == 1)
m.e185 = Constraint(expr= (4.83202054247519 - m.x172)**2 + (5.08041476544912 -
    m.x174)**2 + (6.32621379041806 - m.x176)**2 + 75.9704013248235 * m.b121
    <= 76.9704013248235)
m.e186 = Constraint(expr= (6.86422157586402 - m.x172)**2 + (7.66428209799864 -
    m.x174)**2 + (0.09709175573132 - m.x176)**2 + 140.659182931282 * m.b122
    <= 141.659182931282)
m.e187 = Constraint(expr= (4.84862000711289 - m.x172)**2 + (3.45257195120785 -
    m.x174)**2 + (7.39094773970617 - m.x176)**2 + 109.037662329134 * m.b123
    <= 110.037662329134)
m.e188 = Constraint(expr= (1.90653576175828 - m.x172)**2 + (9.06815267710453 -
    m.x174)**2 + (0.329270310437709 - m.x176)**2 + 179.094987294124 * m.b124
    <= 180.094987294124)
m.e189 = Constraint(expr= (8.91873287322862 - m.x172)**2 + (3.005493222209 -
    m.x174)**2 + (6.72603314933737 - m.x176)**2 + 149.370448589907 * m.b125
    <= 150.370448589907)
m.e190 = Constraint(expr= (2.79219011695411 - m.x172)**2 + (0.0802363505466042
    - m.x174)**2 + (5.8239689013093 - m.x176)**2 + 161.969348685106 * m.b126
    <= 162.969348685106)
m.e191 = Constraint(expr= (8.45192604487847 - m.x172)**2 + (0.960982267180915
    - m.x174)**2 + (7.08846749273086 - m.x176)**2 + 179.094987294124 * m.b127
    <= 180.094987294124)
m.e192 = Constraint(expr= (9.76694746975659 - m.x172)**2 + (1.64767982343444 -
    m.x174)**2 + (3.89461195866276 - m.x176)**2 + 152.326136990614 * m.b128
    <= 153.326136990614)
m.e193 = Constraint(expr= (3.92650027388399 - m.x172)**2 + (8.57900429288824 -
    m.x174)**2 + (9.23525817101371 - m.x176)**2 + 147.501061227256 * m.b129
    <= 148.501061227256)
m.e194 = Constraint(expr= (0.679990404106158 - m.x172)**2 + (7.93354548453717
    - m.x174)**2 + (6.24827514848977 - m.x176)**2 + 150.218840203818 * m.b130
    <= 151.218840203818)
m.e195 = Constraint(expr= (3.80282662917579 - m.x172)**2 + (5.00336142496769 -
    m.x174)**2 + (6.01003348085459 - m.x176)**2 + 79.871242402384 * m.b131
    <= 80.871242402384)
m.e196 = Constraint(expr= (6.54293331034743 - m.x172)**2 + (1.49363772657694 -
    m.x174)**2 + (3.58497465463316 - m.x176)**2 + 108.386687957096 * m.b132
    <= 109.386687957096)
m.e197 = Constraint(expr= (5.20241765093859 - m.x172)**2 + (5.86977990966318 -
    m.x174)**2 + (6.440337805336 - m.x176)**2 + 73.72646594677 * m.b133
    <= 74.72646594677)
m.e198 = Constraint(expr= (5.87470028021075 - m.x172)**2 + (2.67028689434427 -
    m.x174)**2 + (0.749156996429077 - m.x176)**2 + 131.767274170968 * m.b134
    <= 132.767274170968)
m.e199 = Constraint(expr= (2.89776733906328 - m.x172)**2 + (5.22108290497701 -
    m.x174)**2 + (7.57016691626461 - m.x176)**2 + 107.46773494331 * m.b135
    <= 108.46773494331)
m.e200 = Constraint(expr= (3.25002624472116 - m.x172)**2 + (6.977422017743 -
    m.x174)**2 + (0.695695115140367 - m.x176)**2 + 124.533164159302 * m.b136
    <= 125.533164159302)
m.e201 = Constraint(expr= (8.47049713128073 - m.x172)**2 + (4.20582102463618 -
    m.x174)**2 + (4.93941262529365 - m.x176)**2 + 106.740936443786 * m.b137
    <= 107.740936443786)
m.e202 = Constraint(expr= (0.786615440794736 - m.x172)**2 + (1.54813106254315
    - m.x174)**2 + (2.98963379540322 - m.x176)**2 + 150.565522268974 * m.b138
    <= 151.565522268974)
m.e203 = Constraint(expr= (5.17568572881879 - m.x172)**2 + (2.02627806544288 -
    m.x174)**2 + (9.2740633418688 - m.x176)**2 + 163.973027168021 * m.b139
    <= 164.973027168021)
m.e204 = Constraint(expr= (9.11874181180651 - m.x172)**2 + (9.07966816070985 -
    m.x174)**2 + (1.64995049320116 - m.x176)**2 + 161.969348685106 * m.b140
    <= 162.969348685106)
m.e205 = Constraint(expr= (8.26392769674786 - m.x172)**2 + (4.29716878332203 -
    m.x174)**2 + (3.06511979366618 - m.x176)**2 + 98.8575703440414 * m.b141
    <= 99.8575703440414)
m.e206 = Constraint(expr= (2.95522257480442 - m.x172)**2 + (1.29725120442498 -
    m.x174)**2 + (0.799527585103169 - m.x176)**2 + 147.501061227256 * m.b142
    <= 148.501061227256)
m.e207 = Constraint(expr= (5.59281220526297 - m.x172)**2 + (5.08387949672858 -
    m.x174)**2 + (0.547463810150197 - m.x176)**2 + 109.493435167956 * m.b143
    <= 110.493435167956)
m.e208 = Constraint(expr= (5.5713321706538 - m.x172)**2 + (3.89813512317444 -
    m.x174)**2 + (0.378899938163517 - m.x176)**2 + 123.353905785717 * m.b144
    <= 124.353905785717)
m.e209 = Constraint(expr= (1.47483805835463 - m.x172)**2 + (0.989752492299246
    - m.x174)**2 + (5.36717263813865 - m.x176)**2 + 161.162335824934 * m.b145
    <= 162.162335824934)
m.e210 = Constraint(expr= (4.61507078501251 - m.x172)**2 + (0.234707301612243
    - m.x174)**2 + (3.97342857514894 - m.x176)**2 + 124.302670822369 * m.b146
    <= 125.302670822369)
m.e211 = Constraint(expr= (9.15405801517484 - m.x172)**2 + (4.26169733166395 -
    m.x174)**2 + (4.89911772871142 - m.x176)**2 + 116.160211358947 * m.b147
    <= 117.160211358947)
m.e212 = Constraint(expr= (6.23408727244271 - m.x172)**2 + (0.755925845511098
    - m.x174)**2 + (5.40595672236618 - m.x176)**2 + 134.909618001418 * m.b148
    <= 135.909618001418)
m.e213 = Constraint(expr= (5.16744991507397 - m.x172)**2 + (5.25535097293888 -
    m.x174)**2 + (3.81062986996748 - m.x176)**2 + 54.9767406737741 * m.b149
    <= 55.9767406737741)
m.e214 = Constraint(expr= (7.23609076996082 - m.x172)**2 + (3.30048962157922 -
    m.x174)**2 + (8.05002431260521 - m.x176)**2 + 143.305588261876 * m.b150
    <= 144.305588261876)
m.e215 = Constraint(expr= m.b121 + m.b122 + m.b123 + m.b124 + m.b125 + m.b126
    + m.b127 + m.b128 + m.b129 + m.b130 + m.b131 + m.b132 + m.b133 + m.b134 +
    m.b135 + m.b136 + m.b137 + m.b138 + m.b139 + m.b140 + m.b141 + m.b142 +
    m.b143 + m.b144 + m.b145 + m.b146 + m.b147 + m.b148 + m.b149 + m.b150 == 1)
m.e216 = Constraint(expr= m.b1 + m.b31 + m.b61 + m.b91 + m.b121 <= 1)
m.e217 = Constraint(expr= m.b2 + m.b32 + m.b62 + m.b92 + m.b122 <= 1)
m.e218 = Constraint(expr= m.b3 + m.b33 + m.b63 + m.b93 + m.b123 <= 1)
m.e219 = Constraint(expr= m.b4 + m.b34 + m.b64 + m.b94 + m.b124 <= 1)
m.e220 = Constraint(expr= m.b5 + m.b35 + m.b65 + m.b95 + m.b125 <= 1)
m.e221 = Constraint(expr= m.b6 + m.b36 + m.b66 + m.b96 + m.b126 <= 1)
m.e222 = Constraint(expr= m.b7 + m.b37 + m.b67 + m.b97 + m.b127 <= 1)
m.e223 = Constraint(expr= m.b8 + m.b38 + m.b68 + m.b98 + m.b128 <= 1)
m.e224 = Constraint(expr= m.b9 + m.b39 + m.b69 + m.b99 + m.b129 <= 1)
m.e225 = Constraint(expr= m.b10 + m.b40 + m.b70 + m.b100 + m.b130 <= 1)
m.e226 = Constraint(expr= m.b11 + m.b41 + m.b71 + m.b101 + m.b131 <= 1)
m.e227 = Constraint(expr= m.b12 + m.b42 + m.b72 + m.b102 + m.b132 <= 1)
m.e228 = Constraint(expr= m.b13 + m.b43 + m.b73 + m.b103 + m.b133 <= 1)
m.e229 = Constraint(expr= m.b14 + m.b44 + m.b74 + m.b104 + m.b134 <= 1)
m.e230 = Constraint(expr= m.b15 + m.b45 + m.b75 + m.b105 + m.b135 <= 1)
m.e231 = Constraint(expr= m.b16 + m.b46 + m.b76 + m.b106 + m.b136 <= 1)
m.e232 = Constraint(expr= m.b17 + m.b47 + m.b77 + m.b107 + m.b137 <= 1)
m.e233 = Constraint(expr= m.b18 + m.b48 + m.b78 + m.b108 + m.b138 <= 1)
m.e234 = Constraint(expr= m.b19 + m.b49 + m.b79 + m.b109 + m.b139 <= 1)
m.e235 = Constraint(expr= m.b20 + m.b50 + m.b80 + m.b110 + m.b140 <= 1)
m.e236 = Constraint(expr= m.b21 + m.b51 + m.b81 + m.b111 + m.b141 <= 1)
m.e237 = Constraint(expr= m.b22 + m.b52 + m.b82 + m.b112 + m.b142 <= 1)
m.e238 = Constraint(expr= m.b23 + m.b53 + m.b83 + m.b113 + m.b143 <= 1)
m.e239 = Constraint(expr= m.b24 + m.b54 + m.b84 + m.b114 + m.b144 <= 1)
m.e240 = Constraint(expr= m.b25 + m.b55 + m.b85 + m.b115 + m.b145 <= 1)
m.e241 = Constraint(expr= m.b26 + m.b56 + m.b86 + m.b116 + m.b146 <= 1)
m.e242 = Constraint(expr= m.b27 + m.b57 + m.b87 + m.b117 + m.b147 <= 1)
m.e243 = Constraint(expr= m.b28 + m.b58 + m.b88 + m.b118 + m.b148 <= 1)
m.e244 = Constraint(expr= m.b29 + m.b59 + m.b89 + m.b119 + m.b149 <= 1)
m.e245 = Constraint(expr= m.b30 + m.b60 + m.b90 + m.b120 + m.b150 <= 1)
m.e246 = Constraint(expr= m.x151 - m.x152 <= 0)
m.e247 = Constraint(expr= m.x152 - m.x160 <= 0)
m.e248 = Constraint(expr= m.x160 - m.x166 <= 0)
m.e249 = Constraint(expr= m.x166 - m.x172 <= 0)
