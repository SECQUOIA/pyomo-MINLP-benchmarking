#  MINLP written by GAMS Convert at 08/20/20 01:30:33
#
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         92       84        1        7        0        0        0        0
#
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         98       91        7        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#
#  Nonzero counts
#      Total    const       NL      DLL
#        451      169      282        0
#
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals, bounds=(0, 1), initialize=0.4)
m.x2 = Var(within=Reals, bounds=(0, 1), initialize=0.6)
m.x3 = Var(within=Reals, bounds=(0, 1), initialize=0.4625)
m.x4 = Var(within=Reals, bounds=(0, 1), initialize=0.5375)
m.x5 = Var(within=Reals, bounds=(0, 1), initialize=0.525)
m.x6 = Var(within=Reals, bounds=(0, 1), initialize=0.475)
m.x7 = Var(within=Reals, bounds=(0, 1), initialize=0.5875)
m.x8 = Var(within=Reals, bounds=(0, 1), initialize=0.4125)
m.x9 = Var(within=Reals, bounds=(0, 1), initialize=0.65)
m.x10 = Var(within=Reals, bounds=(0, 1), initialize=0.35)
m.x11 = Var(within=Reals, bounds=(0, 1), initialize=0.7125)
m.x12 = Var(within=Reals, bounds=(0, 1), initialize=0.2875)
m.x13 = Var(within=Reals, bounds=(0, 1), initialize=0.775)
m.x14 = Var(within=Reals, bounds=(0, 1), initialize=0.225)
m.x15 = Var(within=Reals, bounds=(0, 1), initialize=0.8375)
m.x16 = Var(within=Reals, bounds=(0, 1), initialize=0.1625)
m.x17 = Var(within=Reals, bounds=(0, 1), initialize=0.9)
m.x18 = Var(within=Reals, bounds=(0, 1), initialize=0.1)
m.x19 = Var(within=Reals, bounds=(0, 1), initialize=0.2)
m.x20 = Var(within=Reals, bounds=(0, 1), initialize=0.8)
m.x21 = Var(within=Reals, bounds=(0, 1), initialize=0.3)
m.x22 = Var(within=Reals, bounds=(0, 1), initialize=0.7)
m.x23 = Var(within=Reals, bounds=(0, 1), initialize=0.4)
m.x24 = Var(within=Reals, bounds=(0, 1), initialize=0.6)
m.x25 = Var(within=Reals, bounds=(0, 1), initialize=0.5)
m.x26 = Var(within=Reals, bounds=(0, 1), initialize=0.5)
m.x27 = Var(within=Reals, bounds=(0, 1), initialize=0.6)
m.x28 = Var(within=Reals, bounds=(0, 1), initialize=0.4)
m.x29 = Var(within=Reals, bounds=(0, 1), initialize=0.7)
m.x30 = Var(within=Reals, bounds=(0, 1), initialize=0.3)
m.x31 = Var(within=Reals, bounds=(0, 1), initialize=0.8)
m.x32 = Var(within=Reals, bounds=(0, 1), initialize=0.2)
m.x33 = Var(within=Reals, bounds=(0, 1), initialize=0.9)
m.x34 = Var(within=Reals, bounds=(0, 1), initialize=0.1)
m.x35 = Var(within=Reals, bounds=(0, 1), initialize=1)
m.x36 = Var(within=Reals, bounds=(0, 1), initialize=0)
m.x37 = Var(within=Reals, bounds=(0, None), initialize=40)
m.x38 = Var(within=Reals, bounds=(0, None), initialize=127)
m.x39 = Var(within=Reals, bounds=(0, None), initialize=127)
m.x40 = Var(within=Reals, bounds=(0, None), initialize=127)
m.x41 = Var(within=Reals, bounds=(0, None), initialize=127)
m.x42 = Var(within=Reals, bounds=(0, None), initialize=127)
m.x43 = Var(within=Reals, bounds=(0, None), initialize=27)
m.x44 = Var(within=Reals, bounds=(0, None), initialize=27)
m.x45 = Var(within=Reals, bounds=(0, None), initialize=27)
m.x46 = Var(within=Reals, bounds=(0, None), initialize=87)
m.x47 = Var(within=Reals, bounds=(0, None), initialize=87)
m.x48 = Var(within=Reals, bounds=(0, None), initialize=87)
m.x49 = Var(within=Reals, bounds=(0, None), initialize=87)
m.x50 = Var(within=Reals, bounds=(0, None), initialize=87)
m.x51 = Var(within=Reals, bounds=(0, None), initialize=87)
m.x52 = Var(within=Reals, bounds=(0, None), initialize=87)
m.x53 = Var(within=Reals, bounds=(0, None), initialize=87)
m.x54 = Var(within=Reals, bounds=(345, 390), initialize=380)
m.x55 = Var(within=Reals, bounds=(345, 390), initialize=375)
m.x56 = Var(within=Reals, bounds=(345, 390), initialize=372.5)
m.x57 = Var(within=Reals, bounds=(345, 390), initialize=370)
m.x58 = Var(within=Reals, bounds=(345, 390), initialize=367.5)
m.x59 = Var(within=Reals, bounds=(345, 390), initialize=365)
m.x60 = Var(within=Reals, bounds=(345, 390), initialize=362.5)
m.x61 = Var(within=Reals, bounds=(345, 390), initialize=360)
m.x62 = Var(within=Reals, bounds=(345, 390), initialize=355)
m.x63 = Var(within=Reals, bounds=(0, 100), initialize=14.2857142857143)
m.x64 = Var(within=Reals, bounds=(0, 100), initialize=14.2857142857143)
m.x65 = Var(within=Reals, bounds=(0, 100), initialize=14.2857142857143)
m.x66 = Var(within=Reals, bounds=(0, 100), initialize=14.2857142857143)
m.x67 = Var(within=Reals, bounds=(0, 100), initialize=14.2857142857143)
m.x68 = Var(within=Reals, bounds=(0, 100), initialize=14.2857142857143)
m.x69 = Var(within=Reals, bounds=(0, 100), initialize=14.2857142857143)
m.x70 = Var(within=Reals, bounds=(0.1, 0.95), initialize=0.45)
m.x71 = Var(within=Reals, bounds=(50, 80), initialize=60)
m.x72 = Var(within=Reals, bounds=(20, 50), initialize=40)
m.x73 = Var(within=Reals, bounds=(-1.5, -0.496714536653818),
            initialize=-0.954871459437791)
