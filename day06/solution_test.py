from .solution import parse_input, part1, part2


EXAMPLE_INPUT = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

def test_part1_example():
    data = parse_input(EXAMPLE_INPUT)
    assert part1(data) == 4277556


def test_part2_example():
    assert part2(EXAMPLE_INPUT) == 3263827