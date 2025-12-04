from .solution import parse_input, part1, part2


EXAMPLE_INPUT = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


def test_part1_example():
    data = parse_input(EXAMPLE_INPUT)
    assert part1(data) == 13


def test_part2_example():
    data = parse_input(EXAMPLE_INPUT)
    assert part2(data) == 43