m.x74 = Var(within=Reals, bounds=(-1.5, -0.496714536653818),
            initialize=-0.972170917937763)
m.x75 = Var(within=Reals, bounds=(-1.5, -0.496714536653818),
            initialize=-0.977321724319633)
m.x76 = Var(within=Reals, bounds=(-1.5, -0.496714536653818),
            initialize=-0.982151492959225)
m.x77 = Var(within=Reals, bounds=(-1.5, -0.496714536653818),
            initialize=-0.986662793667597)
m.x78 = Var(within=Reals, bounds=(-1.5, -0.496714536653818),
            initialize=-0.990858232660528)
m.x79 = Var(within=Reals, bounds=(-1.5, -0.496714536653818),
            initialize=-0.994740453837617)
m.x80 = Var(within=Reals, bounds=(-1.5, -0.496714536653818),
            initialize=-0.998312139997537)
m.x81 = Var(within=Reals, bounds=(-1.5, -0.496714536653818),
            initialize=-1.01209290612999)
m.x82 = Var(within=Reals, bounds=(0, 0.151822697193183),
            initialize=0.0971285302367615)
m.x83 = Var(within=Reals, bounds=(0, 0.151822697193183),
            initialize=0.0755763285867959)
m.x84 = Var(within=Reals, bounds=(0, 0.151822697193183),
            initialize=0.0644929360644884)
m.x85 = Var(within=Reals, bounds=(0, 0.151822697193183),
            initialize=0.0538822972811403)
m.x86 = Var(within=Reals, bounds=(0, 0.151822697193183),
            initialize=0.0437417989462674)
m.x87 = Var(within=Reals, bounds=(0, 0.151822697193183),
            initialize=0.0340688284351046)
m.x88 = Var(within=Reals, bounds=(0, 0.151822697193183),
            initialize=0.0248607738701702)
m.x89 = Var(within=Reals, bounds=(0, 0.151822697193183),
            initialize=0.0161150242028288)
m.x90 = Var(within=Reals, bounds=(0, 0.151822697193183), initialize=0)
m.b91 = Var(within=Binary, bounds=(0, 1))
m.b92 = Var(within=Binary, bounds=(0, 1))
m.b93 = Var(within=Binary, bounds=(0, 1))
m.b94 = Var(within=Binary, bounds=(0, 1))
m.b95 = Var(within=Binary, bounds=(0, 1))
m.b96 = Var(within=Binary, bounds=(0, 1))
m.b97 = Var(within=Binary, bounds=(0, 1))

m.obj = Objective(expr=50*m.x70 - m.x71, sense=minimize)

m.c1 = Constraint(expr=-48.9*exp((-3925.690806 + 562.2*(1.33213*(1 - 0.00177872643187478*m.x54)**1.5 + 0.012420366417645
                                                        * m.x54 - 2.62863*(1 - 0.00177872643187478*m.x54)**3 - 3.33399*(1 - 0.00177872643187478*m.x54)**6)
                                  )/m.x54)*m.x1 + 1.2*m.x19 == 0)

m.c2 = Constraint(expr=-41*exp((-4311.896226 + 591.8*(1.38091*(1 - 0.00168976005407232*m.x54)**1.5 + 0.0123117100371747 *
                                                      m.x54 - 2.83433*(1 - 0.00168976005407232*m.x54)**3 - 2.79168*(1 - 0.00168976005407232*m.x54)**6))
                               / m.x54)*m.x2 + 1.2*m.x20 == 0)

m.c3 = Constraint(expr=-48.9*exp((-3925.690806 + 562.2*(1.33213*(1 - 0.00177872643187478*m.x55)**1.5 + 0.012420366417645
                                                        * m.x55 - 2.62863*(1 - 0.00177872643187478*m.x55)**3 - 3.33399*(1 - 0.00177872643187478*m.x55)**6)
                                  )/m.x55)*m.x3 + 1.12*m.x21 == 0)

m.c4 = Constraint(expr=-41*exp((-4311.896226 + 591.8*(1.38091*(1 - 0.00168976005407232*m.x55)**1.5 + 0.0123117100371747 *
                                                      m.x55 - 2.83433*(1 - 0.00168976005407232*m.x55)**3 - 2.79168*(1 - 0.00168976005407232*m.x55)**6))
                               / m.x55)*m.x4 + 1.12*m.x22 == 0)

m.c5 = Constraint(expr=-48.9*exp((-3925.690806 + 562.2*(1.33213*(1 - 0.00177872643187478*m.x56)**1.5 + 0.012420366417645
                                                        * m.x56 - 2.62863*(1 - 0.00177872643187478*m.x56)**3 - 3.33399*(1 - 0.00177872643187478*m.x56)**6)
                                  )/m.x56)*m.x5 + 1.11333333333333*m.x23 == 0)

m.c6 = Constraint(expr=-41*exp((-4311.896226 + 591.8*(1.38091*(1 - 0.00168976005407232*m.x56)**1.5 + 0.0123117100371747 *
                                                      m.x56 - 2.83433*(1 - 0.00168976005407232*m.x56)**3 - 2.79168*(1 - 0.00168976005407232*m.x56)**6))
                               / m.x56)*m.x6 + 1.11333333333333*m.x24 == 0)

