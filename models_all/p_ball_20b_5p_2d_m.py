# MINLP written by GAMS Convert at 05/07/21 17:13:00
#
# Equation counts
#     Total        E        G        L        N        X        C        B
#       169        5        0      164        0        0        0        0
#
# Variable counts
#                  x        b        i      s1s      s2s       sc       si
#     Total     cont   binary  integer     sos1     sos2    scont     sint
#       130       30      100        0        0        0        0        0
# FX      0
#
# Nonzero counts
#     Total    const       NL
#       628      428      200
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
m.b13 = Var(within=Binary, bounds=(0,1), initialize=1)
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
m.b57 = Var(within=Binary, bounds=(0,1), initialize=1)
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
m.b76 = Var(within=Binary, bounds=(0,1), initialize=1)
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
m.b92 = Var(within=Binary, bounds=(0,1), initialize=1)
m.b93 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b94 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b95 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b96 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b97 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b98 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b99 = Var(within=Binary, bounds=(0,1), initialize=0)
m.b100 = Var(within=Binary, bounds=(0,1), initialize=0)
m.x101 = Var(within=Reals, bounds=(0,10), initialize=4.42317283955211)
m.x102 = Var(within=Reals, bounds=(0,10), initialize=5.03240021704025)
m.x103 = Var(within=Reals, bounds=(0,10), initialize=0.609227377488138)
m.x104 = Var(within=Reals, bounds=(0,10), initialize=7.96948572261155)
m.x105 = Var(within=Reals, bounds=(0,10), initialize=7.96948572261155)
m.x106 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x107 = Var(within=Reals, bounds=(0,10), initialize=5.03240021704025)
m.x108 = Var(within=Reals, bounds=(0,10), initialize=0.609227377488138)
m.x109 = Var(within=Reals, bounds=(0,10), initialize=7.96948572261155)
m.x110 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x111 = Var(within=Reals, bounds=(0,10), initialize=5.03240021704025)
m.x112 = Var(within=Reals, bounds=(0,10), initialize=0.609227377488136)
m.x113 = Var(within=Reals, bounds=(0,10), initialize=7.96948572261155)
m.x114 = Var(within=Reals, bounds=(0,10), initialize=0)
m.x115 = Var(within=Reals, bounds=(0,10), initialize=5.03240021704025)
m.x116 = Var(within=Reals, bounds=(0,10), initialize=0.609227377488136)
m.x117 = Var(within=Reals, bounds=(0,10), initialize=7.96948572261155)
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

m.obj = Objective(sense=minimize, expr= m.x103 + m.x106 + m.x108 + m.x110 +
    m.x112 + m.x114 + m.x116 + m.x118 + m.x119 + m.x120 + m.x121 + m.x122 +
    m.x123 + m.x124 + m.x125 + m.x126 + m.x127 + m.x128 + m.x129 + m.x130)

