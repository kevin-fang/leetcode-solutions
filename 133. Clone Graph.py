"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def helper(self, node, visited):
        new_node = Node(node.val, neighbors = []);
        visited[node.val] = new_node
            
        for neighbor in node.neighbors:
            if neighbor.val not in visited:
                neighbor_node = self.helper(neighbor, visited)
                new_node.neighbors.append(neighbor_node)
            else:
                new_node.neighbors.append(visited[neighbor.val])
                
        return new_node
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visited = {}
        new_node = self.helper(node, visited);
        return new_node