m.c7 = Constraint(expr=-48.9*exp((-3925.690806 + 562.2*(1.33213*(1 - 0.00177872643187478*m.x57)**1.5 + 0.012420366417645
                                                        * m.x57 - 2.62863*(1 - 0.00177872643187478*m.x57)**3 - 3.33399*(1 - 0.00177872643187478*m.x57)**6)
                                  )/m.x57)*m.x7 + 1.10666666666667*m.x25 == 0)

m.c8 = Constraint(expr=-41*exp((-4311.896226 + 591.8*(1.38091*(1 - 0.00168976005407232*m.x57)**1.5 + 0.0123117100371747 *
                                                      m.x57 - 2.83433*(1 - 0.00168976005407232*m.x57)**3 - 2.79168*(1 - 0.00168976005407232*m.x57)**6))
                               / m.x57)*m.x8 + 1.10666666666667*m.x26 == 0)

m.c9 = Constraint(expr=-48.9*exp((-3925.690806 + 562.2*(1.33213*(1 - 0.00177872643187478*m.x58)**1.5 + 0.012420366417645
                                                        * m.x58 - 2.62863*(1 - 0.00177872643187478*m.x58)**3 - 3.33399*(1 - 0.00177872643187478*m.x58)**6)
                                  )/m.x58)*m.x9 + 1.1*m.x27 == 0)

m.c10 = Constraint(expr=-41*exp((-4311.896226 + 591.8*(1.38091*(1 - 0.00168976005407232*m.x58)**1.5 + 0.0123117100371747
                                                       * m.x58 - 2.83433*(1 - 0.00168976005407232*m.x58)**3 - 2.79168*(1 - 0.00168976005407232*m.x58)**6
                                                       ))/m.x58)*m.x10 + 1.1*m.x28 == 0)

m.c11 = Constraint(expr=-48.9*exp((-3925.690806 + 562.2*(1.33213*(1 - 0.00177872643187478*m.x59)**1.5 +
                                                         0.012420366417645*m.x59 - 2.62863*(1 - 0.00177872643187478*m.x59)**3 - 3.33399*(1 -
                                                                                                                                         0.00177872643187478*m.x59)**6))/m.x59)*m.x11 + 1.09333333333333*m.x29 == 0)

m.c12 = Constraint(expr=-41*exp((-4311.896226 + 591.8*(1.38091*(1 - 0.00168976005407232*m.x59)**1.5 + 0.0123117100371747
                                                       * m.x59 - 2.83433*(1 - 0.00168976005407232*m.x59)**3 - 2.79168*(1 - 0.00168976005407232*m.x59)**6
                                                       ))/m.x59)*m.x12 + 1.09333333333333*m.x30 == 0)

m.c13 = Constraint(expr=-48.9*exp((-3925.690806 + 562.2*(1.33213*(1 - 0.00177872643187478*m.x60)**1.5 +
                                                         0.012420366417645*m.x60 - 2.62863*(1 - 0.00177872643187478*m.x60)**3 - 3.33399*(1 -
                                                                                                                                         0.00177872643187478*m.x60)**6))/m.x60)*m.x13 + 1.08666666666667*m.x31 == 0)

m.c14 = Constraint(expr=-41*exp((-4311.896226 + 591.8*(1.38091*(1 - 0.00168976005407232*m.x60)**1.5 + 0.0123117100371747
                                                       * m.x60 - 2.83433*(1 - 0.00168976005407232*m.x60)**3 - 2.79168*(1 - 0.00168976005407232*m.x60)**6
                                                       ))/m.x60)*m.x14 + 1.08666666666667*m.x32 == 0)

m.c15 = Constraint(expr=-48.9*exp((-3925.690806 + 562.2*(1.33213*(1 - 0.00177872643187478*m.x61)**1.5 +
                                                         0.012420366417645*m.x61 - 2.62863*(1 - 0.00177872643187478*m.x61)**3 - 3.33399*(1 -
                                                                                                                                         0.00177872643187478*m.x61)**6))/m.x61)*m.x15 + 1.08*m.x33 == 0)

m.c16 = Constraint(expr=-41*exp((-4311.896226 + 591.8*(1.38091*(1 - 0.00168976005407232*m.x61)**1.5 + 0.0123117100371747
                                                       * m.x61 - 2.83433*(1 - 0.00168976005407232*m.x61)**3 - 2.79168*(1 - 0.00168976005407232*m.x61)**6
                                                       ))/m.x61)*m.x16 + 1.08*m.x34 == 0)

m.c17 = Constraint(expr=-48.9*exp((-3925.690806 + 562.2*(1.33213*(1 - 0.00177872643187478*m.x62)**1.5 +
                                                         0.012420366417645*m.x62 - 2.62863*(1 - 0.00177872643187478*m.x62)**3 - 3.33399*(1 -
                                                                                                                                         0.00177872643187478*m.x62)**6))/m.x62)*m.x17 + 1.05*m.x35 == 0)

m.c18 = Constraint(expr=-41*exp((-4311.896226 + 591.8*(1.38091*(1 - 0.00168976005407232*m.x62)**1.5 + 0.0123117100371747
                                                       * m.x62 - 2.83433*(1 - 0.00168976005407232*m.x62)**3 - 2.79168*(1 - 0.00168976005407232*m.x62)**6
                                                       ))/m.x62)*m.x18 + 1.05*m.x36 == 0)

m.c19 = Constraint(expr=- m.x1 - m.x2 + m.x19 + m.x20 == 0)

m.c20 = Constraint(expr=- m.x3 - m.x4 + m.x21 + m.x22 == 0)

m.c21 = Constraint(expr=- m.x5 - m.x6 + m.x23 + m.x24 == 0)

