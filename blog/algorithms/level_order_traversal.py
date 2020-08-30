from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def level_order( root ):
    q = deque()
    q.append(root)
    seen = set()
    results = []
    level = 0
    
    while q:
        current = q.popleft()
        
        if current.left and current.left not in seen:
            seen.add(current.left)
            q.append(current.left)
        if current.right and current.right not in seen:
            seen.add(current.right)
            q.append(current.right)
        
        results.append(current.data)
    
    return results

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


assert level_order(root) == [1,2,3,4,5]