m.e1 = Constraint(expr= m.x101 - m.x102 - m.x103 <= 0)
m.e2 = Constraint(expr= -m.x101 + m.x102 - m.x103 <= 0)
m.e3 = Constraint(expr= m.x104 - m.x105 - m.x106 <= 0)
m.e4 = Constraint(expr= -m.x104 + m.x105 - m.x106 <= 0)
m.e5 = Constraint(expr= m.x101 - m.x107 - m.x108 <= 0)
m.e6 = Constraint(expr= -m.x101 + m.x107 - m.x108 <= 0)
m.e7 = Constraint(expr= m.x104 - m.x109 - m.x110 <= 0)
m.e8 = Constraint(expr= -m.x104 + m.x109 - m.x110 <= 0)
m.e9 = Constraint(expr= m.x101 - m.x111 - m.x112 <= 0)
m.e10 = Constraint(expr= -m.x101 + m.x111 - m.x112 <= 0)
m.e11 = Constraint(expr= m.x104 - m.x113 - m.x114 <= 0)
m.e12 = Constraint(expr= -m.x104 + m.x113 - m.x114 <= 0)
m.e13 = Constraint(expr= m.x101 - m.x115 - m.x116 <= 0)
m.e14 = Constraint(expr= -m.x101 + m.x115 - m.x116 <= 0)
m.e15 = Constraint(expr= m.x104 - m.x117 - m.x118 <= 0)
m.e16 = Constraint(expr= -m.x104 + m.x117 - m.x118 <= 0)
m.e17 = Constraint(expr= m.x102 - m.x107 - m.x119 <= 0)
m.e18 = Constraint(expr= -m.x102 + m.x107 - m.x119 <= 0)
m.e19 = Constraint(expr= m.x105 - m.x109 - m.x120 <= 0)
m.e20 = Constraint(expr= -m.x105 + m.x109 - m.x120 <= 0)
m.e21 = Constraint(expr= m.x102 - m.x111 - m.x121 <= 0)
m.e22 = Constraint(expr= -m.x102 + m.x111 - m.x121 <= 0)
m.e23 = Constraint(expr= m.x105 - m.x113 - m.x122 <= 0)
m.e24 = Constraint(expr= -m.x105 + m.x113 - m.x122 <= 0)
m.e25 = Constraint(expr= m.x102 - m.x115 - m.x123 <= 0)
m.e26 = Constraint(expr= -m.x102 + m.x115 - m.x123 <= 0)
m.e27 = Constraint(expr= m.x105 - m.x117 - m.x124 <= 0)
m.e28 = Constraint(expr= -m.x105 + m.x117 - m.x124 <= 0)
m.e29 = Constraint(expr= m.x107 - m.x111 - m.x125 <= 0)
m.e30 = Constraint(expr= -m.x107 + m.x111 - m.x125 <= 0)
m.e31 = Constraint(expr= m.x109 - m.x113 - m.x126 <= 0)
m.e32 = Constraint(expr= -m.x109 + m.x113 - m.x126 <= 0)
m.e33 = Constraint(expr= m.x107 - m.x115 - m.x127 <= 0)
m.e34 = Constraint(expr= -m.x107 + m.x115 - m.x127 <= 0)
m.e35 = Constraint(expr= m.x109 - m.x117 - m.x128 <= 0)
m.e36 = Constraint(expr= -m.x109 + m.x117 - m.x128 <= 0)
m.e37 = Constraint(expr= m.x111 - m.x115 - m.x129 <= 0)
m.e38 = Constraint(expr= -m.x111 + m.x115 - m.x129 <= 0)
m.e39 = Constraint(expr= m.x113 - m.x117 - m.x130 <= 0)
m.e40 = Constraint(expr= -m.x113 + m.x117 - m.x130 <= 0)
m.e41 = Constraint(expr= (0.0236753863366035 - m.x101)**2 + (0.861938468195851
    - m.x104)**2 + 133.598318045686 * m.b1 <= 134.598318045686)
m.e42 = Constraint(expr= (1.43095891437813 - m.x101)**2 + (5.10831625828775 -
    m.x104)**2 + 94.8544563231416 * m.b2 <= 95.8544563231416)
m.e43 = Constraint(expr= (1.21379363277567 - m.x101)**2 + (3.00432848540233 -
    m.x104)**2 + 87.4797735261255 * m.b3 <= 88.4797735261255)
m.e44 = Constraint(expr= (8.84443217821809 - m.x101)**2 + (0.384566405581435 -
    m.x104)**2 + 103.126413671578 * m.b4 <= 104.126413671578)
m.e45 = Constraint(expr= (5.88364087295228 - m.x101)**2 + (7.44470191338639 -
    m.x104)**2 + 95.2983106051005 * m.b5 <= 96.2983106051005)
m.e46 = Constraint(expr= (8.07096798042338 - m.x101)**2 + (5.55715186969177 -
    m.x104)**2 + 105.43767414173 * m.b6 <= 106.43767414173)
