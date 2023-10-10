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
python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 2000 --strategy GOA --method-name cplex_ipopth_1thread --threads 1 --stalling-limit 2000 --result-folder nonconvex-before-rewrite &

sleep 3s

python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"baron"}' --iteration-limit 2000 --strategy GOA --method-name cplex_baron_1thread --threads 1 --stalling-limit 2000 --result-folder nonconvex-before-rewrite &

sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"conopt"}' --iteration-limit 2000 --strategy GOA --method-name cplex_conopt_1thread --threads 1 --stalling-limit 2000 --result-folder nonconvex-before-rewrite &

sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"msnlp"}' --iteration-limit 2000 --strategy GOA --method-name cplex_msnlp_1thread --threads 1 --stalling-limit 2000 --result-folder nonconvex-before-rewrite &


# gurobi
sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver gurobi_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 2000 --strategy GOA --method-name gurobi_ipopth_1thread --threads 1 --stalling-limit 2000 --result-folder nonconvex-before-rewrite &

sleep 3s

python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver gurobi_persistent --nlp-solver gams --nlp-solver-args '{"solver":"baron"}' --iteration-limit 2000 --strategy GOA --method-name gurobi_baron_1thread --threads 1 --stalling-limit 2000 --result-folder nonconvex-before-rewrite &

sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver gurobi_persistent --nlp-solver gams --nlp-solver-args '{"solver":"conopt"}' --iteration-limit 2000 --strategy GOA --method-name gurobi_conopt_1thread --threads 1 --stalling-limit 2000 --result-folder nonconvex-before-rewrite &

sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver gurobi_persistent --nlp-solver gams --nlp-solver-args '{"solver":"msnlp"}' --iteration-limit 2000 --strategy GOA --method-name gurobi_msnlp_1thread --threads 1 --stalling-limit 2000 --result-folder nonconvex-before-rewrite &

wait
echo "succeed"