m.c22 = Constraint(expr=- m.x7 - m.x8 + m.x25 + m.x26 == 0)

m.c23 = Constraint(expr=- m.x9 - m.x10 + m.x27 + m.x28 == 0)

m.c24 = Constraint(expr=- m.x11 - m.x12 + m.x29 + m.x30 == 0)

m.c25 = Constraint(expr=- m.x13 - m.x14 + m.x31 + m.x32 == 0)

m.c26 = Constraint(expr=- m.x15 - m.x16 + m.x33 + m.x34 == 0)

m.c27 = Constraint(expr=- m.x17 - m.x18 + m.x35 + m.x36 == 0)

m.c28 = Constraint(expr=m.x38*m.x3 + m.x47*m.x21 - m.x39 *
                   m.x5 - m.x46*m.x19 - 0.7*m.x63 == 0)

m.c29 = Constraint(expr=m.x38*m.x4 + m.x47*m.x22 - m.x39 *
                   m.x6 - m.x46*m.x20 - 0.3*m.x63 == 0)

m.c30 = Constraint(expr=m.x39*m.x5 + m.x48*m.x23 - m.x40 *
                   m.x7 - m.x47*m.x21 - 0.7*m.x64 == 0)

m.c31 = Constraint(expr=m.x39*m.x6 + m.x48*m.x24 - m.x40 *
                   m.x8 - m.x47*m.x22 - 0.3*m.x64 == 0)

m.c32 = Constraint(expr=m.x40*m.x7 + m.x49*m.x25 - m.x41 *
                   m.x9 - m.x48*m.x23 - 0.7*m.x65 == 0)

m.c33 = Constraint(expr=m.x40*m.x8 + m.x49*m.x26 - m.x41 *
                   m.x10 - m.x48*m.x24 - 0.3*m.x65 == 0)

m.c34 = Constraint(expr=m.x41*m.x9 + m.x50*m.x27 - m.x42 *
                   m.x11 - m.x49*m.x25 - 0.7*m.x66 == 0)

m.c35 = Constraint(expr=m.x41*m.x10 + m.x50*m.x28 - m.x42 *
                   m.x12 - m.x49*m.x26 - 0.3*m.x66 == 0)

m.c36 = Constraint(expr=m.x42*m.x11 + m.x51*m.x29 - m.x43 *
                   m.x13 - m.x50*m.x27 - 0.7*m.x67 == 0)

m.c37 = Constraint(expr=m.x42*m.x12 + m.x51*m.x30 - m.x43 *
                   m.x14 - m.x50*m.x28 - 0.3*m.x67 == 0)

m.c38 = Constraint(expr=m.x43*m.x13 + m.x52*m.x31 - m.x44 *
                   m.x15 - m.x51*m.x29 - 0.7*m.x68 == 0)

m.c39 = Constraint(expr=m.x43*m.x14 + m.x52*m.x32 - m.x44 *
                   m.x16 - m.x51*m.x30 - 0.3*m.x68 == 0)

m.c40 = Constraint(expr=m.x44*m.x15 + m.x53*m.x33 - m.x45 *
                   m.x17 - m.x52*m.x31 - 0.7*m.x69 == 0)

m.c41 = Constraint(expr=m.x44*m.x16 + m.x53*m.x34 - m.x45 *
                   m.x18 - m.x52*m.x32 - 0.3*m.x69 == 0)

m.c42 = Constraint(expr=m.x37*m.x1 + m.x46*m.x19 - m.x38*m.x3 == 0)

m.c43 = Constraint(expr=m.x37*m.x2 + m.x46*m.x20 - m.x38*m.x4 == 0)

m.c44 = Constraint(expr=(m.x45 + m.x71)*m.x17 - m.x53*m.x33 == 0)

m.c45 = Constraint(expr=(m.x45 + m.x71)*m.x18 - m.x53*m.x34 == 0)

m.c46 = Constraint(expr=m.x38 - m.x39 - m.x46 + m.x47 - m.x63 == 0)

m.c47 = Constraint(expr=m.x39 - m.x40 - m.x47 + m.x48 - m.x64 == 0)

m.c48 = Constraint(expr=m.x40 - m.x41 - m.x48 + m.x49 - m.x65 == 0)

m.c49 = Constraint(expr=m.x41 - m.x42 - m.x49 + m.x50 - m.x66 == 0)

m.c50 = Constraint(expr=m.x42 - m.x43 - m.x50 + m.x51 - m.x67 == 0)

m.c51 = Constraint(expr=m.x43 - m.x44 - m.x51 + m.x52 - m.x68 == 0)

m.c52 = Constraint(expr=m.x44 - m.x45 - m.x52 + m.x53 - m.x69 == 0)

m.c53 = Constraint(expr=m.x37 - m.x38 + m.x46 == 0)

m.c54 = Constraint(expr=m.x45 - m.x53 + m.x71 == 0)

m.c55 = Constraint(expr=-m.x70*m.x71 + m.x45 == 0)

m.c56 = Constraint(expr=m.x37 - m.x72 == 0)