m.e47 = Constraint(expr= (9.60611615222079 - m.x101)**2 + (3.49008429472371 -
    m.x104)**2 + 118.60294806901 * m.b7 <= 119.60294806901)
m.e48 = Constraint(expr= (3.8828653966979 - m.x101)**2 + (5.56627471425883 -
    m.x104)**2 + 65.8153811229109 * m.b8 <= 66.8153811229109)
m.e49 = Constraint(expr= (3.47709171076729 - m.x101)**2 + (1.01589173470293 -
    m.x104)**2 + 81.404902491826 * m.b9 <= 82.404902491826)
m.e50 = Constraint(expr= (3.29737974336435 - m.x101)**2 + (4.14110922298337 -
    m.x104)**2 + 58.2801217051105 * m.b10 <= 59.2801217051105)
m.e51 = Constraint(expr= (8.28345883424477 - m.x101)**2 + (7.50806458757389 -
    m.x104)**2 + 133.598318045686 * m.b11 <= 134.598318045686)
m.e52 = Constraint(expr= (5.4084966970588 - m.x101)**2 + (7.74684442267358 -
    m.x104)**2 + 93.8794468182122 * m.b12 <= 94.8794468182122)
m.e53 = Constraint(expr= (3.43292425314245 - m.x101)**2 + (7.8299358039566 -
    m.x104)**2 + 103.126413671578 * m.b13 <= 104.126413671578)
m.e54 = Constraint(expr= (8.35004447905012 - m.x101)**2 + (1.33263454148094 -
    m.x104)**2 + 86.2293028346251 * m.b14 <= 87.2293028346251)
m.e55 = Constraint(expr= (2.65420450303518 - m.x101)**2 + (6.31096321892449 -
    m.x104)**2 + 90.5806541970954 * m.b15 <= 91.5806541970954)
m.e56 = Constraint(expr= (5.8344315991351 - m.x101)**2 + (8.56684140863644 -
    m.x104)**2 + 112.431237492188 * m.b16 <= 113.431237492188)
m.e57 = Constraint(expr= (4.10957657319824 - m.x101)**2 + (7.8233834211224 -
    m.x104)**2 + 95.3905990097055 * m.b17 <= 96.3905990097055)
m.e58 = Constraint(expr= (7.39474057003054 - m.x101)**2 + (2.49738552645804 -
    m.x104)**2 + 72.1079233169562 * m.b18 <= 73.1079233169562)
m.e59 = Constraint(expr= (6.14221519240217 - m.x101)**2 + (3.03591203112434 -
    m.x104)**2 + 55.1492512196064 * m.b19 <= 56.1492512196064)
m.e60 = Constraint(expr= (8.26974385940666 - m.x101)**2 + (4.22323814320874 -
    m.x104)**2 + 97.1056389080134 * m.b20 <= 98.1056389080134)
m.e61 = Constraint(expr= m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8
    + m.b9 + m.b10 + m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17 +
    m.b18 + m.b19 + m.b20 == 1)
m.e62 = Constraint(expr= (0.0236753863366035 - m.x102)**2 + (0.861938468195851
    - m.x105)**2 + 133.598318045686 * m.b21 <= 134.598318045686)
m.e63 = Constraint(expr= (1.43095891437813 - m.x102)**2 + (5.10831625828775 -
    m.x105)**2 + 94.8544563231416 * m.b22 <= 95.8544563231416)
m.e64 = Constraint(expr= (1.21379363277567 - m.x102)**2 + (3.00432848540233 -
    m.x105)**2 + 87.4797735261255 * m.b23 <= 88.4797735261255)
m.e65 = Constraint(expr= (8.84443217821809 - m.x102)**2 + (0.384566405581435 -
    m.x105)**2 + 103.126413671578 * m.b24 <= 104.126413671578)
