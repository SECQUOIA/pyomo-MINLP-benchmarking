#  MINLP written by GAMS Convert at 05/15/20 00:51:12
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         12       10        2        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         18       10        0        8        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         43       27       16        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.i10 = Var(within=Integers,bounds=(0,100000),initialize=0)
m.i11 = Var(within=Integers,bounds=(0,32000),initialize=0)
m.i12 = Var(within=Integers,bounds=(0,78000),initialize=0)
m.i13 = Var(within=Integers,bounds=(0,56000),initialize=0)
m.i14 = Var(within=Integers,bounds=(0,43000),initialize=0)
m.i15 = Var(within=Integers,bounds=(0,100000),initialize=0)
m.i16 = Var(within=Integers,bounds=(0,55000),initialize=0)
m.i17 = Var(within=Integers,bounds=(0,78000),initialize=0)

m.obj = Objective(expr=   m.x9, sense=minimize)

m.c2 = Constraint(expr=1.07813636363636*m.x1 - sqrt(0.0476190476190476*(-0.00313636363636371*m.x1 - 0.150909090909091*
                       m.x2 - 0.267772727272727*m.x3 - 0.308636363636363*m.x4 - 0.423318181818182*m.x5 - 
                       0.0687727272727274*m.x6 - 0.290227272727273*m.x7 + 0.548045454545455*m.x8)**2 + 
                       0.0476190476190476*(0.0058636363636364*m.x1 - 0.0729090909090906*m.x2 - 0.384772727272727*m.x3 - 
                       0.407636363636363*m.x4 - 0.459318181818182*m.x5 - 0.0897727272727273*m.x6 - 0.373227272727273*
                       m.x7 + 0.593045454545455*m.x8)**2 + 0.0476190476190476*(-0.0171363636363637*m.x1 - 
                       0.0369090909090906*m.x2 + 0.251227272727273*m.x3 + 0.261363636363637*m.x4 + 0.196681818181818*
                       m.x5 + 0.0312272727272727*m.x6 + 0.212772727272727*m.x7 - 0.368954545454545*m.x8)**2 + 
                       0.0476190476190476*(0.0820909090909094*m.x2 - 0.0261363636363636*m.x1 + 0.116227272727273*m.x3 + 
                       0.142363636363637*m.x4 + 0.158681818181818*m.x5 + 0.0642272727272726*m.x6 - 0.116227272727273*
                       m.x7 - 0.168954545454545*m.x8)**2 + 0.0476190476190476*(-0.0231363636363637*m.x1 - 
                       0.0909090909090906*m.x2 - 0.193772727272727*m.x3 - 0.149636363636363*m.x4 - 0.0283181818181817*
                       m.x5 - 0.0617727272727273*m.x6 + 0.0397727272727273*m.x7 + 0.0710454545454546*m.x8)**2 + 
                       0.0476190476190476*(-0.00113636363636371*m.x1 - 0.110909090909091*m.x2 - 0.0557727272727273*m.x3
                        - 0.0306363636363634*m.x4 + 0.0246818181818182*m.x5 - 0.0797727272727273*m.x6 + 
                       0.184772727272727*m.x7 + 0.166045454545455*m.x8)**2 + 0.0476190476190476*(0.0308636363636363*m.x1
                        - 0.114909090909091*m.x2 + 0.0642272727272726*m.x3 + 0.132363636363637*m.x4 + 0.185681818181818*
                       m.x5 - 0.0687727272727274*m.x6 - 0.0932272727272727*m.x7 + 1.08304545454545*m.x8)**2 + 
                       0.0476190476190476*(0.0488636363636363*m.x1 - 0.145909090909091*m.x2 + 0.203227272727273*m.x3 + 
                       0.213363636363637*m.x4 + 0.245681818181818*m.x5 - 0.0607727272727274*m.x6 + 0.0847727272727272*
                       m.x7 + 0.167045454545455*m.x8)**2 + 0.0476190476190476*(0.0778636363636362*m.x1 - 
                       0.0899090909090907*m.x2 - 0.170772727272727*m.x3 - 0.160636363636363*m.x4 - 0.131318181818182*
                       m.x5 - 0.0187727272727274*m.x6 - 0.164227272727273*m.x7 - 0.440954545454545*m.x8)**2 + 
                       0.0476190476190476*(0.0388636363636363*m.x1 + 0.372090909090909*m.x2 + 0.0952272727272727*m.x3 + 
                       0.0633636363636367*m.x4 + 0.0916818181818184*m.x5 + 0.219227272727273*m.x6 - 0.160227272727273*
                       m.x7 - 0.0449545454545452*m.x8)**2 + 0.0476190476190476*(0.0138636363636364*m.x1 - 
                       0.107909090909091*m.x2 + 0.104227272727273*m.x3 + 0.111363636363637*m.x4 + 0.0956818181818184*
                       m.x5 - 0.0117727272727273*m.x6 + 0.0957727272727273*m.x7 - 0.256954545454545*m.x8)**2 + 
                       0.0476190476190476*(0.0248636363636363*m.x1 + 0.0660909090909094*m.x2 - 0.0587727272727274*m.x3
                        - 0.0936363636363633*m.x4 - 0.218318181818182*m.x5 + 0.0582272727272726*m.x6 - 
                       0.0672272727272727*m.x7 - 0.303954545454545*m.x8)**2 + 0.0476190476190476*(0.0018636363636364*
                       m.x1 + 0.273090909090909*m.x2 + 0.196227272727273*m.x3 + 0.202363636363637*m.x4 + 
                       0.211681818181818*m.x5 + 0.121227272727273*m.x6 + 0.420772727272727*m.x7 - 0.122954545454545*m.x8
                       )**2 + 0.0476190476190476*(0.216090909090909*m.x2 - 0.0151363636363637*m.x1 + 0.0662272727272726*
                       m.x3 + 0.0373636363636367*m.x4 - 0.0353181818181816*m.x5 + 0.0642272727272726*m.x6 + 
                       0.552772727272727*m.x7 + 0.0870454545454546*m.x8)**2 + 0.0476190476190476*(-0.0171363636363637*
                       m.x1 - 0.167909090909091*m.x2 - 0.0677727272727273*m.x3 - 0.100636363636363*m.x4 - 
                       0.162318181818182*m.x5 - 0.0687727272727274*m.x6 + 0.104772727272727*m.x7 + 0.115045454545455*
                       m.x8)**2 + 0.0476190476190476*(-0.00713636363636372*m.x1 - 0.00690909090909053*m.x2 + 
                       0.0452272727272727*m.x3 + 0.0553636363636367*m.x4 + 0.0436818181818184*m.x5 - 0.0157727272727273*
                       m.x6 + 0.141772727272727*m.x7 - 0.267954545454545*m.x8)**2 + 0.0476190476190476*(
                       0.0088636363636363*m.x1 + 0.119090909090909*m.x2 + 0.196227272727273*m.x3 + 0.168363636363637*
                       m.x4 + 0.0826818181818183*m.x5 + 0.0502272727272726*m.x6 - 0.0362272727272728*m.x7 - 
                       0.151954545454545*m.x8)**2 + 0.0476190476190476*(0.0018636363636364*m.x1 - 0.0389090909090906*
                       m.x2 - 0.151772727272727*m.x3 - 0.185636363636363*m.x4 - 0.291318181818182*m.x5 - 
                       0.00877272727272738*m.x6 - 0.375227272727273*m.x7 - 0.206954545454545*m.x8)**2 + 
                       0.0476190476190476*(0.100090909090909*m.x2 - 0.0211363636363637*m.x1 + 0.184227272727273*m.x3 + 
                       0.218363636363637*m.x4 + 0.472681818181818*m.x5 + 0.0692272727272727*m.x6 - 0.0202272727272728*
                       m.x7 - 0.170954545454545*m.x8)**2 + 0.0476190476190476*(-0.0421363636363636*m.x1 - 
                       0.0139090909090906*m.x2 - 0.0437727272727273*m.x3 - 0.0336363636363632*m.x4 + 0.0526818181818183*
                       m.x5 - 0.0157727272727273*m.x6 - 0.263227272727273*m.x7 - 0.202954545454545*m.x8)**2 + 
                       0.0476190476190476*(0.124090909090909*m.x2 - 0.0471363636363638*m.x1 - 0.0197727272727273*m.x3 - 
                       0.0106363636363633*m.x4 + 0.0406818181818183*m.x5 + 0.0182272727272728*m.x6 + 0.184772727272727*
                       m.x7 + 0.0170454545454546*m.x8)**2 + 0.0476190476190476*(-0.0331363636363637*m.x1 - 
                       0.203909090909091*m.x2 - 0.107772727272727*m.x3 - 0.124636363636363*m.x4 - 0.153318181818182*m.x5
                        - 0.126772727272727*m.x6 - 0.0632272727272727*m.x7 - 0.138954545454545*m.x8)**2) + 
                       1.09290909090909*m.x2 + 1.11977272727273*m.x3 + 1.12363636363636*m.x4 + 1.12131818181818*m.x5 + 
                       1.09177272727273*m.x6 + 1.14122727272727*m.x7 + 1.12895454545455*m.x8 >= 0.05)

