import os
import sys
import logging
from datetime import datetime
from util.julian_datetime import get_julian_datetime
from csv import writer as csv_writer
from argparse import ArgumentParser
from contextlib import contextmanager
from importlib import import_module
from pyomo.environ import SolverFactory
from pyomo.opt import SolverStatus
from pyomo.opt import TerminationCondition as tc
from util.parse_to_gams import (termination_condition_to_gams_format,
                                solver_status_to_gams, obj_to_gams_format, objest_to_gams_format)
from util.gams_optionfile import gams_optionfile
from datetime import datetime
import sys
import json
sys.setrecursionlimit(100000)


def parse_command_line_arguments():
    parser = ArgumentParser(
        description='Benchmark specified solver on problem files')
    parser.add_argument('--redo-existing', dest='skip_existing', default=True,
                        action='store_const', const=False,
                        help='Redo benchmark if result file is already existing')
    parser.add_argument('--no-skip-failed', dest='skip_failed', default=True,
                        action='store_const', const=False,
                        help="Skip file if file in 'failed_models.txt'")
    parser.add_argument('--solver', dest='solver_name', type=str, required=True,
                        metavar='solver_name',
                        choices=['baron', 'mindtpy', 'feas-pump', 'gams', 'couenne'])
    parser.add_argument('--gams-solver', dest='gams_solver_name', type=str, required=False,
                        metavar='gams_solver_name')
    parser.add_argument('--gams-solver-optionfile', dest='gams_solver_optionfile', type=str, required=False,
                        metavar='gams_solver_optionfile')
    parser.add_argument('--strategy', dest='solver_strategy', type=str,
                        required=False, metavar='solver_strategy', default="OA",
                        help='Solver strategy (if applicable)')
    parser.add_argument('--init-strategy', dest='init_strategy', type=str,
                        required=False, metavar='init_strategy',
                        help='Initialization strategy (if applicable)')
    parser.add_argument('--timelimit', dest='timelimit', type=int,
                        required=False, metavar='timelimit', default=60,
                        help='Time limit (sec) for each model')
    parser.add_argument('--model-dir', dest='model_dir', default='models',
                        required=False, metavar='model_dir',
                        help='Directory where models are stored as .py files')
    parser.add_argument('--single-tree', dest='single_tree', default=False,
                        action='store_const', const=True,
                        help='Call single-tree implementation of MindtPy')
    parser.add_argument('--feasibility-norm', dest='feasibility_norm', type=str, default='L_infinity',
                        required=False, metavar='feasibility_norm', choices=['L1', 'L2', 'L_infinity'])
    parser.add_argument('--stalling-limit', dest='stalling_limit', type=int,
                        required=False, metavar='stalling_limit', default=15,
                        help='Stalling limit for each model')
    parser.add_argument('--ecp-tolerance', dest='ecp_tolerance', type=float,
                        required=False, metavar='ecp_tolerance', default=1e-4,
                        help='Feasibility tolerance used to determine the stopping criterion in the ECP method.')
    parser.add_argument('--differentiate-mode', dest='differentiate_mode', type=str, default="reverse_symbolic",
                        required=False, metavar='differentiate_mode', choices=["reverse_symbolic", "sympy"])
    parser.add_argument('--mip-solver', dest='mip_solver', type=str, default='cplex',
                        required=False, metavar='mip_solver')
    parser.add_argument('--mip-regularization-solver', dest='mip_regularization_solver', type=str, default=None,
                        required=False, metavar='mip_regularization_solver')
    parser.add_argument('--linearize-inactive', dest='linearize_inactive', default=False,
                        action='store_const', const=True,
                        help='Add OA cuts for all constriants no matter active or inactive')
    parser.add_argument('--nlp-solver', dest='nlp_solver', type=str, default='ipopt',
                        required=False, metavar='nlp_solver')
    parser.add_argument('--method-name', dest='method_name', type=str, default='',
                        required=False, metavar='method_name')
    parser.add_argument('--iteration-limit', dest='iteration_limit', type=int, default=30,
                        required=False, metavar='iteration_limit')
    parser.add_argument('--solver-tee', dest='solver_tee', default=False,
                        action='store_const', const=True,
                        help='Output the log of nlp and mip solvers')
    parser.add_argument('--mip-solver-args', dest='mip_solver_args', type=str, default='',
                        required=False, metavar='mip_solver_args')
    parser.add_argument('--nlp-solver-args', dest='nlp_solver_args', type=str, default='',
                        required=False, metavar='nlp_solver_args')
    parser.add_argument('--threads', dest='threads', type=int,
                        required=False, metavar='threads', default=0,
                        help='Threads for mip solver')
    parser.add_argument('--skip-folder', dest='skip_floder', type=str, default='',
                        required=False, metavar='skip_floder')
    parser.add_argument('--add-slack', dest='add_slack', default=False,
                        action='store_const', const=True,
                        help='activate add_slack option')
    parser.add_argument('--equality-relaxation', dest='equality_relaxation', default=False,
                        action='store_const', const=True,
                        help='activate equality_relaxation option')
    parser.add_argument('--result-folder', dest='result_floder', type=str, default='',
                        required=False, metavar='result_floder')
    parser.add_argument('--add-regularization', dest='add_regularization', type=str, default=None,
                        required=False, metavar='add_regularization')
    parser.add_argument('--add-no-good-cuts', dest='add_no_good_cuts', default=False,
                        action='store_const', const=True,
                        help='Add integer cuts (no-good cuts) to binary variables to disallow same integer solution again.')
    parser.add_argument('--not-add-cuts-at-incumbent', dest='add_cuts_at_incumbent', default=True,
                        action='store_const', const=False,
                        help='Add integer cuts (no-good cuts) to binary variables to disallow same integer solution again.')
    parser.add_argument('--new-folder-when-skip', dest='new_folder_when_skip', default=False,
                        action='store_const', const=True,
                        help='whether create new folder when skip folder is provided')
    parser.add_argument('--level-coef', dest='level_coef', type=float,
                        required=False, metavar='level_coef', default=0.5,
                        help='Feasibility tolerance used to determine the stopping criterion in the ECP method.')
    parser.add_argument('--sqp-lag-scaling-coef', dest='sqp_lag_scaling_coef', type=str, default=None,
                        required=False, metavar='sqp_lag_scaling_coef', choices=['fixed', 'variable_dependent'])
    parser.add_argument('--use-tabu-list', dest='use_tabu_list', default=False,
                        action='store_const', const=True,
                        help='whether use tabu list')
    return parser.parse_args()


