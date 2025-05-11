#!/usr/bin/env python3

import random
import time
from src.utils.render import render
from src.utils.config import Config
from utils.menu import (
    UserMenu,
    change_char,
    change_grid_size,
    change_lifecycle,
    change_threshold,
)  # Importing UserMenu and etc from menu.py

# Global config object to update settings
BASIC_CONFIG = Config(width=10, height=10, threshhold=0.5, lifecycle=5, living_ch="■")


def random_state(width: int, height: int) -> list[list[int]]:
    """Generate a random state for the game of life."""
    state = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            state[i][j] = random_cell(threshold=0.5)
    return state


def random_cell(threshold: float) -> int:
    """Generate a random boolean value based on a threshold."""
    random_number = random.random()
    return 1 if random_number < threshold else 0


def dead_state(width: int, height: int) -> list[list[int]]:
    """Generate a dead state for the game of life."""
    return [[0 for _ in range(width)] for _ in range(height)]


def count_neighbors(
    state: list[list[int]], x: int, y: int, rows: int, cols: int
) -> int:
    """Count all live neighbors around (x, y)."""
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
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
            if state[i][j] == 1:
                if neighbors in [2, 3]:
                    nx_state[i][j] = 1  # Survives
                else:
                    nx_state[i][j] = 0  # Dies
            else:
                if neighbors == 3:
                    nx_state[i][j] = 1  # Reproduction
    return nx_state


def game_loop(config: Config) -> None:
    """Main game loop that runs the Game of Life."""
    state = random_state(config.width, config.height)
    render(state=state, living_ch=config.living_ch)
    for cycle in range(config.lifecycle):
        print(f"\nCycle: {cycle + 1}/{config.lifecycle}")
        render(state=state, living_ch=config.living_ch)
        state = next_state(state)
        time.sleep(0.5)  # Adjust speed here


def main():
    menu = """
Choose an action:
1. Start Game Of Life
2. Settings Game Of Life
Q. Quit
"""

    sub_menu = """
Settings:
1. Change Grid Size (N x N)
2. Change Threshold (0 -> 1.0)
3. Change Lifecycle numbers (2 -> N)
4. Change which char is living cells (#, *, Etc)
Q. Back
"""

    settings_menu = UserMenu(
        menu=sub_menu,
        actions={
            "1": lambda: change_grid_size(BASIC_CONFIG),
            "2": lambda: change_threshold(BASIC_CONFIG),
            "3": lambda: change_lifecycle(BASIC_CONFIG),
            "4": lambda: change_char(BASIC_CONFIG),
        },
    )

    actions = {
        "1": lambda: game_loop(config=BASIC_CONFIG),
        "2": settings_menu.display_menu,
        "q": lambda: print("Quitting..."),
    }

    menu_instance = UserMenu(
        menu=menu,
        actions=actions,
    )
    menu_instance.display_menu()


if __name__ == "__main__":
    main()
