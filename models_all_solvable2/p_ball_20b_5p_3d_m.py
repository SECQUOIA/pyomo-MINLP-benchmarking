# MINLP written by GAMS Convert at 05/07/21 17:13:00
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       189        5        0      184        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       145       45      100        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       788      488      300
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
m.x111 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x112 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x113 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x114 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x115 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x116 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x117 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x118 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x119 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x120 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x121 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x122 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x123 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x124 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x125 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x126 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x127 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x128 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x129 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x130 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x131 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x132 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x133 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x134 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x135 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x136 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x137 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x138 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x139 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x140 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x141 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x142 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x143 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x144 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x145 = Var(within=Reals, bounds=(0,10), initialize=0)

m.obj = Objective(sense=minimize, expr= m.x103 + m.x106 + m.x109 + m.x111 +
    m.x113 + m.x115 + m.x117 + m.x119 + m.x121 + m.x123 + m.x125 + m.x127 +
    m.x128 + m.x129 + m.x130 + m.x131 + m.x132 + m.x133 + m.x134 + m.x135 +
    m.x136 + m.x137 + m.x138 + m.x139 + m.x140 + m.x141 + m.x142 + m.x143 +
    m.x144 + m.x145)

m.e1 = Constraint(expr= m.x101 - m.x102 - m.x103 <= 0)
m.e2 = Constraint(expr= -m.x101 + m.x102 - m.x103 <= 0)
m.e3 = Constraint(expr= m.x104 - m.x105 - m.x106 <= 0)
m.e4 = Constraint(expr= -m.x104 + m.x105 - m.x106 <= 0)
m.e5 = Constraint(expr= m.x107 - m.x108 - m.x109 <= 0)
m.e6 = Constraint(expr= -m.x107 + m.x108 - m.x109 <= 0)
m.e7 = Constraint(expr= m.x101 - m.x110 - m.x111 <= 0)
m.e8 = Constraint(expr= -m.x101 + m.x110 - m.x111 <= 0)
m.e9 = Constraint(expr= m.x104 - m.x112 - m.x113 <= 0)
m.e10 = Constraint(expr= -m.x104 + m.x112 - m.x113 <= 0)
m.e11 = Constraint(expr= m.x107 - m.x114 - m.x115 <= 0)
m.e12 = Constraint(expr= -m.x107 + m.x114 - m.x115 <= 0)
m.e13 = Constraint(expr= m.x101 - m.x116 - m.x117 <= 0)
m.e14 = Constraint(expr= -m.x101 + m.x116 - m.x117 <= 0)
m.e15 = Constraint(expr= m.x104 - m.x118 - m.x119 <= 0)
m.e16 = Constraint(expr= -m.x104 + m.x118 - m.x119 <= 0)
m.e17 = Constraint(expr= m.x107 - m.x120 - m.x121 <= 0)
m.e18 = Constraint(expr= -m.x107 + m.x120 - m.x121 <= 0)
m.e19 = Constraint(expr= m.x101 - m.x122 - m.x123 <= 0)
m.e20 = Constraint(expr= -m.x101 + m.x122 - m.x123 <= 0)
m.e21 = Constraint(expr= m.x104 - m.x124 - m.x125 <= 0)
m.e22 = Constraint(expr= -m.x104 + m.x124 - m.x125 <= 0)
m.e23 = Constraint(expr= m.x107 - m.x126 - m.x127 <= 0)
m.e24 = Constraint(expr= -m.x107 + m.x126 - m.x127 <= 0)
m.e25 = Constraint(expr= m.x102 - m.x110 - m.x128 <= 0)
m.e26 = Constraint(expr= -m.x102 + m.x110 - m.x128 <= 0)
m.e27 = Constraint(expr= m.x105 - m.x112 - m.x129 <= 0)
m.e28 = Constraint(expr= -m.x105 + m.x112 - m.x129 <= 0)
m.e29 = Constraint(expr= m.x108 - m.x114 - m.x130 <= 0)
m.e30 = Constraint(expr= -m.x108 + m.x114 - m.x130 <= 0)
m.e31 = Constraint(expr= m.x102 - m.x116 - m.x131 <= 0)
m.e32 = Constraint(expr= -m.x102 + m.x116 - m.x131 <= 0)
m.e33 = Constraint(expr= m.x105 - m.x118 - m.x132 <= 0)
m.e34 = Constraint(expr= -m.x105 + m.x118 - m.x132 <= 0)
m.e35 = Constraint(expr= m.x108 - m.x120 - m.x133 <= 0)
m.e36 = Constraint(expr= -m.x108 + m.x120 - m.x133 <= 0)
m.e37 = Constraint(expr= m.x102 - m.x122 - m.x134 <= 0)
m.e38 = Constraint(expr= -m.x102 + m.x122 - m.x134 <= 0)
m.e39 = Constraint(expr= m.x105 - m.x124 - m.x135 <= 0)
m.e40 = Constraint(expr= -m.x105 + m.x124 - m.x135 <= 0)
m.e41 = Constraint(expr= m.x108 - m.x126 - m.x136 <= 0)
m.e42 = Constraint(expr= -m.x108 + m.x126 - m.x136 <= 0)
m.e43 = Constraint(expr= m.x110 - m.x116 - m.x137 <= 0)
m.e44 = Constraint(expr= -m.x110 + m.x116 - m.x137 <= 0)
m.e45 = Constraint(expr= m.x112 - m.x118 - m.x138 <= 0)
m.e46 = Constraint(expr= -m.x112 + m.x118 - m.x138 <= 0)
m.e47 = Constraint(expr= m.x114 - m.x120 - m.x139 <= 0)
m.e48 = Constraint(expr= -m.x114 + m.x120 - m.x139 <= 0)
m.e49 = Constraint(expr= m.x110 - m.x122 - m.x140 <= 0)
m.e50 = Constraint(expr= -m.x110 + m.x122 - m.x140 <= 0)
m.e51 = Constraint(expr= m.x112 - m.x124 - m.x141 <= 0)
m.e52 = Constraint(expr= -m.x112 + m.x124 - m.x141 <= 0)
m.e53 = Constraint(expr= m.x114 - m.x126 - m.x142 <= 0)
m.e54 = Constraint(expr= -m.x114 + m.x126 - m.x142 <= 0)
m.e55 = Constraint(expr= m.x116 - m.x122 - m.x143 <= 0)
m.e56 = Constraint(expr= -m.x116 + m.x122 - m.x143 <= 0)
m.e57 = Constraint(expr= m.x118 - m.x124 - m.x144 <= 0)
m.e58 = Constraint(expr= -m.x118 + m.x124 - m.x144 <= 0)
m.e59 = Constraint(expr= m.x120 - m.x126 - m.x145 <= 0)
m.e60 = Constraint(expr= -m.x120 + m.x126 - m.x145 <= 0)
m.e61 = Constraint(expr= (0.483311857356823 - m.x101)**2 + (0.114242198506904
    - m.x104)**2 + (7.12048883659032 - m.x107)**2 + 188.522461227626 * m.b1
    <= 189.522461227626)
