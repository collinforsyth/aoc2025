from pathlib import Path
from dataclasses import dataclass
import re
from collections import deque
import z3

CURR_DIR = Path(__file__).parent
INPUT_PATH = CURR_DIR / "input.txt"


@dataclass(frozen=True, slots=True)
class Machine:
    indicators: str
    schematic: list[list[int]]
    joltages: list[int]


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
            machines.append(Machine(match.group(1), schematics, joltages))
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


# note: after trying several ways of pruning the input space,
# there wasn't an obvious solution besides an optimizer.
# todo: come back and remove any dependencies if there is a good solution.
def part2(machines: list[Machine]) -> int:
    result = 0
    for machine in machines:
        buttons = machine.schematic
        target = machine.joltages
        num_buttons = len(buttons)
        num_counters = len(target)
        solver = z3.Optimize()

        # each button is a variable
        button_presses = [z3.Int(f"press_{j}") for j in range(num_buttons)]
        for j in range(num_buttons):
            # needs to be nonnegatives, not a normal system of linear equations
            solver.add(button_presses[j] >= 0)

        # for each counter i, create a vector that says the sum of these
        # vectors must equal the target value
        for i in range(num_counters):
            vectors = [button_presses[j] for j in range(num_buttons) if i in buttons[j]]
            solver.add(z3.Sum(vectors) == target[i])
        total_presses = z3.Sum(button_presses)

        # setting objective to be minimize total_presses
        solver.minimize(total_presses)

        # produce optimal values -> assuming we can solve all of these
        solver.check()

        model = solver.model()
        min_presses = model.eval(total_presses).as_long()
        result += min_presses
    return result


def main():
    text = INPUT_PATH.read_text().rstrip("\n")
    input = parse_input(text)

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
