"""Solution to Ellen's Alien Game exercise."""


def new_aliens_collection(list_of_coords):
    return [Alien(*coords) for coords in list_of_coords]


class Alien:
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate, health=3):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = health
        Alien.total_aliens_created = Alien.total_aliens_created + 1

    def hit(self):
        self.health = self.health - 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, other_object):
        pass
