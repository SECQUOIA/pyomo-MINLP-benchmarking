#!/bin/bash

# need to be activated mannually
# conda activate mindtpy_before_rewrite
conda env list
# replace ipopt with ipopt

# 1. convex

# 1.1 Cplex

# 1.1.1 Multi tree

# # OA

# cplex
python run_benchmarks.py --solver mindtpy --model-dir models_all_solvable2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 2000 --strategy OA --method-name cplex_ipopth_1thread --threads 1 --stalling-limit 2000 --result-folder convex-after-rewrite3 --skip-folder convex-after-rewrite3/mindtpy-OA-singletree-2023_10_08_18_44_00  --no-skip-failed --single-tree &

sleep 3s

python run_benchmarks.py --solver mindtpy --model-dir models_all_solvable2 --timelimit 900 --mip-solver gurobi_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 2000 --strategy OA --method-name cplex_ipopth_1thread --threads 1 --stalling-limit 2000 --result-folder convex-after-rewrite3 --skip-folder convex-after-rewrite3/mindtpy-OA-singletree-2023_10_08_18_44_09 --no-skip-failed --single-tree &

wait
echo "succeed"
