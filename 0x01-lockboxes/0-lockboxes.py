#!/usr/bin/python3

"""module"""


def canUnlockAll(boxes):
    # Keep track of the boxes that have been visited
    visited = [False] * len(boxes)
    visited[0] = True  # Mark the first box as visited

    # Create a queue to perform breadth-first search
    queue = [0]

    # Perform BFS
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < len(boxes) and not visited[key]:
                visited[key] = True
                queue.append(key)

    # Check if all boxes have been visited
    return all(visited)
