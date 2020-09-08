from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        if not root:
            return results
        
        dfs(root, 0, True, results)
        
        return results

def dfs(root, level, leftToRight, results):
    if not root:
        return
    
    # if new level is not created yet, create it
    if len(results) - 1 < level:
        results.append([])
    
    dfs(root.left, level + 1, not leftToRight, results)
    
    # print(root.val, " : ", level)
    if leftToRight:
        results[level].append(root.val)
    else:
        results[level].insert(0, root.val)
    
    dfs(root.right, level + 1, not leftToRight, results)


s = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

assert s.zigzagLevelOrder(root) == [
  [3],
  [20,9],
  [15,7]
]
