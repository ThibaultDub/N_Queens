from datetime import timedelta
from algo import Algo
import boardLine
import board
import time


# start_time = time.time()
# b = Algo.recuit(250, 60, 0.99, 1000, 50)
# b = Algo.gen(grid_size=10, pop_size=5, best_pop_size=2)

# print(b)
# print("Fitness : " + str(b.fitness))
# print("--- %s seconds ---" % (time.time() - start_time))

# a= boardLine.BoardLine(8)
# b= boardLine.BoardLine(8)
# print(a)
# print(b)
# a.reproduce(b)


# l1 = boardLine.Line(8, 0)
# l2 = boardLine.Line(8, 1)
# l3 = boardLine.Line(8, 2)
# l4 = boardLine.Line(8, 3)
# l5 = boardLine.Line(8, 4)
# l6 = boardLine.Line(8, 5)
# l7 = boardLine.Line(8, 6)
# l8 = boardLine.Line(8, 7)
#
# lines1 = [l1, l2, l3, l4, l5, l6, l7, l8]
# lines2 = [l8, l7, l6, l5, l4, l3, l2, l1]
#
# a = boardLine.BoardLine(8,lines1)
# b = boardLine.BoardLine(8,lines2)
# print(a)
# print(b)
# a.reproduce(b)

b= Algo.tabou(60)
print(b)
print("fitness : "+str(b.fitness))