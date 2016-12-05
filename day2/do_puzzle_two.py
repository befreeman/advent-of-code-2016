""" Complete the puzzle! """


from puzzle_two import Keypad


# create the keypad!
keypad = Keypad()

# for each line in the data file
combination = ''
for line in open('puzzle_two_data.txt', 'r').read().split('\n'):
    if len(line) > 0:
        for letter in line:
            if letter == 'U':
                keypad.move_up()
            elif letter == 'D':
                keypad.move_down()
            elif letter == 'L':
                keypad.move_left()
            elif letter == 'R':
                keypad.move_right()
        combination = combination + str(keypad.get_key())

print(combination)

