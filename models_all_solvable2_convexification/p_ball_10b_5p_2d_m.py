# MINLP written by GAMS Convert at 05/07/21 17:12:59
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       109        5        0      104        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#        80       30       50        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       378      278      100
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.b1 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b2 = Var(within=Binary, bounds=(0,1), initialize=1)
m.b3 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b4 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b5 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b6 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b7 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b8 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b9 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b10 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b11 = Var(within=Binary, bounds=(0,1), initialize=1)
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
m.b30 = Var(within=Binary, bounds=(0,1), initialize=1)
m.b31 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b32 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b33 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b34 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b35 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b36 = Var(within=Binary, bounds=(0,1), initialize=1)
m.b37 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b38 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b39 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b40 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b41 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b42 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b43 = Var(within=Binary, bounds=(0,1), initialize=1)
m.b44 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b45 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b46 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b47 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b48 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b49 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b50 = Var(within=Binary, bounds=(0,1), initialize=0)
m.x51 = Var(within=Reals, bounds=(0,10), initialize=1.37695009606239)
m.x52 = Var(within=Reals, bounds=(0,10), initialize=1.42378547420432)
m.x53 = Var(within=Reals, bounds=(0,10), initialize=0.0468353781419294)
m.x54 = Var(within=Reals, bounds=(0,10), initialize=4.71045051597106)
m.x55 = Var(within=Reals, bounds=(0,10), initialize=4.71045051597106)
m.x56 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x57 = Var(within=Reals, bounds=(0,10), initialize=1.91800199645783)
m.x58 = Var(within=Reals, bounds=(0,10), initialize=0.541051900395441)
m.x59 = Var(within=Reals, bounds=(0,10), initialize=4.71045051597106)
m.x60 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x61 = Var(within=Reals, bounds=(0,10), initialize=3.61191140798068)
m.x62 = Var(within=Reals, bounds=(0,10), initialize=2.23496131191829)
m.x63 = Var(within=Reals, bounds=(0,10), initialize=4.71045051597106)
m.x64 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x65 = Var(within=Reals, bounds=(0,10), initialize=3.89283484794216)
m.x66 = Var(within=Reals, bounds=(0,10), initialize=2.51588475187977)
m.x67 = Var(within=Reals, bounds=(0,10), initialize=3.64078525445372)
m.x68 = Var(within=Reals, bounds=(0,10), initialize=1.06966526151734)
m.x69 = Var(within=Reals, bounds=(0,10), initialize=0.494216522253511)
m.x70 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x71 = Var(within=Reals, bounds=(0,10), initialize=2.18812593377636)
m.x72 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x73 = Var(within=Reals, bounds=(0,10), initialize=2.46904937373784)
m.x74 = Var(within=Reals, bounds=(0,10), initialize=1.06966526151734)
m.x75 = Var(within=Reals, bounds=(0,10), initialize=1.69390941152285)
m.x76 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x77 = Var(within=Reals, bounds=(0,10), initialize=1.97483285148432)
m.x78 = Var(within=Reals, bounds=(0,10), initialize=1.06966526151734)
m.x79 = Var(within=Reals, bounds=(0,10), initialize=0.280923439961476)
m.x80 = Var(within=Reals, bounds=(0,10), initialize=1.06966526151734)

m.obj = Objective(sense=minimize, expr= m.x53 + m.x56 + m.x58 + m.x60 + m.x62
    + m.x64 + m.x66 + m.x68 + m.x69 + m.x70 + m.x71 + m.x72 + m.x73 + m.x74 +
    m.x75 + m.x76 + m.x77 + m.x78 + m.x79 + m.x80)

