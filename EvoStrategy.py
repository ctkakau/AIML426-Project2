#    This file is part of DEAP.
#
#    DEAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    DEAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with DEAP. If not, see <http://www.gnu.org/licenses/>.

### reorganise code to include arguments in main() function
### add switch for benchmarks.griewank and benchmarks.rosenbrock
### ES with switch for benchmarks and algorithm

import array
import random

import numpy

from deap import algorithms
from deap import base
from deap import benchmarks
from deap import creator
from deap import tools

def main(
  IND_SIZE = 30,
  MIN_VALUE = 4,
  MAX_VALUE = 5,
  MIN_STRATEGY = 0.5,
  MAX_STRATEGY = 2, #decrease from 3
  NGEN = 500, 
  MUTPB = 0.4, #increase from 0.3
  CXPB = 0.5, # decrease from 0.6
  MU = 10, 
  LAMBDA = 100,
  SEED = None,
  BENCH = 'f1'
):
    
    # set seed
    random.seed(SEED)
    
    
    # remove previous classes to prevent the warning on multi-run experiment
    try:
        del creator.FitnessMin
        del creator.Individual
        del creator.Strategy
        
    except Exception as e:
        pass


    # create Fitness, Individual, and strategy
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", array.array, typecode="d", fitness=creator.FitnessMin, strategy=None)
    creator.create("Strategy", array.array, typecode="d")
    
    
    # Individual and strategy generator
    def generateES(icls, scls, size, imin, imax, smin, smax):
        ind = icls(random.uniform(imin, imax) for _ in range(size))
        ind.strategy = scls(random.uniform(smin, smax) for _ in range(size))
        return ind
    
    
    # Check strategies are within bounds
    def checkStrategy(minstrategy):
        def decorator(func):
            def wrappper(*args, **kargs):
                children = func(*args, **kargs)
                for child in children:
                    for i, s in enumerate(child.strategy):
                        if s < minstrategy:
                            child.strategy[i] = minstrategy
                return children
            return wrappper
        return decorator
    
    
    # create toolbox and register evolutionary operations
    toolbox = base.Toolbox()
    toolbox.register("individual", generateES, creator.Individual, creator.Strategy,
        IND_SIZE, MIN_VALUE, MAX_VALUE, MIN_STRATEGY, MAX_STRATEGY)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("mate", tools.cxESBlend, alpha = 0.1)
    toolbox.register("mutate", tools.mutESLogNormal, c=0.817, indpb = 0.8) # c=1.0, indpb=0.03)
    toolbox.register("select", tools.selTournament, tournsize = 5) # tournsize=3)
    toolbox.decorate("mate", checkStrategy(MIN_STRATEGY))
    toolbox.decorate("mutate", checkStrategy(MIN_STRATEGY))
    
    
    # switch between griewank or rosenbrock benchmarks
    if BENCH == 'f2':
      toolbox.register("evaluate", benchmarks.griewank)#  benchmarks.sphere)
      ALGO = algorithms.eaMuPlusLambda
    elif BENCH == 'f1':
      toolbox.register("evaluate", benchmarks.rosenbrock)#  benchmarks.sphere)
      ALGO = algorithms.eaMuCommaLambda
    
    ##### initialise population, hall of fame, and statistics
    pop = toolbox.population(n=MU)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    pop, logbook = ALGO(pop, toolbox, mu=MU, lambda_=LAMBDA, 
        cxpb=CXPB, mutpb=MUTPB, ngen=NGEN, stats=stats, halloffame=hof, verbose = False)

    return pop, logbook, hof


if __name__ == "__main__":
    main()
