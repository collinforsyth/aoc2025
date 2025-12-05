from .solution import parse_input, part1, part2


EXAMPLE_INPUT = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


def test_part1_example():
    data = parse_input(EXAMPLE_INPUT)
    assert part1(data[0], data[1]) == 3


def test_part2_example():
    data = parse_input(EXAMPLE_INPUT)
    print(data[0])
    assert part2(data[0]) == 14