from pathlib import Path
from collections import deque

CURR_DIR = Path(__file__).parent
INPUT_PATH = CURR_DIR / "input.txt"


def parse_input(text: str) -> dict[str, set[str]]:
    parts = [line.split(":") for line in text.splitlines()]
    d: dict[str, set[str]] = {}
    for p in parts:
        vals = {n for n in p[1].strip().split()}
        d[p[0]] = vals
    return d


def part1(nodes: dict[str, set[str]]) -> int:
    sorted = topological_sort(nodes)
    return count_paths(nodes, sorted, "you", "out")


def count_paths(
    nodes: dict[str, set[str]], sorted: list[str], start: str, end: str
) -> int:
    counts = {key: 0 for key in sorted}
    counts[start] = 1
    for n in sorted:
        if n not in nodes:
            continue
        for neighbor in nodes[n]:
            counts[neighbor] += counts[n]
    return counts[end]

def count_paths_with_ignores(
    nodes: dict[str, set[str]],
    sorted: list[str],
    start: str,
    end: str,
    a: str,
    b: str,
) -> int:
    counts: dict[str, list[int]] = {
        node: [0, 0, 0, 0] for node in sorted
    }

    # state indexes:
    # 0 == not a or b
    # 1 == a
    # 2 == b
    # 3 == both
    start_state = 0
    if start == a:
        start_state |= 1  # saw a
    if start == b:
        start_state |= 2  # saw b

    counts[start][start_state] = 1

    # propagate in topological order
    for n in sorted:
        if n not in nodes:
            continue

        for state in range(4):
            paths_to_here = counts[n][state]
            if paths_to_here == 0:
                continue

            for neighbor in nodes[n]:
                new_state = state
                if neighbor == a:
                    new_state |= 1
                if neighbor == b:
                    new_state |= 2

                counts[neighbor][new_state] += paths_to_here

    return counts[end][3]

def topological_sort(nodes: dict[str, set[str]]) -> list[str]:
    all_nodes = set(nodes.keys())
    for neighbors in nodes.values():
        all_nodes.update(neighbors)

    indegree = {node: 0 for node in all_nodes}
    adj = {node: nodes.get(node, set()) for node in all_nodes}

    # compute indegree: the count of edges pointing into a specific node
    for node in adj:
        for next_node in adj[node]:
            indegree[next_node] += 1

    res: list[str] = []
    queue: deque[str] = deque()
    [queue.append(node) for node in all_nodes if indegree[node] == 0]

    # kahn's algorithm
    while queue:
        top = queue.popleft()
        res.append(top)
        for next_node in adj[top]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)

    return res


def part2(nodes: dict[str, set[str]]) -> int:
    sorted = topological_sort(nodes)
    return count_paths_with_ignores(nodes, sorted, 'svr', 'out', 'dac', 'fft')


def main():
    text = INPUT_PATH.read_text().rstrip("\n")
    input = parse_input(text)

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