@contextmanager
def redirect_stdout(ofile_obj):
    original_stdout = sys.stdout
    sys.stdout = ofile_obj
    yield
    sys.stdout = original_stdout


@contextmanager
def load_model(model_name):
    global model_scope
    model_scope = import_module(model_name)
    yield
    del model_scope


def construct_trace_data(opt, results):
    problem = results['Problem'][0]
    solver = results['Solver'][0]
    if args.solver_name in ['mindtpy', 'gdpopt', 'gams', 'couenne']:
        trace_data = [
            model_name,  # GAMS model filename
            'MINLP',     # LP, MIP, NLP, etc.
            solver['Name'] + ("_singletree_" if args.single_tree ==
                              True else "_")+args.method_name,
            args.nlp_solver,  # default NLP solver
            args.mip_solver,  # default MIP solver
            get_julian_datetime(datetime.now()),  # start day/time of job
            # direction 0=min, 1=max
            0 if (problem['Sense'] ==
                  1 or problem['Sense'] == 'minimize') else 1,
            # total number of equations
            results['Problem'][0]['Number of constraints'],
            # total number of variables
            results['Problem'][0]['Number of variables'],
            results['Problem'][0]['Number of binary variables'] + \
            results['Problem'][0]['Number of integer variables'],  # total number of discrete variables
            '',  # 'nznum?',  # number of nonzeros
            '',  # 'nlz?',  # number of nonlinear nonzeros
            0,  # 1= optfile included
            # GAMS model return status - see the GAMS return codes section.
            termination_condition_to_gams_format(
                solver.Termination_condition, problem),
            # GAMS solver return status - see the GAMS return codes section.
            solver_status_to_gams(
                solver.Status, solver.Termination_condition, problem),
            obj_to_gams_format(problem),
            objest_to_gams_format(problem),
            solver['Wallclock time'],  # resource time used (sec)
            # number of solver iterations
            solver['Iterations'] if args.single_tree == False else solver['Num nodes'],
            0,  # dom used
            0,  # nodes used
            '# best solution found at ' + \
                str(solver['Best solution found time']) + ' seconds' + \
            '. fixed nlp time: ' + str(solver['Timing']['fixed subproblem']) + \
            '. mip time: ' + str(solver['Timing']['master']) + \
            '. initialization time: ' + str(solver['Timing']['initialization']) + \
            '. OA cut time: ' + str(solver['Timing']['OA cut generation']) + \
            '. Affine cut generation time: ' + str(solver['Timing']['Affine cut generation']) + \
            '. Nogood cut generation time: ' + str(solver['Timing']['Nogood cut generation']) + \
            '. ECP cut generation time: ' + str(solver['Timing']['ECP cut generation']) + \
            '. Regularization master time: ' + str(solver['Timing']['regularization master']) + \
            '. fp master time: ' + str(solver['Timing']['fp master']) + \
            '. fp master time: ' + str(solver['Timing']['fp subproblem']) + \
            '. PyomoNLP time: ' + str(solver['Timing']['PyomoNLP']) + \
            '. Number of infeasible nlp subproblems: ' + \
                str(solver['Num infeasible nlp subproblem'])
        ]
        return trace_data


