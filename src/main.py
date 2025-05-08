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
    pass


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


state = dead_state(3, 3)
print(state)
