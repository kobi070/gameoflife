#!/usr/bin/env python3
import random
import time
from render import render
from dataclasses import dataclass

"""
Rules:
        Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
        Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
        Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
        Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
"""


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


def count_neighbors(
    state: list[list[int]], x: int, y: int, rows: int, cols: int
) -> int:
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


def next_state(state: list[list[int]]) -> list[list[int]]:
    """Generate the next board state based on Game of Life rules."""
    rows, cols = len(state), len(state[0])
    nx_state = dead_state(width=rows, height=cols)

    for i in range(rows):
        for j in range(cols):
            neighbors = count_neighbors(state, i, j, rows, cols)
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


@dataclass
class Config:
    """Defines the params we allow the user to change in the game settings"""

    width: int
    height: int
    threshhold: float
    lifecycle: int
    living_ch: chr

    def setSize(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def setThreshold(self, th: float) -> None:
        self.threshhold = th

    def setLifecycle(self, lfc: int) -> None:
        self.lifecycle = lfc

    def setLiveCh(self, liveCh: chr) -> None:
        self.living_ch = liveCh


def game_loop(config: Config) -> None:
    """Main game loop that runs the Game of Life."""
    state = random_state(config.width, config.height)

    for cycle in range(config.lifecycle):
        print(f"\nCycle: {cycle + 1}/{config.lifecycle}")
        render(state=state, living_ch=config.living_ch)
        state = next_state(state)
        time.sleep(0.5)  # Adjust speed here


if __name__ == "__main__":
    # Example configuration
    config = Config(
        width=10,
        height=10,
        threshhold=0.5,
        lifecycle=20,
        living_ch="■",  # Unicode square character
    )
    game_loop(config)
