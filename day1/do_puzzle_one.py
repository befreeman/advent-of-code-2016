""" Complete the puzzle! """

from puzzle_one import Navigate

# create the navigator!
nav = Navigate()

# for each direction in the data file
for direction in open('puzzle_one_data.txt', 'r').read().split(' '):
    distance = int(direction[1:-1])
    if direction[0] == 'R':
        nav.travel_right(distance)
    else:
        nav.travel_left(distance)

print('Answer 1: {0}'.format(nav.get_distance()))
print('Answer 2: {0}'.format(nav.easter_bunny_hq_distance))
