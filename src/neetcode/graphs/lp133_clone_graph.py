from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: "Node" | None) -> "Node" | None:
        if not node:
            return None

        queue = deque()
        copies = {}
        seen = set()

        queue.append(node)
        seen.add(node.val)
        copies[node.val] = Node(node.val)

        while queue:
            front = queue.popleft()

            for neighbor in front.neighbors:
                if neighbor.val not in seen:
                    seen.add(neighbor.val)
                    copies[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)

                copies[front.val].neighbors.append(copies[neighbor.val])

        return copies[node.val]
