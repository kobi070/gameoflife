#!/usr/bin/env python3
from pyfiglet import Figlet


def pretty_title(text: str):
    """
    ## Pretty Title Function:
        - Displays a title in a fancy ASCII art format.
        - Uses the Figlet library to create the ASCII art.
        - The text is centered and has a specified width.
    """
    f = Figlet("3d-ascii", justify="center", width=100)
    print(f.renderText(text))


if __name__ == "__main__":
    pass