m.e66 = Constraint(expr= (5.88364087295228 - m.x102)**2 + (7.44470191338639 -
    m.x105)**2 + 95.2983106051005 * m.b25 <= 96.2983106051005)
m.e67 = Constraint(expr= (8.07096798042338 - m.x102)**2 + (5.55715186969177 -
    m.x105)**2 + 105.43767414173 * m.b26 <= 106.43767414173)
m.e68 = Constraint(expr= (9.60611615222079 - m.x102)**2 + (3.49008429472371 -
    m.x105)**2 + 118.60294806901 * m.b27 <= 119.60294806901)
m.e69 = Constraint(expr= (3.8828653966979 - m.x102)**2 + (5.56627471425883 -
    m.x105)**2 + 65.8153811229109 * m.b28 <= 66.8153811229109)
m.e70 = Constraint(expr= (3.47709171076729 - m.x102)**2 + (1.01589173470293 -
    m.x105)**2 + 81.404902491826 * m.b29 <= 82.404902491826)
m.e71 = Constraint(expr= (3.29737974336435 - m.x102)**2 + (4.14110922298337 -
    m.x105)**2 + 58.2801217051105 * m.b30 <= 59.2801217051105)
m.e72 = Constraint(expr= (8.28345883424477 - m.x102)**2 + (7.50806458757389 -
    m.x105)**2 + 133.598318045686 * m.b31 <= 134.598318045686)
m.e73 = Constraint(expr= (5.4084966970588 - m.x102)**2 + (7.74684442267358 -
    m.x105)**2 + 93.8794468182122 * m.b32 <= 94.8794468182122)
m.e74 = Constraint(expr= (3.43292425314245 - m.x102)**2 + (7.8299358039566 -
    m.x105)**2 + 103.126413671578 * m.b33 <= 104.126413671578)
m.e75 = Constraint(expr= (8.35004447905012 - m.x102)**2 + (1.33263454148094 -
    m.x105)**2 + 86.2293028346251 * m.b34 <= 87.2293028346251)
m.e76 = Constraint(expr= (2.65420450303518 - m.x102)**2 + (6.31096321892449 -
    m.x105)**2 + 90.5806541970954 * m.b35 <= 91.5806541970954)
m.e77 = Constraint(expr= (5.8344315991351 - m.x102)**2 + (8.56684140863644 -
    m.x105)**2 + 112.431237492188 * m.b36 <= 113.431237492188)
m.e78 = Constraint(expr= (4.10957657319824 - m.x102)**2 + (7.8233834211224 -
    m.x105)**2 + 95.3905990097055 * m.b37 <= 96.3905990097055)
m.e79 = Constraint(expr= (7.39474057003054 - m.x102)**2 + (2.49738552645804 -
    m.x105)**2 + 72.1079233169562 * m.b38 <= 73.1079233169562)
m.e80 = Constraint(expr= (6.14221519240217 - m.x102)**2 + (3.03591203112434 -
    m.x105)**2 + 55.1492512196064 * m.b39 <= 56.1492512196064)
m.e81 = Constraint(expr= (8.26974385940666 - m.x102)**2 + (4.22323814320874 -
    m.x105)**2 + 97.1056389080134 * m.b40 <= 98.1056389080134)
m.e82 = Constraint(expr= m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 + m.b27
    + m.b28 + m.b29 + m.b30 + m.b31 + m.b32 + m.b33 + m.b34 + m.b35 + m.b36 +
    m.b37 + m.b38 + m.b39 + m.b40 == 1)
m.e83 = Constraint(expr= (0.0236753863366035 - m.x107)**2 + (0.861938468195851
    - m.x109)**2 + 133.598318045686 * m.b41 <= 134.598318045686)
m.e84 = Constraint(expr= (1.43095891437813 - m.x107)**2 + (5.10831625828775 -
    m.x109)**2 + 94.8544563231416 * m.b42 <= 95.8544563231416)
