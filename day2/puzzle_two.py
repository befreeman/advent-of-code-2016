"""
Let's solve Advent of Code Day 2!
"""


class Keypad(object):
    """ Hold onto your hat and lets decipher a keypad code! """

    def __init__(self):
        """ let's define the keypad state """
        self._row_one   = [1, 2, 3]
        self._row_two   = [4, 5, 6]
        self._row_three = [7, 8, 9]
        self.keypad = [self._row_one, self._row_two, self._row_three]

        # the keypad starts at number 5, row 2, column 2
        # but lists start counting at 0, so row 1, column 1
        self.row = 1
        self.column = 1

    def get_key(self):
        """ get the current key based on the row / column """
        return self.keypad[self.row][self.column]

    def move_up(self):
        """ move up on the keypad """
        if self.row > 0:
            self.row = self.row - 1

    def move_down(self):
        """ move down on the keypad """
        # make sure we don't go past the keypad length
        # just in case it might change
        if self.row < len(self._row_one) - 1:
            self.row = self.row + 1

    def move_left(self):
        """ move left on the keypad """
        if self.column > 0:
            self.column = self.column - 1

    def move_right(self):
        """ move right on the keypad """
        # make sure we don't go past the keypad length
        # just in case it might change
        if self.column < len(self.keypad) - 1:
            self.column = self.column + 1
