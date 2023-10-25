# MINLP written by GAMS Convert at 05/07/21 17:13:00
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       139        5        0      134        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       105       30       75        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       503      353      150
#
# Reformulation has removed 1 variable and 1 equation

from pyomo.environ import *

model = m = ConcreteModel()

m.b1 = Var(within=Binary, bounds=(0,1), initialize=1)
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
m.b19 = Var(within=Binary, bounds=(0,1), initialize=1)
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
m.b42 = Var(within=Binary, bounds=(0,1), initialize=1)
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
m.b56 = Var(within=Binary, bounds=(0,1), initialize=1)
m.b57 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b58 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b59 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b60 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b61 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b62 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b63 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b64 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b65 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b66 = Var(within=Binary, bounds=(0,1), initialize=1)
m.b67 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b68 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b69 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b70 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b71 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b72 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b73 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b74 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b75 = Var(within=Binary, bounds=(0,1), initialize=0)
m.x76 = Var(within=Reals, bounds=(0,10), initialize=8.95906267878703)
m.x77 = Var(within=Reals, bounds=(0,10), initialize=8.95906267878703)
m.x78 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x79 = Var(within=Reals, bounds=(0,10), initialize=7.61846710348714)
m.x80 = Var(within=Reals, bounds=(0,10), initialize=7.02977358343362)
m.x81 = Var(within=Reals, bounds=(0,10), initialize=0.58869352005352)
m.x82 = Var(within=Reals, bounds=(0,10), initialize=8.95906267878703)
m.x83 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x84 = Var(within=Reals, bounds=(0,10), initialize=6.22238510231117)
m.x85 = Var(within=Reals, bounds=(0,10), initialize=1.39608200117597)
m.x86 = Var(within=Reals, bounds=(0,10), initialize=8.95906267878703)
m.x87 = Var(within=Reals, bounds=(0,10), initialize=1.11022302462516e-16)
m.x88 = Var(within=Reals, bounds=(0,10), initialize=6.52219222156143)
m.x89 = Var(within=Reals, bounds=(0,10), initialize=1.0962748819257)
m.x90 = Var(within=Reals, bounds=(0,10), initialize=8.95906267878703)
m.x91 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x92 = Var(within=Reals, bounds=(0,10), initialize=6.52219222156143)
m.x93 = Var(within=Reals, bounds=(0,10), initialize=1.0962748819257)
m.x94 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x95 = Var(within=Reals, bounds=(0,10), initialize=0.807388481122451)
m.x96 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x97 = Var(within=Reals, bounds=(0,10), initialize=0.507581361872184)
m.x98 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x99 = Var(within=Reals, bounds=(0,10), initialize=0.507581361872184)
m.x100 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x101 = Var(within=Reals, bounds=(0,10), initialize=0.299807119250266)
m.x102 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x103 = Var(within=Reals, bounds=(0,10), initialize=0.299807119250266)
m.x104 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x105 = Var(within=Reals, bounds=(0,10), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x78 + m.x81 + m.x83 + m.x85 + m.x87
    + m.x89 + m.x91 + m.x93 + m.x94 + m.x95 + m.x96 + m.x97 + m.x98 + m.x99 +
    m.x100 + m.x101 + m.x102 + m.x103 + m.x104 + m.x105)