def benchmark_model(timelimit):
    if args.solver_name == 'couenne':
        opt = SolverFactory(args.solver_name, executable='~/couenne')
    else:
        opt = SolverFactory(args.solver_name)
    try:
        with open(result_file, 'w') as result_file_obj, redirect_stdout(result_file_obj):
            if args.solver_name == 'mindtpy':
                opt.CONFIG.logger.propagate = False
                opt.CONFIG.logger.addHandler(logging.FileHandler(
                    sys.stdout.name, mode=sys.stdout.mode))
                opt.CONFIG.logger.info('--------Yes--------')
            model = model_scope.m
            if args.gams_solver_optionfile is not None:
                print('Use optionfile')
                print(args.gams_solver_name +
                      '-'+args.gams_solver_optionfile)

            if args.solver_name == 'baron':  # baron
                results = opt.solve(
                    model, tee=True, time_limit=timelimit, threads=args.threads)
            if args.solver_name == 'couenne':
                results = opt.solve(
                    model, tee=True, timelimit=timelimit)
            elif args.solver_name == 'gams':
                results = opt.solve(
                    model, solver=args.gams_solver_name, tee=True, tracefile=trace_file,
                    # io_options={'output_filename': model.name},
                    add_options=gams_optionfile[args.gams_solver_name if args.gams_solver_optionfile is None else args.gams_solver_name+'-'+args.gams_solver_optionfile])
            else:  # MindtPy
                results = opt.solve(model, tee=True, time_limit=timelimit,
                                    mip_solver=args.mip_solver,
                                    nlp_solver=args.nlp_solver,
                                    mip_regularization_solver=args.mip_regularization_solver,
                                    strategy=args.solver_strategy,
                                    feasibility_norm=args.feasibility_norm,
                                    differentiate_mode=args.differentiate_mode,
                                    linearize_inactive=args.linearize_inactive,
                                    single_tree=args.single_tree,
                                    iteration_limit=args.iteration_limit,
                                    solver_tee=args.solver_tee,
                                    mip_solver_args=json.loads(
                                        args.mip_solver_args) if args.mip_solver_args != '' else {},
                                    nlp_solver_args=json.loads(
                                        args.nlp_solver_args) if args.nlp_solver_args != '' else {},
                                    threads=args.threads,
                                    stalling_limit=args.stalling_limit,
                                    ecp_tolerance=args.ecp_tolerance,
                                    init_strategy=args.init_strategy,
                                    add_slack=args.add_slack,
                                    equality_relaxation=args.equality_relaxation,
                                    add_regularization=args.add_regularization,
                                    add_no_good_cuts=args.add_no_good_cuts,
                                    add_cuts_at_incumbent=args.add_cuts_at_incumbent,
                                    level_coef=args.level_coef,
                                    sqp_lag_scaling_coef=args.sqp_lag_scaling_coef,
                                    use_tabu_list=args.use_tabu_list
                                    )
        with open(result_file, 'a') as result_file_obj, redirect_stdout(result_file_obj):
            print('\n-------Result-------')
            print(results)
            print('args.mip_solver: ', args.mip_solver)
            print('args.init_strategy: ', args.init_strategy)
            print('args.nlp_solver: ', args.nlp_solver)
            print('args.solver_strategy: ', args.solver_strategy)
            print('args.feasibility_norm: ', args.feasibility_norm)
            print('args.differentiate_mode: ', args.differentiate_mode)
            print('args.linearize_inactive: ', args.linearize_inactive)
            print('args.single_tree: ', args.single_tree)
            print('args.iteration_limit: ', args.iteration_limit)
            print('args.solver_tee: ', args.solver_tee)
            print('args.mip_solver_args: ', args.mip_solver_args)
            print('args.nlp_solver_args: ', args.nlp_solver_args)
            print('args.threads: ', args.threads)
            print('args.stalling_limit: ', args.stalling_limit)
            print('args.ecp_tolerance: ', args.ecp_tolerance)
            print('args.add_slack: ', args.add_slack)

        solving_time = results.Solver[0].Wallclock_time
        if results.Solver[0].Termination_condition == tc.optimal:
            solving_times.append([model_name, solving_time])
        elif results.Solver[0].Termination_condition == tc.maxTimeLimit:
            solving_times.append([model_name, 'maxTimeLimit'])
        elif results.Solver[0].Termination_condition == tc.maxIterations:
            solving_times.append([model_name, 'maxIterations'])
        if args.solver_name == 'mindtpy':
            trace_data = construct_trace_data(opt, results)
            if args.solver_name == 'mindtpy':
                with open(trace_file, 'w') as trace_file_obj:
                    trace_file_obj.write(', '.join(str(el)
                                                   for el in trace_data) + '\n')

    except Exception as e:
        error_file_obj.write(model_file+'\n')
        print(f"Failed to solve '{model_file}'", file=sys.stderr)
        print(e, file=sys.stderr)
        print(f"File written to '{error_file}'", file=sys.stderr)
    if args.solver_name == 'mindtpy':
        del opt.CONFIG.logger.handlers[0]


