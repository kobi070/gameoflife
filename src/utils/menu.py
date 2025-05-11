#!/usr/bin/env python3

import os
from typing import Callable
from dataclasses import dataclass
from gameoflife.src.utils.pretty_title import pretty_title
from main import game_loop, BASIC_CONFIG


@dataclass
class UserMenu:
    menu: str
    actions: dict[str, Callable]
    sub_menu: list = None

    def display_menu(self):
        while True:
            pretty_title("Game Of Life")
            user_input = input(self.menu).strip().lower()
            if user_input == "q":
                print("Exiting the menu...")
                break
            try:
                os.system("cls" if os.name == "nt" else "clear")
                self.actions[user_input]()
            except KeyError:
                print("Unknown action, try again")

    def add_action(self, action: str, func: Callable):
        self.actions[action] = func
        print(f"Function '{func.__name__}' added to action '{action}'.")


def change_grid_size():
    try:
        w = int(input("Enter new grid width: "))
        h = int(input("Enter new grid height: "))
        BASIC_CONFIG.setSize(width=w, height=h)
        print(f"Grid size set to {w}x{h}")
    except ValueError:
        print("Invalid input. Please enter integers.")


def change_threshold():
    try:
        th = float(input("Enter new threshold (0.0 to 1.0): "))
        if 0.0 <= th <= 1.0:
            BASIC_CONFIG.setThreshold(th)
            print(f"Threshold set to {th}")
        else:
            print("Threshold must be between 0.0 and 1.0")
    except ValueError:
        print("Invalid input. Please enter a float.")


def change_lifecycle():
    try:
        lfc = int(input("Enter number of lifecycles (e.g., 5, 10): "))
        if lfc > 0:
            BASIC_CONFIG.setLifecycle(lfc)
            print(f"Lifecycle count set to {lfc}")
        else:
            print("Lifecycle must be a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")


def change_char():
    ch = input("Enter a single character to represent living cells: ").strip()
    if len(ch) == 1:
        BASIC_CONFIG.setLiveCh(ch)
        print(f"Live cell character set to '{ch}'")
    else:
        print("Please enter a single character.")


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
4. Change which char is livin cells (#, *, Etc)
Q. Back
"""

    settings_menu = UserMenu(
        menu=sub_menu,
        actions={
            "1": change_grid_size,
            "2": change_threshold,
            "3": change_lifecycle,
            "4": change_char,
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
