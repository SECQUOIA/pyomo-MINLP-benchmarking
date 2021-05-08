# MINLP written by GAMS Convert at 05/07/21 17:13:01
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       229        5        0      224        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       180       30      150        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       878      578      300
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
m.b25 = Var(within=Binary, bounds=(0,1), initialize=1)
m.b26 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b27 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b28 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b29 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b30 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b31 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b32 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b33 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b34 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b35 = Var(within=Binary, bounds=(0,1), initialize=1)
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
m.b69 = Var(within=Binary, bounds=(0,1), initialize=1)
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
m.b107 = Var(within=Binary, bounds=(0,1), initialize=1)
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
m.b144 = Var(within=Binary, bounds=(0,1), initialize=1)
m.b145 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b146 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b147 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b148 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b149 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b150 = Var(within=Binary, bounds=(0,1), initialize=0)
m.x151 = Var(within=Reals, bounds=(0,10), initialize=2.80824226248558)
m.x152 = Var(within=Reals, bounds=(0,10), initialize=2.80824226248558)
m.x153 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x154 = Var(within=Reals, bounds=(0,10), initialize=3.25902574907896)
m.x155 = Var(within=Reals, bounds=(0,10), initialize=3.25902574907896)
m.x156 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x157 = Var(within=Reals, bounds=(0,10), initialize=2.80824226248558)
m.x158 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x159 = Var(within=Reals, bounds=(0,10), initialize=3.25902574907896)
m.x160 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x161 = Var(within=Reals, bounds=(0,10), initialize=2.80824226248558)
m.x162 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x163 = Var(within=Reals, bounds=(0,10), initialize=3.25902574907896)
m.x164 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x165 = Var(within=Reals, bounds=(0,10), initialize=2.88110099828265)
m.x166 = Var(within=Reals, bounds=(0,10), initialize=0.072858735797072)
m.x167 = Var(within=Reals, bounds=(0,10), initialize=3.25902574907896)
m.x168 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x169 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x170 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x171 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x172 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x173 = Var(within=Reals, bounds=(0,10), initialize=0.072858735797072)
m.x174 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x175 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x176 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x177 = Var(within=Reals, bounds=(0,10), initialize=0.072858735797072)
m.x178 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x179 = Var(within=Reals, bounds=(0,10), initialize=0.072858735797072)
m.x180 = Var(within=Reals, bounds=(0,10), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x153 + m.x156 + m.x158 + m.x160 +
    m.x162 + m.x164 + m.x166 + m.x168 + m.x169 + m.x170 + m.x171 + m.x172 +
    m.x173 + m.x174 + m.x175 + m.x176 + m.x177 + m.x178 + m.x179 + m.x180)

m.e1 = Constraint(expr= m.x151 - m.x152 - m.x153 <= 0)
m.e2 = Constraint(expr= -m.x151 + m.x152 - m.x153 <= 0)
m.e3 = Constraint(expr= m.x154 - m.x155 - m.x156 <= 0)
m.e4 = Constraint(expr= -m.x154 + m.x155 - m.x156 <= 0)
m.e5 = Constraint(expr= m.x151 - m.x157 - m.x158 <= 0)
m.e6 = Constraint(expr= -m.x151 + m.x157 - m.x158 <= 0)
m.e7 = Constraint(expr= m.x154 - m.x159 - m.x160 <= 0)
m.e8 = Constraint(expr= -m.x154 + m.x159 - m.x160 <= 0)
m.e9 = Constraint(expr= m.x151 - m.x161 - m.x162 <= 0)
m.e10 = Constraint(expr= -m.x151 + m.x161 - m.x162 <= 0)
m.e11 = Constraint(expr= m.x154 - m.x163 - m.x164 <= 0)
m.e12 = Constraint(expr= -m.x154 + m.x163 - m.x164 <= 0)
m.e13 = Constraint(expr= m.x151 - m.x165 - m.x166 <= 0)
m.e14 = Constraint(expr= -m.x151 + m.x165 - m.x166 <= 0)
m.e15 = Constraint(expr= m.x154 - m.x167 - m.x168 <= 0)
m.e16 = Constraint(expr= -m.x154 + m.x167 - m.x168 <= 0)
m.e17 = Constraint(expr= m.x152 - m.x157 - m.x169 <= 0)
m.e18 = Constraint(expr= -m.x152 + m.x157 - m.x169 <= 0)
m.e19 = Constraint(expr= m.x155 - m.x159 - m.x170 <= 0)
m.e20 = Constraint(expr= -m.x155 + m.x159 - m.x170 <= 0)
m.e21 = Constraint(expr= m.x152 - m.x161 - m.x171 <= 0)
m.e22 = Constraint(expr= -m.x152 + m.x161 - m.x171 <= 0)
m.e23 = Constraint(expr= m.x155 - m.x163 - m.x172 <= 0)
m.e24 = Constraint(expr= -m.x155 + m.x163 - m.x172 <= 0)
m.e25 = Constraint(expr= m.x152 - m.x165 - m.x173 <= 0)
m.e26 = Constraint(expr= -m.x152 + m.x165 - m.x173 <= 0)
m.e27 = Constraint(expr= m.x155 - m.x167 - m.x174 <= 0)
m.e28 = Constraint(expr= -m.x155 + m.x167 - m.x174 <= 0)
m.e29 = Constraint(expr= m.x157 - m.x161 - m.x175 <= 0)
m.e30 = Constraint(expr= -m.x157 + m.x161 - m.x175 <= 0)
m.e31 = Constraint(expr= m.x159 - m.x163 - m.x176 <= 0)
m.e32 = Constraint(expr= -m.x159 + m.x163 - m.x176 <= 0)
m.e33 = Constraint(expr= m.x157 - m.x165 - m.x177 <= 0)
m.e34 = Constraint(expr= -m.x157 + m.x165 - m.x177 <= 0)
m.e35 = Constraint(expr= m.x159 - m.x167 - m.x178 <= 0)
m.e36 = Constraint(expr= -m.x159 + m.x167 - m.x178 <= 0)
m.e37 = Constraint(expr= m.x161 - m.x165 - m.x179 <= 0)
m.e38 = Constraint(expr= -m.x161 + m.x165 - m.x179 <= 0)
m.e39 = Constraint(expr= m.x163 - m.x167 - m.x180 <= 0)
m.e40 = Constraint(expr= -m.x163 + m.x167 - m.x180 <= 0)
m.e41 = Constraint(expr= (3.58392835071893 - m.x151)**2 + (0.44370753979378 -
    m.x154)**2 + 117.37605108924 * m.b1 <= 118.37605108924)