m.e1 = Constraint(expr= m.x76 - m.x77 - m.x78 <= 0)
m.e2 = Constraint(expr= -m.x76 + m.x77 - m.x78 <= 0)
m.e3 = Constraint(expr= m.x79 - m.x80 - m.x81 <= 0)
m.e4 = Constraint(expr= -m.x79 + m.x80 - m.x81 <= 0)
m.e5 = Constraint(expr= m.x76 - m.x82 - m.x83 <= 0)
m.e6 = Constraint(expr= -m.x76 + m.x82 - m.x83 <= 0)
m.e7 = Constraint(expr= m.x79 - m.x84 - m.x85 <= 0)
m.e8 = Constraint(expr= -m.x79 + m.x84 - m.x85 <= 0)
m.e9 = Constraint(expr= m.x76 - m.x86 - m.x87 <= 0)
m.e10 = Constraint(expr= -m.x76 + m.x86 - m.x87 <= 0)
m.e11 = Constraint(expr= m.x79 - m.x88 - m.x89 <= 0)
m.e12 = Constraint(expr= -m.x79 + m.x88 - m.x89 <= 0)
m.e13 = Constraint(expr= m.x76 - m.x90 - m.x91 <= 0)
m.e14 = Constraint(expr= -m.x76 + m.x90 - m.x91 <= 0)
m.e15 = Constraint(expr= m.x79 - m.x92 - m.x93 <= 0)
m.e16 = Constraint(expr= -m.x79 + m.x92 - m.x93 <= 0)
m.e17 = Constraint(expr= m.x77 - m.x82 - m.x94 <= 0)
m.e18 = Constraint(expr= -m.x77 + m.x82 - m.x94 <= 0)
m.e19 = Constraint(expr= m.x80 - m.x84 - m.x95 <= 0)
m.e20 = Constraint(expr= -m.x80 + m.x84 - m.x95 <= 0)
m.e21 = Constraint(expr= m.x77 - m.x86 - m.x96 <= 0)
m.e22 = Constraint(expr= -m.x77 + m.x86 - m.x96 <= 0)
m.e23 = Constraint(expr= m.x80 - m.x88 - m.x97 <= 0)
m.e24 = Constraint(expr= -m.x80 + m.x88 - m.x97 <= 0)
m.e25 = Constraint(expr= m.x77 - m.x90 - m.x98 <= 0)
m.e26 = Constraint(expr= -m.x77 + m.x90 - m.x98 <= 0)
m.e27 = Constraint(expr= m.x80 - m.x92 - m.x99 <= 0)
m.e28 = Constraint(expr= -m.x80 + m.x92 - m.x99 <= 0)
m.e29 = Constraint(expr= m.x82 - m.x86 - m.x100 <= 0)
m.e30 = Constraint(expr= -m.x82 + m.x86 - m.x100 <= 0)
m.e31 = Constraint(expr= m.x84 - m.x88 - m.x101 <= 0)
m.e32 = Constraint(expr= -m.x84 + m.x88 - m.x101 <= 0)
m.e33 = Constraint(expr= m.x82 - m.x90 - m.x102 <= 0)
m.e34 = Constraint(expr= -m.x82 + m.x90 - m.x102 <= 0)
m.e35 = Constraint(expr= m.x84 - m.x92 - m.x103 <= 0)
m.e36 = Constraint(expr= -m.x84 + m.x92 - m.x103 <= 0)
m.e37 = Constraint(expr= m.x86 - m.x90 - m.x104 <= 0)
m.e38 = Constraint(expr= -m.x86 + m.x90 - m.x104 <= 0)
m.e39 = Constraint(expr= m.x88 - m.x92 - m.x105 <= 0)
m.e40 = Constraint(expr= -m.x88 + m.x92 - m.x105 <= 0)
m.e41 = Constraint(expr= (8.68340342427357 - m.x76)**2 + (8.57974596088368 -
    m.x79)**2 + 122.913026025479 * m.b1 <= 123.913026025479)
m.e42 = Constraint(expr= (9.63614333912176 - m.x76)**2 + (8.80176337918095 -
    m.x79)**2 + 144.203684439948 * m.b2 <= 145.203684439948)
m.e43 = Constraint(expr= (3.68142205418198 - m.x76)**2 + (1.1692321814062 -
    m.x79)**2 + 113.075460968432 * m.b3 <= 114.075460968432)
m.e44 = Constraint(expr= (9.7121756733827 - m.x76)**2 + (7.68772804421774 -
    m.x79)**2 + 132.715787162747 * m.b4 <= 133.715787162747)
m.e45 = Constraint(expr= (3.2772228491781 - m.x76)**2 + (8.20105404549271 -
    m.x79)**2 + 71.5990957077621 * m.b5 <= 72.5990957077621)
m.e46 = Constraint(expr= (8.95169370625893 - m.x76)**2 + (5.71833771240185 -
    m.x79)**2 + 101.022453999802 * m.b6 <= 102.022453999802)
m.e47 = Constraint(expr= (6.39713701672676 - m.x76)**2 + (2.19374777991393 -
    m.x79)**2 + 76.9700130269697 * m.b7 <= 77.9700130269697)
