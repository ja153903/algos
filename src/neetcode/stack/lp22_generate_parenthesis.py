from collections import deque, namedtuple

Node = namedtuple("Node", ["path", "left", "right"])


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        queue = deque()
        queue.append(Node("(", n - 1, n))

        while queue:
            front = queue.popleft()

            if front.left == 0 and front.right == 0:
                result.append(front.path)
            else:
                if front.left > 0:
                    queue.append(Node(f"{front.path}(", front.left - 1, front.right))

                if front.right > front.left:
                    queue.append(Node(f"{front.path})", front.left, front.right - 1))

        return result