m.c57 = Constraint(expr=-3.13659116407937e-5*((-46242.079590558 + (-33.92 + (0.23695 + m.x54*(-0.000100566666666667 +
                                                                                              1.7825e-8*m.x54))*m.x54)*m.x54 + 4674.1308*(1.33213*(1 - 0.00177872643187478*m.x54)**1.5 +
                                                                                                                                          0.012420366417645*m.x54 - 2.62863*(1 - 0.00177872643187478*m.x54)**3 - 3.33399*(1 -
                                                                                                                                                                                                                          0.00177872643187478*m.x54)**6) + (-58.05441722 + 8.314*(1.998195*(1 - 0.00177872643187478*m.x54)
                                                                                                                                                                                                                                                                                  ** 0.5 - 7.88589*(1 - 0.00177872643187478*m.x54)**2 - 20.00394*(1 - 0.00177872643187478*m.x54)**5
                                                                                                                                                                                                                                                                                  ))*m.x54)*m.x1 + (-55570.3234397208 + (-24.35 + (0.25625 + m.x54*(-9.21666666666667e-5 +
                                                                                                                                                                                                                                                                                                                                                    1.22775e-8*m.x54))*m.x54)*m.x54 + 4920.2252*(1.38091*(1 - 0.00168976005407232*m.x54)**1.5 +
                                                                                                                                                                                                                                                                                                                                                                                                 0.0123117100371747*m.x54 - 2.83433*(1 - 0.00168976005407232*m.x54)**3 - 2.79168*(1 -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  0.00168976005407232*m.x54)**6) + (-60.57638598 + 8.314*(2.071365*(1 - 0.00168976005407232*m.x54)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ** 0.5 - 8.50299*(1 - 0.00168976005407232*m.x54)**2 - 16.75008*(1 - 0.00168976005407232*m.x54)**5
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ))*m.x54)*m.x2) + m.x73 == 0)

m.c58 = Constraint(expr=-3.13659116407937e-5*((-46242.079590558 + (-33.92 + (0.23695 + m.x55*(-0.000100566666666667 +
                                                                                              1.7825e-8*m.x55))*m.x55)*m.x55 + 4674.1308*(1.33213*(1 - 0.00177872643187478*m.x55)**1.5 +
                                                                                                                                          0.012420366417645*m.x55 - 2.62863*(1 - 0.00177872643187478*m.x55)**3 - 3.33399*(1 -
                                                                                                                                                                                                                          0.00177872643187478*m.x55)**6) + (-58.05441722 + 8.314*(1.998195*(1 - 0.00177872643187478*m.x55)
                                                                                                                                                                                                                                                                                  ** 0.5 - 7.88589*(1 - 0.00177872643187478*m.x55)**2 - 20.00394*(1 - 0.00177872643187478*m.x55)**5
                                                                                                                                                                                                                                                                                  ))*m.x55)*m.x3 + (-55570.3234397208 + (-24.35 + (0.25625 + m.x55*(-9.21666666666667e-5 +
                                                                                                                                                                                                                                                                                                                                                    1.22775e-8*m.x55))*m.x55)*m.x55 + 4920.2252*(1.38091*(1 - 0.00168976005407232*m.x55)**1.5 +
                                                                                                                                                                                                                                                                                                                                                                                                 0.0123117100371747*m.x55 - 2.83433*(1 - 0.00168976005407232*m.x55)**3 - 2.79168*(1 -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  0.00168976005407232*m.x55)**6) + (-60.57638598 + 8.314*(2.071365*(1 - 0.00168976005407232*m.x55)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ** 0.5 - 8.50299*(1 - 0.00168976005407232*m.x55)**2 - 16.75008*(1 - 0.00168976005407232*m.x55)**5
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ))*m.x55)*m.x4) + m.x74 == 0)

m.c59 = Constraint(expr=-3.13659116407937e-5*((-46242.079590558 + (-33.92 + (0.23695 + m.x56*(-0.000100566666666667 +
                                                                                              1.7825e-8*m.x56))*m.x56)*m.x56 + 4674.1308*(1.33213*(1 - 0.00177872643187478*m.x56)**1.5 +
                                                                                                                                          0.012420366417645*m.x56 - 2.62863*(1 - 0.00177872643187478*m.x56)**3 - 3.33399*(1 -
                                                                                                                                                                                                                          0.00177872643187478*m.x56)**6) + (-58.05441722 + 8.314*(1.998195*(1 - 0.00177872643187478*m.x56)
                                                                                                                                                                                                                                                                                  ** 0.5 - 7.88589*(1 - 0.00177872643187478*m.x56)**2 - 20.00394*(1 - 0.00177872643187478*m.x56)**5
                                                                                                                                                                                                                                                                                  ))*m.x56)*m.x5 + (-55570.3234397208 + (-24.35 + (0.25625 + m.x56*(-9.21666666666667e-5 +
                                                                                                                                                                                                                                                                                                                                                    1.22775e-8*m.x56))*m.x56)*m.x56 + 4920.2252*(1.38091*(1 - 0.00168976005407232*m.x56)**1.5 +
                                                                                                                                                                                                                                                                                                                                                                                                 0.0123117100371747*m.x56 - 2.83433*(1 - 0.00168976005407232*m.x56)**3 - 2.79168*(1 -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  0.00168976005407232*m.x56)**6) + (-60.57638598 + 8.314*(2.071365*(1 - 0.00168976005407232*m.x56)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ** 0.5 - 8.50299*(1 - 0.00168976005407232*m.x56)**2 - 16.75008*(1 - 0.00168976005407232*m.x56)**5
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ))*m.x56)*m.x6) + m.x75 == 0)

