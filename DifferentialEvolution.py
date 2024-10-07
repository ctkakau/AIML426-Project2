#    This file is part of EAP.
#
#    EAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    EAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with EAP. If not, see <http://www.gnu.org/licenses/>.

import random
import array

import numpy

from deap import base
from deap import benchmarks
from deap import creator
from deap import tools

# Problem dimension


def main(
  CR = 0.25,
    F = 1,  
    MU = 30,
    NGEN = 20,
    NDIM = 10,
    BENCH = 'f1',
    LAMBDA = 20,
    SEED = None):
      
      # remove previous classes to prevent the warning on multi-run experiment
    try:
        del creator.FitnessMin
        del creator.Individual
        
    except Exception as e:
        pass
    
    random.seed(SEED)
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessMin)
    
    toolbox = base.Toolbox()
    toolbox.register("attr_float", random.uniform, -3, 3)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, NDIM)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("select", tools.selRandom, k=3)
    
    # switch for f1 and f2)
    if BENCH == 'f1':
      toolbox.register("evaluate", benchmarks.rosenbrock)
    else:
      toolbox.register("evaluate", benchmarks.griewank)

    pop = toolbox.population(n=MU);
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    logbook = tools.Logbook()
    logbook.header = "gen", "evals", "std", "min", "avg", "max"

    # Evaluate the individuals
    fitnesses = toolbox.map(toolbox.evaluate, pop)
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    record = stats.compile(pop)
    logbook.record(gen=0, evals=len(pop), **record)
    # print(logbook.stream)

    for g in range(1, NGEN):
        for k, agent in enumerate(pop):
            a,b,c = toolbox.select(pop)
            y = toolbox.clone(agent)
            index = random.randrange(NDIM)
            for i, value in enumerate(agent):
                if i == index or random.random() < CR:
                    y[i] = a[i] + F*(b[i]-c[i])
            y.fitness.values = toolbox.evaluate(y)
            if y.fitness > agent.fitness:
                pop[k] = y
        hof.update(pop)
        record = stats.compile(pop)
        logbook.record(gen=g, evals=len(pop), **record)
        # print(logbook.stream)

    # print("Best individual is ", hof[0], hof[0].fitness.values[0])
    return pop, logbook, hof,

if __name__ == "__main__":
    main()
