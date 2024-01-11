#!/usr/bin/python3
"""
Lock boxes keys and traversal
"""


def canUnlockAll(boxes):
    """
    checks if list boxes can open.
    """
    if len(boxes) == 1:
        return True
    if not boxes[0]:
        return False
    new = boxes[0].copy()
    create_dictionary = {f"{x}": boxes[x] for x in range(1, len(boxes))}
    states = [True]
    count = 500
    open_boxes = []
    while create_dictionary:
        for box, key in create_dictionary.items():
            for i in new:
                if i == int(box):
                    if key:
                        new += key
                    states.append(True)
                    open_boxes.append(box)
                    break
        if len(states) == len(boxes):
            return True
        if open_boxes:
            for open_boxe in open_boxes:
                if open_boxe not in create_dictionary.keys():
                    continue
                del create_dictionary[open_boxe]
        count -= 1
        if count == 0:
            return False


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]  # False
    print(canUnlockAll(boxes))