m.e62 = Constraint(expr= (5.2590135790233 - m.x101)**2 + (7.33259189570392 -
    m.x104)**2 + (5.312333476343 - m.x107)**2 + 98.8166159288294 * m.b2
    <= 99.8166159288294)
m.e63 = Constraint(expr= (7.41517046461879 - m.x101)**2 + (9.62332773098117 -
    m.x104)**2 + (4.79943898486809 - m.x107)**2 + 167.849028003939 * m.b3
    <= 168.849028003939)
m.e64 = Constraint(expr= (6.671843981803 - m.x101)**2 + (8.10658123259484 -
    m.x104)**2 + (8.43381689055527 - m.x107)**2 + 144.62434214578 * m.b4
    <= 145.62434214578)
m.e65 = Constraint(expr= (9.05870575338678 - m.x101)**2 + (8.3311941216586 -
    m.x104)**2 + (2.43718333261179 - m.x107)**2 + 188.522461227626 * m.b5
    <= 189.522461227626)
m.e66 = Constraint(expr= (2.45247392282192 - m.x101)**2 + (3.04490781414335 -
    m.x104)**2 + (3.74797873360784 - m.x107)**2 + 119.618424440661 * m.b6
    <= 120.618424440661)
m.e67 = Constraint(expr= (3.17249885664207 - m.x101)**2 + (0.899014640298569 -
    m.x104)**2 + (6.53554769882638 - m.x107)**2 + 128.282312211875 * m.b7
    <= 129.282312211875)
m.e68 = Constraint(expr= (7.19140474364188 - m.x101)**2 + (6.78752778006733 -
    m.x104)**2 + (7.10371917668867 - m.x107)**2 + 108.45575250014 * m.b8
    <= 109.45575250014)
