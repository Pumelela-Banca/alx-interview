#!/usr/bin/python3
"""
rotate 2-D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    rotates 2-D matrix 90 degrees clockwise
    """
    N = len(matrix)
    for x in range(0, int(N / 2)):
        for y in range(x, N - x - 1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[N - 1 - y][x]
            matrix[N - 1 - y][x] = matrix[N - 1 - x][N - 1 - y]
            matrix[N - 1 - x][N - 1 - y] = matrix[y][N - 1 - x]
            matrix[y][N - 1 - x] = temp

if __name__ == "__main__":
    matrix = [[1, 2, 3,4],
              [4, 5, 6,33],
              [7, 8, 9,12]]

    rotate_2d_matrix(matrix)
    print(matrix)