m.e48 = Constraint(expr= (8.63324272987351 - m.x76)**2 + (2.92174290170279 -
    m.x79)**2 + 86.0532928024441 * m.b8 <= 87.0532928024441)
m.e49 = Constraint(expr= (3.63244627881363 - m.x76)**2 + (1.91739848753332 -
    m.x79)**2 + 101.707832966379 * m.b9 <= 102.707832966379)
m.e50 = Constraint(expr= (0.303084489788861 - m.x76)**2 + (2.88588654972735 -
    m.x79)**2 + 144.203684439948 * m.b10 <= 145.203684439948)
m.e51 = Constraint(expr= (9.32557624217471 - m.x76)**2 + (5.59175556022082 -
    m.x79)**2 + 107.566095593812 * m.b11 <= 108.566095593812)
m.e52 = Constraint(expr= (8.52118108549064 - m.x76)**2 + (5.32332318998315 -
    m.x79)**2 + 90.6220952924323 * m.b12 <= 91.6220952924323)
m.e53 = Constraint(expr= (4.01861330995576 - m.x76)**2 + (9.65380890252737 -
    m.x79)**2 + 97.233140568496 * m.b13 <= 98.233140568496)
m.e54 = Constraint(expr= (2.49020328922613 - m.x76)**2 + (0.874596139412213 -
    m.x79)**2 + 135.249644224288 * m.b14 <= 136.249644224288)
m.e55 = Constraint(expr= (0.545671492825244 - m.x76)**2 + (3.81401698819633 -
    m.x79)**2 + 128.252112242799 * m.b15 <= 129.252112242799)
m.e56 = Constraint(expr= m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8
    + m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 == 1)
m.e57 = Constraint(expr= (8.68340342427357 - m.x77)**2 + (8.57974596088368 -
    m.x80)**2 + 122.913026025479 * m.b16 <= 123.913026025479)
m.e58 = Constraint(expr= (9.63614333912176 - m.x77)**2 + (8.80176337918095 -
    m.x80)**2 + 144.203684439948 * m.b17 <= 145.203684439948)
m.e59 = Constraint(expr= (3.68142205418198 - m.x77)**2 + (1.1692321814062 -
    m.x80)**2 + 113.075460968432 * m.b18 <= 114.075460968432)
m.e60 = Constraint(expr= (9.7121756733827 - m.x77)**2 + (7.68772804421774 -
    m.x80)**2 + 132.715787162747 * m.b19 <= 133.715787162747)
m.e61 = Constraint(expr= (3.2772228491781 - m.x77)**2 + (8.20105404549271 -
    m.x80)**2 + 71.5990957077621 * m.b20 <= 72.5990957077621)
m.e62 = Constraint(expr= (8.95169370625893 - m.x77)**2 + (5.71833771240185 -
    m.x80)**2 + 101.022453999802 * m.b21 <= 102.022453999802)
m.e63 = Constraint(expr= (6.39713701672676 - m.x77)**2 + (2.19374777991393 -
    m.x80)**2 + 76.9700130269697 * m.b22 <= 77.9700130269697)
m.e64 = Constraint(expr= (8.63324272987351 - m.x77)**2 + (2.92174290170279 -
    m.x80)**2 + 86.0532928024441 * m.b23 <= 87.0532928024441)
m.e65 = Constraint(expr= (3.63244627881363 - m.x77)**2 + (1.91739848753332 -
    m.x80)**2 + 101.707832966379 * m.b24 <= 102.707832966379)
m.e66 = Constraint(expr= (0.303084489788861 - m.x77)**2 + (2.88588654972735 -
    m.x80)**2 + 144.203684439948 * m.b25 <= 145.203684439948)
m.e67 = Constraint(expr= (9.32557624217471 - m.x77)**2 + (5.59175556022082 -
    m.x80)**2 + 107.566095593812 * m.b26 <= 108.566095593812)
m.e68 = Constraint(expr= (8.52118108549064 - m.x77)**2 + (5.32332318998315 -
    m.x80)**2 + 90.6220952924323 * m.b27 <= 91.6220952924323)