m.e1 = Constraint(expr= m.x51 - m.x52 - m.x53 <= 0)
m.e2 = Constraint(expr= -m.x51 + m.x52 - m.x53 <= 0)
m.e3 = Constraint(expr= m.x54 - m.x55 - m.x56 <= 0)
m.e4 = Constraint(expr= -m.x54 + m.x55 - m.x56 <= 0)
m.e5 = Constraint(expr= m.x51 - m.x57 - m.x58 <= 0)
m.e6 = Constraint(expr= -m.x51 + m.x57 - m.x58 <= 0)
m.e7 = Constraint(expr= m.x54 - m.x59 - m.x60 <= 0)
m.e8 = Constraint(expr= -m.x54 + m.x59 - m.x60 <= 0)
m.e9 = Constraint(expr= m.x51 - m.x61 - m.x62 <= 0)
m.e10 = Constraint(expr= -m.x51 + m.x61 - m.x62 <= 0)
m.e11 = Constraint(expr= m.x54 - m.x63 - m.x64 <= 0)
m.e12 = Constraint(expr= -m.x54 + m.x63 - m.x64 <= 0)
m.e13 = Constraint(expr= m.x51 - m.x65 - m.x66 <= 0)
m.e14 = Constraint(expr= -m.x51 + m.x65 - m.x66 <= 0)
m.e15 = Constraint(expr= m.x54 - m.x67 - m.x68 <= 0)
m.e16 = Constraint(expr= -m.x54 + m.x67 - m.x68 <= 0)
m.e17 = Constraint(expr= m.x52 - m.x57 - m.x69 <= 0)
m.e18 = Constraint(expr= -m.x52 + m.x57 - m.x69 <= 0)
m.e19 = Constraint(expr= m.x55 - m.x59 - m.x70 <= 0)
m.e20 = Constraint(expr= -m.x55 + m.x59 - m.x70 <= 0)
m.e21 = Constraint(expr= m.x52 - m.x61 - m.x71 <= 0)
m.e22 = Constraint(expr= -m.x52 + m.x61 - m.x71 <= 0)
m.e23 = Constraint(expr= m.x55 - m.x63 - m.x72 <= 0)
m.e24 = Constraint(expr= -m.x55 + m.x63 - m.x72 <= 0)
m.e25 = Constraint(expr= m.x52 - m.x65 - m.x73 <= 0)
m.e26 = Constraint(expr= -m.x52 + m.x65 - m.x73 <= 0)
m.e27 = Constraint(expr= m.x55 - m.x67 - m.x74 <= 0)
m.e28 = Constraint(expr= -m.x55 + m.x67 - m.x74 <= 0)
m.e29 = Constraint(expr= m.x57 - m.x61 - m.x75 <= 0)
m.e30 = Constraint(expr= -m.x57 + m.x61 - m.x75 <= 0)
m.e31 = Constraint(expr= m.x59 - m.x63 - m.x76 <= 0)
m.e32 = Constraint(expr= -m.x59 + m.x63 - m.x76 <= 0)
m.e33 = Constraint(expr= m.x57 - m.x65 - m.x77 <= 0)
m.e34 = Constraint(expr= -m.x57 + m.x65 - m.x77 <= 0)
m.e35 = Constraint(expr= m.x59 - m.x67 - m.x78 <= 0)
m.e36 = Constraint(expr= -m.x59 + m.x67 - m.x78 <= 0)
m.e37 = Constraint(expr= m.x61 - m.x65 - m.x79 <= 0)
m.e38 = Constraint(expr= -m.x61 + m.x65 - m.x79 <= 0)
m.e39 = Constraint(expr= m.x63 - m.x67 - m.x80 <= 0)
m.e40 = Constraint(expr= -m.x63 + m.x67 - m.x80 <= 0)
m.e41 = Constraint(expr= (0.648386267690458 - m.x51)**2 + (5.34198386756466 -
    m.x54)**2 + 109.233018040634 * m.b1 <= 110.233018040634)
m.e42 = Constraint(expr= (0.38028139143083 - m.x51)**2 + (4.79200736168083 -
    m.x54)**2 + 108.933937361066 * m.b2 <= 109.933937361066)