m.e69 = Constraint(expr= (0.581905599074722 - m.x101)**2 + (8.05664566308502 -
    m.x104)**2 + (0.465270839540525 - m.x107)**2 + 163.557092366753 * m.b9
    <= 164.557092366753)
m.e70 = Constraint(expr= (2.89314656575976 - m.x101)**2 + (2.98350648433744 -
    m.x104)**2 + (4.94095686412664 - m.x107)**2 + 101.809153524392 * m.b10
    <= 102.809153524392)
m.e71 = Constraint(expr= (2.18223181481477 - m.x101)**2 + (6.36734447251869 -
    m.x104)**2 + (6.99053555821422 - m.x107)**2 + 135.200072571286 * m.b11
    <= 136.200072571286)
m.e72 = Constraint(expr= (8.39213303571845 - m.x101)**2 + (0.0966493493157039
    - m.x104)**2 + (0.992650538147096 - m.x107)**2 + 168.474583620344 * m.b12
    <= 169.474583620344)
m.e73 = Constraint(expr= (6.8673656213906 - m.x101)**2 + (8.47463209326542 -
    m.x104)**2 + (0.494039939513553 - m.x107)**2 + 188.895677706624 * m.b13
    <= 189.895677706624)
m.e74 = Constraint(expr= (2.07334522686175 - m.x101)**2 + (0.611759422337085 -
    m.x104)**2 + (7.49872182399417 - m.x107)**2 + 157.156134140441 * m.b14
    <= 158.156134140441)
m.e75 = Constraint(expr= (5.58287553353321 - m.x101)**2 + (7.41023187669618 -
    m.x104)**2 + (5.78186220125907 - m.x107)**2 + 102.681819435286 * m.b15
    <= 103.681819435286)
m.e76 = Constraint(expr= (3.75663662491927 - m.x101)**2 + (2.16100057183036 -
    m.x104)**2 + (9.4954261517135 - m.x107)**2 + 153.416411666872 * m.b16
    <= 154.416411666872)
m.e77 = Constraint(expr= (4.04360404243071 - m.x101)**2 + (7.5903513366217 -
    m.x104)**2 + (3.71685851137678 - m.x107)**2 + 100.651007858618 * m.b17
    <= 101.651007858618)
m.e78 = Constraint(expr= (1.45072437530262 - m.x101)**2 + (1.11420059440894 -
    m.x104)**2 + (9.42819884441584 - m.x107)**2 + 188.895677706624 * m.b18
    <= 189.895677706624)
m.e79 = Constraint(expr= (8.44626629441698 - m.x101)**2 + (8.81210793727421 -
    m.x104)**2 + (9.26767041565757 - m.x107)**2 + 168.474583620344 * m.b19
    <= 169.474583620344)
m.e80 = Constraint(expr= (4.74415255019913 - m.x101)**2 + (2.8194183128037 -
    m.x104)**2 + (1.76655535189797 - m.x107)**2 + 126.464760843581 * m.b20
    <= 127.464760843581)
m.e81 = Constraint(expr= m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8
    + m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17 +
    m.b18 + m.b19 + m.b20 == 1)
m.e82 = Constraint(expr= (0.483311857356823 - m.x102)**2 + (0.114242198506904
    - m.x105)**2 + (7.12048883659032 - m.x108)**2 + 188.522461227626 * m.b21
    <= 189.522461227626)
m.e83 = Constraint(expr= (5.2590135790233 - m.x102)**2 + (7.33259189570392 -
    m.x105)**2 + (5.312333476343 - m.x108)**2 + 98.8166159288294 * m.b22
    <= 99.8166159288294)
m.e84 = Constraint(expr= (7.41517046461879 - m.x102)**2 + (9.62332773098117 -
    m.x105)**2 + (4.79943898486809 - m.x108)**2 + 167.849028003939 * m.b23
    <= 168.849028003939)
m.e85 = Constraint(expr= (6.671843981803 - m.x102)**2 + (8.10658123259484 -
    m.x105)**2 + (8.43381689055527 - m.x108)**2 + 144.62434214578 * m.b24
    <= 145.62434214578)
m.e86 = Constraint(expr= (9.05870575338678 - m.x102)**2 + (8.3311941216586 -
    m.x105)**2 + (2.43718333261179 - m.x108)**2 + 188.522461227626 * m.b25
    <= 189.522461227626)