m.e42 = Constraint(expr= (1.95628884344 - m.x151)**2 + (0.390503036650278 -
    m.x154)**2 + 140.241701004457 * m.b2 <= 141.241701004457)
m.e43 = Constraint(expr= (4.55035690490668 - m.x151)**2 + (7.27185840240323 -
    m.x154)**2 + 71.5594363053072 * m.b3 <= 72.5594363053072)
m.e44 = Constraint(expr= (6.2100872388646 - m.x151)**2 + (6.48745936675473 -
    m.x154)**2 + 70.1361240423208 * m.b4 <= 71.1361240423208)
m.e45 = Constraint(expr= (3.1786343207553 - m.x151)**2 + (2.35630065859291 -
    m.x154)**2 + 91.0983527000505 * m.b5 <= 92.0983527000505)
m.e46 = Constraint(expr= (2.77208272832737 - m.x151)**2 + (6.63537019621518 -
    m.x154)**2 + 78.1787285426132 * m.b6 <= 79.1787285426132)
m.e47 = Constraint(expr= (5.05196451835929 - m.x151)**2 + (9.78029757859562 -
    m.x154)**2 + 117.525315958044 * m.b7 <= 118.525315958044)
m.e48 = Constraint(expr= (4.91358831690657 - m.x151)**2 + (9.95200766490468 -
    m.x154)**2 + 120.184782975767 * m.b8 <= 121.184782975767)
m.e49 = Constraint(expr= (1.82270973029123 - m.x151)**2 + (3.08924661212034 -
    m.x154)**2 + 100.562560044535 * m.b9 <= 101.562560044535)
m.e50 = Constraint(expr= (8.90416070287928 - m.x151)**2 + (8.76903198117563 -
    m.x154)**2 + 140.241701004457 * m.b10 <= 141.241701004457)
m.e51 = Constraint(expr= (9.55691722438547 - m.x151)**2 + (7.67982230145412 -
    m.x154)**2 + 131.965894836477 * m.b11 <= 132.965894836477)
m.e52 = Constraint(expr= (5.63154215917614 - m.x151)**2 + (5.19669129629487 -
    m.x154)**2 + 61.1865070415458 * m.b12 <= 62.1865070415458)
m.e53 = Constraint(expr= (1.22506785607057 - m.x151)**2 + (1.73643838760701 -
    m.x154)**2 + 129.251385415199 * m.b13 <= 130.251385415199)
m.e54 = Constraint(expr= (3.56742024375224 - m.x151)**2 + (9.67716416398758 -
    m.x154)**2 + 122.549628719203 * m.b14 <= 123.549628719203)
m.e55 = Constraint(expr= (6.4469689992634 - m.x151)**2 + (3.27001587839258 -
    m.x154)**2 + 94.7662927771576 * m.b15 <= 95.7662927771576)
m.e56 = Constraint(expr= (6.10753237542196 - m.x151)**2 + (4.19206922588061 -
    m.x154)**2 + 78.2445398454346 * m.b16 <= 79.2445398454346)
m.e57 = Constraint(expr= (3.65877473332061 - m.x151)**2 + (3.63421268850839 -
    m.x154)**2 + 68.5611029512265 * m.b17 <= 69.5611029512265)
m.e58 = Constraint(expr= (1.2178860076098 - m.x151)**2 + (2.16125505734127 -
    m.x154)**2 + 123.013834343708 * m.b18 <= 124.013834343708)
m.e59 = Constraint(expr= (0.592074869235123 - m.x151)**2 + (4.93671199500253 -
    m.x154)**2 + 106.643311548917 * m.b19 <= 107.643311548917)
m.e60 = Constraint(expr= (6.7402850724876 - m.x151)**2 + (1.57064570718754 -
    m.x154)**2 + 125.533092608851 * m.b20 <= 126.533092608851)
m.e61 = Constraint(expr= (4.86197880938116 - m.x151)**2 + (0.383551455477691 -
    m.x154)**2 + 125.003682175941 * m.b21 <= 126.003682175941)
