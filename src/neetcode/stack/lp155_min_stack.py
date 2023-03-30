from collections import namedtuple

MinStackNode = namedtuple("MinStackNode", ["value", "minimum"])


class MinStack:
    def __init__(self):
        self.stack: list[MinStackNode] = []

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append(MinStackNode(value, value))
        else:
            current_min = self.getMin()
            self.stack.append(MinStackNode(value, min(value, current_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.last.value

    def getMin(self) -> int:
        return self.last.minimum

    @property
    def last(self) -> MinStackNode:
        return self.stack[-1]
