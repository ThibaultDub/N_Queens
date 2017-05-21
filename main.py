from datetime import timedelta
from algo import Algo
import boardLine
import board
import time


start_time = time.time()
b = Algo.recuit(size=10, t=5, gap=.80, n1=30, n2=30)
# b = Algo.gen(grid_size=6, pop_size=5, best_pop_size=3, mutation_chance=0.05)
print(b)
print("Fitness : " + str(b.fitness))
print("--- %s seconds ---" % (time.time() - start_time))

# a= boardLine.BoardLine(8)
# b= boardLine.BoardLine(8)
# print(a)
# print(b)
# a.reproduce(b)

#
# l1 = boardLine.Line(8, 0)
# l2 = boardLine.Line(8, 1)
# l3 = boardLine.Line(8, 2)
# l4 = boardLine.Line(8, 3)
# l5 = boardLine.Line(8, 4)
# l6 = boardLine.Line(8, 5)
# l7 = boardLine.Line(8, 6)
# l8 = boardLine.Line(8, 7)
# #
# lines1 = [l1, l2, l3, l4, l5, l6, l7, l8]
#
# # lines2 = [l8, l7, l6, l5, l4, l3, l2, l1]
# #
# a = boardLine.BoardLine(8,lines1)
# a.mutate(0.5)
# print(a)
# b = boardLine.BoardLine(8,lines2)
# print(a)
# print(b)
# [c,d] = a.reproduce(b)
# c.reproduce(d)

#
# start_time = time.time()
# a=Algo.tabou(size=100, taboo_size=100)
# print(a)
#
# print("Fitness : " + str(a.fitness))
# print("--- %s seconds ---" % (time.time() - start_time))
