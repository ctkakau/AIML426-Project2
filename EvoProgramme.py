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
    
    # set seed
    random.seed(SEED)
    
    
    # remove previous classes to prevent the warning on multi-run experiment
    try:
        del creator.FitnessMin
        del creator.Individual
        del creator.Variance
        
    except Exception as e:
        pass


    # create Fitness, Individual, and strategy
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", array.array, typecode="d", fitness=creator.FitnessMin, variance=None)
    creator.create("Variance", array.array, typecode="d")
    
    
    # Individual and strategy generator
    def generateEP(icls, vcls, size, imin, imax,):
        ind = icls(random.uniform(imin, imax) for _ in range(size))
        ind.variance = vcls(numpy.random.standard_cauchy() for _ in range(size))
        return ind


    # mutation operator:  Meta-EP  
    def mutateEP(indiv, c, epsilon, indpb):
      size = len(indiv)
      
      for indx in range(size):
        if random.random() < indpb:
          
          # create noise
          rxi = numpy.random.standard_cauchy()
          rvi = numpy.random.standard_cauchy()
          
          # prevent sqrt error
          var_ = abs(indiv.variance[indx])
          
          # introduce noise
          indiv.variance[indx] = indiv.variance[indx] + rvi*numpy.sqrt(c*var_)
          indiv[indx] = indiv[indx] + rxi*numpy.sqrt(var_)
          # keep variance above epsilon
          indiv.variance[indx] = max(indiv.variance[indx], epsilon)
          
      del indiv.fitness.values
          
      return indiv,

    
    
    # create toolbox and register evolutionary operations
    toolbox = base.Toolbox()
    toolbox.register("individual", generateEP, creator.Individual, creator.Variance,
        IND_SIZE, MIN_VALUE, MAX_VALUE, )
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("mate", tools.cxESBlend, alpha = 0.1)
    toolbox.register("mutate", mutateEP, c = 0.871, epsilon = 0.0001, indpb = 0.99) #tools.mutESLogNormal, c=0.817, indpb = 0.8) # c=1.0, indpb=0.03)
    toolbox.register("select", tools.selBest)

    
    # switch between griewank or rosenbrock benchmarks
    if BENCH == 'f2':
      toolbox.register("evaluate", benchmarks.griewank)#  benchmarks.sphere)
      ALGO = algorithms.eaMuCommaLambda
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
