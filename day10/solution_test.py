from .solution import parse_input, part1, part2


EXAMPLE_INPUT = """\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

def test_part1_example():
    data = parse_input(EXAMPLE_INPUT)
    assert part1(data) == 50


def test_part2_example():
    data = parse_input(EXAMPLE_INPUT)
    assert part2(data) == 24