m.c3 = Constraint(expr=-sqrt(0.0476190476190476*(-0.00313636363636371*m.x1 - 0.150909090909091*m.x2 - 0.267772727272727*
                       m.x3 - 0.308636363636363*m.x4 - 0.423318181818182*m.x5 - 0.0687727272727274*m.x6 - 
                       0.290227272727273*m.x7 + 0.548045454545455*m.x8)**2 + 0.0476190476190476*(0.0058636363636364*m.x1
                        - 0.0729090909090906*m.x2 - 0.384772727272727*m.x3 - 0.407636363636363*m.x4 - 0.459318181818182*
                       m.x5 - 0.0897727272727273*m.x6 - 0.373227272727273*m.x7 + 0.593045454545455*m.x8)**2 + 
                       0.0476190476190476*(-0.0171363636363637*m.x1 - 0.0369090909090906*m.x2 + 0.251227272727273*m.x3
                        + 0.261363636363637*m.x4 + 0.196681818181818*m.x5 + 0.0312272727272727*m.x6 + 0.212772727272727*
                       m.x7 - 0.368954545454545*m.x8)**2 + 0.0476190476190476*(0.0820909090909094*m.x2 - 
                       0.0261363636363636*m.x1 + 0.116227272727273*m.x3 + 0.142363636363637*m.x4 + 0.158681818181818*
                       m.x5 + 0.0642272727272726*m.x6 - 0.116227272727273*m.x7 - 0.168954545454545*m.x8)**2 + 
                       0.0476190476190476*(-0.0231363636363637*m.x1 - 0.0909090909090906*m.x2 - 0.193772727272727*m.x3
                        - 0.149636363636363*m.x4 - 0.0283181818181817*m.x5 - 0.0617727272727273*m.x6 + 
                       0.0397727272727273*m.x7 + 0.0710454545454546*m.x8)**2 + 0.0476190476190476*(-0.00113636363636371*
                       m.x1 - 0.110909090909091*m.x2 - 0.0557727272727273*m.x3 - 0.0306363636363634*m.x4 + 
                       0.0246818181818182*m.x5 - 0.0797727272727273*m.x6 + 0.184772727272727*m.x7 + 0.166045454545455*
                       m.x8)**2 + 0.0476190476190476*(0.0308636363636363*m.x1 - 0.114909090909091*m.x2 + 
                       0.0642272727272726*m.x3 + 0.132363636363637*m.x4 + 0.185681818181818*m.x5 - 0.0687727272727274*
                       m.x6 - 0.0932272727272727*m.x7 + 1.08304545454545*m.x8)**2 + 0.0476190476190476*(
                       0.0488636363636363*m.x1 - 0.145909090909091*m.x2 + 0.203227272727273*m.x3 + 0.213363636363637*
                       m.x4 + 0.245681818181818*m.x5 - 0.0607727272727274*m.x6 + 0.0847727272727272*m.x7 + 
                       0.167045454545455*m.x8)**2 + 0.0476190476190476*(0.0778636363636362*m.x1 - 0.0899090909090907*
                       m.x2 - 0.170772727272727*m.x3 - 0.160636363636363*m.x4 - 0.131318181818182*m.x5 - 
                       0.0187727272727274*m.x6 - 0.164227272727273*m.x7 - 0.440954545454545*m.x8)**2 + 
                       0.0476190476190476*(0.0388636363636363*m.x1 + 0.372090909090909*m.x2 + 0.0952272727272727*m.x3 + 
                       0.0633636363636367*m.x4 + 0.0916818181818184*m.x5 + 0.219227272727273*m.x6 - 0.160227272727273*
                       m.x7 - 0.0449545454545452*m.x8)**2 + 0.0476190476190476*(0.0138636363636364*m.x1 - 
                       0.107909090909091*m.x2 + 0.104227272727273*m.x3 + 0.111363636363637*m.x4 + 0.0956818181818184*
                       m.x5 - 0.0117727272727273*m.x6 + 0.0957727272727273*m.x7 - 0.256954545454545*m.x8)**2 + 
                       0.0476190476190476*(0.0248636363636363*m.x1 + 0.0660909090909094*m.x2 - 0.0587727272727274*m.x3
                        - 0.0936363636363633*m.x4 - 0.218318181818182*m.x5 + 0.0582272727272726*m.x6 - 
                       0.0672272727272727*m.x7 - 0.303954545454545*m.x8)**2 + 0.0476190476190476*(0.0018636363636364*
                       m.x1 + 0.273090909090909*m.x2 + 0.196227272727273*m.x3 + 0.202363636363637*m.x4 + 
                       0.211681818181818*m.x5 + 0.121227272727273*m.x6 + 0.420772727272727*m.x7 - 0.122954545454545*m.x8
                       )**2 + 0.0476190476190476*(0.216090909090909*m.x2 - 0.0151363636363637*m.x1 + 0.0662272727272726*
                       m.x3 + 0.0373636363636367*m.x4 - 0.0353181818181816*m.x5 + 0.0642272727272726*m.x6 + 
                       0.552772727272727*m.x7 + 0.0870454545454546*m.x8)**2 + 0.0476190476190476*(-0.0171363636363637*
                       m.x1 - 0.167909090909091*m.x2 - 0.0677727272727273*m.x3 - 0.100636363636363*m.x4 - 
                       0.162318181818182*m.x5 - 0.0687727272727274*m.x6 + 0.104772727272727*m.x7 + 0.115045454545455*
                       m.x8)**2 + 0.0476190476190476*(-0.00713636363636372*m.x1 - 0.00690909090909053*m.x2 + 
                       0.0452272727272727*m.x3 + 0.0553636363636367*m.x4 + 0.0436818181818184*m.x5 - 0.0157727272727273*
                       m.x6 + 0.141772727272727*m.x7 - 0.267954545454545*m.x8)**2 + 0.0476190476190476*(
                       0.0088636363636363*m.x1 + 0.119090909090909*m.x2 + 0.196227272727273*m.x3 + 0.168363636363637*
                       m.x4 + 0.0826818181818183*m.x5 + 0.0502272727272726*m.x6 - 0.0362272727272728*m.x7 - 
                       0.151954545454545*m.x8)**2 + 0.0476190476190476*(0.0018636363636364*m.x1 - 0.0389090909090906*
                       m.x2 - 0.151772727272727*m.x3 - 0.185636363636363*m.x4 - 0.291318181818182*m.x5 - 
                       0.00877272727272738*m.x6 - 0.375227272727273*m.x7 - 0.206954545454545*m.x8)**2 + 
                       0.0476190476190476*(0.100090909090909*m.x2 - 0.0211363636363637*m.x1 + 0.184227272727273*m.x3 + 
                       0.218363636363637*m.x4 + 0.472681818181818*m.x5 + 0.0692272727272727*m.x6 - 0.0202272727272728*
                       m.x7 - 0.170954545454545*m.x8)**2 + 0.0476190476190476*(-0.0421363636363636*m.x1 - 
                       0.0139090909090906*m.x2 - 0.0437727272727273*m.x3 - 0.0336363636363632*m.x4 + 0.0526818181818183*
                       m.x5 - 0.0157727272727273*m.x6 - 0.263227272727273*m.x7 - 0.202954545454545*m.x8)**2 + 
                       0.0476190476190476*(0.124090909090909*m.x2 - 0.0471363636363638*m.x1 - 0.0197727272727273*m.x3 - 
                       0.0106363636363633*m.x4 + 0.0406818181818183*m.x5 + 0.0182272727272728*m.x6 + 0.184772727272727*
                       m.x7 + 0.0170454545454546*m.x8)**2 + 0.0476190476190476*(-0.0331363636363637*m.x1 - 
                       0.203909090909091*m.x2 - 0.107772727272727*m.x3 - 0.124636363636363*m.x4 - 0.153318181818182*m.x5
                        - 0.126772727272727*m.x6 - 0.0632272727272727*m.x7 - 0.138954545454545*m.x8)**2) + m.x9 >= 0)

m.c4 = Constraint(expr=   m.x1 + m.x2 + m.x3 + m.x4 + m.x5 + m.x6 + m.x7 + m.x8 == 1)

m.c5 = Constraint(expr= - 100000*m.x1 + m.i10 == 0)

m.c6 = Constraint(expr= - 32000*m.x2 + m.i11 == 0)

m.c7 = Constraint(expr= - 78000*m.x3 + m.i12 == 0)

m.c8 = Constraint(expr= - 56000*m.x4 + m.i13 == 0)

m.c9 = Constraint(expr= - 43000*m.x5 + m.i14 == 0)

m.c10 = Constraint(expr= - 100000*m.x6 + m.i15 == 0)

m.c11 = Constraint(expr= - 55000*m.x7 + m.i16 == 0)

m.c12 = Constraint(expr= - 78000*m.x8 + m.i17 == 0)
