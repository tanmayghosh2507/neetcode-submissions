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

        old_dict = {} # val <-> node
        graph_dict = {} # val <-> new node
        # visited = set()

        def create_nodes(node):
            old_dict[node.val] = node
            new_node = Node(node.val)
            graph_dict[node.val] = new_node
            # visited.add(node.val)

            for n in node.neighbors:
                if n.val not in old_dict:
                    create_nodes(n)
        

        create_nodes(node)

        for val, new_node in graph_dict.items():
            old_node = old_dict[val]
            for n in old_node.neighbors:
                new_node.neighbors.append(graph_dict[n.val])
        
        return graph_dict[node.val]
