"""
Let's solve the first puzzle from Advent of Code!
"""


class Navigate(object):
    """ """
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
        self.location[self.facing] = self.location[self.facing] + distance

    def travel_left(self, distance):
        """ combine 'turn_left' and 'travel' """
        self.turn_left()
        self.travel(distance)

    def travel_right(self, distance):
        """ combine 'turn_right' and 'travel' """
        self.turn_right()
        self.travel(distance)

    def get_distance(self):
        """ get the total distance from where you started """
        x = abs(self.location['north'] - self.location['south'])
        y = abs(self.location['east'] - self.location['west'])
        return x + y
