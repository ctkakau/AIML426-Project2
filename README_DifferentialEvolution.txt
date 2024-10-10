#############################
#
# README:  DifferentialEvolution
#
#############################

This README provides information on the script:

DifferentialEvolution.py

Functionality:
This script performs a Differential Evolution to try to optimise for two benchmarks:  Rosenbrock's and Griewank's functions.  The script makes minor modifications but is for the most part, the example script from the deap github site:

link:  https://github.com/DEAP/deap/blob/master/examples/de/basic.py

The script allows for users to modify some parameters in order to meet their particular needs.  The script has one user accessible function (main()) which has sufficient default parameters to run without the user providing any inputs.  

USAGE:
# import library
import DifferentialEvolution as devo

# run with default settings
pop, logbook, hof = devo.main()

#### user accessible functions:
main(CR = 0.25,
    F = 1,  
    MU = 30,
    NGEN = 20,
    NDIM = 10,
    BENCH = 'f1',
    LAMBDA = 20,
    SEED = None):

#### arguments:
CR: float, 
F: float,
MU: float, number of individuals selected in next generation
NGEN: float, number of generations to evolve
NDIM: float, number of variables in individual
BENCH: chr, selector for evaluation - 'f1' calls the Rosenbrock benchmark, 'f2' calls the Griewank benchmark
LAMBDA: float, number of individuals in first generation
SEED: float, seed for controlling randomness in the experiments

#### returns:
pop: list, list of all individuals in each generation of the experiment
logbook: list of dicts, statistics of each generation: 'gen', 'n-evals', 'max', 'min', 'average', 'standard deviation'
hof:  list, Hall of fame that holds the N-best individuals across all generations.

The script can be run from the command line.  An R-Markdown document is also availabe that runs the script and reports results of a seeded experiment at:

https://github.com/ctkakau/AIML426-Project2/blob/main/Q2_AIML426_project_2.Rmd

The R-Markdown file assumes the DifferentialEvolution.py script is in the same working directory.
