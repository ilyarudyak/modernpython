from typing import *
from collections import OrderedDict, deque


def f(x: int, y: int) -> int:
    return x + y


def g(x: Sequence[int]) -> None:
    print(len(x))


if __name__ == '__main__':
    x = 10  # type: int
    y: int = 20

    print(f'x={x} y={y}')

    print(f(10, 20))
    # print(f(10, 'hello'))

    # z = {}  # type: OrderedDict
    # z: OrderedDict = {}
    z: OrderedDict = OrderedDict()

    g([10, 20, 30])
    # g('abcdef')

    fifo = deque()  # type: Deque[int]
    fifo.append(10)
    # fifo.append('hello')

    print(f'the answer is {x} today')
