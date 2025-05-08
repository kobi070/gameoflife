#!/usr/bin/env python3
import random


def random_state(width: int, height: int) -> list[list[int]]:
    """Generate a ramdom state for the game of life
    Args:
        width (int): Width of the state
        height (int): Height of the state
    Returns:
        list[list[int]]: Random state
    Example:
        >>> random_state(3, 3)
        [[0, 1, 0], [1, 0, 1], [0, 0, 1]]
        >>> random_state(2, 2)
        [[1, 0], [0, 1]]
        >>> random_state(1, 1)
        [[0]]
        >>> random_state(0, 0)
        []
    """
    # Initialize the state with all dead cells
    state = dead_state(width, height)

    # Randomly set some cells to alive
    for i in range(height):
        for j in range(width):
            # Set the cell to alive with a 50% chance
            state[i][j] = random_cell(threshold=0.5)
    return state


def random_cell(threshold: float) -> int:
    """Generate a random boolean value based on a threshold
    Args:
        threshold (float): Threshold for the random number
    Returns:
        bool: 1 if the random number is less than the threshold, 0 otherwise
    Example:
        >>> random(0.5)
        1
        >>> random(0.1)
        0
        >>> random(0.9)
        1
    """
    random_number = random.random()

    if random_number < threshold:
        return 1
    else:
        return 0


def dead_state(width: int, height: int) -> list[list[int]]:
    """Generate a dead state for the game of life
    Args:
        width (int): Width of the state
        height (int): Height of the state
    Returns:
        list[list[int]]: Dead state
    Example:
        >>> dead_state(3, 3)
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        >>> dead_state(2, 2)
        [[0, 0], [0, 0]]
        >>> dead_state(1, 1)
        [[0]]
        >>> dead_state(0, 0)
        []
    """
    state = [[0 for _ in range(width)] for _ in range(height)]
    return state
