import math


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token in ("+", "-", "*", "/"):
                b, a = stack.pop(), stack.pop()
                stack.append(self.eval(a, b, token))
            else:
                stack.append(int(token))

        return stack.pop()

    def eval(self, a: int, b: int, op: str) -> int:
        match op:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b
            case _:
                return math.trunc(a / b)
