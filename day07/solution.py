from pathlib import Path

CURR_DIR = Path(__file__).parent
INPUT_PATH = CURR_DIR / "input.txt"


def parse_input(text: str) -> list[str]:
    return [line for line in text.splitlines() if text.strip()]


def part1(data: list[str]) -> int:
    beams = ["" for _ in range(len(data[0]))]
    result = 0
    # start the beam
    for i, c in enumerate(data[0]):
        if c == "S":
            beams[i] = "|"
    for line in data[1:]:
        for i, c in enumerate(line):
            if c == "^" and beams[i] == "|":
                # split!
                result += 1
                beams[i - 1], beams[i], beams[i + 1] = "|", ".", "|"

    return result


def part2(data: list[str]) -> int:
    num_rows = len(data)
    num_cols = len(data[0])
    dp = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

    for i, c in enumerate(data[0]):
        if c == "S":
            dp[0][i] = 1
    for row in range(num_rows - 1):
        for col in range(num_cols):
            if dp[row][col] > 0:
                if data[row][col] == "^":
                    # split paths, and handle additional paths that can reach this
                    dp[row + 1][col - 1] += dp[row][col]
                    dp[row + 1][col + 1] += dp[row][col]
                else:
                    # path is directly below
                    dp[row + 1][col] += dp[row][col]
    return sum(dp[-1])


def main():
    text = INPUT_PATH.read_text().rstrip("\n")
    input = parse_input(text)

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
