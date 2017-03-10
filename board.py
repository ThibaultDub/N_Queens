from random import randint, choice


class Board:
    def __init__(self, n):
        self.n = n
        self.pos = [] #todo : change into set()
        self.forbidden_pos = []

    def __repr__(self):
        string = (" _" * self.n + "\n")
        for row in range(self.n):
            string += ("|")
            for col in range(self.n):
                if [row, col] in self.pos and not [row, col] in self.forbidden_pos:
                    string += ("D|")
                elif [row, col] in self.forbidden_pos and [row, col] in self.pos:
                    string += ("X|")
                else:
                    string += ("_|")
            string += "\n"

        return string

    def add_queen(self, x, y):
        if [x, y] not in self.pos:
            self.pos.append([x, y])

    def add_random_queens(self, number=1):
        for i in range(min(number, self.n * self.n)):
            x = randint(0, self.n - 1)
            y = randint(0, self.n - 1)
            while [x, y] in self.pos:
                x = randint(0, self.n - 1)
                y = randint(0, self.n - 1)
            self.add_queen(x, y)

    def reset_board(self):
        self.pos = []
        self.forbidden_pos = []

    def check_board(self):
        """iterates through queens and adds every position they can reach in the forbidden_pos attribute"""
        for queen in self.pos:
            for row in range(self.n):  # horizontally
                if [row, queen[1]] != queen:
                    self.forbidden_pos.append([row, queen[1]])
            for col in range(self.n):  # vertically
                if [queen[0], col] != queen:
                    self.forbidden_pos.append([queen[0], col])
            for i in range(-self.n, self.n):  # diagonally
                x = queen[0] - i
                y = queen[1] - i
                if x >= 0 and y >= 0 and [x, y] != queen:
                    self.forbidden_pos.append([x, y])
                x = queen[0] - i
                y = queen[1] + i
                if x < self.n and y < self.n and [x, y] != queen:
                    self.forbidden_pos.append([x, y])
        return self.forbidden_pos

    def fitness(self):
        """calculates the fitness of the board
        the fitness represents the number of queens on forbidden positions"""
        self.check_board()
        f = 0
        for queen in self.pos:
            if queen in self.forbidden_pos:
                f += 1
        return f

    def neighbour(self):
        """transforms the board into a neighbour one
        two neighbour boards have only one different queen"""
        print(self.pos)
        initial = self.pos.pop(randint(0,len(self.pos)-1)) # we kick a random element from
        x = randint(0, self.n)
        y = randint(0, self.n)
        while [x, y] == initial:
            x = randint(0, self.n)
            y = randint(0, self.n)
        self.pos.append([x, y])
        print(self.pos)
