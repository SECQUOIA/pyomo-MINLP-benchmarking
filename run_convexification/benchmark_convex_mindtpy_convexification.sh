# GUROBI
sleep 3s
python ../run_benchmarks.py --solver mindtpy --model-dir models_all_solvable2 --timelimit 900 --mip-solver gurobi_persistent --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 5000 --strategy OA --method-name gurobi_ipopth_1thread_convexification --threads 1 --stalling-limit 5000 --result-folder convex-convexification --use-baron-convexification &
