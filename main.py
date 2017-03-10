import board

# b = board.Board(8)
# b.add_random_queens(6)
#
# i=0
# while b.fitness()>=1:
#     i+=1
#     b.reset_board()
#     b.add_random_queens(6)
#     b.fitness()
#
#
# print("fitness = " + str(b.fitness()))
# print(b)
# print(i)


b = board.Board(8)
b.add_random_queens(5)
print(b)
b.neighbour()
print(b)