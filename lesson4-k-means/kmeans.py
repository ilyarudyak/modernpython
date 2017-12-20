from typing import Tuple, Iterable, Sequence, List, Dict, DefaultDict
from random import sample
from math import fsum, sqrt
from collections import defaultdict
from pprint import pprint

Point = Tuple[float, ...]
Centroid = Point


def mean(data: Iterable[float]) -> float:
    """Accurate arithmetic mean"""
    data = list(data)
    return fsum(data) / len(data)


def dist(p: Point, q: Point, sqrt=sqrt, fsum=fsum, zip=zip) -> float:
    """Multi-dimensional euclidean distance"""
    return sqrt(fsum((x1 - x2) ** 2.0 for x1, x2 in zip(p, q)))


def partial(func, *args):
    """Rewrite functools.partial() in a way that doesn't confuse mypy"""
    def inner(*moreargs):
        return func(*args, *moreargs)
    return inner


def assign_data(centroids: Sequence[Centroid], data: Iterable[Point]) -> Dict[Centroid, Sequence[Point]]:
    """Assign data to the closest centroid"""
    d: DefaultDict[Centroid, Sequence[Point]] = defaultdict(list)
    for point in data:
        centroid = min(centroids, key=partial(dist, point))
        d[centroid].append(point)
    return dict(d)


def transpose(matrix: Iterable[Iterable]) -> Iterable[tuple]:
    """Swap rows with columns for a 2-D array"""
    return zip(*matrix)


def compute_centroids(groups: Iterable[Sequence[Point]]) -> List[Centroid]:
    """Compute the centroid of each group"""
    return [tuple(map(mean, transpose(group))) for group in groups]


if __name__ == '__main__':
    points = [
        (10, 41, 23),
        (22, 30, 29),
        (11, 42, 5),
        (20, 32, 4),
        (12, 40, 12),
        (21, 36, 23),
    ]

    centroids = [(9, 39, 20), (12, 36, 25)]
    pprint(assign_data(centroids, points))
