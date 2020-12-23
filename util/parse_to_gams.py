from pyomo.opt import TerminationCondition
from pyomo.opt import SolverStatus
from pyomo.opt.base import problem


def obj_to_gams_format(problem):
    """
    docstring
    """
    if (problem['Sense'] == 1 or problem['Sense'] == 'minimize'):
        if problem['Upper bound'] != float('inf'):
            return problem['Upper bound']
        else:
            return 'NA'
    else:
        if problem['Lower bound'] != float('inf'):
            return problem['Lower bound']
        else:
            return 'NA'


def objest_to_gams_format(problem):
    """
    docstring
    """
    if (problem['Sense'] == 1 or problem['Sense'] == 'minimize'):
        if problem['Lower bound'] != float('inf'):
            return problem['Lower bound']
        else:
            return 'NA'
    else:
        if problem['Upper bound'] != float('inf'):
            return problem['Upper bound']
        else:
            return 'NA'


def termination_condition_to_gams_format(tc, problem):
    """Converts termination condition to Gams 'MODEL STATUS CODE'
        http://www.gamsworld.org/performance/status_codes.htm
    """

    if tc is TerminationCondition.unknown:
        return 12
    if tc is TerminationCondition.maxTimeLimit:
        if problem['Sense'] == 1 or problem['Sense'] == 'minimize':
            if problem['Upper bound'] in {float('inf'), float('-inf')}:
                return 14
            else:
                return 8
        else:
            if problem['Lower bound'] in {float('inf'), float('-inf')}:
                return 14
            else:
                return 8
    if tc is TerminationCondition.maxIterations:
        return 2
    if tc is TerminationCondition.minFunctionValue:
        return 1
    if tc is TerminationCondition.minStepLength:
        return 16
    if tc is TerminationCondition.globallyOptimal:
        return 1
    if tc is TerminationCondition.locallyOptimal:
        return 2
    if tc is TerminationCondition.feasible:
        return 8
    if tc is TerminationCondition.optimal:
        return 1
    if tc is TerminationCondition.maxEvaluations:
        return 13
    if tc is TerminationCondition.other:
        return 14
    if tc is TerminationCondition.unbounded:
        return 3
    if tc is TerminationCondition.infeasible:
        return 4
    if tc is TerminationCondition.infeasibleOrUnbounded:
        return 4
    if tc is TerminationCondition.invalidProblem:
        return 13
    if tc is TerminationCondition.intermediateNonInteger:
        return 6
    if tc is TerminationCondition.noSolution:
        return 13
    if tc is TerminationCondition.solverFailure:
        return 12
    if tc is TerminationCondition.internalSolverError:
        return 12
    if tc is TerminationCondition.error:
        return 12
    if tc is TerminationCondition.userInterrupt:
        return 8
    if tc is TerminationCondition.resourceInterrupt:
        return 3
    if tc is TerminationCondition.licensingProblems:
        return 11


def solver_status_to_gams(ss, tc, problem):
    """Converts solution status to Gams 'SOLVER STATUS CODE'
        http://www.gamsworld.org/performance/status_codes.htm
    """
    if ss == SolverStatus.ok:       # Normal termination
        if tc == TerminationCondition.maxTimeLimit:
            return 3
        if tc == TerminationCondition.maxIterations:
            return 2
        if problem['Sense'] == 1 or problem['Sense'] == 'minimize':
            if problem['Upper bound'] in {float('inf'), float('-inf')}:
                return 4
        else:
            if problem['Lower bound'] in {float('inf'), float('-inf')}:
                return 4
        return 1

    if ss == SolverStatus.warning:  # Termination with unusual condition
        return 6
    if ss == SolverStatus.error:    # Terminated internally with error
        return 10
    if ss == SolverStatus.aborted:  # Terminated due to external conditions
        return 4
    if ss == SolverStatus.unknown:  # An unitialized value
        return 13
