from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


MOVE = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]


def walk(maze: list[str], cur: Point, end: Point, path: list[Point], seen: list[list[int]]) -> bool:
    print(cur)

    if cur.x > len(maze[0]) or cur.x < 0 or cur.y > len(maze) or cur.y < 0:
        return False

    if maze[cur.y][cur.x] == "#":
        return False

    if cur == end:
        path.append(end)
        return True

    if seen[cur.y][cur.x]:
        return False

    seen[cur.y][cur.x] = True
    path.append(cur)

    for m in MOVE:
        x = cur.x + m[1]
        y = cur.y + m[0]
        if walk(maze, Point(x, y), end, path, seen):
            return True

    path.pop()
    return False


def find_path(maze: list[str], start: Point, end: Point) -> list[Point]:
    path: list[Point] = []
    seen = [[False] * len(maze[0]) for _ in range(len(maze))]
    walk(maze, start, end, path, seen)
    return path


def main():
    maze = [
        "####### #",
        "####### #",
        "####### #",
        "#       #",
        "# #######"
    ]
    path = find_path(maze, Point(7, 0), Point(1, 4))
    assert path == [
        Point(7, 0),
        Point(7, 1),
        Point(7, 2),
        Point(7, 3),
        Point(6, 3),
        Point(5, 3),
        Point(4, 3),
        Point(3, 3),
        Point(2, 3),
        Point(1, 3),
        Point(1, 4),
    ]


if __name__ == '__main__':
    main()
