from datetime import timedelta
from algo import Algo
import boardLine
import board
import time

# start_time = time.perf_counter()
# for i in range(100000):
#     b= boardLine.BoardLine(8)
# end_time = time.perf_counter()
# print(timedelta(seconds=end_time - start_time))
#
# l1 = boardLine.Line(8, 3)
# l2 = boardLine.Line(8, 6)
# l3 = boardLine.Line(8, 2)
# l4 = boardLine.Line(8, 7)
# l5 = boardLine.Line(8, 1)
# l6 = boardLine.Line(8, 4)
# l7 = boardLine.Line(8, 0)
# l8 = boardLine.Line(8, 5)


# start_time = time.time()
# b = boardLine.BoardLine(500)
# b.fitness()
# print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
b = Algo.recuit(250, 60, 0.99, 1000, 50)
# b = Algo.gen(10, 5)

print(b)
print("Fitness : " + str(b.fitness))
print("--- %s seconds ---" % (time.time() - start_time))
