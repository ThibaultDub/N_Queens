import random
import sys

import copy

import math

from boardLine import BoardLine


class Algo:

    @staticmethod
    def gen(size, ):



    @staticmethod
    def recuit(size, t, gap, n1, n2):
        xi = BoardLine(size)
        fmin = xi.fitness()
        i = 0
        # t = 0.8
        # gap = 2
        # n1 = 20  # nb de changements de T°
        # n2 = 20  # nb d'iterations / T°
        for k in range(0, n1):
            percentage = int(k/n1*100)
            print(str(percentage) + "% [" + "-"*percentage + " "*(100-percentage) +"] fmin = " + str(fmin)+" "*5, end = "\r")
            for l in range(0, n2):
                y = xi.random_neighbour()
                y_fitness = y.fitness()
                if y_fitness == 0:  # on break si on trouve une solution parfaite
                    return y
                delta_f = y_fitness - xi.fitness()
                if delta_f <= 0:
                    xi = copy.copy(y)
                    xi_fitness = y_fitness
                    if xi_fitness < fmin:
                        fmin = xi_fitness
                        xmin = copy.copy(xi)
                else:
                    if random.random() <= math.exp(-delta_f/t):
                        xi = copy.copy(y)
                i += 1
            t *= gap
        return xmin

    @staticmethod
    def tabou(
            size):  # TODO: Attention le tableau tabou ne semble pas fonctionner : il n'a jamais aucun element en commun avec C
        xi = BoardLine(size)
        i = 0
        t = set()
        xmin = copy.copy(xi)
        fmin = xmin.fitness()
        c = xi.neighbours()
        while (not len(c) == 0) and fmin != 0:
            c = xi.neighbours()
            c = c - t
            if len(c) > 0:
                local_f_min = sys.maxsize
                for neighbour in c:
                    if neighbour.fitness() < local_f_min:
                        local_f_min = neighbour.fitness()
                        y = copy.copy(neighbour)
                    local_f_min = min(local_f_min, neighbour.fitness())
                delta_f = y.fitness() - xi.fitness()
                if delta_f >= 0:
                    t.add(xi)
                if local_f_min < fmin:
                    fmin = y.fitness()
                    xmin = copy.copy(y)
                xi = y
            i += 1
        print(i)

        return xmin
