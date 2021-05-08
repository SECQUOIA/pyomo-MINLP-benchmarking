#!/bin/bash

# These are commands for TORQUE Queue System.
# For more details about TORQUE, please refer to http://newton.cheme.cmu.edu/euler/euler.html

# Set the number of nodes and processes per node
#PBS -l nodes=1:ppn=8

# Set max wallclock time
#PBS -l walltime=150:00:00

# Set maximum memory
#PBS -l mem=16gb

# Set name of job
#PBS -N GOA1

# Use submission environment
#PBS -V
# source ~/.bashrc
cd ~/pyomo-MINLP-benchmarking

python run_benchmarks.py --solver mindtpy --model-dir models_all_solvable2 --timelimit 900 --mip-solver cplex --nlp-solver ipopt --iteration-limit 2000 --strategy OA --method-name direct_cplex_8threads --threads 8 --stalling-limit 2000 --result-folder LOA

# use subsolver from gams
python run_benchmarks.py --solver mindtpy --model-dir models_all_solvable2 --timelimit 900 --mip-solver cplex --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 2000 --strategy OA --method-name direct_cplex_8threads --threads 8 --stalling-limit 2000 --result-folder LOA

# skip folder
python run_benchmarks.py --solver mindtpy --model-dir models_all_solvable2 --timelimit 900 --mip-solver cplex --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 2000 --strategy OA --method-name no_regularization_direct_cplex_8threads --threads 8 --stalling-limit 2000 --result-folder LOA --skip-folder LOA/mindtpy-OA-2021_02_14_12_03_32 --no-skip-failed