m.e62 = Constraint(expr= (1.8799102211015 - m.x151)**2 + (8.11097800063776 -
    m.x154)**2 + 111.618317672146 * m.b22 <= 112.618317672146)
m.e63 = Constraint(expr= (7.64684982583741 - m.x151)**2 + (0.420960467093494 -
    m.x154)**2 + 160.611756853376 * m.b23 <= 161.611756853376)
m.e64 = Constraint(expr= (3.86587305838289 - m.x151)**2 + (3.43289089140431 -
    m.x154)**2 + 68.5364474973792 * m.b24 <= 69.5364474973792)
m.e65 = Constraint(expr= (1.93085934314818 - m.x151)**2 + (3.48739999687651 -
    m.x154)**2 + 94.0180040498471 * m.b25 <= 95.0180040498471)
m.e66 = Constraint(expr= (8.14411066658926 - m.x151)**2 + (3.28390698782521 -
    m.x154)**2 + 120.943028096043 * m.b26 <= 121.943028096043)
m.e67 = Constraint(expr= (3.92781648828775 - m.x151)**2 + (4.5879692218008 -
    m.x154)**2 + 55.2445625258556 * m.b27 <= 56.2445625258556)
m.e68 = Constraint(expr= (9.43530528332928 - m.x151)**2 + (6.2115811426888 -
    m.x154)**2 + 114.385124970594 * m.b28 <= 115.385124970594)
m.e69 = Constraint(expr= (5.94277300911337 - m.x151)**2 + (2.72126258813597 -
    m.x154)**2 + 96.0912915355006 * m.b29 <= 97.0912915355006)
m.e70 = Constraint(expr= (0.272938801260022 - m.x151)**2 + (9.52106324081905 -
    m.x154)**2 + 160.611756853376 * m.b30 <= 161.611756853376)
m.e71 = Constraint(expr= m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8
    + m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17 +
    m.b18 + m.b19 + m.b20 + m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 +
    m.b27 + m.b28 + m.b29 + m.b30 == 1)
m.e72 = Constraint(expr= (3.58392835071893 - m.x152)**2 + (0.44370753979378 -
    m.x155)**2 + 117.37605108924 * m.b31 <= 118.37605108924)
m.e73 = Constraint(expr= (1.95628884344 - m.x152)**2 + (0.390503036650278 -
    m.x155)**2 + 140.241701004457 * m.b32 <= 141.241701004457)
m.e74 = Constraint(expr= (4.55035690490668 - m.x152)**2 + (7.27185840240323 -
    m.x155)**2 + 71.5594363053072 * m.b33 <= 72.5594363053072)
m.e75 = Constraint(expr= (6.2100872388646 - m.x152)**2 + (6.48745936675473 -
    m.x155)**2 + 70.1361240423208 * m.b34 <= 71.1361240423208)
m.e76 = Constraint(expr= (3.1786343207553 - m.x152)**2 + (2.35630065859291 -
    m.x155)**2 + 91.0983527000505 * m.b35 <= 92.0983527000505)
m.e77 = Constraint(expr= (2.77208272832737 - m.x152)**2 + (6.63537019621518 -
    m.x155)**2 + 78.1787285426132 * m.b36 <= 79.1787285426132)
m.e78 = Constraint(expr= (5.05196451835929 - m.x152)**2 + (9.78029757859562 -
    m.x155)**2 + 117.525315958044 * m.b37 <= 118.525315958044)
m.e79 = Constraint(expr= (4.91358831690657 - m.x152)**2 + (9.95200766490468 -
    m.x155)**2 + 120.184782975767 * m.b38 <= 121.184782975767)
m.e80 = Constraint(expr= (1.82270973029123 - m.x152)**2 + (3.08924661212034 -
    m.x155)**2 + 100.562560044535 * m.b39 <= 101.562560044535)
m.e81 = Constraint(expr= (8.90416070287928 - m.x152)**2 + (8.76903198117563 -
    m.x155)**2 + 140.241701004457 * m.b40 <= 141.241701004457)
m.e82 = Constraint(expr= (9.55691722438547 - m.x152)**2 + (7.67982230145412 -
    m.x155)**2 + 131.965894836477 * m.b41 <= 132.965894836477)
m.e83 = Constraint(expr= (5.63154215917614 - m.x152)**2 + (5.19669129629487 -
    m.x155)**2 + 61.1865070415458 * m.b42 <= 62.1865070415458)
m.e84 = Constraint(expr= (1.22506785607057 - m.x152)**2 + (1.73643838760701 -
    m.x155)**2 + 129.251385415199 * m.b43 <= 130.251385415199)
m.e85 = Constraint(expr= (3.56742024375224 - m.x152)**2 + (9.67716416398758 -
    m.x155)**2 + 122.549628719203 * m.b44 <= 123.549628719203)
m.e86 = Constraint(expr= (6.4469689992634 - m.x152)**2 + (3.27001587839258 -
    m.x155)**2 + 94.7662927771576 * m.b45 <= 95.7662927771576)
m.e87 = Constraint(expr= (6.10753237542196 - m.x152)**2 + (4.19206922588061 -
    m.x155)**2 + 78.2445398454346 * m.b46 <= 79.2445398454346)