if __name__ == '__main__':
    args = parse_command_line_arguments()
    current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    ####### SETUP (directories and files) #######
    sys.path.insert(0, './'+args.model_dir)  # necessary to import models

    if not os.path.exists('results'):
        print("Creating new directory: './results'")
        os.makedirs('results')
    if args.result_floder != '':
        if not os.path.exists('results/'+args.result_floder):
            print("Creating " + args.result_floder + " under results folder")
            os.makedirs('results'+args.result_floder)

    # Set various filenames
    model_files = [model_file for model_file in sorted(
        os.listdir(args.model_dir)) if model_file.endswith('.py')]
    if args.skip_floder != '' and args.new_folder_when_skip is False:
        solver_dir = args.skip_floder

    else:
        solver_dir = ((args.result_floder + '/') if args.result_floder != '' else '') + \
            args.solver_name + (f"-{args.gams_solver_name}" if args.gams_solver_name else "") +\
            (f"-{args.gams_solver_optionfile}" if args.gams_solver_optionfile else "") + \
            (f"-{args.solver_strategy}" if args.solver_strategy and args.solver_name == 'mindtpy' else "") + \
            ("-singletree-" if args.single_tree else "-") + current_time
    error_file = f"./results/{solver_dir}/failed_models.txt"
    solving_times_file = f"./results/{solver_dir}/solving_times.csv"
    if not os.path.exists('./results/'+solver_dir):
        print(f"Creating new directory: './results/{solver_dir}'")
        os.makedirs('./results/'+solver_dir)

    # Load previously failed model (or create empty file)
    prev_failed_models = set()
    try:
        with open(f"./results/{args.skip_floder}/failed_models.txt", 'r') as error_file_obj:
            for line in error_file_obj:
                prev_failed_models.add(line.strip())
    except FileNotFoundError:
        with open(error_file, 'a'):
            pass

    solving_times = [['Instance name', 'Average solving time']]

    print('################################')
    print(f"Benchmarking solver '{args.solver_name}' " +
          ("with strategy '{args.solver_strategy}'" if args.solver_strategy else ""))
    print(f"Writing to './results/{solver_dir}'")
    print(f"Failed model files will be written to '{error_file}'")
    print(f"Solving times will be written to '{solving_times_file}'")
    print('################################')

    for model_file in model_files:
        model_name, _ = os.path.splitext(model_file)  # removes ending
        result_file = './results/'+solver_dir+'/'+model_name+'.txt'
        if args.solver_name == 'mindtpy':
            trace_file = './results/'+solver_dir+'/'+model_name+'.trc'
        elif args.solver_name == 'gams':
            trace_file = os.path.dirname(os.path.abspath(
                __file__)) + '/results/'+solver_dir+'/'+model_name+'.trc'
        sys.stdout = sys.__stdout__
        if args.skip_existing and os.path.exists('./results/'+args.skip_floder+'/'+model_name+'.trc'):
            print(f"Skipping '{trace_file}'")
            print(
                "File exists already, please use the '--redo-existing' flag to override")
            continue

        elif args.skip_failed and model_file in prev_failed_models:
            print(f"Skipping '{trace_file}'")
            print(
                "File listed in 'failed_models.txt', please use the '--no-skip-failed' flag to override")
            continue

        else:
            print(f"Benchmarking '{model_file}'")
            # This causes all stdout to be written to the results file
            # and the model to be loaded as model_scope.m
            with open(error_file, 'a') as error_file_obj, load_model(model_name):
                benchmark_model(args.timelimit)

    with open(solving_times_file, 'w') as time_file:
        time_writer = csv_writer(time_file)
        time_writer.writerows(solving_times)
