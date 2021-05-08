general_option = ('option MIP = CPLEX;'
                  'option NLP = IPOPTH;'
                  'option threads = 1;'
                  'option optcr = 0.001;'
                  'option optca = 0.0;'
                  'GAMS_MODEL.nodLim = 1E8;'
                  'option domLim = 1E8;'
                  'option iterLim = 1E8;'
                  'option resLim = 900;')

gams_optionfile = {
    'bonminh-B-BB': [
        general_option +
        'GAMS_MODEL.optfile = 1;'
        '\n'
        '$onecho > bonminh.opt \n'
        'bonmin.algorithm B-BB \n'
        'milp_solver CPLEX\n'
        'bonmin.time_limit 900\n'
        '$offecho'
    ],
    'bonminh-B-HYB': [
        general_option +
        'GAMS_MODEL.optfile = 2;'
        '\n'
        '$onecho > bonminh.op2 \n'
        'bonmin.algorithm B-HYB \n'
        'milp_solver CPLEX\n'
        'bonmin.time_limit 900\n'
        '$offecho'
    ],
    'bonminh-B-OA': [
        general_option +
        'GAMS_MODEL.optfile = 3;'
        '\n'
        '$onecho > bonminh.op3 \n'
        'bonmin.algorithm B-OA \n'
        'milp_solver CPLEX\n'
        'bonmin.time_limit 900\n'
        '$offecho'
    ],
    'AlphaECP': [
        general_option +
        'GAMS_MODEL.optfile = 1;'
        '\n'
        '$onecho > AlphaECP.opt \n'
        'ECPmaster 1 \n'
        'TOLepsg 1E-6\n'
        '$offecho'
    ],
    'dicopt': [
        general_option +
        'GAMS_MODEL.optfile = 1;'
        '\n'
        '$onecho > dicopt.opt \n'
        'convex 1 \n'
        'stop 1 \n'
        'maxcycles 1E8\n'
        'infeasder 1\n'
        '$offecho'
    ],
    'sbb': [
        general_option +
        'GAMS_MODEL.optfile = 1;'
        '\n'
        '$onecho > sbb.opt \n'
        'memnodes 5E7\n'
        '$offecho'
    ],
    'scip': [
        general_option
        #  +
        # 'GAMS_MODEL.optfile = 1;'
        # '\n'
        # '$onecho > scip.opt \n'
        # 'constraints/nonlinear/assumeconvex True\n'
        # '$offecho'
    ],
    'SHOT-multi-tree': [
        general_option +
        'GAMS_MODEL.optfile = 1;'
        '\n'
        '$onecho > shot.opt \n'
        'Dual.MIP.NumberOfThreads 1\n'
        'Dual.MIP.Solver 0\n'
        'Primal.FixedInteger.Solver 2\n'
        'Subsolver.GAMS.NLP.Solver ipopth\n'
        'Termination.ObjectiveGap.Absolute 0\n'
        'Termination.ObjectiveGap.Relative 0.001\n'
        'Termination.TimeLimit 900\n'
        'Dual.TreeStrategy 1\n'
        '$offecho'
    ],
    'SHOT-single-tree': [
        general_option +
        'GAMS_MODEL.optfile = 2;'
        '\n'
        '$onecho > shot.op2 \n'
        'Dual.MIP.NumberOfThreads 1\n'
        'Dual.MIP.Solver 0\n'
        'Primal.FixedInteger.Solver 2\n'
        'Subsolver.GAMS.NLP.Solver ipopth\n'
        'Termination.ObjectiveGap.Absolute 0\n'
        'Termination.ObjectiveGap.Relative 0.001\n'
        'Termination.TimeLimit 900\n'
        'Dual.TreeStrategy 0\n'
        '$offecho'
    ],
    'baron': [
        general_option
    ],
    'antigone': [
        general_option
    ],
    'Couenne': [
        general_option +
        'GAMS_MODEL.optfile = 1;'
        '\n'
        '$onecho > Couenne.opt \n'
        'lp_solver Clp\n'
        '$offecho'
    ],
    'KNITRO': [
        general_option +
        'GAMS_MODEL.optfile = 1;'
        '\n'
        '$onecho > KNITRO.opt \n'
        'mip_method 2\n'
        '$offecho'
    ],
    'LINDO': [
        general_option +
        'GAMS_MODEL.optfile = 1;'
        '\n'
        '$onecho > LINDO.opt \n'
        'USEGOP 0\n'
        'SPLEX_ITRLMT -1\n'
        'MIP_ITRLIM -1\n'
        '$offecho'
    ],
    'lindoglobal': [
        general_option +
        'GAMS_MODEL.optfile = 1;'
        '\n'
        '$onecho > LINDO.opt \n'
        'SPLEX_ITRLMT -1\n'
        'MIP_ITRLIM -1\n'
        '$offecho'
    ]
}
