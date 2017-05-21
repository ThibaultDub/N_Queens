import random
import math


class BoardLine:

    def __init__(self, n, lines=[], gen = False):

        self.n = n
        self.lines = lines
        self.forbidden = []

        if lines == []:
            if gen:
                for i in range(self.n):
                    col = random.randint(0, self.n-1)
                    self.lines.append(Line(self.n, col))
            else:
                available = list(range(self.n))
                for i in range(self.n):
                    index_available = random.randint(0, len(available) - 1)
                    queen_index = available.pop(index_available)
                    self.lines.append(Line(self.n, queen_index))

        if not gen:
            self.fitness = self.get_fitness()

        if gen:
            self.fitness = self.get_fitness_gen()



    def __repr__(self):
        string = " _" * self.n + "\n"
        for col in self.lines:
            string += col.__repr__()
            string += "\n"
        return string

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self) -> int:
        res = 0
        for line in self.lines:
            res += 31 * line.__hash__()
        return res


    def get_fitness(self):
        fitness = 0
        for line_number in range(0, self.n):  # =y
            line = self.lines[line_number]
            column_number = line.queen  # =x
            queen = (column_number, line_number)
            i = 1
            for searching_line_number in range(line_number + 1, self.n):
                x_left = queen[0] - i
                x_right = queen[0] + i
                y = queen[1] + i
                if self.lines[y].queen == x_left:
                    fitness += 1
                if self.lines[y].queen == x_right:
                    fitness += 1
                if x_left < 0 and x_right > self.n:
                    break;

                i += 1
        return fitness

    def get_fitness_gen(self):
        fitness = 0
        for line_number in range(0, self.n):  # =y
            line = self.lines[line_number]
            column_number = line.queen  # =x
            queen = (column_number, line_number)
            i = 1
            for searching_line_number in range(line_number + 1, self.n):
                x_left = queen[0] - i
                x_right = queen[0] + i
                y = queen[1] + i
                if self.lines[y].queen == x_left:
                    fitness += 1
                if self.lines[y].queen == x_right:
                    fitness += 1
                if self.lines[y].queen == column_number:
                    fitness += 1

                i += 1
        return fitness




    def neighbours(self): # TODO : une autre fonction de voisinage qui ne permute pas toutes les colonnes entre elles, mais seulement une seule(aléatoire) avec toutes les autres
        neighbourhood = set()
        for i in range(self.n):
            for j in range(i):
                temp = self.lines.copy()
                temp[i], temp[j] = temp[j], temp[i]
                new_board = BoardLine(self.n, temp)
                neighbourhood.add(new_board)
        return neighbourhood


    def random_neighbour(self):
        i = random.randint(0,self.n-1)
        j=random.randint(0,self.n-1)
        while i==j:
            j=random.randint(0,self.n-1)
        temp = self.lines.copy()
        temp[i], temp[j] = temp[j], temp[i]
        return BoardLine(self.n, temp)

    # def reproduce(self, other):
    #
    #     new_lines1 = self.lines[:int(round(self.n/2))] # 2e moitié de la première grille
    #     new_lines1.extend(other.lines[int(round(self.n/2)):]) # avec la première moitié de la seconde grille
    #
    #     new_lines2 = other.lines[:int(round(self.n/2))] # 2e moitié de la seconde grille
    #     new_lines2.extend(self.lines[int(round(self.n/2)):]) # avec la première moitié de la première
    #
    #     new1 = BoardLine(self.n, new_lines1, True)
    #     new2 = BoardLine(self.n, new_lines2, True)
    #     return([new1, new2])

    # def reproduce(self, other):
    #     grid1_lines1 = self.lines[:self.n:2] # 1 ligne sur deux à partir de 0
    #     grid1_lines2 = other.lines[1:self.n:2] # 1 ligne sur deux à partir de 1
    #     grid2_lines1 = self.lines[1:self.n:2] # 1 ligne sur deux à partir de 1
    #     grid2_lines2 = other.lines[:self.n:2] # 1 ligne sur deux à partir de 0
    #
    #
    #     grid1_lines = [None] * (len(grid1_lines1) + len(grid1_lines2))
    #     grid1_lines[::2] = grid1_lines1
    #     grid1_lines[1::2] = grid1_lines2
    #     grid2_lines = [None] * (len(grid2_lines1) + len(grid2_lines2))
    #     grid2_lines[::2] = grid2_lines2
    #     grid2_lines[1::2] = grid2_lines1
    #
    #     new1 = BoardLine(self.n, grid1_lines, True)
    #     new2 = BoardLine(self.n, grid2_lines, True)
    #     return([new1, new2])

    # def reproduce(self, other):
    #     new_lines1 = []
    #     new_lines2 = []
    #     for i in range(self.n):
    #         proba = random.random()
    #         threshold = 1-self.fitness/(other.fitness+self.fitness)
    #         if(proba<=threshold):
    #             new_lines1.append(self.lines[i])
    #             new_lines2.append(other.lines[i])
    #         else:
    #             new_lines1.append(other.lines[i])
    #             new_lines2.append(self.lines[i])
    #
    #     new1 = BoardLine(self.n, new_lines1, True)
    #     new2 = BoardLine(self.n, new_lines2, True)
    #     return [new1,new2]

    def reproduce(self, other):
        p = random.randint(0,self.n-1)
        new_lines1 = self.lines[:p] # 2e moitié de la première grille
        new_lines1.extend(other.lines[p:]) # avec la première moitié de la seconde grille

        new_lines2 = other.lines[:p] # 2e moitié de la seconde grille
        new_lines2.extend(self.lines[p:]) # avec la première moitié de la première

        new1 = BoardLine(self.n, new_lines1, True)
        new2 = BoardLine(self.n, new_lines2, True)
        return([new1, new2])


    def mutate(self, mutation_chance):
        rand = random.random()
        if rand<mutation_chance:
            index1 =random.randint(0,self.n - 1)
            index2 =random.randint(0,self.n - 1)
            self.lines[index1], self.lines[index2] = self.lines[index2], self.lines[index1]
            self.fitness = self.get_fitness_gen()





class Line:
    def __init__(self, n, queen=0):
        self.n = n
        self.queen = queen

    def __repr__(self):
        str = "|"
        for i in range(self.n):
            if i == self.queen:
                str += "D|"
            else:
                str += "_|"
        return str

    def __hash__(self):
        return 13*self.n+17*self.queen
