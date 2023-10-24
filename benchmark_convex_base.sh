
sleep 3s
python run_benchmarks.py --solver gams --model-dir models_simple_test --timelimit 900 --gams-solver SHOT --gams-solver-optionfile cplex-multi-tree --result-folder convex-base

# sleep 3s
# python run_benchmarks.py --solver gams --model-dir models_simple_test --timelimit 900 --gams-solver SHOT --gams-solver-optionfile cplex-single-tree --result-folder convex-base

# sleep 3s
# python run_benchmarks.py --solver gams --model-dir models_simple_test --timelimit 900 --gams-solver SHOT --gams-solver-optionfile gurobi-multi-tree --result-folder convex-base

# sleep 3s
# python run_benchmarks.py --solver gams --model-dir models_simple_test --timelimit 900 --gams-solver SHOT --gams-solver-optionfile gurobi-single-tree --result-folder convex-base
