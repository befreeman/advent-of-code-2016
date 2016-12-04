"""
Test the Navigate class!
"""

import unittest

from puzzle_one import Navigate


class TestNavigate(unittest.TestCase):
    """ Make sure Navigate works correctly """

    def setUp(self):
        """ create a Navigate object for each test """
        self.nav = Navigate()

    def test_can_create_navigate(self):
        """ make sure we can make Navigate and it is configured correctly """
        nav = Navigate()
        self.assertTrue(nav)
        self.assertEqual(nav.location['north'], 0)
        self.assertEqual(nav.location['east'], 0)
        self.assertEqual(nav.location['south'], 0)
        self.assertEqual(nav.location['west'], 0)
        self.assertEqual(nav.facing, 'north')
        self.assertTrue(nav.directions[0] == nav.facing)

    def test_turn_left(self):
        """ make sure 'turn_left' changes 'facing' to the left """
        # face west
        self.nav.turn_left()
        self.assertTrue(self.nav.facing == 'west')

        # face south
        self.nav.turn_left()
        self.assertTrue(self.nav.facing == 'south')

    def test_turn_right(self):
        """ make sure 'turn_right' changes 'facing' to the right """
        # face east
        self.nav.turn_right()
        self.assertTrue(self.nav.facing == 'east')

        # set 'facing' to 'west' to see that it jumps position in the list
        self.nav.facing = 'west'
        self.nav.turn_right()
        self.assertTrue(self.nav.facing == 'north')

    def test_travel(self):
        """ make sure we travel in the intended direction """

        # travel 4 from the original facing
        self.nav.travel(4)
        self.assertTrue(self.nav.location[self.nav.facing] == 4)

        # travel 3 from a new direction
        self.nav.facing = 'south'
        self.nav.travel(3)
        self.assertTrue(self.nav.location[self.nav.facing] == 3)

        # check that backtracking works on the original facing
        self.nav.facing = 'north'
        self.nav.travel(-2)
        self.assertTrue(self.nav.location[self.nav.facing] == 2)

    def test_distance(self):
        """ make sure we track distance from the origin correctly """
        # R2 L3 - 5 blocks away
        self.nav.travel_right(2)
        self.nav.travel_left(3)
        self.assertTrue(self.nav.get_distance() == 5)

        # reset nav
        self.nav = Navigate()

        # R2 R2 R2 - 2 blocks away
        self.nav.travel_right(2)
        self.nav.travel_right(2)
        self.nav.travel_right(2)
        self.assertTrue(self.nav.get_distance() == 2)

        # reset nav
        self.nav = Navigate()

        # R5 L5 R5 R3 - 12 blocks away
        self.nav.travel_right(5)
        self.nav.travel_left(5)
        self.nav.travel_right(5)
        self.nav.travel_right(3)
        self.assertTrue(self.nav.get_distance() == 12)

if __name__ == '__main__':
    unittest.main()
