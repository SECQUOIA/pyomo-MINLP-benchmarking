#!/usr/bin/env bash

GAMS="GAMS"
# INSTANCEDIR is the directory of gams files that can downloaded from http://minlplib.org/download.html
if [ $USER == debernal ] ; then
    INSTANCEDIR=/home/bernalde/MINLPLib/data/gms
else
    INSTANCEDIR=/Users/zedongpeng/Documents/CMU/MindtPy/minlplib/gms 
fi

# TESTSET is the txt file of instance names 

TESTSET="convex"
PYOMOMODELDIR="models_all_solvable3"
SKIPEXISTING=0   # whether to skip runs for which a trace file already exists

GAMSOPTS="reslim=100 threads=1"
# TODO memlimit?

INSTANCES=`cut -d" " -f1 ${TESTSET}.txt`

# run a solver/option-file combination on a particular instance
# $1 = instance
# $2 = solvername
# $3 = option file number
function runinstance ()
{
   TRACEFILE=${TESTSET}.trc/$1.$2.$3.trc

   if [ $SKIPEXISTING == 1 ] && [ -e $TRACEFILE ] ; then
      echo "Skip solver $2 with option file $3 on instance $1"
      return
   fi

   echo "Run solver $2 with option file $3 on instance $1"

   mkdir -p ${TESTSET}.trc
   mkdir -p ${TESTSET}.log

   # initialize trace files
   cat > $TRACEFILE <<EOF
* Trace Record Definition
* GamsSolve
* InputFileName,SolverName,OptionFile,Direction,NumberOfEquations,NumberOfVariables,NumberOfDiscreteVariables,NumberOfNonZeros,NumberOfNonlinearNonZeros,
* ModelStatus,SolverStatus,ObjectiveValue,ObjectiveValueEstimate,SolverTime,ETSolver,NumberOfIterations,NumberOfNodes
EOF


   # if [ $USER == bernalde ] ; then
      $GAMS ${INSTANCEDIR}/$1 MINLP=$2 MIQCP=$2 OPTFILE=$3 $GAMSOPTS LF=${TESTSET}.log/$1.$2.$3.log O=${TESTSET}.log/$1.$2.$3.lst TRACE=$TRACEFILE

      # change name of gams.py into actual instance name .py
      # you can define the directory to store the auto-generated pyomo files by changing PYOMOMODELDIR

      # when your gams version is below 34.3, the name of generated pyomo file is gams.py
      # mv gams.py ${PYOMOMODELDIR}/$1.py

      # when your gams version is 34.3 or above, the name of generated pyomo file is pyomo.py
      mv pyomo.py ${PYOMOMODELDIR}/$1.py

   # else

   # fi
}

# run a solver/option-file combination on the set of instances
# $1 = solvername
# $2 = option file number
function runsolveropt ()
{
   for i in $INSTANCES
   do
      runinstance $i $1 $2
   done
}

# run all
runsolveropt convert 1
