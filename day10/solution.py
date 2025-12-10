from pathlib import Path
from dataclasses import dataclass
import re

CURR_DIR = Path(__file__).parent
INPUT_PATH = CURR_DIR / "input.txt"


@dataclass(frozen=True, slots=True)
class Machine:
    indicators: str
    schematic: list[list[int]]
    joltages: list[int]


def parse_input(text: str) -> list[Machine]:
    machines : list[Machine] = []
    for line in text.splitlines():
        pattern = r'\[(.*?)\](.*)\{(.*?)\}'
        match = re.match(pattern, line)
        if match:
            joltages = [int(v) for v in match.group(3).split(',')]
            schematic_group = re.findall(r'\(([^)]+)\)', line)
            schematics = [[int(x) for x in group.split(',')] for group in schematic_group]
            machines.append(Machine(match.group(1), schematics, joltages))
    return machines


def part1(machines: list[Machine]) -> int:
    for machine in machines:
        initial_state = ['.' * len(machine.indicators)]
        print(initial_state)
        print(machine)
    return 0


def part2(input: list[Machine]) -> int:
    return 0


def main():
    text = INPUT_PATH.read_text().rstrip("\n")
    input = parse_input(text)

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
