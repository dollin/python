
"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that
all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.
For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""
def sort_rgb(array):
    r = 0
    g = 0
    b = 0
    for x in array:
        r += 1 if x == 'R' else 0
        g += 1 if x == 'G' else 0
        b += 1 if x == 'B' else 0

    print(f'{r}, {g}, {b}')
    array[:r] = ['R'] * r
    array[r: r + g] = ['G'] * g
    array[r + g: r + g + b] = ['B'] * b


arr = ['R', 'B', 'G', 'R', 'G', 'B', 'G', 'B']
print(','.join(arr))
sort_rgb(arr)
print(','.join(arr))
