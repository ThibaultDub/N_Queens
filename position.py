class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.is_occupied = False
        # self.is_forbidden = False

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"

    def get_neighbours_pos(self, n):
        """returns a list containing all the positions of """
        neighbours = {(self.x - 1, self.y), (self.x - 1, self.y - 1), (self.x - 1, self.y + 1), (self.x, self.y - 1),
                      (self.x, self.y + 1), (self.x + 1, self.y), (self.x + 1, self.y - 1), (self.x + 1, self.y + 1)}
        if self.x == 0:
            neighbours.remove((self.x - 1, self.y))
            neighbours.remove((self.x - 1, self.y + 1))
            neighbours.remove((self.x - 1, self.y - 1))
        elif self.x == n - 1:
            neighbours.remove((self.x + 1, self.y))
            neighbours.remove((self.x + 1, self.y + 1))
            neighbours.remove((self.x + 1, self.y - 1))
        if self.y == 0:
            neighbours.remove((self.x, self.y - 1))
            neighbours.remove((self.x + 1, self.y - 1))
            neighbours.remove((self.x - 1, self.y - 1))

        elif self.y == n - 1:
            neighbours.remove((self.x, self.y + 1))
            neighbours.remove((self.x + 1, self.y + 1))
            neighbours.remove((self.x - 1, self.y + 1))

        return neighbours
