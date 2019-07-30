import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(funcName)s[%(lineno)d] %(message)s"
)

matrix = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
not_yet_visited = [[True, True, True], [True, True, True], [True, True, True]]

def go_right(row, start, end):
    for i in range(start, end):
        if not_yet_visited[row][i]:
            not_yet_visited[row][i] = False
            logging.info(matrix[row][i])


def go_down(col, start, end):
    for i in range(start, end):
        if not_yet_visited[i][col]:
            not_yet_visited[i][col] = False
            logging.info(matrix[i][col])

def go_left(row, start, end):
    for i in range(start - 1, end - 1, -1):
        if not_yet_visited[row][i]:
            not_yet_visited[row][i] = False
            logging.info(matrix[row][i])


def go_up(col, start, end):
    for i in range(start - 1, end - 1, -1):
        if not_yet_visited[i][col]:
            not_yet_visited[i][col] = False
            logging.info(matrix[i][col])


go_right(0, 0, 3)
go_down(2, 0, 3)
go_left(2, 3, 0)
go_up(0, 3, 0)