m.e43 = Constraint(expr= (4.59553989190787 - m.x51)**2 + (2.92927044373959 -
    m.x54)**2 + 54.6585416851302 * m.b3 <= 55.6585416851302)
m.e44 = Constraint(expr= (7.79089239319392 - m.x51)**2 + (3.09688601355012 -
    m.x54)**2 + 72.9946165089168 * m.b4 <= 73.9946165089168)
m.e45 = Constraint(expr= (2.20597420581599 - m.x51)**2 + (0.880296019425143 -
    m.x54)**2 + 103.212034038779 * m.b5 <= 104.212034038779)
m.e46 = Constraint(expr= (4.31093077060147 - m.x51)**2 + (5.42555328385657 -
    m.x54)**2 + 56.8881542099775 * m.b6 <= 57.8881542099775)
m.e47 = Constraint(expr= (8.68776252232421 - m.x51)**2 + (7.42106012944621 -
    m.x54)**2 + 103.212034038779 * m.b7 <= 104.212034038779)
m.e48 = Constraint(expr= (3.86794113528858 - m.x51)**2 + (9.34863265837716 -
    m.x54)**2 + 120.378073325993 * m.b8 <= 121.378073325993)
m.e49 = Constraint(expr= (8.94294324678777 - m.x51)**2 + (0.712193380632226 -
    m.x54)**2 + 120.378073325993 * m.b9 <= 121.378073325993)
m.e50 = Constraint(expr= (1.56734614217404 - m.x51)**2 + (5.6469805099144 -
    m.x54)**2 + 96.4999714251602 * m.b10 <= 97.4999714251602)
m.e51 = Constraint(expr= m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8
    + m.b9 + m.b10 == 1)
m.e52 = Constraint(expr= (0.648386267690458 - m.x52)**2 + (5.34198386756466 -
    m.x55)**2 + 109.233018040634 * m.b11 <= 110.233018040634)
m.e53 = Constraint(expr= (0.38028139143083 - m.x52)**2 + (4.79200736168083 -
    m.x55)**2 + 108.933937361066 * m.b12 <= 109.933937361066)
m.e54 = Constraint(expr= (4.59553989190787 - m.x52)**2 + (2.92927044373959 -
    m.x55)**2 + 54.6585416851302 * m.b13 <= 55.6585416851302)
m.e55 = Constraint(expr= (7.79089239319392 - m.x52)**2 + (3.09688601355012 -
    m.x55)**2 + 72.9946165089168 * m.b14 <= 73.9946165089168)
m.e56 = Constraint(expr= (2.20597420581599 - m.x52)**2 + (0.880296019425143 -
    m.x55)**2 + 103.212034038779 * m.b15 <= 104.212034038779)
m.e57 = Constraint(expr= (4.31093077060147 - m.x52)**2 + (5.42555328385657 -
    m.x55)**2 + 56.8881542099775 * m.b16 <= 57.8881542099775)
m.e58 = Constraint(expr= (8.68776252232421 - m.x52)**2 + (7.42106012944621 -
    m.x55)**2 + 103.212034038779 * m.b17 <= 104.212034038779)
m.e59 = Constraint(expr= (3.86794113528858 - m.x52)**2 + (9.34863265837716 -
    m.x55)**2 + 120.378073325993 * m.b18 <= 121.378073325993)
m.e60 = Constraint(expr= (8.94294324678777 - m.x52)**2 + (0.712193380632226 -
    m.x55)**2 + 120.378073325993 * m.b19 <= 121.378073325993)
m.e61 = Constraint(expr= (1.56734614217404 - m.x52)**2 + (5.6469805099144 -
    m.x55)**2 + 96.4999714251602 * m.b20 <= 97.4999714251602)
m.e62 = Constraint(expr= m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17
    + m.b18 + m.b19 + m.b20 == 1)
m.e63 = Constraint(expr= (0.648386267690458 - m.x57)**2 + (5.34198386756466 -
    m.x59)**2 + 109.233018040634 * m.b21 <= 110.233018040634)
