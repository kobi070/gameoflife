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
    # apply the rules to the next_grid_state without touching the last state we recived
    next_grid_state = dead_state(width=len(state), height=len(state))

    # To keep in ming all edgeds of the grid have only 3 nieghbors
    # All top rows and colums which is 0 or n -1 (length of the row/column) have 5 neighbors
    # Only the middle of the grid have the max amount of neighbors which is 8
    # Example:
    # [0,0,0]
    # [0,1.0]
    # [0,0,1]
    # On [0,0] the neighbors are => [0,1] && [1,0]
    # On [0,1] the neighbors are => [0,0], [0,2], [1,0], [1,1], [1,2]
    # Only on [1,1] all the grid are is neighbors

    # Loop the entire of the grid (not the best soulution but the first solution we will try)
    # Rule 1 : Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
    for i in range(len(state)):
        for j in range(len(state)):
            if(is_edge(x=i, y=j, length=len(state))):
                print("We are on the edge of the grid therfore have 3 neighbors")
            elif(is_middle(x=i, y=j, length=len(state))):
                print("We are on middle of first/last row/cols therfore have 5 neighbors")
    pass


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
    pass
ans = is_edge(x=4, y=4, length=5)
print(ans)
