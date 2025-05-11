#!/usr/bin/env python3

import os
from typing import Callable
from dataclasses import dataclass
from pretty_title import pretty_title
# from config import Config


@dataclass
class UserMenu:
    """
    ## UserMenu Class:
        - Displays a menu and executes the corresponding action based on user input.
        - The menu is displayed in a loop until the user chooses to quit.
        - The class allows passing arguments and keyword arguments to the actions.
    """

    menu: str
    actions: dict[str, Callable]
    sub_menu: list = None
    # config: Config = None

    def __post_init__(self):
        """
        Initializes the UserMenu class.
        """
        pass
        # self.config = Config()

    def display_menu(self):
        while True:
            pretty_title("Menu Creator")
            user_input = input(self.menu)
            if user_input == "q" or input == "Q":
                print("Exiting the menu...")
                break
            try:
                os.system("cls" if os.name == "nt" else "clear")
                self.actions[user_input]()
            except KeyError:
                print("Unknown action, try again")

    def add_action(self, action: str, func: Callable):
        """
        Adds a new action to the menu.
        """
        self.actions[action] = func
        print(f"Function '{func.__name__}' added to action '{action}'.")


def main():
    menu = """
    Choose an action:
    1. Start Game Of Life
    2. Settings Game Of Life
    Q. Quit
    """

    sub_menu_ec2 = """Settings:
    1. Change Grid Size (N x Ns)
    2. Change Threshold (0 -> 1.0)
    3. Change Lifecycle numbers (2 -> N)
    4. Change which char is livin cells (#, *, Etc)
    Q. BACK
    """

    actions = {
        "1": lambda: print("Starting GOL..."),
        "2": UserMenu(
            menu=sub_menu_ec2,
            actions={
                "1": lambda: print("Changing grid size..."),
                "2": lambda: print("Chagning threshhold..."),
                "3": lambda: print("Changing lifecycle number..."),
                "4": lambda: print("Changing char..."),
            },
        ).display_menu,
        "q": lambda: print("Going Back..."),
    }

    menu_instance = UserMenu(
        menu=menu,
        actions=actions,
    )
    menu_instance.display_menu()


if __name__ == "__main__":
    main()
