
sleep 3s
python run_benchmarks.py --solver gams --model-dir models_all_solvable2 --timelimit 900 --gams-solver SHOT --gams-solver-optionfile cplex-multi-tree --result-folder convex-base

sleep 3s
python run_benchmarks.py --solver gams --model-dir models_all_solvable2 --timelimit 900 --gams-solver SHOT --gams-solver-optionfile cplex-single-tree --result-folder convex-base

sleep 3s
python run_benchmarks.py --solver gams --model-dir models_all_solvable2 --timelimit 900 --gams-solver SHOT --gams-solver-optionfile gurobi-multi-tree --result-folder convex-base

sleep 3s
python run_benchmarks.py --solver gams --model-dir models_all_solvable2 --timelimit 900 --gams-solver SHOT --gams-solver-optionfile gurobi-single-tree --result-folder convex-base
