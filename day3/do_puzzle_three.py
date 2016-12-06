"""
Let's do puzzle 3 from Advent of Code!

Looks like we might not need a class this time
"""

# start with 0 triangles counted
triangles = 0

# begin each column
column_one   = []
column_two   = []
column_three = []

# for each line in the data
for line in open('puzzle_three_data.txt', 'r').read().split('\n'):

    # remove any whitespace in the line
    sides = list(filter(None, line.split(' ')))
    sides = list(int(n) for n in sides)

    if sides:
        column_one.append(sides[0])
        column_two.append(sides[1])
        column_three.append(sides[2])

# combine the lists
column_one.extend(column_two)
column_one.extend(column_three)
columns = column_one

for a, b, c in zip(*[iter(columns)]*3):

    # check each pair of sides
    if a + b > c and a + c > b and b + c > a:

        # we have a triangle
        triangles = triangles + 1

print(triangles)