m.e69 = Constraint(expr= (4.01861330995576 - m.x77)**2 + (9.65380890252737 -
    m.x80)**2 + 97.233140568496 * m.b28 <= 98.233140568496)
m.e70 = Constraint(expr= (2.49020328922613 - m.x77)**2 + (0.874596139412213 -
    m.x80)**2 + 135.249644224288 * m.b29 <= 136.249644224288)
m.e71 = Constraint(expr= (0.545671492825244 - m.x77)**2 + (3.81401698819633 -
    m.x80)**2 + 128.252112242799 * m.b30 <= 129.252112242799)
m.e72 = Constraint(expr= m.b16 + m.b17 + m.b18 + m.b19 + m.b20 + m.b21 + m.b22
    + m.b23 + m.b24 + m.b25 + m.b26 + m.b27 + m.b28 + m.b29 + m.b30 == 1)
m.e73 = Constraint(expr= (8.68340342427357 - m.x82)**2 + (8.57974596088368 -
    m.x84)**2 + 122.913026025479 * m.b31 <= 123.913026025479)
m.e74 = Constraint(expr= (9.63614333912176 - m.x82)**2 + (8.80176337918095 -
    m.x84)**2 + 144.203684439948 * m.b32 <= 145.203684439948)
m.e75 = Constraint(expr= (3.68142205418198 - m.x82)**2 + (1.1692321814062 -
    m.x84)**2 + 113.075460968432 * m.b33 <= 114.075460968432)
m.e76 = Constraint(expr= (9.7121756733827 - m.x82)**2 + (7.68772804421774 -
    m.x84)**2 + 132.715787162747 * m.b34 <= 133.715787162747)
m.e77 = Constraint(expr= (3.2772228491781 - m.x82)**2 + (8.20105404549271 -
    m.x84)**2 + 71.5990957077621 * m.b35 <= 72.5990957077621)
m.e78 = Constraint(expr= (8.95169370625893 - m.x82)**2 + (5.71833771240185 -
    m.x84)**2 + 101.022453999802 * m.b36 <= 102.022453999802)
m.e79 = Constraint(expr= (6.39713701672676 - m.x82)**2 + (2.19374777991393 -
    m.x84)**2 + 76.9700130269697 * m.b37 <= 77.9700130269697)
m.e80 = Constraint(expr= (8.63324272987351 - m.x82)**2 + (2.92174290170279 -
    m.x84)**2 + 86.0532928024441 * m.b38 <= 87.0532928024441)
m.e81 = Constraint(expr= (3.63244627881363 - m.x82)**2 + (1.91739848753332 -
    m.x84)**2 + 101.707832966379 * m.b39 <= 102.707832966379)
m.e82 = Constraint(expr= (0.303084489788861 - m.x82)**2 + (2.88588654972735 -
    m.x84)**2 + 144.203684439948 * m.b40 <= 145.203684439948)
m.e83 = Constraint(expr= (9.32557624217471 - m.x82)**2 + (5.59175556022082 -
    m.x84)**2 + 107.566095593812 * m.b41 <= 108.566095593812)
m.e84 = Constraint(expr= (8.52118108549064 - m.x82)**2 + (5.32332318998315 -
    m.x84)**2 + 90.6220952924323 * m.b42 <= 91.6220952924323)
m.e85 = Constraint(expr= (4.01861330995576 - m.x82)**2 + (9.65380890252737 -
    m.x84)**2 + 97.233140568496 * m.b43 <= 98.233140568496)
m.e86 = Constraint(expr= (2.49020328922613 - m.x82)**2 + (0.874596139412213 -
    m.x84)**2 + 135.249644224288 * m.b44 <= 136.249644224288)
m.e87 = Constraint(expr= (0.545671492825244 - m.x82)**2 + (3.81401698819633 -
    m.x84)**2 + 128.252112242799 * m.b45 <= 129.252112242799)
m.e88 = Constraint(expr= m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 + m.b37
    + m.b38 + m.b39 + m.b40 + m.b41 + m.b42 + m.b43 + m.b44 + m.b45 == 1)
m.e89 = Constraint(expr= (8.68340342427357 - m.x86)**2 + (8.57974596088368 -
    m.x88)**2 + 122.913026025479 * m.b46 <= 123.913026025479)
