
def edit_dist(from_str, to_str, m, n):
    if m == len(from_str):
        return len(from_str) - n
    if n == len(to_str):
        return len(to_str) - m
    if from_str[m] == to_str[n]:
        return edit_dist(from_str, to_str, m + 1, n + 1)

    return 1 + min(edit_dist(from_str, to_str, m + 1, n),
                   edit_dist(from_str, to_str, m, n + 1),
                   edit_dist(from_str, to_str, m + 1, n + 1))

print(edit_dist('kitteng', 'bittnd', 0, 0))
print(edit_dist('saturday', 'sunday', 0, 0))

a = []
[a.append(x) for x in range(10)]
print(a)

b = [x for x in range(10)]
print(b)

for x in range(10):
    print(x)

print([x for x in range(10)])