m.e88 = Constraint(expr= (3.65877473332061 - m.x152)**2 + (3.63421268850839 -
    m.x155)**2 + 68.5611029512265 * m.b47 <= 69.5611029512265)
m.e89 = Constraint(expr= (1.2178860076098 - m.x152)**2 + (2.16125505734127 -
    m.x155)**2 + 123.013834343708 * m.b48 <= 124.013834343708)
m.e90 = Constraint(expr= (0.592074869235123 - m.x152)**2 + (4.93671199500253 -
    m.x155)**2 + 106.643311548917 * m.b49 <= 107.643311548917)
m.e91 = Constraint(expr= (6.7402850724876 - m.x152)**2 + (1.57064570718754 -
    m.x155)**2 + 125.533092608851 * m.b50 <= 126.533092608851)
m.e92 = Constraint(expr= (4.86197880938116 - m.x152)**2 + (0.383551455477691 -
    m.x155)**2 + 125.003682175941 * m.b51 <= 126.003682175941)
m.e93 = Constraint(expr= (1.8799102211015 - m.x152)**2 + (8.11097800063776 -
    m.x155)**2 + 111.618317672146 * m.b52 <= 112.618317672146)
m.e94 = Constraint(expr= (7.64684982583741 - m.x152)**2 + (0.420960467093494 -
    m.x155)**2 + 160.611756853376 * m.b53 <= 161.611756853376)
m.e95 = Constraint(expr= (3.86587305838289 - m.x152)**2 + (3.43289089140431 -
    m.x155)**2 + 68.5364474973792 * m.b54 <= 69.5364474973792)
m.e96 = Constraint(expr= (1.93085934314818 - m.x152)**2 + (3.48739999687651 -
    m.x155)**2 + 94.0180040498471 * m.b55 <= 95.0180040498471)
m.e97 = Constraint(expr= (8.14411066658926 - m.x152)**2 + (3.28390698782521 -
    m.x155)**2 + 120.943028096043 * m.b56 <= 121.943028096043)
m.e98 = Constraint(expr= (3.92781648828775 - m.x152)**2 + (4.5879692218008 -
    m.x155)**2 + 55.2445625258556 * m.b57 <= 56.2445625258556)
m.e99 = Constraint(expr= (9.43530528332928 - m.x152)**2 + (6.2115811426888 -
    m.x155)**2 + 114.385124970594 * m.b58 <= 115.385124970594)
m.e100 = Constraint(expr= (5.94277300911337 - m.x152)**2 + (2.72126258813597 -
    m.x155)**2 + 96.0912915355006 * m.b59 <= 97.0912915355006)
m.e101 = Constraint(expr= (0.272938801260022 - m.x152)**2 + (9.52106324081905
    - m.x155)**2 + 160.611756853376 * m.b60 <= 161.611756853376)
m.e102 = Constraint(expr= m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 + m.b37
    + m.b38 + m.b39 + m.b40 + m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 +
    m.b47 + m.b48 + m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 +
    m.b56 + m.b57 + m.b58 + m.b59 + m.b60 == 1)
m.e103 = Constraint(expr= (3.58392835071893 - m.x157)**2 + (0.44370753979378 -
    m.x159)**2 + 117.37605108924 * m.b61 <= 118.37605108924)
m.e104 = Constraint(expr= (1.95628884344 - m.x157)**2 + (0.390503036650278 -
    m.x159)**2 + 140.241701004457 * m.b62 <= 141.241701004457)
m.e105 = Constraint(expr= (4.55035690490668 - m.x157)**2 + (7.27185840240323 -
    m.x159)**2 + 71.5594363053072 * m.b63 <= 72.5594363053072)
m.e106 = Constraint(expr= (6.2100872388646 - m.x157)**2 + (6.48745936675473 -
    m.x159)**2 + 70.1361240423208 * m.b64 <= 71.1361240423208)
m.e107 = Constraint(expr= (3.1786343207553 - m.x157)**2 + (2.35630065859291 -
    m.x159)**2 + 91.0983527000505 * m.b65 <= 92.0983527000505)
m.e108 = Constraint(expr= (2.77208272832737 - m.x157)**2 + (6.63537019621518 -
    m.x159)**2 + 78.1787285426132 * m.b66 <= 79.1787285426132)
m.e109 = Constraint(expr= (5.05196451835929 - m.x157)**2 + (9.78029757859562 -
    m.x159)**2 + 117.525315958044 * m.b67 <= 118.525315958044)
m.e110 = Constraint(expr= (4.91358831690657 - m.x157)**2 + (9.95200766490468 -
    m.x159)**2 + 120.184782975767 * m.b68 <= 121.184782975767)
m.e111 = Constraint(expr= (1.82270973029123 - m.x157)**2 + (3.08924661212034 -
    m.x159)**2 + 100.562560044535 * m.b69 <= 101.562560044535)
m.e112 = Constraint(expr= (8.90416070287928 - m.x157)**2 + (8.76903198117563 -
    m.x159)**2 + 140.241701004457 * m.b70 <= 141.241701004457)
m.e113 = Constraint(expr= (9.55691722438547 - m.x157)**2 + (7.67982230145412 -
    m.x159)**2 + 131.965894836477 * m.b71 <= 132.965894836477)
