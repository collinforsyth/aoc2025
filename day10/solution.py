from pathlib import Path
from dataclasses import dataclass
import re
from collections import deque

CURR_DIR = Path(__file__).parent
INPUT_PATH = CURR_DIR / "input.txt"


@dataclass(frozen=True, slots=True)
class Machine:
    indicators: str
    schematic: list[list[int]]
    joltages: tuple[int, ...]


def parse_input(text: str) -> list[Machine]:
    machines: list[Machine] = []
    for line in text.splitlines():
        pattern = r"\[(.*?)\](.*)\{(.*?)\}"
        match = re.match(pattern, line)
        if match:
            joltages = [int(v) for v in match.group(3).split(",")]
            schematic_group = re.findall(r"\(([^)]+)\)", line)
            schematics = [
                [int(x) for x in group.split(",")] for group in schematic_group
            ]
            machines.append(Machine(match.group(1), schematics, tuple(joltages)))
    return machines


def part1(machines: list[Machine]) -> int:
    fewest_buttons = 0
    for machine in machines:
        initial_state = "." * len(machine.indicators)
        visited: dict[str, int] = {}
        queue: deque[str] = deque()

        queue.append(initial_state)
        visited[initial_state] = 0
        found = False
        while queue and not found:
            state = queue.popleft()
            for transition in machine.schematic:
                s = []
                for i, c in enumerate(state):
                    if i in transition:
                        if c == ".":
                            s.append("#")
                        else:
                            s.append(".")
                    else:
                        s.append(c)
                new_state = "".join(s)
                if new_state == machine.indicators:
                    fewest_buttons += visited[state] + 1
                    found = True
                    break
                if new_state not in visited:
                    visited[new_state] = visited[state] + 1
                    queue.append(new_state)
    return fewest_buttons


def part2(machines: list[Machine]) -> int:
    return 0


def main():
    text = INPUT_PATH.read_text().rstrip("\n")
    input = parse_input(text)

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
