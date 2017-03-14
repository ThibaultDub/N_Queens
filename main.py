import time
from datetime import timedelta

import board

start_time = time.monotonic()

b = board.Board(8)
b.add_random_queens(6)
print(b)
# while b.fitness()>=4:
#     b.neighbour()
#     print(b)


# i = 0
# while b.fitness() >= 3:
#     i += 1
#     b.reset_board()
#     b.add_random_queens(6)
#     b.fitness()
#
# print("fitness = " + str(b.fitness()))
# print(b)
# print("loops : " + str(i))
# end_time = time.monotonic()
# print(timedelta(seconds=end_time - start_time))



