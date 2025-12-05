from pathlib import Path
from typing import List
from dataclasses import dataclass

CURR_DIR = Path(__file__).parent
INPUT_PATH = CURR_DIR / "input.txt"


@dataclass(frozen=True, slots=True)
class Range:
    low: int
    high: int


def parse_input(text: str) -> tuple[List[Range], List[int]]:
    parts = text.split('\n\n', 1)
    ranges = [Range(int(p[0]), int(p[1])) for line in parts[0].split() for p in [line.split('-')]]
    ingredients = [int(line) for line in parts[1].split()]
    return ranges, ingredients

def part1(freshness_ranges: List[Range], ingredients: List[int]) -> int:
    fresh_count = 0
    for ingredient in ingredients:
        for range in freshness_ranges:
            if range.low <= ingredient <= range.high:
                fresh_count+=1
                break
    return fresh_count


def part2(freshness_ranges: List[Range]) -> int:
    # merging intervals problem
    freshness_ranges.sort(key=lambda r: r.low)
    merged : List[Range] = []
    for i, curr in enumerate(freshness_ranges):
        low, high = curr.low, curr.high
        if merged and merged[-1].high >= curr.high:
            # current already contained
            continue
        # else find end of merged array
        for j in range(i+1, len(freshness_ranges)):
            if freshness_ranges[j].low <= high:
                high = max(freshness_ranges[j].high, high)
        merged.append(Range(low, high))

    return sum((r.high - r.low) + 1 for r in merged)


def main():
    text = INPUT_PATH.read_text().rstrip("\n")
    data = parse_input(text)

    print("Part 1:", part1(data[0], data[1]))
    print("Part 2:", part2(data[0]))


if __name__ == "__main__":
    main()