m.e87 = Constraint(expr= (2.45247392282192 - m.x102)**2 + (3.04490781414335 -
    m.x105)**2 + (3.74797873360784 - m.x108)**2 + 119.618424440661 * m.b26
    <= 120.618424440661)
m.e88 = Constraint(expr= (3.17249885664207 - m.x102)**2 + (0.899014640298569 -
    m.x105)**2 + (6.53554769882638 - m.x108)**2 + 128.282312211875 * m.b27
    <= 129.282312211875)
m.e89 = Constraint(expr= (7.19140474364188 - m.x102)**2 + (6.78752778006733 -
    m.x105)**2 + (7.10371917668867 - m.x108)**2 + 108.45575250014 * m.b28
    <= 109.45575250014)
m.e90 = Constraint(expr= (0.581905599074722 - m.x102)**2 + (8.05664566308502 -
    m.x105)**2 + (0.465270839540525 - m.x108)**2 + 163.557092366753 * m.b29
    <= 164.557092366753)
m.e91 = Constraint(expr= (2.89314656575976 - m.x102)**2 + (2.98350648433744 -
    m.x105)**2 + (4.94095686412664 - m.x108)**2 + 101.809153524392 * m.b30
    <= 102.809153524392)
m.e92 = Constraint(expr= (2.18223181481477 - m.x102)**2 + (6.36734447251869 -
    m.x105)**2 + (6.99053555821422 - m.x108)**2 + 135.200072571286 * m.b31
    <= 136.200072571286)
m.e93 = Constraint(expr= (8.39213303571845 - m.x102)**2 + (0.0966493493157039
    - m.x105)**2 + (0.992650538147096 - m.x108)**2 + 168.474583620344 * m.b32
    <= 169.474583620344)
m.e94 = Constraint(expr= (6.8673656213906 - m.x102)**2 + (8.47463209326542 -
    m.x105)**2 + (0.494039939513553 - m.x108)**2 + 188.895677706624 * m.b33
    <= 189.895677706624)
m.e95 = Constraint(expr= (2.07334522686175 - m.x102)**2 + (0.611759422337085 -
    m.x105)**2 + (7.49872182399417 - m.x108)**2 + 157.156134140441 * m.b34
    <= 158.156134140441)
m.e96 = Constraint(expr= (5.58287553353321 - m.x102)**2 + (7.41023187669618 -
    m.x105)**2 + (5.78186220125907 - m.x108)**2 + 102.681819435286 * m.b35
    <= 103.681819435286)
m.e97 = Constraint(expr= (3.75663662491927 - m.x102)**2 + (2.16100057183036 -
    m.x105)**2 + (9.4954261517135 - m.x108)**2 + 153.416411666872 * m.b36
    <= 154.416411666872)
m.e98 = Constraint(expr= (4.04360404243071 - m.x102)**2 + (7.5903513366217 -
    m.x105)**2 + (3.71685851137678 - m.x108)**2 + 100.651007858618 * m.b37
    <= 101.651007858618)
m.e99 = Constraint(expr= (1.45072437530262 - m.x102)**2 + (1.11420059440894 -
    m.x105)**2 + (9.42819884441584 - m.x108)**2 + 188.895677706624 * m.b38
    <= 189.895677706624)
m.e100 = Constraint(expr= (8.44626629441698 - m.x102)**2 + (8.81210793727421 -
    m.x105)**2 + (9.26767041565757 - m.x108)**2 + 168.474583620344 * m.b39
    <= 169.474583620344)
m.e101 = Constraint(expr= (4.74415255019913 - m.x102)**2 + (2.8194183128037 -
    m.x105)**2 + (1.76655535189797 - m.x108)**2 + 126.464760843581 * m.b40
    <= 127.464760843581)
m.e102 = Constraint(expr= m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 + m.b27
    + m.b28 + m.b29 + m.b30 + m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 +
    m.b37 + m.b38 + m.b39 + m.b40 == 1)
m.e103 = Constraint(expr= (0.483311857356823 - m.x110)**2 + (0.114242198506904
    - m.x112)**2 + (7.12048883659032 - m.x114)**2 + 188.522461227626 * m.b41
    <= 189.522461227626)
m.e104 = Constraint(expr= (5.2590135790233 - m.x110)**2 + (7.33259189570392 -
    m.x112)**2 + (5.312333476343 - m.x114)**2 + 98.8166159288294 * m.b42
    <= 99.8166159288294)
