from typing import List

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Node:
        
        # Start with root of tree (preorder[0])
        return self.traverse(0, 0, len(inorder) - 1, preorder, inorder)
    
    # preStart: INDEX of ROOT NODE on each recursive call
    # inStart, inEnd: boundaries of INORDER list
    
    
    # (int, int, int, list, list) -> Node
    def traverse(self, preStart, inStart, inEnd, preOrder, inOrder):
        # bounds check for both lists
        if (preStart > len(preOrder) - 1 or inStart > inEnd):
            return None
        
        # before returning the root, set the left and right nodes
        root = Node(preOrder[preStart])
        
        rootIndexInorder = inOrder.index(root.val)
        
        # preStart + 1, bc n L r; for a given root index, in preorder array, it's left
        # node is +1, it's right node is + 2 [node, LEFT, right] and [node, left, RIGHT]
        root.left = self.traverse(preStart + 1, 
                                  inStart, rootIndexInorder - 1, preOrder, inOrder)
        
        # skip all left subtrees to get immediate right child, rootIndexInorder + inStart
        root.right = self.traverse(preStart + rootIndexInorder - inStart + 1, 
                                   rootIndexInorder + 1, inEnd, preOrder, inOrder)
        
        return root
        
root = Node(3, 
    Node(9), Node(20, Node(15), Node(7))
    )
s = Solution()

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

results = []
def inOrd(root):
    if not root:
        return
    inOrd(root.left)
    results.append(root.val)
    inOrd(root.right)
    return results

assert inOrd(s.buildTree(preorder, inorder)) == inorder