# Globals for the directions
# Change the values as you see fit
EAST = 2
NORTH = 1
WEST = 0
SOUTH = 3


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, moves):
        for move in moves:
            if move == "R":
                self.direction += 1
                self.direction %= 4
            elif move == "L":
                self.direction += 3
                self.direction %= 4
            elif move == "A":
                if self.direction == EAST:
                    self.coordinates = (self.coordinates[0]+1, self.coordinates[1])
                elif self.direction == WEST:
                    self.coordinates = (self.coordinates[0]-1, self.coordinates[1])
                elif self.direction == NORTH:
                    self.coordinates = (self.coordinates[0], self.coordinates[1]+1)
                elif self.direction == SOUTH:
                    self.coordinates = (self.coordinates[0], self.coordinates[1]-1)