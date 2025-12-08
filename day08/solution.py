from pathlib import Path
from dataclasses import dataclass
from typing import Iterator
import math
import heapq

CURR_DIR = Path(__file__).parent
INPUT_PATH = CURR_DIR / "input.txt"


@dataclass(frozen=True, slots=True, order=True)
class Point:
    x: int
    y: int
    z: int

    def __iter__(self) -> Iterator[int]:
        return iter((self.x, self.y, self.z))


def parse_input(text: str) -> list[Point]:
    vals = [line.split(",") for line in text.splitlines() if text.strip()]
    points = [Point(int(v[0]), int(v[1]), int(v[2])) for v in vals]
    return points


def part1(data: list[Point], k: int) -> int:
    connections: set[tuple[Point, Point]] = set()
    smallest = k_smallest(data, connections, k)
    for c in smallest:
        connections.add((c[0], c[1]))

    circuits = find_circuits(connections)
    circuits.sort(key=lambda c: len(c), reverse=True)
    result = 1
    for i in range(3):
        result *= len(circuits[i])
    return result


def k_smallest(
    data: list[Point], seen: set[tuple[Point, Point]], k : int,
) -> list[tuple[Point, Point, float]]:
    distances : list[tuple[float, Point, Point]] = []
    
    # generate all values first
    # Q: can we use a streaming approach with heapq here?
    for i in range(len(data)):
        for j in range(i + 1, len(data)): 
            p1, p2 = data[i], data[j]
            
            # normalize ordering for the seen check
            t = (p1, p2) if p1 <= p2 else (p2, p1)
            
            if t in seen:
                continue
                
            dist = math.dist(p1, p2)
            # store with normalized ordering
            distances.append((dist, t[0], t[1]))
    
    # grab top K
    k_smallest : list[tuple[float, Point, Point]] = heapq.nsmallest(k, distances, key=lambda x: x[0])
    
    return [(p1, p2, dist) for dist, p1, p2 in k_smallest]


def find_circuits(connections: set[tuple[Point, Point]]) -> list[set[Point]]:
    if not connections:
        return []

    graph: dict[Point, set[Point]] = {}
    for p1, p2 in connections:
        graph.setdefault(p1, set()).add(p2)
        graph.setdefault(p2, set()).add(p1)

    visited: set[Point] = set()
    circuits: list[set[Point]] = []

    def dfs(point: Point, circuit: set[Point]):
        visited.add(point)
        circuit.add(point)
        for neighbor in graph.get(point, []):
            if neighbor not in visited:
                dfs(neighbor, circuit)

    for point in graph:
        if point not in visited:
            circuit: set[Point] = set()
            dfs(point, circuit)
            circuits.append(circuit)

    return circuits


def part2() -> int:
    return 0


def main():
    text = INPUT_PATH.read_text().rstrip("\n")
    input = parse_input(text)

    print("Part 1:", part1(input, 1000))
    print("Part 2:", part2())


if __name__ == "__main__":
    main()
