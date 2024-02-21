#!/usr/bin/python3
"""
rotate 2-D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    rotates 2-D matrix 90 degrees clockwise
    """
    n = len(matrix)
    for x in range(0, int(n / 2)):
        for y in range(x, n - x - 1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[n - 1 - y][x]
            matrix[n - 1 - y][x] = matrix[n - 1 - x][n - 1 - y]
            matrix[n - 1 - x][n - 1 - y] = matrix[y][n - 1 - x]
            matrix[y][n - 1 - x] = temp


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 63],
              [7, 8, 92]]

    rotate_2d_matrix(matrix)
    print(matrix)
