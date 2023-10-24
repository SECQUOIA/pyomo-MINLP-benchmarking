#!/bin/bash

# need to be activated mannually
# conda activate mindtpy_before_rewrite
conda env list
# replace ipopt with ipopt

# 1. convex

# 1.1 Cplex

# 1.1.1 Multi tree

# # OA

# # cplex
# python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 5000 --strategy GOA --method-name cplex_ipopth_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite --single-tree &

# sleep 3s
# python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"baron"}' --iteration-limit 5000 --strategy GOA --method-name cplex_baron_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite --single-tree &

# sleep 3s
# python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"conopt"}' --iteration-limit 5000 --strategy GOA --method-name cplex_conopt_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite --single-tree &

# # gurobi
# sleep 3s
# python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver gurobi_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 5000 --strategy GOA --method-name gurobi_ipopth_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite --single-tree &

# sleep 3s
# python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver gurobi_persistent --nlp-solver gams --nlp-solver-args '{"solver":"baron"}' --iteration-limit 5000 --strategy GOA --method-name gurobi_baron_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite --single-tree &

# sleep 3s
# python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver gurobi_persistent --nlp-solver gams --nlp-solver-args '{"solver":"conopt"}' --iteration-limit 5000 --strategy GOA --method-name gurobi_conopt_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite --single-tree &


# tabu list

# # cplex
# python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 5000 --strategy GOA --method-name cplex_ipopth_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite2-tabu-list --use-tabu-list &

# sleep 3s
# python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"baron"}' --iteration-limit 5000 --strategy GOA --method-name cplex_baron_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite2-tabu-list --use-tabu-list &

# sleep 3s
# python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"conopt"}' --iteration-limit 5000 --strategy GOA --method-name cplex_conopt_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite2-tabu-list --use-tabu-list &

# # cplex
# python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 5000 --strategy GOA --method-name cplex_ipopth_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite2-tabu-list --use-tabu-list --single-tree &

# sleep 3s
# python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"baron"}' --iteration-limit 5000 --strategy GOA --method-name cplex_baron_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite2-tabu-list --use-tabu-list --single-tree &

# sleep 3s
# python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"conopt"}' --iteration-limit 5000 --strategy GOA --method-name cplex_conopt_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite2-tabu-list --use-tabu-list --single-tree &

# max_binary

# cplex
sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 5000 --strategy GOA --method-name cplex_ipopth_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite3-max-binary --init-strategy max_binary &

sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"baron"}' --iteration-limit 5000 --strategy GOA --method-name cplex_baron_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite3-max-binary --init-strategy max_binary &

sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"conopt"}' --iteration-limit 5000 --strategy GOA --method-name cplex_conopt_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite3-max-binary --init-strategy max_binary &

# cplex
python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 5000 --strategy GOA --method-name cplex_ipopth_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite3-max-binary --init-strategy max_binary --single-tree &

sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"baron"}' --iteration-limit 5000 --strategy GOA --method-name cplex_baron_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite3-max-binary --init-strategy max_binary --single-tree &

sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"conopt"}' --iteration-limit 5000 --strategy GOA --method-name cplex_conopt_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite3-max-binary --init-strategy max_binary --single-tree &

# max-binary   
# tabu list
# cplex
python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 5000 --strategy GOA --method-name cplex_ipopth_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite4-max-binary-tabu-list --init-strategy max_binary --use-tabu-list &

sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"baron"}' --iteration-limit 5000 --strategy GOA --method-name cplex_baron_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite4-max-binary-tabu-list --init-strategy max_binary --use-tabu-list &

sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"conopt"}' --iteration-limit 5000 --strategy GOA --method-name cplex_conopt_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite4-max-binary-tabu-list --init-strategy max_binary --use-tabu-list &

# cplex
python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 5000 --strategy GOA --method-name cplex_ipopth_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite4-max-binary-tabu-list --init-strategy max_binary --use-tabu-list --single-tree &

sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"baron"}' --iteration-limit 5000 --strategy GOA --method-name cplex_baron_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite4-max-binary-tabu-list --init-strategy max_binary --use-tabu-list --single-tree &

sleep 3s
python run_benchmarks.py --solver mindtpy --model-dir models_nonconvex_simple2 --timelimit 900 --mip-solver cplex_persistent --nlp-solver gams --nlp-solver-args '{"solver":"conopt"}' --iteration-limit 5000 --strategy GOA --method-name cplex_conopt_1thread --threads 1 --stalling-limit 5000 --result-folder nonconvex-after-rewrite4-max-binary-tabu-list --init-strategy max_binary --use-tabu-list --single-tree &

wait
echo "succeed"
