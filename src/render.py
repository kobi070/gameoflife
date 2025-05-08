#!/usr/bin/env python3


def render(state: list[list[int]]) -> str:
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
    return "\n".join(["".join(["#" if cell else " " for cell in row]) for row in state])


board = [[0, 1, 0], [1, 0, 1], [0, 0, 1]]
print(render(board))