m.e105 = Constraint(expr= (7.41517046461879 - m.x110)**2 + (9.62332773098117 -
    m.x112)**2 + (4.79943898486809 - m.x114)**2 + 167.849028003939 * m.b43
    <= 168.849028003939)
m.e106 = Constraint(expr= (6.671843981803 - m.x110)**2 + (8.10658123259484 -
    m.x112)**2 + (8.43381689055527 - m.x114)**2 + 144.62434214578 * m.b44
    <= 145.62434214578)
m.e107 = Constraint(expr= (9.05870575338678 - m.x110)**2 + (8.3311941216586 -
    m.x112)**2 + (2.43718333261179 - m.x114)**2 + 188.522461227626 * m.b45
    <= 189.522461227626)
m.e108 = Constraint(expr= (2.45247392282192 - m.x110)**2 + (3.04490781414335 -
    m.x112)**2 + (3.74797873360784 - m.x114)**2 + 119.618424440661 * m.b46
    <= 120.618424440661)
m.e109 = Constraint(expr= (3.17249885664207 - m.x110)**2 + (0.899014640298569
    - m.x112)**2 + (6.53554769882638 - m.x114)**2 + 128.282312211875 * m.b47
    <= 129.282312211875)
m.e110 = Constraint(expr= (7.19140474364188 - m.x110)**2 + (6.78752778006733 -
    m.x112)**2 + (7.10371917668867 - m.x114)**2 + 108.45575250014 * m.b48
    <= 109.45575250014)
m.e111 = Constraint(expr= (0.581905599074722 - m.x110)**2 + (8.05664566308502
    - m.x112)**2 + (0.465270839540525 - m.x114)**2 + 163.557092366753 * m.b49
    <= 164.557092366753)
m.e112 = Constraint(expr= (2.89314656575976 - m.x110)**2 + (2.98350648433744 -
    m.x112)**2 + (4.94095686412664 - m.x114)**2 + 101.809153524392 * m.b50
    <= 102.809153524392)
m.e113 = Constraint(expr= (2.18223181481477 - m.x110)**2 + (6.36734447251869 -
    m.x112)**2 + (6.99053555821422 - m.x114)**2 + 135.200072571286 * m.b51
    <= 136.200072571286)
m.e114 = Constraint(expr= (8.39213303571845 - m.x110)**2 + (0.0966493493157039
    - m.x112)**2 + (0.992650538147096 - m.x114)**2 + 168.474583620344 * m.b52
    <= 169.474583620344)
m.e115 = Constraint(expr= (6.8673656213906 - m.x110)**2 + (8.47463209326542 -
    m.x112)**2 + (0.494039939513553 - m.x114)**2 + 188.895677706624 * m.b53
    <= 189.895677706624)
m.e116 = Constraint(expr= (2.07334522686175 - m.x110)**2 + (0.611759422337085
    - m.x112)**2 + (7.49872182399417 - m.x114)**2 + 157.156134140441 * m.b54
    <= 158.156134140441)
m.e117 = Constraint(expr= (5.58287553353321 - m.x110)**2 + (7.41023187669618 -
    m.x112)**2 + (5.78186220125907 - m.x114)**2 + 102.681819435286 * m.b55
    <= 103.681819435286)
m.e118 = Constraint(expr= (3.75663662491927 - m.x110)**2 + (2.16100057183036 -
    m.x112)**2 + (9.4954261517135 - m.x114)**2 + 153.416411666872 * m.b56
    <= 154.416411666872)
m.e119 = Constraint(expr= (4.04360404243071 - m.x110)**2 + (7.5903513366217 -
    m.x112)**2 + (3.71685851137678 - m.x114)**2 + 100.651007858618 * m.b57
    <= 101.651007858618)
m.e120 = Constraint(expr= (1.45072437530262 - m.x110)**2 + (1.11420059440894 -
    m.x112)**2 + (9.42819884441584 - m.x114)**2 + 188.895677706624 * m.b58
    <= 189.895677706624)
m.e121 = Constraint(expr= (8.44626629441698 - m.x110)**2 + (8.81210793727421 -
    m.x112)**2 + (9.26767041565757 - m.x114)**2 + 168.474583620344 * m.b59
    <= 169.474583620344)
m.e122 = Constraint(expr= (4.74415255019913 - m.x110)**2 + (2.8194183128037 -
    m.x112)**2 + (1.76655535189797 - m.x114)**2 + 126.464760843581 * m.b60
    <= 127.464760843581)