m.e85 = Constraint(expr= (1.21379363277567 - m.x107)**2 + (3.00432848540233 -
    m.x109)**2 + 87.4797735261255 * m.b43 <= 88.4797735261255)
m.e86 = Constraint(expr= (8.84443217821809 - m.x107)**2 + (0.384566405581435 -
    m.x109)**2 + 103.126413671578 * m.b44 <= 104.126413671578)
m.e87 = Constraint(expr= (5.88364087295228 - m.x107)**2 + (7.44470191338639 -
    m.x109)**2 + 95.2983106051005 * m.b45 <= 96.2983106051005)
m.e88 = Constraint(expr= (8.07096798042338 - m.x107)**2 + (5.55715186969177 -
    m.x109)**2 + 105.43767414173 * m.b46 <= 106.43767414173)
m.e89 = Constraint(expr= (9.60611615222079 - m.x107)**2 + (3.49008429472371 -
    m.x109)**2 + 118.60294806901 * m.b47 <= 119.60294806901)
m.e90 = Constraint(expr= (3.8828653966979 - m.x107)**2 + (5.56627471425883 -
    m.x109)**2 + 65.8153811229109 * m.b48 <= 66.8153811229109)
m.e91 = Constraint(expr= (3.47709171076729 - m.x107)**2 + (1.01589173470293 -
    m.x109)**2 + 81.404902491826 * m.b49 <= 82.404902491826)
m.e92 = Constraint(expr= (3.29737974336435 - m.x107)**2 + (4.14110922298337 -
    m.x109)**2 + 58.2801217051105 * m.b50 <= 59.2801217051105)
m.e93 = Constraint(expr= (8.28345883424477 - m.x107)**2 + (7.50806458757389 -
    m.x109)**2 + 133.598318045686 * m.b51 <= 134.598318045686)
m.e94 = Constraint(expr= (5.4084966970588 - m.x107)**2 + (7.74684442267358 -
    m.x109)**2 + 93.8794468182122 * m.b52 <= 94.8794468182122)
m.e95 = Constraint(expr= (3.43292425314245 - m.x107)**2 + (7.8299358039566 -
    m.x109)**2 + 103.126413671578 * m.b53 <= 104.126413671578)
m.e96 = Constraint(expr= (8.35004447905012 - m.x107)**2 + (1.33263454148094 -
    m.x109)**2 + 86.2293028346251 * m.b54 <= 87.2293028346251)
m.e97 = Constraint(expr= (2.65420450303518 - m.x107)**2 + (6.31096321892449 -
    m.x109)**2 + 90.5806541970954 * m.b55 <= 91.5806541970954)
m.e98 = Constraint(expr= (5.8344315991351 - m.x107)**2 + (8.56684140863644 -
    m.x109)**2 + 112.431237492188 * m.b56 <= 113.431237492188)
m.e99 = Constraint(expr= (4.10957657319824 - m.x107)**2 + (7.8233834211224 -
    m.x109)**2 + 95.3905990097055 * m.b57 <= 96.3905990097055)
m.e100 = Constraint(expr= (7.39474057003054 - m.x107)**2 + (2.49738552645804 -
    m.x109)**2 + 72.1079233169562 * m.b58 <= 73.1079233169562)
m.e101 = Constraint(expr= (6.14221519240217 - m.x107)**2 + (3.03591203112434 -
    m.x109)**2 + 55.1492512196064 * m.b59 <= 56.1492512196064)
m.e102 = Constraint(expr= (8.26974385940666 - m.x107)**2 + (4.22323814320874 -
    m.x109)**2 + 97.1056389080134 * m.b60 <= 98.1056389080134)
m.e103 = Constraint(expr= m.b41 + m.b42 + m.b43 + m.b44 + m.b45 + m.b46 + m.b47
    + m.b48 + m.b49 + m.b50 + m.b51 + m.b52 + m.b53 + m.b54 + m.b55 + m.b56 +
    m.b57 + m.b58 + m.b59 + m.b60 == 1)
