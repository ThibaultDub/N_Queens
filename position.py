class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"

    def get_neighbours_pos(self, n):
        """returns a list containing all the positions of """
        initial_neighbours = [Position(self.x - 1, self.y),
                              Position(self.x - 1, self.y - 1),
                              Position(self.x - 1, self.y + 1),
                              Position(self.x, self.y - 1),
                              Position(self.x, self.y + 1),
                              Position(self.x + 1, self.y),
                              Position(self.x + 1, self.y - 1),
                              Position(self.x + 1, self.y + 1)]
        neighbours = []
        for neighbour in initial_neighbours:
            if not (neighbour.x > n - 1 or neighbour.y > n - 1 or neighbour.x < 0 or neighbour.y < 0):
                neighbours.append(neighbour)

        return neighbours
