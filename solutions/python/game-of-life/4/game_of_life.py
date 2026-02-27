"""Conway's Game of Life.

This module implements the Game of Life, a cellular automaton devised by the British
mathematician John Horton Conway in 1970. The game consists of a grid of cells that can
be in one of two states: alive or dead. The state of each cell changes based on the
number of alive neighbors it has, following specific rules.
"""

DIRECTIONS = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


def count_live_neighbors(matrix: list[list[int]], row: int, col: int) -> int:
    """Counts the number of live neighbors for a given cell in the matrix."""
    row_count = len(matrix)
    column_count = len(matrix[0])
    live_neighbor_count = 0
    for row_offset, col_offset in DIRECTIONS:
        neighbor_row = row + row_offset
        neighbor_col = col + col_offset
        if (
            0 <= neighbor_row < row_count
            and 0 <= neighbor_col < column_count
            and matrix[neighbor_row][neighbor_col] == 1
        ):
            live_neighbor_count += 1
    return live_neighbor_count


def tick(matrix: list[list[int]]) -> list[list[int]]:
    """Returns the next state of the matrix after applying the Game of Life rules."""
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = [[0] * cols for idx in range(rows)]
    for row in range(rows):
        for col in range(cols):
            live_neighbors = count_live_neighbors(matrix, row, col)
            cell = matrix[row][col]
            if cell == 1 and live_neighbors in {2, 3}:
                new_matrix[row][col] = 1
            elif cell == 0 and live_neighbors == 3:
                new_matrix[row][col] = 1
    return new_matrix


def evolve(matrix: list[list[int]], generations: int) -> list[list[int]]:
    """Return the state of the matrix after a given number of generations."""
    current = matrix
    remaining_generations = generations
    while remaining_generations > 0:
        current = tick(current)
        remaining_generations -= 1
    return current
