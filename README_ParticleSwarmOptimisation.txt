#############################
#
# README:  Particle Swarm Optimisation
#
#############################

This README provides information on the script:

ParticleSwarmOptimisation.py

Functionality:
This script performs a Particle Swarm Optimisation to try to optimise for two benchmarks:  Rosenbrock's and Griewank's functions.  The script makes minor modifications but is for the most part, the example script from the deap github site:

link:  https://github.com/DEAP/deap/blob/028516b63af193580d442e9518a0355136ee60c5/examples/pso/basic.py#L4

The script allows for users to modify some parameters in order to meet their particular needs.  The script has one user accessible function (main()) which has sufficient default parameters to run without the user providing any inputs.  

USAGE:
# import library
import ParticleSwarmOptimisation as pso

# run with default settings
pop, logbook, hof = devo.main()

#### user accessible functions:
main(    PMIN= -30,
    PMAX = 30,
    SMIN = -3,
    SMAX = 3,
    PHI1=2.8,
    PHI2=0.5,
    BENCH = 'f1',
    SEED = None,
    NGEN = 30,
    MU=30,
    NDIM = 20,
):

#### arguments:
PMIN: float, minimum value of each dimension in particle vector
PMAX: float, maximium value of each dimension in particle vector
SMIN: float, minimum velocity value for each dimension of the velocity vector
SMAX: float, maximum velocity value for each dimension of the velocity vector
PHI1: float, cognitive or individual acceleration coefficient
PHI2: float, social acceleration coefficient
BENCH: chr, indicator for one of two benchmarks: 'f1' Rosenbrock, 'f2' Griewank
SEED: float, control randomness
NGEN: float, number of generations for evolution
MU: float, number of children generated
NDIM: float, number of dimensions of individual

#### returns:
pop: list, list of all individuals in each generation of the experiment
logbook: list of dicts, statistics of each generation: 'gen', 'n-evals', 'max', 'min', 'average', 'standard deviation'
hof:  list, Hall of fame that holds the N-best individuals across all generations.

The script can be run from the command line.  An R-Markdown document is also availabe that runs the script and reports results of a seeded experiment at:

https://github.com/ctkakau/AIML426-Project2/blob/main/Q2_AIML426_project_2.Rmd

The R-Markdown file assumes the ParticleSwarmOptimisation.py script is in the same working directory.
