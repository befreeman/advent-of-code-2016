"""
Let's test the Keypad Class!
"""

import unittest

from puzzle_two import Keypad


class TestKeypad(unittest.TestCase):
    """ make sure keypad works as expected! """

    def setUp(self):
        """ set up an instance of keypad for the test cases """
        self.keypad = Keypad()

    def test_can_make_keypad(self):
        """ test the default keypad """

        # make sure we start on the middle key, 5
        self.assertTrue(self.keypad.row == 1)
        self.assertTrue(self.keypad.column == 1)

    def test_get_key(self):
        """ make sure that 'get_key' returns the expected value """
        # check the midle middle
        self.assertEqual(self.keypad.get_key(), 5)

        # check the top left
        self.keypad.row = 0
        self.keypad.column = 0
        self.assertEqual(self.keypad.get_key(), 1)

        # check the bottom right
        self.keypad.row = 2
        self.keypad.column = 2
        self.assertEqual(self.keypad.get_key(), 9)

    def test_move_up(self):
        """ make sure we move up correctly"""
        # make sure we move up from 1 to 0
        self.keypad.move_up()
        self.assertTrue(self.keypad.row == 0)

        # make sure that, when we can't move up, we stay at 0
        self.keypad.move_up()
        self.assertTrue(self.keypad.row == 0)

    def test_move_down(self):
        """ make sure we move down correctly """
        # make sure we can move down a row
        self.keypad.move_down()
        self.assertTrue(self.keypad.row == 2)

        # make sure that, when we can't move down, we stay at 2
        self.keypad.move_down()
        self.assertTrue(self.keypad.row == 2)

    def test_move_left(self):
        """ make sure we move left correctly """
        # make sure we move left from 1 to 0
        self.keypad.move_left()
        self.assertTrue(self.keypad.column == 0)

        # make sure that, when we can't move left, we stay at 0
        self.keypad.move_left()
        self.assertTrue(self.keypad.column == 0)

    def test_move_right(self):
        """ make sure we move down correctly """
        # make sure we can move down a row
        self.keypad.move_right()
        self.assertTrue(self.keypad.column== 2)

        # make sure that, when we can't move down, we stay at 2
        self.keypad.move_right()
        self.assertTrue(self.keypad.column== 2)

    def test_AoC_instructions(self):
        """ run through the AoC puzzle 2 example """
        # first row - ULL - ends at 1
        self.keypad.move_up()
        self.keypad.move_left()
        self.keypad.move_left()
        self.assertTrue(self.keypad.get_key() == 1)

        # second row - RRDDD - ends at 9
        self.keypad.move_right()
        self.keypad.move_right()
        self.keypad.move_down()
        self.keypad.move_down()
        self.keypad.move_down()
        self.assertTrue(self.keypad.get_key() == 9)

        # third row - LURDL - ends at 8
        self.keypad.move_left()
        self.keypad.move_up()
        self.keypad.move_right()
        self.keypad.move_down()
        self.keypad.move_left()
        self.assertTrue(self.keypad.get_key() == 8)

        # fourth row - UUUUD - ends at 5
        self.keypad.move_up()
        self.keypad.move_up()
        self.keypad.move_up()
        self.keypad.move_up()
        self.keypad.move_down()
        self.assertTrue(self.keypad.get_key() == 5)

