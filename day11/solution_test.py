from .solution import parse_input, part1, part2


EXAMPLE_INPUT = """\
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

EXAMPLE_INPUT_PART_2 = """\
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""


def test_part1_example():
    input = parse_input(EXAMPLE_INPUT)
    assert part1(input) == 5


def test_part2_example():
    input = parse_input(EXAMPLE_INPUT_PART_2)
    assert part2(input) == 2
