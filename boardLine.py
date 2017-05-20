import random
import math


class BoardLine:

    def __init__(self, n, lines=[]):
        self.n = n
        self.lines = lines  # [Line(self.n, random.randint(0, self.n)) for i in range(self.n)]
        self.forbidden = []
        if lines == []:
            available = list(range(self.n))
            for i in range(self.n):
                queen_index = available.pop(random.randint(0, len(available) - 1))
                self.lines.append(Line(self.n, queen_index))
        self.fitness = self.get_fitness()


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

    def reproduce(self, other):
        # lines1 = self.lines[:int(round(self.n/2))]
        # print(type(lines1))
        # second_half1 = other.lines[int(round(self.n/2)):]
        # print(type(second_half1))
        # lines1.extend(second_half1)
        # print(type(lines1))

        new_lines1 = self.lines[:int(round(self.n/2))] # 2e moitié de la première grille
        new_lines1.extend(other.lines[int(round(self.n/2)):]) # avec la première moitié de la seconde grille

        new_lines2 = other.lines[:int(round(self.n/2))] # 2e moitié de la seconde grille
        new_lines2.extend(self.lines[int(round(self.n/2)):]) # avec la première moitié de la première

        new1 = BoardLine(self.n, new_lines1)
        new2 = BoardLine(self.n, new_lines2)

        print(new1)
        print(new2)
        return([new1, new2])

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
