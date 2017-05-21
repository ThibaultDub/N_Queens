from algo import Algo
import time



start_time = time.time()
# b = Algo.recuit(size=10, t=5, gap=.80, n1=30, n2=30)
# b = Algo.gen(grid_size=10, pop_size=1000, best_pop_size=100, mutation_chance=0.2)
b = Algo.tabou(100,20)
print(b)
print("Fitness : " + str(b.fitness))
print(b.get_fitness)
print("--- %s seconds ---" % (time.time() - start_time))

