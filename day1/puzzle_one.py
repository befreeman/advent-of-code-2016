"""
Let's solve the first puzzle from Advent of Code!
"""


class Navigate(object):
    """ hold the logic for navigating the AoC puzzle 1 directions """

    def __init__(self):
        """ create the state for navigation """
        self.location = {
            'north': 0,
            'east' : 0,
            'south': 0,
            'west' : 0,
        }

        self.directions = ['north', 'east', 'south', 'west']
        self.facing = 'north'
        self.places_visited = set()
        self.easter_bunny_hq_visited = False
        self.easter_bunny_hq_distance = 0

    def _get_position(self):
        """ get the current position of 'facing' in 'directions' """
        return self.directions.index(self.facing)

    def turn_left(self):
        """ change direction to face left """
        self.facing = self.directions[self._get_position() - 1]

    def turn_right(self):
        """ change direction to face right """
        self.facing = self.directions[(self._get_position() + 1) % 4]

    def travel(self, distance):
        """ go the distance specified in the instruction """
        for unit in range(distance):
            self.location[self.facing] = self.location[self.facing] + 1
            self._store_state()

    def travel_left(self, distance):
        """ combine 'turn_left' and 'travel' """
        self.turn_left()
        self.travel(distance)

    def travel_right(self, distance):
        """ combine 'turn_right' and 'travel' """
        self.turn_right()
        self.travel(distance)

    def _get_grid_coordinates(self):
        """ convert the location dictionary to x / y coordinates """
        x = self.location['north'] - self.location['south']
        y = self.location['east'] - self.location['west']
        return x, y

    def get_distance(self):
        """ get the total distance from where you started """
        x, y = self._get_grid_coordinates()
        return abs(x) + abs(y)

    def _store_state(self):
        """ store the location visited in x, y after each unit of travel """
        x, y = self._get_grid_coordinates()
        if (x, y) in self.places_visited and not self.easter_bunny_hq_visited:
            self.easter_bunny_hq_visited = True
            self.easter_bunny_hq_distance = self.get_distance()
        else:
            self.places_visited.add((x, y))
