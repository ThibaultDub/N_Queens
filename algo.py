import random
import sys
import copy
import time
import math
from operator import attrgetter

from boardLine import BoardLine


class Algo:
    @staticmethod
    def gen(grid_size, pop_size, best_pop_size, mutation_chance):
        """
            Fonction appelant la méthode du recuit simulé pour résoudre le problème des N Dames.

            param size: taille de l'échiquier
            param pop_size: Taille de la population générée à chaque itération
            param best_pop_size: nombre d'éléments sur lesquels seront basées les générations suivantes
        """
        population = []

        for i in range(pop_size):  # On crée une population de base
            grid = BoardLine(grid_size, lines=[], gen=True)
            population.append(grid)
        sum_of_fitnesses = sum([element.fitness for element in population])
        ponder = [(element.fitness / sum_of_fitnesses) for element in population]
        best_pop = random.choices(population, weights=ponder, k=best_pop_size)
        best_grid_met = min(best_pop, key=attrgetter('fitness'))
        while (best_grid_met.fitness > 0):
            population = []
            while len(population) < pop_size:  # reproductions
                [father, mother] = random.choices(best_pop, k=2)
                population.extend(father.reproduce(mother))

            for element in population:  # mutations
                element.mutate(mutation_chance)
            biggest = max(population, key=attrgetter('fitness'))
            reverse_fitnesses = [biggest.fitness - element.fitness + 1 for element in population]
            sum_of_reverse_fitnesses = sum(reverse_fitnesses)
            ponder = [element / sum_of_reverse_fitnesses for element in reverse_fitnesses]
            best_pop = random.choices(population, k=best_pop_size, weights=ponder)  # Selection
            best_grid_met = min(best_pop, key=attrgetter('fitness'))
            print(best_grid_met)
            print(best_grid_met.fitness)

        return best_grid_met

    @staticmethod
    def recuit(size, t, gap, n1, n2):
        """
            Fonction appelant la méthode du recuit simulé pour résoudre le problème des N Dames.

            param size: taille de l'échiquier
            param t: Température initiale
            param gap : coefficient multipliant la temperature actuelle pour obtenir la température suivante
            param n1 : nombre de changements de température
            param n2: nombre d'itération par température
            type size: int
            type t: int
            type gap: float <= 1
            type n1: int
            type n2: int
        """
        xi = BoardLine(size)
        fmin = xi.fitness
        i = 0
        for k in range(0, n1):
            percentage = int(k / n1 * 100)
            print("\r" + str(percentage) + "% [" + "-" * percentage + " " * (100 - percentage) + "] fmin = " + str(
                fmin) + " " * 5, end="")
            for l in range(0, n2):
                y = xi.random_neighbour()
                y_fitness = y.fitness
                if y_fitness == 0:  # on break si on trouve une solution parfaite
                    return y
                delta_f = y_fitness - xi.fitness
                if delta_f <= 0:
                    xi = copy.copy(y)
                    xi_fitness = y_fitness
                    if xi_fitness < fmin:
                        fmin = xi_fitness
                        xmin = copy.copy(xi)
                else:
                    if random.random() <= math.exp(-delta_f / t):
                        xi = copy.copy(y)
                i += 1
            t *= gap
        return xmin

    @staticmethod
    def tabou(size, taboo_size=20):
        xi = BoardLine(size)
        i = 0
        t = [None]*taboo_size
        xmin = copy.copy(xi)
        fmin = xmin.fitness
        c = [0]
        id_taboo = 0
        while (not len(c) == 0) and fmin != 0:
            c = xi.neighbours()
            for board in t:
                if (board in c):
                    c.remove(board)
            if len(c) != 0:
                local_f_min = sys.maxsize
                for neighbour in c:
                    if neighbour.fitness < local_f_min:
                        local_f_min = neighbour.fitness
                        y = copy.copy(neighbour)
                delta_f = y.fitness - xi.fitness
                if delta_f >= 0:
                    t[id_taboo%taboo_size]=xi
                    id_taboo += 1
                if y.fitness < fmin:
                    fmin = y.fitness
                    xmin = copy.copy(y)
                xi = y
            i += 1

        return xmin
