from enum import Enum
import copy


class Direction(Enum):
    N = (-1, 0)  # Up
    E = (0, 1)   # Right
    S = (1, 0)   # Down
    W = (0, -1)  # Left


with open("inputs/06.txt", "r") as f:
    lines = f.readlines()
initial_grid = [list(l.strip()) for l in lines]
initial_dir = Direction.N


def find_start(grid):
    for x, row in enumerate(grid):
        if "^" in row:  # Find the '^' character
            return (x, row.index("^"))


def get_next_pos(pos, direction):
    return (pos[0] + direction.value[0], pos[1] + direction.value[1])


def is_blocked(grid, start_pos, start_dir, block_pos):
    test_grid = [row[:] for row in grid]
    test_grid[block_pos[0]][block_pos[1]] = "#"

    visited = set()
    pos = start_pos
    direction = start_dir

    while True:
        if (pos, direction) in visited:
            return True  # Loop detected
        visited.add((pos, direction))

        next_pos = get_next_pos(pos, direction)

        if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
            return False  # Guard exits grid

        if test_grid[next_pos[0]][next_pos[1]] == "#":
            direction = order[(order.index(direction) + 1) % 4]
        else:
            pos = next_pos


def solve(grid, start_pos, start_dir):
    visited = set()
    blocked_positions = set()
    pos = start_pos
    direction = start_dir

    visited.add(pos)
    order = [Direction.N, Direction.E, Direction.S, Direction.W]

    while True:
        visited.add(pos)
        next_pos = get_next_pos(pos, direction)

        if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
            break  # Guard exits the grid

        block_pos = get_next_pos(pos, direction)
        if (
            0 <= block_pos[0] < len(grid) and
            0 <= block_pos[1] < len(grid[0]) and
            grid[block_pos[0]][block_pos[1]] == "." and  # Must be an empty spot
            block_pos != start_pos                      # Can't block the start position
        ):
            if is_blocked(grid, start_pos, start_dir, block_pos):
                blocked_positions.add(block_pos)

        if grid[next_pos[0]][next_pos[1]] == "#":
            direction = order[(order.index(direction) + 1) % 4]
        else:
            pos = next_pos

    return len(visited), len(blocked_positions)


initial_pos = find_start(initial_grid)
initial_grid[initial_pos[0]][initial_pos[1]] = "."
order = [Direction.N, Direction.E, Direction.S, Direction.W]

part1, part2 = solve(initial_grid, initial_pos, initial_dir)

print("Part 1:", part1)
print("Part 2:", part2)

