'''
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 1
        ans = []
        
        stack = [root]
        while stack:
            level = []
            while stack:
                node = stack.pop()
                if node:
                    if not node.left and not node.right:
                        ans.append(depth)
                    level += node.left, node.right
            stack = level[::-1]
            depth += 1
        print(ans)
        return min(ans)
        
#DFS
class Solution:
    def minDepth(self, root: 'TreeNode') -> 'int':
        if root is None:
            return 0
        
        if root.left is None:
            return self.minDepth(root.right) +1
        if root.right is None:
            return self.minDepth(root.left) +1
            
        return min(self.minDepth(root.left), self.minDepth(root.right)) +1