m.e64 = Constraint(expr= (0.38028139143083 - m.x57)**2 + (4.79200736168083 -
    m.x59)**2 + 108.933937361066 * m.b22 <= 109.933937361066)
m.e65 = Constraint(expr= (4.59553989190787 - m.x57)**2 + (2.92927044373959 -
    m.x59)**2 + 54.6585416851302 * m.b23 <= 55.6585416851302)
m.e66 = Constraint(expr= (7.79089239319392 - m.x57)**2 + (3.09688601355012 -
    m.x59)**2 + 72.9946165089168 * m.b24 <= 73.9946165089168)
m.e67 = Constraint(expr= (2.20597420581599 - m.x57)**2 + (0.880296019425143 -
    m.x59)**2 + 103.212034038779 * m.b25 <= 104.212034038779)
m.e68 = Constraint(expr= (4.31093077060147 - m.x57)**2 + (5.42555328385657 -
    m.x59)**2 + 56.8881542099775 * m.b26 <= 57.8881542099775)
m.e69 = Constraint(expr= (8.68776252232421 - m.x57)**2 + (7.42106012944621 -
    m.x59)**2 + 103.212034038779 * m.b27 <= 104.212034038779)
m.e70 = Constraint(expr= (3.86794113528858 - m.x57)**2 + (9.34863265837716 -
    m.x59)**2 + 120.378073325993 * m.b28 <= 121.378073325993)
m.e71 = Constraint(expr= (8.94294324678777 - m.x57)**2 + (0.712193380632226 -
    m.x59)**2 + 120.378073325993 * m.b29 <= 121.378073325993)
m.e72 = Constraint(expr= (1.56734614217404 - m.x57)**2 + (5.6469805099144 -
    m.x59)**2 + 96.4999714251602 * m.b30 <= 97.4999714251602)
m.e73 = Constraint(expr= m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 + m.b27
    + m.b28 + m.b29 + m.b30 == 1)
m.e74 = Constraint(expr= (0.648386267690458 - m.x61)**2 + (5.34198386756466 -
    m.x63)**2 + 109.233018040634 * m.b31 <= 110.233018040634)
m.e75 = Constraint(expr= (0.38028139143083 - m.x61)**2 + (4.79200736168083 -
    m.x63)**2 + 108.933937361066 * m.b32 <= 109.933937361066)
m.e76 = Constraint(expr= (4.59553989190787 - m.x61)**2 + (2.92927044373959 -
    m.x63)**2 + 54.6585416851302 * m.b33 <= 55.6585416851302)
m.e77 = Constraint(expr= (7.79089239319392 - m.x61)**2 + (3.09688601355012 -
    m.x63)**2 + 72.9946165089168 * m.b34 <= 73.9946165089168)
m.e78 = Constraint(expr= (2.20597420581599 - m.x61)**2 + (0.880296019425143 -
    m.x63)**2 + 103.212034038779 * m.b35 <= 104.212034038779)
m.e79 = Constraint(expr= (4.31093077060147 - m.x61)**2 + (5.42555328385657 -
    m.x63)**2 + 56.8881542099775 * m.b36 <= 57.8881542099775)
m.e80 = Constraint(expr= (8.68776252232421 - m.x61)**2 + (7.42106012944621 -
    m.x63)**2 + 103.212034038779 * m.b37 <= 104.212034038779)
m.e81 = Constraint(expr= (3.86794113528858 - m.x61)**2 + (9.34863265837716 -
    m.x63)**2 + 120.378073325993 * m.b38 <= 121.378073325993)
m.e82 = Constraint(expr= (8.94294324678777 - m.x61)**2 + (0.712193380632226 -
    m.x63)**2 + 120.378073325993 * m.b39 <= 121.378073325993)
