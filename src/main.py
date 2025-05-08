
def random_state(width: int, height: int) -> list[list[int]]:
    """ Generate a ramdom state for the game of life
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