#############################
#
# README:  Evolutionary Programming
#
#############################

This README provides information on the script:

EvoProgramme.py

Functionality:
This script performs an Evolutionary Programme to try to optimise for two benchmarks:  Rosenbrock's and Griewank's functions.  The script makes minor modifications but is for the most part, the example script from the deap github site:

link:  

The script allows for users to modify some parameters in order to meet their particular needs.  The script has one user accessible function (main()) which has sufficient default parameters to run without the user providing any inputs.  

USAGE:
# import package
import EvoProgramme as ep

# run with default settings
pop, logbook, hof = ep.main()

#### user accessible functions:
main(    IND_SIZE = 30,
  MIN_VALUE = -30,
  MAX_VALUE = 30,
  NGEN = 5, 
  MUTPB = 1, #increase from 0.3
  CXPB = 0, # decrease from 0.6
  MU = 10, 
  LAMBDA = 10,
  SEED = None,
  BENCH = 'f1'

):

#### arguments:

IND_SIZE: float, number of dimensions in individual
MIN_VALUE: float, minimum value for individual's dimensions
MAX_VALUE: float, maximum value for individual's dimensions
NGEN: float, number of generations
MUTPB: float, probability of mutation occurring
CXPB: float, probability of crossover occurring
MU: float, number of children to generate
LAMBDA: float, initial population size
SEED: float, control randomness
BENCH: chr, indicator for evaluation function, 'f1' Rosenbrock, 'f2' Griewank

#### returns:
pop: list, list of all individuals in each generation of the experiment
logbook: list of dicts, statistics of each generation: 'gen', 'n-evals', 'max', 'min', 'average', 'standard deviation'
hof:  list, Hall of fame that holds the N-best individuals across all generations.

The script can be run from the command line.  An R-Markdown document is also availabe that runs the script and reports results of a seeded experiment at:

https://github.com/ctkakau/AIML426-Project2/blob/main/Q1_AIML426_project_2.Rmd

The R-Markdown file assumes the EvoProgramme.py script is in the same working directory.