m.c60 = Constraint(expr=-3.13659116407937e-5*((-46242.079590558 + (-33.92 + (0.23695 + m.x57*(-0.000100566666666667 +
                                                                                              1.7825e-8*m.x57))*m.x57)*m.x57 + 4674.1308*(1.33213*(1 - 0.00177872643187478*m.x57)**1.5 +
                                                                                                                                          0.012420366417645*m.x57 - 2.62863*(1 - 0.00177872643187478*m.x57)**3 - 3.33399*(1 -
                                                                                                                                                                                                                          0.00177872643187478*m.x57)**6) + (-58.05441722 + 8.314*(1.998195*(1 - 0.00177872643187478*m.x57)
                                                                                                                                                                                                                                                                                  ** 0.5 - 7.88589*(1 - 0.00177872643187478*m.x57)**2 - 20.00394*(1 - 0.00177872643187478*m.x57)**5
                                                                                                                                                                                                                                                                                  ))*m.x57)*m.x7 + (-55570.3234397208 + (-24.35 + (0.25625 + m.x57*(-9.21666666666667e-5 +
                                                                                                                                                                                                                                                                                                                                                    1.22775e-8*m.x57))*m.x57)*m.x57 + 4920.2252*(1.38091*(1 - 0.00168976005407232*m.x57)**1.5 +
                                                                                                                                                                                                                                                                                                                                                                                                 0.0123117100371747*m.x57 - 2.83433*(1 - 0.00168976005407232*m.x57)**3 - 2.79168*(1 -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  0.00168976005407232*m.x57)**6) + (-60.57638598 + 8.314*(2.071365*(1 - 0.00168976005407232*m.x57)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ** 0.5 - 8.50299*(1 - 0.00168976005407232*m.x57)**2 - 16.75008*(1 - 0.00168976005407232*m.x57)**5
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ))*m.x57)*m.x8) + m.x76 == 0)

m.c61 = Constraint(expr=-3.13659116407937e-5*((-46242.079590558 + (-33.92 + (0.23695 + m.x58*(-0.000100566666666667 +
                                                                                              1.7825e-8*m.x58))*m.x58)*m.x58 + 4674.1308*(1.33213*(1 - 0.00177872643187478*m.x58)**1.5 +
                                                                                                                                          0.012420366417645*m.x58 - 2.62863*(1 - 0.00177872643187478*m.x58)**3 - 3.33399*(1 -
                                                                                                                                                                                                                          0.00177872643187478*m.x58)**6) + (-58.05441722 + 8.314*(1.998195*(1 - 0.00177872643187478*m.x58)
                                                                                                                                                                                                                                                                                  ** 0.5 - 7.88589*(1 - 0.00177872643187478*m.x58)**2 - 20.00394*(1 - 0.00177872643187478*m.x58)**5
                                                                                                                                                                                                                                                                                  ))*m.x58)*m.x9 + (-55570.3234397208 + (-24.35 + (0.25625 + m.x58*(-9.21666666666667e-5 +
                                                                                                                                                                                                                                                                                                                                                    1.22775e-8*m.x58))*m.x58)*m.x58 + 4920.2252*(1.38091*(1 - 0.00168976005407232*m.x58)**1.5 +
                                                                                                                                                                                                                                                                                                                                                                                                 0.0123117100371747*m.x58 - 2.83433*(1 - 0.00168976005407232*m.x58)**3 - 2.79168*(1 -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  0.00168976005407232*m.x58)**6) + (-60.57638598 + 8.314*(2.071365*(1 - 0.00168976005407232*m.x58)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ** 0.5 - 8.50299*(1 - 0.00168976005407232*m.x58)**2 - 16.75008*(1 - 0.00168976005407232*m.x58)**5
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ))*m.x58)*m.x10) + m.x77 == 0)

m.c62 = Constraint(expr=-3.13659116407937e-5*((-46242.079590558 + (-33.92 + (0.23695 + m.x59*(-0.000100566666666667 +
                                                                                              1.7825e-8*m.x59))*m.x59)*m.x59 + 4674.1308*(1.33213*(1 - 0.00177872643187478*m.x59)**1.5 +
                                                                                                                                          0.012420366417645*m.x59 - 2.62863*(1 - 0.00177872643187478*m.x59)**3 - 3.33399*(1 -
                                                                                                                                                                                                                          0.00177872643187478*m.x59)**6) + (-58.05441722 + 8.314*(1.998195*(1 - 0.00177872643187478*m.x59)
                                                                                                                                                                                                                                                                                  ** 0.5 - 7.88589*(1 - 0.00177872643187478*m.x59)**2 - 20.00394*(1 - 0.00177872643187478*m.x59)**5
                                                                                                                                                                                                                                                                                  ))*m.x59)*m.x11 + (-55570.3234397208 + (-24.35 + (0.25625 + m.x59*(-9.21666666666667e-5 +
                                                                                                                                                                                                                                                                                                                                                     1.22775e-8*m.x59))*m.x59)*m.x59 + 4920.2252*(1.38091*(1 - 0.00168976005407232*m.x59)**1.5 +
                                                                                                                                                                                                                                                                                                                                                                                                  0.0123117100371747*m.x59 - 2.83433*(1 - 0.00168976005407232*m.x59)**3 - 2.79168*(1 -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   0.00168976005407232*m.x59)**6) + (-60.57638598 + 8.314*(2.071365*(1 - 0.00168976005407232*m.x59)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ** 0.5 - 8.50299*(1 - 0.00168976005407232*m.x59)**2 - 16.75008*(1 - 0.00168976005407232*m.x59)**5
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ))*m.x59)*m.x12) + m.x78 == 0)

m.c63 = Constraint(expr=-3.13659116407937e-5*((-46242.079590558 + (-33.92 + (0.23695 + m.x60*(-0.000100566666666667 +
                                                                                              1.7825e-8*m.x60))*m.x60)*m.x60 + 4674.1308*(1.33213*(1 - 0.00177872643187478*m.x60)**1.5 +
                                                                                                                                          0.012420366417645*m.x60 - 2.62863*(1 - 0.00177872643187478*m.x60)**3 - 3.33399*(1 -
                                                                                                                                                                                                                          0.00177872643187478*m.x60)**6) + (-58.05441722 + 8.314*(1.998195*(1 - 0.00177872643187478*m.x60)
                                                                                                                                                                                                                                                                                  ** 0.5 - 7.88589*(1 - 0.00177872643187478*m.x60)**2 - 20.00394*(1 - 0.00177872643187478*m.x60)**5
                                                                                                                                                                                                                                                                                  ))*m.x60)*m.x13 + (-55570.3234397208 + (-24.35 + (0.25625 + m.x60*(-9.21666666666667e-5 +
                                                                                                                                                                                                                                                                                                                                                     1.22775e-8*m.x60))*m.x60)*m.x60 + 4920.2252*(1.38091*(1 - 0.00168976005407232*m.x60)**1.5 +
                                                                                                                                                                                                                                                                                                                                                                                                  0.0123117100371747*m.x60 - 2.83433*(1 - 0.00168976005407232*m.x60)**3 - 2.79168*(1 -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   0.00168976005407232*m.x60)**6) + (-60.57638598 + 8.314*(2.071365*(1 - 0.00168976005407232*m.x60)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ** 0.5 - 8.50299*(1 - 0.00168976005407232*m.x60)**2 - 16.75008*(1 - 0.00168976005407232*m.x60)**5
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ))*m.x60)*m.x14) + m.x79 == 0)

