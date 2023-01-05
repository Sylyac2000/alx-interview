#!/usr/bin/python3
"""
function that determine if all boxes can be openned
"""


def canUnlockAll(boxes):

    if (type(boxes) is not list or len(boxes) == 0):
        return False
    # Set of boxes that we have keys for
    keys = set([0])

    # Queue of boxes to search through
    queue = set(boxes[0]).difference(set([0]))
    while len(queue) > 0:
        box = queue.pop()
        if not box or box >= len(boxes) or box < 0:
            continue
        if box not in keys:
            queue = queue.union(boxes[box])
            keys.add(box)
    # Return whether we have a key for all boxes
    return len(keys) == len(boxes)
