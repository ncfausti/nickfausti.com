class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)
    
# iterative inorder
def iter_inorder(root):
    if not(root):
        return []

    stack = []
    results = []
    current = root

    while True:
        # if current is not None, push it to stack
        # and traverse left
        if current:
            stack.append(current)
            current = current.left
        
        # if current is None, but stack not empty, 
        # check for items in stack, use it, and traverse right
        elif stack:
            current = stack.pop()
            # do something with current here, 
            # i.e. print, add to results, yield, etc.
            results.append(current.val)

            # go down the right next
            current = current.right
        else:
            break
    
    return results

if __name__ == "__main__": 
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5

    results = []

    assert iter_inorder(n1) == [4, 2, 5, 1, 3]

    assert iter_inorder(None) == []