m.c64 = Constraint(expr=-3.13659116407937e-5*((-46242.079590558 + (-33.92 + (0.23695 + m.x61*(-0.000100566666666667 +
                                                                                              1.7825e-8*m.x61))*m.x61)*m.x61 + 4674.1308*(1.33213*(1 - 0.00177872643187478*m.x61)**1.5 +
                                                                                                                                          0.012420366417645*m.x61 - 2.62863*(1 - 0.00177872643187478*m.x61)**3 - 3.33399*(1 -
                                                                                                                                                                                                                          0.00177872643187478*m.x61)**6) + (-58.05441722 + 8.314*(1.998195*(1 - 0.00177872643187478*m.x61)
                                                                                                                                                                                                                                                                                  ** 0.5 - 7.88589*(1 - 0.00177872643187478*m.x61)**2 - 20.00394*(1 - 0.00177872643187478*m.x61)**5
                                                                                                                                                                                                                                                                                  ))*m.x61)*m.x15 + (-55570.3234397208 + (-24.35 + (0.25625 + m.x61*(-9.21666666666667e-5 +
                                                                                                                                                                                                                                                                                                                                                     1.22775e-8*m.x61))*m.x61)*m.x61 + 4920.2252*(1.38091*(1 - 0.00168976005407232*m.x61)**1.5 +
                                                                                                                                                                                                                                                                                                                                                                                                  0.0123117100371747*m.x61 - 2.83433*(1 - 0.00168976005407232*m.x61)**3 - 2.79168*(1 -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   0.00168976005407232*m.x61)**6) + (-60.57638598 + 8.314*(2.071365*(1 - 0.00168976005407232*m.x61)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ** 0.5 - 8.50299*(1 - 0.00168976005407232*m.x61)**2 - 16.75008*(1 - 0.00168976005407232*m.x61)**5
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ))*m.x61)*m.x16) + m.x80 == 0)

m.c65 = Constraint(expr=-3.13659116407937e-5*((-46242.079590558 + (-33.92 + (0.23695 + m.x62*(-0.000100566666666667 +
                                                                                              1.7825e-8*m.x62))*m.x62)*m.x62 + 4674.1308*(1.33213*(1 - 0.00177872643187478*m.x62)**1.5 +
                                                                                                                                          0.012420366417645*m.x62 - 2.62863*(1 - 0.00177872643187478*m.x62)**3 - 3.33399*(1 -
                                                                                                                                                                                                                          0.00177872643187478*m.x62)**6) + (-58.05441722 + 8.314*(1.998195*(1 - 0.00177872643187478*m.x62)
                                                                                                                                                                                                                                                                                  ** 0.5 - 7.88589*(1 - 0.00177872643187478*m.x62)**2 - 20.00394*(1 - 0.00177872643187478*m.x62)**5
                                                                                                                                                                                                                                                                                  ))*m.x62)*m.x17 + (-55570.3234397208 + (-24.35 + (0.25625 + m.x62*(-9.21666666666667e-5 +
                                                                                                                                                                                                                                                                                                                                                     1.22775e-8*m.x62))*m.x62)*m.x62 + 4920.2252*(1.38091*(1 - 0.00168976005407232*m.x62)**1.5 +
                                                                                                                                                                                                                                                                                                                                                                                                  0.0123117100371747*m.x62 - 2.83433*(1 - 0.00168976005407232*m.x62)**3 - 2.79168*(1 -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   0.00168976005407232*m.x62)**6) + (-60.57638598 + 8.314*(2.071365*(1 - 0.00168976005407232*m.x62)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ** 0.5 - 8.50299*(1 - 0.00168976005407232*m.x62)**2 - 16.75008*(1 - 0.00168976005407232*m.x62)**5
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ))*m.x62)*m.x18) + m.x81 == 0)

m.c66 = Constraint(expr=-3.13659116407937e-5*((-13603.886229474 + (-33.92 + (0.23695 + m.x54*(-0.000100566666666667 +
                                                                                              1.7825e-8*m.x54))*m.x54)*m.x54)*m.x19 + (-19721.2182167568 + (-24.35 + (0.25625 + m.x54*(-
                                                                                                                                                                                       9.21666666666667e-5 + 1.22775e-8*m.x54))*m.x54)*m.x54)*m.x20) + m.x82 == 0)

m.c67 = Constraint(expr=-3.13659116407937e-5*((-13603.886229474 + (-33.92 + (0.23695 + m.x55*(-0.000100566666666667 +
                                                                                              1.7825e-8*m.x55))*m.x55)*m.x55)*m.x21 + (-19721.2182167568 + (-24.35 + (0.25625 + m.x55*(-
                                                                                                                                                                                       9.21666666666667e-5 + 1.22775e-8*m.x55))*m.x55)*m.x55)*m.x22) + m.x83 == 0)

