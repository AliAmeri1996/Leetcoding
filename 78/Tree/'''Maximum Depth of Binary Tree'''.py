'''Maximum Depth of Binary Tree'''
#val: this is the value of the node, zero means if you dont provide a value, itll be zero

#self.left:A reference (pointer) to the node’s left child.If the node has no left child, this will be None

#self.right: A reference (pointer) to the node’s right child.If the node has no right child, this will also be None.
'''these are the attribute of the class TreeNode'''



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:  #root is an object of class TreeNode which means it gets all the attribute of that class
        if not root: #This is the base case of the recursion — the foundation of the counting process.
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
# whenever you count the number of nodes, add +1

    

#self.maxDepth(root.left)...It recursively computes the maximum depth (number of nodes) in the subtree that starts at root.left
'''Why this results in a count of nodes: Because every recursive call adds exactly one for its current node, and stops when it reaches None.'''


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.maxDepth(root))
