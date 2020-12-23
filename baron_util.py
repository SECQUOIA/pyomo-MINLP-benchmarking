import time
import os
import cplex
from pyomo.environ import *
# Euler
special_baron_path = "/home/canl1/work/SAAOA/baron4ieg"
# Local
# special_baron_path = "~/opt/baron4ieg"


def add_baron_cuts(model):
    timea = time.time()
    output_filename, symbol_map, var_ids = model.baronwrite(
        "root_relaxation_baron.bar", format="bar")
    os.system("sed -i '1 a dolocal:0; ' root_relaxation_baron.bar")
    os.system("sed -i '1 a numloc:0; ' root_relaxation_baron.bar")
    os.system("sed -i '1 a maxtime:10000; ' root_relaxation_baron.bar")
    # os.system("sed -i '1 a prlevel:0; ' root_relaxation_baron.bar")
    os.system("sed -i '1 a ppdo:0; ' root_relaxation_baron.bar")
    os.system("sed -i '1 a pscdo:0; ' root_relaxation_baron.bar")
    os.system('''sed -i '1 a CplexLibName: "/opt/ibm/ILOG/CPLEX_Studio129/cplex/bin/x86-64_linux/libcplex1290.so"; ' root_relaxation_baron.bar''')
    # os.system('''sed -i '1 a CplexLibName: "/Users/zedongpeng/opt/CPLEX_Studio1210/cplex/bin/x86-64_osx/libcplex12100.dylib"; ' root_relaxation_baron.bar''')

    os.system(special_baron_path + " root_relaxation_baron.bar")
    cplex_model = cplex.Cplex("relax.lp")

    timeb = time.time()
    print("lp file generation time", timeb - timea)
    # create additional variables in the pyomo model
    var_names = cplex_model.variables.get_names()
    num_bar_vars = sum("bar_var" in var for var in var_names)
    model.bar_set = RangeSet(num_bar_vars)
    model.bar_var = Var(model.bar_set)

    # create a map from cplex var id to pyomo var name
    varid_to_var = {}
    bar_var_indices = []
    # print('len(var_ids): ', len(var_ids))
    for vid in var_ids:
        name = symbol_map.byObject[vid]
        var_data = symbol_map.bySymbol[name]()
        varid_cplex = cplex_model.variables.get_indices(name)
        varid_to_var[varid_cplex] = var_data
    # print(varid_to_var)

    cplex_var_names = cplex_model.variables.get_names()
    # print('cplex_var_names: ', cplex_var_names)
    for i in range(len(cplex_var_names)):
        varname = cplex_var_names[i]
        # print(varname, end=' ')
        if "bar_var" in varname:
            # print('Yes')
            varid_pyomo = int(varname.split("bar_var")[1])
            varid_to_var[i] = model.bar_var[varid_pyomo]
            bar_var_indices.append(i)

    # update variable bounds in pyomo
    var_lb = cplex_model.variables.get_lower_bounds()
    var_ub = cplex_model.variables.get_upper_bounds()
    for i in range(len(var_lb)):
        if i in varid_to_var:
            var = varid_to_var[i]
            var.setlb(var_lb[i])
            var.setub(var_ub[i])
    # #To create a list that contain information of the linear constraints in the original pyomo model
    # for c in model.component_objects(Constraint):

    # add constraints that have bar_var
    model.baroncuts = ConstraintList()
    nconstraints = cplex_model.linear_constraints.get_num()
    # print('nconstraints', nconstraints)
    # print('nvariables', cplex_model.variables.get_num())
    for c in range(nconstraints):
        row = cplex_model.linear_constraints.get_rows(c)
        rhs = cplex_model.linear_constraints.get_rhs(c)
        sense = cplex_model.linear_constraints.get_senses(c)
        if sum(varid in bar_var_indices for varid in row.ind) > 0:
            # print(len(row.ind))
            # for i in range(len(row.ind)):
            #     print('i ', i)
            #     print('row.val[i] ', row.val[i])
            #     print('row.ind[i] ', row.ind[i])
            #     print('varid_to_var', varid_to_var)
            #     print(len(varid_to_var))
            #     print('varid_to_var[row.ind[i]] ', varid_to_var[row.ind[i]])
            expr = sum(row.val[i] * varid_to_var[row.ind[i]]
                       for i in range(len(row.ind)))
            if sense == 'G':
                model.baroncuts.add(expr >= rhs)
            if sense == 'L':
                model.baroncuts.add(expr <= rhs)
            if sense == 'E':
                model.baroncuts.add(expr == rhs)
    # change objective
    # model.obj.deactivate()
    next(model.component_data_objects(Objective, active=True)).deactivate()
    coeff = cplex_model.objective.get_linear()
    if cplex_model.objective.get_sense() == 1:
        model.baron_obj = Objective(expr=sum(varid_to_var[i] * coeff[i] for i in range(
            cplex_model.variables.get_num()) if i in varid_to_var.keys()), sense=minimize)
    else:
        model.baron_obj = Objective(expr=sum(varid_to_var[i] * coeff[i] for i in range(
            cplex_model.variables.get_num()) if i in varid_to_var.keys()), sense=maximize)

    timec = time.time()
    print("time to add the cuts to pyomo model", timec-timeb)


def solve_relaxed_baron_model(model):
    output_filename, symbol_map, var_ids = model.baronwrite(
        "root_relaxation_baron.bar", format="bar")
    os.system("sed -i '1 a dolocal:0; ' root_relaxation_baron.bar")
    os.system("sed -i '1 a numloc:0; ' root_relaxation_baron.bar")
    os.system("sed -i '1 a maxtime:10000; ' root_relaxation_baron.bar")
    os.system("sed -i '1 a prlevel:1; ' root_relaxation_baron.bar")
    os.system('''sed -i '1 a CplexLibName: "/opt/ibm/ILOG/CPLEX_Studio129/cplex/bin/x86-64_linux/libcplex1290.so"; ' root_relaxation_baron.bar''')
    os.system(special_baron_path + " root_relaxation_baron.bar")
    cplex_model = cplex.Cplex("relax.lp")
    cplex_model.solve()