m.e114 = Constraint(expr= (5.63154215917614 - m.x157)**2 + (5.19669129629487 -
    m.x159)**2 + 61.1865070415458 * m.b72 <= 62.1865070415458)
m.e115 = Constraint(expr= (1.22506785607057 - m.x157)**2 + (1.73643838760701 -
    m.x159)**2 + 129.251385415199 * m.b73 <= 130.251385415199)
m.e116 = Constraint(expr= (3.56742024375224 - m.x157)**2 + (9.67716416398758 -
    m.x159)**2 + 122.549628719203 * m.b74 <= 123.549628719203)
m.e117 = Constraint(expr= (6.4469689992634 - m.x157)**2 + (3.27001587839258 -
    m.x159)**2 + 94.7662927771576 * m.b75 <= 95.7662927771576)
m.e118 = Constraint(expr= (6.10753237542196 - m.x157)**2 + (4.19206922588061 -
    m.x159)**2 + 78.2445398454346 * m.b76 <= 79.2445398454346)
m.e119 = Constraint(expr= (3.65877473332061 - m.x157)**2 + (3.63421268850839 -
    m.x159)**2 + 68.5611029512265 * m.b77 <= 69.5611029512265)
m.e120 = Constraint(expr= (1.2178860076098 - m.x157)**2 + (2.16125505734127 -
    m.x159)**2 + 123.013834343708 * m.b78 <= 124.013834343708)
m.e121 = Constraint(expr= (0.592074869235123 - m.x157)**2 + (4.93671199500253
    - m.x159)**2 + 106.643311548917 * m.b79 <= 107.643311548917)
m.e122 = Constraint(expr= (6.7402850724876 - m.x157)**2 + (1.57064570718754 -
    m.x159)**2 + 125.533092608851 * m.b80 <= 126.533092608851)
m.e123 = Constraint(expr= (4.86197880938116 - m.x157)**2 + (0.383551455477691
    - m.x159)**2 + 125.003682175941 * m.b81 <= 126.003682175941)
m.e124 = Constraint(expr= (1.8799102211015 - m.x157)**2 + (8.11097800063776 -
    m.x159)**2 + 111.618317672146 * m.b82 <= 112.618317672146)
m.e125 = Constraint(expr= (7.64684982583741 - m.x157)**2 + (0.420960467093494
    - m.x159)**2 + 160.611756853376 * m.b83 <= 161.611756853376)
m.e126 = Constraint(expr= (3.86587305838289 - m.x157)**2 + (3.43289089140431 -
    m.x159)**2 + 68.5364474973792 * m.b84 <= 69.5364474973792)
m.e127 = Constraint(expr= (1.93085934314818 - m.x157)**2 + (3.48739999687651 -
    m.x159)**2 + 94.0180040498471 * m.b85 <= 95.0180040498471)
m.e128 = Constraint(expr= (8.14411066658926 - m.x157)**2 + (3.28390698782521 -
    m.x159)**2 + 120.943028096043 * m.b86 <= 121.943028096043)
m.e129 = Constraint(expr= (3.92781648828775 - m.x157)**2 + (4.5879692218008 -
    m.x159)**2 + 55.2445625258556 * m.b87 <= 56.2445625258556)
m.e130 = Constraint(expr= (9.43530528332928 - m.x157)**2 + (6.2115811426888 -
    m.x159)**2 + 114.385124970594 * m.b88 <= 115.385124970594)
m.e131 = Constraint(expr= (5.94277300911337 - m.x157)**2 + (2.72126258813597 -
    m.x159)**2 + 96.0912915355006 * m.b89 <= 97.0912915355006)
m.e132 = Constraint(expr= (0.272938801260022 - m.x157)**2 + (9.52106324081905
    - m.x159)**2 + 160.611756853376 * m.b90 <= 161.611756853376)
m.e133 = Constraint(expr= m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b66 + m.b67
    + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 + m.b73 + m.b74 + m.b75 + m.b76 +
    m.b77 + m.b78 + m.b79 + m.b80 + m.b81 + m.b82 + m.b83 + m.b84 + m.b85 +
    m.b86 + m.b87 + m.b88 + m.b89 + m.b90 == 1)
m.e134 = Constraint(expr= (3.58392835071893 - m.x161)**2 + (0.44370753979378 -
    m.x163)**2 + 117.37605108924 * m.b91 <= 118.37605108924)
m.e135 = Constraint(expr= (1.95628884344 - m.x161)**2 + (0.390503036650278 -
    m.x163)**2 + 140.241701004457 * m.b92 <= 141.241701004457)
m.e136 = Constraint(expr= (4.55035690490668 - m.x161)**2 + (7.27185840240323 -
    m.x163)**2 + 71.5594363053072 * m.b93 <= 72.5594363053072)
m.e137 = Constraint(expr= (6.2100872388646 - m.x161)**2 + (6.48745936675473 -
    m.x163)**2 + 70.1361240423208 * m.b94 <= 71.1361240423208)
m.e138 = Constraint(expr= (3.1786343207553 - m.x161)**2 + (2.35630065859291 -
    m.x163)**2 + 91.0983527000505 * m.b95 <= 92.0983527000505)
m.e139 = Constraint(expr= (2.77208272832737 - m.x161)**2 + (6.63537019621518 -
    m.x163)**2 + 78.1787285426132 * m.b96 <= 79.1787285426132)
