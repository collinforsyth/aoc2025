from .solution import parse_input, part1, part2


EXAMPLE_INPUT = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

def test_part1_example():
    data = parse_input(EXAMPLE_INPUT)
    assert part1(data) == 50


def test_part2_example():
    data = parse_input(EXAMPLE_INPUT)
    assert part2(data) == 24