m.e123 = Constraint(expr= m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47
    + m.b48 + m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 +
    m.b57 + m.b58 + m.b59 + m.b60 == 1)
m.e124 = Constraint(expr= (0.483311857356823 - m.x116)**2 + (0.114242198506904
    - m.x118)**2 + (7.12048883659032 - m.x120)**2 + 188.522461227626 * m.b61
    <= 189.522461227626)
m.e125 = Constraint(expr= (5.2590135790233 - m.x116)**2 + (7.33259189570392 -
    m.x118)**2 + (5.312333476343 - m.x120)**2 + 98.8166159288294 * m.b62
    <= 99.8166159288294)
m.e126 = Constraint(expr= (7.41517046461879 - m.x116)**2 + (9.62332773098117 -
    m.x118)**2 + (4.79943898486809 - m.x120)**2 + 167.849028003939 * m.b63
    <= 168.849028003939)
m.e127 = Constraint(expr= (6.671843981803 - m.x116)**2 + (8.10658123259484 -
    m.x118)**2 + (8.43381689055527 - m.x120)**2 + 144.62434214578 * m.b64
    <= 145.62434214578)
m.e128 = Constraint(expr= (9.05870575338678 - m.x116)**2 + (8.3311941216586 -
    m.x118)**2 + (2.43718333261179 - m.x120)**2 + 188.522461227626 * m.b65
    <= 189.522461227626)
m.e129 = Constraint(expr= (2.45247392282192 - m.x116)**2 + (3.04490781414335 -
    m.x118)**2 + (3.74797873360784 - m.x120)**2 + 119.618424440661 * m.b66
    <= 120.618424440661)
m.e130 = Constraint(expr= (3.17249885664207 - m.x116)**2 + (0.899014640298569
    - m.x118)**2 + (6.53554769882638 - m.x120)**2 + 128.282312211875 * m.b67
    <= 129.282312211875)
m.e131 = Constraint(expr= (7.19140474364188 - m.x116)**2 + (6.78752778006733 -
    m.x118)**2 + (7.10371917668867 - m.x120)**2 + 108.45575250014 * m.b68
    <= 109.45575250014)
m.e132 = Constraint(expr= (0.581905599074722 - m.x116)**2 + (8.05664566308502
    - m.x118)**2 + (0.465270839540525 - m.x120)**2 + 163.557092366753 * m.b69
    <= 164.557092366753)
m.e133 = Constraint(expr= (2.89314656575976 - m.x116)**2 + (2.98350648433744 -
    m.x118)**2 + (4.94095686412664 - m.x120)**2 + 101.809153524392 * m.b70
    <= 102.809153524392)
m.e134 = Constraint(expr= (2.18223181481477 - m.x116)**2 + (6.36734447251869 -
    m.x118)**2 + (6.99053555821422 - m.x120)**2 + 135.200072571286 * m.b71
    <= 136.200072571286)
m.e135 = Constraint(expr= (8.39213303571845 - m.x116)**2 + (0.0966493493157039
    - m.x118)**2 + (0.992650538147096 - m.x120)**2 + 168.474583620344 * m.b72
    <= 169.474583620344)
m.e136 = Constraint(expr= (6.8673656213906 - m.x116)**2 + (8.47463209326542 -
    m.x118)**2 + (0.494039939513553 - m.x120)**2 + 188.895677706624 * m.b73
    <= 189.895677706624)
m.e137 = Constraint(expr= (2.07334522686175 - m.x116)**2 + (0.611759422337085
    - m.x118)**2 + (7.49872182399417 - m.x120)**2 + 157.156134140441 * m.b74
    <= 158.156134140441)
m.e138 = Constraint(expr= (5.58287553353321 - m.x116)**2 + (7.41023187669618 -
    m.x118)**2 + (5.78186220125907 - m.x120)**2 + 102.681819435286 * m.b75
    <= 103.681819435286)
m.e139 = Constraint(expr= (3.75663662491927 - m.x116)**2 + (2.16100057183036 -
    m.x118)**2 + (9.4954261517135 - m.x120)**2 + 153.416411666872 * m.b76
    <= 154.416411666872)
m.e140 = Constraint(expr= (4.04360404243071 - m.x116)**2 + (7.5903513366217 -
    m.x118)**2 + (3.71685851137678 - m.x120)**2 + 100.651007858618 * m.b77
    <= 101.651007858618)
