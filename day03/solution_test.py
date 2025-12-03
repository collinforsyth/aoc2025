from .solution import parse_input, part1, part2


EXAMPLE_INPUT = """\
987654321111111
811111111111119
234234234234278
818181911112111
"""


def test_part1_example():
    data = parse_input(EXAMPLE_INPUT)
    assert part1(data) == 357


def test_part2_example():
    data = parse_input(EXAMPLE_INPUT)
    assert part2(data) == 3121910778619