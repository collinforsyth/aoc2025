from pathlib import Path
from typing import List

CURR_DIR = Path(__file__).parent
INPUT_PATH = CURR_DIR / "input.txt"


def parse_input(text: str):
    return [line.strip() for line in text.splitlines() if line.strip()]


def part1(data: List[str]) -> int:
    result = 0
    for line in data:
        first, idx = 0, 0
        for i, c in enumerate(line[:-1]):
            val = int(c)
            if first < val:
                first, idx = val, i
        second = 0
        for v in line[idx + 1 :]:
            second = max(second, int(v))
        result += (first * 10) + second
    return result


def part2(data: str) -> int:
    result = 0
    for line in data:
        max_voltage: List[int] = []
        i = 0
        while len(max_voltage) < 12:
            j = i
            k = len(line) - 11 + len(max_voltage)
            curr_max = 0
            while j < k:
                curr_val = int(line[j])
                if curr_max < curr_val:
                    curr_max = curr_val
                    i = j
                j += 1
            max_voltage.append(curr_max)
            i += 1
        result += int("".join(map(str, max_voltage)))
    return result


def main():
    text = INPUT_PATH.read_text().rstrip("\n")
    data = parse_input(text)

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))


if __name__ == "__main__":
    main()
