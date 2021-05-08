# pyomo-MINLP-benchmarking

## What is this?
This repository mostly contains the `run_benchmarks.py` script as well as
a collection of MINLP problems/models, which have been taken from the
[MINLPlib](http://www.minlplib.org/) and converted to [Pyomo](https://github.com/Pyomo/pyomo) models with the
`translate.sh` file.

## Example usage

### Translate gms model to pyomo model

1. Download the gms file from the [MINLPlib](http://www.minlplib.org/).

2. Create a txt file(like [convex.txt](./convex.txt)) to denote the instances that you want to translate.

3. Check the `INSTANCEDIR`, `TESTSET` and `PYOMOMODELDIR` in translate.sh and run it.

### Benchmark

When running

```sh
# show some help
python run_benchmarks.py -h  

python run_benchmarks.py --solver mindtpy --model-dir models_all_solvable2 --timelimit 900 --mip-solver cplex --nlp-solver ipopt --iteration-limit 2000 --strategy OA --method-name direct_cplex_8threads --threads 8 --stalling-limit 2000 --result-folder LOA

# use subsolver from gams
python run_benchmarks.py --solver mindtpy --model-dir models_all_solvable2 --timelimit 900 --mip-solver cplex --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 2000 --strategy OA --method-name direct_cplex_8threads --threads 8 --stalling-limit 2000 --result-folder LOA

# skip folder
python run_benchmarks.py --solver mindtpy --model-dir models_all_solvable2 --timelimit 900 --mip-solver cplex --nlp-solver gams --nlp-solver-args '{"solver":"ipopth"}' --iteration-limit 2000 --strategy OA --method-name no_regularization_direct_cplex_8threads --threads 8 --stalling-limit 2000 --result-folder LOA --skip-folder LOA/mindtpy-OA-2021_02_14_12_03_32 --no-skip-failed

```
After running, the `results/<solver>` dir will contain
- a `.txt` file for each model output
- `trace_file.trc` which can be loaded into [Paver](https://github.com/coin-or/Paver) to generate automatic benchmarking plots (not yet tested)
- `solving_times.csv` which contains the model name, aswell as the solving time or the termination condition/error
