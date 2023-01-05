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
    queue = [0]

    # While there are boxes to search through
    while queue:
        # Take the next box
        box = queue.pop(0)
        list_key = boxes[box]
        # For each key in the box
        for key in list_key:
            # If we don't have a key for this box yet
            if key not in keys:
                # Add the key and the box to our sets
                keys.add(key)
                queue.append(key)

    # Return whether we have a key for all boxes
    return len(keys) == len(boxes)