m.e90 = Constraint(expr= (9.63614333912176 - m.x86)**2 + (8.80176337918095 -
    m.x88)**2 + 144.203684439948 * m.b47 <= 145.203684439948)
m.e91 = Constraint(expr= (3.68142205418198 - m.x86)**2 + (1.1692321814062 -
    m.x88)**2 + 113.075460968432 * m.b48 <= 114.075460968432)
m.e92 = Constraint(expr= (9.7121756733827 - m.x86)**2 + (7.68772804421774 -
    m.x88)**2 + 132.715787162747 * m.b49 <= 133.715787162747)
m.e93 = Constraint(expr= (3.2772228491781 - m.x86)**2 + (8.20105404549271 -
    m.x88)**2 + 71.5990957077621 * m.b50 <= 72.5990957077621)
m.e94 = Constraint(expr= (8.95169370625893 - m.x86)**2 + (5.71833771240185 -
    m.x88)**2 + 101.022453999802 * m.b51 <= 102.022453999802)
m.e95 = Constraint(expr= (6.39713701672676 - m.x86)**2 + (2.19374777991393 -
    m.x88)**2 + 76.9700130269697 * m.b52 <= 77.9700130269697)
m.e96 = Constraint(expr= (8.63324272987351 - m.x86)**2 + (2.92174290170279 -
    m.x88)**2 + 86.0532928024441 * m.b53 <= 87.0532928024441)
m.e97 = Constraint(expr= (3.63244627881363 - m.x86)**2 + (1.91739848753332 -
    m.x88)**2 + 101.707832966379 * m.b54 <= 102.707832966379)
m.e98 = Constraint(expr= (0.303084489788861 - m.x86)**2 + (2.88588654972735 -
    m.x88)**2 + 144.203684439948 * m.b55 <= 145.203684439948)
m.e99 = Constraint(expr= (9.32557624217471 - m.x86)**2 + (5.59175556022082 -
    m.x88)**2 + 107.566095593812 * m.b56 <= 108.566095593812)
m.e100 = Constraint(expr= (8.52118108549064 - m.x86)**2 + (5.32332318998315 -
    m.x88)**2 + 90.6220952924323 * m.b57 <= 91.6220952924323)
m.e101 = Constraint(expr= (4.01861330995576 - m.x86)**2 + (9.65380890252737 -
    m.x88)**2 + 97.233140568496 * m.b58 <= 98.233140568496)
m.e102 = Constraint(expr= (2.49020328922613 - m.x86)**2 + (0.874596139412213 -
    m.x88)**2 + 135.249644224288 * m.b59 <= 136.249644224288)
m.e103 = Constraint(expr= (0.545671492825244 - m.x86)**2 + (3.81401698819633 -
    m.x88)**2 + 128.252112242799 * m.b60 <= 129.252112242799)
m.e104 = Constraint(expr= m.b46 + m.b47 + m.b48 + m.b49 + m.b50 + m.b51 + m.b52
    + m.b53 + m.b54 + m.b55 + m.b56 + m.b57 + m.b58 + m.b59 + m.b60 == 1)
m.e105 = Constraint(expr= (8.68340342427357 - m.x90)**2 + (8.57974596088368 -
    m.x92)**2 + 122.913026025479 * m.b61 <= 123.913026025479)
m.e106 = Constraint(expr= (9.63614333912176 - m.x90)**2 + (8.80176337918095 -
    m.x92)**2 + 144.203684439948 * m.b62 <= 145.203684439948)
m.e107 = Constraint(expr= (3.68142205418198 - m.x90)**2 + (1.1692321814062 -
    m.x92)**2 + 113.075460968432 * m.b63 <= 114.075460968432)
m.e108 = Constraint(expr= (9.7121756733827 - m.x90)**2 + (7.68772804421774 -
    m.x92)**2 + 132.715787162747 * m.b64 <= 133.715787162747)
m.e109 = Constraint(expr= (3.2772228491781 - m.x90)**2 + (8.20105404549271 -
    m.x92)**2 + 71.5990957077621 * m.b65 <= 72.5990957077621)
m.e110 = Constraint(expr= (8.95169370625893 - m.x90)**2 + (5.71833771240185 -
    m.x92)**2 + 101.022453999802 * m.b66 <= 102.022453999802)