m.e104 = Constraint(expr= (0.0236753863366035 - m.x111)**2 + (0.861938468195851
    - m.x113)**2 + 133.598318045686 * m.b61 <= 134.598318045686)
m.e105 = Constraint(expr= (1.43095891437813 - m.x111)**2 + (5.10831625828775 -
    m.x113)**2 + 94.8544563231416 * m.b62 <= 95.8544563231416)
m.e106 = Constraint(expr= (1.21379363277567 - m.x111)**2 + (3.00432848540233 -
    m.x113)**2 + 87.4797735261255 * m.b63 <= 88.4797735261255)
m.e107 = Constraint(expr= (8.84443217821809 - m.x111)**2 + (0.384566405581435
    - m.x113)**2 + 103.126413671578 * m.b64 <= 104.126413671578)
m.e108 = Constraint(expr= (5.88364087295228 - m.x111)**2 + (7.44470191338639 -
    m.x113)**2 + 95.2983106051005 * m.b65 <= 96.2983106051005)
m.e109 = Constraint(expr= (8.07096798042338 - m.x111)**2 + (5.55715186969177 -
    m.x113)**2 + 105.43767414173 * m.b66 <= 106.43767414173)
m.e110 = Constraint(expr= (9.60611615222079 - m.x111)**2 + (3.49008429472371 -
    m.x113)**2 + 118.60294806901 * m.b67 <= 119.60294806901)
m.e111 = Constraint(expr= (3.8828653966979 - m.x111)**2 + (5.56627471425883 -
    m.x113)**2 + 65.8153811229109 * m.b68 <= 66.8153811229109)
m.e112 = Constraint(expr= (3.47709171076729 - m.x111)**2 + (1.01589173470293 -
    m.x113)**2 + 81.404902491826 * m.b69 <= 82.404902491826)
m.e113 = Constraint(expr= (3.29737974336435 - m.x111)**2 + (4.14110922298337 -
    m.x113)**2 + 58.2801217051105 * m.b70 <= 59.2801217051105)
m.e114 = Constraint(expr= (8.28345883424477 - m.x111)**2 + (7.50806458757389 -
    m.x113)**2 + 133.598318045686 * m.b71 <= 134.598318045686)
m.e115 = Constraint(expr= (5.4084966970588 - m.x111)**2 + (7.74684442267358 -
    m.x113)**2 + 93.8794468182122 * m.b72 <= 94.8794468182122)
m.e116 = Constraint(expr= (3.43292425314245 - m.x111)**2 + (7.8299358039566 -
    m.x113)**2 + 103.126413671578 * m.b73 <= 104.126413671578)
m.e117 = Constraint(expr= (8.35004447905012 - m.x111)**2 + (1.33263454148094 -
    m.x113)**2 + 86.2293028346251 * m.b74 <= 87.2293028346251)
m.e118 = Constraint(expr= (2.65420450303518 - m.x111)**2 + (6.31096321892449 -
    m.x113)**2 + 90.5806541970954 * m.b75 <= 91.5806541970954)
m.e119 = Constraint(expr= (5.8344315991351 - m.x111)**2 + (8.56684140863644 -
    m.x113)**2 + 112.431237492188 * m.b76 <= 113.431237492188)
m.e120 = Constraint(expr= (4.10957657319824 - m.x111)**2 + (7.8233834211224 -
    m.x113)**2 + 95.3905990097055 * m.b77 <= 96.3905990097055)
m.e121 = Constraint(expr= (7.39474057003054 - m.x111)**2 + (2.49738552645804 -
    m.x113)**2 + 72.1079233169562 * m.b78 <= 73.1079233169562)
m.e122 = Constraint(expr= (6.14221519240217 - m.x111)**2 + (3.03591203112434 -
    m.x113)**2 + 55.1492512196064 * m.b79 <= 56.1492512196064)
