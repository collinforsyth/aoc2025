# aoc2025/day1/solution.py
from pathlib import Path

CURR_DIR = Path(__file__).parent
INPUT_PATH = CURR_DIR / "input.txt"


def parse_input(text: str):
    return [line.strip() for line in text.splitlines() if line.strip()]


def part1(data: str) -> int:
    start = 50
    count = 0
    for instruction in data:
        if instruction.startswith("L"):
            start -= int(instruction[1:])
        else:
            start += int(instruction[1:])
        start %= 100
        if start == 0:
            count += 1
    return count


def part2(data: str) -> int:
    start = 50
    count = 0
    for instruction in data:
        dist = int(instruction[1:])
        if instruction.startswith("L"):
            # distance to previous multiple of 100
            offset = start % 100
            if offset == 0:
                offset = 100
            crossings = 0
            if dist >= offset:
                crossings = 1 + (dist - offset) // 100
            start -= dist
        else:
            # distance to next multiple of 100
            rem = start % 100
            offset = (100 - rem) if rem != 0 else 100
            crossings = 0
            if dist >= offset:
                crossings = 1 + (dist - offset) // 100
            start += dist
        count += crossings
    return count


def main():
    text = INPUT_PATH.read_text().rstrip("\n")
    data = parse_input(text)

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