m.e83 = Constraint(expr= (1.56734614217404 - m.x61)**2 + (5.6469805099144 -
    m.x63)**2 + 96.4999714251602 * m.b40 <= 97.4999714251602)
m.e84 = Constraint(expr= m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 + m.b37
    + m.b38 + m.b39 + m.b40 == 1)
m.e85 = Constraint(expr= (0.648386267690458 - m.x65)**2 + (5.34198386756466 -
    m.x67)**2 + 109.233018040634 * m.b41 <= 110.233018040634)
m.e86 = Constraint(expr= (0.38028139143083 - m.x65)**2 + (4.79200736168083 -
    m.x67)**2 + 108.933937361066 * m.b42 <= 109.933937361066)
m.e87 = Constraint(expr= (4.59553989190787 - m.x65)**2 + (2.92927044373959 -
    m.x67)**2 + 54.6585416851302 * m.b43 <= 55.6585416851302)
m.e88 = Constraint(expr= (7.79089239319392 - m.x65)**2 + (3.09688601355012 -
    m.x67)**2 + 72.9946165089168 * m.b44 <= 73.9946165089168)
m.e89 = Constraint(expr= (2.20597420581599 - m.x65)**2 + (0.880296019425143 -
    m.x67)**2 + 103.212034038779 * m.b45 <= 104.212034038779)
m.e90 = Constraint(expr= (4.31093077060147 - m.x65)**2 + (5.42555328385657 -
    m.x67)**2 + 56.8881542099775 * m.b46 <= 57.8881542099775)
m.e91 = Constraint(expr= (8.68776252232421 - m.x65)**2 + (7.42106012944621 -
    m.x67)**2 + 103.212034038779 * m.b47 <= 104.212034038779)
m.e92 = Constraint(expr= (3.86794113528858 - m.x65)**2 + (9.34863265837716 -
    m.x67)**2 + 120.378073325993 * m.b48 <= 121.378073325993)
m.e93 = Constraint(expr= (8.94294324678777 - m.x65)**2 + (0.712193380632226 -
    m.x67)**2 + 120.378073325993 * m.b49 <= 121.378073325993)
m.e94 = Constraint(expr= (1.56734614217404 - m.x65)**2 + (5.6469805099144 -
    m.x67)**2 + 96.4999714251602 * m.b50 <= 97.4999714251602)
m.e95 = Constraint(expr= m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47
    + m.b48 + m.b49 + m.b50 == 1)
m.e96 = Constraint(expr= m.b1 + m.b11 + m.b21 + m.b31 + m.b41 <= 1)
m.e97 = Constraint(expr= m.b2 + m.b12 + m.b22 + m.b32 + m.b42 <= 1)
m.e98 = Constraint(expr= m.b3 + m.b13 + m.b23 + m.b33 + m.b43 <= 1)
m.e99 = Constraint(expr= m.b4 + m.b14 + m.b24 + m.b34 + m.b44 <= 1)
m.e100 = Constraint(expr= m.b5 + m.b15 + m.b25 + m.b35 + m.b45 <= 1)
m.e101 = Constraint(expr= m.b6 + m.b16 + m.b26 + m.b36 + m.b46 <= 1)
m.e102 = Constraint(expr= m.b7 + m.b17 + m.b27 + m.b37 + m.b47 <= 1)
m.e103 = Constraint(expr= m.b8 + m.b18 + m.b28 + m.b38 + m.b48 <= 1)
m.e104 = Constraint(expr= m.b9 + m.b19 + m.b29 + m.b39 + m.b49 <= 1)
m.e105 = Constraint(expr= m.b10 + m.b20 + m.b30 + m.b40 + m.b50 <= 1)
m.e106 = Constraint(expr= m.x51 - m.x52 <= 0)
m.e107 = Constraint(expr= m.x52 - m.x57 <= 0)
m.e108 = Constraint(expr= m.x57 - m.x61 <= 0)
m.e109 = Constraint(expr= m.x61 - m.x65 <= 0)
