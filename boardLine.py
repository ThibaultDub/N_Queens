import random


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
        # self.atr_fitness = self.fitness() # TODO : Changer le recuit pour prendre en compte l'attribut fitness

                # self.queens = [line.queen for line in self.columns]

    def __repr__(self):
        string = " _" * self.n + "\n"
        for col in self.lines:
            string += col.__repr__()
            string += "\n"
        return string

    def fitness(self):  # A RETESTER ET DEBUGGER
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



    def neighbours(self):
        neighbourhood = set()
        for i in range(self.n):
            for j in range(i):
                temp = self.lines.copy()
                x = temp[i]
                temp[i] = temp[j]
                temp[j] = x
                new_board = BoardLine(self.n, temp)
                neighbourhood.add(new_board)
        return neighbourhood


    def random_neighbour(self):
        i = random.randint(0,self.n-1)
        j=random.randint(0,self.n-1)
        while i==j:
            j=random.randint(0,self.n-1)
        temp = self.lines.copy()
        x = temp[i]
        temp[i] = temp[j]
        temp[j] = x
        return BoardLine(self.n, temp)


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

    # @property
    # def queen(self):
    #     return self.queen



        # @queen.setter
        # def queen(self, queen):
        #     self.queen = queen
