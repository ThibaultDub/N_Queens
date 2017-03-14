import position


class Queen(position.Position):

    def get_moving_pos(self, n):
        moving_pos = []
        for row in range(n):  # horizontally
            if position.Position(row, self.y) != self:
                moving_pos.append(position.Position(row, self.y))
        for col in range(n):  # vertically
            if position.Position(self.x, col) != self:
                moving_pos.append(position.Position(self.x, col))
        for i in range(-n, n):  # diagonally
            x = self.x - i
            y = self.y - i
            if x >= 0 and y >= 0 and position.Position(x, y) != self:
                moving_pos.append(position.Position(x, y))
            x = self.x - i
            y = self.y + i
            if x < n and y < n and position.Position(x, y) != self:
                moving_pos.append(position.Position(x, y))
        return moving_pos
