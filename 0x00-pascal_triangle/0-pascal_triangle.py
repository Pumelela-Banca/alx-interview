#!/usr/bin/python3

"""
Contains funtion that prints a list of arrays
"""


def pascal_triangle(n):
    """
    It returns triangular lists
    """
    if n <= 0:
        return []

    all_list = [[1], [1, 1]]
    if n == 1:
        return [1]
    elif n == 2:
        return all_list
    else:
        on = [1, 1]
        new = [1]
        for x in range(2, n):
            for y in range(len(on)):
                if y == len(on) - 1:
                    new.append(1)
                    all_list.append(new)
                    on = new
                    new = [1]
                    continue
                new.append(on[y] + on[y + 1])
        return all_list


if __name__ == "__main__":
    print(pascal_triangle(5))
