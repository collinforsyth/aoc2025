from pathlib import Path
from dataclasses import dataclass
from functools import reduce
from itertools import zip_longest



CURR_DIR = Path(__file__).parent
INPUT_PATH = CURR_DIR / "input.txt"


@dataclass(frozen=True, slots=True)
class Problem:
    numbers: list[int]
    op: str


def parse_input(text: str) -> list[Problem]:
    lines = [line.split() for line in text.splitlines() if line.strip()]
    problems: list[Problem] = []
    for i in range(len(lines[0])):
        numbers = [int(row[i]) for row in lines[:-1]]
        op = lines[-1][i]
        problems.append(Problem(numbers, op))
    return problems


def part1(problems: list[Problem]) -> int:
    result = 0
    for problem in problems:
        if problem.op == "*":
            result += reduce(lambda x, y: x * y, problem.numbers)
        else:
            result += sum(problem.numbers)
    return result


def part2(text: str) -> int:
    transposed = list(zip_longest(*text.splitlines(), fillvalue=' '))

    problems : list[Problem] = []
    vals: list[int] = []
    operator: str = ""
    for line in transposed:
        digits : list[str] = []
        for c in line:
            if c.isdigit():
                digits.append(c)
            elif c in '*+':
                operator = c
        if digits:
            n = int(''.join(digits))
            vals.append(n) 
        else:
            problems.append(Problem(vals, operator))
            vals = []
    problems.append(Problem(vals, operator))
    return part1(problems)


def main():
    text = INPUT_PATH.read_text().rstrip("\n")
    input = parse_input(text)

    print("Part 1:", part1(input))
    print("Part 2:", part2(text))


if __name__ == "__main__":
    main()
