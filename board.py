from random import randint, choice
import queen, position


class Board:
    def __init__(self, n=8, queen_pos=[]):
        self.n = n
        self.pos = []
        self.queen_pos = queen_pos
        self.forbidden_pos = []

        for row in range(self.n):
            for col in range(self.n):
                self.pos.append(position.Position(row, col))
        for queen in queen_pos:
            self.update_forbidden(queen)

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
        new_queen = queen.Queen(x, y)
        if new_queen not in self.queen_pos:
            self.queen_pos.append(new_queen)
            self.update_forbidden(new_queen)
            return True  # Adding successful
        return False  # Adding successful

    def update_forbidden(self, new_queen):
        self.forbidden_pos.extend(new_queen.get_moving_pos(self.n))

    def add_random_queens(self, number=1):
        for i in range(number):
            new = choice(self.pos)
            while not self.add_queen(new.x, new.y):
                new = choice(self.pos)

    def reset_board(self):
        self.queen_pos = []
        self.forbidden_pos = []

    def fitness(self):
        """calculates the fitness of the board
        the fitness represents the number of queens on forbidden positions"""
        f = 0
        for queen in self.queen_pos:
            if queen in self.forbidden_pos:
                f += 1
        return f

    def neighbour(self):
        """transforms the board into a neighbour one
        two neighbour boards have only one queen which has moved of one position in any direction"""

        new_queens = self.queen_pos

        initial = new_queens.pop(randint(0, len(new_queens) - 1))  # we kick a random queen
        neighbours = initial.get_neighbours_pos(self.n)
        new_queen = choice(neighbours)
        while new_queen == initial or new_queen in new_queens:
            new_queen = choice(initial.get_neighbours_pos(self.n))
        new_queens.append(new_queen)
        return Board(self.n, new_queens)

