#!/bin/bash

# need to be activated mannually
# conda activate mindtpy_before_rewrite
conda env list
# replace ipopt with ipopt

# 1. convex

# 1.1 Cplex

# 1.1.1 Multi tree

# # OA

conda env list
# conda environments:

sleep 3s
# python run_benchmarks.py --solver mindtpy --model-dir models_all_solvable2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 5000 --strategy OA --method-name cplex_ipopth_1thread_convexification --threads 1 --stalling-limit 5000 --result-folder convex-convexification --use-baron-convexification &

sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_all_solvable2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 5000 --strategy ECP --method-name cplex_ipopth_1thread_convexification --threads 1 --stalling-limit 5000 --result-folder convex-convexification --use-baron-convexification &

sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_all_solvable2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 5000 --strategy OA --method-name cplex_ipopth_1thread_convexification --threads 1 --stalling-limit 5000 --result-folder convex-convexification --use-baron-convexification --single-tree  &

# GUROBI
sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_all_solvable2 --timelimit 900 --mip-solver gurobi_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 5000 --strategy OA --method-name gurobi_ipopth_1thread_convexification --threads 1 --stalling-limit 5000 --result-folder convex-convexification --use-baron-convexification &

sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_all_solvable2 --timelimit 900 --mip-solver gurobi_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 5000 --strategy ECP --method-name gurobi_ipopth_1thread_convexification --threads 1 --stalling-limit 5000 --result-folder convex-convexification --use-baron-convexification &

sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_all_solvable2 --timelimit 900 --mip-solver gurobi_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 5000 --strategy OA --method-name gurobi_ipopth_1thread_convexification --threads 1 --stalling-limit 5000 --result-folder convex-convexification --use-baron-convexification --single-tree  &

wait
echo "succeed"
