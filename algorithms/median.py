
"""
Compute the running median of a sequence of numbers. That is, given a stream of numbers,
print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""
def median(lst):
    sorted_list = []
    for val in lst:
        added = False
        for i, sorted_val in enumerate(sorted_list):
            if val < sorted_val:
                sorted_list.insert(i, val)
                added = True
                break
        if not added:
            sorted_list.append(val)
        if len(sorted_list) % 2 != 0:
            print(sorted_list[int((len(sorted_list) - 1) / 2)])
        else:
            print((sorted_list[int((len(sorted_list) - 1) / 2)] + sorted_list[int((len(sorted_list) + 1) / 2)]) / 2)

median([2, 1, 5, 7, 2, 0, 5])
