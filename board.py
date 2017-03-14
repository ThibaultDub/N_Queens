from random import randint, choice
import queen, position


class Board:
    def __init__(self, n=8):
        self.n = n
        self.pos = []
        self.queen_pos = []
        self.forbidden_pos = []

        for row in range(self.n):
            for col in range(self.n):
                self.pos.append(position.Position(row, col))

    def __repr__(self):
        string = (" _" * self.n + "\n")
        for row in range(self.n):
            string += ("|")
            for col in range(self.n):
                if queen.Queen(row, col) in self.queen_pos and queen.Queen(row, col) not in self.forbidden_pos:
                    string += ("D|")
                elif queen.Queen(row, col) in self.queen_pos and queen.Queen(row, col) in self.forbidden_pos:
                    string += ("X|")
                else:
                    string += ("_|")
            string += "\n"

        return string

    def add_queen(self, x, y):
        if position.Position(x, y) not in self.queen_pos:
            self.queen_pos.append(queen.Queen(x, y))

    def add_random_queens(self, number=1):
        for i in range(min(number, self.n * self.n)):
            x = randint(0, self.n - 1)
            y = randint(0, self.n - 1)
            while position.Position(x, y) in self.queen_pos:
                x = randint(0, self.n - 1)
                y = randint(0, self.n - 1)
            self.add_queen(x, y)

    def reset_board(self):
        self.queen_pos = []
        self.forbidden_pos = []

    def check_board(self):
        """iterates through queens and adds every position they can reach in the forbidden_pos attribute"""
        for queen in self.queen_pos:
            self.forbidden_pos.extend(queen.get_moving_pos(self.n))
        return self.forbidden_pos

    def fitness(self):
        """calculates the fitness of the board
        the fitness represents the number of queens on forbidden positions"""
        self.check_board()
        f = 0
        for queen in self.queen_pos:
            if queen in self.forbidden_pos:
                f += 1
        return f

    def neighbour(self):
        """transforms the board into a neighbour one
        two neighbour boards have only one queen which has moved of one position in any direction"""

        initial = self.queen_pos.pop(randint(0, len(self.queen_pos) - 1))  # we kick a random queen
        print(type(initial))
        new_queen = choice(initial.neighbour())
        while new_queen == initial:
            new_queen = choice(initial.neighbour())
        print("adding queen : " + str(new_queen))
        self.queen_pos.append(new_queen)
