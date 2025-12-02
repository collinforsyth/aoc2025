from .solution import parse_input, part1, part2


EXAMPLE_INPUT = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def test_part1_example():
    data = parse_input(EXAMPLE_INPUT)
    assert part1(data) == 3


def test_part2_example():
    data = parse_input(EXAMPLE_INPUT)
    assert part2(data) == 6