m.e123 = Constraint(expr= (8.26974385940666 - m.x111)**2 + (4.22323814320874 -
    m.x113)**2 + 97.1056389080134 * m.b80 <= 98.1056389080134)
m.e124 = Constraint(expr= m.b61 + m.b62 + m.b63 + m.b64 + m.b65 + m.b66 + m.b67
    + m.b68 + m.b69 + m.b70 + m.b71 + m.b72 + m.b73 + m.b74 + m.b75 + m.b76 +
    m.b77 + m.b78 + m.b79 + m.b80 == 1)
m.e125 = Constraint(expr= (0.0236753863366035 - m.x115)**2 + (0.861938468195851
    - m.x117)**2 + 133.598318045686 * m.b81 <= 134.598318045686)
m.e126 = Constraint(expr= (1.43095891437813 - m.x115)**2 + (5.10831625828775 -
    m.x117)**2 + 94.8544563231416 * m.b82 <= 95.8544563231416)
m.e127 = Constraint(expr= (1.21379363277567 - m.x115)**2 + (3.00432848540233 -
    m.x117)**2 + 87.4797735261255 * m.b83 <= 88.4797735261255)
m.e128 = Constraint(expr= (8.84443217821809 - m.x115)**2 + (0.384566405581435
    - m.x117)**2 + 103.126413671578 * m.b84 <= 104.126413671578)
m.e129 = Constraint(expr= (5.88364087295228 - m.x115)**2 + (7.44470191338639 -
    m.x117)**2 + 95.2983106051005 * m.b85 <= 96.2983106051005)
m.e130 = Constraint(expr= (8.07096798042338 - m.x115)**2 + (5.55715186969177 -
    m.x117)**2 + 105.43767414173 * m.b86 <= 106.43767414173)
m.e131 = Constraint(expr= (9.60611615222079 - m.x115)**2 + (3.49008429472371 -
    m.x117)**2 + 118.60294806901 * m.b87 <= 119.60294806901)
m.e132 = Constraint(expr= (3.8828653966979 - m.x115)**2 + (5.56627471425883 -
    m.x117)**2 + 65.8153811229109 * m.b88 <= 66.8153811229109)
m.e133 = Constraint(expr= (3.47709171076729 - m.x115)**2 + (1.01589173470293 -
    m.x117)**2 + 81.404902491826 * m.b89 <= 82.404902491826)
m.e134 = Constraint(expr= (3.29737974336435 - m.x115)**2 + (4.14110922298337 -
    m.x117)**2 + 58.2801217051105 * m.b90 <= 59.2801217051105)
m.e135 = Constraint(expr= (8.28345883424477 - m.x115)**2 + (7.50806458757389 -
    m.x117)**2 + 133.598318045686 * m.b91 <= 134.598318045686)
m.e136 = Constraint(expr= (5.4084966970588 - m.x115)**2 + (7.74684442267358 -
    m.x117)**2 + 93.8794468182122 * m.b92 <= 94.8794468182122)
m.e137 = Constraint(expr= (3.43292425314245 - m.x115)**2 + (7.8299358039566 -
    m.x117)**2 + 103.126413671578 * m.b93 <= 104.126413671578)
m.e138 = Constraint(expr= (8.35004447905012 - m.x115)**2 + (1.33263454148094 -
    m.x117)**2 + 86.2293028346251 * m.b94 <= 87.2293028346251)
m.e139 = Constraint(expr= (2.65420450303518 - m.x115)**2 + (6.31096321892449 -
    m.x117)**2 + 90.5806541970954 * m.b95 <= 91.5806541970954)
m.e140 = Constraint(expr= (5.8344315991351 - m.x115)**2 + (8.56684140863644 -
    m.x117)**2 + 112.431237492188 * m.b96 <= 113.431237492188)
