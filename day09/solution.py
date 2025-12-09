from pathlib import Path
from dataclasses import dataclass

CURR_DIR = Path(__file__).parent
INPUT_PATH = CURR_DIR / "input.txt"


@dataclass(frozen=True, slots=True)
class Point:
    x: int
    y: int


def parse_input(text: str) -> list[Point]:
    lines = [
        Point(int(row[0]), int(row[1]))
        for row in [line.split(",") for line in text.splitlines() if line.strip()]
    ]
    return lines


def part1(input: list[Point]) -> int:
    result = 0
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            result = max(result, area(input[i], input[j]))
    return result



def part2(input: list[Point]) -> int:
    # first build the grid
    max_x = max(p.x for p in input)
    max_y = max(p.y for p in input)

    grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for g in grid:
        print(g)
    for p in input:
        grid[p.y][p.x] = '#'
    print('\n')
    for g in grid:
        print(g)
    for i in range(len(input)):
        p1 = input[i]
        p2 = input[(i + 1) % len(input)]  # Wrap around at the end
        # Draw line from p1 to p2
        draw_line(grid, p1, p2)  # Mark edge cells
    print('\n')
    for g in grid:
        print(g)
    print(max_x, max_y)
    return 0

def area(p1: Point, p2: Point) -> int:
    width = abs(1 + p1.x - p2.x)
    height = abs(1 + p1.y - p2.y)
    return width * height

def draw_line(grid: list[list[str]], p1: Point, p2: Point):
    if p1.y == p2.y:
        x_start = min(p1.x, p2.x)
        x_end = max(p1.x, p2.x)
        for x in range(x_start, x_end + 1):
            if grid[p1.y][x] not in '#X':
                grid[p1.y][x] = 'X'
    else:
        y_start = min(p1.y, p2.y)
        y_end = max(p1.y, p2.y)
        for y in range(y_start, y_end + 1):
            if grid[y][p1.x] not in '#X':
                grid[y][p1.x] = 'X'

def fill(grid: list[list[str]], points: list[Point]):
    # TODO
    return None

def main():
    text = INPUT_PATH.read_text().rstrip("\n")
    input = parse_input(text)

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