m.e141 = Constraint(expr= (1.45072437530262 - m.x116)**2 + (1.11420059440894 -
    m.x118)**2 + (9.42819884441584 - m.x120)**2 + 188.895677706624 * m.b78
    <= 189.895677706624)
m.e142 = Constraint(expr= (8.44626629441698 - m.x116)**2 + (8.81210793727421 -
    m.x118)**2 + (9.26767041565757 - m.x120)**2 + 168.474583620344 * m.b79
    <= 169.474583620344)
m.e143 = Constraint(expr= (4.74415255019913 - m.x116)**2 + (2.8194183128037 -
    m.x118)**2 + (1.76655535189797 - m.x120)**2 + 126.464760843581 * m.b80
    <= 127.464760843581)
m.e144 = Constraint(expr= m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b66 + m.b67
    + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 + m.b73 + m.b74 + m.b75 + m.b76 +
    m.b77 + m.b78 + m.b79 + m.b80 == 1)
m.e145 = Constraint(expr= (0.483311857356823 - m.x122)**2 + (0.114242198506904
    - m.x124)**2 + (7.12048883659032 - m.x126)**2 + 188.522461227626 * m.b81
    <= 189.522461227626)
m.e146 = Constraint(expr= (5.2590135790233 - m.x122)**2 + (7.33259189570392 -
    m.x124)**2 + (5.312333476343 - m.x126)**2 + 98.8166159288294 * m.b82
    <= 99.8166159288294)
m.e147 = Constraint(expr= (7.41517046461879 - m.x122)**2 + (9.62332773098117 -
    m.x124)**2 + (4.79943898486809 - m.x126)**2 + 167.849028003939 * m.b83
    <= 168.849028003939)
m.e148 = Constraint(expr= (6.671843981803 - m.x122)**2 + (8.10658123259484 -
    m.x124)**2 + (8.43381689055527 - m.x126)**2 + 144.62434214578 * m.b84
    <= 145.62434214578)
m.e149 = Constraint(expr= (9.05870575338678 - m.x122)**2 + (8.3311941216586 -
    m.x124)**2 + (2.43718333261179 - m.x126)**2 + 188.522461227626 * m.b85
    <= 189.522461227626)
m.e150 = Constraint(expr= (2.45247392282192 - m.x122)**2 + (3.04490781414335 -
    m.x124)**2 + (3.74797873360784 - m.x126)**2 + 119.618424440661 * m.b86
    <= 120.618424440661)
m.e151 = Constraint(expr= (3.17249885664207 - m.x122)**2 + (0.899014640298569
    - m.x124)**2 + (6.53554769882638 - m.x126)**2 + 128.282312211875 * m.b87
    <= 129.282312211875)
m.e152 = Constraint(expr= (7.19140474364188 - m.x122)**2 + (6.78752778006733 -
    m.x124)**2 + (7.10371917668867 - m.x126)**2 + 108.45575250014 * m.b88
    <= 109.45575250014)
m.e153 = Constraint(expr= (0.581905599074722 - m.x122)**2 + (8.05664566308502
    - m.x124)**2 + (0.465270839540525 - m.x126)**2 + 163.557092366753 * m.b89
    <= 164.557092366753)
m.e154 = Constraint(expr= (2.89314656575976 - m.x122)**2 + (2.98350648433744 -
    m.x124)**2 + (4.94095686412664 - m.x126)**2 + 101.809153524392 * m.b90
    <= 102.809153524392)
m.e155 = Constraint(expr= (2.18223181481477 - m.x122)**2 + (6.36734447251869 -
    m.x124)**2 + (6.99053555821422 - m.x126)**2 + 135.200072571286 * m.b91
    <= 136.200072571286)
m.e156 = Constraint(expr= (8.39213303571845 - m.x122)**2 + (0.0966493493157039
    - m.x124)**2 + (0.992650538147096 - m.x126)**2 + 168.474583620344 * m.b92
    <= 169.474583620344)
m.e157 = Constraint(expr= (6.8673656213906 - m.x122)**2 + (8.47463209326542 -
    m.x124)**2 + (0.494039939513553 - m.x126)**2 + 188.895677706624 * m.b93
    <= 189.895677706624)
m.e158 = Constraint(expr= (2.07334522686175 - m.x122)**2 + (0.611759422337085
    - m.x124)**2 + (7.49872182399417 - m.x126)**2 + 157.156134140441 * m.b94
    <= 158.156134140441)
