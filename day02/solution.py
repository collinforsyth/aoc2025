# aoc2025/day1/solution.py
from pathlib import Path
from typing import List, Dict

CURR_DIR = Path(__file__).parent
INPUT_PATH = CURR_DIR / "input.txt"


def parse_input(text: str) -> List[str]:
    return [line.strip() for line in text.split(",") if line.strip()]


def part1(data: List[str]) -> int:
    invalid = 0
    for rng in data:
        low, high = rng.split("-")
        for val in range(int(low), int(high)+1):
            s = str(val)
            t = len(s) // 2
            if s[:t] == s[t:]:
                invalid += val
    return invalid


def part2(data: str) -> int:
    count = 0
    for rng in data:
        low, high = map(int, rng.split("-"))
        for val in range(low, high + 1):
            s = str(val)
            l = len(s)
            # block lengths, 1, 2, 3, ... , len(s) // (2 + 1)
            for i in range(1, l // 2 + 1):
                # can ignore sequences that don't modulo into block
                if l % i != 0:
                    continue
                blk = s[:i]  # block to check for repeats
                # construct string and check equality
                if blk * (l // i) == s:
                    count += val
                    break
    return count


def main():
    text = INPUT_PATH.read_text().rstrip("\n")
    data = parse_input(text)

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