m.e140 = Constraint(expr= (5.05196451835929 - m.x161)**2 + (9.78029757859562 -
    m.x163)**2 + 117.525315958044 * m.b97 <= 118.525315958044)
m.e141 = Constraint(expr= (4.91358831690657 - m.x161)**2 + (9.95200766490468 -
    m.x163)**2 + 120.184782975767 * m.b98 <= 121.184782975767)
m.e142 = Constraint(expr= (1.82270973029123 - m.x161)**2 + (3.08924661212034 -
    m.x163)**2 + 100.562560044535 * m.b99 <= 101.562560044535)
m.e143 = Constraint(expr= (8.90416070287928 - m.x161)**2 + (8.76903198117563 -
    m.x163)**2 + 140.241701004457 * m.b100 <= 141.241701004457)
m.e144 = Constraint(expr= (9.55691722438547 - m.x161)**2 + (7.67982230145412 -
    m.x163)**2 + 131.965894836477 * m.b101 <= 132.965894836477)
m.e145 = Constraint(expr= (5.63154215917614 - m.x161)**2 + (5.19669129629487 -
    m.x163)**2 + 61.1865070415458 * m.b102 <= 62.1865070415458)
m.e146 = Constraint(expr= (1.22506785607057 - m.x161)**2 + (1.73643838760701 -
    m.x163)**2 + 129.251385415199 * m.b103 <= 130.251385415199)
m.e147 = Constraint(expr= (3.56742024375224 - m.x161)**2 + (9.67716416398758 -
    m.x163)**2 + 122.549628719203 * m.b104 <= 123.549628719203)
m.e148 = Constraint(expr= (6.4469689992634 - m.x161)**2 + (3.27001587839258 -
    m.x163)**2 + 94.7662927771576 * m.b105 <= 95.7662927771576)
m.e149 = Constraint(expr= (6.10753237542196 - m.x161)**2 + (4.19206922588061 -
    m.x163)**2 + 78.2445398454346 * m.b106 <= 79.2445398454346)
m.e150 = Constraint(expr= (3.65877473332061 - m.x161)**2 + (3.63421268850839 -
    m.x163)**2 + 68.5611029512265 * m.b107 <= 69.5611029512265)
m.e151 = Constraint(expr= (1.2178860076098 - m.x161)**2 + (2.16125505734127 -
    m.x163)**2 + 123.013834343708 * m.b108 <= 124.013834343708)
m.e152 = Constraint(expr= (0.592074869235123 - m.x161)**2 + (4.93671199500253
    - m.x163)**2 + 106.643311548917 * m.b109 <= 107.643311548917)
m.e153 = Constraint(expr= (6.7402850724876 - m.x161)**2 + (1.57064570718754 -
    m.x163)**2 + 125.533092608851 * m.b110 <= 126.533092608851)
m.e154 = Constraint(expr= (4.86197880938116 - m.x161)**2 + (0.383551455477691
    - m.x163)**2 + 125.003682175941 * m.b111 <= 126.003682175941)
m.e155 = Constraint(expr= (1.8799102211015 - m.x161)**2 + (8.11097800063776 -
    m.x163)**2 + 111.618317672146 * m.b112 <= 112.618317672146)
m.e156 = Constraint(expr= (7.64684982583741 - m.x161)**2 + (0.420960467093494
    - m.x163)**2 + 160.611756853376 * m.b113 <= 161.611756853376)
m.e157 = Constraint(expr= (3.86587305838289 - m.x161)**2 + (3.43289089140431 -
    m.x163)**2 + 68.5364474973792 * m.b114 <= 69.5364474973792)
m.e158 = Constraint(expr= (1.93085934314818 - m.x161)**2 + (3.48739999687651 -
    m.x163)**2 + 94.0180040498471 * m.b115 <= 95.0180040498471)
m.e159 = Constraint(expr= (8.14411066658926 - m.x161)**2 + (3.28390698782521 -
    m.x163)**2 + 120.943028096043 * m.b116 <= 121.943028096043)
m.e160 = Constraint(expr= (3.92781648828775 - m.x161)**2 + (4.5879692218008 -
    m.x163)**2 + 55.2445625258556 * m.b117 <= 56.2445625258556)
m.e161 = Constraint(expr= (9.43530528332928 - m.x161)**2 + (6.2115811426888 -
    m.x163)**2 + 114.385124970594 * m.b118 <= 115.385124970594)
m.e162 = Constraint(expr= (5.94277300911337 - m.x161)**2 + (2.72126258813597 -
    m.x163)**2 + 96.0912915355006 * m.b119 <= 97.0912915355006)
m.e163 = Constraint(expr= (0.272938801260022 - m.x161)**2 + (9.52106324081905
    - m.x163)**2 + 160.611756853376 * m.b120 <= 161.611756853376)
m.e164 = Constraint(expr= m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b96 + m.b97
    + m.b98 + m.b99 + m.b100 + m.b101 + m.b102 + m.b103 + m.b104 + m.b105 +
    m.b106 + m.b107 + m.b108 + m.b109 + m.b110 + m.b111 + m.b112 + m.b113 +
    m.b114 + m.b115 + m.b116 + m.b117 + m.b118 + m.b119 + m.b120 == 1)
