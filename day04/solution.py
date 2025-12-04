from pathlib import Path
from typing import List
from copy import deepcopy

CURR_DIR = Path(__file__).parent
INPUT_PATH = CURR_DIR / "input.txt"


def parse_input(text: str) -> List[List[str]]:
    return [list(line) for line in text.strip().splitlines()]


def part1(grid: List[List[str]]) -> int:
    result = 0
    for row_idx, row in enumerate(grid):
        for col_idx, val in enumerate(row):
            if val != '@':
                continue
            count = adjacent_count(grid, row_idx, col_idx, '@')
            if count < 4:
                result += 1
    return result


def part2(grid: List[List[str]]) -> int:
    result = 0
    while True:
        curr = 0
        for row_idx, row in enumerate(grid):
            for col_idx, val in enumerate(row):
                if val != '@':
                    continue
                count = adjacent_count(grid, row_idx, col_idx, '@')
                if count < 4:
                    # set each marker to '$' so it can be removed at the end of iteration
                    grid[row_idx][col_idx] = '$'
        curr = 0
        for row_idx, row in enumerate(grid):
            for col_idx, val in enumerate(row):
                if val == '$':
                    # mark as removed
                    grid[row_idx][col_idx] = '.'
                    curr +=1
        if curr == 0:
            break
        result+=curr
    return result

def adjacent_count(grid: List[List[str]], row: int, col: int, target: str) -> int:
    rows, cols = len(grid), len(grid[0])
    directions : List[tuple[int,int]] = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    count = 0
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if grid[new_row][new_col] == target:
                count+=1
    return count

def main():
    text = INPUT_PATH.read_text().rstrip("\n")
    data = parse_input(text)

    print("Part 1:", part1(deepcopy(data)))
    print("Part 2:", part2(deepcopy(data)))


if __name__ == "__main__":
    main()
