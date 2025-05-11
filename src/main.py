#!/usr/bin/env python3
import random
from enum import Enum


class CellStatus(Enum):
    DEAD = 0
    ALIVE = 1


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


def next_state(state: list[list[int]]) -> list[list[int]]:
    """Generate the next board state game based on the rule of game of life
    Args:
        state (list[list[int]]): current state
    Returns:
        list[list[int]]: Next state
    Rules:
        Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
        Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
        Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
        Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
    """
    # Initialize the next state as a dead_state
    nx_state = dead_state(width=len(state), height=len(state))
    for i in range(len(state)):
        for j in range(len(state)):
            if is_edge(x=i, y=j, length=len(state)):
                # Checks the sum of 3 neighbors
                sum_of_3 = state[i + 1, j] + state[i, j + 1] + state[i + 1, j + 1]
                if sum_of_3 in [0, 1]:
                    nx_state[i][j] = CellStatus.DEAD.value

                if sum_of_3 in [2, 3]:
                    nx_state[i][j] = CellStatus.ALIVE.value

                if is_alive(num=state[i][j]) is CellStatus.DEAD and sum_of_3 == 3:
                    nx_state[i][j] = CellStatus.ALIVE.value

                if is_alive(num=state[i][j]) is CellStatus.ALIVE and sum_of_3 > 3:
                    nx_state[i][j] = CellStatus.DEAD.value

            elif is_middle(x=i, y=j, length=len(state)):
                pass
            else:
                print("We are on a cell with eight neighbors")
    pass


def count_neighbors(state: list[list[int]], x: int, y: int, rows: int, cols: int) -> int:
    # Count all live neighbors around (x, y)
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            count += state[nx][ny]
    return count


def next_state_v2(state: list[list[int]]) -> list[list[int]]:
    """Generate the next board state based on Game of Life rules."""
    rows, cols = len(state), len(state[0])
    nx_state = dead_state(width=rows, height=cols)

    for i in range(rows):
        for j in range(cols):
            neighbors = count_neighbors(i, j)
            if state[i][j] == 1:  # Alive
                if neighbors in [2, 3]:
                    nx_state[i][j] = 1  # Survives
                else:
                    nx_state[i][j] = 0  # Dies
            else:  # Dead
                if neighbors == 3:
                    nx_state[i][j] = 1  # Reproduction
                else:
                    nx_state[i][j] = 0  # Stays dead

    return nx_state


def is_edge(x: int, y: int, length: int) -> bool:
    """Checks if the cell is the edge of the grid"""
    # Edges = [0,0], [0, N-1], [N-1, 0], [N-1, N-1] where N = length of the 2D Array
    # if N = even => N = 4 => 3 * 2 = 9 is the last sum of cells
    # if N = odd => N = 5 => 4 * 2 = 4 is the last sum of cells
    sum_of_index = x + y
    return (
        sum_of_index == 0
        or sum_of_index == (length - 1)
        or sum_of_index == (2 * (length - 1))
    )


def is_middle(x: int, y: int, length: int) -> bool:
    """Checks if we are on the first/last row/col in the middle of the row/col"""
    coord_possible_vals = [a for a in range(1, length)]
    coord_possible_pair = [a for a in range(1, length - 1)]

    if (
        x in coord_possible_vals
        and y in coord_possible_pair
        or y in coord_possible_vals
        and x in coord_possible_pair
    ):
        return True
    return False


def is_alive(num: int) -> CellStatus:
    if num == CellStatus.ALIVE:
        return CellStatus.ALIVE
    return CellStatus.DEAD


print(is_alive(num=1))