m.e165 = Constraint(expr= (3.58392835071893 - m.x165)**2 + (0.44370753979378 -
    m.x167)**2 + 117.37605108924 * m.b121 <= 118.37605108924)
m.e166 = Constraint(expr= (1.95628884344 - m.x165)**2 + (0.390503036650278 -
    m.x167)**2 + 140.241701004457 * m.b122 <= 141.241701004457)
m.e167 = Constraint(expr= (4.55035690490668 - m.x165)**2 + (7.27185840240323 -
    m.x167)**2 + 71.5594363053072 * m.b123 <= 72.5594363053072)
m.e168 = Constraint(expr= (6.2100872388646 - m.x165)**2 + (6.48745936675473 -
    m.x167)**2 + 70.1361240423208 * m.b124 <= 71.1361240423208)
m.e169 = Constraint(expr= (3.1786343207553 - m.x165)**2 + (2.35630065859291 -
    m.x167)**2 + 91.0983527000505 * m.b125 <= 92.0983527000505)
m.e170 = Constraint(expr= (2.77208272832737 - m.x165)**2 + (6.63537019621518 -
    m.x167)**2 + 78.1787285426132 * m.b126 <= 79.1787285426132)
m.e171 = Constraint(expr= (5.05196451835929 - m.x165)**2 + (9.78029757859562 -
    m.x167)**2 + 117.525315958044 * m.b127 <= 118.525315958044)
m.e172 = Constraint(expr= (4.91358831690657 - m.x165)**2 + (9.95200766490468 -
    m.x167)**2 + 120.184782975767 * m.b128 <= 121.184782975767)
m.e173 = Constraint(expr= (1.82270973029123 - m.x165)**2 + (3.08924661212034 -
    m.x167)**2 + 100.562560044535 * m.b129 <= 101.562560044535)
m.e174 = Constraint(expr= (8.90416070287928 - m.x165)**2 + (8.76903198117563 -
    m.x167)**2 + 140.241701004457 * m.b130 <= 141.241701004457)
m.e175 = Constraint(expr= (9.55691722438547 - m.x165)**2 + (7.67982230145412 -
    m.x167)**2 + 131.965894836477 * m.b131 <= 132.965894836477)
m.e176 = Constraint(expr= (5.63154215917614 - m.x165)**2 + (5.19669129629487 -
    m.x167)**2 + 61.1865070415458 * m.b132 <= 62.1865070415458)
m.e177 = Constraint(expr= (1.22506785607057 - m.x165)**2 + (1.73643838760701 -
    m.x167)**2 + 129.251385415199 * m.b133 <= 130.251385415199)
m.e178 = Constraint(expr= (3.56742024375224 - m.x165)**2 + (9.67716416398758 -
    m.x167)**2 + 122.549628719203 * m.b134 <= 123.549628719203)
m.e179 = Constraint(expr= (6.4469689992634 - m.x165)**2 + (3.27001587839258 -
    m.x167)**2 + 94.7662927771576 * m.b135 <= 95.7662927771576)
m.e180 = Constraint(expr= (6.10753237542196 - m.x165)**2 + (4.19206922588061 -
    m.x167)**2 + 78.2445398454346 * m.b136 <= 79.2445398454346)
m.e181 = Constraint(expr= (3.65877473332061 - m.x165)**2 + (3.63421268850839 -
    m.x167)**2 + 68.5611029512265 * m.b137 <= 69.5611029512265)
m.e182 = Constraint(expr= (1.2178860076098 - m.x165)**2 + (2.16125505734127 -
    m.x167)**2 + 123.013834343708 * m.b138 <= 124.013834343708)
m.e183 = Constraint(expr= (0.592074869235123 - m.x165)**2 + (4.93671199500253
    - m.x167)**2 + 106.643311548917 * m.b139 <= 107.643311548917)
m.e184 = Constraint(expr= (6.7402850724876 - m.x165)**2 + (1.57064570718754 -
    m.x167)**2 + 125.533092608851 * m.b140 <= 126.533092608851)
m.e185 = Constraint(expr= (4.86197880938116 - m.x165)**2 + (0.383551455477691
    - m.x167)**2 + 125.003682175941 * m.b141 <= 126.003682175941)
m.e186 = Constraint(expr= (1.8799102211015 - m.x165)**2 + (8.11097800063776 -
    m.x167)**2 + 111.618317672146 * m.b142 <= 112.618317672146)
m.e187 = Constraint(expr= (7.64684982583741 - m.x165)**2 + (0.420960467093494
    - m.x167)**2 + 160.611756853376 * m.b143 <= 161.611756853376)
m.e188 = Constraint(expr= (3.86587305838289 - m.x165)**2 + (3.43289089140431 -
    m.x167)**2 + 68.5364474973792 * m.b144 <= 69.5364474973792)
m.e189 = Constraint(expr= (1.93085934314818 - m.x165)**2 + (3.48739999687651 -
    m.x167)**2 + 94.0180040498471 * m.b145 <= 95.0180040498471)
m.e190 = Constraint(expr= (8.14411066658926 - m.x165)**2 + (3.28390698782521 -
    m.x167)**2 + 120.943028096043 * m.b146 <= 121.943028096043)
