#############################
#
# README:  Population Based Incremental Learning
#
#############################

This README provides information on the script:

pbil.py

Functionality:
This script performs a Population Based Incremental Learning method to try to optimise for two benchmarks:  Rosenbrock's and Griewank's functions.  The script makes minor modifications but is for the most part, the example script from the deap github site:

link:  https://github.com/DEAP/deap/blob/028516b63af193580d442e9518a0355136ee60c5/examples/eda/pbil.py

The script allows for users to modify some parameters in order to meet their particular needs.  The script has one user accessible function (main()) which has sufficient default parameters to run without the user providing any inputs.  

USAGE:
# import package
import pbil

# run with default settings
pop, logbook, hof = pbil.main()

#### user accessible functions:
main(    
  MU = 5,
  NGEN = 5,
  NDIM = 10,
  PATH = '10_269',
  SEED = 42,
  MUTPROB = 0.1, 
  MUTSHIFT = 0.05,
  L_RATE = 0.3,
):

#### arguments:

MU: float, number of children to generate
NGEN: float, number of generations
NDIM: float, number of dimensions or items in knapsack
PATH: chr, path to file holding knapsack information, expects two columns with headers indicating the total number of items, and the max weight of the knapsack, values in each row represent an item with column1 the item's value and column2 the item's weight
MUTPROB: float, probability of mutation occurring to an individual 
MUTSHIFT: float, probability of mutation occurring to an item within the individual
SEED: float, control randomness
L_RATE: float, learning rate for the algorithm

#### returns:
pop: list, list of all individuals in each generation of the experiment
logbook: list of dicts, statistics of each generation: 'gen', 'n-evals', 'max', 'min', 'average', 'standard deviation'
hof:  list, Hall of fame that holds the N-best individuals across all generations.

The script can be run from the command line.  An R-Markdown document is also availabe that runs the script and reports results of a seeded experiment at:

https://github.com/ctkakau/AIML426-Project2/blob/main/Q3_AIML426_project_2.Rmd

The R-Markdown file assumes the pbil.py script is in the same working directory.
