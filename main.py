from algo import Algo
import time



start_time = time.time()
b = Algo.recuit(size=100, t=50, gap=.90, n1=600, n2=50)
# b = Algo.gen(grid_size=10, pop_size=1000, best_pop_size=100, mutation_chance=0.2) # l'algorithme genetique doit etre lance sur CPython 3.6 ou superieur
# b = Algo.tabou(100,20)
print(b)
print("Fitness : " + str(b.fitness))
print("--- %s seconds ---" % (time.time() - start_time))
