"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        visited = {}
        def clone(node):
            if node in visited:
                return visited[node]
            cloned_node = Node(node.val)
            visited[node] = cloned_node
            for neighbor in node.neighbors:
                cloned_node.neighbors.append(clone(neighbor))

            return cloned_node
        return clone(node)

