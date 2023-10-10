#!/bin/bash

# need to be activated mannually
# conda activate mindtpy_before_rewrite
conda env list
# replace ipopt with ipopt


# # OA
module load gams/44.3
python run_benchmarks.py --solver gams --model-dir models_nonconvex_simple2 --timelimit 900 --gams-solver scip --result-folder nonconvex-base &

python run_benchmarks.py --solver gams --model-dir models_nonconvex_simple2 --timelimit 900 --gams-solver antigone --result-folder nonconvex-base &

python run_benchmarks.py --solver gams --model-dir models_nonconvex_simple2 --timelimit 900 --gams-solver baron --result-folder nonconvex-base &

python run_benchmarks.py --solver gams --model-dir models_nonconvex_simple2 --timelimit 900 --gams-solver lindoglobal --result-folder nonconvex-base &

python run_benchmarks.py --solver gams --model-dir models_nonconvex_simple2 --timelimit 900 --gams-solver SHOT --gams-solver-optionfile multi-tree --result-folder nonconvex-base &

python run_benchmarks.py --solver gams --model-dir models_nonconvex_simple2 --timelimit 900 --gams-solver SHOT --gams-solver-optionfile single-tree --result-folder nonconvex-base &
