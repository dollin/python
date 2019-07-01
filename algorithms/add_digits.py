import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] [%(threadName)s] %(funcName)s:%(lineno)d %(message)s',
)

class AddDigits:

    """
    defdef addDigits(self, num: int) -> int:
    def add_digits(self, num):
    """
    def add_digits(self, num):
        if num < 10:
            return num
        while num > 0:
            total = num % 10
            num //= 10
            num += total
            if num < 10:
                return num


def main():
    ad = AddDigits()
    logging.info(ad.add_digits(12384))


if __name__ == '__main__':
    main()


def traverse(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))


def dfs(i, j):
    if (i, j) in visited:
        return
    visited.add((i, j))
    # Traverse neighbors
    for direction in directions:
        next_i, next_j = i + direction[0], j + direction[1]
        if 0 <= next_i < rows and 0 <= next_j < cols: # Check boundary
            # Add any other checking here ^
            dfs(next_i, next_j)


# for i in range(rows):
#     for j in range(cols):
#         dfs(i, j)