m.e141 = Constraint(expr= (4.10957657319824 - m.x115)**2 + (7.8233834211224 -
    m.x117)**2 + 95.3905990097055 * m.b97 <= 96.3905990097055)
m.e142 = Constraint(expr= (7.39474057003054 - m.x115)**2 + (2.49738552645804 -
    m.x117)**2 + 72.1079233169562 * m.b98 <= 73.1079233169562)
m.e143 = Constraint(expr= (6.14221519240217 - m.x115)**2 + (3.03591203112434 -
    m.x117)**2 + 55.1492512196064 * m.b99 <= 56.1492512196064)
m.e144 = Constraint(expr= (8.26974385940666 - m.x115)**2 + (4.22323814320874 -
    m.x117)**2 + 97.1056389080134 * m.b100 <= 98.1056389080134)
m.e145 = Constraint(expr= m.b81 + m.b82 + m.b83 + m.b84 + m.b85 + m.b86 + m.b87
    + m.b88 + m.b89 + m.b90 + m.b91 + m.b92 + m.b93 + m.b94 + m.b95 + m.b96 +
    m.b97 + m.b98 + m.b99 + m.b100 == 1)
m.e146 = Constraint(expr= m.b1 + m.b21 + m.b41 + m.b61 + m.b81 <= 1)
m.e147 = Constraint(expr= m.b2 + m.b22 + m.b42 + m.b62 + m.b82 <= 1)
m.e148 = Constraint(expr= m.b3 + m.b23 + m.b43 + m.b63 + m.b83 <= 1)
m.e149 = Constraint(expr= m.b4 + m.b24 + m.b44 + m.b64 + m.b84 <= 1)
m.e150 = Constraint(expr= m.b5 + m.b25 + m.b45 + m.b65 + m.b85 <= 1)
m.e151 = Constraint(expr= m.b6 + m.b26 + m.b46 + m.b66 + m.b86 <= 1)
m.e152 = Constraint(expr= m.b7 + m.b27 + m.b47 + m.b67 + m.b87 <= 1)
m.e153 = Constraint(expr= m.b8 + m.b28 + m.b48 + m.b68 + m.b88 <= 1)
m.e154 = Constraint(expr= m.b9 + m.b29 + m.b49 + m.b69 + m.b89 <= 1)
m.e155 = Constraint(expr= m.b10 + m.b30 + m.b50 + m.b70 + m.b90 <= 1)
m.e156 = Constraint(expr= m.b11 + m.b31 + m.b51 + m.b71 + m.b91 <= 1)
m.e157 = Constraint(expr= m.b12 + m.b32 + m.b52 + m.b72 + m.b92 <= 1)
m.e158 = Constraint(expr= m.b13 + m.b33 + m.b53 + m.b73 + m.b93 <= 1)
m.e159 = Constraint(expr= m.b14 + m.b34 + m.b54 + m.b74 + m.b94 <= 1)
m.e160 = Constraint(expr= m.b15 + m.b35 + m.b55 + m.b75 + m.b95 <= 1)
m.e161 = Constraint(expr= m.b16 + m.b36 + m.b56 + m.b76 + m.b96 <= 1)
m.e162 = Constraint(expr= m.b17 + m.b37 + m.b57 + m.b77 + m.b97 <= 1)
m.e163 = Constraint(expr= m.b18 + m.b38 + m.b58 + m.b78 + m.b98 <= 1)
m.e164 = Constraint(expr= m.b19 + m.b39 + m.b59 + m.b79 + m.b99 <= 1)
m.e165 = Constraint(expr= m.b20 + m.b40 + m.b60 + m.b80 + m.b100 <= 1)
m.e166 = Constraint(expr= m.x101 - m.x102 <= 0)
m.e167 = Constraint(expr= m.x102 - m.x107 <= 0)
m.e168 = Constraint(expr= m.x107 - m.x111 <= 0)
m.e169 = Constraint(expr= m.x111 - m.x115 <= 0)
