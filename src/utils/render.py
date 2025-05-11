#!/usr/bin/env python3


def render(state: list[list[int]], living_ch: chr) -> str:
    """Render the game of life state as a string
    Args:
        state (list[list[int]]): State of the game of life
    Returns:
        str: Rendered state
    Example:
        >>> render([[0, 1], [1, 0]])
        '  #\n#  '
        >>> render([[1, 1], [1, 1]])
        '##\n##'
        >>> render([[0, 0], [0, 0]])
        '  \n  '
    """
    # Each string (alive, dead) represents how the console preseves 0/1
    # TODO: allow the user to chose which ch will represent alive string
    alive = living_ch
    dead = "    "

    # rendered_state holds the entire string which in printed into the
    rendered_state = "\n".join(
        ["".join([alive if cell else dead for cell in row]) for row in state]
    )
    return print(rendered_state)
