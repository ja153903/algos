class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            match ch:
                case "(":
                    stack.append(")")
                case "[":
                    stack.append("]")
                case "{":
                    stack.append("}")
                case _:
                    if len(stack) == 0 or stack.pop() != ch:
                        return False

        return len(stack) == 0