m.c68 = Constraint(expr=-3.13659116407937e-5*((-13603.886229474 + (-33.92 + (0.23695 + m.x56*(-0.000100566666666667 +
                                                                                              1.7825e-8*m.x56))*m.x56)*m.x56)*m.x23 + (-19721.2182167568 + (-24.35 + (0.25625 + m.x56*(-
                                                                                                                                                                                       9.21666666666667e-5 + 1.22775e-8*m.x56))*m.x56)*m.x56)*m.x24) + m.x84 == 0)

m.c69 = Constraint(expr=-3.13659116407937e-5*((-13603.886229474 + (-33.92 + (0.23695 + m.x57*(-0.000100566666666667 +
                                                                                              1.7825e-8*m.x57))*m.x57)*m.x57)*m.x25 + (-19721.2182167568 + (-24.35 + (0.25625 + m.x57*(-
                                                                                                                                                                                       9.21666666666667e-5 + 1.22775e-8*m.x57))*m.x57)*m.x57)*m.x26) + m.x85 == 0)

m.c70 = Constraint(expr=-3.13659116407937e-5*((-13603.886229474 + (-33.92 + (0.23695 + m.x58*(-0.000100566666666667 +
                                                                                              1.7825e-8*m.x58))*m.x58)*m.x58)*m.x27 + (-19721.2182167568 + (-24.35 + (0.25625 + m.x58*(-
                                                                                                                                                                                       9.21666666666667e-5 + 1.22775e-8*m.x58))*m.x58)*m.x58)*m.x28) + m.x86 == 0)

m.c71 = Constraint(expr=-3.13659116407937e-5*((-13603.886229474 + (-33.92 + (0.23695 + m.x59*(-0.000100566666666667 +
                                                                                              1.7825e-8*m.x59))*m.x59)*m.x59)*m.x29 + (-19721.2182167568 + (-24.35 + (0.25625 + m.x59*(-
                                                                                                                                                                                       9.21666666666667e-5 + 1.22775e-8*m.x59))*m.x59)*m.x59)*m.x30) + m.x87 == 0)

m.c72 = Constraint(expr=-3.13659116407937e-5*((-13603.886229474 + (-33.92 + (0.23695 + m.x60*(-0.000100566666666667 +
                                                                                              1.7825e-8*m.x60))*m.x60)*m.x60)*m.x31 + (-19721.2182167568 + (-24.35 + (0.25625 + m.x60*(-
                                                                                                                                                                                       9.21666666666667e-5 + 1.22775e-8*m.x60))*m.x60)*m.x60)*m.x32) + m.x88 == 0)

m.c73 = Constraint(expr=-3.13659116407937e-5*((-13603.886229474 + (-33.92 + (0.23695 + m.x61*(-0.000100566666666667 +
                                                                                              1.7825e-8*m.x61))*m.x61)*m.x61)*m.x33 + (-19721.2182167568 + (-24.35 + (0.25625 + m.x61*(-
                                                                                                                                                                                       9.21666666666667e-5 + 1.22775e-8*m.x61))*m.x61)*m.x61)*m.x34) + m.x89 == 0)

m.c74 = Constraint(expr=-3.13659116407937e-5*((-13603.886229474 + (-33.92 + (0.23695 + m.x62*(-0.000100566666666667 +
                                                                                              1.7825e-8*m.x62))*m.x62)*m.x62)*m.x35 + (-19721.2182167568 + (-24.35 + (0.25625 + m.x62*(-
                                                                                                                                                                                       9.21666666666667e-5 + 1.22775e-8*m.x62))*m.x62)*m.x62)*m.x36) + m.x90 == 0)

m.c75 = Constraint(expr=m.x38*m.x74 + m.x47*m.x83 - m.x39 *
                   m.x75 - m.x46*m.x82 + 0.999444137682208*m.x63 == 0)

m.c76 = Constraint(expr=m.x39*m.x75 + m.x48*m.x84 - m.x40 *
                   m.x76 - m.x47*m.x83 + 0.999444137682208*m.x64 == 0)

m.c77 = Constraint(expr=m.x40*m.x76 + m.x49*m.x85 - m.x41 *
                   m.x77 - m.x48*m.x84 + 0.999444137682208*m.x65 == 0)

m.c78 = Constraint(expr=m.x41*m.x77 + m.x50*m.x86 - m.x42 *
                   m.x78 - m.x49*m.x85 + 0.999444137682208*m.x66 == 0)

m.c79 = Constraint(expr=m.x42*m.x78 + m.x51*m.x87 - m.x43 *
                   m.x79 - m.x50*m.x86 + 0.999444137682208*m.x67 == 0)

m.c80 = Constraint(expr=m.x43*m.x79 + m.x52*m.x88 - m.x44 *
                   m.x80 - m.x51*m.x87 + 0.999444137682208*m.x68 == 0)

m.c81 = Constraint(expr=m.x44*m.x80 + m.x53*m.x89 - m.x45 *
                   m.x81 - m.x52*m.x88 + 0.999444137682208*m.x69 == 0)

m.c82 = Constraint(expr=m.x17 >= 0.95)

m.c83 = Constraint(expr=m.x63 + m.x64 + m.x65 +
                   m.x66 + m.x67 + m.x68 + m.x69 == 100)

m.c84 = Constraint(expr=m.b91 + m.b92 + m.b93 +
                   m.b94 + m.b95 + m.b96 + m.b97 == 1)

m.c85 = Constraint(expr=m.x63 - 100*m.b91 <= 0)

m.c86 = Constraint(expr=m.x64 - 100*m.b92 <= 0)

m.c87 = Constraint(expr=m.x65 - 100*m.b93 <= 0)

m.c88 = Constraint(expr=m.x66 - 100*m.b94 <= 0)

m.c89 = Constraint(expr=m.x67 - 100*m.b95 <= 0)

m.c90 = Constraint(expr=m.x68 - 100*m.b96 <= 0)

m.c91 = Constraint(expr=m.x69 - 100*m.b97 <= 0)