m.e111 = Constraint(expr= (6.39713701672676 - m.x90)**2 + (2.19374777991393 -
    m.x92)**2 + 76.9700130269697 * m.b67 <= 77.9700130269697)
m.e112 = Constraint(expr= (8.63324272987351 - m.x90)**2 + (2.92174290170279 -
    m.x92)**2 + 86.0532928024441 * m.b68 <= 87.0532928024441)
m.e113 = Constraint(expr= (3.63244627881363 - m.x90)**2 + (1.91739848753332 -
    m.x92)**2 + 101.707832966379 * m.b69 <= 102.707832966379)
m.e114 = Constraint(expr= (0.303084489788861 - m.x90)**2 + (2.88588654972735 -
    m.x92)**2 + 144.203684439948 * m.b70 <= 145.203684439948)
m.e115 = Constraint(expr= (9.32557624217471 - m.x90)**2 + (5.59175556022082 -
    m.x92)**2 + 107.566095593812 * m.b71 <= 108.566095593812)
m.e116 = Constraint(expr= (8.52118108549064 - m.x90)**2 + (5.32332318998315 -
    m.x92)**2 + 90.6220952924323 * m.b72 <= 91.6220952924323)
m.e117 = Constraint(expr= (4.01861330995576 - m.x90)**2 + (9.65380890252737 -
    m.x92)**2 + 97.233140568496 * m.b73 <= 98.233140568496)
m.e118 = Constraint(expr= (2.49020328922613 - m.x90)**2 + (0.874596139412213 -
    m.x92)**2 + 135.249644224288 * m.b74 <= 136.249644224288)
m.e119 = Constraint(expr= (0.545671492825244 - m.x90)**2 + (3.81401698819633 -
    m.x92)**2 + 128.252112242799 * m.b75 <= 129.252112242799)
m.e120 = Constraint(expr= m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b66 + m.b67
    + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 + m.b73 + m.b74 + m.b75 == 1)
m.e121 = Constraint(expr= m.b1 + m.b16 + m.b31 + m.b46 + m.b61 <= 1)
m.e122 = Constraint(expr= m.b2 + m.b17 + m.b32 + m.b47 + m.b62 <= 1)
m.e123 = Constraint(expr= m.b3 + m.b18 + m.b33 + m.b48 + m.b63 <= 1)
m.e124 = Constraint(expr= m.b4 + m.b19 + m.b34 + m.b49 + m.b64 <= 1)
m.e125 = Constraint(expr= m.b5 + m.b20 + m.b35 + m.b50 + m.b65 <= 1)
m.e126 = Constraint(expr= m.b6 + m.b21 + m.b36 + m.b51 + m.b66 <= 1)
m.e127 = Constraint(expr= m.b7 + m.b22 + m.b37 + m.b52 + m.b67 <= 1)
m.e128 = Constraint(expr= m.b8 + m.b23 + m.b38 + m.b53 + m.b68 <= 1)
m.e129 = Constraint(expr= m.b9 + m.b24 + m.b39 + m.b54 + m.b69 <= 1)
m.e130 = Constraint(expr= m.b10 + m.b25 + m.b40 + m.b55 + m.b70 <= 1)
m.e131 = Constraint(expr= m.b11 + m.b26 + m.b41 + m.b56 + m.b71 <= 1)
m.e132 = Constraint(expr= m.b12 + m.b27 + m.b42 + m.b57 + m.b72 <= 1)
m.e133 = Constraint(expr= m.b13 + m.b28 + m.b43 + m.b58 + m.b73 <= 1)
m.e134 = Constraint(expr= m.b14 + m.b29 + m.b44 + m.b59 + m.b74 <= 1)
m.e135 = Constraint(expr= m.b15 + m.b30 + m.b45 + m.b60 + m.b75 <= 1)
m.e136 = Constraint(expr= m.x76 - m.x77 <= 0)
m.e137 = Constraint(expr= m.x77 - m.x82 <= 0)
m.e138 = Constraint(expr= m.x82 - m.x86 <= 0)
m.e139 = Constraint(expr= m.x86 - m.x90 <= 0)