m.e159 = Constraint(expr= (5.58287553353321 - m.x122)**2 + (7.41023187669618 -
    m.x124)**2 + (5.78186220125907 - m.x126)**2 + 102.681819435286 * m.b95
    <= 103.681819435286)
m.e160 = Constraint(expr= (3.75663662491927 - m.x122)**2 + (2.16100057183036 -
    m.x124)**2 + (9.4954261517135 - m.x126)**2 + 153.416411666872 * m.b96
    <= 154.416411666872)
m.e161 = Constraint(expr= (4.04360404243071 - m.x122)**2 + (7.5903513366217 -
    m.x124)**2 + (3.71685851137678 - m.x126)**2 + 100.651007858618 * m.b97
    <= 101.651007858618)
m.e162 = Constraint(expr= (1.45072437530262 - m.x122)**2 + (1.11420059440894 -
    m.x124)**2 + (9.42819884441584 - m.x126)**2 + 188.895677706624 * m.b98
    <= 189.895677706624)
m.e163 = Constraint(expr= (8.44626629441698 - m.x122)**2 + (8.81210793727421 -
    m.x124)**2 + (9.26767041565757 - m.x126)**2 + 168.474583620344 * m.b99
    <= 169.474583620344)
m.e164 = Constraint(expr= (4.74415255019913 - m.x122)**2 + (2.8194183128037 -
    m.x124)**2 + (1.76655535189797 - m.x126)**2 + 126.464760843581 * m.b100
    <= 127.464760843581)
m.e165 = Constraint(expr= m.b81 + m.b82 + m.b83 + m.b84 + m.b85 + m.b86 + m.b87
    + m.b88 + m.b89 + m.b90 + m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b96 +
    m.b97 + m.b98 + m.b99 + m.b100 == 1)
m.e166 = Constraint(expr= m.b1 + m.b21 + m.b41 + m.b61 + m.b81 <= 1)
m.e167 = Constraint(expr= m.b2 + m.b22 + m.b42 + m.b62 + m.b82 <= 1)
m.e168 = Constraint(expr= m.b3 + m.b23 + m.b43 + m.b63 + m.b83 <= 1)
m.e169 = Constraint(expr= m.b4 + m.b24 + m.b44 + m.b64 + m.b84 <= 1)
m.e170 = Constraint(expr= m.b5 + m.b25 + m.b45 + m.b65 + m.b85 <= 1)
m.e171 = Constraint(expr= m.b6 + m.b26 + m.b46 + m.b66 + m.b86 <= 1)
m.e172 = Constraint(expr= m.b7 + m.b27 + m.b47 + m.b67 + m.b87 <= 1)
m.e173 = Constraint(expr= m.b8 + m.b28 + m.b48 + m.b68 + m.b88 <= 1)
m.e174 = Constraint(expr= m.b9 + m.b29 + m.b49 + m.b69 + m.b89 <= 1)
m.e175 = Constraint(expr= m.b10 + m.b30 + m.b50 + m.b70 + m.b90 <= 1)
m.e176 = Constraint(expr= m.b11 + m.b31 + m.b51 + m.b71 + m.b91 <= 1)
m.e177 = Constraint(expr= m.b12 + m.b32 + m.b52 + m.b72 + m.b92 <= 1)
m.e178 = Constraint(expr= m.b13 + m.b33 + m.b53 + m.b73 + m.b93 <= 1)
m.e179 = Constraint(expr= m.b14 + m.b34 + m.b54 + m.b74 + m.b94 <= 1)
m.e180 = Constraint(expr= m.b15 + m.b35 + m.b55 + m.b75 + m.b95 <= 1)
m.e181 = Constraint(expr= m.b16 + m.b36 + m.b56 + m.b76 + m.b96 <= 1)
m.e182 = Constraint(expr= m.b17 + m.b37 + m.b57 + m.b77 + m.b97 <= 1)
m.e183 = Constraint(expr= m.b18 + m.b38 + m.b58 + m.b78 + m.b98 <= 1)
m.e184 = Constraint(expr= m.b19 + m.b39 + m.b59 + m.b79 + m.b99 <= 1)
m.e185 = Constraint(expr= m.b20 + m.b40 + m.b60 + m.b80 + m.b100 <= 1)
m.e186 = Constraint(expr= m.x101 - m.x102 <= 0)
m.e187 = Constraint(expr= m.x102 - m.x110 <= 0)
m.e188 = Constraint(expr= m.x110 - m.x116 <= 0)
m.e189 = Constraint(expr= m.x116 - m.x122 <= 0)