m.e191 = Constraint(expr= (3.92781648828775 - m.x165)**2 + (4.5879692218008 -
    m.x167)**2 + 55.2445625258556 * m.b147 <= 56.2445625258556)
m.e192 = Constraint(expr= (9.43530528332928 - m.x165)**2 + (6.2115811426888 -
    m.x167)**2 + 114.385124970594 * m.b148 <= 115.385124970594)
m.e193 = Constraint(expr= (5.94277300911337 - m.x165)**2 + (2.72126258813597 -
    m.x167)**2 + 96.0912915355006 * m.b149 <= 97.0912915355006)
m.e194 = Constraint(expr= (0.272938801260022 - m.x165)**2 + (9.52106324081905
    - m.x167)**2 + 160.611756853376 * m.b150 <= 161.611756853376)
m.e195 = Constraint(expr= m.b121 + m.b122 + m.b123 + m.b124 + m.b125 + m.b126
    + m.b127 + m.b128 + m.b129 + m.b130 + m.b131 + m.b132 + m.b133 + m.b134 +
    m.b135 + m.b136 + m.b137 + m.b138 + m.b139 + m.b140 + m.b141 + m.b142 +
    m.b143 + m.b144 + m.b145 + m.b146 + m.b147 + m.b148 + m.b149 + m.b150 == 1)
m.e196 = Constraint(expr= m.b1 + m.b31 + m.b61 + m.b91 + m.b121 <= 1)
m.e197 = Constraint(expr= m.b2 + m.b32 + m.b62 + m.b92 + m.b122 <= 1)
m.e198 = Constraint(expr= m.b3 + m.b33 + m.b63 + m.b93 + m.b123 <= 1)
m.e199 = Constraint(expr= m.b4 + m.b34 + m.b64 + m.b94 + m.b124 <= 1)
m.e200 = Constraint(expr= m.b5 + m.b35 + m.b65 + m.b95 + m.b125 <= 1)
m.e201 = Constraint(expr= m.b6 + m.b36 + m.b66 + m.b96 + m.b126 <= 1)
m.e202 = Constraint(expr= m.b7 + m.b37 + m.b67 + m.b97 + m.b127 <= 1)
m.e203 = Constraint(expr= m.b8 + m.b38 + m.b68 + m.b98 + m.b128 <= 1)
m.e204 = Constraint(expr= m.b9 + m.b39 + m.b69 + m.b99 + m.b129 <= 1)
m.e205 = Constraint(expr= m.b10 + m.b40 + m.b70 + m.b100 + m.b130 <= 1)
m.e206 = Constraint(expr= m.b11 + m.b41 + m.b71 + m.b101 + m.b131 <= 1)
m.e207 = Constraint(expr= m.b12 + m.b42 + m.b72 + m.b102 + m.b132 <= 1)
m.e208 = Constraint(expr= m.b13 + m.b43 + m.b73 + m.b103 + m.b133 <= 1)
m.e209 = Constraint(expr= m.b14 + m.b44 + m.b74 + m.b104 + m.b134 <= 1)
m.e210 = Constraint(expr= m.b15 + m.b45 + m.b75 + m.b105 + m.b135 <= 1)
m.e211 = Constraint(expr= m.b16 + m.b46 + m.b76 + m.b106 + m.b136 <= 1)
m.e212 = Constraint(expr= m.b17 + m.b47 + m.b77 + m.b107 + m.b137 <= 1)
m.e213 = Constraint(expr= m.b18 + m.b48 + m.b78 + m.b108 + m.b138 <= 1)
m.e214 = Constraint(expr= m.b19 + m.b49 + m.b79 + m.b109 + m.b139 <= 1)
m.e215 = Constraint(expr= m.b20 + m.b50 + m.b80 + m.b110 + m.b140 <= 1)
m.e216 = Constraint(expr= m.b21 + m.b51 + m.b81 + m.b111 + m.b141 <= 1)
m.e217 = Constraint(expr= m.b22 + m.b52 + m.b82 + m.b112 + m.b142 <= 1)
m.e218 = Constraint(expr= m.b23 + m.b53 + m.b83 + m.b113 + m.b143 <= 1)
m.e219 = Constraint(expr= m.b24 + m.b54 + m.b84 + m.b114 + m.b144 <= 1)
m.e220 = Constraint(expr= m.b25 + m.b55 + m.b85 + m.b115 + m.b145 <= 1)
m.e221 = Constraint(expr= m.b26 + m.b56 + m.b86 + m.b116 + m.b146 <= 1)
m.e222 = Constraint(expr= m.b27 + m.b57 + m.b87 + m.b117 + m.b147 <= 1)
m.e223 = Constraint(expr= m.b28 + m.b58 + m.b88 + m.b118 + m.b148 <= 1)
m.e224 = Constraint(expr= m.b29 + m.b59 + m.b89 + m.b119 + m.b149 <= 1)
m.e225 = Constraint(expr= m.b30 + m.b60 + m.b90 + m.b120 + m.b150 <= 1)
m.e226 = Constraint(expr= m.x151 - m.x152 <= 0)
m.e227 = Constraint(expr= m.x152 - m.x157 <= 0)
m.e228 = Constraint(expr= m.x157 - m.x161 <= 0)
m.e229 = Constraint(expr= m.x161 - m.x165 <= 0)
